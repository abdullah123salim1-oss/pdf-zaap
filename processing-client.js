import { LIBRARIES, LIMITS, boundedCanvasSize, createProcessor, validateFiles, validatePageCount, yieldToEventLoop } from './processing-core.js';
export { LIMITS, validateFiles } from './processing-core.js';

const libraryPromises = new Map();
export async function loadLibrary(name) {
  const library = LIBRARIES[name];
  const existing = globalThis[library.global] || globalThis[library.alias];
  if (existing) return existing;
  if (!libraryPromises.has(name)) {
    libraryPromises.set(name, new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = library.url;
      script.onload = () => {
        const value = globalThis[library.global] || globalThis[library.alias];
        if (value) resolve(value);
        else reject(new Error('A conversion library could not be initialized. Please refresh and try again.'));
      };
      script.onerror = () => {
        script.remove();
        reject(new Error('A conversion library could not be downloaded. Check your connection and try again.'));
      };
      document.head.appendChild(script);
    }).catch(error => {
      libraryPromises.delete(name);
      throw error;
    }));
  }
  return libraryPromises.get(name);
}

function checkCancelled(signal) {
  if (signal?.aborted) throw new DOMException('Processing cancelled.', 'AbortError');
}

function awaitLibrary(name, signal) {
  const promise = loadLibrary(name);
  if (!signal) return promise;
  // Do not leave the UI locked if a CDN stalls. The shared code download can
  // finish/cache in the background, but it never owns any document bytes.
  return new Promise((resolve, reject) => {
    const abort = () => reject(new DOMException('Processing cancelled.', 'AbortError'));
    signal.addEventListener('abort', abort, { once: true });
    promise.then(value => {
      signal.removeEventListener('abort', abort);
      resolve(value);
    }, error => {
      signal.removeEventListener('abort', abort);
      reject(error);
    });
    if (signal.aborted) { signal.removeEventListener('abort', abort); abort(); }
  });
}

// A fresh worker per job releases the libraries, parsed PDFs and output structures together.
// Only bootstrap failures fall back: never repeat expensive work after a job has started.
export async function createEngine({ onProgress = () => {}, signal } = {}) {
  checkCancelled(signal);
  if (typeof Worker !== 'undefined') {
    let worker;
    let close;
    try {
      worker = new Worker(new URL('./processing-worker.js', import.meta.url));
      let nextId = 0;
      const pending = new Map();
      let closed = false;
      let resolveReady, rejectReady;
      const ready = new Promise((resolve, reject) => { resolveReady = resolve; rejectReady = reject; });
      const timer = setTimeout(() => close(new Error('The background worker could not start.')), 10_000);
      const abort = () => close(new DOMException('Processing cancelled.', 'AbortError'));
      close = (error = new Error('Processing worker closed.')) => {
        if (closed) return;
        closed = true;
        clearTimeout(timer);
        signal?.removeEventListener('abort', abort);
        worker.terminate();
        rejectReady(error);
        for (const request of pending.values()) request.reject(error);
        pending.clear();
      };
      signal?.addEventListener('abort', abort, { once: true });
      worker.onmessage = ({ data }) => {
        if (closed) return;
        if (data.type === 'ready') { clearTimeout(timer); resolveReady(); }
        else if (data.type === 'startup-error') close(new Error(data.message));
        else if (data.type === 'progress') onProgress(data.percent, data.text);
        else {
          const request = pending.get(data.id);
          if (!request) return;
          pending.delete(data.id);
          if (data.type === 'error') request.reject(new Error(data.message));
          else request.resolve(data.result);
        }
      };
      worker.onerror = event => { event.preventDefault(); close(new Error(event.message || 'Background processing failed.')); };
      worker.onmessageerror = () => close(new Error('The background worker returned an unreadable response.'));
      await ready;
      checkCancelled(signal);
      return {
        mode: 'worker',
        call(command, payload, transfer = []) {
          checkCancelled(signal);
          if (closed) return Promise.reject(new Error('The background worker is no longer available. Please retry.'));
          const id = ++nextId;
          return new Promise((resolve, reject) => {
            pending.set(id, { resolve, reject });
            try { worker.postMessage({ id, command, payload }, transfer); }
            catch (error) { pending.delete(id); reject(error); }
          });
        },
        close
      };
    } catch (error) {
      close?.(error);
      worker?.terminate();
      checkCancelled(signal);
      onProgress(5, 'Background worker unavailable; using browser-compatible processing...');
    }
  }
  const processor = createProcessor({ loadLibrary: name => awaitLibrary(name, signal), onProgress, checkCancelled: () => checkCancelled(signal) });
  return { mode: 'cooperative', call: (command, payload) => processor.handle(command, payload), close: () => processor.dispose() };
}

async function withPDF(file, signal, usePDF, useWorker) {
  const pdfjs = await awaitLibrary('pdfjs', signal);
  checkCancelled(signal);
  const workerURL = new URL('./pdfjs-worker.js', import.meta.url).href;
  if (useWorker === undefined) {
    // Text-only jobs have no output worker to establish availability. Probe
    // before reading the input, including environments that block construction.
    useWorker = false;
    if (typeof Worker !== 'undefined') {
      try {
        const probe = new Worker(workerURL);
        probe.terminate();
        useWorker = true;
      } catch { /* Use PDF.js's cooperative fallback below. */ }
    }
  }
  // PDF.js's fake-worker fallback loads workerSrc as a DOM script. In that
  // mode use the vendor bundle, not our importScripts-only worker entry.
  pdfjs.GlobalWorkerOptions.workerSrc = useWorker
    ? workerURL
    : LIBRARIES.pdfjs.url.replace('/pdf.min.js', '/pdf.worker.min.js');
  const task = pdfjs.getDocument({
    data: new Uint8Array(await file.arrayBuffer()),
    isEvalSupported: false,
    canvasMaxAreaInBytes: LIMITS.maxCanvasPixels * 4
  });
  let destruction;
  const destroy = () => destruction ||= task.destroy();
  const abort = () => { destroy().catch(() => {}); };
  signal?.addEventListener('abort', abort, { once: true });
  try {
    checkCancelled(signal);
    const pdf = await task.promise;
    checkCancelled(signal);
    return await usePDF(pdf);
  } finally {
    signal?.removeEventListener('abort', abort);
    await destroy();
  }
}

export function canvasToBlob(canvas, type = 'image/jpeg', quality = 0.85) {
  return new Promise((resolve, reject) => {
    canvas.toBlob(blob => blob ? resolve(blob) : reject(new Error('The page could not be encoded. Try a smaller document.')), type, quality);
  });
}

async function grayscaleCanvas(canvas, engine) {
  const context = canvas.getContext('2d');
  const image = context.getImageData(0, 0, canvas.width, canvas.height);
  const { pixels } = await engine.call('grayscale', { pixels: image.data.buffer }, [image.data.buffer]);
  context.putImageData(new ImageData(new Uint8ClampedArray(pixels), canvas.width, canvas.height), 0, 0);
}

async function renderPDF(tool, file, options, engine, onProgress, signal) {
  const png = tool === 'pdf-to-png';
  const imageExport = tool === 'pdf-to-jpg' || png;
  const filename = tool === 'pdf-to-powerpoint' ? file.name.replace(/\.pdf$/i, '') + '.pptx'
    : imageExport ? 'extracted_images.zip' : tool === 'grayscale-pdf' ? 'grayscale.pdf' : 'compressed.pdf';
  const canvas = document.createElement('canvas');
  try {
    await withPDF(file, signal, async pdf => {
      validatePageCount(pdf.numPages, true);
      await engine.call('startRaster', { tool, total: pdf.numPages, filename });
      for (let index = 1; index <= pdf.numPages; index++) {
        checkCancelled(signal);
        const page = await pdf.getPage(index);
        try {
          const original = page.getViewport({ scale: 1 });
          const size = boundedCanvasSize(original.width, original.height, imageExport || tool === 'pdf-to-powerpoint' ? 1.5 : 1.25);
          const viewport = page.getViewport({ scale: size.scale });
          canvas.width = size.width;
          canvas.height = size.height;
          const context = canvas.getContext('2d', { willReadFrequently: tool === 'grayscale-pdf' });
          if (!context) throw new Error('Your browser could not allocate a page canvas. Try a smaller document.');
          await page.render({ canvasContext: context, viewport, background: 'rgb(255,255,255)' }).promise;
          checkCancelled(signal);
          if (tool === 'grayscale-pdf') await grayscaleCanvas(canvas, engine);
          const quality = tool === 'compress-pdf' ? Math.min(1, Math.max(0.1, Number(options.quality) || 0.6)) : 0.85;
          const data = await (await canvasToBlob(canvas, png ? 'image/png' : 'image/jpeg', quality)).arrayBuffer();
          // Transfer ownership; never retain a base64 copy of every page on the main thread.
          await engine.call('addRasterPage', { data, width: original.width, height: original.height }, [data]);
        } finally {
          canvas.width = canvas.height = 0;
          page.cleanup();
        }
        onProgress(15 + 70 * index / pdf.numPages, `Processing page ${index}/${pdf.numPages}...`);
        await yieldToEventLoop();
      }
    }, engine.mode === 'worker');
    // The source PDF.js document/worker is destroyed before output serialization starts.
    return await engine.call('finishRaster');
  } finally {
    canvas.width = canvas.height = 0;
  }
}

async function extractText(file, onProgress, signal) {
  const parts = [];
  let length = 0;
  await withPDF(file, signal, async pdf => {
    validatePageCount(pdf.numPages);
    for (let index = 1; index <= pdf.numPages; index++) {
      checkCancelled(signal);
      const page = await pdf.getPage(index);
      try {
        const content = await page.getTextContent();
        const text = `--- Page ${index} ---\n${content.items.map(item => item.str).join(' ')}\n\n`;
        length += text.length;
        if (length * 2 > LIMITS.maxRasterBytes) throw new Error('Extracted text exceeds the safety limit. Use fewer pages.');
        parts.push(text);
      } finally { page.cleanup(); }
      onProgress(20 + 70 * index / pdf.numPages, `Extracting page ${index}/${pdf.numPages}...`);
      await yieldToEventLoop();
    }
  });
  return { data: new Blob(parts, { type: 'text/plain' }), filename: 'extracted_text.txt', type: 'text/plain' };
}

async function wordToPDF(file, onProgress, signal) {
  const html2pdf = await awaitLibrary('html2pdf', signal);
  checkCancelled(signal);
  onProgress(20, 'Reading DOCX components...');
  const engine = await createEngine({ onProgress, signal });
  let html;
  try { ({ html } = await engine.call('wordToHTML', { file })); }
  finally { engine.close(); }
  // Release the DOCX parser/ZIP structures before constructing the DOM/canvas.
  checkCancelled(signal);
  const element = document.createElement('div');
  element.style.padding = '20px';
  element.innerHTML = html;
  html = null;
  const existingClones = new Set(document.querySelectorAll('iframe.html2canvas-container'));
  let renderer;
  try {
    onProgress(45, 'Measuring document layout...');
    await yieldToEventLoop();
    checkCancelled(signal);
    renderer = html2pdf().from(element).set({
      margin: 1,
      image: { type: 'jpeg', quality: 0.85 },
      html2canvas: { scale: 1.25 },
      jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
    });
    await renderer.toContainer();
    const container = await renderer.get('container');
    // Image loading can change the measured height after the DOCX HTML is attached.
    await Promise.all(Array.from(container.querySelectorAll('img'), image => image.decode().catch(() => {})));
    checkCancelled(signal);
    const width = Math.max(container.scrollWidth, container.getBoundingClientRect().width);
    const height = Math.max(container.scrollHeight, container.getBoundingClientRect().height);
    const size = boundedCanvasSize(width, height, 1.25, LIMITS.maxWordCanvasPixels, LIMITS.maxWordCanvasDimension);
    // html2pdf renders one tall DOM canvas, so refuse unsafe lengths rather than crashing.
    if (size.scale < 0.75) throw new Error('This Word document is too long to render safely. Split it into smaller documents first.');
    await renderer.set({ html2canvas: { scale: size.scale } });
    checkCancelled(signal);
    onProgress(65, 'Rendering document pages...');
    await yieldToEventLoop();
    checkCancelled(signal);
    await renderer.toCanvas();
    checkCancelled(signal);
    onProgress(90, 'Exporting PDF...');
    await yieldToEventLoop();
    checkCancelled(signal);
    const data = await renderer.outputPdf('blob');
    checkCancelled(signal);
    return { data, filename: 'converted.pdf', type: 'application/pdf' };
  } finally {
    if (renderer?.prop.canvas) renderer.prop.canvas.width = renderer.prop.canvas.height = 0;
    renderer?.prop.overlay?.remove();
    // html2canvas can leave its cloned-document iframe behind on a render error.
    for (const clone of document.querySelectorAll('iframe.html2canvas-container')) {
      if (!existingClones.has(clone)) clone.remove();
    }
    element.replaceChildren();
  }
}

const rasterTools = new Set(['compress-pdf', 'grayscale-pdf', 'pdf-to-powerpoint', 'pdf-to-jpg', 'pdf-to-png']);
const workerTools = new Set(['merge-pdf', 'split-pdf', 'rotate-pdf', 'jpg-to-pdf', 'png-to-pdf', 'add-watermark-pdf', 'number-pdf-pages', 'delete-pdf-pages', 'extract-pages-pdf', 'reorder-pages-pdf', 'crop-pdf', 'resize-pdf', 'flatten-pdf', 'pdf-metadata-editor', 'repair-pdf', 'unlock-pdf', 'esign-pdf', 'ppt-to-pdf']);

export function supportsTool(tool) {
  return tool === 'word-to-pdf' || tool === 'pdf-to-text' || rasterTools.has(tool) || workerTools.has(tool);
}

export async function runTool(tool, files, options = {}, { onProgress = () => {}, signal } = {}) {
  // File objects are cloned to the worker without first materializing bytes on the UI thread.
  validateFiles(files, tool);
  checkCancelled(signal);
  if (tool === 'word-to-pdf') return wordToPDF(files[0], onProgress, signal);
  if (tool === 'pdf-to-text') return extractText(files[0], onProgress, signal);
  if (!supportsTool(tool)) {
    throw new Error('This tool is not implemented yet. No file has been changed. Please choose another tool.');
  }
  const engine = await createEngine({ onProgress, signal });
  try {
    const result = rasterTools.has(tool)
      ? await renderPDF(tool, files[0], options, engine, onProgress, signal)
      : await engine.call('execute', { tool, files, options });
    checkCancelled(signal);
    return result;
  } finally { engine.close(); }
}

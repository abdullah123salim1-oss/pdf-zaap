// DOM-free processing shared by the dedicated worker and its cooperative fallback.
// Limits bound input and intermediate allocations, not just the final download.
const MiB = 1024 * 1024;
export const LIMITS = Object.freeze({
  maxFileBytes: 100 * MiB,
  maxTotalFileBytes: 200 * MiB,
  maxFiles: 100,
  maxPages: 2000,
  maxRasterPages: 200,
  maxCanvasPixels: 4_000_000,
  maxCanvasDimension: 4096,
  maxRasterBytes: 100 * MiB,
  maxRangeCharacters: 20_000,
  maxRangeParts: 2000,
  pageBatchSize: 10,
  progressIntervalMs: 100,
  maxZipEntries: 10_000,
  maxSlideXmlBytes: 2 * MiB,
  maxPresentationXmlBytes: 32 * MiB,
  maxSlideTextCharacters: 20_000,
  maxWordFileBytes: 20 * MiB,
  maxWordHtmlCharacters: 8_000_000,
  maxWordCanvasPixels: 8_000_000,
  maxWordCanvasDimension: 8192
});

// Match the versions already used by the static site. Loaded only when needed.
export const LIBRARIES = Object.freeze({
  pdfLib: { global: 'PDFLib', url: 'https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js' },
  zip: { global: 'JSZip', url: 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js' },
  pptx: { global: 'pptxgen', alias: 'PptxGenJS', url: 'https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js' },
  pdfjs: { global: 'pdfjsLib', url: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js' },
  mammoth: { global: 'mammoth', url: 'https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js' },
  html2pdf: { global: 'html2pdf', url: 'https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js' }
});

export function validateFiles(files, tool = '') {
  if (!files.length) throw new Error('Please select a file first.');
  if (files.length > LIMITS.maxFiles) throw new Error(`Select at most ${LIMITS.maxFiles} files at a time.`);
  let total = 0;
  for (const file of files) {
    if (!file || !Number.isSafeInteger(file.size) || file.size <= 0) throw new Error('Empty or invalid files cannot be processed.');
    const limit = tool === 'word-to-pdf' ? LIMITS.maxWordFileBytes : LIMITS.maxFileBytes;
    if (file.size > limit) throw new Error(`Each file must be ${limit / MiB} MB or smaller. Split this document before processing.`);
    total += file.size;
  }
  if (total > LIMITS.maxTotalFileBytes) throw new Error(`Selected files must total ${LIMITS.maxTotalFileBytes / MiB} MB or less.`);
}

export function validatePageCount(count, raster = false) {
  const limit = raster ? LIMITS.maxRasterPages : LIMITS.maxPages;
  if (!Number.isSafeInteger(count) || count < 1) throw new Error('The document has no valid pages.');
  if (count > limit) throw new Error(`This operation supports at most ${limit} pages. Split the document into smaller parts first.`);
}

function selectionParts(input) {
  if (typeof input !== 'string' || !input.trim()) throw new Error('Please enter at least one page number (e.g. 1-3, 5).');
  if (input.length > LIMITS.maxRangeCharacters) throw new Error('The page selection is too long. Use shorter ranges.');
  const parts = input.split(',');
  if (parts.length > LIMITS.maxRangeParts) throw new Error('There are too many page selections. Use ranges instead.');
  return parts.map(part => part.trim());
}

function pageNumber(value, maxPages) {
  const number = Number(value);
  if (!Number.isSafeInteger(number) || number < 1 || number > maxPages) {
    throw new Error(`Page ${value} is out of range (this document has ${maxPages} pages).`);
  }
  return number;
}

// Validate endpoints BEFORE expansion, then union intervals so overlaps cost no extra pages.
export function parsePageRanges(input, maxPages) {
  validatePageCount(maxPages);
  const intervals = selectionParts(input).map(chunk => {
    const match = /^(\d+)(?:\s*-\s*(\d+))?$/.exec(chunk);
    if (!match) throw new Error(`"${chunk}" is not a valid page number or range.`);
    const a = pageNumber(match[1], maxPages);
    const b = pageNumber(match[2] || match[1], maxPages);
    return [Math.min(a, b), Math.max(a, b)];
  }).sort((a, b) => a[0] - b[0]);
  const merged = [];
  for (const interval of intervals) {
    const last = merged[merged.length - 1];
    if (last && interval[0] <= last[1] + 1) last[1] = Math.max(last[1], interval[1]);
    else merged.push(interval);
  }
  const pages = [];
  for (const [start, end] of merged) {
    for (let page = start; page <= end; page++) pages.push(page - 1);
  }
  return pages;
}

export function parsePageOrder(input, maxPages) {
  validatePageCount(maxPages);
  const seen = new Set();
  const order = [];
  for (const chunk of selectionParts(input)) {
    if (!/^\d+$/.test(chunk)) throw new Error(`"${chunk}" is not a valid page number.`);
    const page = pageNumber(chunk, maxPages);
    if (seen.has(page)) throw new Error(`Page ${page} is listed more than once. Use every page exactly once.`);
    seen.add(page);
    order.push(page - 1);
  }
  if (order.length !== maxPages) throw new Error(`Please list all ${maxPages} pages exactly once (you entered ${order.length}).`);
  return order;
}

export function boundedCanvasSize(width, height, desiredScale = 1.25, maxPixels = LIMITS.maxCanvasPixels, maxDimension = LIMITS.maxCanvasDimension) {
  if (![width, height, desiredScale].every(n => Number.isFinite(n) && n > 0)) throw new Error('This page has invalid dimensions.');
  const scale = Math.min(desiredScale, Math.sqrt(maxPixels / width) / Math.sqrt(height), maxDimension / width, maxDimension / height);
  if (!Number.isFinite(scale) || scale <= 0) throw new Error('This page is too large to render safely.');
  return { scale, width: Math.max(1, Math.floor(width * scale)), height: Math.max(1, Math.floor(height * scale)) };
}

export function sortedSlideNames(names) {
  const slides = [];
  for (const name of names) {
    const match = /^ppt\/slides\/slide(\d+)\.xml$/.exec(name);
    if (match) {
      const number = Number(match[1]);
      if (!Number.isSafeInteger(number) || number < 1) throw new Error('Invalid slide number in this presentation.');
      slides.push({ name, number });
    }
  }
  return slides.sort((a, b) => a.number - b.number).map(slide => slide.name);
}

export function yieldToEventLoop() {
  if (globalThis.scheduler?.yield) return globalThis.scheduler.yield();
  return new Promise(resolve => setTimeout(resolve, 0));
}

export function createProgressReporter(notify, now = () => performance.now()) {
  let lastTime = -Infinity;
  let lastPercent = -1;
  let lastText = '';
  return (percent, text) => {
    percent = Math.max(0, Math.min(100, Math.round(percent)));
    const time = now();
    if (percent === lastPercent && text === lastText) return;
    if (percent !== 100 && time - lastTime < LIMITS.progressIntervalMs) return;
    lastTime = time;
    lastPercent = percent;
    lastText = text;
    notify(percent, text);
  };
}

// Stream rather than inflate an arbitrarily large XML entry with entry.async('string').
export function readZipText(entry, maxBytes = LIMITS.maxSlideXmlBytes) {
  return new Promise((resolve, reject) => {
    let size = 0;
    let parts = [];
    let settled = false;
    const decoder = new TextDecoder();
    const stream = entry.internalStream('uint8array');
    const fail = error => {
      if (settled) return;
      settled = true;
      stream.pause();
      parts = [];
      reject(error);
    };
    stream.on('data', chunk => {
      if (settled) return;
      size += chunk.byteLength;
      if (size > maxBytes) return fail(new Error('Presentation slide XML exceeds the safe decompression limit.'));
      parts.push(decoder.decode(chunk, { stream: true }));
    });
    stream.on('error', fail);
    stream.on('end', () => {
      if (settled) return;
      settled = true;
      parts.push(decoder.decode());
      resolve({ text: parts.join(''), size });
      parts = [];
    });
    stream.resume();
  });
}

function wrapPdfText(text, font, size, maxWidth) {
  const lines = [];
  let line = '';
  let width = 0;
  const spaceWidth = font.widthOfTextAtSize(' ', size);
  for (const word of text.split(/\s+/).filter(Boolean)) {
    const wordWidth = font.widthOfTextAtSize(word, size);
    if (line && width + spaceWidth + wordWidth > maxWidth) {
      lines.push(line);
      line = word;
      width = wordWidth;
    } else {
      width += (line ? spaceWidth : 0) + wordWidth;
      line += (line ? ' ' : '') + word;
    }
  }
  if (line) lines.push(line);
  return lines;
}

function imageDataURL(bytes) {
  // PptxGenJS requires base64; keep this conversion and its strings off the UI thread.
  const chunks = [];
  for (let i = 0; i < bytes.length; i += 32768) chunks.push(String.fromCharCode(...bytes.subarray(i, i + 32768)));
  return 'data:image/jpeg;base64,' + btoa(chunks.join(''));
}

export function createProcessor({ loadLibrary, onProgress = () => {}, checkCancelled = () => {}, cooperative = true }) {
  const progress = createProgressReporter(onProgress);
  let raster = null;
  const checkpoint = async () => {
    checkCancelled();
    // A worker already leaves the UI free and can be terminated externally.
    // Only the main-thread fallback needs timer yields (which otherwise add up).
    if (cooperative) await yieldToEventLoop();
    checkCancelled();
  };
  const save = async (doc, filename, compatibility = false) => {
    progress(95, 'Writing output document...');
    await checkpoint();
    const data = await doc.save({ useObjectStreams: !compatibility, objectsPerTick: cooperative ? 25 : Infinity });
    checkCancelled();
    return { data, filename, type: 'application/pdf' };
  };
  const loadPDF = async (file, options = {}) => {
    const { PDFDocument } = await loadLibrary('pdfLib');
    // Do not retain another local copy of the complete input buffer.
    const doc = await PDFDocument.load(await file.arrayBuffer(), { parseSpeed: cooperative ? 50 : Infinity, ...options });
    validatePageCount(doc.getPageCount());
    return doc;
  };
  const copyPageBatches = async (out, source, indices, consume, label = 'Copying pages') => {
    const { PDFObjectCopier, PDFPage } = await loadLibrary('pdfLib');
    await source.flush();
    // Equivalent to PDFDocument.copyPages, but keep ONE copier across batches.
    // Calling copyPages/embedPages separately for every batch duplicates shared
    // fonts/images and can multiply output size by the number of batches.
    const copier = PDFObjectCopier.for(source.context, out.context);
    for (let start = 0; start < indices.length; start += LIMITS.pageBatchSize) {
      const pages = [];
      for (const index of indices.slice(start, start + LIMITS.pageBatchSize)) {
        const node = copier.copy(source.getPage(index).node);
        pages.push(PDFPage.of(node, out.context.register(node), out));
      }
      await consume(pages);
      progress(30 + 60 * (start + pages.length) / indices.length, `${label}: ${start + pages.length}/${indices.length}...`);
      await checkpoint();
    }
  };
  const copyPages = (out, source, indices) => copyPageBatches(out, source, indices, pages => {
    for (const page of pages) out.addPage(page);
  });

  async function presentationToPDF(file) {
    if (!/\.pptx$/i.test(file.name)) throw new Error('Please upload a .pptx file. Save legacy .ppt files as .pptx in PowerPoint first.');
    const JSZip = await loadLibrary('zip');
    const { PDFDocument, StandardFonts, rgb } = await loadLibrary('pdfLib');
    progress(20, 'Unpacking presentation...');
    let zip = await JSZip.loadAsync(await file.arrayBuffer());
    const names = Object.keys(zip.files);
    if (names.length > LIMITS.maxZipEntries) throw new Error('This presentation contains too many ZIP entries.');
    const slides = sortedSlideNames(names);
    if (!slides.length) throw new Error('No slides were found inside this PPTX file.');
    validatePageCount(slides.length);
    const doc = await PDFDocument.create();
    const regular = await doc.embedFont(StandardFonts.Helvetica);
    const bold = await doc.embedFont(StandardFonts.HelveticaBold);
    const decode = text => text.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&amp;/g, '&');
    let xmlBytes = 0;
    async function drawSlide(name) {
      const { text: xml, size } = await readZipText(zip.files[name], Math.min(LIMITS.maxSlideXmlBytes, LIMITS.maxPresentationXmlBytes - xmlBytes));
      xmlBytes += size;
      const texts = [];
      const pattern = /<a:t(?:\s[^>]*)?>([\s\S]*?)<\/a:t>/g;
      let match;
      let textLength = 0;
      while (texts.length < 23 && (match = pattern.exec(xml))) {
        const text = decode(match[1]).trim();
        textLength += text.length;
        if (textLength > LIMITS.maxSlideTextCharacters) throw new Error('This slide contains too much text to convert safely.');
        if (text) texts.push(text);
      }
      const page = doc.addPage([720, 540]);
      let y = 492;
      if (texts.length) {
        const title = texts.shift();
        const size = title.length > 90 ? 22 : 28;
        for (const line of wrapPdfText(title, bold, size, 620)) {
          if (y < 40) break;
          page.drawText(line, { x: 50, y, size, font: bold, color: rgb(0.12, 0.12, 0.14) });
          y -= size * 1.3;
        }
        y -= 12;
      }
      for (const text of texts) {
        for (const line of wrapPdfText('\u2022 ' + text, regular, 14, 620)) {
          if (y < 40) break;
          page.drawText(line, { x: 58, y, size: 14, font: regular, color: rgb(0.25, 0.25, 0.28) });
          y -= 14 * 1.45;
        }
        y -= 6;
        if (y < 40) break;
      }
    }
    for (let i = 0; i < slides.length; i++) {
      await drawSlide(slides[i]);
      zip.remove(slides[i]);
      progress(20 + 65 * (i + 1) / slides.length, `Converting slide ${i + 1}/${slides.length}...`);
      await checkpoint();
    }
    zip = null;
    return save(doc, file.name.replace(/\.pptx$/i, '') + '.pdf');
  }

  async function execute(tool, files, options = {}) {
    validateFiles(files, tool);
    checkCancelled();
    progress(10, 'Reading document...');
    await checkpoint();
    const file = files[0];
    if (tool === 'ppt-to-pdf') return presentationToPDF(file);
    const { PDFDocument, StandardFonts, degrees, rgb } = await loadLibrary('pdfLib');

    if (tool === 'merge-pdf') {
      const out = await PDFDocument.create();
      for (let i = 0; i < files.length; i++) {
        const source = await loadPDF(files[i]);
        validatePageCount(out.getPageCount() + source.getPageCount());
        await copyPages(out, source, source.getPageIndices());
        progress(20 + 65 * (i + 1) / files.length, `Merging file ${i + 1}/${files.length}...`);
      }
      return save(out, 'merged.pdf');
    }
    if (tool === 'jpg-to-pdf' || tool === 'png-to-pdf') {
      const out = await PDFDocument.create();
      for (let i = 0; i < files.length; i++) {
        const image = tool === 'jpg-to-pdf' ? await out.embedJpg(await files[i].arrayBuffer()) : await out.embedPng(await files[i].arrayBuffer());
        const page = out.addPage([image.width, image.height]);
        page.drawImage(image, { x: 0, y: 0, width: image.width, height: image.height });
        await image.embed();
        progress(20 + 65 * (i + 1) / files.length, `Embedding image ${i + 1}/${files.length}...`);
        await checkpoint();
      }
      return save(out, 'images_converted.pdf');
    }

    let doc;
    try {
      doc = await loadPDF(file, tool === 'repair-pdf' || tool === 'unlock-pdf' ? { ignoreEncryption: true, throwOnInvalidObject: false } : {});
    } catch (error) {
      if (tool === 'repair-pdf' && !/at most/.test(error.message)) throw new Error('This file is too damaged to recover automatically. Please obtain a new copy.');
      throw error;
    }
    if (doc.isEncrypted) throw new Error('Encrypted PDFs are not supported by this processing engine. Please unlock the document in a trusted PDF editor first.');
    const total = doc.getPageCount();

    if (['split-pdf', 'extract-pages-pdf', 'delete-pdf-pages', 'reorder-pages-pdf'].includes(tool)) {
      let indices = tool === 'reorder-pages-pdf' ? parsePageOrder(options.order, total) : parsePageRanges(options.range, total);
      if (tool === 'delete-pdf-pages') {
        if (indices.length === total) throw new Error('You cannot delete every page — leave at least one page in the document.');
        const removed = new Set(indices);
        indices = doc.getPageIndices().filter(index => !removed.has(index));
      }
      const out = await PDFDocument.create();
      await copyPages(out, doc, indices);
      doc = null;
      const names = { 'split-pdf': 'split.pdf', 'extract-pages-pdf': 'extracted-pages.pdf', 'delete-pdf-pages': 'deleted-pages.pdf', 'reorder-pages-pdf': 'reordered.pdf' };
      return save(out, names[tool]);
    }

    if (tool === 'resize-pdf') {
      const [width, height] = options.format === 'letter' ? [612, 792] : [595.28, 841.89];
      const out = await PDFDocument.create();
      await copyPageBatches(out, doc, doc.getPageIndices(), async sources => {
        // These pages already belong to the destination context: embedPages
        // neither reparses the file nor recopies shared resources.
        for (const page of sources) if (!page.node.Contents()) page.pushOperators();
        const embedded = await out.embedPages(sources);
        for (const image of embedded) {
          const page = out.addPage([width, height]);
          const scale = Math.min(width / image.width, height / image.height);
          const w = image.width * scale;
          const h = image.height * scale;
          page.drawPage(image, { x: (width - w) / 2, y: (height - h) / 2, width: w, height: h });
          await image.embed();
        }
      }, 'Resizing pages');
      doc = null;
      return save(out, 'resized.pdf');
    }

    if (tool === 'flatten-pdf') {
      progress(60, 'Flattening form fields...');
      const form = doc.getForm();
      if (form.getFields().length) form.flatten();
      return save(doc, 'flattened.pdf');
    }
    if (tool === 'pdf-metadata-editor') {
      const { title = '', author = '', subject = '', keywords = '' } = options;
      if (!title && !author && !subject && !keywords) throw new Error('Fill in at least one metadata field before processing.');
      if (title) doc.setTitle(title);
      if (author) doc.setAuthor(author);
      if (subject) doc.setSubject(subject);
      if (keywords) doc.setKeywords(keywords.split(',').map(k => k.trim()).filter(Boolean));
      doc.setModificationDate(new Date());
      return save(doc, 'metadata-updated.pdf');
    }
    // Repair intentionally favors compatibility; normal tools use compressed object streams.
    if (tool === 'repair-pdf') return save(doc, 'repaired.pdf', true);
    if (tool === 'unlock-pdf') return save(doc, 'unlocked.pdf');
    if (tool === 'protect-pdf') throw new Error('Password encryption is not supported by this processing engine. No file has been changed.');
    if (tool === 'esign-pdf') {
      const image = await doc.embedPng(options.signature);
      doc.getPage(0).drawImage(image, { x: 50, y: 50, width: 180, height: 90 });
      return save(doc, 'signed.pdf');
    }

    let font;
    if (tool === 'add-watermark-pdf') font = await doc.embedFont(StandardFonts.HelveticaBold);
    if (tool === 'number-pdf-pages') font = await doc.embedFont(StandardFonts.Helvetica);
    const clampPct = value => Math.min(Math.max(Number(value) || 0, 0), 45) / 100;
    for (let index = 0; index < total; index++) {
      const page = doc.getPage(index);
      const { width, height } = page.getSize();
      switch (tool) {
        case 'rotate-pdf':
          page.setRotation(degrees(page.getRotation().angle + (Number(options.angle) || 90)));
          break;
        case 'add-watermark-pdf':
          page.drawText(options.text || 'CONFIDENTIAL', { x: width / 6, y: height / 2.5, size: 50, font, color: rgb(1, 0.32, 0), opacity: Number(options.opacity) || 0.4, rotate: degrees(45) });
          break;
        case 'number-pdf-pages':
          page.drawText(`Page ${index + 1} of ${total}`, { x: options.position === 'bottom-right' ? width - 100 : width / 2 - 20, y: 25, size: Number(options.fontSize) || 12, font, color: rgb(0.2, 0.2, 0.2) });
          break;
        case 'crop-pdf': {
          const l = clampPct(options.left), r = clampPct(options.right), t = clampPct(options.top), b = clampPct(options.bottom);
          const w = width * (1 - l - r), h = height * (1 - t - b);
          if (w > 10 && h > 10) page.setCropBox(width * l, height * b, w, h);
          break;
        }
        default:
          throw new Error('This tool is not implemented yet. No file has been changed.');
      }
      progress(25 + 60 * (index + 1) / total, `Processing page ${index + 1}/${total}...`);
      if ((index + 1) % 5 === 0) await checkpoint();
    }
    const names = { 'rotate-pdf': 'rotated.pdf', 'add-watermark-pdf': 'watermarked.pdf', 'number-pdf-pages': 'numbered.pdf', 'crop-pdf': 'cropped.pdf' };
    return save(doc, names[tool]);
  }

  async function startRaster({ tool, total, filename }) {
    validatePageCount(total, true);
    raster = { tool, total, filename, count: 0, bytes: 0 };
    if (tool === 'pdf-to-powerpoint') {
      const PptxGenJS = await loadLibrary('pptx');
      raster.output = new PptxGenJS();
      raster.output.defineLayout({ name: 'PDFZAAP_SLIDES', width: 10, height: 7.5 });
      raster.output.layout = 'PDFZAAP_SLIDES';
    } else if (tool === 'pdf-to-jpg' || tool === 'pdf-to-png') {
      const JSZip = await loadLibrary('zip');
      raster.output = new JSZip();
    } else if (tool === 'compress-pdf' || tool === 'grayscale-pdf') {
      const { PDFDocument } = await loadLibrary('pdfLib');
      raster.output = await PDFDocument.create();
    } else throw new Error('Unknown raster operation.');
  }

  async function addRasterPage({ data, width, height }) {
    if (!raster || raster.count >= raster.total) throw new Error('Invalid raster processing session.');
    boundedCanvasSize(width, height);
    const bytes = new Uint8Array(data);
    raster.bytes += bytes.byteLength;
    if (raster.bytes > LIMITS.maxRasterBytes) throw new Error('Rendered images exceed the 100 MB safety limit. Use fewer pages or lower quality.');
    raster.count++;
    const { tool, output, count } = raster;
    if (tool === 'pdf-to-powerpoint') {
      const scale = Math.min(10 / width, 7.5 / height);
      const w = width * scale, h = height * scale;
      output.addSlide().addImage({ data: imageDataURL(bytes), x: (10 - w) / 2, y: (7.5 - h) / 2, w, h });
    } else if (tool === 'pdf-to-jpg' || tool === 'pdf-to-png') {
      output.file(`page-${count}.${tool === 'pdf-to-png' ? 'png' : 'jpg'}`, bytes);
    } else {
      const image = await output.embedJpg(bytes);
      // Pixel resolution must not change the physical PDF page size.
      output.addPage([width, height]).drawImage(image, { x: 0, y: 0, width, height });
      await image.embed();
    }
  }

  async function grayscale({ pixels }) {
    const data = new Uint8ClampedArray(pixels);
    if (data.length % 4 || data.length > LIMITS.maxCanvasPixels * 4) throw new Error('Grayscale image exceeds the canvas safety limit.');
    for (let start = 0; start < data.length; start += 1024 * 1024) {
      const end = Math.min(start + 1024 * 1024, data.length);
      for (let i = start; i < end; i += 4) {
        const brightness = 0.34 * data[i] + 0.5 * data[i + 1] + 0.16 * data[i + 2];
        data[i] = data[i + 1] = data[i + 2] = brightness;
      }
      await checkpoint();
    }
    return { pixels: data.buffer };
  }

  async function finishRaster() {
    if (!raster || raster.count !== raster.total) throw new Error('Not all pages have been processed.');
    const { tool, output, filename } = raster;
    raster = null;
    progress(92, 'Building output file...');
    await checkpoint();
    if (tool === 'pdf-to-powerpoint') {
      const data = await output.write({ outputType: 'arraybuffer' });
      return { data, filename, type: 'application/vnd.openxmlformats-officedocument.presentationml.presentation' };
    }
    if (tool === 'pdf-to-jpg' || tool === 'pdf-to-png') {
      const data = await output.generateAsync({ type: 'uint8array', streamFiles: true, compression: 'STORE' }, meta => progress(92 + meta.percent * 0.07, 'Packing images...'));
      return { data, filename, type: 'application/zip' };
    }
    return save(output, filename);
  }

  return {
    async handle(command, payload = {}) {
      checkCancelled();
      switch (command) {
        case 'execute': return execute(payload.tool, payload.files, payload.options);
        case 'wordToHTML': {
          validateFiles([payload.file], 'word-to-pdf');
          const mammoth = await loadLibrary('mammoth');
          const { value } = await mammoth.convertToHtml({ arrayBuffer: await payload.file.arrayBuffer() });
          checkCancelled();
          if (value.length > LIMITS.maxWordHtmlCharacters) throw new Error('Converted Word content is too large. Split the document into smaller parts first.');
          return { html: value };
        }
        case 'startRaster': return startRaster(payload);
        case 'addRasterPage': return addRasterPage(payload);
        case 'grayscale': return grayscale(payload);
        case 'finishRaster': return finishRaster();
        default: throw new Error('Unknown processing command.');
      }
    },
    dispose() { raster = null; }
  };
}

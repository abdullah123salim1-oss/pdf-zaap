// Converters introduced on main while the worker refactor was in review.
// Preserve their formats/content while adapting them to the same job lifecycle.
import { LIMITS, boundedCanvasSize, validatePageCount, yieldToEventLoop } from './processing-core.js';

const dependencies = {
  'ocr-pdf': ['pdfjs', 'tesseract'],
  'html-to-pdf': ['html2pdf'],
  'excel-to-pdf': ['xlsx', 'html2pdf'],
  'pdf-to-html': ['pdfjs'],
  'pdf-to-epub': ['pdfjs', 'zip'],
  'pdf-to-word': ['pdfjs', 'zip'],
  'pdf-to-excel': ['pdfjs', 'xlsx'],
  'compare-pdf': ['pdfjs']
};

export async function runAdvancedTool(tool, files, { loadLibrary, renderHTML, canvasToBlob, onProgress, signal }) {
  const libraries = {};
  for (const name of dependencies[tool]) libraries[name] = await loadLibrary(name);
  const check = () => { if (signal?.aborted) throw new DOMException('Processing cancelled.', 'AbortError'); };
  check();
  const tasks = new Set();
  const ocrWorkers = new Set();
  let canvas;
  let output;
  let textCharacters = 0;
  const setProgressUI = (percent, text) => { check(); onProgress(Math.min(percent, 99), text); };
  const createDownloadLink = (data, filename, type, note) => { check(); output = { data, filename, type, note }; };
  const JSZip = libraries.zip;
  const XLSX = libraries.xlsx;
  const html2pdf = libraries.html2pdf;
  const pdfjsLib = {
    getDocument(options) {
      check();
      const task = libraries.pdfjs.getDocument({ ...options, isEvalSupported: false, canvasMaxAreaInBytes: LIMITS.maxCanvasPixels * 4 });
      tasks.add(task);
      return { promise: task.promise.then(pdf => { validatePageCount(pdf.numPages, tool === 'ocr-pdf'); check(); return pdf; }) };
    }
  };
  const guarded = promise => new Promise((resolve, reject) => {
    const abort = () => reject(new DOMException('Processing cancelled.', 'AbortError'));
    signal?.addEventListener('abort', abort, { once: true });
    Promise.resolve(promise).then(value => { signal?.removeEventListener('abort', abort); resolve(value); }, error => { signal?.removeEventListener('abort', abort); reject(error); });
    if (signal?.aborted) { signal.removeEventListener('abort', abort); abort(); }
  });
  const Tesseract = libraries.tesseract && {
    createWorker: (...args) => guarded(libraries.tesseract.createWorker(...args).then(worker => {
      let termination;
      const wrapped = {
        recognize: async image => {
          check();
          const bytes = new Uint8Array(await (await canvasToBlob(image, 'image/png')).arrayBuffer());
          check();
          return guarded(worker.recognize(bytes));
        },
        terminate: () => termination ||= Promise.resolve(worker.terminate())
      };
      if (signal?.aborted) { wrapped.terminate().catch(() => {}); check(); }
      ocrWorkers.add(wrapped);
      return wrapped;
    }))
  };
  function getCanvas(size) {
    canvas ||= document.createElement('canvas');
    canvas.width = size.width;
    canvas.height = size.height;
    return canvas;
  }
  async function renderPageToCanvas(pdf, pageNum, scale) {
    check();
    const page = await pdf.getPage(pageNum);
    try {
      const base = page.getViewport({ scale: 1 });
      const size = boundedCanvasSize(base.width, base.height, scale);
      const canvas = getCanvas(size);
      await page.render({ canvasContext: canvas.getContext('2d'), viewport: page.getViewport({ scale: size.scale }), background: 'rgb(255,255,255)' }).promise;
      check();
      return canvas;
    } finally { page.cleanup(); }
  }
  const abort = () => {
    for (const task of tasks) task.destroy().catch(() => {});
    for (const worker of ocrWorkers) worker.terminate().catch(() => {});
  };
  signal?.addEventListener('abort', abort, { once: true });
  try {
    const runners = {
      'ocr-pdf': runOCRPDF, 'html-to-pdf': runHTMLToPDF, 'excel-to-pdf': runExcelToPDF,
      'pdf-to-html': runPDFToHTML, 'pdf-to-epub': runPDFToEPUB, 'pdf-to-word': runPDFToWord,
      'pdf-to-excel': runPDFToExcel, 'compare-pdf': runComparePDF
    };
    await runners[tool](tool === 'compare-pdf' ? files : files[0]);
    check();
    return output;
  } finally {
    signal?.removeEventListener('abort', abort);
    if (canvas) canvas.width = canvas.height = 0;
    await Promise.allSettled([...tasks].map(task => task.destroy()));
    await Promise.allSettled([...ocrWorkers].map(worker => worker.terminate()));
  }

// Helper: extract text lines from a pdf.js page (grouped by Y coordinate)
async function extractPageLines(page) {
  check();
  let content;
  try { content = await page.getTextContent(); } finally { page.cleanup(); }
  await yieldToEventLoop();
  check();
  const byY = new Map();
  for (const item of content.items) {
    if (!item.str) continue;
    const y = Math.round(item.transform[5]);
    const bucket = byY.get(y);
    if (bucket) bucket.push([item.transform[4], item.str]);
    else byY.set(y, [[item.transform[4], item.str]]);
  }
  const lines = [];
  const ys = Array.from(byY.keys()).sort((a, b) => b - a);
  for (const y of ys) {
    const parts = byY.get(y).sort((a, b) => a[0] - b[0]);
    lines.push(parts.map(p => p[1]).join(' ').replace(/\s+/g, ' ').trim());
  }
  textCharacters += lines.reduce((sum, line) => sum + line.length, 0);
  if (textCharacters * 2 > LIMITS.maxRasterBytes) throw new Error('Extracted text exceeds the safety limit. Use fewer pages.');
  return lines.filter(l => l.length > 0);
}

function escapeXml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// OCR PDF (Tesseract.js — recognition runs in a local Web Worker; only the public language model is downloaded)
async function runOCRPDF(file) {
  if (typeof Tesseract === 'undefined') throw new Error('The OCR engine failed to load. Please refresh the page and try again.');
  setProgressUI(5, 'Preparing OCR engine...');
  const isImage = /\.(jpe?g|png|webp|bmp)$/i.test(file.name);
  const baseName = file.name.replace(/\.[^.]+$/, '');

  const worker = await Tesseract.createWorker('eng', 1, {
    logger: m => {
      if (!signal?.aborted && m.status === 'recognizing text') {
        setProgressUI(10 + Math.round(m.progress * 85), `Recognizing text… ${Math.round(m.progress * 100)}%`);
      }
    }
  });

  try {
    let allText = '';
    if (isImage) {
      setProgressUI(10, 'Loading image...');
      const img = await createImageBitmap(file);
      let canvas;
      try {
        const size = boundedCanvasSize(img.width, img.height, 1);
        canvas = getCanvas(size);
        canvas.getContext('2d').drawImage(img, 0, 0, size.width, size.height);
      } finally { img.close(); }
      const { data } = await worker.recognize(canvas);
      allText = data.text;
      canvas.width = canvas.height = 0;
    } else {
      const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
      for (let i = 1; i <= pdf.numPages; i++) {
        setProgressUI(5 + Math.round(((i - 1) / pdf.numPages) * 90), `Preparing page ${i} of ${pdf.numPages} for OCR...`);
        const canvas = await renderPageToCanvas(pdf, i, 2);
        const { data } = await worker.recognize(canvas);
        allText += `--- Page ${i} ---\n${data.text.trim()}\n\n`;
        canvas.width = canvas.height = 0;
        if (allText.length * 2 > LIMITS.maxRasterBytes) throw new Error('Recognized text exceeds the safety limit. Use fewer pages.');
        await yieldToEventLoop();
      }
    }
    if (!allText.trim()) {
      throw new Error('No readable text was found. Make sure the document contains clear, printed English text (photos of handwriting are not supported).');
    }
    setProgressUI(98, 'Building text file...');
    createDownloadLink(new TextEncoder().encode(allText), `${baseName}_ocr.txt`, 'text/plain',
      'OCR finished. The output is a plain-text file with the recognized words. Check a few paragraphs — OCR is not perfect, so always proofread before submitting important documents.');
  } finally {
    await worker.terminate();
  }
}

// HTML to PDF (html2pdf.js renders the markup in your browser)
async function runHTMLToPDF(file) {
  if (typeof html2pdf === 'undefined') throw new Error('The PDF rendering engine failed to load. Please refresh the page and try again.');
  setProgressUI(20, 'Reading HTML file...');
  const text = await file.text();
  check();
  if (text.length > LIMITS.maxWordHtmlCharacters) throw new Error('HTML content is too large. Use a smaller file.');
  const baseName = file.name.replace(/\.[^.]+$/, '');

  const container = document.createElement('div');
  container.style.width = '720px';
  container.style.padding = '12px';
  container.style.fontFamily = 'Arial, Helvetica, sans-serif';
  container.style.fontSize = '13px';
  container.style.lineHeight = '1.55';
  container.style.color = '#111';
  container.innerHTML = text;
  // Neutralize scripts inside user markup before rendering
  container.querySelectorAll('script, iframe, object, embed, link[rel="import"]').forEach(el => el.remove());

  setProgressUI(55, 'Rendering pages...');
  const pdfBlob = await renderHTML(container, { margin: 10, jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } });

  setProgressUI(100, 'Processing completed!');
  createDownloadLink(pdfBlob, `${baseName}.pdf`, 'application/pdf',
    'Done. Note: images and styles from external URLs may not be embedded — keep assets local or inline for the best result.');
}

// Excel to PDF (SheetJS parses the workbook, html2pdf renders the sheets)
async function runExcelToPDF(file) {
  if (typeof XLSX === 'undefined' || typeof html2pdf === 'undefined') throw new Error('The spreadsheet engine failed to load. Please refresh the page and try again.');
  setProgressUI(15, 'Reading workbook...');
  const wb = XLSX.read(await file.arrayBuffer(), { type: 'array' });
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const sheetNames = wb.SheetNames.slice(0, 10);

  let body = '';
  for (let i = 0; i < sheetNames.length; i++) {
    setProgressUI(20 + Math.round((i / sheetNames.length) * 40), `Rendering sheet ${i + 1} of ${sheetNames.length}: ${sheetNames[i]}`);
    const sheet = wb.Sheets[sheetNames[i]];
    if (!sheet || !sheet['!ref']) continue;
    const range = XLSX.utils.decode_range(sheet['!ref']);
    const maxRow = Math.min(range.e.r, range.s.r + 4999);
    const rows = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '', range: { s: range.s, e: { r: maxRow, c: range.e.c } } });
    if (!rows.length) continue;
    let table = '<table style="border-collapse:collapse;width:100%;font-size:10px;font-family:Arial,sans-serif;margin:8px 0 20px;">';
    table += '<thead><tr>' + rows[0].map(h => `<th style="border:1px solid #999;padding:3px 6px;background:#f0f0f0;">${escapeHtml(h)}</th>`).join('') + '</tr></thead><tbody>';
    for (let r = 1; r < rows.length; r++) {
      table += '<tr>' + rows[r].map(c => `<td style="border:1px solid #ccc;padding:2px 6px;">${escapeHtml(c)}</td>`).join('') + '</tr>';
    }
    table += '</tbody></table>';
    if (table.length + body.length > LIMITS.maxWordHtmlCharacters) throw new Error('The workbook is too large to render safely. Use fewer rows.');
    body += `<h3 style="font-family:Arial,sans-serif;font-size:14px;">${escapeHtml(sheetNames[i])}</h3>` + table;
  }
  if (!body) throw new Error('No readable sheets were found in this workbook.');

  const container = document.createElement('div');
  container.innerHTML = body;

  setProgressUI(70, 'Building PDF...');
  const pdfBlob = await renderHTML(container, { margin: [8, 6, 8, 6], jsPDF: { unit: 'mm', format: 'a4', orientation: 'landscape' } });

  setProgressUI(100, 'Processing completed!');
  createDownloadLink(pdfBlob, `${baseName}.pdf`, 'application/pdf',
    `Done. ${sheetNames.length} sheet(s) exported, up to 5,000 rows per sheet. Very wide columns may be split across pages.`);
}

// PDF to HTML (pdf.js text extraction, grouped into readable lines)
async function runPDFToHTML(file) {
  setProgressUI(15, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  let pagesHtml = '';
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(15 + Math.round((i / pdf.numPages) * 75), `Converting page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    const paras = lines.map(l => `<p>${escapeHtml(l)}</p>`).join('');
    pagesHtml += `<section class="page"><h2>Page ${i}</h2>${paras || '<p><em>(no extractable text on this page)</em></p>'}</section>`;
  }
  const doc = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapeHtml(baseName)} — converted from PDF</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;max-width:800px;margin:2rem auto;padding:0 1.25rem;color:#222;line-height:1.6;}
h1{font-size:1.5rem;} h2{font-size:1.1rem;margin-top:2rem;border-bottom:1px solid #ddd;padding-bottom:.3rem;}
p{margin:.4rem 0;} .meta{color:#666;font-size:.85rem;}
</style>
</head>
<body>
<h1>${escapeHtml(baseName)}</h1>
<p class="meta">Converted from PDF in the browser by PDFZaap. Text is extracted in reading order; complex multi-column layouts may not map perfectly.</p>
${pagesHtml}
</body>
</html>`;
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(new TextEncoder().encode(doc), `${baseName}.html`, 'text/html',
    'Done. The HTML preserves text in reading order. Page graphics are not embedded — use PDF to JPG or PDF to PNG for images.');
}

// PDF to EPUB (minimal valid EPUB 3 built with JSZip)
async function runPDFToEPUB(file) {
  if (typeof JSZip === 'undefined') throw new Error('The EPUB builder failed to load. Please refresh the page and try again.');
  setProgressUI(10, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const bookTitle = baseName.replace(/[_-]+/g, ' ');
  const chapters = [];
  const navItems = [];
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(10 + Math.round((i / pdf.numPages) * 70), `Preparing chapter ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    const paras = lines.map(l => `<p>${escapeXml(l)}</p>`).join('');
    chapters.push(`<section epub:type="chapter"><h2>Page ${i}</h2>${paras || '<p>(no extractable text)</p>'}</section>`);
    navItems.push(`<li><a href="c${i}.xhtml">Page ${i}</a></li>`);
  }
  const id = 'zaap-' + Date.now().toString(36);
  const opf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">${id}</dc:identifier>
    <dc:title>${escapeXml(bookTitle)}</dc:title>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">${new Date().toISOString().replace(/\.\d{3}Z/, 'Z')}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    ${chapters.map((_, i) => `<item id="c${i + 1}" href="c${i + 1}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
  </manifest>
  <spine>${chapters.map((_, i) => `<itemref idref="c${i + 1}"/>`).join('')}</spine>
</package>`;
  const nav = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Navigation</title></head>
<body><nav epub:type="toc"><h1>Contents</h1><ol>${navItems.join('')}</ol></nav></body>
</html>`;
  const xhtmlFor = (i, body) => `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Page ${i}</title></head>
<body>${body}</body>
</html>`;

  const zip = new JSZip();
  zip.file('mimetype', 'application/epub+zip', { compression: 'STORE' });
  zip.file('META-INF/container.xml', `<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>`, { compression: 'STORE' });
  zip.file('OEBPS/content.opf', opf);
  zip.file('OEBPS/nav.xhtml', nav);
  chapters.forEach((c, i) => zip.file(`OEBPS/c${i + 1}.xhtml`, xhtmlFor(i + 1, c)));

  setProgressUI(90, 'Packing EPUB file...');
  const blob = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE' });
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(blob, `${baseName}.epub`, 'application/epub+zip',
    'Done. The EPUB is reflowable text — each PDF page becomes one chapter. Graphics are not embedded; use OCR PDF first if your source is scanned.');
}

// PDF to Word (minimal valid DOCX built with JSZip — text-based conversion)
async function runPDFToWord(file) {
  if (typeof JSZip === 'undefined') throw new Error('The DOCX builder failed to load. Please refresh the page and try again.');
  setProgressUI(10, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  let bodyXml = '';
  let pageBreakCount = 0;
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(10 + Math.round((i / pdf.numPages) * 75), `Converting page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    if (i > 1) {
      bodyXml += `<w:p><w:r><w:br w:type="page"/></w:r></w:p>`;
      pageBreakCount++;
    }
    bodyXml += lines.length
      ? lines.map(l => `<w:p><w:r><w:t xml:space="preserve">${escapeXml(l)}</w:t></w:r></w:p>`).join('')
      : `<w:p><w:r><w:t xml:space="preserve">(no extractable text)</w:t></w:r></w:p>`;
  }
  const documentXml = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>${bodyXml}<w:sectPr><w:pgSz w:w="12240" w:h="15840"/></w:sectPr></w:body>
</w:document>`;
  const contentTypes = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>`;
  const rels = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`;

  const zip = new JSZip();
  zip.file('[Content_Types].xml', contentTypes);
  zip.file('_rels/.rels', rels);
  zip.file('word/document.xml', documentXml);

  setProgressUI(95, 'Packing Word file...');
  const blob = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE' });
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(blob, `${baseName}.docx`, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'Done. This is a text-based conversion: all words and the reading order are preserved, but multi-column layouts, tables and images are simplified. For pixel-perfect fidelity, export pages as images instead.');
}

// PDF to Excel (pdf.js text lines → SheetJS worksheet)
async function runPDFToExcel(file) {
  if (typeof XLSX === 'undefined') throw new Error('The spreadsheet engine failed to load. Please refresh the page and try again.');
  setProgressUI(15, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const rows = [];
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(15 + Math.round((i / pdf.numPages) * 70), `Extracting rows from page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    lines.forEach(line => {
      const cells = line.split(/\t|\s{2,}/).map(c => c.trim()).filter(Boolean);
      rows.push(cells.length ? cells : ['']);
    });
    if (i < pdf.numPages) rows.push([]);
  }
  if (!rows.length) throw new Error('No extractable text was found in this PDF.');
  const ws = XLSX.utils.aoa_to_sheet(rows);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Page text');
  const out = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
  setProgressUI(100, 'Export complete!');
  createDownloadLink(new Blob([out], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }),
    `${baseName}.xlsx`, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'Done. Each text line becomes a spreadsheet row; cells are split where the PDF used tabs or clear column spacing. Complex tables may need a little manual cleanup.');
}

// Compare PDFs (pdf.js text extraction + line diff → HTML report)
async function diffLines(a, b) {
  const n = a.length, m = b.length;
  // Guard: DP is O(n*m); cap for very large documents
  if ((n + 1) * (m + 1) > 9_000_000) return null;
  const dp = Array.from({ length: n + 1 }, () => new Uint32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    if (i % 100 === 0) { await yieldToEventLoop(); check(); }
    for (let j = m - 1; j >= 0; j--) {
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const out = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) { out.push({ t: 'eq', s: a[i] }); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { out.push({ t: 'del', s: a[i] }); i++; }
    else { out.push({ t: 'add', s: b[j] }); j++; }
  }
  while (i < n) { out.push({ t: 'del', s: a[i] }); i++; }
  while (j < m) { out.push({ t: 'add', s: b[j] }); j++; }
  return out;
}

async function runComparePDF(files) {
  if (files.length < 2) throw new Error('Please select exactly two PDF files to compare.');
  if (files.length > 2) throw new Error('Please select exactly two PDF files to compare.');
  setProgressUI(15, 'Reading first document...');
  const pdfA = await pdfjsLib.getDocument({ data: await files[0].arrayBuffer() }).promise;
  setProgressUI(35, 'Reading second document...');
  const pdfB = await pdfjsLib.getDocument({ data: await files[1].arrayBuffer() }).promise;

  const collect = async (pdf) => {
    const all = [];
    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const lines = await extractPageLines(page);
      lines.forEach(l => all.push(l));
    }
    return all;
  };
  setProgressUI(55, 'Extracting text...');
  const linesA = await collect(pdfA);
  const linesB = await collect(pdfB);

  setProgressUI(75, 'Computing differences...');
  const ops = await diffLines(linesA, linesB);
  const additions = ops ? ops.filter(o => o.t === 'add').length : 0;
  const deletions = ops ? ops.filter(o => o.t === 'del').length : 0;

  let rowsHtml;
  if (ops) {
    rowsHtml = ops.map(o => {
      if (o.t === 'eq') return `<tr class="same"><td>${escapeHtml(o.s)}</td></tr>`;
      if (o.t === 'add') return `<tr class="add"><td>+ ${escapeHtml(o.s)}</td></tr>`;
      return `<tr class="del"><td>- ${escapeHtml(o.s)}</td></tr>`;
    }).join('');
  } else {
    rowsHtml = `<p>The documents are too large for a line-by-line diff in the browser. Both text exports are listed below for manual review.</p>`;
  }

  const report = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Comparison: ${escapeHtml(files[0].name)} vs ${escapeHtml(files[1].name)}</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;max-width:900px;margin:2rem auto;padding:0 1.25rem;color:#222;}
h1{font-size:1.4rem;} .meta{color:#555;font-size:.9rem;}
table{width:100%;border-collapse:collapse;font-size:.85rem;font-family:Consolas,Monaco,monospace;}
td{padding:.2rem .5rem;border-bottom:1px solid #eee;white-space:pre-wrap;}
tr.add td{background:#e6f6e6;color:#145214;}
tr.del td{background:#fdecea;color:#7a1f1f;}
.summary{background:#f7f7f7;border:1px solid #ddd;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0;}
</style>
</head>
<body>
<h1>PDF comparison report</h1>
<p class="meta">Document A: ${escapeHtml(files[0].name)} (${pdfA.numPages} pages, ${linesA.length} lines) &middot; Document B: ${escapeHtml(files[1].name)} (${pdfB.numPages} pages, ${linesB.length} lines) &middot; Generated in the browser by PDFZaap</p>
<div class="summary"><strong>Result:</strong> ${ops ? `${additions} added line(s), ${deletions} removed line(s) compared to document A.` : 'Detailed diff unavailable (documents too large).'}</div>
<table><tbody>${rowsHtml}</tbody></table>
</body>
</html>`;
  setProgressUI(100, 'Report ready!');
  createDownloadLink(new TextEncoder().encode(report),
    `${files[0].name.replace(/\.[^.]+$/, '')}_vs_${files[1].name.replace(/\.[^.]+$/, '')}_report.html`, 'text/html',
    `Done. ${ops ? `Found ${additions} added and ${deletions} removed lines.` : 'Opened as an HTML report you can view in any browser.'}`);
}


}

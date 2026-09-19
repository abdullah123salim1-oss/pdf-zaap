// Real-browser integration tests, with CDN bundles served from matching npm fixtures.
// No documents or fixture contents are sent over the network.
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { chromium } from 'playwright';
import { PDFDocument, rgb } from 'pdf-lib';
import JSZip from 'jszip';

const root = fileURLToPath(new URL('../', import.meta.url));
const server = createServer(async (request, response) => {
  const name = decodeURIComponent(new URL(request.url, 'http://test').pathname);
  const filename = path.resolve(root, '.' + (name === '/' ? '/index.html' : name));
  if (!filename.startsWith(root) || name.includes('/.git')) { response.writeHead(403).end(); return; }
  try {
    const data = await readFile(filename);
    const type = { '.js': 'text/javascript', '.html': 'text/html', '.css': 'text/css', '.png': 'image/png' }[path.extname(filename)] || 'application/octet-stream';
    response.writeHead(200, { 'Content-Type': type }).end(data);
  } catch { response.writeHead(404).end(); }
});
await new Promise(resolve => server.listen(0, '0.0.0.0', resolve));
const base = `http://127.0.0.1:${server.address().port}`;
let browser;
try {
  browser = await chromium.launch({
    headless: true,
    ...(process.env.BROWSER_EXECUTABLE ? { executablePath: process.env.BROWSER_EXECUTABLE } : {}),
    args: ['--no-sandbox', '--disable-dev-shm-usage']
  });
  const context = await browser.newContext({ acceptDownloads: true });
  const dependencies = [
    ['/pdf-lib@', 'pdf-lib/dist/pdf-lib.min.js'],
    ['/pdf.worker.min.js', 'pdfjs-dist/build/pdf.worker.min.js'],
    ['/pdf.min.js', 'pdfjs-dist/build/pdf.min.js'],
    ['/jszip.min.js', 'jszip/dist/jszip.min.js'],
    ['/pptxgen.bundle.js', 'pptxgenjs/dist/pptxgen.bundle.js'],
    ['/mammoth.browser.min.js', 'mammoth/mammoth.browser.min.js'],
    ['/html2pdf.bundle.min.js', 'html2pdf.js/dist/html2pdf.bundle.min.js']
  ];
  await context.route('**/*', async route => {
    const url = route.request().url();
    if (url.startsWith(base) || url.startsWith('blob:') || url.startsWith('data:')) return route.continue();
    const dependency = dependencies.find(([pattern]) => url.includes(pattern));
    if (dependency) return route.fulfill({ path: path.join(root, 'node_modules', dependency[1]), contentType: 'text/javascript', headers: { 'Access-Control-Allow-Origin': '*' } });
    return route.fulfill({ body: '', contentType: 'text/plain', headers: { 'Access-Control-Allow-Origin': '*' } });
  });
  const page = await context.newPage();
  const errors = [];
  const downloads = [];
  page.on('download', download => downloads.push(download));
  page.on('pageerror', error => errors.push(error.message));
  await page.addInitScript(() => {
    window.ownedCanvases = [];
    const create = document.createElement.bind(document);
    document.createElement = (name, ...args) => {
      const element = create(name, ...args);
      if (name === 'canvas' && new Error().stack.includes('renderPDF')) window.ownedCanvases.push(element);
      return element;
    };
    window.revokedURLs = [];
    const revoke = URL.revokeObjectURL.bind(URL);
    URL.revokeObjectURL = url => { window.revokedURLs.push(url); revoke(url); };
    window.mainFileReads = 0;
    const read = File.prototype.arrayBuffer;
    File.prototype.arrayBuffer = function () { window.mainFileReads++; return read.call(this); };
  });

  async function pdfFixture(count = 3, dimensions = [612, 792]) {
    const doc = await PDFDocument.create();
    for (let i = 0; i < count; i++) {
      const page = doc.addPage(dimensions);
      page.drawRectangle({ x: 20, y: 20, width: 200, height: 200, color: rgb(1, 0, 0) });
      page.drawText(`Test page ${i + 1}`, { x: 30, y: 300, size: 20 });
    }
    return Buffer.from(await doc.save());
  }
  const sample = await pdfFixture();
  async function openTool(tool, data = sample, name = 'sample.pdf') {
    await page.goto(`${base}/${tool}.html`);
    await page.locator('#ws-file-input').setInputFiles({ name, mimeType: 'application/octet-stream', buffer: data });
    await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  }
  async function finish() {
    await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled, undefined, { timeout: 30_000 });
    const status = await page.locator('#ws-progress-status').textContent();
    assert.equal(status, 'Processing completed!', status);
    if (!downloads.length) await page.waitForEvent('download');
    const download = downloads.shift();
    assert.equal(await download.failure(), null);
    const data = await readFile(await download.path());
    assert.equal(page.workers().length, 0, 'workers must terminate at the end of a job');
    assert.ok(await page.evaluate(() => window.ownedCanvases.every(canvas => canvas.width === 0 && canvas.height === 0)), 'owned canvases must be released');
    return Buffer.from(data);
  }
  async function processTool(tool, data = sample, name = 'sample.pdf') {
    await openTool(tool, data, name);
    await page.locator('#ws-process-btn').click();
    return finish();
  }

  await page.goto(`${base}/resize-pdf.html`);
  assert.equal(await page.evaluate(async () => {
    const { createEngine } = await import('./processing-client.js');
    const engine = await createEngine();
    const mode = engine.mode;
    engine.close();
    return mode;
  }), 'worker', 'worker startup must not silently fall back');
  console.log('PASS real dedicated-worker startup');

  const resizedBytes = await processTool('resize-pdf', await pdfFixture(25));
  assert.equal(await page.evaluate(() => window.mainFileReads), 0, 'vector inputs should only be read in the worker');
  const resized = await PDFDocument.load(resizedBytes);
  assert.equal(resized.getPageCount(), 25);
  assert.deepEqual(resized.getPage(0).getSize(), { width: 595.28, height: 841.89 });
  const resizedText = await page.evaluate(async bytes => {
    const { runTool } = await import('./processing-client.js');
    const result = await runTool('pdf-to-text', [new File([new Uint8Array(bytes)], 'resized.pdf')]);
    return result.data.text();
  }, Array.from(resizedBytes));
  assert.match(resizedText, /Test page 25/);
  console.log('PASS vector resize, destination references, shared resources and one worker-side read');

  for (const tool of ['grayscale-pdf', 'compress-pdf']) {
    const doc = await PDFDocument.load(await processTool(tool));
    assert.equal(doc.getPageCount(), 3);
    assert.deepEqual(doc.getPage(0).getSize(), { width: 612, height: 792 });
    console.log(`PASS ${tool}, original physical dimensions and canvas/worker cleanup`);
  }
  const huge = await PDFDocument.load(await processTool('grayscale-pdf', await pdfFixture(1, [30000, 30000])));
  assert.equal(huge.getPage(0).getWidth(), 30000);
  console.log('PASS oversized page uses a bounded raster, not a giant canvas');

  for (const tool of ['pdf-to-jpg', 'pdf-to-png', 'pdf-to-powerpoint']) {
    const zip = await JSZip.loadAsync(await processTool(tool));
    if (tool === 'pdf-to-powerpoint') {
      assert.equal(Object.keys(zip.files).filter(name => /^ppt\/slides\/slide\d+\.xml$/.test(name)).length, 3);
      assert.equal(Object.keys(zip.files).filter(name => /ppt\/media\/.*\.jpeg$/.test(name)).length, 3);
    } else assert.equal(Object.keys(zip.files).filter(name => /^page-\d+\./.test(name)).length, 3);
    console.log(`PASS ${tool} output archive and cleanup`);
  }

  const slides = new JSZip();
  for (const number of [10, 1, 2]) slides.file(`ppt/slides/slide${number}.xml`, `<p:sld><a:t>Slide ${number}</a:t></p:sld>`);
  const pptBytes = await slides.generateAsync({ type: 'nodebuffer' });
  const converted = await PDFDocument.load(await processTool('ppt-to-pdf', pptBytes, 'slides.pptx'));
  assert.equal(converted.getPageCount(), 3);
  console.log('PASS worker-side PPTX extraction and PDF serialization');

  const word = new JSZip();
  word.file('[Content_Types].xml', '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>');
  word.file('_rels/.rels', '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>');
  word.file('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>A short Word document for conversion.</w:t></w:r></w:p></w:body></w:document>');
  const wordBytes = await word.generateAsync({ type: 'nodebuffer' });
  const wordPDF = await PDFDocument.load(await processTool('word-to-pdf', wordBytes, 'document.docx'));
  assert.ok(wordPDF.getPageCount() > 0);
  assert.equal(await page.evaluate(() => window.mainFileReads), 0, 'DOCX parsing belongs in the worker');
  assert.equal(await page.locator('.html2pdf__overlay').count(), 0);
  console.log('PASS worker-side DOCX parsing, lower-resolution Word rendering and DOM cleanup');

  await openTool('reorder-pages-pdf');
  await page.locator('#pages-order-input').fill('1,1,3');
  await page.locator('#ws-process-btn').click();
  await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  assert.match(await page.locator('#ws-progress-status').textContent(), /more than once/);
  assert.equal(await page.locator('#direct-dl-link').count(), 0);
  await page.locator('#pages-order-input').fill('3,1,2');
  await page.locator('#ws-process-btn').click();
  assert.equal((await PDFDocument.load(await finish())).getPageCount(), 3);
  assert.equal(await page.locator('#ws-progress-bar').evaluate(bar => bar.style.backgroundColor), '');
  console.log('PASS duplicate order rejected without a bogus download, then successful retry');

  await openTool('grayscale-pdf', await pdfFixture(60));
  await page.locator('#ws-process-btn').click();
  await page.waitForFunction(() => /Processing page \d+\/60/.test(document.getElementById('ws-progress-status').textContent));
  await page.locator('#ws-cancel-btn').click();
  await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  assert.match(await page.locator('#ws-progress-status').textContent(), /cancelled/);
  assert.equal(await page.locator('#direct-dl-link').count(), 0);
  assert.equal(page.workers().length, 0);
  assert.ok(await page.evaluate(() => window.ownedCanvases.every(canvas => canvas.width === 0 && canvas.height === 0)));
  console.log('PASS mid-document cancellation releases workers/canvas and restores controls');

  await openTool('number-pdf-pages');
  await page.evaluate(() => { window.Worker = undefined; });
  await page.locator('#ws-process-btn').click();
  assert.equal((await PDFDocument.load(await finish())).getPageCount(), 3);
  const oldURL = await page.locator('#direct-dl-link').getAttribute('href');
  await page.locator('#ws-process-btn').click();
  await finish();
  assert.ok((await page.evaluate(() => window.revokedURLs)).includes(oldURL));
  const newURL = await page.locator('#direct-dl-link').getAttribute('href');
  await page.evaluate(() => clearWorkspaceFile());
  assert.ok((await page.evaluate(() => window.revokedURLs)).includes(newURL));
  console.log('PASS no-Worker fallback and output URL revocation on replacement/reset');

  await openTool('grayscale-pdf');
  await page.evaluate(() => { window.Worker = class { constructor() { throw new Error('Workers blocked'); } }; });
  await page.locator('#ws-process-btn').click();
  assert.equal((await PDFDocument.load(await finish())).getPageCount(), 3);
  console.log('PASS raster fallback when Worker construction is blocked');

  await openTool('pdf-to-text');
  await page.evaluate(() => { window.Worker = class { constructor() { throw new Error('Workers blocked'); } }; });
  await page.locator('#ws-process-btn').click();
  assert.match((await finish()).toString(), /Test page 3/);
  console.log('PASS PDF text parser fallback without an importScripts-on-main failure');

  word.file('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'
    + '<w:p><w:r><w:t>A paragraph in a very long Word document.</w:t></w:r></w:p>'.repeat(800) + '</w:body></w:document>');
  await openTool('word-to-pdf', await word.generateAsync({ type: 'nodebuffer' }), 'long.docx');
  await page.locator('#ws-process-btn').click();
  await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  assert.match(await page.locator('#ws-progress-status').textContent(), /too long to render safely/);
  assert.equal(await page.locator('.html2pdf__overlay').count(), 0);
  assert.equal(await page.locator('#direct-dl-link').count(), 0);
  console.log('PASS long Word documents are rejected before allocating a giant canvas');

  await openTool('ocr-pdf');
  await page.locator('#ws-process-btn').click();
  await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  assert.match(await page.locator('#ws-progress-status').textContent(), /not implemented/);
  assert.equal(await page.locator('#direct-dl-link').count(), 0);
  assert.equal(await page.evaluate(() => window.mainFileReads), 0);
  console.log('PASS placeholder tools fail honestly without reading/copying the source');

  await page.goto(`${base}/index.html#rotate-pdf`);
  await page.locator('#ws-file-input').setInputFiles({ name: 'sample.pdf', mimeType: 'application/pdf', buffer: sample });
  await page.waitForFunction(() => !document.getElementById('ws-process-btn').disabled);
  await page.locator('#ws-process-btn').click();
  assert.equal((await PDFDocument.load(await finish())).getPage(0).getRotation().angle, 90);
  const spaURL = await page.locator('#direct-dl-link').getAttribute('href');
  await page.evaluate(() => { location.hash = 'split-pdf'; });
  await page.locator('#split-pages-input').waitFor();
  assert.ok((await page.evaluate(() => window.revokedURLs)).includes(spaURL));
  assert.ok(await page.locator('#ws-process-btn').isDisabled());
  console.log('PASS homepage hash-router workflow and navigation cleanup');

  assert.deepEqual(errors, [], `Unexpected browser errors: ${errors.join('\n')}`);
  console.log('All browser integration checks passed.');
} finally {
  await browser?.close();
  await new Promise(resolve => server.close(resolve));
}

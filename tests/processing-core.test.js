import test from 'node:test';
import assert from 'node:assert/strict';
import * as PDFLib from 'pdf-lib';
import JSZip from 'jszip';
import {
  LIMITS, boundedCanvasSize, createProcessor, createProgressReporter,
  parsePageOrder, parsePageRanges, readZipText, sortedSlideNames, validateFiles, validatePageCount
} from '../processing-core.js';

function processor(extra = {}) {
  return createProcessor({ loadLibrary: async name => ({ pdfLib: PDFLib, zip: JSZip })[name], ...extra });
}

async function inputPDF(count = 3, images = false) {
  const doc = await PDFLib.PDFDocument.create();
  const image = images ? await doc.embedPng(Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=', 'base64')) : null;
  for (let i = 0; i < count; i++) {
    const page = doc.addPage([300 + i, 500]);
    page.drawText(`Page ${i + 1}`);
    if (image) page.drawImage(image, { x: 50, y: 50, width: 100, height: 100 });
  }
  const bytes = await doc.save();
  let reads = 0;
  return { name: 'sample.pdf', size: bytes.length, arrayBuffer: async () => { reads++; return bytes.slice().buffer; }, get reads() { return reads; } };
}

async function execute(tool, file, options = {}) {
  const result = await processor().handle('execute', { tool, files: [file], options });
  return { result, doc: await PDFLib.PDFDocument.load(result.data) };
}

test('ranges merge overlaps and reversed intervals into unique sorted pages', () => {
  assert.deepEqual(parsePageRanges('5-3, 1-2, 2-4, 7, 7', 10), [0, 1, 2, 3, 4, 6]);
  assert.equal(parsePageRanges(`1-${LIMITS.maxPages},1-${LIMITS.maxPages}`, LIMITS.maxPages).length, LIMITS.maxPages);
});

test('huge/unsafe ranges are rejected before expansion', () => {
  for (const range of ['1-100000000000', '9007199254740993', '0-100', '1-Infinity', '1,,2', '1.1', '-2']) {
    assert.throws(() => parsePageRanges(range, 100));
  }
  assert.throws(() => parsePageRanges('1'.repeat(LIMITS.maxRangeCharacters + 1), 100), /too long/);
  assert.throws(() => parsePageRanges(Array(LIMITS.maxRangeParts + 1).fill('1').join(','), 100), /too many/);
  assert.throws(() => parsePageRanges('', 100), /at least/);
  assert.throws(() => parsePageRanges('1', Infinity));
});

test('page order rejects duplicates even when the length is correct', () => {
  assert.deepEqual(parsePageOrder('3, 1, 2', 3), [2, 0, 1]);
  assert.throws(() => parsePageOrder('1,1,3', 3), /more than once/);
  assert.throws(() => parsePageOrder('1,1,not-a-number', 3), /more than once/);
  assert.throws(() => parsePageOrder('1,2', 3), /all 3 pages/);
  assert.throws(() => parsePageOrder('1,2,4', 3), /out of range/);
  assert.throws(() => parsePageOrder('1,2,', 3), /valid page/);
});

test('file, total-input and page limits are enforced', () => {
  assert.throws(() => validateFiles([]), /select/);
  assert.throws(() => validateFiles([{ size: 0 }]), /Empty/);
  assert.throws(() => validateFiles([{ size: LIMITS.maxFileBytes + 1 }]), /100 MB/);
  assert.throws(() => validateFiles(Array(3).fill({ size: LIMITS.maxFileBytes })), /total 200 MB/);
  assert.throws(() => validateFiles(Array(LIMITS.maxFiles + 1).fill({ size: 1 })), /at most/);
  assert.throws(() => validateFiles([{ size: LIMITS.maxWordFileBytes + 1 }], 'word-to-pdf'), /20 MB/);
  assert.throws(() => validatePageCount(LIMITS.maxRasterPages + 1, true), /200 pages/);
  assert.throws(() => validatePageCount(LIMITS.maxPages + 1), /2000 pages/);
  validateFiles([{ size: LIMITS.maxFileBytes }]);
});

test('oversized files are rejected before reading or loading a library', async () => {
  let reads = 0;
  const engine = createProcessor({ loadLibrary: async () => { throw new Error('should not load'); } });
  await assert.rejects(engine.handle('execute', { tool: 'resize-pdf', files: [{ size: LIMITS.maxFileBytes + 1, arrayBuffer: () => { reads++; } }] }), /100 MB/);
  assert.equal(reads, 0);
});

test('raster dimensions bound both area and longest edge, without upscaling extra', () => {
  for (const [w, h] of [[612, 792], [30000, 30000], [1000000, 2], [2, 1000000], [1e200, 1e200]]) {
    const size = boundedCanvasSize(w, h, 1.5);
    assert.ok(size.scale <= 1.5);
    assert.ok(size.width * size.height <= LIMITS.maxCanvasPixels);
    assert.ok(size.width <= LIMITS.maxCanvasDimension && size.height <= LIMITS.maxCanvasDimension);
    assert.ok(size.width > 0 && size.height > 0);
  }
  for (const dim of [0, -1, Infinity, NaN]) assert.throws(() => boundedCanvasSize(dim, 100));
});

test('slide names sort numerically, ignoring unrelated entries', () => {
  assert.deepEqual(sortedSlideNames(['ppt/slides/slide10.xml', 'ppt/slides/slide2.xml', 'ppt/slides/_rels/slide1.xml.rels', 'ppt/slides/slide1.xml']), ['ppt/slides/slide1.xml', 'ppt/slides/slide2.xml', 'ppt/slides/slide10.xml']);
});

test('worker progress is throttled, with completion never dropped', () => {
  const calls = [];
  let time = 0;
  const report = createProgressReporter((...args) => calls.push(args), () => time);
  report(10.1, 'Reading');
  for (let i = 0; i < 100; i++) report(20, `Page ${i}`);
  time = 100;
  report(30, 'Writing');
  report(100, 'Done');
  report(100, 'Done');
  assert.deepEqual(calls, [[10, 'Reading'], [30, 'Writing'], [100, 'Done']]);
});

test('decompression is streamed and stopped at a byte limit', async () => {
  const zip = new JSZip();
  zip.file('large.xml', 'x'.repeat(500000));
  const loaded = await JSZip.loadAsync(await zip.generateAsync({ type: 'uint8array', compression: 'DEFLATE' }));
  await assert.rejects(readZipText(loaded.file('large.xml'), 1024), /decompression limit/);
  zip.file('utf8.xml', '<a:t>é &amp; test</a:t>');
  const result = await readZipText(zip.file('utf8.xml'));
  assert.equal(result.text, '<a:t>é &amp; test</a:t>');
  assert.equal(result.size, new TextEncoder().encode(result.text).length);
});

test('resize reads once, embeds valid destination resources and preserves shared images across batches', async () => {
  const file = await inputPDF(25, true);
  const { doc } = await execute('resize-pdf', file, { format: 'letter' });
  assert.equal(file.reads, 1);
  assert.equal(doc.getPageCount(), 25);
  for (const page of doc.getPages()) {
    assert.deepEqual(page.getSize(), { width: 612, height: 792 });
    const xobjects = page.node.Resources().lookup(PDFLib.PDFName.of('XObject'), PDFLib.PDFDict);
    assert.ok(xobjects.entries().length > 0);
    for (const [, ref] of xobjects.entries()) assert.ok(doc.context.lookup(ref) instanceof PDFLib.PDFRawStream);
  }
  const imageObjects = doc.context.enumerateIndirectObjects().filter(([, value]) => value instanceof PDFLib.PDFRawStream && value.dict.get(PDFLib.PDFName.of('Subtype')) === PDFLib.PDFName.of('Image'));
  assert.equal(imageObjects.length, 1, 'shared images must not be duplicated per batch');
});

test('split/extract/reorder/delete operate on valid unique selections', async () => {
  const file = await inputPDF();
  for (const tool of ['split-pdf', 'extract-pages-pdf']) {
    const { doc } = await execute(tool, file, { range: '3,1,1' });
    assert.deepEqual(doc.getPages().map(page => page.getWidth()), [300, 302]);
  }
  const { doc: reordered } = await execute('reorder-pages-pdf', file, { order: '3,1,2' });
  assert.deepEqual(reordered.getPages().map(page => page.getWidth()), [302, 300, 301]);
  const { doc: deleted } = await execute('delete-pdf-pages', file, { range: '2' });
  assert.deepEqual(deleted.getPages().map(page => page.getWidth()), [300, 302]);
  await assert.rejects(execute('reorder-pages-pdf', file, { order: '1,1,3' }), /more than once/);
  await assert.rejects(execute('delete-pdf-pages', file, { range: '1-3' }), /every page/);
});

test('vector editing and fallback loops yield so timers can run', async () => {
  const file = await inputPDF(35);
  let ticks = 0;
  const timer = setInterval(() => ticks++, 0);
  try {
    for (const [tool, options] of [
      ['rotate-pdf', { angle: 180 }], ['add-watermark-pdf', { text: 'DRAFT' }],
      ['number-pdf-pages', { position: 'bottom-right' }], ['crop-pdf', { left: 10 }]
    ]) {
      const { doc } = await execute(tool, file, options);
      assert.equal(doc.getPageCount(), 35);
      if (tool === 'rotate-pdf') assert.equal(doc.getPage(0).getRotation().angle, 180);
      if (tool === 'crop-pdf') assert.equal(doc.getPage(0).getCropBox().width, 270);
    }
  } finally { clearInterval(timer); }
  assert.ok(ticks >= 4);
});

test('flatten removes fields and uses object streams', async () => {
  const source = await PDFLib.PDFDocument.create();
  const page = source.addPage();
  const field = source.getForm().createTextField('name');
  field.setText('Test');
  field.addToPage(page);
  const data = await source.save();
  const { doc, result } = await execute('flatten-pdf', new File([data], 'form.pdf'));
  assert.equal(doc.getForm().getFields().length, 0);
  assert.match(new TextDecoder().decode(result.data), /\/Type \/ObjStm/);
});

test('PPTX conversion uses numeric slide order and rejects excessive XML', async () => {
  const zip = new JSZip();
  for (const number of [10, 2, 1]) zip.file(`ppt/slides/slide${number}.xml`, `<p:sld><a:t>Slide ${number}</a:t></p:sld>`);
  const data = await zip.generateAsync({ type: 'uint8array' });
  const { doc } = await execute('ppt-to-pdf', new File([data], 'slides.pptx'));
  assert.equal(doc.getPageCount(), 3);
  zip.file('ppt/slides/slide1.xml', 'x'.repeat(LIMITS.maxSlideXmlBytes + 1));
  const bomb = await zip.generateAsync({ type: 'uint8array', compression: 'DEFLATE' });
  await assert.rejects(execute('ppt-to-pdf', new File([bomb], 'large.pptx')), /decompression limit/);
});

test('grayscale preserves alpha and rejects oversized buffers', async () => {
  const engine = processor();
  const { pixels } = await engine.handle('grayscale', { pixels: new Uint8ClampedArray([255, 0, 0, 123, 0, 255, 0, 255]).buffer });
  assert.deepEqual([...new Uint8Array(pixels)], [87, 87, 87, 123, 128, 128, 128, 255]);
  await assert.rejects(engine.handle('grayscale', { pixels: new ArrayBuffer(LIMITS.maxCanvasPixels * 4 + 4) }), /safety limit/);
});

test('raster page and cumulative asset limits reject before serialization', async () => {
  const engine = processor();
  await assert.rejects(engine.handle('startRaster', { tool: 'grayscale-pdf', total: LIMITS.maxRasterPages + 1 }), /200 pages/);
  await engine.handle('startRaster', { tool: 'pdf-to-png', total: 1, filename: 'images.zip' });
  await assert.rejects(engine.handle('finishRaster'), /Not all pages/);
  await assert.rejects(engine.handle('addRasterPage', { data: new ArrayBuffer(LIMITS.maxRasterBytes + 1), width: 10, height: 10 }), /100 MB/);
  engine.dispose();
});


test('resize also handles genuinely blank pages without content streams', async () => {
  const source = await PDFLib.PDFDocument.create();
  source.addPage([300, 500]);
  const file = new File([await source.save()], 'blank.pdf');
  const { doc } = await execute('resize-pdf', file);
  assert.equal(doc.getPageCount(), 1);
  assert.deepEqual(doc.getPage(0).getSize(), { width: 595.28, height: 841.89 });
});

test('merge preserves page order and shares resources within each source', async () => {
  const source = await inputPDF(25, true);
  const result = await processor().handle('execute', { tool: 'merge-pdf', files: [source, await inputPDF(2)] });
  const doc = await PDFLib.PDFDocument.load(result.data);
  assert.equal(doc.getPageCount(), 27);
  assert.equal(doc.getPage(24).getWidth(), 324);
  assert.equal(doc.getPage(25).getWidth(), 300);
  const images = doc.context.enumerateIndirectObjects().filter(([, value]) => value instanceof PDFLib.PDFRawStream && value.dict.get(PDFLib.PDFName.of('Subtype')) === PDFLib.PDFName.of('Image'));
  assert.equal(images.length, 1);
});


test('Word HTML is bounded before it can be cloned to the UI thread', async () => {
  const engine = createProcessor({ loadLibrary: async () => ({ convertToHtml: async () => ({ value: 'x'.repeat(LIMITS.maxWordHtmlCharacters + 1) }) }) });
  await assert.rejects(engine.handle('wordToHTML', { file: new File(['docx'], 'large.docx') }), /Word content is too large/);
});


test('upstream A4 image layout is preserved by the worker engine', async () => {
  const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=', 'base64');
  const { doc, result } = await execute('png-to-pdf', new File([png], 'image.png'), { pageSize: 'a4' });
  assert.deepEqual(doc.getPage(0).getSize(), { width: 595.28, height: 841.89 });
  assert.match(result.note, /A4/);
});

test('upstream archival prep retains its metadata and certification caveat', async () => {
  const { doc, result } = await execute('pdf-to-pdfa', await inputPDF());
  assert.equal(doc.getSubject(), 'Prepared for long-term archiving');
  assert.match(result.note, /not a certified PDF\/A conversion/);
});

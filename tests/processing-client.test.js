import test from 'node:test';
import assert from 'node:assert/strict';
import { createEngine, runTool } from '../processing-client.js';
import { LIMITS } from '../processing-core.js';

function replaceGlobals(t, values) {
  const previous = new Map(Object.keys(values).map(key => [key, Object.getOwnPropertyDescriptor(globalThis, key)]));
  Object.assign(globalThis, values);
  t.after(() => {
    for (const [key, descriptor] of previous) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor);
      else delete globalThis[key];
    }
  });
}

test('worker calls clone File objects and explicitly transfer owned buffers', async t => {
  let instance;
  class FakeWorker {
    constructor() { instance = this; queueMicrotask(() => this.onmessage({ data: { type: 'ready' } })); }
    postMessage(message, transfer) {
      this.message = message;
      this.transfer = transfer;
      queueMicrotask(() => this.onmessage({ data: { type: 'result', id: message.id, result: 'ok' } }));
    }
    terminate() { this.terminated = true; }
  }
  replaceGlobals(t, { Worker: FakeWorker });
  const engine = await createEngine();
  assert.equal(engine.mode, 'worker');
  const file = new File(['test'], 'test.pdf');
  file.arrayBuffer = () => { throw new Error('must not read on main thread'); };
  assert.equal(await engine.call('execute', { files: [file] }), 'ok');
  assert.equal(instance.message.payload.files[0], file);
  const pixels = new ArrayBuffer(4);
  await engine.call('grayscale', { pixels }, [pixels]);
  assert.deepEqual(instance.transfer, [pixels]);
  engine.close();
  assert.equal(instance.terminated, true);
});

test('abort terminates worker and rejects pending work', async t => {
  let terminated = false;
  class FakeWorker {
    constructor() { queueMicrotask(() => this.onmessage({ data: { type: 'ready' } })); }
    postMessage() {}
    terminate() { terminated = true; }
  }
  replaceGlobals(t, { Worker: FakeWorker });
  const controller = new AbortController();
  const engine = await createEngine({ signal: controller.signal });
  const request = engine.call('execute', {});
  controller.abort();
  await assert.rejects(request, { name: 'AbortError' });
  assert.equal(terminated, true);
});

test('a worker runtime failure does not replay work on the main thread', async t => {
  let starts = 0;
  let terminated = false;
  class FakeWorker {
    constructor() { starts++; queueMicrotask(() => this.onmessage({ data: { type: 'ready' } })); }
    postMessage() { queueMicrotask(() => this.onerror({ message: 'Worker crashed', preventDefault() {} })); }
    terminate() { terminated = true; }
  }
  replaceGlobals(t, { Worker: FakeWorker });
  const engine = await createEngine();
  await assert.rejects(engine.call('execute', {}), /Worker crashed/);
  assert.equal(starts, 1);
  assert.equal(terminated, true);
});

test('worker construction and bootstrap errors use the cooperative fallback', async t => {
  replaceGlobals(t, { Worker: class { constructor() { throw new Error('blocked by policy'); } } });
  let engine = await createEngine();
  assert.equal(engine.mode, 'cooperative');
  engine.close();
  let terminated = false;
  globalThis.Worker = class {
    constructor() { queueMicrotask(() => this.onmessage({ data: { type: 'startup-error', message: 'not supported' } })); }
    terminate() { terminated = true; }
  };
  engine = await createEngine();
  assert.equal(engine.mode, 'cooperative');
  assert.equal(terminated, true);
  engine.close();
});

function rasterMocks(t, { pages = 3, failure, encodeFailure = false, resultSize = 3 } = {}) {
  const events = [];
  const canvases = [];
  const output = {
    embedJpg: async () => ({ embed: async () => {} }),
    addPage: dimensions => { events.push(['output-page', dimensions]); return { drawImage() {} }; },
    flush: async () => {},
    save: async () => { events.push('save'); return new Uint8Array(resultSize); }
  };
  const task = {
    destroy: async () => { events.push('destroy'); },
    promise: Promise.resolve({
      numPages: pages,
      getPage: async index => ({
        getViewport: ({ scale }) => ({ width: 612 * scale, height: 792 * scale }),
        render: () => ({ promise: failure && index === 2 ? Promise.reject(new Error('render failed')) : Promise.resolve() }),
        cleanup: () => events.push(`cleanup-${index}`)
      })
    })
  };
  replaceGlobals(t, {
    Worker: undefined,
    PDFLib: { PDFDocument: { create: async () => output } },
    pdfjsLib: { version: '3.11.174', GlobalWorkerOptions: {}, getDocument: () => task },
    document: {
      createElement: tag => {
        assert.equal(tag, 'canvas');
        const canvas = {
          width: 0, height: 0, getContext: () => ({}),
          toBlob: callback => callback(encodeFailure ? null : new Blob(['jpeg']))
        };
        canvases.push(canvas);
        return canvas;
      }
    }
  });
  return { events, canvases };
}

test('raster work is incremental, reuses a canvas, and destroys the source before saving', async t => {
  const { events, canvases } = rasterMocks(t);
  const result = await runTool('compress-pdf', [new File(['input'], 'sample.pdf')]);
  assert.equal(result.filename, 'compressed.pdf');
  assert.equal(canvases.length, 1);
  assert.equal(canvases[0].width, 0);
  assert.equal(canvases[0].height, 0);
  assert.deepEqual(events.filter(event => typeof event === 'string'), ['cleanup-1', 'cleanup-2', 'cleanup-3', 'destroy', 'save']);
  assert.deepEqual(events.filter(Array.isArray).map(event => event[1]), [[612, 792], [612, 792], [612, 792]]);
});

test('a rendering error cleans canvas/page/document and never serializes partial output', async t => {
  const { events, canvases } = rasterMocks(t, { failure: true });
  await assert.rejects(runTool('compress-pdf', [new File(['input'], 'sample.pdf')]), /render failed/);
  assert.equal(canvases[0].width, 0);
  assert.deepEqual(events.filter(event => typeof event === 'string'), ['cleanup-1', 'cleanup-2', 'destroy']);
});

test('an encoding error still destroys the PDF and canvas', async t => {
  const { events, canvases } = rasterMocks(t, { encodeFailure: true });
  await assert.rejects(runTool('compress-pdf', [new File(['input'], 'sample.pdf')]), /could not be encoded/);
  assert.equal(canvases[0].height, 0);
  assert.ok(events.includes('destroy'));
  assert.ok(!events.includes('save'));
});

test('raster page limit rejects before any page is rendered', async t => {
  const { events, canvases } = rasterMocks(t, { pages: LIMITS.maxRasterPages + 1 });
  await assert.rejects(runTool('compress-pdf', [new File(['input'], 'sample.pdf')]), /at most 200/);
  assert.deepEqual(events, ['destroy']);
  assert.equal(canvases[0].width, 0);
});

test('placeholder tools reject immediately, without reading the input', async () => {
  let reads = 0;
  const file = { name: 'sample.pdf', size: 10, arrayBuffer: () => { reads++; } };
  await assert.rejects(runTool('protect-pdf', [file]), /not implemented/);
  assert.equal(reads, 0);
});


test('cancellation remains responsive while a main-thread library download is stalled', { timeout: 1000 }, async t => {
  let script;
  replaceGlobals(t, {
    html2pdf: undefined,
    document: { createElement: () => ({ remove() {} }), head: { appendChild: element => { script = element; } } }
  });
  const controller = new AbortController();
  const job = runTool('word-to-pdf', [new File(['docx'], 'document.docx')], {}, { signal: controller.signal });
  assert.ok(script, 'the library request has started');
  controller.abort();
  await assert.rejects(job, { name: 'AbortError' });
  // Finish the outstanding request so the shared loader cache does not stay pending.
  script.onerror();
});


test('target compression reuses one parsed input across quality-search passes', async t => {
  const { events, canvases } = rasterMocks(t);
  let reads = 0;
  const file = { name: 'sample.pdf', size: 10, arrayBuffer: async () => { reads++; return new ArrayBuffer(10); } };
  const result = await runTool('compress-pdf', [file], { targetKB: 1 });
  assert.equal(reads, 1);
  assert.equal(canvases.length, 1);
  assert.equal(events.filter(event => event === 'destroy').length, 1);
  assert.equal(events.filter(event => event === 'save').length, 5);
  assert.match(result.note, /Target.*reached/);
});

test('unreachable compression targets return an honest bounded best-effort result', async t => {
  const { events } = rasterMocks(t, { resultSize: 2048 });
  const result = await runTool('compress-pdf', [new File(['pdf'], 'file.pdf')], { targetKB: 1 });
  assert.match(result.note, /Target not reached/);
  assert.equal(events.filter(event => event === 'save').length, 4);
  assert.equal(events.filter(event => event === 'destroy').length, 1);
});

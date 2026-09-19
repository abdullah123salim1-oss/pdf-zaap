import test from 'node:test';
import assert from 'node:assert/strict';
import { runTool } from '../processing-client.js';

test('Word rendering errors release the canvas, overlay and newly cloned document', async t => {
  const originals = new Map(['Worker', 'mammoth', 'html2pdf', 'document'].map(key => [key, Object.getOwnPropertyDescriptor(globalThis, key)]));
  t.after(() => {
    for (const [key, descriptor] of originals) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor);
      else delete globalThis[key];
    }
  });
  const existing = { removed: false, remove() { this.removed = true; } };
  const leaked = { removed: false, remove() { this.removed = true; } };
  const clones = [existing];
  const element = { style: {}, replaceChildren() { this.cleared = true; } };
  const canvas = { width: 1000, height: 2000 };
  const overlay = { remove() { this.removed = true; } };
  const container = {
    scrollWidth: 500, scrollHeight: 1000,
    getBoundingClientRect: () => ({ width: 500, height: 1000 }),
    querySelectorAll: () => []
  };
  const renderer = {
    prop: { canvas, overlay },
    from() { return this; },
    set() { return this; },
    toContainer: async () => { clones.push(leaked); },
    get: async () => container,
    toCanvas: async () => { throw new Error('Renderer failed'); }
  };
  globalThis.Worker = undefined;
  globalThis.document = { createElement: () => element, querySelectorAll: () => clones };
  globalThis.mammoth = { convertToHtml: async () => ({ value: '<p>Word content</p>' }) };
  globalThis.html2pdf = () => renderer;
  await assert.rejects(runTool('word-to-pdf', [new File(['docx'], 'document.docx')]), /Renderer failed/);
  assert.equal(canvas.width, 0);
  assert.equal(canvas.height, 0);
  assert.equal(overlay.removed, true);
  assert.equal(leaked.removed, true);
  assert.equal(existing.removed, false, 'do not remove a pre-existing unrelated clone');
  assert.equal(element.cleared, true);
});

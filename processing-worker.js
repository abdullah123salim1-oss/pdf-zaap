// Classic worker: importScripts supports the site's pinned UMD library bundles.
// The shared core is an ES module so it is also directly testable without a DOM.
let processor;
let queue = Promise.resolve();

const ready = import('./processing-core.js').then(({ createProcessor, LIBRARIES }) => {
  processor = createProcessor({
    cooperative: false,
    loadLibrary: async name => {
      const library = LIBRARIES[name];
      if (!self[library.global] && !(library.alias && self[library.alias])) importScripts(library.url);
      const value = self[library.global] || self[library.alias];
      if (!value) throw new Error('A conversion library could not be loaded. Please refresh and try again.');
      return value;
    },
    onProgress: (percent, text) => self.postMessage({ type: 'progress', percent, text })
  });
  self.postMessage({ type: 'ready' });
}).catch(error => {
  self.postMessage({ type: 'startup-error', message: error.message });
});

self.onmessage = ({ data: { id, command, payload } }) => {
  queue = queue.then(async () => {
    await ready;
    try {
      if (!processor) throw new Error('The processing worker could not start.');
      const result = await processor.handle(command, payload);
      const transfer = new Set();
      for (const value of [result?.data, result?.pixels]) {
        if (value instanceof ArrayBuffer) transfer.add(value);
        else if (ArrayBuffer.isView(value)) transfer.add(value.buffer);
      }
      self.postMessage({ type: 'result', id, result }, [...transfer]);
    } catch (error) {
      processor?.dispose();
      self.postMessage({ type: 'error', id, message: error.message || String(error) });
    }
  });
};

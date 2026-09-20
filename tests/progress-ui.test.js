import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

function ui() {
  let time = 0;
  let writes = 0;
  let width = '';
  let text = '';
  let timerId = 0;
  const timers = new Map();
  const bar = { style: { get width() { return width; }, set width(value) { writes++; width = value; } } };
  const status = { get textContent() { return text; }, set textContent(value) { writes++; text = value; } };
  const context = vm.createContext({
    window: { addEventListener() {} },
    document: { getElementById: id => id === 'ws-progress-bar' ? bar : id === 'ws-progress-status' ? status : null },
    performance: { now: () => time },
    setTimeout: callback => { timers.set(++timerId, callback); return timerId; },
    clearTimeout: id => timers.delete(id)
  });
  vm.runInContext(readFileSync(new URL('../script.js', import.meta.url), 'utf8'), context);
  return {
    run: source => vm.runInContext(source, context),
    get width() { return width; }, get text() { return text; }, get writes() { return writes; }, get pending() { return timers.size; },
    tick: () => { time += 100; for (const callback of [...timers.values()]) callback(); }
  };
}

test('hundreds of progress updates coalesce to one trailing DOM update', () => {
  const app = ui();
  app.run("setProgressUI(10, 'Starting'); for(let i=0;i<1000;i++) setProgressUI(20, 'Page ' + i);");
  assert.equal(app.writes, 2);
  assert.equal(app.pending, 1);
  app.tick();
  assert.equal(app.writes, 4);
  assert.equal(app.text, 'Page 999');
  assert.equal(app.width, '20%');
  assert.equal(app.pending, 0);
});

test('completion and errors cannot be overwritten by stale progress', () => {
  const app = ui();
  app.run("setProgressUI(10, 'Starting'); setProgressUI(60, 'Old status'); setProgressUI(100, 'Done');");
  app.tick();
  assert.equal(app.text, 'Done');
  assert.equal(app.width, '100%');
  app.run("setProgressUI(75, 'Pending'); setProgressUI(0, 'Error: invalid document', true);");
  app.tick();
  assert.equal(app.text, 'Error: invalid document');
  assert.equal(app.pending, 0);
});

test('reset discards pending updates and repeated values do not rewrite DOM', () => {
  const app = ui();
  app.run("setProgressUI(10, 'Starting'); setProgressUI(10, 'Starting');");
  app.tick();
  assert.equal(app.writes, 2);
  app.run("setProgressUI(70, 'Pending'); resetProgressUI();");
  app.tick();
  assert.equal(app.text, 'Starting');
  assert.equal(app.pending, 0);
});

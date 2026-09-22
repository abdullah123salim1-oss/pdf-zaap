// Accessibility gate: runs axe-core over every static page inside jsdom.
//
// Lighthouse scores its Accessibility category from axe rule results, so a page
// with zero axe violations is the precondition for 100. Rules that need real
// layout or paint (color-contrast, target-size) cannot be evaluated by jsdom and
// are reported as "incomplete" — see tests/audit-a11y.mjs notes and
// scripts/lighthouse-report.mjs for measuring those in a real browser.
//
// Usage: node tests/audit-a11y.mjs [rootDir]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { JSDOM } from 'jsdom';
import axe from 'axe-core';

const ROOT = process.argv[2] || path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SKIP = new Set(['node_modules', '.git', '.cache', 'scripts']);
const ORIGIN = 'https://www.pdfzaap.online';

function pages(dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP.has(entry.name) || entry.name.startsWith('.')) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...pages(full));
    else if (entry.name.endsWith('.html')) out.push(full);
  }
  return out.sort();
}

const violations = [];
const incomplete = new Map();
let audited = 0;

for (const file of pages(ROOT)) {
  const rel = path.relative(ROOT, file).split(path.sep).join('/');
  const urlPath = '/' + rel.replace(/index\.html$/, '');
  const dom = new JSDOM(fs.readFileSync(file, 'utf8'), {
    runScripts: 'outside-only',
    pretendToBeVisual: true,
    url: ORIGIN + urlPath,
  });
  dom.window.eval(axe.source);
  let result;
  try {
    result = await dom.window.axe.run(dom.window.document, {
      resultTypes: ['violations', 'incomplete'],
      runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice'] },
    });
  } finally {
    dom.window.close();
  }
  audited++;
  for (const v of result.violations) {
    for (const node of v.nodes) {
      violations.push({ rule: v.id, impact: v.impact, help: v.help, file: rel, target: node.target.join(' ') });
    }
  }
  for (const item of result.incomplete) {
    const key = item.id;
    incomplete.set(key, (incomplete.get(key) || 0) + item.nodes.length);
  }
}

console.log(`axe-core ${axe.version} — audited ${audited} pages`);
for (const [rule, count] of [...incomplete].sort()) {
  console.log(`  not evaluable in jsdom (needs a browser): ${rule} (${count} node(s))`);
}

if (!violations.length) {
  console.log('PASS: 0 accessibility violations');
  process.exit(0);
}

const byRule = new Map();
for (const v of violations) {
  if (!byRule.has(v.rule)) byRule.set(v.rule, { ...v, count: 0, files: new Set() });
  const entry = byRule.get(v.rule);
  entry.count++;
  entry.files.add(v.file);
}
for (const [, entry] of [...byRule].sort((a, b) => b.count - a.count)) {
  console.log(`FAIL [${entry.impact}] ${entry.rule}: ${entry.count} node(s) across ${entry.files.size} page(s) — ${entry.help}`);
  for (const v of violations.filter((x) => x.rule === entry.rule).slice(0, 3)) {
    console.log(`        ${v.file} ${v.target}`);
  }
}
console.log(`\n${violations.length} violation(s) across ${audited} page(s)`);
process.exit(1);

// Real Lighthouse run — this is the only way to measure the four category
// scores, because Accessibility's color-contrast/target-size rules and the whole
// Performance category (FCP, LCP, TBT, CLS, Speed Index) need a real browser.
//
// The sandbox/CI image used for this repo has no Chrome and no apt or browser
// CDN access, so this script is meant for a machine that has Chrome:
//
//   npm ci
//   npm i --no-save lighthouse@12 chrome-launcher
//   npm run lighthouse                       # local static server (http)
//   npm run lighthouse -- --url https://www.pdfzaap.online/   # live origin
//
// A local http:// run will report is-on-https/redirects-http as failing in
// Best Practices — that is an artefact of localhost, not of the site.
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const args = process.argv.slice(2);
const urlFlag = args.indexOf('--url');
const explicitUrl = urlFlag >= 0 ? args[urlFlag + 1] : '';

const PAGES = [
  '/',
  '/compress-pdf.html',
  '/merge-pdf.html',
  '/jpg-to-pdf.html',
  '/pdf-to-word.html',
  '/blog/',
];

const root = fileURLToPath(new URL('../', import.meta.url));
const server = createServer(async (request, response) => {
  const name = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
  const filename = path.resolve(root, '.' + (name.endsWith('/') ? name + 'index.html' : name));
  if (!filename.startsWith(root) || name.includes('/.git')) { response.writeHead(403).end(); return; }
  try {
    const data = await readFile(filename);
    const type = { '.js': 'text/javascript', '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.png': 'image/png', '.ico': 'image/x-icon', '.xml': 'application/xml', '.txt': 'text/plain' }[path.extname(filename)] || 'application/octet-stream';
    response.writeHead(200, { 'Content-Type': type }).end(data);
  } catch { response.writeHead(404).end(); }
});

let base = explicitUrl.replace(/\/$/, '');
if (!base) {
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  base = `http://127.0.0.1:${server.address().port}`;
}

const { default: lighthouse } = await import('lighthouse');
const { launch } = await import('chrome-launcher');
const chrome = await launch({ chromeFlags: ['--headless=new', '--no-sandbox', '--disable-dev-shm-usage'] });

const CATEGORIES = ['performance', 'accessibility', 'best-practices', 'seo'];
const failures = [];

console.log(`Lighthouse against ${base}\n`);
for (const page of PAGES) {
  const target = base + page;
  const result = await lighthouse(target, {
    port: chrome.port,
    output: 'json',
    onlyCategories: CATEGORIES,
    logLevel: 'error',
  });
  if (!result?.lhr) { console.log(`${page.padEnd(34)} RUN FAILED`); failures.push(page); continue; }
  const scores = CATEGORIES.map((id) => {
    const category = result.lhr.categories[id];
    return `${id}=${category.score === null ? 'n/a' : Math.round(category.score * 100)}`;
  });
  const line = `${page.padEnd(34)} ${scores.join('  ')}`;
  console.log(line);
  for (const id of CATEGORIES) {
    const category = result.lhr.categories[id];
    if (category.score !== null && category.score < 1) {
      for (const ref of category.auditRefs) {
        const audit = result.lhr.audits[ref.id];
        if (audit && ref.weight > 0 && audit.score !== null && audit.score < 1) {
          failures.push(`${page} ${id}/${ref.id}: ${audit.title}`);
        }
      }
    }
  }
}

await chrome.kill();
server.close();

console.log('');
if (!failures.length) {
  console.log('PASS: every category scored 100 on every audited page');
  process.exit(0);
}
console.log('Failing weighted audits:');
for (const f of failures) console.log('  ' + f);
process.exit(1);

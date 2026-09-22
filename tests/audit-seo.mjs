// SEO / Best-Practices gate for the statically checkable Lighthouse 12 audits.
//
// Audit list mirrors node_modules/lighthouse/core/config/default-config.js:
//   seo:            is-crawlable, document-title, meta-description, link-text,
//                   crawlable-anchors, image-alt, hreflang, canonical
//   best-practices: viewport, font-size, doctype, charset
// Audits that need a live origin or a real browser (http-status-code,
// robots-txt, is-on-https, redirects-http, errors-in-console, inspector-issues)
// are reported as unchecked — see scripts/lighthouse-report.mjs.
//
// Usage: node tests/audit-seo.mjs [rootDir]
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = process.argv[2] || path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SKIP = new Set(['node_modules', '.git', '.cache', 'scripts']);
const BASE = 'https://www.pdfzaap.online';
// Lighthouse's hreflang audit accepts 'x-default' (NO_LANGUAGE) and validates
// only the language subtag with axe's isValidLang.
const NO_LANGUAGE = 'x-default';
const VALID_LANGS = new Set(['en', 'id', 'ur']);
const GENERIC_LINK_TEXT = new Set([
  'click here', 'here', 'more', 'link', 'this', 'read more', 'learn more',
  'start here', 'klik di sini', 'sini', 'detail', 'details', 'more info',
]);

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

const problems = [];
const add = (audit, page, msg) => problems.push({ audit, page, msg });
let checked = 0;

for (const file of pages(ROOT)) {
  const rel = path.relative(ROOT, file).split(path.sep).join('/');
  const html = fs.readFileSync(file, 'utf8');
  checked++;

  // document-title
  const titles = [...html.matchAll(/<title[^>]*>([\s\S]*?)<\/title>/g)];
  if (!titles.length || !titles[0][1].trim()) add('document-title', rel, 'missing/empty <title>');
  else if (titles.length > 1) add('document-title', rel, `${titles.length} <title> elements`);
  else if (titles[0][1].trim().length > 70) add('document-title', rel, `title is ${titles[0][1].trim().length} chars (>70 truncates in SERPs)`);

  // meta-description
  const desc = html.match(/<meta\s+name="description"\s+content="([^"]*)"/);
  if (!desc || !desc[1].trim()) add('meta-description', rel, 'missing/empty meta description');
  else if (desc[1].length > 300) add('meta-description', rel, `description is ${desc[1].length} chars (>300)`);

  // canonical
  const canonicals = [...html.matchAll(/<link\s+rel="canonical"\s+href="([^"]*)"/g)].map((m) => m[1]);
  const expected = BASE + '/' + (rel.endsWith('index.html') ? rel.slice(0, -'index.html'.length) : rel);
  if (canonicals.length !== 1) add('canonical', rel, `${canonicals.length} canonical link(s)`);
  else if (canonicals[0] !== expected) add('canonical', rel, `canonical "${canonicals[0]}" != page URL "${expected}"`);

  // is-crawlable — 404.html is intentionally noindex and is absent from sitemap.xml
  for (const m of html.matchAll(/<meta\s+name="robots"\s+content="([^"]*)"/g)) {
    if (/noindex/i.test(m[1]) && rel !== '404.html') add('is-crawlable', rel, `meta robots blocks indexing: ${m[1]}`);
  }

  // hreflang
  for (const m of html.matchAll(/<link\s+rel="alternate"[^>]*>/g)) {
    const tag = m[0];
    const code = tag.match(/hreflang="([^"]*)"/);
    const href = tag.match(/href="([^"]*)"/);
    if (code) {
      const value = code[1];
      const primary = value.split('-')[0].toLowerCase();
      if (value.toLowerCase() !== NO_LANGUAGE && !VALID_LANGS.has(primary)) {
        add('hreflang', rel, `invalid hreflang "${value}"`);
      }
    }
    if (href && !/^https?:/.test(href[1])) add('hreflang', rel, `hreflang href not fully qualified: ${href[1]}`);
  }

  // image-alt
  for (const m of html.matchAll(/<img\b[^>]*>/g)) {
    if (!/\balt=/.test(m[0])) add('image-alt', rel, m[0].slice(0, 100));
  }

  // crawlable-anchors
  const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map((m) => m[1]));
  for (const m of html.matchAll(/<a\b[^>]*\shref="#([^"]*)"/g)) {
    if (m[1] && !ids.has(m[1])) add('crawlable-anchors', rel, `href="#${m[1]}" has no matching id`);
  }

  // link-text
  for (const m of html.matchAll(/<a\b[^>]*\shref="(?!mailto:|#|tel:)([^"]*)"[^>]*>([\s\S]*?)<\/a>/g)) {
    const text = m[2].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').replace(/➔/g, '').trim().toLowerCase();
    if (GENERIC_LINK_TEXT.has(text)) add('link-text', rel, `generic anchor text "${text}" -> ${m[1]}`);
  }

  // Markup sanity: every inline event handler must parse as JavaScript.
  // A bulk edit once emitted onclick="applyFilterTab(\'all\', this)" — valid to
  // an HTML parser, a SyntaxError to the browser, and invisible to axe.
  for (const m of html.matchAll(/\son([a-z]+)\s*=\s*"([^"]*)"/g)) {
    const [, event, body] = m;
    if (!body.trim()) continue;
    const decoded = body
      .replace(/&amp;/g, '&').replace(/&quot;/g, '"')
      .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&#39;/g, "'");
    try {
      new Function(decoded);
    } catch (error) {
      add('inline-handler-syntax', rel, `on${event}="${body.slice(0, 80)}" does not parse: ${error.message}`);
    }
  }

  // best-practices: viewport / doctype / charset / font-size
  const viewport = html.match(/<meta\s+name="viewport"\s+content="([^"]*)"/);
  if (!viewport) add('viewport', rel, 'missing meta viewport');
  else if (/user-scalable\s*=\s*no/i.test(viewport[1]) || /maximum-scale\s*=\s*([0-4](\.\d+)?)\s*[,;]/i.test(viewport[1])) {
    add('viewport', rel, `viewport blocks zoom: ${viewport[1]}`);
  }
  if (!/^\s*<!doctype html>/i.test(html)) add('doctype', rel, 'missing <!DOCTYPE html>');
  if (!/<meta\s+charset="?utf-8"?/i.test(html)) add('charset', rel, 'missing <meta charset>');
  for (const m of html.matchAll(/font-size:\s*([0-9.]+)(px|rem|em)/g)) {
    const px = parseFloat(m[1]) * (m[2] === 'px' ? 1 : 16);
    if (px < 12) add('font-size', rel, `inline font-size ${m[0]} = ${px}px (<12px)`);
  }
}

console.log(`checked ${checked} pages`);
if (!problems.length) {
  console.log('PASS: no statically detectable SEO / best-practice failures');
  console.log('unchecked here (needs a live origin or a browser): http-status-code, robots-txt,');
  console.log('  is-on-https, redirects-http, errors-in-console, inspector-issues');
  process.exit(0);
}

const byAudit = new Map();
for (const p of problems) {
  if (!byAudit.has(p.audit)) byAudit.set(p.audit, []);
  byAudit.get(p.audit).push(p);
}
for (const [audit, items] of [...byAudit].sort()) {
  console.log(`FAIL ${audit} (${items.length})`);
  for (const item of items.slice(0, 12)) console.log(`   ${item.page}: ${item.msg}`);
  if (items.length > 12) console.log(`   ... and ${items.length - 12} more`);
}
process.exit(1);

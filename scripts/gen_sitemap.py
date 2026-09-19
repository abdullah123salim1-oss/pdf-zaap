#!/usr/bin/env python3
"""Generate sitemap.xml (www host) with real lastmod dates from file mtimes."""
import os, glob, re
from datetime import datetime, timezone

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = "https://www.pdfzaap.online"

# This is a new site: the only real content dates are (a) each blog post's
# published date (embedded in the file) and (b) 2026-09-19, the day the
# tool/trust page content was finalized in this release. No older dates are
# invented.
SITE_DATE = "2026-09-19"

def lastmod(rel):
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    if rel.startswith("blog/") and rel.endswith(".html"):
        m = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', open(p, encoding="utf-8").read())
        if m:
            return m.group(1)
    return SITE_DATE

urls = []
def add(rel, priority="0.8", change="weekly"):
    if rel.startswith("http"):
        return
    urls.append((f"{BASE}/{rel}", rel, priority, change))

# Homepage
add("", "1.0")

# Tool pages (35)
for f in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    name = os.path.basename(f)
    if name in ("index.html", "404.html", "about.html", "contact.html", "privacy.html", "terms.html"):
        continue
    # exclude the new non-tool pages handled below
    add(f"{name}", "0.9")

# Blog index + posts
add("blog/", "0.7")
for f in sorted(glob.glob(os.path.join(ROOT, "blog", "*.html"))):
    name = os.path.basename(f)
    if name == "index.html":
        continue
    add(f"blog/{name}", "0.6")

# Language pages
add("id/gabung-pdf.html", "0.7")
add("id/kompres-pdf.html", "0.7")
add("ur/pdf-compress-kaise-karein.html", "0.7")
add("ur/pdf-merge-kaise-karein.html", "0.7")

# Trust pages
add("about.html", "0.5")
add("contact.html", "0.5")
add("privacy.html", "0.5")
add("terms.html", "0.5")

items = []
for url, rel, prio, ch in urls:
    lm = lastmod(rel if rel else "index.html")
    items.append(f'''  <url>
    <loc>{url}</loc>
    <lastmod>{lm}</lastmod>
    <changefreq>{ch}</changefreq>
    <priority>{prio}</priority>
  </url>''')

out = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(items)}
</urlset>
'''
os.makedirs(ROOT, exist_ok=True)
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(out)
print(f"sitemap.xml written with {len(items)} URLs")

#!/usr/bin/env python3
"""Generate the 6 new blog posts (Step 10) using the same template as the
existing fixed posts."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import BASE, navbar, footer
import content_blog_new

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Exact <style> block shared by all blog posts (taken from an existing post)
def _load_style():
    ref = open(os.path.join(ROOT, "blog", "compress-pdf-for-email.html"), encoding="utf-8").read()
    m = re.search(r"<style>.*?</style>", ref, re.S)
    return m.group(0)

STYLE = _load_style()

MONTHS = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

def fmt_date(iso):
    y, m, d = map(int, iso.split("-"))
    return f"{MONTHS[m]} {d}, {y}"

def _j(s):
    return json.dumps(s, ensure_ascii=False)


def post_html(slug, c):
    path = f"blog/{slug}.html"
    full = f"{BASE}/{path}"
    url = f"/{path}"
    faq_schema_entries = ",\n".join(
        '    {\n      "@type": "Question",\n      "name": %s,\n      "acceptedAnswer": {\n        "@type": "Answer",\n        "text": %s\n      }\n    }' % (_j(q), _j(a))
        for q, a in c["faqs"]
    )
    faq_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_schema_entries}
    ]
  }}
  </script>'''
    faq_html = "\n".join(
        f'''      <details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in c["faqs"]
    )
    related_html = "\n".join(f"          <li>{li}</li>" for li in c["related"])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">
{STYLE}

  <title>{c["title"]}</title>
  <meta name="description" content="{c["meta"]}">
  <link rel="canonical" href="{full}">

  <meta property="og:title" content="{c["og_title"]}">
  <meta property="og:description" content="{c["og_desc"]}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{full}">
  <meta property="og:image" content="{BASE}/og-image.png">
  <meta property="og:image:alt" content="PDFZaap — free browser-based PDF tools that never upload your files">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_US">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{c["og_title"]}">
  <meta name="twitter:description" content="{c["og_desc"]}">
  <meta name="twitter:image" content="{BASE}/og-image.png">

  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#FF5200">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {json.dumps(c["og_title"])},
    "description": {json.dumps(c["meta"])},
    "author": {{"@type": "Person", "name": "Abdullah Salim", "url": "{BASE}/about.html#team"}},
    "publisher": {{
      "@type": "Organization",
      "name": "PDFZaap",
      "logo": {{
        "@type": "ImageObject",
        "url": "{BASE}/logo.png"
      }}
    }},
    "datePublished": "{c["date"]}",
    "dateModified": "{c["date"]}",
    "mainEntityOfPage": "{full}"
  }}
  </script>

{faq_schema}
</head>
<body>

{navbar()}

  <main class="post-container">

  <nav class="breadcrumb" aria-label="Breadcrumb" style="margin-top:1.25rem;"><a href="/">Home</a> <span>&gt;</span> <a href="/blog/">Blog</a> <span>&gt;</span> <span>{c["h1"]}</span></nav>
    <article>

      <h1>{c["h1"]}</h1>

      <p class="post-meta">Published {fmt_date(c["date"])} · {c["read"]} min read</p>

{c["body"]}

      <h2>Frequently Asked Questions</h2>

{faq_html}

      <div class="related-box">
        <h2>Related guides &amp; tools</h2>
        <ul>
{related_html}
        </ul>
      </div>

      <div class="cta-box">
        <p>{c["cta_text"]}</p>
        <a class="cta-btn" href="{c["cta_href"]}">{c["cta_label"]}</a>
      </div>

    </article>
  </main>

{footer()}

  <script src="/script.js" defer></script>
</body>
</html>
'''
    return html


def main():
    from html.parser import HTMLParser

    class TextCounter(HTMLParser):
        def __init__(self):
            super().__init__()
            self.skip = 0
            self.text = []
        def handle_starttag(self, tag, attrs):
            if tag in ("script", "style"):
                self.skip += 1
        def handle_endtag(self, tag):
            if tag in ("script", "style") and self.skip:
                self.skip -= 1
        def handle_data(self, data):
            if not self.skip:
                self.text.append(data)

    count = 0
    for slug, c in content_blog_new.POSTS.items():
        html = post_html(slug, c)
        # visible word count check (body + faqs)
        tc = TextCounter()
        body_start = html.find("<article>")
        body_end = html.find("</article>")
        tc.feed(html[body_start:body_end])
        wc = len(" ".join(tc.text).split())
        if wc < 1200:
            print(f"WARNING {slug}: {wc} words (<1200)")
        else:
            print(f"ok {slug}: {wc} words")
        out = os.path.join(ROOT, "blog", f"{slug}.html")
        open(out, "w", encoding="utf-8").write(html)
        count += 1
    print(f"\nGenerated {count} blog posts.")

if __name__ == "__main__":
    main()

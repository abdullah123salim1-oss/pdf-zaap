#!/usr/bin/env python3
"""Generate all 35 standalone tool pages from content modules."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from templates import tool_page_html, TOOL_META
import content_convert
import content_edit
import content_sec_adv
import content_patches

ALL = {}
ALL.update(content_convert.C)
ALL.update(content_edit.C)
ALL.update(content_sec_adv.C)

assert set(ALL) == set(TOOL_META), f"Mismatch: {set(TOOL_META) ^ set(ALL)}"

# Apply depth patches (extra tip + FAQ + when-sentence) to pages under target length
for tool, (tip, faq, when_sentence) in content_patches.P.items():
    c = ALL[tool]
    c["tips"] = list(c["tips"]) + [tip]
    c["faqs"] = list(c["faqs"]) + [faq]
    assert c["when"].count("</p>") == 1, f"{tool}: expected a single <p> in 'when'"
    c["when"] = c["when"].replace("</p>", when_sentence + "</p>")

# reciprocal hreflang for the localized tool pairs (must stay in sync with
# scripts/content_lang.py)
EXTRA_HEAD = {
    "compress-pdf": (
        '  <link rel="alternate" hreflang="en" href="https://www.pdfzaap.online/compress-pdf.html">\n'
        '  <link rel="alternate" hreflang="id" href="https://www.pdfzaap.online/id/kompres-pdf.html">\n'
        '  <link rel="alternate" hreflang="ur" href="https://www.pdfzaap.online/ur/pdf-compress-kaise-karein.html">\n'
        '  <link rel="alternate" hreflang="x-default" href="https://www.pdfzaap.online/compress-pdf.html">'
    ),
    "merge-pdf": (
        '  <link rel="alternate" hreflang="en" href="https://www.pdfzaap.online/merge-pdf.html">\n'
        '  <link rel="alternate" hreflang="id" href="https://www.pdfzaap.online/id/gabung-pdf.html">\n'
        '  <link rel="alternate" hreflang="ur" href="https://www.pdfzaap.online/ur/pdf-merge-kaise-karein.html">\n'
        '  <link rel="alternate" hreflang="x-default" href="https://www.pdfzaap.online/merge-pdf.html">'
    ),
}

def main():
    for tool, c in ALL.items():
        assert len(c["title"]) <= 60, f"{tool}: title too long ({len(c['title'])}): {c['title']}"
        assert len(c["meta"]) <= 155, f"{tool}: meta too long ({len(c['meta'])})"
        html = tool_page_html(tool, c, extra_head=EXTRA_HEAD.get(tool, ""))
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f"{tool}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        words = count_words(html)
        print(f"{tool}.html  words={words}")
    print(f"\nGenerated {len(ALL)} tool pages.")

def count_words(html):
    import re
    body = html.split("<body>", 1)[-1]
    body = body.split("<footer", 1)[0]
    body = re.sub(r"<script.*?</script>", " ", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return len(body.split())

if __name__ == "__main__":
    main()

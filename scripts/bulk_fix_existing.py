#!/usr/bin/env python3
"""Bulk-fix existing pages: www URLs, absolute links, standard header/footer,
breadcrumbs, real author name, Person schema author."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import BASE, navbar, footer

BLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "blog")

def standardize_head_urls(s):
    s = s.replace("https://pdfzaap.online", BASE)
    return s

def absolutize_links(s):
    # ../tool.html -> /tool.html ; ../style.css -> /style.css ; ../favicon.ico -> /favicon.ico
    s = re.sub(r'\.\./([A-Za-z0-9_-]+\.(?:html|css|ico|png|jpg))', r'/\1', s)
    s = s.replace('href="../"', "href=\"../\"")  # noop guard
    return s

def fix_header(s):
    start = s.find("<header class=\"navbar\"")
    end = s.find("</header>", start)
    if start == -1 or end == -1:
        return s
    return s[:start] + navbar() + s[end + len("</header>"):]

def fix_footer(s):
    start = s.find("<footer")
    end = s.find("</footer>", start)
    if start == -1 or end == -1:
        return s
    return s[:start] + footer() + s[end + len("</footer>"):]

def add_breadcrumb(s, title_text):
    m = re.search(r'<main class="post-container">\s*\n', s)
    if not m:
        return s
    crumb = (f'\n  <nav class="breadcrumb" aria-label="Breadcrumb" style="margin-top:1.25rem;">'
             f'<a href="/">Home</a> <span>&gt;</span> <a href="/blog/">Blog</a> <span>&gt;</span> '
             f'<span>{title_text}</span></nav>\n')
    return s[:m.end()] + crumb + s[m.end():]

def person_author_schema(s):
    # Replace Organization author in Article schema with a real Person
    s = re.sub(
        r'"author"\s*:\s*\{\s*"?@type"?\s*:\s*"?Organization"?\s*,\s*"name"\s*:\s*"PDFZaap"?\s*\}',
        '"author": {"@type": "Person", "name": "Abdullah Salim", "url": "%s/about.html#team"}' % BASE,
        s)
    return s

def byline(s):
    s = s.replace("PDFZaap Editorial Team", "Abdullah Salim")
    return s

def process_blog_post(path):
    s = open(path, encoding="utf-8").read()
    title_m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    title_text = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else "Article"
    s = standardize_head_urls(s)
    s = absolutize_links(s)
    s = fix_header(s)
    s = fix_footer(s)
    s = byline(s)
    s = person_author_schema(s)
    if 'class="breadcrumb"' not in s:
        s = add_breadcrumb(s, title_text[:80])
    open(path, "w", encoding="utf-8").write(s)
    print("fixed", os.path.basename(path))

def main():
    for fn in sorted(os.listdir(BLOG_DIR)):
        if fn.endswith(".html") and fn != "index.html":
            process_blog_post(os.path.join(BLOG_DIR, fn))

    # blog/index.html
    p = os.path.join(BLOG_DIR, "index.html")
    s = open(p, encoding="utf-8").read()
    s = standardize_head_urls(s)
    s = absolutize_links(s)
    s = fix_header(s)
    s = fix_footer(s)
    s = s.replace('href="index.html"', 'href="/blog/"')
    open(p, "w", encoding="utf-8").write(s)
    print("fixed blog/index.html")

    # 404.html
    p = os.path.join(os.path.dirname(BLOG_DIR), "404.html")
    s = open(p, encoding="utf-8").read()
    s = standardize_head_urls(s)
    s = absolutize_links(s)
    s = fix_header(s)
    s = fix_footer(s)
    open(p, "w", encoding="utf-8").write(s)
    print("fixed 404.html")

if __name__ == "__main__":
    main()

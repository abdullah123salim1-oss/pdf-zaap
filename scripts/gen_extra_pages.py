#!/usr/bin/env python3
"""Generate Step-10 pages: compress-to-X, intent pages, language pages,
plus trust pages (about/contact/privacy/terms)."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import BASE, LIBS, TOOL_LIBS, TOOL_META, tool_page_html, navbar, footer, head_common
import content_extra
import content_lang

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def _j(s):
    return json.dumps(s, ensure_ascii=False)


def extra_tool_page(path, tool, c, extra_head="", preset_script=""):
    """Extended tool page: custom path, optional direct-answer + extra sections,
    localized support via c['lang'] / c['hreflang']."""
    meta = TOOL_META[tool]
    title, emoji, subtitle, accept, multiple, btn = meta
    lang = c.get("lang", "en")
    og_locale = {"id": "id_ID", "ur": "ur_PK"}.get(lang, "en_US")

    dz = {
        "merge-pdf": ("Select PDF files", "or drop files here"),
        "compress-pdf": ("Select the PDF to compress", "or drop file here"),
        "jpg-to-pdf": ("Select JPG images", "or drop images here"),
        "pdf-to-word": ("Select the PDF", "or drop file here"),
    }[tool]
    dz_multi = tool in ("merge-pdf", "jpg-to-pdf")

    libs = TOOL_LIBS[tool]
    lib_tags = "\n".join(f'  <script src="{LIBS[l]}" defer></script>' for l in libs)

    hreflang_lines = ""
    if c.get("hreflang"):
        hreflang_lines = "\n".join(
            f'  <link rel="alternate" hreflang="{code}" href="{url}">' for code, url in c["hreflang"]
        )

    # breadcrumb: Home > [parent tool] > this page (parent from content 'crumbs' key)
    parent = c.get("crumb_parent")
    if parent:
        p_name, p_path = parent
        crumb2 = ('{"@type": "ListItem", "position": 2, "name": %s, "item": "%s/%s"}'
                  % (_j(p_name), BASE, p_path))
        crumb3 = ('{"@type": "ListItem", "position": 3, "name": %s, '
                  '"item": "%s/%s"}' % (_j(c["h1"]), BASE, path))
        crumbs = f'{crumb2},\n      {crumb3}'
        vis_crumb = f'<a href="/{p_path}">{p_name}</a> <span>&gt;</span> <span>{c["h1"]}</span>'
    else:
        crumbs = ('{"@type": "ListItem", "position": 2, "name": %s, "item": "%s/%s"}'
                  % (_j(c["h1"]), BASE, path))
        vis_crumb = f'<span>{c["h1"]}</span>'

    app_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "PDFZaap {c['h1']}",
    "url": "{BASE}/{path}",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Any (web browser)",
    "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
    "description": "{c['meta']}",
    "publisher": {{"@type": "Organization", "name": "PDFZaap", "url": "{BASE}/"}}
  }}
  </script>'''

    breadcrumb_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/"}},
      {crumbs}
    ]
  }}
  </script>'''

    faq_schema_entries = ",\n".join(
        '    {"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}' % (_j(q), _j(a))
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

    steps_html = "\n".join(
        f'''            <div class="step-item">
              <div class="step-num">{i + 1}</div>
              <h3>{s[0]}</h3>
              <p>{s[1]}</p>
            </div>''' for i, s in enumerate(c["howto"])
    )
    tips_html = "\n".join(f"            <li>{t}</li>" for t in c["tips"])
    faq_html = "\n".join(
        f'''            <details class="faq-item">
              <summary class="faq-trigger"><span>{q}</span><span class="faq-icon">▼</span></summary>
              <div class="faq-content"><p>{a}</p></div>
            </details>''' for q, a in c["faqs"]
    )
    def _icon(rid):
        if rid in TOOL_META:
            return TOOL_META[rid][1]
        return "📉" if rid.startswith("compress-pdf-to-") else "📄"

    related_html = "\n".join(
        f'''            <a href="/{rid}.html" class="tool-card">
              <div class="tool-icon-wrapper">{_icon(rid)}</div>
              <h3>{anchor}</h3>
              <span class="tool-card-link">Use Tool ➔</span>
            </a>''' for rid, anchor in c["related"]
    )

    multiple_attr = " multiple" if dz_multi else ""

    head_extra = (hreflang_lines + "\n" if hreflang_lines else "") + "\n" + app_schema + "\n" + breadcrumb_schema + "\n" + faq_schema
    html = f'''{head_common(path, c["title"], c["meta"], head_extra, lang=lang, og_locale=og_locale)}
<body>
{navbar()}

  <main class="view-container" data-tool="{tool}">
    <div class="workspace-wrapper">
      <div class="workspace-main">

        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="/">Home</a> <span>&gt;</span> {vis_crumb}
        </nav>

        <h1 class="workspace-title">{emoji} {c['h1']}</h1>
        <p class="subtitle">{subtitle}</p>
{c.get('direct_answer', '')}

        <div class="dropzone" id="ws-dropzone">
          <div class="dropzone-icon">📥</div>
          <h3>{dz[0]}</h3>
          <p>{dz[1]}</p>
          <input type="file" id="ws-file-input" class="display-none" accept="{accept}"{multiple_attr}>
        </div>

        <div class="file-list" id="ws-file-list"></div>
        <div class="options-panel display-none" id="ws-options-panel"></div>

        <div class="progress-bar-container" id="ws-progress-container">
          <div class="progress-bar-outer"><div class="progress-bar-inner" id="ws-progress-bar"></div></div>
          <p class="progress-status" id="ws-progress-status">Processing document contents...</p>
        </div>

        <button class="btn btn-primary full-width" id="ws-process-btn" disabled>{btn}</button>

        <div class="security-note">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Files processed locally in your browser — nothing is uploaded to a server</span>
        </div>

        <div id="ws-output-box" class="output-container"></div>

        <section class="tool-intro padding-top-bot">
          {c['intro']}
        </section>
{c.get('extra_sections', '')}

        <section class="how-it-works padding-top-bot">
          <div class="section-header margin-bot-3">
            <h2>How to {c['howto_title']}</h2>
          </div>
          <div class="steps">
{steps_html}
          </div>
        </section>

        <section class="padding-vert-2">
          <div class="section-header margin-bot-3">
            <h2>Why use PDFZaap to {c['why_title']}</h2>
          </div>
{c['why']}
        </section>

        <section class="padding-vert-2">
          <div class="section-header margin-bot-3">
            <h2>Tips &amp; common problems</h2>
          </div>
          <ul class="tips-list">
{tips_html}
          </ul>
        </section>

        <section class="padding-vert-2">
          <div class="section-header margin-bot-3">
            <h2>When to use this vs. related tools</h2>
          </div>
{c['when']}
        </section>

        <section class="faq-section margin-top-3-no-pad">
          <div class="section-header margin-bot-3">
            <h2>Questions &amp; Answers</h2>
          </div>
          <div id="ws-faqs">
{faq_html}
          </div>
        </section>

        <section class="padding-top-4">
          <div class="section-header margin-bot-2-5">
            <h2>Related PDF Tools</h2>
          </div>
          <div class="tools-grid grid-2-cols-no-pad">
{related_html}
          </div>
        </section>

      </div>
    </div>
  </main>

{footer()}

{lib_tags}
  <script src="/script.js" defer></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      activeTool = '{tool}';
      if (typeof setupOptionsPanel === 'function') setupOptionsPanel(activeTool);
{preset_script}
    }});
  </script>
</body>
</html>
'''
    return html


def content_page(path, c):
    """Content-only page (no tool UI)."""
    faq_schema_entries = ",\n".join(
        '    {"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}' % (_j(q), _j(a))
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
        f'''            <details class="faq-item">
              <summary class="faq-trigger"><span>{q}</span><span class="faq-icon">▼</span></summary>
              <div class="faq-content"><p>{a}</p></div>
            </details>''' for q, a in c["faqs"]
    )
    related_html = "\n".join(
        f'''            <a href="/{rid}.html" class="tool-card">
              <div class="tool-icon-wrapper">{TOOL_META[rid][1]}</div>
              <h3>{anchor}</h3>
              <span class="tool-card-link">Use Tool ➔</span>
            </a>''' for rid, anchor in c["related"]
    )
    article_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {json.dumps(c['h1'])},
    "description": {json.dumps(c['meta'])},
    "author": {{"@type": "Person", "name": "Abdullah Salim", "url": "{BASE}/about.html#team"}},
    "publisher": {{"@type": "Organization", "name": "PDFZaap", "url": "{BASE}/"}},
    "datePublished": "2026-09-19",
    "dateModified": "2026-09-19",
    "mainEntityOfPage": "{BASE}/{path}",
    "image": "{BASE}/og-image.png"
  }}
  </script>'''
    breadcrumb_schema2 = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/"}},
      {{"@type": "ListItem", "position": 2, "name": {json.dumps(c['h1'])}, "item": "{BASE}/{path}"}}
    ]
  }}
  </script>'''
    head_extra = article_schema + "\n" + breadcrumb_schema2 + "\n" + faq_schema
    html = f'''{head_common(path, c["title"], c["meta"], head_extra)}
<body>
{navbar()}

  <main class="view-container">
    <div style="max-width:860px;margin:2rem auto;padding:0 2rem 4rem;">

      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>&gt;</span> <span>{c['h1']}</span>
      </nav>

      <h1 class="workspace-title">{c['h1']}</h1>
      <p class="post-meta" style="color:var(--subtext);margin-bottom:1.5rem;">By Abdullah Salim · September 19, 2026</p>
{c['direct_answer']}
      <section class="tool-intro">
        {c['intro']}
      </section>
{c['extra_sections']}

      <section class="faq-section margin-top-3-no-pad">
        <div class="section-header margin-bot-3">
          <h2>Questions &amp; Answers</h2>
        </div>
        <div id="page-faqs">
{faq_html}
        </div>
      </section>

      <section class="padding-top-4">
        <div class="section-header margin-bot-2-5">
          <h2>Related PDF Tools</h2>
        </div>
        <div class="tools-grid grid-2-cols-no-pad">
{related_html}
        </div>
      </section>

    </div>
  </main>

{footer()}

  <script src="/script.js" defer></script>
</body>
</html>
'''
    return html


def trust_page(path, c):
    schema = c.get("schema", "")
    html = f'''{head_common(path, c["title"], c["meta"], schema)}
<body>
{navbar()}

  <main class="view-container">
    <div style="max-width:860px;margin:2rem auto;padding:0 2rem 4rem;">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>&gt;</span> <span>{c['h1']}</span>
      </nav>
      <h1 class="workspace-title">{c['h1']}</h1>
      <p class="post-meta" style="color:var(--subtext);margin-bottom:1.5rem;">Last updated September 19, 2026</p>
      <div style="color:var(--subtext);line-height:1.8;">
{c['body']}
      </div>
    </div>
  </main>

{footer()}

  <script src="/script.js" defer></script>
</body>
</html>
'''
    return html


SIZE_SIBLINGS = {
    "compress-pdf-to-100kb": ["compress-pdf-to-200kb"],
    "compress-pdf-to-200kb": ["compress-pdf-to-100kb", "compress-pdf-to-500kb"],
    "compress-pdf-to-500kb": ["compress-pdf-to-200kb", "compress-pdf-to-1mb"],
    "compress-pdf-to-1mb": ["compress-pdf-to-500kb", "compress-pdf-to-2mb"],
    "compress-pdf-to-2mb": ["compress-pdf-to-1mb"],
}
SIZE_SIBLING_LABEL = {
    "compress-pdf-to-100kb": "Compress PDF to 100KB",
    "compress-pdf-to-200kb": "Compress PDF to 200KB",
    "compress-pdf-to-500kb": "Compress PDF to 500KB",
    "compress-pdf-to-1mb": "Compress PDF to 1MB",
    "compress-pdf-to-2mb": "Compress PDF to 2MB",
}


def expand_size_entry(slug, c):
    """Turn the compact COMPRESS_SIZES entry into the full page structure."""
    label = c["label"]
    related = [(s, SIZE_SIBLING_LABEL[s]) for s in SIZE_SIBLINGS[slug]]
    related += [("compress-pdf", "Compress PDF"), ("split-pdf", "Split PDF")]
    return dict(
        title=c["title"], meta=c["meta"], h1=c["h1"],
        crumb_parent=c["crumb_parent"],
        intro=c["angle_intro"],
        extra_sections=f'''        <section class="padding-vert-2">
          {c["where_from"]}
        </section>''',
        howto_title=f"compress a PDF to {label}",
        howto=[
            ("Open the tool above", f"This page loads the Compress PDF tool with the target size preset to {label}. No extra settings are needed to start."),
            ("Select your PDF", "Click the dropzone or drag the file in. The file is read by your browser and processed locally — nothing is uploaded."),
            (f"Run the compression", f"The tool searches for the best image quality that gets the file under {label}, then shows the result size and, if the target was not reachable, how far off it landed."),
            ("Check the output", f"Open the downloaded file and spot-check a dense page. If it is legible and under {label}, it is ready to upload."),
        ],
        why_title=f"need a page preset to {label}",
        why=f'''<ul class="tips-list">
            <li><strong>The target is already set.</strong> The quality slider and target field start from {label}, so you do not have to know what the tool calls "quality 4" or a specific slider position.</li>
            <li><strong>You get an honest report.</strong> If {label} is not reachable for your particular document, the result says so and shows the actual size — no silent quality sacrifice, no false "done".</li>
            <li><strong>The file never leaves your device.</strong> Processing runs in your browser (PDF.js + pdf-lib), the same engine as the main compress tool.</li>
            <li><strong>No account, no watermark, no limit on uses.</strong></li>
          </ul>''',
        tips=c["extra_tips"],
        when=f'<p>{c["when_links"]}</p>',
        faqs=c["faqs"],
        related=related,
    )


def main():
    count = 0
    # --- A. compress-to-X pages
    for slug, c in content_extra.COMPRESS_SIZES.items():
        preset = f"      const _t = document.getElementById('compress-target');\n      if (_t) _t.value = '{c['kb']}';"
        html = extra_tool_page(f"{slug}.html", "compress-pdf", expand_size_entry(slug, c), preset_script=preset)
        open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8").write(html)
        print("wrote", slug)
        count += 1

    # --- B. intent pages
    for slug, c in content_extra.INTENT.items():
        if c["tool"] is None:
            html = content_page(f"{slug}.html", c)
        else:
            preset = ""
            if slug == "jpg-to-pdf-a4":
                preset = "      const _p = document.getElementById('img-page-size');\n      if (_p) _p.value = 'a4';"
            html = extra_tool_page(f"{slug}.html", c["tool"], c, preset_script=preset)
        open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8").write(html)
        print("wrote", slug)
        count += 1

    # --- D. language pages
    for path, c in content_lang.LANG.items():
        html = extra_tool_page(f"{path}.html", c["tool"], c)
        out = os.path.join(ROOT, f"{path}.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(html)
        print("wrote", path)
        count += 1

    # --- trust pages
    import content_trust
    for path, c in content_trust.TRUST.items():
        html = trust_page(f"{path}.html", c)
        open(os.path.join(ROOT, f"{path}.html"), "w", encoding="utf-8").write(html)
        print("wrote", path)
        count += 1

    print(f"\nGenerated {count} extra pages.")

if __name__ == "__main__":
    main()

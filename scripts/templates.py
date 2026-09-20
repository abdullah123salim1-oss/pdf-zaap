"""Shared HTML templates + constants for PDFZaap page generation."""

BASE = "https://www.pdfzaap.online"

LIBS = {
    "pdf-lib": "https://unpkg.com/pdf-lib@1.17.1/dist/pdf-lib.min.js",
    "pdfjs": "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js",
    "tesseract": "https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js",
    "html2pdf": "https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js",
    "mammoth": "https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js",
    "xlsx": "https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js",
    "pptxgenjs": "https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js",
    "fabric": "https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.0/fabric.min.js",
    "jszip": "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js",
}

# Which CDN libraries each tool actually uses (verified against script.js engines)
TOOL_LIBS = {
    "merge-pdf": ["pdf-lib"],
    "split-pdf": ["pdf-lib"],
    "compress-pdf": ["pdfjs", "pdf-lib"],
    "rotate-pdf": ["pdf-lib"],
    "delete-pdf-pages": ["pdf-lib"],
    "extract-pages-pdf": ["pdf-lib"],
    "reorder-pages-pdf": ["pdf-lib"],
    "number-pdf-pages": ["pdf-lib"],
    "add-watermark-pdf": ["pdf-lib"],
    "crop-pdf": ["pdf-lib"],
    "resize-pdf": ["pdf-lib"],
    "flatten-pdf": ["pdf-lib"],
    "protect-pdf": ["pdf-lib"],
    "unlock-pdf": ["pdf-lib"],
    "repair-pdf": ["pdf-lib"],
    "pdf-metadata-editor": ["pdf-lib"],
    "pdf-to-pdfa": ["pdf-lib"],
    "grayscale-pdf": ["pdfjs", "pdf-lib"],
    "pdf-to-jpg": ["pdfjs", "jszip"],
    "pdf-to-png": ["pdfjs", "jszip"],
    "pdf-to-text": ["pdfjs"],
    "jpg-to-pdf": ["pdf-lib"],
    "png-to-pdf": ["pdf-lib"],
    "word-to-pdf": ["mammoth", "html2pdf"],
    "esign-pdf": ["pdf-lib", "fabric"],
    "ppt-to-pdf": ["jszip", "pdf-lib"],
    "pdf-to-powerpoint": ["pdfjs", "pptxgenjs"],
    "ocr-pdf": ["pdfjs", "tesseract"],
    "compare-pdf": ["pdfjs"],
    "html-to-pdf": ["html2pdf"],
    "excel-to-pdf": ["xlsx", "html2pdf"],
    "pdf-to-html": ["pdfjs"],
    "pdf-to-epub": ["pdfjs", "jszip"],
    "pdf-to-word": ["pdfjs", "jszip"],
    "pdf-to-excel": ["pdfjs", "xlsx"],
}

TOOL_META = {
    # id: (title, emoji, subtitle, accept, multiple, execBtnText)
    "pdf-to-word": ("PDF to Word", "📝", "Extract PDF text into an editable Word (.docx) document", ".pdf", False, "Convert to Word"),
    "pdf-to-jpg": ("PDF to JPG", "🖼️", "Turn each PDF page into a JPG image (ZIP download)", ".pdf", False, "Convert PDF to JPG"),
    "pdf-to-excel": ("PDF to Excel", "📊", "Turn PDF text lines into spreadsheet rows (.xlsx)", ".pdf", False, "Extract to Excel"),
    "pdf-to-powerpoint": ("PDF to PowerPoint", "📈", "Turn each PDF page into a PowerPoint slide", ".pdf", False, "Convert to PowerPoint"),
    "pdf-to-text": ("PDF to Text", "📝", "Extract plain, copyable text from a PDF", ".pdf", False, "Extract Plain Text"),
    "pdf-to-html": ("PDF to HTML", "🌐", "Extract PDF text into a clean, readable HTML page", ".pdf", False, "Generate HTML"),
    "pdf-to-png": ("PDF to PNG", "🖼️", "Export PDF pages as PNG images (ZIP download)", ".pdf", False, "Convert PDF to PNG"),
    "pdf-to-epub": ("PDF to EPUB", "📚", "Turn a PDF's text into a reflowable EPUB e-book", ".pdf", False, "Convert to EPUB"),
    "pdf-to-pdfa": ("PDF Archival Prep", "💾", "Embed archival metadata for long-term storage", ".pdf", False, "Prep for Archiving"),
    "word-to-pdf": ("Word to PDF", "📄", "Convert a Word DOCX document into a PDF", ".docx", False, "Convert to PDF"),
    "jpg-to-pdf": ("JPG to PDF", "🖼️", "Combine one or more JPG images into a single PDF", ".jpg,.jpeg", True, "Convert to PDF"),
    "excel-to-pdf": ("Excel to PDF", "📊", "Convert an Excel workbook to bordered-table PDF pages", ".xlsx,.xls", False, "Convert Excel to PDF"),
    "ppt-to-pdf": ("PowerPoint to PDF", "📈", "Convert a PPTX presentation to PDF pages", ".pptx", False, "Convert PPT to PDF"),
    "html-to-pdf": ("HTML to PDF", "🌐", "Convert an HTML file to a printed-style PDF", ".html,.htm,.txt", False, "Convert HTML to PDF"),
    "png-to-pdf": ("PNG to PDF", "🖼️", "Combine one or more PNG images into a single PDF", ".png", True, "Convert to PDF"),
    "merge-pdf": ("Merge PDF", "🔗", "Combine multiple PDF files into one document", ".pdf", True, "Merge PDFs"),
    "split-pdf": ("Split PDF", "✂️", "Pull out specific pages or ranges into a new PDF", ".pdf", False, "Split PDF"),
    "compress-pdf": ("Compress PDF", "📉", "Reduce PDF file size — pick a quality or a target size", ".pdf", False, "Compress PDF"),
    "rotate-pdf": ("Rotate PDF", "🔄", "Rotate PDF pages by 90, 180 or 270 degrees", ".pdf", False, "Rotate PDF Pages"),
    "delete-pdf-pages": ("Delete PDF Pages", "❌", "Remove specific pages from a PDF", ".pdf", False, "Discard Pages"),
    "extract-pages-pdf": ("Extract Pages", "📤", "Save selected pages as a new PDF", ".pdf", False, "Extract Selected Pages"),
    "reorder-pages-pdf": ("Reorder Pages", "🔀", "Rearrange the page order of a PDF", ".pdf", False, "Reorder Pages"),
    "number-pdf-pages": ("Add Page Numbers", "🔢", "Insert page numbers into a PDF", ".pdf", False, "Add Page Numbers"),
    "add-watermark-pdf": ("Add Watermark", "💧", "Stamp text across every page of a PDF", ".pdf", False, "Add Watermark"),
    "crop-pdf": ("Crop PDF", "✂️", "Trim margins from PDF pages", ".pdf", False, "Crop Pages"),
    "resize-pdf": ("Resize PDF", "📐", "Scale PDF pages to A4 or US Letter", ".pdf", False, "Resize Pages"),
    "unlock-pdf": ("Unlock PDF", "🔓", "Remove a restriction password from a PDF", ".pdf", False, "Unlock PDF"),
    "protect-pdf": ("Protect PDF", "🔒", "Encrypt a PDF with a password", ".pdf", False, "Protect PDF"),
    "esign-pdf": ("E-Sign PDF", "✍️", "Draw and embed a signature on a PDF", ".pdf", False, "Sign PDF"),
    "repair-pdf": ("Repair PDF", "🩹", "Rebuild a corrupted PDF file", ".pdf", False, "Repair PDF"),
    "ocr-pdf": ("OCR PDF", "👁️", "Recognize text in scanned PDFs and images", ".pdf,.jpg,.jpeg,.png,.webp", False, "Extract Text (OCR)"),
    "compare-pdf": ("Compare PDFs", "⚖️", "Diff the text of two PDF versions", ".pdf", True, "Compare Documents"),
    "pdf-metadata-editor": ("PDF Metadata Editor", "🏷️", "Edit a PDF's Title, Author, Subject and Keywords", ".pdf", False, "Update Metadata"),
    "flatten-pdf": ("Flatten PDF", "🥞", "Merge form fields and annotations into static pages", ".pdf", False, "Flatten PDF"),
    "grayscale-pdf": ("Grayscale PDF", "🌫️", "Convert PDF pages to black and white", ".pdf", False, "Convert to Grayscale"),
}

TOOL_DROPZONE = {
    "merge-pdf": ("Select PDF files", "or drop files here", True),
    "compare-pdf": ("Select exactly 2 PDF files", "or drop files here", True),
    "jpg-to-pdf": ("Select JPG images", "or drop images here", True),
    "png-to-pdf": ("Select PNG images", "or drop images here", True),
    "ocr-pdf": ("Select a scanned PDF or image", "or drop a file here", False),
}

CATEGORY_LABEL = {"convert": "Convert", "edit": "Edit & Organize", "security": "Security", "advanced": "Advanced"}


def head_common(path, title, desc, extra_head="", lang="en", og_locale="en_US"):
    """Head block for root-level pages."""
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{BASE}/{path}">
  <link rel="icon" href="/favicon.ico" type="image/x-icon">
  <link rel="apple-touch-icon" href="/logo.png">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#FF5200">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{BASE}/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:url" content="{BASE}/{path}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="PDFZaap">
  <meta property="og:locale" content="{og_locale}">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/og-image.png">
  <meta name="twitter:site" content="@pdfzaap">
{extra_head}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">
</head>'''


def navbar():
    return '''  <header class="navbar" id="main-nav">
    <a href="/" class="logo">⚡ PDF<span>Zaap</span></a>
    <ul class="nav-links">
      <li><a class="nav-link" href="/">Home</a></li>
      <li><a class="nav-link" href="/#tools-anchor">All Tools</a></li>
      <li><a class="nav-link" href="/blog/">Blog</a></li>
      <li><a href="/compress-pdf.html" class="btn btn-primary">Compress PDF</a></li>
    </ul>
  </header>'''


def footer():
    return '''  <footer class="footer">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>⚡ PDF<span>Zaap</span></h4>
        <p>Free, browser-based PDF tools that process your files locally — no uploads, no signup, no watermarks.</p>
      </div>
      <div class="footer-col">
        <h5>Popular Tools</h5>
        <ul class="footer-links">
          <li><a href="/pdf-to-word.html">PDF to Word</a></li>
          <li><a href="/jpg-to-pdf.html">JPG to PDF</a></li>
          <li><a href="/pdf-to-jpg.html">PDF to JPG</a></li>
          <li><a href="/word-to-pdf.html">Word to PDF</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Edit &amp; Organize</h5>
        <ul class="footer-links">
          <li><a href="/merge-pdf.html">Merge PDF</a></li>
          <li><a href="/split-pdf.html">Split PDF</a></li>
          <li><a href="/compress-pdf.html">Compress PDF</a></li>
          <li><a href="/add-watermark-pdf.html">Add Watermark</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Security &amp; Advanced</h5>
        <ul class="footer-links">
          <li><a href="/protect-pdf.html">Protect PDF</a></li>
          <li><a href="/esign-pdf.html">E-Sign PDF</a></li>
          <li><a href="/ocr-pdf.html">OCR PDF</a></li>
          <li><a href="/flatten-pdf.html">Flatten PDF</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul class="footer-links">
          <li><a href="/about.html">About</a></li>
          <li><a href="/contact.html">Contact</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 PDFZaap. All rights reserved. Built for fast, private PDF work.</p>
      <div class="footer-legal-links">
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms of Service</a>
      </div>
    </div>
  </footer>'''


def tool_page_html(tool, c, extra_head="", extra_scripts="", dropzone_override=None):
    """Full standalone tool page. c = content dict for this tool."""
    meta = TOOL_META[tool]
    title, emoji, subtitle, accept, multiple, btn = meta
    dz_title, dz_ext, dz_multi = TOOL_DROPZONE.get(tool, (f"Select your file", "or drop file here", False))
    if dropzone_override:
        dz_title, dz_ext, dz_multi = dropzone_override
    libs = TOOL_LIBS[tool]
    lib_tags = "\n".join(f'  <script src="{LIBS[l]}" defer></script>' for l in libs)

    breadcrumb_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "{BASE}/"}},
      {{"@type": "ListItem", "position": 2, "name": "{c['h1'].strip(' #').split('—')[0].strip()}", "item": "{BASE}/{tool}.html"}}
    ]
  }}
  </script>'''

    app_schema = f'''  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "PDFZaap {c['h1'].strip(' #').split('—')[0].strip()}",
    "url": "{BASE}/{tool}.html",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Any (web browser)",
    "offers": {{"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
    "description": "{c['meta']}",
    "publisher": {{"@type": "Organization", "name": "PDFZaap", "url": "{BASE}/"}}
  }}
  </script>'''

    faq_schema_entries = ",\n".join(
        '    {"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}' % (_json(q), _json(a))
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

    related_html = "\n".join(
        f'''            <a href="/{rid}.html" class="tool-card">
              <div class="tool-icon-wrapper">{TOOL_META[rid][1]}</div>
              <h3>{anchor}</h3>
              <span class="tool-card-link">Use Tool ➔</span>
            </a>''' for rid, anchor in c["related"]
    )

    canvas_html = ""
    if tool == "esign-pdf":
        canvas_html = '''
        <div id="ws-canvas-wrapper" class="ws-canvas-wrapper display-none">
          <p class="canvas-label">Draw Your Signature Below:</p>
          <div class="fabric-canvas-container">
            <canvas id="esign-fabric-canvas" width="400" height="200"></canvas>
          </div>
          <button class="btn btn-secondary canvas-clear-btn" onclick="clearSignatureCanvas()">Clear Canvas</button>
        </div>'''

    multiple_attr = " multiple" if (dz_multi and accept != ".pdf") or (dz_multi and tool in ("merge-pdf", "compare-pdf")) else ""
    # merge-pdf & compare-pdf accept multiple PDFs; image tools accept multiple images
    multiple_attr = " multiple" if dz_multi else ""

    head_extra = (extra_head + "\n" if extra_head else "") + app_schema + "\n" + breadcrumb_schema + "\n" + faq_schema
    html = f'''{head_common(f"{tool}.html", c["title"], c["meta"], head_extra)}
<body>
{navbar()}

  <main class="view-container" data-tool="{tool}">
    <div class="workspace-wrapper">
      <div class="workspace-main">

        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="/">Home</a> <span>&gt;</span> <span>{meta[1]} {meta[0]}</span>
        </nav>

        <h1 class="workspace-title">{emoji} {c['h1']}</h1>
        <p class="subtitle">{subtitle}</p>

        <div class="dropzone" id="ws-dropzone">
          <div class="dropzone-icon">📥</div>
          <h3>{dz_title}</h3>
          <p>{dz_ext}</p>
          <input type="file" id="ws-file-input" class="display-none" accept="{accept}"{multiple_attr}>
        </div>

        <div class="file-list" id="ws-file-list"></div>
        <div class="options-panel display-none" id="ws-options-panel"></div>
{canvas_html}

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
    }});
  </script>
{extra_scripts}
</body>
</html>
'''
    return html


def _json(s):
    import json
    return json.dumps(s, ensure_ascii=False)

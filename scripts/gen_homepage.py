#!/usr/bin/env python3
"""Generate the static, crawlable homepage (index.html)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from templates import BASE, navbar, footer, head_common

LOGO_JSON = '{"@type": "ImageObject", "url": "' + BASE + '/og-image.png", "width": 1200, "height": 630}'

TITLE = "PDFZaap — 35 Free PDF Tools That Run in Your Browser"
DESC = "35 free PDF tools that run entirely in your browser — merge, compress, convert, sign and edit PDFs. No signup, no watermark, no uploads."

GROUPS = [
    ("Convert", "convert", [
        ("pdf-to-word", "Extract PDF text into an editable Word document"),
        ("pdf-to-jpg", "Turn each PDF page into a JPG image"),
        ("pdf-to-excel", "Turn PDF text lines into spreadsheet rows"),
        ("pdf-to-powerpoint", "Turn PDF pages into PowerPoint slides"),
        ("pdf-to-text", "Extract plain, copyable text from a PDF"),
        ("pdf-to-html", "Extract PDF text into a clean HTML page"),
        ("pdf-to-png", "Export PDF pages as lossless PNG images"),
        ("pdf-to-epub", "Turn a PDF's text into a reflowable e-book"),
        ("pdf-to-pdfa", "Embed archival metadata for long-term storage"),
        ("word-to-pdf", "Convert a Word DOCX document into a PDF"),
        ("jpg-to-pdf", "Combine JPG images into one PDF"),
        ("excel-to-pdf", "Convert an Excel workbook to PDF pages"),
        ("ppt-to-pdf", "Convert a PPTX presentation to PDF pages"),
        ("html-to-pdf", "Convert an HTML file to a printed PDF"),
        ("png-to-pdf", "Combine PNG images into one PDF"),
    ]),
    ("Edit & Organize", "edit", [
        ("merge-pdf", "Combine multiple PDF files into one document"),
        ("split-pdf", "Pull out specific pages or ranges into a new PDF"),
        ("compress-pdf", "Reduce file size — pick a quality or a target size"),
        ("rotate-pdf", "Rotate pages by 90°, 180° or 270°"),
        ("delete-pdf-pages", "Remove specific pages from a PDF"),
        ("extract-pages-pdf", "Save selected pages as a new PDF"),
        ("reorder-pages-pdf", "Rearrange the page order of a PDF"),
        ("number-pdf-pages", "Insert 'Page N of M' labels into a PDF"),
        ("add-watermark-pdf", "Stamp text across every page of a PDF"),
        ("crop-pdf", "Trim margins from PDF pages"),
        ("resize-pdf", "Scale PDF pages to A4 or US Letter"),
        ("grayscale-pdf", "Convert PDF pages to black and white"),
    ]),
    ("Security", "security", [
        ("unlock-pdf", "Remove a restriction password from a PDF"),
        ("protect-pdf", "Encrypt a PDF with a password"),
        ("esign-pdf", "Draw and embed a signature on a PDF"),
    ]),
    ("Advanced", "advanced", [
        ("repair-pdf", "Rebuild a corrupted PDF file"),
        ("ocr-pdf", "Recognize text in scanned PDFs and images"),
        ("compare-pdf", "Diff the text of two PDF versions"),
        ("pdf-metadata-editor", "Edit a PDF's Title, Author, Subject and Keywords"),
        ("flatten-pdf", "Merge form fields into static, uneditable pages"),
    ]),
]

EMOJI = {
    "pdf-to-word": "📝", "pdf-to-jpg": "🖼️", "pdf-to-excel": "📊", "pdf-to-powerpoint": "📈",
    "pdf-to-text": "📝", "pdf-to-html": "🌐", "pdf-to-png": "🖼️", "pdf-to-epub": "📚",
    "pdf-to-pdfa": "💾", "word-to-pdf": "📄", "jpg-to-pdf": "🖼️", "excel-to-pdf": "📊",
    "ppt-to-pdf": "📈", "html-to-pdf": "🌐", "png-to-pdf": "🖼️",
    "merge-pdf": "🔗", "split-pdf": "✂️", "compress-pdf": "📉", "rotate-pdf": "🔄",
    "delete-pdf-pages": "❌", "extract-pages-pdf": "📤", "reorder-pages-pdf": "🔀",
    "number-pdf-pages": "🔢", "add-watermark-pdf": "💧", "crop-pdf": "✂️",
    "resize-pdf": "📐", "grayscale-pdf": "🌫️",
    "unlock-pdf": "🔓", "protect-pdf": "🔒", "esign-pdf": "✍️",
    "repair-pdf": "🩹", "ocr-pdf": "👁️", "compare-pdf": "⚖️",
    "pdf-metadata-editor": "🏷️", "flatten-pdf": "🥞",
}

BLOG_TEASERS = [
    ("blog/compress-pdf-for-email.html", "Optimization", "How to Compress a PDF for Email (Under 2 MB)", "Shrink any PDF to fit email attachment limits in three private steps, with a limit cheat sheet for Gmail, Outlook and more."),
    ("blog/merge-pdf-without-adobe.html", "Tutorial", "How to Merge PDF Files Without Adobe Acrobat", "Combine PDFs for free in your browser — no Adobe, no account, no upload — with step-by-step examples."),
    ("blog/pdf-to-word-without-losing-formatting.html", "Conversion", "How to Convert a PDF to Word Without Losing Formatting", "What actually happens in a PDF-to-Word conversion, and how to get the best result for free."),
    ("blog/how-to-check-if-pdf-tool-uploads-files.html", "Privacy", "How to Check if an Online PDF Tool Uploads Your Files", "A 5-minute DevTools walkthrough that shows exactly what leaves your device — use it on any site."),
]

FAQS = [
    ("Is PDFZaap really free?", "Yes. All 35 tools are free with no account, no subscription and no paid tier. The site is a static, server-light site, which is what makes a no-signup, no-meter model practical."),
    ("Are my files uploaded to a server?", "No. Every tool runs in your browser using client-side WebAssembly and JavaScript libraries. Your file is read from disk by the browser, processed in your tab's memory, and the result is saved back to your device. The only things that ever download are the page assets (styles, scripts, fonts) and, for the OCR tool on first use, the public English language model from the Tesseract project."),
    ("How can I verify my files stay on my device?", "Open your browser's developer tools (F12 or right-click → Inspect), go to the Network tab, then run any tool with a test file. You should see no upload request containing your file. We explain the whole check, step by step, in our guide on how to check whether an online PDF tool uploads files."),
    ("Is there a file size limit?", "There is no imposed limit on file size or on how many files you process. The practical limits are your device: very large documents use more browser memory and take longer, since all processing happens locally."),
    ("Does it work on iPhone and Android?", "Yes — the tools run in mobile browsers (Safari, Chrome and others) with touch support for the signature canvas. Some workflows, like adding many files at once, are faster on a desktop, but nothing is desktop-only."),
    ("Why is my compressed PDF still large?", "Compression here works by re-rendering pages as images, which shrinks image-heavy PDFs a lot but gains little on text-only or already-optimized files. The result note tells you honestly when that happens. Our guide on why PDF files are large explains the six usual causes and what actually fixes each one."),
]

def card_html(tool, desc, cat):
    return f'''        <a href="/{tool}.html" class="tool-card" data-category="{cat}">
          <div class="tool-icon-wrapper">{EMOJI[tool]}</div>
          <h3>{title_of(tool)}</h3>
          <p>{desc}</p>
          <span class="tool-card-link">Use Tool ➔</span>
        </a>'''

def title_of(tool):
    return {
        "pdf-to-word": "PDF to Word", "pdf-to-jpg": "PDF to JPG", "pdf-to-excel": "PDF to Excel",
        "pdf-to-powerpoint": "PDF to PowerPoint", "pdf-to-text": "PDF to Text", "pdf-to-html": "PDF to HTML",
        "pdf-to-png": "PDF to PNG", "pdf-to-epub": "PDF to EPUB", "pdf-to-pdfa": "PDF Archival Prep",
        "word-to-pdf": "Word to PDF", "jpg-to-pdf": "JPG to PDF", "excel-to-pdf": "Excel to PDF",
        "ppt-to-pdf": "PowerPoint to PDF", "html-to-pdf": "HTML to PDF", "png-to-pdf": "PNG to PDF",
        "merge-pdf": "Merge PDF", "split-pdf": "Split PDF", "compress-pdf": "Compress PDF",
        "rotate-pdf": "Rotate PDF", "delete-pdf-pages": "Delete PDF Pages",
        "extract-pages-pdf": "Extract Pages", "reorder-pages-pdf": "Reorder Pages",
        "number-pdf-pages": "Add Page Numbers", "add-watermark-pdf": "Add Watermark",
        "crop-pdf": "Crop PDF", "resize-pdf": "Resize PDF", "grayscale-pdf": "Grayscale PDF",
        "unlock-pdf": "Unlock PDF", "protect-pdf": "Protect PDF", "esign-pdf": "E-Sign PDF",
        "repair-pdf": "Repair PDF", "ocr-pdf": "OCR PDF", "compare-pdf": "Compare PDFs",
        "pdf-metadata-editor": "PDF Metadata Editor", "flatten-pdf": "Flatten PDF",
    }[tool]

def main():
    grid = []
    for label, cat, tools in GROUPS:
        cards = "\n".join(card_html(t, d, cat) for t, d in tools)
        grid.append(f'''      <section class="tools-group" aria-label="{label} tools">
        <h2 class="tools-group-title">{label}</h2>
        <div class="tools-grid" data-group="{cat}">
{cards}
        </div>
      </section>''')
    grid_html = "\n\n".join(grid)

    faq_html = "\n".join(
        f'''            <details class="faq-item">
              <summary class="faq-trigger"><span>{q}</span><span class="faq-icon">▼</span></summary>
              <div class="faq-content"><p>{a}</p></div>
            </details>''' for q, a in FAQS
    )

    import json
    faq_schema = ",\n".join(
        '    {"@type": "Question", "name": %s, "acceptedAnswer": {"@type": "Answer", "text": %s}}' % (json.dumps(q), json.dumps(a))
        for q, a in FAQS
    )

    blog_html = "\n".join(
        f'''        <a href="/{path}" class="blog-card" style="display:block;padding:1.5rem;">
          <span class="blog-post-category blog-card-tag">{cat}</span>
          <h3>{title}</h3>
          <p class="blog-card-excerpt">{excerpt}</p>
          <span class="tool-card-link">Read Guide ➔</span>
        </a>''' for path, cat, title, excerpt in BLOG_TEASERS
    )

    extra_head = f'''  <meta name="google-site-verification" content="euv5Cu8-6Lf43gRh0tCwjHcz4j9Zuqv7o7PtzbA6v2M">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Organization",
        "@id": "{BASE}/#org",
        "name": "PDFZaap",
        "url": "{BASE}/",
        "logo": {LOGO_JSON},
        "sameAs": [
          "https://github.com/abdullah123salim1-oss/pdf-zaap"
        ],
        "contactPoint": {{
          "@type": "ContactPoint",
          "email": "contact@pdfzaap.online",
          "contactType": "customer support"
        }}
      }},
      {{
        "@type": "WebSite",
        "@id": "{BASE}/#website",
        "url": "{BASE}/",
        "name": "PDFZaap",
        "description": "35 free PDF tools that run entirely in your browser.",
        "publisher": {{"@id": "{BASE}/#org"}}
      }}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_schema}
    ]
  }}
  </script>'''

    html = f'''{head_common("", TITLE, DESC, extra_head)}
<body>

  <noscript>
    <div class="noscript-warning">
      <strong>⚠️ JavaScript is disabled.</strong> PDFZaap's tools require JavaScript to process PDF files in your browser. Please enable JavaScript to use the tools — the guides and tool descriptions remain readable without it.
    </div>
  </noscript>

{navbar()}

  <main class="view-container">

    <section class="hero">
      <h1>Every PDF tool you need — <span>free</span>, and private by design</h1>
      <p>35 tools for merging, compressing, converting, signing and editing PDF documents. Everything runs in your browser: no signup, no watermark, and your files never leave your device.</p>
      <div class="hero-ctas">
        <button type="button" class="btn btn-primary" onclick="scrollToToolsGrid()">Explore PDF Tools</button>
        <a class="btn btn-secondary" href="/is-it-safe-to-use-online-pdf-tools.html">How Your Files Stay Private</a>
      </div>
      <div class="trust-badges">
        <span class="trust-badge">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
          No Signup Required
        </span>
        <span class="trust-badge">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
          No Watermarks
        </span>
        <span class="trust-badge">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
          Files Never Leave Your Device
        </span>
        <span class="trust-badge">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>
          Free — No Subscription
        </span>
      </div>
    </section>

    <section class="search-filter-section" id="tools-anchor">
      <div class="search-wrapper">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="tool-search" class="search-input" placeholder="Search 35 PDF tools..." aria-label="Search 35 PDF tools">
      </div>
      <div class="filter-tabs" id="filter-tabs-container" role="tablist" aria-label="Filter PDF tools by category">
        <button type="button" class="filter-tab active" data-tab="all" onclick="applyFilterTab('all', this)">All Tools</button>
        <button type="button" class="filter-tab" data-tab="convert" onclick="applyFilterTab('convert', this)">Convert</button>
        <button type="button" class="filter-tab" data-tab="edit" onclick="applyFilterTab('edit', this)">Edit &amp; Organize</button>
        <button type="button" class="filter-tab" data-tab="security" onclick="applyFilterTab('security', this)">Security</button>
        <button type="button" class="filter-tab" data-tab="advanced" onclick="applyFilterTab('advanced', this)">Advanced</button>
      </div>
    </section>

    <section id="main-tools-grid" class="homepage-tools">

{grid_html}

    </section>

    <section class="why-us" id="why-pdfzaap-section">
      <div class="section-header">
        <h2>Why Use PDFZaap</h2>
        <p class="subtext-muted">Fast, private document processing that runs right in your browser.</p>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <h3>⚡ Client-Side Processing</h3>
          <p>Tools run on WebAssembly and JavaScript in your browser tab. No server queues, no upload waits — processing speed depends on your device, not a data center.</p>
        </div>
        <div class="feature-card">
          <h3>🛡️ Nothing Uploaded</h3>
          <p>Your files are read from disk by the browser and processed in local memory. There is no upload endpoint to begin with — and you can verify it yourself in the Network tab.</p>
        </div>
        <div class="feature-card">
          <h3>🆓 Free, No Account</h3>
          <p>All 35 tools are free with no subscription, no daily limits and no watermark. There is no account to create because there is no server to hold one.</p>
        </div>
        <div class="feature-card">
          <h3>💻 Works on Desktop and Mobile</h3>
          <p>Chrome, Safari, Firefox and Edge on Windows, macOS, Linux, iOS and Android. Touch input works for drawing signatures and selecting files.</p>
        </div>
        <div class="feature-card">
          <h3>🔍 Verifiable Privacy</h3>
          <p>We publish a step-by-step guide for proving that a PDF tool does not upload your files. Run the check on PDFZaap or on any competitor.</p>
        </div>
        <div class="feature-card">
          <h3>🧾 Honest About Limits</h3>
          <p>Each tool page states exactly what it does and what it cannot do — e.g. PDF to Word is a text-based conversion, and compression re-renders pages as images. No fine-print surprises.</p>
        </div>
      </div>
    </section>

    <section class="how-it-works">
      <div class="section-header">
        <h2>How It Works</h2>
        <p class="subtext-muted">Three steps, all on your device.</p>
      </div>
      <div class="steps">
        <div class="step-item">
          <div class="step-num">1</div>
          <h3>Select File</h3>
          <p>Drag and drop your file or choose it from your device. It stays on your machine.</p>
        </div>
        <div class="step-item">
          <div class="step-num">2</div>
          <h3>Process</h3>
          <p>Set any options and run the tool. Everything is processed in your browser's memory.</p>
        </div>
        <div class="step-item">
          <div class="step-num">3</div>
          <h3>Download</h3>
          <p>Save the finished file straight to your device — nothing was ever sent anywhere.</p>
        </div>
      </div>
    </section>

    <section class="faq-section">
      <div class="section-header">
        <h2>Frequently Asked Questions</h2>
        <p class="subtext-muted">Straight answers about how PDFZaap works.</p>
      </div>
      <div id="homepage-faqs">
{faq_html}
      </div>
    </section>

    <section class="blog-teaser" id="blog-teaser">
      <div class="section-header">
        <h2>Guides &amp; Tutorials</h2>
        <p class="subtext-muted">Practical PDF guides from the PDFZaap blog.</p>
      </div>
      <div class="blog-grid">
{blog_html}
      </div>
      <p style="text-align:center;margin-top:1.5rem;"><a class="btn btn-secondary" href="/blog/">View All Guides</a></p>
    </section>

    <section class="about-section" id="about-us-section">
      <div class="section-header">
        <h2>About PDFZaap</h2>
      </div>
      <p class="about-text">
        PDFZaap is a free collection of browser-based PDF tools. The design decision is simple: run everything client-side, so documents are processed on the device that owns them. It is a small project with an opinion — your files are yours, and software should be transparent about what it can and cannot do.
      </p>
      <div class="stats-bar">
        <div class="stat-box">
          <h4>35</h4>
          <p>Free PDF Tools</p>
        </div>
        <div class="stat-box">
          <h4>0</h4>
          <p>Files Uploaded to Servers</p>
        </div>
        <div class="stat-box">
          <h4>0</h4>
          <p>Accounts Required</p>
        </div>
        <div class="stat-box">
          <h4>100%</h4>
          <p>Client-Side Processing</p>
        </div>
      </div>
      <p style="text-align:center;margin-top:1.5rem;"><a class="btn btn-secondary" href="/about.html">About the Project &amp; Team</a></p>
    </section>

  </main>

{footer()}

  <button type="button" class="scroll-top-btn" id="scroll-top" onclick="scrollToTop()" aria-label="Scroll to top">
    ▲
  </button>

  <div class="cookie-banner" id="cookie-banner">
    <div class="cookie-content">
      We use a single local browser storage value to remember your cookie preference. No third-party tracking cookies are set. See our <a href="/privacy.html">Privacy Policy</a>.
    </div>
    <div class="cookie-btns">
      <button type="button" class="btn btn-secondary btn-sm" onclick="acceptCookies(false)">Decline</button>
      <button type="button" class="btn btn-primary btn-sm" onclick="acceptCookies(true)">Accept</button>
    </div>
  </div>

  <script src="/script.js" defer></script>
</body>
</html>
'''
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html written")

if __name__ == "__main__":
    main()

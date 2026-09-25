# Content for the 15 Convert-category tool pages.
# Each entry: title(<=60), meta(<=155), h1, intro, howto_title, howto(4 steps), why_title, why, tips(4-5), when, faqs(4-5), related(4)

C = {}

C["pdf-to-word"] = dict(
    title="Convert PDF to Word Free — PDF to DOCX Online | PDFZaap",
    meta="Turn a PDF into an editable Word document in your browser. Text-based conversion, free, private, no signup, no upload. Perfect for repurposing reports.",
    h1="Convert PDF to Word — Free & Private",
    # The <div class="quick-answer"> block is the extractable snippet answer
    # (40 words) that sits above the fold for "how do I convert a pdf to word".
    intro="""<div class="quick-answer">
          <h2>Quick answer: how do I convert a PDF to a Word document?</h2>
          <p>Open this page, select your PDF, click <strong>Convert to Word</strong>, then download the <code>.docx</code>. The conversion runs in your browser, so nothing is uploaded and no account is needed. Text-based PDFs become editable Word paragraphs; scanned PDFs need OCR first. Columns and tables are simplified, not cloned.</p>
        </div>
        <p>Need to edit a PDF but it doesn't allow changes? This free PDF to Word tool reads your document's text layer and rebuilds it as an editable Word document in Microsoft Word's native <code>.docx</code> format, right in your browser. Every word lands as editable text in reading order, a page break is written between PDF pages, and the file never leaves your device. It is a text-based conversion — the honest trade-off for doing everything client-side — so complex multi-column layouts are simplified rather than cloned pixel-for-pixel.</p>""",
    howto_title="convert a PDF to Word",
    howto=[
        ("Select the PDF", "Click the dropzone and pick the PDF document you want to make editable. One file at a time, 100 MB or smaller."),
        ("Click Convert to Word", "The button is enabled as soon as a file is selected. There are no settings to choose — the output is always a Word .docx."),
        ("Wait for the extraction", "The Word converter reads each page's text layer, joins the words that share a line, and writes one Word paragraph per line. Larger documents take a few extra seconds because the work happens on your own device."),
        ("Download the Word file", "Save the .docx and keep editing it in Microsoft Word, Google Docs or LibreOffice — all of them open this file format."),
    ],
    why_title="edit PDF text without a server",
    why="""<p><strong class='subtext'>Privacy first.</strong> Most online converters upload your document to a third-party server, which matters when the file contains contracts, payroll data, student records or unpublished work. PDFZaap runs the whole PDF to Word conversion in your browser memory: the file is read locally, the DOCX is assembled locally, and only the finished file is saved to your device. You can even try it on an unstable or offline-capable connection once the page has loaded.</p><p class='subtext'><strong>Nothing to unlock.</strong> There is no free tier and no paid tier to compare it with, so no quota gates this PDF to Word converter: converting PDFs here has no daily job count, no watermark and no "upgrade to unlock unlimited conversions" step.</p><p class='subtext'><strong>Know the limits up front.</strong> This is a text extraction, not a layout engine. Straightforward documents — reports, letters, manuscripts, forms with visible text — convert cleanly. Documents built from many text boxes, sidebars or embedded charts may need light re-arranging afterwards — the table below shows exactly which way each element goes. If the PDF is a scan, there is no text to extract: run the <a href='/ocr-pdf.html'>OCR PDF tool</a> first to get the words, then convert.</p>
        <div class="table-scroll">
          <table class="post-table">
            <thead>
              <tr>
                <th scope="col">What is in the PDF</th>
                <th scope="col">What the .docx keeps</th>
                <th scope="col">What you fix afterwards</th>
              </tr>
            </thead>
            <tbody>
              <tr><th scope="row">Body text</th><td>Real, selectable, editable paragraphs in reading order</td><td>Nothing — retype and reformat as usual</td></tr>
              <tr><th scope="row">Page breaks</th><td>One explicit page break per PDF page, so page structure survives reflow</td><td>Adjust spacing if the re-flowed text shifts pages</td></tr>
              <tr><th scope="row">Headings, bold, italics, font sizes</th><td>The words only, in Word's default style</td><td>Reapply Word styles (Heading 1, Bold) on the way back out</td></tr>
              <tr><th scope="row">Tables</th><td>Each cell as its own line of text</td><td>Redraw the table, or use <a href='/pdf-to-excel.html'>PDF to Excel</a> for editable rows</td></tr>
              <tr><th scope="row">Two-column and sidebar layouts</th><td>Text grouped by height, so columns on the same line merge into one line</td><td>Convert a one-column copy, or split page ranges first</td></tr>
              <tr><th scope="row">Images, charts, signatures</th><td>Nothing — they are not text</td><td>Export the page as a picture with <a href='/pdf-to-jpg.html'>PDF to JPG</a></td></tr>
              <tr><th scope="row">Scanned pages</th><td>Nothing — a scan has no text layer to read</td><td>Run <a href='/ocr-pdf.html'>OCR PDF</a> on the scan, then convert the result</td></tr>
            </tbody>
          </table>
        </div>""",
    tips=[
        "Run <a href='/pdf-to-text.html'>PDF to Text</a> first if you only need to check that the text extracts well before committing to a conversion.",
        "If the output reads in the wrong order, the PDF likely uses a multi-column layout. Converting a one-column copy (or selecting a page range with <a href='/split-pdf.html'>Split PDF</a>) gives a cleaner result.",
        "Page breaks are inserted between PDF pages, so your Word document keeps the same page structure even if it reflows.",
        "To convert scanned PDFs, scan at 300 dpi with high contrast and run OCR before this tool — a sharper scan is the single biggest quality lever on the finished Word file.",
        "Keep the output as .docx rather than converting twice: Microsoft Word, Word for the web, Google Docs and LibreOffice all read it, so pick whichever of the Word formats your collaborators use.",
        "Going the other way later? <a href='/word-to-pdf.html'>Word to PDF</a> rebuilds the fixed-layout copy once your edits are done.",
    ],
    when="<p>Choose this tool when the goal is <em>editing the words</em> — when you need to convert PDFs into editable Word documents without sending the file to anyone else's server. If you need the PDF's exact visual design, export pages as images with <a href='/pdf-to-jpg.html'>PDF to JPG</a> instead. If you want plain copyable text without a Word file, <a href='/pdf-to-text.html'>PDF to Text</a> is faster. If the tables matter more than the prose, <a href='/pdf-to-excel.html'>PDF to Excel</a> hands you editable rows instead of loose text lines. And if you are going the other direction — putting a Word document into PDF — use <a href='/word-to-pdf.html'>Word to PDF</a>. For deeper guidance on what to expect from browser-based conversion, read <a href='/pdf-to-word-without-losing-formatting.html'>PDF to Word without losing formatting</a> and <a href='/blog/how-to-convert-pdf-to-word-on-mac-free.html'>How to convert PDF to Word on Mac for free</a>.</p>",
    faqs=[
        ("Is the Word file really editable?", "Yes — it is a standard .docx with normal editable paragraphs. You can retype, reformat and save it from Microsoft Word, Google Docs, LibreOffice or similar."),
        ("Can I convert a scanned PDF to Word?", "Not directly. Scanned PDFs are pictures of pages, so there is no text to extract. Run the <a href='/ocr-pdf.html'>OCR PDF tool</a> first to read the words, then feed the result into this free PDF to Word converter."),
        ("Are tables preserved?", "Table cells come out as text lines in reading order. They are not rebuilt as a real Word table, so plan to re-draw complex tables by hand."),
        ("Is this PDF to Word conversion free, or is there a limit to unlock?", "Free, with no signup, no daily quota and no paid plan that unlocks unlimited work — every tool on this site is the full one. The only limits are memory guards that protect your own device: a PDF must be 100 MB or smaller and no larger than 2,000 pages, and a document whose extracted text is enormous is refused with a prompt to split it."),
        ("Will my fonts, bold text and headings survive the conversion?", "No. The .docx is written as plain text in Word's default style, so typefaces, sizes, colours and heading levels are not carried across. Reapply your styles in Word once the text is in place — that is still faster than retyping the document."),
        ("Which Word formats will open the downloaded file?", "The output is Office Open XML (.docx), which Microsoft Word 2007 and newer, Word for the web, Google Docs and LibreOffice all open. The legacy binary .doc format is not produced; if a system demands .doc, open the .docx in Word and use Save As."),
    ],
    related=[("pdf-to-text", "PDF to Text"), ("word-to-pdf", "Word to PDF"), ("pdf-to-excel", "PDF to Excel"), ("ocr-pdf", "OCR PDF")],
)

C["pdf-to-jpg"] = dict(
    title="Convert PDF to JPG Free Online — Extract Images | PDFZaap",
    meta="Turn every PDF page into a JPG image in your browser. Pages render at 2× resolution and download as a ZIP. Free, private, no upload, no watermark.",
    h1="Convert PDF to JPG — Pages as Images",
    intro="<p>Sometimes you need a PDF as pictures: a page for a slide deck, a screenshot-style preview, or an upload form that only accepts images. This tool renders each page of your PDF to a JPG at double the standard resolution and bundles all pages into a ZIP. Rendering happens in your browser, so the document never touches a server.</p>",
    howto_title="turn a PDF into JPG images",
    howto=[
        ("Select the PDF", "Click the dropzone or drag the file in. One file at a time is supported."),
        ("Click Convert PDF to JPG", "The button becomes active once the file is ready."),
        ("Watch the render progress", "Each page is drawn to a canvas and encoded as JPEG. A 10-page document typically finishes in a few seconds."),
        ("Download the ZIP", "You get one JPG per page, named page-1.jpg, page-2.jpg, and so on, inside a single archive."),
    ],
    why_title="export PDF pages as images privately",
    why="<p><strong class='subtext'>No upload means no exposure.</strong> Upload-based converters store your pages on someone else's infrastructure and, depending on their policy, may delete them after a delay — or not at all. Here the page pixels only ever exist in your browser's canvas and then on your own disk. That is the difference you want when the document is a passport scan, a medical report or a draft contract.</p><p class='subtext'><strong>2× resolution keeps things usable.</strong> Pages render at double scale, which is plenty sharp for presentations, chat attachments and most print previews. If you need higher fidelity, or a lossless format for graphic work, the <a href='/pdf-to-png.html'>PDF to PNG</a> tool exports the same pages as PNG.</p>",
    tips=[
        "For a single page you do not want to convert, trim it out first with <a href='/extract-pages-pdf.html'>Extract Pages</a> so the ZIP stays small.",
        "JPG is lossy: pages with fine text or line art may show slight artifacts when heavily scaled up later. Use PNG for archival-quality images.",
        "Very long documents create large ZIPs — the browser does all the encoding locally, so patience and memory are the only constraints.",
        "Need the images as one PDF again? Combine them with <a href='/jpg-to-pdf.html'>JPG to PDF</a>.",
    ],
    when="<p>Use <strong>PDF to JPG</strong> when you need web-friendly images to share or paste. Choose <a href='/pdf-to-png.html'>PDF to PNG</a> for lossless quality, <a href='/pdf-to-text.html'>PDF to Text</a> if you actually want the words, and <a href='/pdf-to-powerpoint.html'>PDF to PowerPoint</a> if the real destination is a slide deck. Our guide <a href='/blog/how-to-convert-jpg-to-pdf-on-windows.html'>How to convert JPG to PDF on Windows</a> covers the reverse direction.</p>",
    faqs=[
        ("What resolution are the images?", "Pages render at 2× the PDF's native scale, which is sharp for on-screen use and most print previews. You cannot set a custom DPI in this tool."),
        ("Are all pages included?", "Yes — every page becomes one JPG file, and all of them are packaged in a ZIP download."),
        ("Why is the output a ZIP instead of loose images?", "Browsers can reliably offer one download at a time; the ZIP keeps the pages ordered and named page-1.jpg through page-N.jpg."),
        ("Does it work on encrypted PDFs?", "Not while they are password-locked. Remove a restriction password with <a href='/unlock-pdf.html'>Unlock PDF</a> first (you need the password)."),
    ],
    related=[("pdf-to-png", "PDF to PNG"), ("jpg-to-pdf", "JPG to PDF"), ("pdf-to-text", "PDF to Text"), ("pdf-to-powerpoint", "PDF to PowerPoint")],
)

C["pdf-to-excel"] = dict(
    title="PDF to Excel Converter Free — PDF to XLSX Online | PDFZaap",
    meta="Extract PDF text into an editable Excel sheet in your browser. Each text line becomes a row; clear column gaps become cells. Free, private, no upload.",
    h1="Convert PDF to Excel — Text to .xlsx",
    intro="<p>Spreadsheets trapped inside PDF statements, invoices and reports are painful to work with by hand. This tool reads the text of each PDF page, turns every line into a spreadsheet row, and splits cells where the PDF shows tabs or clear column spacing — then hands you a real <code>.xlsx</code> file. It is a practical extraction, not a table-perfect reconstruction, and the page explains exactly where the limits are.</p>",
    howto_title="pull PDF text into Excel",
    howto=[
        ("Select the PDF", "Upload the statement, invoice or report whose data you need in a spreadsheet."),
        ("Click Extract to Excel", "The browser reads the text line by line, page by page."),
        ("Check the row mapping", "Each visible line becomes a row; columns are guessed from tabs and wide gaps."),
        ("Download the .xlsx", "Open the workbook in Excel or Google Sheets and tidy any tricky rows."),
    ],
    why_title="work with PDF data locally",
    why="<p><strong class='subtext'>Your data stays on your machine.</strong> Financial statements, HR exports and client invoices are exactly the files you should not hand to an upload server. Everything here runs in the browser: the PDF is read locally, the sheet is built locally, and the download goes straight to your device.</p><p class='subtext'><strong>Honest about what it is.</strong> This is a text-line extraction with simple column detection. A clean, tab-aligned PDF table converts well; a PDF with merged cells, rotated text or graphics-drawn rules will need manual cleanup. If you need the table rebuilt perfectly, a dedicated table-extraction service (or re-exporting from the source system) is the right tool — we would rather tell you that than pretend otherwise.</p>",
    tips=[
        "Prefer the original? If you can get the data as CSV or XLSX from the source system, do that — this tool is for when you only have the PDF.",
        "Lines that should be one row but wrapped onto two in the PDF will appear as two rows; merge them in Excel.",
        "For scanned PDFs there is no text layer: run <a href='/ocr-pdf.html'>OCR PDF</a> first, then paste the recognized text into your sheet.",
        "Very dense reports may need several passes: extract, inspect, then re-extract a narrower page range with <a href='/extract-pages-pdf.html'>Extract Pages</a>.",
    ],
    when="<p>Reach for this when you need <em>editable rows</em> from a text-based PDF. For plain text you want to paste into a document, use <a href='/pdf-to-text.html'>PDF to Text</a>; for Word-style documents, <a href='/pdf-to-word.html'>PDF to Word</a>; and to go the other way (spreadsheet → PDF), use <a href='/excel-to-pdf.html'>Excel to PDF</a>. See also <a href='/blog/why-is-my-pdf-file-so-large.html'>Why is my PDF file so large?</a> for context on what PDFs actually contain.</p>",
    faqs=[
        ("Will my table's columns line up?", "If the PDF uses real tab stops or consistent spacing, yes. If columns are only visually aligned by text boxes, cells will fall into a single column and need splitting."),
        ("Are formulas preserved?", "No — you get the visible values as cell values, which is what you need for analysis anyway."),
        ("Does it handle multiple pages?", "Yes, every page is included, with a blank row between pages so you can see where one page ends."),
        ("Is the output a real Excel file?", "Yes, a standard .xlsx that opens in Excel, Google Sheets, LibreOffice and most spreadsheet apps."),
    ],
    related=[("excel-to-pdf", "Excel to PDF"), ("pdf-to-text", "PDF to Text"), ("pdf-to-word", "PDF to Word"), ("ocr-pdf", "OCR PDF")],
)

C["pdf-to-powerpoint"] = dict(
    title="PDF to PowerPoint Converter Free — PDF to PPTX | PDFZaap",
    meta="Turn every PDF page into a PowerPoint slide in your browser. Pages become high-quality slide images you can arrange. Free, private, no upload.",
    h1="Convert PDF to PowerPoint — Pages as Slides",
    intro="<p>Presentations that arrive as PDFs are easy to admire and hard to reuse. This tool renders each PDF page as a high-resolution image and places it on its own PowerPoint slide in a 10 × 7.5 inch deck. The result is a genuine <code>.pptx</code> you can reorder, duplicate or annotate. Rendering and packaging both happen locally in your browser.</p>",
    howto_title="turn PDF pages into slides",
    howto=[
        ("Select the PDF", "Upload the document you want as a slide deck."),
        ("Click Convert to PowerPoint", "The button activates as soon as the file is loaded."),
        ("Wait for page rendering", "Each page is drawn at 2× scale and added to a slide in order."),
        ("Download the .pptx", "Open it in PowerPoint, Keynote or Google Slides and rearrange slides as needed."),
    ],
    why_title="reuse PDF decks without a server",
    why="<p><strong class='subtext'>Private by construction.</strong> Slides often contain numbers, roadmaps and client work. Because the conversion runs entirely in your browser, the PDF and the resulting deck never cross the network at all.</p><p class='subtext'><strong>Images, not editable shapes — here's the deal.</strong> Each slide is a faithful image of the page, so the visuals are perfect, but you cannot edit the individual text boxes. That is the honest limitation of client-side conversion. If you need editable shapes and text, you need the original file or a server-side conversion service; for most 'reuse and present' workflows, image slides are exactly what you want.</p>",
    tips=[
        "Use <a href='/split-pdf.html'>Split PDF</a> first to skip title pages or appendices you do not want as slides.",
        "After downloading, set your deck's slide size to 10 × 7.5 inches if your template differs, to avoid letterboxing.",
        "Add speaker notes in the presentation app for each image slide to build a proper talk track.",
        "For a PDF that is really a stack of photos, <a href='/pdf-to-jpg.html'>PDF to JPG</a> may be more useful than slides.",
    ],
    when="<p>Use this tool when the destination is a <em>presentation</em>. If you only want page images, <a href='/pdf-to-jpg.html'>PDF to JPG</a> is simpler. To go the other direction, <a href='/ppt-to-pdf.html'>PowerPoint to PDF</a> turns decks into documents. And for editable documents rather than slides, <a href='/pdf-to-word.html'>PDF to Word</a> extracts real text.</p>",
    faqs=[
        ("Are the slides editable?", "The slide images are not — each page is a faithful picture. You can rearrange, duplicate and annotate slides, but not edit text within a page."),
        ("What slide size is used?", "A 10 by 7.5 inch custom layout (the classic 4:3 presentation size), with each page fitted to the slide."),
        ("Does it work on long documents?", "Yes, but every page becomes a slide, so a 50-page PDF becomes a 50-slide deck. Trim first with Split PDF if you do not need all of it."),
        ("Why not extract the text as real PowerPoint text?", "Rebuilding editable text boxes from arbitrary PDF layouts is not something a browser can do reliably without a server farm — we would rather give you perfect image slides than broken text boxes."),
    ],
    related=[("ppt-to-pdf", "PowerPoint to PDF"), ("pdf-to-jpg", "PDF to JPG"), ("split-pdf", "Split PDF"), ("pdf-to-word", "PDF to Word")],
)

C["pdf-to-text"] = dict(
    title="PDF to Text Converter Free Online — Extract TXT | PDFZaap",
    meta="Extract clean, copyable text from any PDF in your browser. Page by page, with separators, downloaded as a .txt file. Free and private — no upload.",
    h1="Extract Text from PDF — Free & Fast",
    intro="<p>Need the words out of a PDF — to paste into an email, feed into a search, or keep as a lightweight copy? This tool reads the text layer of your PDF page by page and writes it to a plain-text file with clear page markers. It runs entirely in your browser, so even sensitive documents stay on your device.</p>",
    howto_title="extract text from a PDF",
    howto=[
        ("Select the PDF", "Choose the document with the text you want to pull out."),
        ("Click Extract Plain Text", "Processing starts immediately after the file loads."),
        ("Follow the progress", "Each page is read in order; a counter shows page X of Y."),
        ("Download the .txt", "The file uses '--- Page N ---' separators so you can find content again easily."),
    ],
    why_title="get words out of PDFs without uploading",
    why="<p><strong class='subtext'>Local, instant, no queue.</strong> Upload-based extractors make you wait on their servers and store your document briefly (or, with weaker policies, longer). This reads the text directly from the file in your browser tab — no queue, no deletion timer, no third-party storage, ever.</p><p class='subtext'><strong>The one real limitation.</strong> PDFs that are scans or images have no text layer, so there is nothing to extract — that is what the <a href='/ocr-pdf.html'>OCR PDF</a> tool is for. Also, text follows the order the PDF stores it, which is usually reading order but can be scrambled in heavily designed documents. For straight documents, the output is clean and paste-ready.</p>",
    tips=[
        "Paste the result into a note app to copy chunks without opening the file each time.",
        "For scanned pages, run <a href='/ocr-pdf.html'>OCR PDF</a> first — it recognizes the printed words and gives you a text file too.",
        "Extract a narrower range first with <a href='/extract-pages-pdf.html'>Extract Pages</a> if you only need part of the document.",
        "Plain text is the friendliest input for most translation and summarization tools.",
    ],
    when="<p>Use <strong>PDF to Text</strong> for raw, copyable content. Choose <a href='/pdf-to-word.html'>PDF to Word</a> when the destination is an editable document, <a href='/pdf-to-html.html'>PDF to HTML</a> for a web page, and <a href='/pdf-to-epub.html'>PDF to EPUB</a> for a reflowable e-book. Our article <a href='/blog/how-to-make-pdf-searchable-from-scanner.html'>How to make a scanned PDF searchable</a> explains when OCR is the right first step.</p>",
    faqs=[
        ("Will the formatting be kept?", "No — you get plain text with page separators. Headings and paragraphs come out as lines, not styled blocks."),
        ("Does it work on scanned PDFs?", "Not by itself. Scans have no text layer; use OCR PDF to recognize the text first."),
        ("Is there a limit on document length?", "No imposed limit. Very long documents simply take longer to read in the browser."),
        ("Why are page markers included?", "So you can trace any passage back to its original page when you check the source."),
    ],
    related=[("pdf-to-word", "PDF to Word"), ("ocr-pdf", "OCR PDF"), ("pdf-to-html", "PDF to HTML"), ("extract-pages-pdf", "Extract Pages")],
)

C["pdf-to-html"] = dict(
    title="PDF to HTML Converter Free — PDF to Web Page | PDFZaap",
    meta="Turn a PDF into a clean HTML page in your browser. Text is kept in reading order, one section per page. Self-contained file, free, private.",
    h1="Convert PDF to HTML — Clean Output",
    intro="<p>Publishing a PDF on a website is clumsy — visitors cannot search it or read it comfortably on phones. This tool extracts the PDF's text and wraps it in a self-contained HTML page: one labeled section per page, readable paragraphs, basic embedded styling. Everything happens in your browser, and the output file needs no external assets to open.</p>",
    howto_title="turn a PDF into an HTML page",
    howto=[
        ("Select the PDF", "Upload the document you want to publish as a web page."),
        ("Click Generate HTML", "The extraction starts immediately."),
        ("Watch pages convert", "Each page's text is grouped into lines and paragraphs in reading order."),
        ("Download the .html", "Open the file in any browser, or upload it to your site as-is."),
    ],
    why_title="share PDF content on the web privately",
    why="<p><strong class='subtext'>No server in the middle.</strong> The PDF is parsed locally and the HTML is assembled locally — there is no upload step where your draft, internal report or client document could be stored by a third party.</p><p class='subtext'><strong>Content, not design.</strong> Be clear about what you get: the words in reading order, nicely wrapped — not a clone of the visual layout. Multi-column pages may read out of design order, and images are not embedded. For most 'put this information online so people can search it' jobs, that is exactly the right trade. For design fidelity, export page images with <a href='/pdf-to-jpg.html'>PDF to JPG</a> and build the page around them.</p>",
    tips=[
        "Add your own CSS later: the page uses simple semantic markup (h1, h2, p) that is easy to restyle.",
        "For scanned PDFs, run <a href='/ocr-pdf.html'>OCR PDF</a> first so the HTML contains real words.",
        "Combine the output with <a href='/html-to-pdf.html'>HTML to PDF</a> workflows: extract, edit the HTML, then re-print to PDF if you need an updated document.",
        "Keep pages under ~2,000 words per section for comfortable reading on mobile.",
    ],
    when="<p>Choose this when the goal is a <em>web page or embeddable content</em>. Use <a href='/pdf-to-text.html'>PDF to Text</a> for raw text, <a href='/pdf-to-word.html'>PDF to Word</a> for documents, and <a href='/pdf-to-epub.html'>PDF to EPUB</a> for e-books. The reverse direction — HTML to PDF — is covered by our <a href='/html-to-pdf.html'>HTML to PDF tool</a>.</p>",
    faqs=[
        ("Is the HTML self-contained?", "Yes — styles are embedded, so the single .html file renders the same everywhere without extra assets."),
        ("Are images extracted?", "No. Text only. Export page images separately with PDF to JPG or PDF to PNG if you need them."),
        ("Will multi-column layouts read correctly?", "Text is ordered top-to-bottom by vertical position, so dense multi-column designs can read out of intended order. Single-column documents convert cleanly."),
        ("Can I use it for a real website?", "Absolutely — it is valid, simple HTML. Swap in your site's CSS and it fits in."),
    ],
    related=[("html-to-pdf", "HTML to PDF"), ("pdf-to-text", "PDF to Text"), ("pdf-to-word", "PDF to Word"), ("ocr-pdf", "OCR PDF")],
)

C["pdf-to-png"] = dict(
    title="Convert PDF to PNG Free Online — Lossless Pages | PDFZaap",
    meta="Export every PDF page as a lossless PNG image in your browser. 2× render, ZIP download. Free, private, no upload, no watermark.",
    h1="Convert PDF to PNG — Lossless Pages",
    intro="<p>PNG is the choice when JPG artifacts are unacceptable: line art, screenshots, UI mockups, or anything you will zoom or annotate. This tool renders each PDF page to PNG at double resolution and packages the pages in a ZIP. All rendering is local — your file never leaves the browser.</p>",
    howto_title="export PDF pages as PNG",
    howto=[
        ("Select the PDF", "Drag in the document whose pages you need as PNGs."),
        ("Click Convert PDF to PNG", "The button enables as soon as the file is loaded."),
        ("Wait for rendering", "PNG encoding is heavier than JPEG, so expect a few seconds for many pages."),
        ("Download the ZIP", "Each page arrives as page-1.png, page-2.png, and so on."),
    ],
    why_title="get sharp page images without uploading",
    why="<p><strong class='subtext'>Lossless where it matters.</strong> JPEG re-encodes every render, which smears fine text and crisp edges. PNG stores the rendered page exactly, so diagrams, code and small print stay sharp when you zoom or crop.</p><p class='subtext'><strong>Private rendering.</strong> The pages are drawn to canvas in your tab and encoded there. There is no upload, no temporary server copy, no deletion timer to worry about — important when the pages are ID documents, design proofs or confidential diagrams. The trade-off is file size: PNGs are larger than JPGs, which is why <a href='/pdf-to-jpg.html'>PDF to JPG</a> exists as the lighter-weight sibling.</p>",
    tips=[
        "For a single page, extract it first with <a href='/extract-pages-pdf.html'>Extract Pages</a> to keep the ZIP small.",
        "If you are converting for web use and bandwidth matters, JPG at quality 0.8 is often indistinguishable — use PDF to JPG instead.",
        "Annotations and redlines: open the PNGs in any image editor, mark them up, then recombine with <a href='/png-to-pdf.html'>PNG to PDF</a>.",
        "Transparent backgrounds are not created — pages render on white, which matches how PDFs actually display.",
    ],
    when="<p>Use <strong>PDF to PNG</strong> when image quality is the priority. For smaller files, <a href='/pdf-to-jpg.html'>PDF to JPG</a>; for the words rather than pictures, <a href='/pdf-to-text.html'>PDF to Text</a>; and to put images back into a document, <a href='/png-to-pdf.html'>PNG to PDF</a>. More context in <a href='/blog/how-to-combine-scanned-receipts-into-one-pdf.html'>How to combine scanned receipts into one PDF</a>.</p>",
    faqs=[
        ("Why PNG instead of JPG?", "PNG is lossless — no compression artifacts on text, lines or logos. It costs more in file size, which is the trade you make for quality."),
        ("What resolution are the images?", "Pages render at 2× the PDF's native scale, which is sharp for zooming and most print use."),
        ("Are all pages included?", "Yes, one PNG per page, all in a single ZIP download."),
        ("Does it work with encrypted PDFs?", "Only after the password is removed with Unlock PDF — encrypted files cannot be read without the password."),
    ],
    related=[("pdf-to-jpg", "PDF to JPG"), ("png-to-pdf", "PNG to PDF"), ("extract-pages-pdf", "Extract Pages"), ("pdf-to-powerpoint", "PDF to PowerPoint")],
)

C["pdf-to-epub"] = dict(
    title="PDF to EPUB Converter Free — PDF to eBook Online | PDFZaap",
    meta="Convert a PDF into a reflowable EPUB e-book in your browser. Each page becomes a chapter of selectable text. Free, private, no upload.",
    h1="Convert PDF to EPUB — Read Anywhere",
    intro="<p>PDFs are terrible on small screens: fixed pages, tiny text, endless panning. This tool converts your PDF's text into a proper EPUB 3 e-book — reflowable, font-adjustable, with a table of contents — so it reads well on any e-reader or phone. The whole conversion, including the packaging step, happens locally in your browser.</p>",
    howto_title="turn a PDF into an EPUB e-book",
    howto=[
        ("Select the PDF", "Upload the book or long document you want to read on a small screen."),
        ("Click Convert to EPUB", "Text extraction starts immediately."),
        ("Watch chapters build", "Each PDF page becomes one chapter, and a table of contents is generated."),
        ("Download the .epub", "Import it into your e-reader app (Apple Books, Kobo, Kindle via Calibre, etc.)."),
    ],
    why_title="build e-books without sending books to a server",
    why="<p><strong class='subtext'>Your library stays yours.</strong> Manuscripts, course books and internal reports do not need to pass through a conversion service. The text is read locally and the EPUB package is written locally; only the finished .epub is saved to your device.</p><p class='subtext'><strong>Text-first, honestly stated.</strong> This converts the words — images and complex layout are not carried into the EPUB. For text-based books and reports that is a feature: the result reflows to your font size preference. For image-heavy books, expect a text-only companion rather than a full replica. Scanned books need <a href='/ocr-pdf.html'>OCR PDF</a> first, since scans contain no real text.</p>",
    tips=[
        "Set your e-reader's font size after import — the whole point of reflowable text is reading comfort.",
        "Use <a href='/split-pdf.html'>Split PDF</a> to convert a single volume from a multi-book PDF.",
        "Chapters follow PDF page boundaries, so long chapters are normal; split large books manually in your e-reader app.",
        "For a plain text version instead, <a href='/pdf-to-text.html'>PDF to Text</a> is a lighter alternative.",
    ],
    when="<p>Choose this when the destination is an <em>e-reader</em>. For documents you will edit, use <a href='/pdf-to-word.html'>PDF to Word</a>; for a web page, <a href='/pdf-to-html.html'>PDF to HTML</a>; for raw text, <a href='/pdf-to-text.html'>PDF to Text</a>. Scanned sources should go through <a href='/ocr-pdf.html'>OCR PDF</a> before conversion.</p>",
    faqs=[
        ("Will my e-reader accept the file?", "The output is standard EPUB 3 with a navigation document — Apple Books, Kobo, Google Play Books and Calibre all accept it."),
        ("Are images included?", "No. The conversion carries text only, which keeps the file small and the text selectable."),
        ("What about the table of contents?", "Each PDF page becomes a chapter entry, so you get page-level navigation rather than detected headings."),
        ("Does it work on scanned books?", "Not directly — run OCR PDF first to get real text, then convert the result."),
    ],
    related=[("pdf-to-text", "PDF to Text"), ("pdf-to-word", "PDF to Word"), ("ocr-pdf", "OCR PDF"), ("split-pdf", "Split PDF")],
)

C["pdf-to-pdfa"] = dict(
    title="PDF Archival Prep — Metadata for Long-Term Storage | PDFZaap",
    meta="Prepare a PDF for long-term archiving in your browser: embeds title, subject and date metadata. Honest note: this is prep, not certified PDF/A conversion.",
    h1="Prepare a PDF for Archiving",
    intro="<p>Archives fail when documents arrive with no context: no title, no dates, no subject line. This tool writes standard PDF metadata — title, subject, creation and modification dates, creator and producer — into your document in the browser, so archiving systems can index and track it. It is preparation, not certification: the page below explains exactly what PDF/A requires and where a browser's limits are.</p>",
    howto_title="prep a PDF for long-term storage",
    howto=[
        ("Select the PDF", "Upload the document you want to archive."),
        ("Check existing metadata", "If the PDF already has a title, it is kept; otherwise the file name is used."),
        ("Click Prep for Archiving", "Subject, keywords, creator, producer and both date fields are written in."),
        ("Download the prepared PDF", "For certified PDF/A, run the file through a dedicated converter and validator (see below)."),
    ],
    why_title="archive documents with real context",
    why="<p><strong class='subtext'>Metadata is what makes archives usable.</p><p class='subtext'>Decades from now, 'scan_0042.pdf' tells nobody anything. A document with a proper title, subject, author and modification date can be searched, verified and cited. Because the write happens in your browser, the original content is untouched and nothing is uploaded.</p><p class='subtext'><strong>What this is not: a certified PDF/A conversion.</strong> PDF/A (ISO 19005) requires more than metadata — embedded fonts, a specific XMP structure, and a validation pass. Browsers cannot run that validation, and we will not claim otherwise. For certified archival files, convert with dedicated tooling such as LibreOffice (export as PDF/A), Ghostscript, or a commercial validator, then verify the result with a free PDF/A validator.</p>",
    tips=[
        "Give important archives a human-readable file name before converting — metadata helps, but names still matter in plain file listings.",
        "Pair this with <a href='/flatten-pdf.html'>Flatten PDF</a> for forms you want to keep as static records.",
        "Use <a href='/protect-pdf.html'>Protect PDF</a> when the archived record is confidential.",
        "Read <a href='/blog/pdf-vs-pdfa-difference.html'>PDF vs PDF/A: what is the difference?</a> for the full technical picture.",
    ],
    when="<p>Use this tool as the <em>first step</em> of an archival workflow, followed by a proper PDF/A conversion with dedicated tools. For plain metadata editing (any field, including author and keywords), use <a href='/pdf-metadata-editor.html'>PDF Metadata Editor</a>. For confidentiality, <a href='/protect-pdf.html'>Protect PDF</a>; for static forms, <a href='/flatten-pdf.html'>Flatten PDF</a>.</p>",
    faqs=[
        ("Does this produce a certified PDF/A file?", "No. It embeds archival metadata only. Certification requires font embedding and a validation pass that browser tooling cannot perform — use LibreOffice, Ghostscript or a paid service for that final step."),
        ("What is PDF/A?", "An ISO standard (19005) version of PDF for long-term archiving. It mandates things like embedded fonts and an XMP metadata block so the document renders the same in 50 years."),
        ("Are the pages changed?", "No — only the document's metadata fields are written. The visible content is byte-for-byte the same pages."),
        ("Why not just use the Metadata Editor?", "You can! This tool presets the fields archives care about (subject, dates, producer) in one click, while the editor gives you full manual control."),
    ],
    related=[("pdf-metadata-editor", "PDF Metadata Editor"), ("flatten-pdf", "Flatten PDF"), ("protect-pdf", "Protect PDF"), ("compress-pdf", "Compress PDF")],
)

C["word-to-pdf"] = dict(
    title="Word to PDF Converter Free Online — DOCX to PDF | PDFZaap",
    meta="Convert a Word DOCX file into a PDF in your browser. Free, private, no upload, no signup. Text and basic formatting render cleanly on Letter pages.",
    h1="Convert Word to PDF — Free & Private",
    intro="<p>Word documents drift: reflowed paragraphs, missing fonts, slightly different page breaks on every machine. A PDF locks the layout down for the recipient. This tool converts your <code>.docx</code> file to a PDF entirely in your browser — the document is parsed locally, rendered on standard pages, and downloaded. Nothing is uploaded.</p>",
    howto_title="turn a Word document into a PDF",
    howto=[
        ("Select the .docx file", "Click the dropzone and choose your Word document (.docx)."),
        ("Click Convert to PDF", "The file is parsed into structured content right away."),
        ("Watch the render", "The browser lays the content out on Letter-size pages."),
        ("Download the PDF", "Open it to confirm pagination, then send it with confidence."),
    ],
    why_title="lock down Word documents without uploading",
    why="<p><strong class='subtext'>The upload problem.</strong> Contracts, bids, theses and client proposals are the files that get converted to PDF most often — and the files you least want sitting on a stranger's server. Here the DOCX is unzipped and read in your tab, the layout is rendered there, and the PDF is saved locally. There is no queue and no third-party storage.</p><p class='subtext'><strong>What converts well.</strong> Headings, paragraphs, lists, tables and basic styling render cleanly, which covers the large majority of business documents. Very exotic Word features (complex section breaks, text boxes layered over content, linked objects) are simplified rather than cloned. If a document is design-critical, open it in Word first and check the result after converting — the honest workflow for any converter.</p>",
    tips=[
        "Save your final Word file as .docx (not the legacy .doc) for the cleanest conversion.",
        "Set your page size and margins in Word before converting — the converter preserves them but does not reformat.",
        "For a PDF with form fields that others will fill, add the fields in Word first.",
        "Need the reverse direction? <a href='/pdf-to-word.html'>PDF to Word</a> extracts PDF text back into an editable document.",
    ],
    when="<p>Use <strong>Word to PDF</strong> when you need a fixed-layout copy of a document you control. If the source is already a PDF and you need it editable, use <a href='/pdf-to-word.html'>PDF to Word</a>. For spreadsheets, <a href='/excel-to-pdf.html'>Excel to PDF</a>; for presentations, <a href='/ppt-to-pdf.html'>PowerPoint to PDF</a>. See <a href='/blog/how-to-convert-pdf-to-word-on-mac-free.html'>How to convert PDF to Word on Mac free</a> for the opposite workflow.</p>",
    faqs=[
        ("Is the layout preserved?", "Standard documents — text, headings, lists, tables, images in the flow — convert cleanly. Layered text boxes and unusual section breaks may simplify."),
        ("Are images included?", "Images embedded in the Word document are rendered onto the pages, which keeps the document looking complete."),
        ("What page size is used?", "US Letter by default, matching the document's own page setup where readable."),
        ("Why not just 'Print to PDF' from Word?", "You could — this is for when you do not have Word installed, or when you want a repeatable, private conversion without touching the source app."),
    ],
    related=[("pdf-to-word", "PDF to Word"), ("excel-to-pdf", "Excel to PDF"), ("ppt-to-pdf", "PowerPoint to PDF"), ("html-to-pdf", "HTML to PDF")],
)

C["jpg-to-pdf"] = dict(
    title="JPG to PDF Converter Free Online — Images to PDF | PDFZaap",
    meta="Combine one or more JPG images into a single PDF in your browser. Fit-to-image or centered A4/Letter pages. Free, private, no upload.",
    h1="Combine JPG Images into One PDF",
    intro="<p>Receipts, product photos, scanned documents, screenshots — JPGs that need to travel as a single document. This tool places your images on PDF pages in the order you choose: either each image fills its own page, or every image is centered on a standard A4 or US Letter page with margins. All processing is local in your browser.</p>",
    howto_title="turn JPG images into a PDF",
    howto=[
        ("Select your JPGs", "Add as many images as you need — the order you select them is the page order."),
        ("Choose a page layout", "Pick 'Fit page to each image' for full-bleed pages, or A4 / US Letter for images centered on a standard page."),
        ("Reorder if needed", "Remove an image and re-add it to fix the sequence before converting."),
        ("Click Convert to PDF", "Download the combined PDF when the progress bar completes."),
    ],
    why_title="bundle images into documents privately",
    why="<p><strong class='subtext'>No upload, no watermark.</strong> Image-to-PDF services are a classic upload trap: your photos go to their server, sometimes get watermarked on free tiers, and sit in temporary storage. Here the images are embedded into the PDF in your browser tab, and the finished file downloads straight to your device — no watermark, no cap, no account.</p><p class='subtext'><strong>Honest about the output.</strong> Each image becomes a faithful raster page: no text layer is added, so the PDF is not searchable. If you need searchable pages from scans, run <a href='/ocr-pdf.html'>OCR PDF</a> on the result's source images to get the text, or use a dedicated OCR-to-PDF service. Images are never upscaled beyond their native resolution — small images on A4 pages simply sit smaller, which is the correct behavior.</p>",
    tips=[
        "Name your images with numeric prefixes (01.jpg, 02.jpg…) so the folder order is the page order.",
        "For job applications or government uploads, the A4 option produces the standard-page PDFs most portals expect — see our <a href='/jpg-to-pdf-a4.html'>JPG to PDF A4</a> guide.",
        "Keep photo resolutions reasonable (3000px+ for print, 1200px+ for screen) before combining, to keep the PDF light.",
        "Combine with <a href='/compress-pdf.html'>Compress PDF</a> afterwards if the result exceeds an email or portal limit.",
    ],
    when="<p>Use this when you need <em>images in one document</em>. For transparent graphics, <a href='/png-to-pdf.html'>PNG to PDF</a>; for existing PDFs that need combining, <a href='/merge-pdf.html'>Merge PDF</a>; and to split a finished PDF back out, <a href='/split-pdf.html'>Split PDF</a>. Step-by-step walkthrough: <a href='/blog/how-to-convert-jpg-to-pdf-on-windows.html'>How to convert JPG to PDF on Windows</a>.</p>",
    faqs=[
        ("Can I add more than one image?", "Yes — select as many JPGs as you like; each becomes one page in the order selected."),
        ("Why is my image small on the page?", "In A4/Letter mode, images are scaled down to fit with margins but never stretched beyond their native size. Small source images will appear small — that is honest scaling, not a bug."),
        ("Is the text in my images searchable?", "No. The pages are raster images without a text layer. Use OCR PDF on the source images if you need extractable text."),
        ("Does it work on phones?", "Yes — the tool runs in mobile browsers, and image selection works from your photo library."),
    ],
    related=[("png-to-pdf", "PNG to PDF"), ("merge-pdf", "Merge PDF"), ("compress-pdf", "Compress PDF"), ("ocr-pdf", "OCR PDF")],
)

C["excel-to-pdf"] = dict(
    title="Excel to PDF Converter Free Online — XLSX to PDF | PDFZaap",
    meta="Convert an Excel workbook to a PDF in your browser. Sheets render as bordered tables on landscape pages. Up to 10 sheets, 5,000 rows. Free, private.",
    h1="Convert Excel to PDF — Sheets as Tables",
    intro="<p>Spreadsheets are the universal data carrier, but PDFs are the universal document carrier — and clients, banks and governments often want both. This tool reads your <code>.xlsx</code> or <code>.xls</code> workbook in the browser, renders each sheet as a clean bordered table on landscape A4 pages, and hands you a PDF. Your data never leaves the device.</p>",
    howto_title="turn an Excel workbook into a PDF",
    howto=[
        ("Select the workbook", "Upload the .xlsx or .xls file you want to export."),
        ("Click Convert Excel to PDF", "The first sheets are parsed and laid out immediately."),
        ("Follow the sheet progress", "Up to 10 sheets are exported, each labeled with its sheet name."),
        ("Download the PDF", "Check column widths and pagination, then share the file."),
    ],
    why_title="export spreadsheets without leaving the browser",
    why="<p><strong class='subtext'>Private for sensitive data.</strong> Payroll sheets, budgets and client reports are exactly what you do not want uploading to a conversion service. Parsing and rendering happen in your tab; the PDF is written locally.</p><p class='subtext'><strong>Straightforward, with stated limits.</strong> Cells render as bordered tables with headers, which is what most 'send the spreadsheet as a document' jobs need. Charts, images and formula animations are not drawn — you get the values. Very wide sheets paginate across pages, and each export covers up to 10 sheets with 5,000 rows each, which comfortably covers normal reports. If you need charts, print from Excel itself; if you need a huge data dump, filter first.</p>",
    tips=[
        "Set sensible column widths in Excel before converting — the converter uses the data as-is.",
        "Hide helper columns you do not want in the document; hidden cells are not rendered.",
        "For a single table out of a big workbook, copy it to a fresh sheet first.",
        "Reverse direction: pulling data <em>out of</em> a PDF is covered by <a href='/pdf-to-excel.html'>PDF to Excel</a>.",
    ],
    when="<p>Use this when the destination is a <em>PDF document</em> of your data. For the reverse (PDF → spreadsheet), use <a href='/pdf-to-excel.html'>PDF to Excel</a>. For Word-style documents, <a href='/word-to-pdf.html'>Word to PDF</a>; for decks, <a href='/ppt-to-pdf.html'>PowerPoint to PDF</a>. Background reading: <a href='/blog/why-is-my-pdf-file-so-large.html'>Why is my PDF file so large?</a> explains why exported PDFs sometimes surprise you.</p>",
    faqs=[
        ("How many sheets can I convert?", "The first 10 sheets in the workbook. Each becomes its own section labeled with the sheet name."),
        ("Are charts included?", "No — cell values and table structure render, but embedded charts and images are not drawn. Use Excel's own export for chart-heavy workbooks."),
        ("What page format is used?", "Landscape A4, which fits more columns per page than portrait."),
        ("Is my data uploaded anywhere?", "No. The workbook is parsed in your browser and the PDF is generated on your device."),
    ],
    related=[("pdf-to-excel", "PDF to Excel"), ("word-to-pdf", "Word to PDF"), ("png-to-pdf", "PNG to PDF"), ("pdf-to-text", "PDF to Text")],
)

C["ppt-to-pdf"] = dict(
    title="PowerPoint to PDF Converter Free — PPT to PDF | PDFZaap",
    meta="Convert a PPTX presentation to PDF in your browser. Slides become clean PDF pages with their text laid out. Free, private, no upload, no watermark.",
    h1="Convert PowerPoint to PDF",
    intro="<p>Decks should travel as PDFs: identical on every screen, no accidental edits, no font surprises. This tool reads your <code>.pptx</code> file in the browser, lays out each slide's text onto a standard 10 × 7.5 inch PDF page, and gives you back a ready-to-send presentation. Everything runs locally — the deck is never uploaded.</p>",
    howto_title="turn a PPTX deck into a PDF",
    howto=[
        ("Select the .pptx file", "Upload the presentation. Legacy .ppt must be saved as .pptx from PowerPoint first."),
        ("Click Convert PPT to PDF", "Slides are unpacked and processed in order."),
        ("Watch the slide progress", "Each slide's text is laid out on its own PDF page."),
        ("Download the PDF", "Send it out — pagination matches the slide order exactly."),
    ],
    why_title="share decks as stable PDF documents",
    why="<p><strong class='subtext'>PDFs are the professional format for distribution.</strong> A .pptx sent to a client can be opened in a different version of PowerPoint with different fonts and reflowed layouts. The PDF from this tool renders the same everywhere, and recipients cannot (accidentally) change a number while reviewing.</p><p class='subtext'><strong>Text-based, and that matters.</strong> The converter extracts slide text directly from the file and re-lays it out, so the PDF stays small and the text stays selectable for search and copy. What it does not carry: background images, charts, and complex graphics — text is the reliable part, and we say so on the page rather than promising a pixel-perfect clone. For design-heavy decks, PowerPoint's own 'Export as PDF' produces the full-visual result; use this tool when clean, searchable, private text pages are what you need.</p>",
    tips=[
        "Keep slide text concise — dense bullet slides convert to dense PDF pages.",
        "Add titles to your slides in PowerPoint before converting; the first text block on each slide is treated as the title.",
        "For a deck that must keep its exact visuals, use PowerPoint's built-in PDF export instead and keep this tool for text-first documents.",
        "Reverse direction: <a href='/pdf-to-powerpoint.html'>PDF to PowerPoint</a> turns PDF pages into slides.",
    ],
    when="<p>Choose this when you need a <em>stable, searchable PDF of a deck</em>. For pixel-perfect visual export, use PowerPoint's native export. For other office formats, see <a href='/word-to-pdf.html'>Word to PDF</a> and <a href='/excel-to-pdf.html'>Excel to PDF</a>. And when you receive a PDF and need slides back, <a href='/pdf-to-powerpoint.html'>PDF to PowerPoint</a> is the matching tool.</p>",
    faqs=[
        ("Will my slide designs look identical?", "Text is re-laid out cleanly, but background graphics, charts and images are not rendered. For a visual clone, use PowerPoint's built-in PDF export."),
        ("Does it support .ppt files?", "Only .pptx — open legacy .ppt files in PowerPoint and save as .pptx first."),
        ("Are the pages searchable?", "Yes, the text is real text, so Ctrl+F and copy-paste work in any PDF reader."),
        ("What slide size is used?", "Standard 10 × 7.5 inch (720 × 540 pt) pages, matching classic presentation proportions."),
    ],
    related=[("pdf-to-powerpoint", "PDF to PowerPoint"), ("word-to-pdf", "Word to PDF"), ("jpg-to-pdf", "JPG to PDF"), ("pdf-to-text", "PDF to Text")],
)

C["html-to-pdf"] = dict(
    title="HTML to PDF Converter Free Online — Webpage to PDF | PDFZaap",
    meta="Convert an HTML file to a PDF in your browser. Inline styles render reliably; A4 output. Free, private, no upload — your markup stays local.",
    h1="Convert HTML to PDF — Free & Private",
    intro="<p>Generated reports, saved web pages, hand-written HTML documents — all of them become shareable PDFs with this tool. Upload an <code>.html</code> (or plain <code>.txt</code>) file and the browser lays it out on A4 pages and hands you a PDF. The markup is rendered locally, so internal reports and client drafts never leave your machine.</p>",
    howto_title="turn an HTML file into a PDF",
    howto=[
        ("Select the HTML file", "Upload a single .html, .htm or .txt file."),
        ("Click Convert HTML to PDF", "The browser renders the markup onto A4 pages."),
        ("Wait for the render", "Longer documents take a moment as each page is rasterized."),
        ("Download the PDF", "Check the first and last pages, then share."),
    ],
    why_title="print web content without a server",
    why="<p><strong class='subtext'>Private for internal content.</strong> HTML reports often contain numbers and names you would not paste into an upload form. Here the file is read and rendered in your own tab — there is no upload step at all.</p><p class='subtext'><strong>Know the rendering model.</strong> The converter draws the page as it sees it: inline styles and <code>&lt;style&gt;</code> blocks render reliably; external stylesheets and remote images work only if your browser can reach them. Because the page is rendered as images per A4 sheet, the output looks exactly like the layout but the text is not selectable. If you need selectable text, your browser's own 'Print → Save as PDF' is the tool for that job — and we would rather point you there than pretend otherwise.</p>",
    tips=[
        "Inline your CSS (or paste it into a &lt;style&gt; tag) for the most predictable result.",
        "Keep line lengths under ~90 characters for documents that are mostly text.",
        "For plain text files, the converter wraps them in a clean document layout automatically.",
        "The reverse direction — PDF to editable HTML — is covered by <a href='/pdf-to-html.html'>PDF to HTML</a>.",
    ],
    when="<p>Use this when you have an <em>HTML file</em> and need a printable copy. For PDFs you want to read on the web, <a href='/pdf-to-html.html'>PDF to HTML</a> goes the other way. For Word sources, <a href='/word-to-pdf.html'>Word to PDF</a> is usually smoother. Our guide <a href='/blog/how-to-combine-scanned-receipts-into-one-pdf.html'>How to combine scanned receipts into one PDF</a> shows a related no-upload workflow.</p>",
    faqs=[
        ("Is the PDF text selectable?", "No — pages are rendered as images, so the visual is exact but the text cannot be copied. Use your browser's print dialog if you need selectable output."),
        ("Do linked CSS files work?", "They load only if your browser can fetch them from the same origin. Inlining styles ensures the result."),
        ("Can I convert a live website?", "No — this tool converts HTML files you upload. To save a live page, use your browser's 'Save page as…' first, then convert the saved file."),
        ("What page size is the output?", "A4 portrait, with the content flowing across as many pages as needed."),
    ],
    related=[("pdf-to-html", "PDF to HTML"), ("word-to-pdf", "Word to PDF"), ("png-to-pdf", "PNG to PDF"), ("jpg-to-pdf", "JPG to PDF")],
)

C["png-to-pdf"] = dict(
    title="PNG to PDF Converter Free — Combine Images | PDFZaap",
    meta="Combine one or more PNG images into a single PDF in your browser. Fit-to-image or A4/Letter pages. Free, private, no upload, no watermark.",
    h1="Combine PNG Images into One PDF",
    intro="<p>PNGs are the format of choice for screenshots, diagrams and graphics — and they rarely need to travel alone. This tool places your PNG files on PDF pages in the order you add them: each image can fill its own page, or be centered on a standard A4 / US Letter page. All embedding happens locally in your browser.</p>",
    howto_title="turn PNG images into a PDF",
    howto=[
        ("Select your PNGs", "Add as many images as you need, in the page order you want."),
        ("Choose a page layout", "Fit-to-image for full pages, or A4 / US Letter with centered images and margins."),
        ("Fix the order if needed", "Remove an image and re-add it to move it."),
        ("Click Convert to PDF", "Download the combined document when ready."),
    ],
    why_title="bundle graphics into documents privately",
    why="<p><strong class='subtext'>Local and watermark-free.</strong> Image-to-PDF sites typically upload your images, cap free usage, or stamp a watermark. This runs in your browser: the PNGs are embedded into the PDF in your tab and the file downloads to your device — no account, no watermark, no usage meter.</p><p class='subtext'><strong>PNG strengths, honestly stated.</strong> PNG keeps flat colors, text and line art crisp, which makes it ideal for diagrams and UI screenshots. The PDF pages remain raster — no searchable text layer is added. For photos where file size matters more than artifact-free edges, <a href='/jpg-to-pdf.html'>JPG to PDF</a> produces a smaller file at the same workflow.</p>",
    tips=[
        "Screenshots export perfectly — keep them at native resolution to avoid blur on A4 pages.",
        "For transparent PNGs, the PDF page is white behind the graphic; design with that in mind.",
        "Large batches: sort your files numerically before selecting, so the page order is the filename order.",
        "If the combined PDF is too heavy for an email, run <a href='/compress-pdf.html'>Compress PDF</a> afterwards.",
    ],
    when="<p>Use this for <em>graphics-heavy</em> documents; <a href='/jpg-to-pdf.html'>JPG to PDF</a> for photos; <a href='/merge-pdf.html'>Merge PDF</a> when you are combining existing PDFs; and <a href='/split-pdf.html'>Split PDF</a> to break a finished PDF apart. More in <a href='/blog/how-to-convert-jpg-to-pdf-on-windows.html'>How to convert JPG to PDF on Windows</a>.</p>",
    faqs=[
        ("Does it support transparency?", "The image keeps its transparency inside the PDF page, but the page background is white — there is no 'transparent PDF page' concept."),
        ("Can I combine many images?", "Yes, add as many PNGs as you need; each becomes one page."),
        ("Is there a file size limit?", "No hard limit — the browser handles the embedding locally, so your device's memory is the practical ceiling."),
        ("Why choose PNG over JPG for this?", "PNG is lossless for flat graphics and text. For photographs, JPG at good quality is smaller and usually fine — use the JPG tool for those."),
    ],
    related=[("jpg-to-pdf", "JPG to PDF"), ("pdf-to-png", "PDF to PNG"), ("merge-pdf", "Merge PDF"), ("compress-pdf", "Compress PDF")],
)

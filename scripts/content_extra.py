# Content for new long-tail pages (Step 10).
# compress-to-X pages: preset target for the compress tool.
# intent pages: tool + long-form intent content.

COMPRESS_SIZES = {}

def _cs(kb, label, angle_intro, where_from, extra_tips, faqs, when_links):
    return dict(
        kb=kb, label=label,
        angle_intro=angle_intro,
        where_from=where_from,
        extra_tips=extra_tips,
        faqs=faqs,
        when_links=when_links,
    )

COMPRESS_SIZES["compress-pdf-to-100kb"] = _cs(
    100, "100 KB",
    "<p>A 100 KB PDF limit usually comes from a job portal, a government form, or a visa/ID upload that only accepts small files. This page gives you a compress tool preset to 100 KB: select your document, and the tool finds the best quality that gets the result under 100 KB — and it tells you plainly when 100 KB is not reachable for that particular document.</p>",
    """<h2>Where 100 KB limits come from</h2>
<p>Small attachment caps show up in a few predictable places:</p>
<ul class="tips-list">
  <li><strong>Job application portals</strong> — many older ATS systems cap CV/resume uploads at 100 KB to keep their database lean.</li>
  <li><strong>Government forms</strong> — ID cards, certificates and form uploads frequently enforce 100 KB or 200 KB ceilings.</li>
  <li><strong>Visa and embassy upload systems</strong> — scanned documents are often required under 100 KB per file.</li>
  <li><strong>Legacy corporate systems</strong> — internal portals built before broadband-era file sizes still enforce tiny caps.</li>
</ul>
<p>The exact number varies by portal, so always check the instructions of the specific form you are answering. If the portal says 100 KB, aim for 90–95 KB to leave headroom for how the portal measures (KB vs. KiB).</p>""",
    ["If a photo-heavy CV will not reach 100 KB, remove the photo first — a single 300 dpi headshot can cost more than the whole document budget.",
     "Scan or export your CV at 150 dpi instead of 300 dpi before compressing; the lower source resolution makes 100 KB far more reachable.",
     "Keep the compressed file in a separate folder and check it opens correctly before uploading — the upload screen rarely tells you why a file was rejected.",
     "If the portal rejects the file after compression, the limit may be on page count or file format as well as size — check the portal's requirements page."],
    [("Can any PDF be compressed to 100 KB?", "Not always. Image-heavy or long documents may not reach 100 KB without becoming unreadable. The tool reports the smallest size it achieved and says honestly when the target was not met.", ),
     ("What makes a PDF hard to compress to 100 KB?", "Long page counts, high-resolution photos, and dense vector graphics. A 5-page text CV is a different problem from a 30-page report with photographs.", ),
     ("Will the text stay readable at 100 KB?", "For typical documents, yes at the quality the tool settles on. Check a sample page after compression, especially small-print sections.", ),
     ("Does the tool add anything to the file?", "No watermark, no branding, no metadata changes beyond what compression requires. The output is your document, smaller.", ),
     ("Why not just resize the images manually?", "You could, in a graphics editor, per image — the preset automates the quality search so you do not have to guess and re-export repeatedly.")],
    "If 100 KB is not reachable, step up: try <a href='/compress-pdf-to-200kb.html'>compress to 200 KB</a> and check whether the portal accepts the larger file. For the general workflow, see <a href='/compress-pdf.html'>Compress PDF</a> and our guide to <a href='/blog/compress-pdf-for-email.html'>compressing a PDF for email</a>.",
)

COMPRESS_SIZES["compress-pdf-to-200kb"] = _cs(
    200, "200 KB",
    "<p>Two hundred kilobytes is the most common job-portal ceiling we see: large enough for a two-to-four page CV with a photo, small enough for legacy systems. This page presets the compressor to 200 KB — the tool searches for the best quality that lands under the limit and reports the actual result size.</p>",
    """<h2>Where 200 KB limits come from</h2>
<p>200 KB is a sweet spot for systems that want a bit more room than 100 KB but still want to constrain uploads:</p>
<ul class="tips-list">
  <li><strong>National job portals and public-sector applications</strong> — many cap resumes at 200 KB.</li>
  <li><strong>University admission forms</strong> — transcripts and identity documents are often required under 200 KB per file.</li>
  <li><strong>Government certificate uploads</strong> — a common ceiling for scanned certificates and ID documents.</li>
  <li><strong>Freelance platforms</strong> — proposal attachments sometimes carry the same cap.</li>
</ul>
<p>As with any cap, confirm the exact requirement on the form itself — some portals say 200 KB, others 200 KiB, and a few measure per-file versus per-application.</p>""",
    ["A 200 KB budget comfortably fits a 2–4 page CV with one photo at readable quality — if yours will not fit, the photo is the usual suspect.",
     "Convert multi-page documents by compressing the whole file; the tool balances quality across all pages rather than sacrificing the later ones.",
     "After downloading, rename the file to something clean (yourname-cv.pdf) — portals sometimes reject unusual characters in file names.",
     "If the result lands just over the limit (e.g. 205 KB), re-run at a slightly lower manual quality on the <a href='/compress-pdf.html'>Compress PDF</a> page to shave the remainder."],
    [("Is 200 KB enough for a photo CV?", "Usually yes for up to about four pages. A high-resolution photo is the first thing the compression has to give up — expect the photo to soften slightly before the text does.", ),
     ("What if my document is 30 pages?", "Long documents are harder to fit into 200 KB. Consider extracting only the pages the form asks for with <a href='/split-pdf.html'>Split PDF</a> before compressing.", ),
     ("Does the output quality depend on the input?", "Yes. A crisp text document compresses to a much sharper result at 200 KB than a photo-heavy one, because there is less image data to trade away.", ),
     ("Can I use this for email instead of a portal?", "Absolutely — 200 KB is a size that travels through any email system. See our <a href='/blog/compress-pdf-for-email.html'>compress PDF for email</a> guide for the full picture."),
    ],
    "If 200 KB is too tight, the next step up is <a href='/compress-pdf-to-500kb.html'>compress to 500 KB</a>; for email attachments generally, <a href='/compress-pdf-to-2mb.html'>compress to 2 MB</a> is the classic target. The general tool is <a href='/compress-pdf.html'>Compress PDF</a>.",
)

COMPRESS_SIZES["compress-pdf-to-500kb"] = _cs(
    500, "500 KB",
    "<p>Scholarship applications and university portals are the usual source of a 500 KB rule — big enough for a statement of purpose plus a transcript, small enough to keep the application server fast. This page presets the compressor to 500 KB and reports the exact result size after processing.</p>",
    """<h2>Where 500 KB limits come from</h2>
<ul class="tips-list">
  <li><strong>Scholarship applications</strong> — essay PDFs, transcripts and recommendation letters are commonly capped per file.</li>
  <li><strong>University admission portals</strong> — supporting documents (ID, certificates, transcripts) often share a 500 KB per-file ceiling.</li>
  <li><strong>Research and grant applications</strong> — CV and cover-document uploads with mid-size caps.</li>
  <li><strong>Internal HR systems</strong> — onboarding document uploads that allow more room than a job portal but not unlimited size.</li>
</ul>
<p>At 500 KB you have roughly five times the budget of a 100 KB cap, which changes the math: most 3–8 page documents with modest images fit without visible quality loss. The tool will tell you exactly where yours lands.</p>""",
    ["For scholarship essays, keep the source clean: plain text, standard font, no background graphics — it compresses far better than a designed document.",
     "Upload one file per document (essay, transcript, ID separately) rather than a merged bundle, unless the form explicitly asks for a single PDF — use <a href='/merge-pdf.html'>Merge PDF</a> only when required.",
     "Check the final size after compression, not before — the tool's result note shows original versus compressed size side by side.",
     "If a scanned transcript will not reach 500 KB, re-scan at 200 dpi; text stays perfectly legible and the file shrinks dramatically."],
    [("Will a 10-page document fit in 500 KB?", "Often yes if it is mostly text. Photo-heavy documents are the exception — the honest note in the result tells you if the target was not reached.", ),
     ("Do I need to compress before or after merging?", "Compress after merging. Merging does not change quality, and compressing the final file is one step instead of several.", ),
     ("Is 500 KB enough for a letter with a photo?", "Yes — a single standard photograph plus a few pages of text fits comfortably in most cases.", ),
     ("What if the portal actually wants 500 KB or less including the file name?", "File names do not count toward size — only the bytes of the file. But keep the name clean; some legacy portals are picky about characters.")],
    "If your real limit is smaller, step down to <a href='/compress-pdf-to-200kb.html'>200 KB</a> or <a href='/compress-pdf-to-100kb.html'>100 KB</a>; for larger university bundles, <a href='/compress-pdf-to-1mb.html'>1 MB</a> is the next rung. The general tool: <a href='/compress-pdf.html'>Compress PDF</a>.",
)

COMPRESS_SIZES["compress-pdf-to-1mb"] = _cs(
    1024, "1 MB",
    "<p>One megabyte is the most forgiving of the common portal limits — enough for a substantial application bundle: several pages of text plus scanned certificates. This page presets the compressor to 1 MB (1,024 KB) and gives you an honest report of the final size.</p>",
    """<h2>Where 1 MB limits come from</h2>
<ul class="tips-list">
  <li><strong>University application bundles</strong> — combined documents (transcript + ID + letters) under a per-file 1 MB rule.</li>
  <li><strong>Scholarship and fellowship portals</strong> — larger document caps than 500 KB systems.</li>
  <li><strong>Visa support document uploads</strong> — some embassies allow 1 MB per supporting file.</li>
  <li><strong>Corporate document management systems</strong> — mid-size per-file caps on shared drives and intake portals.</li>
</ul>
<p>At 1 MB, the constraint is rarely the document's content and more often the source quality: a 300 dpi scan of a 6-page transcript is already near 1 MB before compression, while a 150 dpi version is comfortably under it. The preset finds the quality that fits, so you do not have to re-scan by trial and error.</p>""",
    ["For multi-document bundles, merge first (<a href='/merge-pdf.html'>Merge PDF</a>), then compress once — one pass over the whole bundle beats compressing each file separately.",
     "If the bundle is close to 1 MB even after compression, remove the lowest-value page (a cover sheet, a duplicate) before re-running.",
     "Keep a copy of the uncompressed original — if the portal bounces the file, you can re-export at higher quality without re-scanning.",
     "Measure with the tool's result note: it states the exact compressed size, so you know whether you are at 0.9 MB or 1.1 MB."],
    [("Can I merge several documents and still stay under 1 MB?", "Frequently yes, especially if they are text-based. Compress after merging so the whole bundle is balanced against the limit in one pass.", ),
     ("What is 1 MB in KB?", "1 MB is 1,024 KB. The preset targets under 1,024 KB, which matches how most portals phrase the limit.", ),
     ("Will a scanned diploma look good at 1 MB?", "A single-page scanned diploma compresses well and stays crisp. Multi-page high-resolution scans are the harder case.", ),
     ("Why does my 4 MB file not reach 1 MB?", "If it is mostly dense text or already-optimized images, re-rendering cannot remove much. The result note says so, and the next lever is removing pages or reducing scan resolution at the source.")],
    "Smaller targets: <a href='/compress-pdf-to-500kb.html'>500 KB</a> and <a href='/compress-pdf-to-200kb.html'>200 KB</a>. For email attachment limits rather than portals, <a href='/compress-pdf-to-2mb.html'>2 MB</a> is the usual target. General tool: <a href='/compress-pdf.html'>Compress PDF</a>.",
)

COMPRESS_SIZES["compress-pdf-to-2mb"] = _cs(
    2048, "2 MB",
    "<p>Two megabytes is the classic email-attachment target: small enough for legacy mail gateways, shared inboxes and old corporate systems, large enough for a real document with images. This page presets the compressor to 2 MB (2,048 KB) and reports the exact final size.</p>",
    """<h2>Where 2 MB limits come from</h2>
<ul class="tips-list">
  <li><strong>Corporate email gateways</strong> — older mail systems and some industry-specific inboxes cap attachments well below modern limits.</li>
  <li><strong>Government and public-sector email</strong> — attachment restrictions that predate current consumer mail norms.</li>
  <li><strong>Client-facing workflows</strong> — sending contracts, reports or invoices to recipients on restricted systems.</li>
  <li><strong>Upload forms that mirror email limits</strong> — web forms built around the same 2 MB convention.</li>
</ul>
<p>Modern consumer email allows much larger attachments, so 2 MB matters most when you do not control the receiving side. The preset gets you under the line with the least quality loss the file can sustain — and if the file is already efficient, it tells you the compression was not worth it.</p>""",
    ["If the recipient uses a modern mailbox, ask whether you can skip compression entirely — a 5 MB PDF is usually fine between consumer accounts.",
     "For invoices and reports, 2 MB leaves room for several pages of images; check the result note to see how much you actually saved.",
     "Combine with a clear file name and a short cover note — at 2 MB the file is still light enough to send with context.",
     "If the document is a scanned contract, compress to 2 MB rather than re-scanning at low resolution: the quality headroom is large at this limit."],
    [("Is 2 MB enough for a photo report?", "For most 5–15 page reports with standard images, yes. Very high-resolution photo spreads are the exception.", ),
     ("Why compress to 2 MB when Gmail allows 25 MB?", "Because the limit is often the recipient's system, not yours. Legacy corporate and public-sector mail is where 2 MB still bites.", ),
     ("What if my file is already under 2 MB?", "You do not need to compress it. Compression trades quality for size — if you are already under the limit, keep the original.", ),
     ("Does the tool ever make the file bigger?", "It can, on already-efficient files — and the result note flags that explicitly so you keep the original instead.")],
    "For portal-specific limits, see the size guides: <a href='/compress-pdf-to-1mb.html'>1 MB</a>, <a href='/compress-pdf-to-500kb.html'>500 KB</a>, <a href='/compress-pdf-to-200kb.html'>200 KB</a>, <a href='/compress-pdf-to-100kb.html'>100 KB</a>. The full email workflow is in our guide <a href='/blog/compress-pdf-for-email.html'>How to compress a PDF for email</a>, and the general tool is <a href='/compress-pdf.html'>Compress PDF</a>.",
)

# ---------------------------------------------------------------- intent pages

INTENT = {}

INTENT["merge-pdf-without-uploading"] = dict(
    tool="merge-pdf",
    title="Merge PDF Without Uploading — Private, Local Merge | PDFZaap",
    meta="Merge PDFs without uploading them: the merge runs entirely in your browser. Free, private, no watermark — plus a guide to verify no upload happens.",
    h1="Merge PDF Without Uploading Your Files",
    direct_answer="<p><strong>Quick answer:</strong> Yes — this merge tool combines PDF files entirely in your browser. The files are read from your device, merged in your tab's memory, and the result is downloaded back to your device. There is no upload step in the architecture, and you can confirm it yourself in the browser's Network tab (steps at the bottom of this page).</p>",
    intro="<p>'Merge PDF without uploading' is one of the most searched phrases around document tools, and the reason is straightforward: merging usually involves exactly the files you would least like to hand over — contracts, invoices, scans of IDs, HR records. This page combines two things: a merge tool that runs entirely client-side, and the context you need to trust that claim, including how to verify it with your own browser.</p>",
    extra_sections="""<h2>What 'without uploading' actually means</h2>
<p>There are three levels of privacy in online PDF tools, and the difference matters:</p>
<ul class="tips-list">
  <li><strong>Server-upload tools.</strong> Your browser sends the file to a server; the server processes it; the file is deleted after a stated delay (or not). Privacy depends on the provider's infrastructure and policies.</li>
  <li><strong>Hybrid tools.</strong> Small files may process locally; larger ones go to a server. The boundary is usually not visible to you.</li>
  <li><strong>Client-side tools.</strong> The file never leaves the device. The browser reads it with a file-picker API, the processing libraries run in your tab (WebAssembly/JavaScript), and the result is written back by a download. There is no network path for the document at all.</li>
</ul>
<p>This tool is in the third category. The page's network traffic is the page's assets — styles, scripts, fonts — and nothing else carries your document.</p>
<h2>Verify it yourself (3 minutes)</h2>
<p>You do not have to take our word for it — or anyone's. The check is the same for any PDF site:</p>
<ol class="tips-list">
  <li>Open the tool page and press <strong>F12</strong> (or right-click → Inspect) to open developer tools.</li>
  <li>Click the <strong>Network</strong> tab and make sure recording is on (the red dot).</li>
  <li>Reload the page once to see the baseline requests, then clear the list.</li>
  <li>Select your file and run the merge.</li>
  <li>Watch the request list: with a client-side tool you will see <strong>no request carrying your file</strong> — no upload, no PUT, no file-named POST. The merge happens silently in your tab, and the result appears as a download.</li>
</ol>
<p>We walk through this with screenshots-level detail in our guide <a href='/blog/how-to-check-if-pdf-tool-uploads-files.html'>How to check if an online PDF tool uploads your files</a> — and the guide is designed to work on any site, including competitors.</p>""",
    howto_title="merge PDFs without uploading",
    howto=[
        ("Add your PDFs", "Click the dropzone and select the files to combine. They are read locally — nothing is transmitted when you select them."),
        ("Check the order", "Files are merged in the order selected. Remove and re-add a file to change its position."),
        ("Click Merge PDFs", "The browser copies every page from every file into one new document, in memory."),
        ("Download the combined PDF", "The finished file saves to your device. Total time is typically seconds, depending on document size and your hardware."),
    ],
    why_title="keep sensitive merges on your device",
    why="<p><strong class='subtext'>The files you merge are the files you protect.</strong> A merged contract bundle, a stack of invoices, or scanned IDs combined for an application are the documents where 'their server' is exactly where you do not want a copy to exist — even temporarily. A client-side merge eliminates the category of risk: there is no upload endpoint on this site, so there is nothing to leak, mis-store or retain.</p><p class='subtext'><strong>Lossless, and honest about its model.</strong> Merging copies original page objects into the new document — no re-encoding, no quality loss, text stays selectable. The limits are practical, not privacy-based: very large batches consume browser memory, and encrypted files must be <a href='/unlock-pdf.html'>unlocked first</a> (with the password) before they can be merged. Those are the same limits any local PDF operation has.</p>",
    tips=[
        "For the privacy-check workflow, use a test file rather than a sensitive one — the point is observing network behavior, and a dummy PDF proves it as well.",
        "Number your files (01-, 02-, 03-) before selecting so the merge order is obvious without counting.",
        "After merging a large bundle, check the page count in a PDF reader before sending — merging is lossless, so the count should be the sum of the inputs.",
        "Pair with <a href='/compress-pdf.html'>Compress PDF</a> when the combined file has to meet a size limit — compress after merging, not before.",
        "On mobile, the same no-upload model applies: the phone's browser does the merging locally too. See <a href='/blog/how-to-merge-pdf-files-on-iphone.html'>merging on iPhone</a> for the mobile walkthrough.",
    ],
    when="<p>This page targets the <em>privacy intent</em>: 'merge pdf without uploading', 'merge pdf offline', 'private pdf merger'. The tool is identical to our standard <a href='/merge-pdf.html'>Merge PDF</a> page — same engine, same free, unlimited use — with the verification guide attached. If you just need to combine files quickly, either page works. For the reverse operation, <a href='/split-pdf.html'>Split PDF</a>; for size limits on the result, the <a href='/compress-pdf-to-200kb.html'>compress to 200 KB</a> preset. And to evaluate any PDF tool's privacy claim, start with <a href='/is-it-safe-to-use-online-pdf-tools.html'>Is it safe to use online PDF tools?</a>.</p>",
    faqs=[
        ("Do my files leave my computer at any point?", "No. The browser reads the files from disk, the merge runs in your tab's memory, and the download writes the result back to your device. The only network traffic is the page's own assets."),
        ("Does this work offline?", "Once the page and its scripts have loaded, the merge itself needs no network connection. You can disable the network in your browser after loading and the tool will still work — a nice demonstration of where the processing happens."),
        ("Is the merge quality preserved?", "Yes — pages are copied structurally, not re-rendered. No compression, no quality loss, no watermark."),
        ("How is this different from server-based mergers?", "Server mergers upload your files, process them remotely and return the result — convenient for very heavy batches, but the document exists on someone else's infrastructure. Here, that step does not exist at all."),
        ("Can I verify the no-upload claim?", "Yes — use the Network-tab steps above, or follow our full guide linked on this page. The check takes about three minutes and works on any PDF tool site."),
    ],
    related=[("merge-pdf", "Merge PDF"), ("compress-pdf", "Compress PDF"), ("split-pdf", "Split PDF"), ("protect-pdf", "Protect PDF")],
)

INTENT["jpg-to-pdf-a4"] = dict(
    tool="jpg-to-pdf",
    title="JPG to PDF A4 — Images on Standard A4 Pages Free | PDFZaap",
    meta="Combine JPG images into a PDF on standard A4 pages: each image centered and scaled to fit. Free, private, no upload — built for A4-expecting portals.",
    h1="JPG to PDF — A4 Page Size",
    direct_answer="<p><strong>Quick answer:</strong> This tool puts each JPG on its own A4 page (210 × 297 mm), scaled to fit with margins and centered. It runs entirely in your browser — select images, choose the A4 preset, download the PDF. No upload, no watermark, no account.</p>",
    intro="<p>Most image-to-PDF tools make each image its own page sized to the image — which is wrong when the destination expects a standard page. Job portals, government forms and university systems frequently expect <strong>A4</strong>: a full A4 sheet per document, with the content sitting inside it. This page presets JPG-to-PDF to A4 so your images land on proper standard pages, centered and scaled to fit — processed locally in your browser.</p>",
    extra_sections="""<h2>Why A4 specifically</h2>
<ul class="tips-list">
  <li><strong>Portal validation</strong> — many upload forms check page dimensions, not just file type. An image-sized page (say 4032 × 3024 px) can be rejected where an A4 page is accepted.</li>
  <li><strong>Print consistency</strong> — A4 pages print at 100% on A4 printers worldwide with no 'fit to page' guesswork.</li>
  <li><strong>International standard</strong> — A4 is the default paper size outside North America; for applications to international institutions it is the safe default.</li>
</ul>
<h2>How the A4 layout works</h2>
<p>Each image is scaled down to fit the A4 page with a 24 pt margin and centered — horizontally and vertically. Images are <strong>never upscaled</strong> beyond their native resolution: a small image on an A4 page simply appears smaller, which is the correct behavior (stretching would blur it). Portrait and landscape images are both handled; a landscape photo on a portrait A4 page is fitted within the width and centered vertically.</p>""",
    howto_title="put JPG images on A4 pages",
    howto=[
        ("Select your JPGs", "Add the images in the page order you want — each one becomes one A4 page."),
        ("Choose A4 in Page size", "The Page size menu defaults to fit-to-image; select 'A4 (210 × 297 mm) — image centered'."),
        ("Fix the order if needed", "Remove an image and re-add it to move it."),
        ("Click Convert to PDF and download", "The result is a standard A4 PDF, ready for portals that check page size."),
    ],
    why_title="meet A4 requirements without a server",
    why="<p><strong class='subtext'>The rejection you are trying to avoid.</strong> 'File format invalid' and 'page size not supported' are the two classic portal rejections for image PDFs. A4 layout fixes the second one at the source: every page in the output is exactly 595 × 842 points (A4 in PDF units), so dimension-checking portals see what they expect.</p><p class='subtext'><strong>Local, watermark-free, unlimited.</strong> The images are embedded in the PDF in your browser tab — no upload, no watermark, no per-day cap. The honest limitation is the same as any raster conversion: the pages are images, so there is no text layer. If the portal also requires searchable text, you need an OCR step on the source images (see <a href='/ocr-pdf.html'>OCR PDF</a>) or a text-based document instead.</p>",
    tips=[
        "Phone photos are landscape by default; if the portal expects portrait A4, rotate the photos before combining (or accept the centered landscape block).",
        "For scanned documents, 300 dpi sources look best on A4 — a 3000 px wide scan fills the page cleanly.",
        "If the combined A4 PDF exceeds a size limit, run <a href='/compress-pdf.html'>Compress PDF</a> with a target size afterwards.",
        "US-based portals that require Letter instead of A4: use the same tool on the <a href='/jpg-to-pdf.html'>JPG to PDF</a> page with the US Letter option.",
        "Step-by-step on Windows (including the A4 choice): <a href='/blog/how-to-convert-jpg-to-pdf-on-windows.html'>How to convert JPG to PDF on Windows</a>.",
    ],
    when="<p>Use this page when the requirement is <em>images on standard A4 pages</em>. For fit-to-image pages (each image fills its page), use <a href='/jpg-to-pdf.html'>JPG to PDF</a>. For PNG graphics, <a href='/png-to-pdf.html'>PNG to PDF</a> (with the same A4 option). When the final PDF has to be small as well as A4, follow with <a href='/compress-pdf-to-1mb.html'>compress to 1 MB</a> or <a href='/compress-pdf-to-2mb.html'>compress to 2 MB</a>.</p>",
    faqs=[
        ("Is the output really A4?", "Yes — every page is exactly A4 (210 × 297 mm, 595.28 × 841.89 pt in PDF units). You can verify in any PDF reader's document properties."),
        ("Why is my small photo small on the page?", "Images are centered and scaled to fit, but never enlarged beyond their native resolution. A 640 px photo on A4 looks smaller but stays sharp — upscaling would only blur it."),
        ("Can I mix portrait and landscape images?", "Yes. Each image is fitted to the A4 page independently, so mixed orientations are fine."),
        ("Is the text in my images searchable?", "No — the pages are raster images. For searchable scans, OCR the source images first with <a href='/ocr-pdf.html'>OCR PDF</a> and build a text document, or accept the image-only output."),
        ("Does it work on a phone?", "Yes — select images from your gallery, pick A4, and convert. The processing happens on the phone itself."),
    ],
    related=[("jpg-to-pdf", "JPG to PDF"), ("png-to-pdf", "PNG to PDF"), ("compress-pdf", "Compress PDF"), ("resize-pdf", "Resize PDF")],
)

INTENT["pdf-to-word-without-losing-formatting"] = dict(
    tool="pdf-to-word",
    title="PDF to Word Without Losing Formatting — Free Guide | PDFZaap",
    meta="What PDF-to-Word conversion can honestly deliver, tier by tier, plus a free in-browser converter that runs privately. Guide + tool.",
    h1="Convert PDF to Word Without Losing Formatting",
    direct_answer="<p><strong>Quick answer:</strong> 'Without losing formatting' has a spectrum. Text-based converters keep every word, paragraph order and page breaks — but complex layouts (multi-column, floating tables) simplify. This page explains the honest tiers of conversion quality and gives you a free, private, in-browser PDF-to-Word tool to get the best achievable result.</p>",
    intro="<p>Every 'PDF to Word without losing formatting' page makes the same promise, and most of them do not explain what the promise can actually deliver. This one does: the three tiers of conversion quality, what determines which tier you land in, and the settings and habits that move a conversion up a tier. Below the guide is our free in-browser converter — private because it runs on your device, and honest about its output, which is a text-based conversion.</p>",
    extra_sections="""<h2>The three tiers of conversion quality</h2>
<table class="post-table" style="width:100%;border-collapse:collapse;font-size:0.95rem;margin:1rem 0;">
  <tr style="background:var(--primary-light);"><th style="border:1px solid var(--border);padding:8px;text-align:left;">Tier</th><th style="border:1px solid var(--border);padding:8px;text-align:left;">What survives</th><th style="border:1px solid var(--border);padding:8px;text-align:left;">What gives</th></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Layout-perfect</strong></td><td style="border:1px solid var(--border);padding:8px;">Everything — positions, columns, tables, fonts</td><td style="border:1px solid var(--border);padding:8px;">Nothing, but it requires heavy server-side engines and is expensive/limited</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Structure-aware</strong></td><td style="border:1px solid var(--border);padding:8px;">Words, paragraphs, headings, page breaks</td><td style="border:1px solid var(--border);padding:8px;">Exact positions, merged tables become rows</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Text-only</strong></td><td style="border:1px solid var(--border);padding:8px;">Words in reading order</td><td style="border:1px solid var(--border);padding:8px;">Everything visual</td></tr>
</table>
<p>Browser-based tools sit at the structure-aware tier: they rebuild the document from the text the PDF contains, which keeps content and order without cloning geometry. That is the honest ceiling of what runs on your device — and for the majority of real documents (reports, letters, forms, manuscripts), it is what you actually need.</p>
<h2>What determines your result</h2>
<ul class="tips-list">
  <li><strong>Source quality.</strong> A PDF exported from Word converts better than a scanned one (scans need <a href='/ocr-pdf.html'>OCR</a> first) and better than a designed multi-column one.</li>
  <li><strong>Text layer integrity.</strong> PDFs with clean text objects convert cleanly; PDFs with fragmented text runs (common in some exporters) can read in slightly scrambled order.</li>
  <li><strong>What you define as 'formatting'.</strong> If you need the words and the structure, a structure-aware conversion delivers. If you need the visual layout pixel-for-pixel, no free converter — browser or server — will do that reliably, and the right move is to re-export from the source document.</li>
</ul>
<h2>Habits that improve the outcome</h2>
<ol class="tips-list">
  <li>Convert a copy, keep the PDF as the master — conversion is a one-way street.</li>
  <li>Check the first and last page immediately; pagination problems hide at the ends.</li>
  <li>For long documents, convert in two halves and compare — it is faster to spot a bad section.</li>
  <li>Rebuild complex tables by hand; no converter makes them perfect.</li>
</ol>
<p>The deeper walkthrough — including Mac-specific notes and when a server tool is worth the upload — is in our guide <a href='/blog/pdf-to-word-without-losing-formatting.html'>How to convert a PDF to Word without losing formatting</a>, and the Mac angle in <a href='/blog/how-to-convert-pdf-to-word-on-mac-free.html'>converting on Mac for free</a>.</p>""",
    howto_title="convert a PDF to Word here",
    howto=[
        ("Select the PDF", "Choose the document you want to make editable."),
        ("Click Convert to Word", "The browser extracts the text and builds a .docx — locally, in seconds to minutes depending on length."),
        ("Download the .docx", "Open it in Word, Google Docs or LibreOffice."),
        ("Spot-check structure", "Scan the first and last pages, and one middle page, for order and completeness."),
    ],
    why_title="a private converter with an honest spec",
    why="<p><strong class='subtext'>Private by architecture.</strong> The converter runs in your browser: the PDF is parsed locally and the Word file is assembled locally. For documents you are repurposing — contracts being redrafted, client work being re-templated — that means the sensitive file never uploads anywhere. There is no free-tier meter, watermark or account, because there is no server holding your document.</p><p class='subtext'><strong>And the spec, stated plainly:</strong> text-based, structure-aware conversion. Words, paragraph order and page breaks are preserved; complex visual layout is simplified. If a document is design-critical, we will tell you that browser conversion is not the right tool rather than pretend otherwise — see the tiers table above.</p>",
    tips=[
        "For a scanned PDF, run <a href='/ocr-pdf.html'>OCR PDF</a> first, then convert the recognized text — direct conversion of a scan yields nothing.",
        "If the reading order is scrambled, the PDF probably uses floating text boxes; converting page ranges separately (<a href='/split-pdf.html'>Split PDF</a> first) often cleans it up.",
        "Keep the original PDF named as the master (document-v1.pdf) and the conversion as a working copy (document-v1-edit.docx).",
        "Going the other way — Word to a locked PDF — is the <a href='/word-to-pdf.html'>Word to PDF</a> tool, also local.",
    ],
    when="<p>This page targets the intent <em>'pdf to word without losing formatting'</em>: the guide explains what the phrase can honestly mean, and the tool does the conversion privately. For plain text extraction, <a href='/pdf-to-text.html'>PDF to Text</a> is lighter. For spreadsheets in the PDF, <a href='/pdf-to-excel.html'>PDF to Excel</a>. Full guides: <a href='/blog/pdf-to-word-without-losing-formatting.html'>without losing formatting</a> and <a href='/blog/how-to-convert-pdf-to-word-on-mac-free.html'>on Mac, free</a>.</p>",
    faqs=[
        ("Will my tables convert perfectly?", "Table content converts as text rows; the table grid itself is not rebuilt as a Word table. Expect to re-draw complex tables — that is true of every free converter, browser or server."),
        ("What about multi-column layouts?", "Text is ordered top-to-bottom by position, so dense multi-column designs can read out of their visual sequence. Single-column documents convert cleanly."),
        ("Is this tool free for large documents?", "Yes — there is no page cap. Very large documents take longer because all processing is on your device."),
        ("Can I convert a scanned PDF directly?", "Not usefully — a scan has no text layer. OCR the pages first, then work with the recognized text."),
        ("Where does my file go during conversion?", "Nowhere. It is read from disk by your browser and the .docx is written back by the download. No upload step exists in this tool."),
    ],
    related=[("pdf-to-word", "PDF to Word"), ("pdf-to-text", "PDF to Text"), ("ocr-pdf", "OCR PDF"), ("word-to-pdf", "Word to PDF")],
)

INTENT["is-it-safe-to-use-online-pdf-tools"] = dict(
    tool=None,
    title="Is It Safe to Use Online PDF Tools? How to Tell | PDFZaap",
    meta="Server-upload vs. client-side PDF tools explained, with a 5-minute DevTools test to verify any tool — including this one — yourself.",
    h1="Is It Safe to Use Online PDF Tools?",
    direct_answer="<p><strong>Quick answer:</strong> It depends on where the processing happens. Server-based tools upload your file to their infrastructure — your privacy then depends on their security and deletion policy. Client-side tools (like PDFZaap) process the file entirely in your browser, so it never leaves your device. You can verify which kind any tool is with the 5-minute test below.</p>",
    intro="<p>'Is it safe?' is the right question to ask before uploading a contract, a scan of your ID, or a client's document to any website — PDF tools included. This page explains the two architectures in plain language, what each one actually means for your privacy, and gives you a test you can run on any site, including this one, so you do not have to trust a marketing claim (ours or anyone else's).</p>",
    extra_sections="""<h2>Two architectures, two privacy models</h2>
<table class="post-table" style="width:100%;border-collapse:collapse;font-size:0.95rem;margin:1rem 0;">
  <tr style="background:var(--primary-light);"><th style="border:1px solid var(--border);padding:8px;text-align:left;"></th><th style="border:1px solid var(--border);padding:8px;text-align:left;">Server-upload tools</th><th style="border:1px solid var(--border);padding:8px;text-align:left;">Local (client-side) tools</th></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Where the file is processed</strong></td><td style="border:1px solid var(--border);padding:8px;">On the provider's servers</td><td style="border:1px solid var(--border);padding:8px;">In your browser, on your device</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Does the file leave your device?</strong></td><td style="border:1px solid var(--border);padding:8px;">Yes — always, that is the model</td><td style="border:1px solid var(--border);padding:8px;">No</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>What you are trusting</strong></td><td style="border:1px solid var(--border);padding:8px;">The provider's security, retention policy, and the laws governing its data</td><td style="border:1px solid var(--border);padding:8px;">Your own browser's file handling (nothing else)</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Typical strengths</strong></td><td style="border:1px solid var(--border);padding:8px;">Handles very heavy documents; advanced engines (OCR, layout-perfect conversion)</td><td style="border:1px solid var(--border);padding:8px;">Privacy by architecture; works after the page loads, even offline</td></tr>
  <tr><td style="border:1px solid var(--border);padding:8px;"><strong>Typical limits</strong></td><td style="border:1px solid var(--border);padding:8px;">File exists on someone else's infrastructure; free tiers may meter usage</td><td style="border:1px solid var(--border);padding:8px;">Uses your device's memory/CPU; some advanced operations are not feasible in a browser</td></tr>
</table>
<p>Neither model is 'safe' or 'unsafe' by default — they are different risk models. A reputable server tool with strong security and a short retention window is a reasonable choice for non-sensitive files. For sensitive files, the client-side model removes the server risk entirely, because the file is never in transit or at rest on someone else's machine.</p>
<h2>How client-side PDF tools work (the short version)</h2>
<p>Modern browsers can run substantial software locally — the same kind of processing that used to require a server, compiled to <strong>WebAssembly</strong> or plain JavaScript. A client-side PDF tool loads those libraries from a CDN when the page opens, and from that moment: your file is read from disk by the browser's file API, the library processes it in your tab's memory, and the result is handed back to you as a download. The document has no network path — not at upload time, not during processing, not at download time. PDFZaap works this way for all 35 tools.</p>
<h2>The 5-minute verification test (any site)</h2>
<ol class="tips-list">
  <li><strong>Open developer tools.</strong> On the tool page, press F12 (Windows/Linux) or Cmd+Option+I (Mac), or right-click the page and choose Inspect.</li>
  <li><strong>Go to the Network tab.</strong> Confirm recording is active (red dot lit). If there is a filter bar, leave it unfiltered.</li>
  <li><strong>Set a baseline.</strong> Reload the page once. You will see requests for the page's assets — HTML, CSS, JavaScript libraries, fonts. Note them. Then use the clear button (🚫) to empty the list.</li>
  <li><strong>Run the tool with a real file.</strong> Select a document (a non-sensitive test file is fine) and click the process button. Watch the request list while it works.</li>
  <li><strong>Read the result.</strong> A client-side tool shows <em>no new request carrying your file</em> — no upload, no file-named request, no POST with your document. A server tool shows a clear upload: a request to the provider's API with your file, usually followed by a progress indication. That single observation is the answer to 'is it safe?' — you now know which model the site runs.</li>
</ol>
<p>We wrote this test as a standalone guide with more detail: <a href='/blog/how-to-check-if-pdf-tool-uploads-files.html'>How to check if an online PDF tool uploads your files</a>.</p>
<h2>What PDFZaap does and does not claim</h2>
<ul class="tips-list">
  <li><strong>We claim:</strong> all 35 tools run client-side; your files are processed in your browser and are not uploaded to our servers; there is no upload endpoint on the site; the only downloads are page assets and (for the OCR tool's first run) the public English language model from the Tesseract project's CDN — the same model file every Tesseract user downloads.</li>
  <li><strong>We do not claim:</strong> that client-side processing makes you invulnerable. Your device's own security matters: a malware-infected machine can access any file your browser can. Local processing reduces exposure to <em>the website</em>; it does not replace basic device hygiene.</li>
  <li><strong>We do not claim:</strong> that every operation is possible locally. Some things — certified PDF/A validation, layout-perfect PDF-to-Word, OCR in 100 languages — are not feasible in a browser, and we say so on the relevant tool pages instead of faking them.</li>
</ul>
<h2>When a server tool is still the right call</h2>
<p>Honest guidance cuts both ways: for a routine, non-sensitive file where you need a capability the browser cannot do (a certified PDF/A conversion, a 200-page OCR job in many languages), a reputable server tool is fine — and checking its privacy policy and retention window before uploading is the sensible habit. The Network-tab test above is the quickest way to know what you are agreeing to, on any site.</p>""",
    faqs=[
        ("Is PDFZaap really 100% client-side?", "Yes, for all 35 tools. The processing libraries load from CDNs when the page opens; from then on, your files are read, processed and written by your browser with no upload step. The single documented exception is OCR's first run, which downloads the public English language model (public, identical for all users) — your document is still not transmitted."),
        ("Why would a site process files locally at all?", "Privacy is the product: documents that never leave the device cannot leak from a server breach, a retention-policy gap, or an employee mistake. It also removes upload waits and server queues."),
        ("Does 'no upload' mean the site knows nothing about my files?", "The site never sees your file contents, names or sizes. If analytics are enabled on the site (see our <a href='/privacy.html'>Privacy Policy</a>), events track only counts — like 'a file was selected' — never file names or contents."),
        ("Can I run the Network-tab test on my phone?", "Phone browsers do not ship a full Network inspector; use a desktop browser for the test. The architecture does not change between phone and desktop — the same client-side code runs on both."),
        ("What about ads on PDF tool sites?", "Many free PDF sites are ad-funded, and ad scripts are a separate privacy channel from file processing — a site can be ad-free or ad-supported and either model on files. PDFZaap currently runs no advertising; see the <a href='/privacy.html'>Privacy Policy</a> for the full statement."),
    ],
    related=[("compress-pdf", "Compress PDF"), ("merge-pdf", "Merge PDF"), ("ocr-pdf", "OCR PDF"), ("protect-pdf", "Protect PDF")],
)

# Titles/meta/H1 for the size-specific pages (per the brief's table)
_SIZES_META = {
    "compress-pdf-to-100kb": (
        "Compress PDF to 100KB Online Free | PDFZaap",
        "Compress PDF to 100KB",
        "Compress a PDF under 100 KB in your browser with a preset target. Built for job portals, government forms and visa uploads. File never uploaded.",
    ),
    "compress-pdf-to-200kb": (
        "Compress PDF to 200KB Online Free | PDFZaap",
        "Compress PDF to 200KB",
        "Compress a PDF under 200 KB in your browser with a preset target. The classic job-portal and certificate-upload limit. File never uploaded.",
    ),
    "compress-pdf-to-500kb": (
        "Compress PDF to 500KB Online Free | PDFZaap",
        "Compress PDF to 500KB",
        "Compress a PDF under 500 KB in your browser with a preset target. Built for scholarship and university application uploads. File never uploaded.",
    ),
    "compress-pdf-to-1mb": (
        "Compress PDF to 1MB Online Free | PDFZaap",
        "Compress PDF to 1MB",
        "Compress a PDF under 1 MB in your browser with a preset target. For university bundles and upload portals with roomier limits. File never uploaded.",
    ),
    "compress-pdf-to-2mb": (
        "Compress PDF to 2MB Online Free | PDFZaap",
        "Compress PDF to 2MB",
        "Compress a PDF under 2 MB in your browser with a preset target. The classic email-attachment size for legacy mail systems. File never uploaded.",
    ),
}
for _k, (_t, _h1, _m) in _SIZES_META.items():
    COMPRESS_SIZES[_k].update(title=_t, h1=_h1, meta=_m)

for _k in COMPRESS_SIZES:
    COMPRESS_SIZES[_k]["crumb_parent"] = ("Compress PDF", "compress-pdf.html")

INTENT["merge-pdf-without-uploading"]["crumb_parent"] = ("Merge PDF", "merge-pdf.html")
INTENT["jpg-to-pdf-a4"]["crumb_parent"] = ("JPG to PDF", "jpg-to-pdf.html")
INTENT["pdf-to-word-without-losing-formatting"]["crumb_parent"] = ("PDF to Word", "pdf-to-word.html")

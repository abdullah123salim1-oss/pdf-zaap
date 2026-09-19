# Content for the 6 new blog posts (Step 10).
# Each body must total 1,200+ visible words (enforced by the generator).
# Dates: staggered across the two weeks before the site's current publish
# date (2026-09-19). Owner should confirm actual publication schedule.

POSTS = {}

# ---------------------------------------------------------------- 1
POSTS["how-to-check-if-pdf-tool-uploads-files"] = dict(
    title="Check If a PDF Tool Uploads Your Files — 5-Minute Test",
    meta="A 5-minute test in your browser's developer tools to find out whether an online PDF tool uploads your file — or processes it locally. No guesswork.",
    og_title="How to Check If an Online PDF Tool Uploads Your Files",
    og_desc="A 5-minute Network-tab test to find out whether any online PDF tool uploads your file or processes it locally.",
    h1="How to Check If an Online PDF Tool Uploads Your Files (5-Minute Test)",
    date="2026-09-12",
    read=7,
    cta_text="Ready to try a tool that processes files locally? The whole collection is free.",
    cta_href="/compress-pdf.html",
    cta_label="Try Compress PDF →",
    body="""
      <p>You have a contract, an ID scan, or a financial statement, and you need to merge, compress, or convert it. An online tool is convenient — but "convenient" usually means your file travels to someone else's server first. The good news: you can find out, in about five minutes and without sending any real document, whether a given tool uploads your file or processes it entirely on your device.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p>Open the tool's page in Chrome or Edge, press <strong>F12</strong> (or right-click → Inspect), go to the <strong>Network</strong> tab, select a test file, and press the process button. If the tab shows no requests carrying your file, the processing is local. This guide explains what each pattern means, step by step.</p>
      </div>

      <h2>Why the question matters</h2>

      <p>Online PDF tools fall into two architectural camps, and the difference between them is everything:</p>

      <p><strong>Server-based tools</strong> work by uploading your document to the provider's server, running the operation there, and handing you a link to download the result. The provider typically promises automatic deletion after a few hours, and many are trustworthy — but your file still crosses the network, passes through their storage, and is subject to their security practices and their jurisdiction. For a grocery list that is a non-issue. For a signed contract, a passport scan, or payroll data, it is a real decision.</p>

      <p><strong>Client-side (local) tools</strong> do the opposite: the page loads the processing software — JavaScript and WebAssembly document engines, the same technology used by Adobe's own browser-based PDF services — into your browser, and your file is processed inside your tab's memory. Nothing about the document leaves your device, because there is no network step in the data path at all. The tool cannot leak your file by accident; the only things the site can see are page views and, if you enable analytics, the events you agree to share.</p>

      <p>Most users cannot tell the two apart from the interface — both show a dropzone, a progress bar, and a download. The Network tab can.</p>

      <h2>The 5-minute test, step by step</h2>

      <p>You will do this in Chrome, Edge, or Brave (all use Chromium's DevTools). Firefox's version works too; the panels are named slightly differently.</p>

      <table class="post-table">
        <tr><th>Step</th><th>What to do</th></tr>
        <tr><td>1</td><td>Open the tool's page. Before selecting any file, press <strong>F12</strong> (Windows/Linux) or <strong>⌘ + Option + I</strong> (Mac) to open DevTools, and click the <strong>Network</strong> tab.</td></tr>
        <tr><td>2</td><td>Tick <strong>Preserve log</strong> at the top of the Network panel, and click the <strong> (Clear)</strong> button to wipe the current list. The list now captures everything from this moment on.</td></tr>
        <tr><td>3</td><td>Create a throwaway test file: any PDF you do not care about, ideally one with a distinctive file name like <code>test-upload-check.pdf</code> so you can spot it in the log.</td></tr>
        <tr><td>4</td><td>Select the file in the tool and click the process button (Merge, Compress, Convert…).</td></tr>
        <tr><td>5</td><td>Watch the Network list as the progress bar runs. Then search the list for your file name and for upload-type requests (explained next).</td></tr>
      </table>

      <h2>Reading the Network tab</h2>

      <p>Three patterns matter:</p>

      <h3>Pattern 1 — an upload request (server-based)</h3>
      <p>A server-based tool will show a request to its own domain or to a storage service (commonly S3, GCS, or an upload API path like <code>/api/upload</code> or <code>/process</code>), with a <strong>POST</strong> method, a large <strong>request payload</strong> of several hundred KB to MB, and your file name in the request body, the query string, or the pre-signed URL. Click the request and look at the <strong>Payload</strong> sub-panel: if you see your file's bytes or name there, your document just left your machine. That is the whole answer — the tool is server-based.</p>

      <h3>Pattern 2 — only local activity (client-side)</h3>
      <p>A truly local tool shows no new network traffic at all while the file is being processed. The progress bar is driven by JavaScript running in your tab. The list in the Network tab stays exactly as it was after the page loaded: fonts, scripts, CSS — static assets, nothing new. If you selected a 5 MB file and the log gained nothing, the 5 MB never crossed the network. Your download at the end is produced from your tab's memory by the browser's download API, which also leaves no upload trace.</p>

      <h3>Pattern 3 — the honest exception (model downloads)</h3>
      <p>One client-side pattern that still shows network traffic: an OCR tool on its first run downloads a language model file (a few MB, from a public CDN such as the Tesseract project's tessdata host). That request contains no part of your document — it is the same public model file every OCR browser app fetches. How to tell the difference: the download's URL is a fixed model path (something like <code>eng.traineddata.gz</code>), its size is constant regardless of your file, and it happens before or during engine setup, not when your file is read. Your document bytes will not appear anywhere in the log. A responsible tool tells you about this first-run download on its page; PDFZaap's <a href="/ocr-pdf.html">OCR tool</a> page states it, and the <a href="/privacy.html">privacy policy</a> does too.</p>

      <h2>The second check: reading the page's code</h2>

      <p>If you want more confidence than one test run gives, look at what the page actually ships. In DevTools, go to the <strong>Sources</strong> tab (or use <strong>⌘ + Option + U</strong> for page source) and search for the tell-tale calls:</p>

      <ul>
        <li><code>fetch(</code>, <code>XMLHttpRequest</code>, or <code>axios.post</code> with a URL pointing at the site's own API — followed by <code>FormData</code> or <code>file.arrayBuffer()</code> — is an upload path.</li>
        <li>References to <code>pdf-lib</code>, <code>pdf.js</code> (Mozilla's PDF engine), or a <code>.wasm</code> WebAssembly file loaded into the page, combined with <code>URL.createObjectURL</code> for the download, is a local processing path.</li>
        <li>Local tools never need a file field in a form. If the only way to "submit" your PDF is to hand it to a form action that POSTs somewhere, it goes over the wire.</li>
      </ul>

      <p>This check is not exhaustive — obfuscated code can hide things — but combined with the Network test it is about as far as a non-malicious-tool vetting goes from a browser.</p>

      <h2>How PDFZaap behaves under this test</h2>

      <p>If you run the test on any PDFZaap tool page you will see Pattern 2: no new requests while the file is processed. The processing libraries (pdf.js, pdf-lib, Tesseract.js for OCR) are loaded with the page, and the file is read, processed, and re-exported inside your tab. The only documented network activity on first use of the OCR tool is the Pattern 3 model download. You can verify all of it yourself with the steps above — that is the point of the architecture, and it is why the <a href="/is-it-safe-to-use-online-pdf-tools.html">privacy explainer</a> walks through the same test.</p>

      <h2>Is server-based always wrong?</h2>

      <p>No. If the document is not sensitive — a public brochure, an open-source paper, a photo of a recipe — a server-based tool is fine, and some capabilities are genuinely easier to do well server-side (certified PDF/A validation, layout-perfect PDF-to-Word conversion of complex documents, for example). The honest framing is a risk decision: match the tool's architecture to the sensitivity of the document. The five-minute test simply makes sure the decision is informed rather than assumed.</p>

      <h2>Quick checklist</h2>

      <ul>
        <li>Open DevTools <em>before</em> selecting the file; clear the Network log.</li>
        <li>Use a throwaway file with a distinctive name.</li>
        <li>No new requests during processing → local. Upload request with your file's bytes or name → server-based.</li>
        <li>A fixed-size model download (OCR) is a documented exception, not an upload.</li>
        <li>Cross-check the page's source for upload calls vs. local engines.</li>
        <li>Match the architecture to the document's sensitivity — and keep the original file until the output is verified.</li>
      </ul>
""",
    faqs=[
        ("Does the 5-minute test work in Firefox or Safari too?", "Yes. Firefox's DevTools (⌘ + Option + I) has a Network panel with the same log, and Safari's Web Inspector (⌘ + Option + I after enabling the Develop menu) does too. The patterns — POST requests with a payload vs. no new requests — are identical in all browsers."),
        ("What if the tool uploads the file but the site is HTTPS?", "HTTPS encrypts the transfer so eavesdroppers cannot read it, but it does not change who receives the file. The file still arrives at the provider's server, sits in their storage, and is subject to their retention policy. Encryption in transit is good; it is not the same as no transfer."),
        ("Can a local tool still send my file somewhere by mistake?", "Not through the tool's own code path: there is no network step between reading the file and producing the download. The residual exposure is normal device-level stuff (your OS, your browser, malware on your machine), which exists whether or not a website is involved."),
        ("The tool showed a download request — is that an upload?", "No. A download in the Network tab (a response with your result file) is the normal end of a local process — the browser writing the file your tab produced. Uploads are requests: POSTs whose payload contains your file, going from your machine to a server."),
        ("Why does the OCR tool download a model on first use?", "OCR needs a trained language model to recognize text. The model (a public file from the Tesseract project's CDN) is the same for every user and contains no information about you or your document. Once downloaded, your browser caches it, so later runs usually show no network activity at all."),
    ],
    related=[
        '<a href="/is-it-safe-to-use-online-pdf-tools.html">Is it safe to use online PDF tools? — the privacy explainer</a> — the two architectures in more depth, plus where the limits of each model are.',
        '<a href="/privacy.html">PDFZaap privacy policy</a> — exactly what the site does and does not collect, including the OCR first-run model download.',
        '<a href="/compress-pdf.html">Compress PDF tool</a> — a local-processing tool you can run the test on right now.',
    ],
)

# ---------------------------------------------------------------- 2
POSTS["why-pdf-blurry-after-compression"] = dict(
    title="Why PDFs Get Blurry After Compression",
    meta="What actually changes when a PDF is compressed, why the result sometimes looks blurry or pixelated, and the settings that keep text and photos legible.",
    og_title="Why PDFs Get Blurry After Compression (And How to Avoid It)",
    og_desc="Why compressed PDFs go blurry or pixelated — what compression changes, the quality/size trade-off, and settings that keep documents legible.",
    h1="Why PDFs Get Blurry After Compression (And How to Avoid It)",
    date="2026-09-13",
    read=7,
    cta_text="Compress your next PDF with an honest quality report — no upload, no watermark.",
    cta_href="/compress-pdf.html",
    cta_label="Compress PDF Now →",
    body="""
      <p>You compressed a 20 MB scan down to 3 MB, and something went wrong: photos look pixelated, the small print under the table has a grainy halo, and the header logo looks like it was faxed. "Blurry after compression" is the most common complaint about PDF compression tools — and it is worth understanding, because it is not random. It follows directly from what compression has to do, and most of it can be predicted and avoided.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p>Compression shrinks files mainly by re-encoding embedded images at lower quality and, in target-size mode, lowering resolution until the limit is met. Text and simple vector graphics usually stay sharp; photos and fine details are what suffer. The fix is to pick a quality (or target size) that matches the document's content and to check a dense page before you send the file anywhere.</p>
      </div>

      <h2>What a PDF actually contains</h2>

      <p>Before "why blurry" makes sense, it helps to see what a PDF is made of. Most documents contain a mix of:</p>

      <ul>
        <li><strong>Text</strong> — stored as vector outlines and font data. This is what makes printed text razor-sharp at any zoom level.</li>
        <li><strong>Vector graphics</strong> — lines, boxes, charts drawn as instructions ("draw a line from here to there"). Also resolution-independent.</li>
        <li><strong>Embedded images</strong> — photographs, scans, logos, screenshots. These are the big weight in most files, and they are stored as pixel grids (usually JPEG-compressed).</li>
        <li><strong>Overprint layers</strong> — on scanned PDFs, the entire page is effectively one big image; there is no real text underneath.</li>
      </ul>

      <p>The size of a typical "too big" PDF is dominated by the images. That is why every compression strategy — from a desktop suite to a browser tool — starts by asking: what can I do to the images?</p>

      <h2>Why blurriness happens: the three mechanisms</h2>

      <h3>1. Lower JPEG quality (compression artifacts)</h3>
      <p>Images inside PDFs are almost always JPEG-encoded, and JPEG is a lossy format: it discards detail the encoder judges inaudible, and the discarded detail comes back as blockiness, ringing around edges, and smearing in gradients. Push the quality down and the artifacts get louder. This is the "pixelated grid" look on photos and the "muddy" look in gray gradients. A text page with a photo will show it in the photo first — the text stays crisp because it is not an image.</p>

      <h3>2. Lower resolution (downsampling)</h3>
      <p>When a tool is told to hit a hard size limit — "under 200 KB" — lowering JPEG quality alone is often not enough, so it also re-samples the images at fewer pixels. A 300 dpi scan becomes 150, then 100. Each step physically removes pixels; when you view the result on screen or print it, the image looks softer or visibly blocky. This is the "everything is slightly out of focus" look, including logos and line art that was previously sharp.</p>

      <h3>3. Rasterization (re-rendering the page as an image)</h3>
      <p>Some compressors take a different route: they re-render each page to a bitmap at a chosen resolution and rebuild the PDF around those bitmaps. This can crush mixed content aggressively (it is how some tools get dramatic size drops on dense documents) — but it also converts your selectable text into picture text. The visual quality depends entirely on the render resolution: at 150 dpi it is fine on screen, at 72 dpi it is visibly soft. And as a side effect you lose searchability and copy-paste, which is a cost no blurriness should force on you unless you accept it deliberately.</p>

      <p>Which of the three you are seeing depends on the tool. A quality-based compressor mostly does (1) plus, in target mode, (2). A re-rendering compressor does (3) with a resolution choice. PDFZaap's <a href="/compress-pdf.html">Compress PDF tool</a> uses the re-rendering approach (it renders pages through Mozilla's PDF engine and re-encodes them), which is why its result note tells you which quality it settled on — so you can judge the trade-off with the information in front of you.</p>

      <h2>Why some files look fine and others do not</h2>

      <p>The same quality setting behaves differently across documents. The variables:</p>

      <table class="post-table">
        <tr><th>Content type</th><th>What you lose first</th></tr>
        <tr><td>Text-heavy document (CV, memo)</td><td>Barely anything visible — there is little image data. Size drop is modest.</td></tr>
        <tr><td>Photo in a text document (headshot, product shot)</td><td>The photo goes grainy while the text stays sharp — the classic "only the picture is blurry" complaint.</td></tr>
        <tr><td>Full-page scan</td><td>Everything softens; fine print is the first casualty.</td></tr>
        <tr><td>Dense vector chart / line art</td><td>Re-rendering can turn clean lines into slightly wobbly pixels; JPEG artifacts crawl into flat white areas.</td></tr>
        <tr><td>Photo-heavy report (slide exports, brochures)</td><td>Large size drops available, at real visible cost in every photo.</td></tr>
      </table>

      <p>The practical rule: a photo-heavy document gives the compressor room to cut a lot and looks noticeably worse at aggressive settings; a text document gives it little room and looks nearly identical until you push far.</p>

      <h2>How to avoid (or predict) the blur</h2>

      <ul>
        <li><strong>Know your content before you compress.</strong> If the document is mostly text, a moderate quality (around 0.5 on a 0.1–1.0 scale) will usually look indistinguishable from the original on screen. If it is photo-heavy and the photos matter, go gentler (0.7–0.8) and expect a smaller size drop.</li>
        <li><strong>Use target size only when a limit is real.</strong> "Under 100 KB" is a portal requirement, not an aesthetic goal. Target mode exists to hit a number, and it will sacrifice quality as far as the number requires — which is honest, but you should know what you are asking for.</li>
        <li><strong>Check a worst-case page.</strong> Do not eyeball the first page. Open the compressed file and look at the page with the smallest print, the darkest photo, or the densest table. If that page is acceptable, the rest is.</li>
        <li><strong>Do not chain compressions.</strong> Compressing an already-compressed file re-encodes its JPEG artifacts, and each pass makes them worse — the "third pass looks terrible" effect. If the first pass did not reach the limit, change the setting on the <em>original</em> file instead of stacking passes.</li>
        <li><strong>Lower the source, not the destination.</strong> For scans, the biggest lever is scan resolution: scanning at 150 dpi instead of 300 dpi roughly quarters the image data before compression ever starts, and the result is sharper than a 300 dpi scan crushed afterward.</li>
        <li><strong>Separate concerns.</strong> If only the photo is the problem, consider removing it, replacing it with a smaller export, or keeping the photo in a separate attachment — rather than degrading the whole document to save a megabyte.</li>
      </ul>

      <h2>When some softness is acceptable (and when it is not)</h2>

      <p>Screen review of a meeting draft, an internal status report, a shared photo album — softness costs you nothing. But: ID documents and certificates where a border or serial number must be legible, contracts with fine print that may be referenced later, engineering drawings with tolerances, medical or legal exhibits — these should be compressed conservatively or not at all, and if a portal's size cap forces the trade, ask the portal for a larger cap or an alternative submission path before accepting an unreadable upload.</p>

      <h2>How to tell what actually happened to your file</h2>

      <p>If a compressed file looks wrong, diagnose before blaming the tool:</p>

      <ul>
        <li>Text sharp but photos grainy → JPEG quality. Raise quality, re-compress from the original.</li>
        <li>Everything uniformly softer → downsampling. Raise the resolution floor or target a larger limit.</li>
        <li>Text no longer selectable → the tool rasterized. Decide whether you accept non-searchable output; if not, use a tool that preserves text (or accept the trade-off knowingly).</li>
        <li>Blurry in places that were also blurry before → the input was the problem, not the compression. Compare against the original.</li>
      </ul>

      <h2>The honest trade-off, in one sentence</h2>

      <p>Every byte you remove comes from somewhere in the document, and the encoder will always take it from images before it touches anything else — so "blur after compression" is the visible side of a size target, and the only real controls are: how much size you actually need to remove, what the document can afford to lose, and checking the worst-case page before the file leaves your hands.</p>
""",
    faqs=[
        ("Why is my text blurry but it was sharp before?", "Pure text pages rarely blur from JPEG settings alone. If selectable text looks soft, the tool likely rasterized the page (re-rendered it as an image) at a low resolution — or the blur was already in the scan. Rasterized text also stops being selectable; if you can no longer copy text from the file, that confirms a re-render happened."),
        ("Is 0.5 quality safe for a professional document?", "For screen viewing and most email attachments, a middle quality around 0.5 is a good default for text-heavy files. For photo-heavy documents where the photos are the content, 0.7–0.8 looks much closer to the original, with a smaller size reduction. Always check a dense page of the result."),
        ("Does compressing twice make it worse?", "Yes — repeatedly. Each pass re-encodes the JPEG data left by the previous pass, so artifacts accumulate. If a first pass misses the target, re-run on the original file with a lower setting instead of compressing the compressed result."),
        ("My scan is 300 dpi. Can I still get under 200 KB without it looking bad?", "For a long document, usually not — 300 dpi scans carry a lot of pixels per page. Your levers, in order of impact: reduce the page count (extract only what the form asks for), re-scan at 150 dpi if you have the source, or use a target-size mode and accept visible softness in photos. A text-only CV at 150 dpi has a much easier time."),
        ("Can I get the size back after it looks too blurry?", "From the compressed file, no — the removed detail is gone. That is why the workflow is: keep the original, compress a copy, check the copy, and only replace the original in your submission folder if the copy is acceptable."),
    ],
    related=[
        '<a href="/compress-pdf.html">Compress PDF tool</a> — quality slider plus target-size mode, with a result note that tells you what the tool actually did.',
        '<a href="/grayscale-pdf.html">Grayscale PDF tool</a> — strip color to cut size on text-heavy documents before (or instead of) a deep compression.',
        '<a href="/compress-pdf-to-200kb.html">Compress PDF to 200KB</a> — the common portal limit, with honest guidance on what fits and what does not.',
    ],
)

# ---------------------------------------------------------------- 3
POSTS["how-to-merge-pdf-on-android-no-app"] = dict(
    title="Merge PDFs on Android Without Installing an App",
    meta="Merge PDFs on Android using only your browser — no app store, no extra permissions, no upload — plus when a desktop wins.",
    og_title="How to Merge PDF Files on Android Without Installing an App",
    og_desc="Combine PDFs on Android using only your browser: step-by-step, ordering tips, common problems, and when a desktop is the better machine.",
    h1="How to Merge PDF Files on Android Without Installing an App",
    date="2026-09-14",
    read=7,
    cta_text="Merging in your Android browser takes about a minute — and the files never leave the phone.",
    cta_href="/merge-pdf.html",
    cta_label="Merge PDF in Browser →",
    body="""
      <p>You have three PDFs on your phone — a form, a certificate, a signed consent — and they need to be one file before you upload them. The default suggestion everywhere is "download a PDF merger app." That is a workable answer, but it is not the only one: an Android phone's browser can merge PDFs locally, with no app store visit, no storage permissions, and no file upload. This guide covers the browser method step by step, plus two honest alternatives for when the phone is not the right machine.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p>Open <a href="/merge-pdf.html">PDFZaap's Merge PDF page</a> in Chrome (or Edge) on your Android phone, tap the dropzone, pick all the PDFs you want to combine, and tap Merge. The merge happens inside the browser using the files on your phone; the combined PDF downloads straight to your Downloads folder. No app, no account, no upload.</p>
      </div>

      <h2>Why the no-app route makes sense on Android</h2>

      <p>PDF apps from the store ask for things a one-time merge does not need: storage permission to browse your whole file system, and (frequently) ads or a subscription for the "pro" merge. A browser-based merge touches only the files you explicitly select, asks for nothing else, and leaves nothing behind. On a work phone with a device policy, it also sidesteps the "is this app allowed?" question entirely. The trade-offs are real — a phone screen is small for verifying page order, and very large merges can strain a mid-range device — so know what you are trading before you choose.</p>

      <h2>Method 1: merge in your Android browser (recommended for most cases)</h2>

      <h3>Step 1 — collect the files in one place</h3>
      <p>The file picker makes merging easier when the PDFs are in one folder. If they arrived through different channels (a share sheet, an email attachment, a download), move them into a single folder with your file manager, or keep track of where each one is. If you want to be sure of the final order, rename them with a number prefix (<code>1-cover.pdf</code>, <code>2-body.pdf</code>, <code>3-signatures.pdf</code>) — most pickers let you sort by name.</p>

      <h3>Step 2 — open the merge tool</h3>
      <p>In Chrome or Edge, open <a href="/merge-pdf.html">pdfzaap.online/merge-pdf.html</a>. The page loads the processing library (pdf-lib, running in WebAssembly-in-your-browser territory — the point is it runs on your device, not on a server). Nothing about your documents is transmitted at this step; the page is the same static site anyone can inspect in the <a href="/is-it-safe-to-use-online-pdf-tools.html">privacy explainer</a>'s test.</p>

      <h3>Step 3 — select the files, in order</h3>
      <p>Tap the dropzone. Android opens its file picker (on most phones: "Files" / the system document picker). Choose your first PDF, then use the picker's multi-select (a checkbox or long-press, depending on your file manager) to add the rest. The order the tool receives them is the order of the pages in the result — so select them in the order you want them to appear. The file list on the page shows what was selected; if the order is wrong, remove and re-select.</p>

      <h3>Step 4 — merge and download</h3>
      <p>Tap <strong>Merge PDFs</strong>. The tool copies the pages from each file into one new document in your browser's memory and produces the combined file. A download prompt appears (or the file lands in your Downloads folder, depending on your browser's settings). Open it in your reader to verify: page count, order, and that no page is rotated or blank.</p>

      <h3>What you are seeing under the hood</h3>
      <p>The merge is a structural operation: pages are copied from the source files into a new document. There is no re-encoding, so the combined file's size is roughly the sum of the parts, and quality is untouched — no blurring, no font substitution. That is also why a merge on a phone is as faithful as a merge on a desktop: the operation is light enough that hardware rarely matters, unless the files are huge (more on that below).</p>

      <h2>Method 2: use the Files app's "combine" where it exists</h2>

      <p>Be honest with yourself about this one: stock Android has no built-in PDF merger, and the Files apps that ship with phones (Google Files, Samsung My Files, Xiaomi Files) differ by manufacturer and version. Some newer Android versions and some OEM file managers offer a "merge PDF" or "combine" option in the PDF viewer's share menu; others do not. If yours does, that is a perfectly fine zero-extra-step route — the merge is local to the phone either way. If it does not (most devices, as of this writing), Method 1 or 3 is your route. Do not trust a blog post that describes a specific menu path for a specific OEM as universal; check your own device.</p>

      <h2>Method 3: move the files to a computer (best for big or sensitive merges)</h2>

      <p>For very large merges — dozens of pages, files in the tens of MB — or for documents you would rather never touch on a mobile device, the sensible move is to transfer them. AirDrop-style share to a laptop, a USB cable, or your own cloud storage all work. Then merge on the desktop using the same browser-based tool, where verifying page order on a big screen is far easier. There is nothing wrong with this: the "no app" goal is about not installing third-party software, not about using the least powerful machine available.</p>

      <h2>Getting the order right (the #1 real-world problem)</h2>

      <p>Almost every "the merge went wrong" story is actually an order problem: page 12 from file B sneaked between pages 3 and 4. The habits that prevent it:</p>

      <ul>
        <li>Number-prefix your file names before you select, and sort the picker by name.</li>
        <li>Read the selected-file list on the tool page <em>before</em> merging, not after.</li>
        <li>After merging, check the first page of each original section, not just the first and last page.</li>
        <li>If a source file is itself out of order, fix it there first — a merge preserves whatever order each file has. The <a href="/reorder-pages-pdf.html">Reorder Pages tool</a> does exactly this, in the same browser.</li>
        <li>Portrait and landscape pages mix fine in one document — but if a scanned page came in rotated, fix it with <a href="/rotate-pdf.html">Rotate PDF</a> before merging, or it stays rotated.</li>
      </ul>

      <h2>Common problems on Android, and what they usually are</h2>

      <table class="post-table">
        <tr><th>Symptom</th><th>Usual cause</th><th>Fix</th></tr>
        <tr><td>File picker shows no PDFs</td><td>You are looking in the wrong storage location (Download vs. Documents vs. a shared-inbox folder)</td><td>Open the PDF once in its native app to learn where it lives, then pick it from there.</td></tr>
        <tr><td>Merge button stays disabled</td><td>Only one file selected, or a non-PDF slipped in</td><td>Select at least two .pdf files.</td></tr>
        <tr><td>Phone freezes on a very large merge</td><td>Memory pressure on a mid-range device with several hundred MB of pages</td><td>Merge in batches (combine A+B, then combine AB+C), or use Method 3 on a desktop.</td></tr>
        <tr><td>Result is bigger than expected</td><td>PDFs do not always deduplicate shared resources when copied</td><td>Normal — a merge is a copy operation. If size matters, compress the result afterward with the <a href="/compress-pdf.html">Compress PDF tool</a>.</td></tr>
        <tr><td>One page looks blank</td><td>That page is blank (or image-only in a form that needs form data) in the source file</td><td>Check the source file — the merge copied what was there.</td></tr>
      </table>

      <h2>Privacy note, in the words that matter</h2>

      <p>In the browser method, the selected PDFs are read by your phone's browser and processed in the page's memory. No part of them is sent to a server — the merge page has no upload endpoint, and you can verify that yourself with the 5-minute Network-tab test described in <a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">How to Check If an Online PDF Tool Uploads Your Files</a>. What the phone does need is a normal browser session; if your employer's device policy allows browsing to that site, it allows the merge.</p>

      <h2>Quick checklist</h2>

      <ul>
        <li>Collect the PDFs in one folder; number-prefix the file names in the order you want.</li>
        <li>Open the merge page in Chrome/Edge; confirm the file list order before merging.</li>
        <li>Merge, download, then verify section boundaries in the result.</li>
        <li>Fix source problems (rotation, order) in the source files first.</li>
        <li>Very large or highly sensitive merges → do them on a desktop with the same tool.</li>
      </ul>
""",
    faqs=[
        ("Does merging PDFs on my phone upload the files anywhere?", "No — in the browser method, the files are read by the page and combined in your browser's memory on the phone. The combined file is produced locally and downloaded to your device. You can verify there is no upload with the Network-tab test in our upload-checking guide."),
        ("Will the merged PDF look different from the originals?", "A merge copies pages without re-encoding them, so each page looks exactly as it did in its source file. Size is roughly the sum of the parts; quality is untouched. Any change you see (rotation, blank pages) was in a source file."),
        ("My phone has 4 GB of RAM and froze mid-merge. What now?", "Mid-range phones can run out of memory on very large merges (hundreds of pages at high resolution). Merge in batches: combine the first half into one file, then combine that with the second half. Or move the work to a desktop — the same browser tool works there and has much more headroom."),
        ("Can I merge a PDF with a scanned image, or a PDF with different page sizes?", "Yes. Pages of different sizes coexist fine in one PDF — each page keeps its own dimensions. The result is simply a document whose pages vary in size, which is normal for combined documents and acceptable to most upload portals."),
        ("Why is the result file bigger than I expected?", "Each source file's resources (fonts, images, page objects) are copied into the output. If two files share the same font, the output may carry it twice. That is a property of structural merging, not data loss. If the total size matters, run the result through the compress tool."),
    ],
    related=[
        '<a href="/merge-pdf.html">Merge PDF tool</a> — the tool used in this guide; works identically on Android, iPhone, and desktop browsers.',
        '<a href="/reorder-pages-pdf.html">Reorder Pages tool</a> — fix page order inside a single PDF, in the browser.',
        '<a href="/compress-pdf.html">Compress PDF tool</a> — shrink the merged result if the upload limit cares about size.',
    ],
)

# ---------------------------------------------------------------- 4
POSTS["how-to-combine-jpg-photos-pdf-iphone"] = dict(
    title="Combine JPG Photos into One PDF on iPhone (No App)",
    meta="Two no-app ways to turn multiple JPG photos into one PDF on iPhone: the built-in Print trick and a private in-browser method, step by step.",
    og_title="How to Combine JPG Photos Into One PDF on iPhone (No App Needed)",
    og_desc="Turn multiple JPG photos into one PDF on iPhone without an app: the built-in Print trick and a private in-browser method, step by step.",
    h1="How to Combine JPG Photos Into One PDF on iPhone (No App Needed)",
    date="2026-09-16",
    read=7,
    cta_text="Combine your photos into a PDF in Safari — no app, no upload, A4 option included.",
    cta_href="/jpg-to-pdf.html",
    cta_label="JPG to PDF →",
    body="""
      <p>Receipts from the week, a set of product photos, scanned pages you took pictures of — sending one PDF instead of six attachments is neater for the recipient and easier for you to keep. iPhones ship with a little-known built-in way to do this, and a browser-based way that is more controllable. Both avoid the app store entirely. Here is each one, honestly, with its limits.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p><strong>Built-in:</strong> in the Photos app, select your images → Share → <strong>Print</strong> → in the print preview, pinch outward on the preview page to zoom it into a full-size document → Share → <strong>Save to Files</strong>. You now have a PDF, one photo per page. <strong>Better control:</strong> open <a href="/jpg-to-pdf.html">PDFZaap's JPG to PDF page</a> in Safari, select the same photos, and download the combined PDF — with an option to place each photo on a standard A4 page.</p>
      </div>

      <h2>Method 1: the built-in Print trick (no network at all)</h2>

      <p>iPhone's print system can render a photo (or a set of them) into the print preview, and the print preview is itself a PDF — which the Share sheet will happily save. That one observation is the whole trick.</p>

      <h3>Step by step</h3>
      <ol>
        <li>Open the <strong>Photos</strong> app and select the images you want in the PDF: tap <strong>Select</strong> (bottom right), then tap each photo. Tap order does not matter here — you can reorder later in some flows, but the saved PDF follows the selection order your iOS version presents, so check the result.</li>
        <li>Tap the <strong>Share</strong> button (the square with an up-arrow) and choose <strong>Print</strong>.</li>
        <li>The print preview appears, showing one photo per page. This is the step people miss: <strong>pinch outward on the preview page</strong> until it fills the screen. The preview has just become a full-size document view.</li>
        <li>Tap the <strong>Share</strong> button of that preview (top of the screen), choose <strong>Save to Files</strong>, pick a location (On My iPhone or iCloud Drive), and save. A .pdf appears in your Files app.</li>
      </ol>

      <h3>What to know about the result</h3>
      <ul>
        <li>One photo per page, in the page size your printer settings imply (typically US Letter or A4 depending on region and defaults) — the photo is fitted onto the page, so there may be white margins around it.</li>
        <li>Orientation follows the photo's orientation as the print preview renders it; if a landscape photo shows sideways, rotate it in Photos first.</li>
        <li>Quality is good for on-screen review and casual sharing. This is a print pipeline, not a document pipeline — do not expect it for archival or print-shop work.</li>
        <li>Selection order: different iOS versions present multi-photo print jobs slightly differently; if the PDF order is not what you want, re-run with a different selection order or use Method 2, where you control the sequence explicitly.</li>
      </ul>

      <p>The strengths of this method: zero network, zero third parties, zero installs. The weaknesses: limited control over page size, order, and layout, and the pinch step confuses most first-time users. For "five receipts into one PDF, fast," it is genuinely enough.</p>

      <h2>Method 2: JPG to PDF in Safari (more control, still no app)</h2>

      <p>When you need the photos in a specific order, on a standard page size, or with the images scaled consistently, a browser-based converter is the better tool. iPhone's Safari opens local files just like a desktop browser — the file picker is part of iOS, and the processing runs in the page on your device.</p>

      <h3>Step by step</h3>
      <ol>
        <li>Open <a href="/jpg-to-pdf.html">pdfzaap.online/jpg-to-pdf.html</a> in Safari.</li>
        <li>Tap the dropzone. Safari's file picker opens, letting you browse your <strong>Photos</strong> library or <strong>Files</strong>. Select the images in the order you want them to appear — that order is the page order of the result.</li>
        <li>In the options panel, choose <strong>Page size</strong>: <em>Fit page to each image</em> (each page is exactly the photo's dimensions), <em>A4 — image centered</em>, or <em>US Letter — image centered</em>. On a centered standard page, each photo is scaled down to fit with margins; photos are never upscaled beyond their native size.</li>
        <li>Tap <strong>Convert to PDF</strong>. The images are combined into one PDF in your browser and the file downloads to your <strong>Downloads</strong> folder (visible in the Files app under Recents/Downloads).</li>
        <li>Open the result in Files and check order and orientation before sending it anywhere.</li>
      </ol>

      <h3>HEIC: the one preparation step most people need</h3>
      <p>iPhones save photos as HEIC by default. The JPG to PDF tool accepts JPG/JPEG files, so if your photos are HEIC you have two honest options: in the Photos app, long-press → Share, and the share sheet will offer to export as JPEG in some flows — or, permanently, go to <strong>Settings → Photos → Transfer to Mac/PC</strong> (and the "Keep Originals" vs "Automatic" behavior in Settings → Photos) so new photos are stored as Most Compatible (JPG). For a one-off, the simplest route is selecting the photos in the file picker: on recent iOS versions, sharing a photo from the picker or from Files can offer a JPG rendition; if the tool does not accept the file, convert the photo to JPG first and reselect. Do not fight this silently — the file simply needs to be a JPG or JPEG before it goes in.</p>

      <h2>Which method should you use?</h2>

      <table class="post-table">
        <tr><th>Situation</th><th>Better method</th><th>Why</th></tr>
        <tr><td>A few receipts or photos, quick send</td><td>Print trick</td><td>Three taps, no network at all.</td></tr>
        <tr><td>Specific page order matters</td><td>Safari + JPG to PDF</td><td>You see and control the selection order directly.</td></tr>
        <tr><td>Portal requires A4 pages</td><td>Safari + JPG to PDF (A4 option)</td><td>The print trick's page size follows printer defaults; the tool sets A4 explicitly.</td></tr>
        <tr><td>Offline / airplane mode</td><td>Print trick</td><td>No page load needed at all.</td></tr>
        <tr><td>Many photos (10+)</td><td>Safari + JPG to PDF</td><td>Selection is simpler and the result is more predictable.</td></tr>
      </table>

      <h2>Getting orientation and order right</h2>

      <ul>
        <li>Rotate a photo in Photos <em>before</em> selecting it (open → edit → crop/rotate), rather than fixing it afterward — both methods render what the file contains.</li>
        <li>For a long sequence, name the order in your head before selecting: "cover, page one, page two…". Re-selecting one photo in Safari's picker means starting the selection over on most iOS versions, so get the list right the first time.</li>
        <li>Mixing portrait and landscape photos is fine — each page takes the image it is given. If you want uniformity, crop to a consistent aspect in Photos first.</li>
      </ul>

      <h2>What stays on your device</h2>

      <p>In the Print trick, everything is a local system feature — nothing touches the network. In the Safari method, the photos are read by the page and combined in your browser's memory; the resulting PDF is written to your device by the browser's download. No photo data is uploaded; the page has no upload endpoint, and the same 5-minute Network-tab test from our <a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">upload-checking guide</a> will show no file traffic if you want to see it for yourself.</p>

      <h2>Quick checklist</h2>

      <ul>
        <li>Quick job → Print trick: select → Share → Print → pinch out → Share → Save to Files.</li>
        <li>Ordered job or A4 requirement → Safari → JPG to PDF → select in order → pick page size → Convert.</li>
        <li>HEIC photos → convert to JPG first (share/export as JPEG, or switch camera storage to Most Compatible).</li>
        <li>Rotate before selecting; verify order and orientation in the saved PDF before sending.</li>
      </ul>
""",
    faqs=[
        ("Does the Print trick work on every iPhone?", "It works on modern iOS versions that include the multi-photo print preview with the pinch-to-zoom gesture. If your preview does not zoom to a full page (older iOS, or a single-photo flow in some versions), use the Safari method instead — it is more consistent across versions."),
        ("My photos are HEIC, not JPG. Will the tool accept them?", "The JPG to PDF tool accepts JPG/JPEG. To convert: share the photo from Photos and choose a JPEG export where offered, or set Settings → Photos to store/transfer in Most Compatible format. Once the file is a JPG, the tool picks it up normally in Safari's file picker."),
        ("Can I put 20 photos in one PDF?", "Yes — select them all in one go. The result is one PDF with one page per photo. If your phone struggles with a very large batch, split it into two batches and merge the two PDFs with the Merge PDF tool (also in the browser)."),
        ("Will the photos lose quality in the PDF?", "The photos are embedded as-is (JPEG data is carried into the PDF, scaled to fit the page). There is no quality-destroying re-compression step in this tool — the output image is the input image, laid out. The print trick renders through the print pipeline, which is good for casual use but less precise."),
        ("Why is there white space around my photo on the page?", "With a standard page size (A4 or Letter) selected, each photo is centered and scaled to fit, so non-matching aspect ratios leave margins. Choose 'Fit page to each image' for edge-to-edge pages that match each photo's own dimensions instead."),
    ],
    related=[
        '<a href="/jpg-to-pdf.html">JPG to PDF tool</a> — the browser tool used in this guide, with fit/A4/US Letter page options.',
        '<a href="/jpg-to-pdf-a4.html">JPG to PDF on A4 pages</a> — the A4-focused variant, for portals and forms that expect A4.',
        '<a href="/merge-pdf.html">Merge PDF tool</a> — combine the result with other PDFs, still in the browser.',
    ],
)

# ---------------------------------------------------------------- 5
POSTS["how-to-make-pdf-smaller-without-adobe"] = dict(
    title="Make a PDF Smaller Without Adobe (Free Method)",
    meta="Shrink any PDF without Adobe: what 'Save as Optimized PDF' actually does, and a free in-browser method that does the same job privately.",
    og_title="How to Make a PDF Smaller Without Adobe (Free Browser Method)",
    og_desc="Shrink any PDF without Adobe: what optimized-PDF export actually does, and a free in-browser method that does the same job privately.",
    h1="How to Make a PDF Smaller Without Adobe (Free Browser Method)",
    date="2026-09-17",
    read=7,
    cta_text="The same result, in your browser, free: pick a quality or a target size and download a smaller PDF.",
    cta_href="/compress-pdf.html",
    cta_label="Compress PDF Now →",
    body="""
      <p>"File too large" is usually a 30-second fix — but the reflex answer for a lot of people is Adobe Acrobat, which means installing a heavyweight suite or paying for a subscription to do a task that is conceptually simple. Here is what the Adobe workflow is actually doing under the hood, and a free browser-based method that achieves the same kind of result without the install, the account, or the upload.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p>Open <a href="/compress-pdf.html">PDFZaap's Compress PDF tool</a> in your browser, select the file, choose either a <strong>quality level</strong> (slider from 0.1 to 1.0, default 0.6) or a <strong>target size</strong> (under 100 KB / 200 KB / 500 KB / 1 MB / 2 MB), and press Compress. The file is processed in your browser and downloaded smaller. No Adobe, no account, no upload.</p>
      </div>

      <h2>What "Save as Optimized PDF" actually does</h2>

      <p>Adobe's optimized export (File → Save As Other → Optimized PDF) offers checkboxes for downsampling images, discarding embedded fonts you do not use, removing hidden layers and unused objects. The size drop comes overwhelmingly from the image work: re-encoding embedded photos at lower quality and resolution. Fonts and vector content contribute a little; in a typical document, images are 80–95% of the bytes. That single fact is the whole game, and it means you do not need Adobe to play it — you need any tool that can re-encode the images in a PDF, which is exactly what the browser-based method below does.</p>

      <h2>The free browser method, step by step</h2>

      <h3>Step 1 — open the tool</h3>
      <p>Go to <a href="/compress-pdf.html">pdfzaap.online/compress-pdf.html</a> in any modern browser (Chrome, Edge, Firefox, Safari). The page loads the processing engines (Mozilla's PDF.js for reading the PDF and rendering pages, plus the output encoding) into your browser. This is the same class of technology Adobe uses for its own in-browser PDF services; the difference is where it runs — here, on your device.</p>

      <h3>Step 2 — select the file</h3>
        <p>Drop the PDF in or browse for it. The file is read into the page's memory locally; nothing is transmitted (verifiable with the Network-tab test in our <a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">upload-checking guide</a>).</p>

      <h3>Step 3 — choose how to shrink it</h3>
      <p>Two modes, and they answer different questions:</p>

      <ul>
        <li><strong>Quality mode (slider 0.1–1.0, default 0.6).</strong> "How much can I let the images give up?" A text-heavy document at 0.5 usually looks indistinguishable on screen and shrinks meaningfully; a photo-heavy document at 0.7 keeps the photos close to original at a smaller drop. You choose the trade-off, and you see the resulting size when the download is ready.</li>
        <li><strong>Target size mode (under 100 / 200 / 500 KB, 1 / 2 MB).</strong> "I must be under X." The tool searches for the best quality that fits the limit and reports the size it reached — and, importantly, tells you honestly if the limit was not reachable for that document. Use this when a portal or an email system imposes the number.</li>
      </ul>

      <h3>Step 4 — check the result</h3>
      <p>Open the downloaded file. Look at the worst-case page (smallest print, darkest photo) — not the first page. If it is acceptable, replace the original in your submission folder; if not, re-run on the original with a different setting (never on the already-compressed file).</p>

      <h2>What you get versus the Adobe route, honestly</h2>

      <table class="post-table">
        <tr><th>Aspect</th><th>Adobe optimized export</th><th>Browser method (PDFZaap)</th></tr>
        <tr><td>Image re-encoding (the main lever)</td><td>Yes, with fine per-image controls</td><td>Yes — quality slider or target-size search</td></tr>
        <tr><td>Font subsetting / unused-object removal</td><td>Yes, explicit controls</td><td>Implicit to the re-render pipeline; no per-object controls</td></tr>
        <tr><td>Text stays selectable?</td><td>Yes (true text preserved)</td><td>No — pages are re-rendered, so text becomes part of the page image. Trade it off knowingly.</td></tr>
        <tr><td>Where the file is processed</td><td>On your computer (desktop app)</td><td>In your browser, on your device</td></tr>
        <tr><td>Cost / account</td><td>Subscription or one-time license</td><td>Free, no account</td></tr>
        <tr><td>Best for</td><td>Archival-grade optimization, complex documents, print workflows</td><td>Email limits, portal caps, everyday shrink jobs</td></tr>
      </table>

      <p>The row that matters most for most people is the last one: if your problem is "this 8 MB attachment must become 2 MB for a portal," the browser method solves it completely. If your problem is "produce the leanest possible archival file while keeping every object surgical," a desktop suite is still the better instrument — and that is a legitimate use, not a criticism of the free route.</p>

      <h2>When the file will not shrink, and why</h2>

      <p>Some PDFs resist compression, and knowing why saves you from hammering a setting that cannot work:</p>

      <ul>
        <li><strong>Already-optimized text documents.</strong> A plain-text PDF is mostly font data and text operations — small to begin with and barely compressible. The drop will be modest. That is the correct behavior, not a bug.</li>
        <li><strong>Dense vector content.</strong> Schematics, circuit diagrams, and heavily plotted charts store their detail as instructions. Re-encoding the page raster can actually make these <em>bigger</em>; the tool's result note flags when the output is not smaller, in which case keep the original.</li>
        <li><strong>Encrypted PDFs.</strong> A password-protected file must be <a href="/unlock-pdf.html">unlocked first</a> (if you have the rights to it) before compression can read and re-encode it.</li>
        <li><strong>The limit is genuinely below the document's information content.</strong> A 40-page photo report cannot become a readable 200 KB. The levers then are removing pages (<a href="/delete-pdf-pages.html">Delete PDF Pages</a>) or re-scanning the source at lower DPI — not a lower quality setting that just destroys the remaining content.</li>
      </ul>

      <h2>A ladder of techniques, gentle to aggressive</h2>

      <ol>
        <li><strong>Moderate quality pass (0.5–0.6).</strong> The default first move; good size drop, minimal visible cost on typical documents.</li>
        <li><strong>Grayscale first, then compress.</strong> If the document is text + simple graphics, <a href="/grayscale-pdf.html">Grayscale PDF</a> removes color data before compression starts — often a visible size cut with no legibility cost.</li>
        <li><strong>Remove pages you do not need.</strong> The single biggest lever when a form asks for "the last three pages." <a href="/delete-pdf-pages.html">Delete PDF Pages</a> or <a href="/extract-pages-pdf.html">Extract Pages</a>, then compress the smaller result.</li>
        <li><strong>Lower the source resolution.</strong> For scans, re-export or re-scan at 150 dpi instead of 300 before compressing. Softer source, sharper final result than crushing a high-res original.</li>
        <li><strong>Target-size mode at the real limit.</strong> When a number governs, let the tool search for the best quality under that number — and read its honest report about what it achieved.</li>
      </ol>

      <h2>Myths worth retiring</h2>

      <ul>
        <li><strong>"Renaming or re-saving as PDF shrinks it."</strong> It does not. A plain re-save copies the data; only re-encoding images (or removing content) changes size.</li>
        <li><strong>"Bigger is better, always compress less."</strong> For portal caps the opposite is true: a file over the limit is a rejected file. Match the setting to the requirement.</li>
        <li><strong>"Compression destroys quality by a fixed amount."</strong> The cost depends on the content — a text page at 0.4 is usually fine; a photo at 0.4 is visibly degraded. That is why you check the worst-case page.</li>
        <li><strong>"You need desktop software for serious compression."</strong> You need a tool that re-encodes images and tells you what it did. Both categories provide that; the browser one simply runs on your device for free.</li>
      </ul>

      <h2>Quick checklist</h2>

      <ul>
        <li>Know the limit (or lack of one) before choosing a mode: target size for limits, quality slider otherwise.</li>
        <li>Text-heavy → 0.5 is a safe starting point. Photo-heavy → 0.7–0.8 if the photos matter.</li>
        <li>Check the worst-case page of the result; re-run from the original if needed.</li>
        <li>Resistant file? Diagnose (already optimized / vector / encrypted / limit too low) before retrying.</li>
        <li>Keep the original until the output is verified and uploaded.</li>
      </ul>
""",
    faqs=[
        ("Is this really the same as Adobe's 'Save as Optimized PDF'?", "The main mechanism is the same: re-encoding the images that dominate the file size. Adobe adds fine per-object controls (font subsetting, layer removal) that a browser tool does not expose. For the common case — getting a file under an email or portal limit — the browser method does the job that matters; for archival-grade optimization of complex files, a desktop suite remains the stronger instrument."),
        ("Will my text still be selectable after compression?", "In PDFZaap's compress tool, no — pages are re-rendered, so text becomes part of the page image. If you need searchable text in the output, the right sequence is usually: compress a copy for the size-constrained upload, and keep the original (with real text) as your master file. Know the trade-off before you rely on the compressed copy."),
        ("The file got bigger after compression. What happened?", "That happens on already-efficient files — mostly text or dense vector content — where re-rendering adds more bytes than the original carried. The tool's result note tells you when the output is not smaller. Keep the original in that case; do not chase it with a lower quality setting."),
        ("What target size should I pick for email?", "Match the strictest limit in the chain: your mail system and your recipient's. Gmail allows 25 MB per message, Outlook 20 MB, many corporate systems 10 MB or less, and some portals 2 MB. When in doubt, the under-2-MB target is the classic safe attachment size."),
        ("Does the tool add a watermark or branding?", "No. The output contains your document's content only — no watermark, no footer, no branding, no added metadata beyond what the re-render requires."),
    ],
    related=[
        '<a href="/compress-pdf.html">Compress PDF tool</a> — quality slider plus target-size modes, with an honest result report.',
        '<a href="/grayscale-pdf.html">Grayscale PDF tool</a> — cut color data before compressing text-heavy documents.',
        '<a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">How to Check If an Online PDF Tool Uploads Your Files</a> — verify the no-upload behavior yourself in 5 minutes.',
    ],
)

# ---------------------------------------------------------------- 6
POSTS["compress-pdf-under-200kb-job-application"] = dict(
    title="Compress a PDF Under 200 KB for a Job Application",
    meta="Fit your CV or application PDF under a 200 KB portal limit: the size budget, the step-by-step method, photo handling, and what a rejection usually means.",
    og_title="How to Compress a PDF Under 200 KB for a Job Application",
    og_desc="Fit a CV or application PDF under a 200 KB portal limit — the size budget, a step-by-step method, photo handling, and what rejections usually mean.",
    h1="How to Compress a PDF Under 200 KB for a Job Application (Step by Step)",
    date="2026-09-18",
    read=7,
    cta_text="The 200 KB preset is already set — select your CV and let the tool find the quality that fits.",
    cta_href="/compress-pdf-to-200kb.html",
    cta_label="Compress to 200 KB →",
    body="""
      <p>"File size must not exceed 200 KB" — the line that appears on more job portals than you would expect, usually without any explanation of how to meet it. Here is the practical reality: a typical CV PDF is 50–300 KB, so most of the time you are not doing heavy compression, you are making the file a little smaller and doing it in a way that keeps the document legible and professional. This guide covers the size budget, the step-by-step method, and what to do when the portal still says no.</p>

      <div class="quick-box">
        <strong>Quick Answer:</strong>
        <p>Open <a href="/compress-pdf-to-200kb.html">PDFZaap's Compress PDF to 200 KB page</a> — the tool loads with the 200 KB target preset. Select your CV, run the compression, check that the result is under 200 KB and still legible, rename it cleanly (<code>yourname-cv.pdf</code>), and upload. Everything happens in your browser; the file is never uploaded to a server for processing.</p>
      </div>

      <h2>What actually fits in 200 KB</h2>

      <p>Useful numbers, so you know whether your document is a 2-minute job or a rethinking job:</p>

      <table class="post-table">
        <tr><th>Document</th><th>Typical size</th><th>Fits 200 KB?</th></tr>
        <tr><td>2-page text CV, no photo, exported from a word processor</td><td>30–100 KB</td><td>Already fits — nothing to do.</td></tr>
        <tr><td>2–4 page CV with one photo</td><td>150–600 KB</td><td>Usually yes, with mild compression; the photo is the swing factor.</td></tr>
        <tr><td>CV plus cover letter, both with photos</td><td>400 KB–2 MB</td><td>Often yes after compression; check the total after combining.</td></tr>
        <tr><td>Portfolio with images / scanned certificate pack</td><td>2 MB+</td><td>Rarely — trim pages or photos first.</td></tr>
      </table>

      <p>The photo is the lesson. A single decent headshot at typical phone-camera resolution can be 100–500 KB by itself. If your CV has a photo and your file is over the limit, the photo is where the bytes are — and it is the part a recruiter is least likely to scrutinize at 72 dpi versus 300 dpi.</p>

      <h2>Step by step</h2>

      <h3>Step 1 — check the limit exactly</h3>
      <p>Re-read the portal's requirement. "200 KB" sometimes means 200,000 bytes and sometimes 200 × 1024 (204,800) bytes; "per file" vs. "per application" matters if you are submitting a CV and a cover letter separately. If the wording is ambiguous, aim for roughly 90% of the stated limit — about 180 KB for a 200 KB cap — to clear either measurement.</p>

      <h3>Step 2 — decide: combine first, or compress first?</h3>
      <p>If the application asks for one combined file (CV + cover letter), merge them first with the <a href="/merge-pdf.html">Merge PDF tool</a>, then compress the combined file against the 200 KB target. Compressing separately and then combining usually lands you over the limit, because both compressed files carry their own overhead. If it asks for separate files, compress each against its own share of the limit.</p>

      <h3>Step 3 — compress with the 200 KB preset</h3>
      <p>Open <a href="/compress-pdf-to-200kb.html">the Compress PDF to 200 KB page</a> and select your PDF. The target field is already set to "Under 200 KB"; the tool then searches for the best image quality that gets the file under the limit. When it finishes, the result note tells you the size it achieved — and if 200 KB was not reachable for this particular document, it says so plainly instead of silently handing you an unreadable file.</p>

      <h3>Step 4 — the 30-second legibility check</h3>
      <p>Open the compressed file. Look at the photo (is it recognizable and professional-looking?), the smallest print (contact details, references), and any colored or shaded section. If all three are fine, the file is good. If the photo is too degraded, go to Step 5.</p>

      <h3>Step 5 — if it does not fit (or looks bad): trim the source</h3>
      <p>In order of least visible cost:</p>
      <ul>
        <li><strong>Export the CV at lower image quality from the source app</strong> — if you have the word processor file, export the photo at a smaller size or replace it with a smaller headshot export (a 400×500 px headshot is plenty for a CV; it will never be printed at A4).</li>
        <li><strong>Remove the photo</strong> — for many applications a photo is optional; a text-only CV compresses to a fraction of the size and stays perfectly sharp.</li>
        <li><strong>Cut pages</strong> — if the document includes a portfolio appendix or old references, move the weakest page out for this submission.</li>
        <li><strong>Re-scan at 150 dpi</strong> — if the source is a scan, a lower-DPI re-scan is the single biggest lever, and the result is sharper than crushing the 300 dpi original.</li>
      </ul>

      <h3>Step 6 — name it and upload</h3>
      <p>Rename the file to something clean and professional: <code>yourname-cv.pdf</code>. Some legacy portals are picky about spaces and special characters in file names, and a clean name also helps the recruiter's file manager. Then upload, and confirm the portal accepts it before you close the tab.</p>

      <h2>What a rejection usually means</h2>

      <p>If the portal still rejects a file you measured as under 200 KB, the problem is rarely the size itself. The usual culprits, in order:</p>

      <ul>
        <li><strong>KB vs. KiB.</strong> The portal counts 200 × 1024 bytes and your file is 201,300 bytes — "under 200 KB" in decimal but over in binary. Re-compress targeting 180 KB.</li>
        <li><strong>Page count or format rules.</strong> Some portals also cap pages (e.g., "max 5 pages") or only accept certain PDF versions. Check the requirements page, not just the size line.</li>
        <li><strong>File name characters.</strong> Spaces, accents, or dashes that the portal's parser dislikes. Use letters and hyphens only.</li>
        <li><strong>The limit is per application, not per file.</strong> If you submitted a CV and a cover letter, the portal may be summing them.</li>
      </ul>

      <h2>What not to do</h2>

      <ul>
        <li><strong>Do not stack compression passes.</strong> Compressing the compressed file degrades quality each round. If a pass misses the target, change the setting on the original.</li>
        <li><strong>Do not use "compressor" sites you have not vetted</strong> — many of them upload your CV to their servers. A CV with your address, work history, and references is exactly the kind of document that should be processed locally; that is the point of a browser-based tool. The 5-minute check in our <a href="/blog/how-to-check-if-pdf-tool-uploads-files.html">upload-checking guide</a> tells you which kind of tool you are using.</li>
        <li><strong>Do not strip content to meet the limit</strong> — removing a skills section to save 30 KB is a worse decision than asking the recruiter for a larger cap or an alternative upload path (a link, a different format).</li>
        <li><strong>Do not skip the legibility check</strong> because "it is only a CV." Recruiters read small print, and a grainy photo is the first thing they see.</li>
      </ul>

      <h2>Quick checklist</h2>

      <ul>
        <li>Confirm the exact limit (KB vs. KiB, per-file vs. per-application) and aim for ~90% of it.</li>
        <li>Combine first if the portal wants one file; compress the combined result.</li>
        <li>Use the 200 KB preset; read the result note (it tells you the achieved size honestly).</li>
        <li>Check the photo, the small print, and the colored sections before uploading.</li>
        <li>Does not fit? Fix the source (photo size, pages, re-scan DPI) — not the quality setting, again and again.</li>
        <li>Rename cleanly, upload, confirm acceptance.</li>
      </ul>
""",
    faqs=[
        ("My CV is already 150 KB. Do I need to compress it?", "No — if it is under the limit, upload it as is. Compression costs visible quality; do not pay that cost for a file that already fits. The 200 KB target only matters when the file is over it."),
        ("Will my photo look bad after compression to 200 KB?", "For a typical 2–3 page CV, usually not: at the quality the tool settles on, a headshot remains clearly recognizable and professional. The check that matters is the one in Step 4 — open the result and look at the photo before you upload."),
        ("The tool says 200 KB is not reachable for my document. Now what?", "The document has more information than 200 KB can carry at readable quality. Your levers: remove the photo, cut a page, re-scan at lower DPI, or (if the portal allows) ask for a larger cap or a link-based submission. Do not force a quality setting that makes the document unreadable — a rejected-quality CV is worse than a late, honest one."),
        ("Does this tool upload my CV to a server?", "No. The compression runs in your browser; the file is read, processed, and re-exported on your device. If you want to see it for yourself, the Network-tab test in our upload-checking guide shows no file traffic during the process."),
        ("200 KB or 200 KiB — does the tool know the difference?", "The target treats 200 KB as 200 × 1,000 bytes (the common portal interpretation), but the safest habit is to aim for around 180 KB as this guide recommends — then the file clears both interpretations of any 200 KB limit."),
    ],
    related=[
        '<a href="/compress-pdf-to-200kb.html">Compress PDF to 200KB</a> — the tool with the 200 KB target preset, used in this guide.',
        '<a href="/compress-pdf-to-100kb.html">Compress PDF to 100KB</a> — for portals with the tighter cap.',
        '<a href="/merge-pdf.html">Merge PDF tool</a> — combine CV and cover letter into one file before compressing.',
    ],
)

# Content for the 11 Edit & Organize tool pages.

C = {}

C["merge-pdf"] = dict(
    title="Merge PDF Files Online Free — Combine PDFs | PDFZaap",
    meta="Combine multiple PDF files into one document in your browser. Free, no signup, no watermark, and your files are never uploaded to a server.",
    h1="Merge PDF Files — Free, Private, No Signup",
    intro="<p>Combine multiple PDF files into one document without sending anything to a server. Add the files in the order you want, merge them, and download the result — all inside your browser. Page quality is preserved exactly, because merging copies the original page objects rather than re-rendering them. No signup, no watermark, no file cap.</p>",
    howto_title="merge PDF files",
    howto=[
        ("Add your PDFs", "Click the dropzone and select several PDF files at once (or add them in batches)."),
        ("Check the order", "Files appear in the list in the order you selected them. Remove one and re-add it to change the sequence."),
        ("Click Merge PDFs", "The browser copies every page from every file into one new document."),
        ("Download the combined PDF", "The finished file saves straight to your device — nothing was uploaded at any point."),
    ],
    why_title="combine documents without uploading",
    why="<p><strong class='subtext'>Privacy is the whole point.</strong> Merging usually involves files you do not want elsewhere: contracts, invoices, scans of IDs, HR paperwork. Upload-based mergers put those files on a third-party server, even if only for an hour. PDFZaap merges in your browser memory using a local PDF engine, so the files never cross the network. You can verify this yourself — see <a href='/is-it-safe-to-use-online-pdf-tools.html'>how to check that an online PDF tool does not upload your files</a>.</p><p class='subtext'><strong>Lossless by design.</strong> Merging here is a structural operation: original pages are copied whole into the new document. There is no re-rendering, no compression, no quality loss — a 100-page merge looks identical to the 100 separate files, and the text stays fully selectable.</p>",
    tips=[
        "Name your files with numeric prefixes (01-cover.pdf, 02-body.pdf…) so the selection order is the page order.",
        "Merged a file by mistake? Split it back apart with <a href='/split-pdf.html'>Split PDF</a> — the page boundaries are preserved.",
        "If the merged file is too large for an email or portal, run <a href='/compress-pdf.html'>Compress PDF</a> with a target size afterwards.",
        "Rotated or misordered pages? Fix orientation with <a href='/rotate-pdf.html'>Rotate PDF</a> before or after merging.",
        "On an iPhone, see <a href='/blog/how-to-merge-pdf-files-on-iphone.html'>How to merge PDF files on iPhone</a> for the mobile workflow.",
    ],
    when="<p>Use <strong>Merge PDF</strong> whenever the job is 'several PDFs, one file' — applications, invoice bundles, multi-part forms. For the reverse operation, <a href='/split-pdf.html'>Split PDF</a> pulls pages out. To fix page order inside one file, <a href='/reorder-pages-pdf.html'>Reorder Pages</a>. For a no-Adobe walkthrough, read <a href='/blog/merge-pdf-without-adobe.html'>How to merge PDF files without Adobe Acrobat</a>, and for privacy-focused merging, our <a href='/merge-pdf-without-uploading.html'>merge PDF without uploading</a> guide. Also available in <a href='/id/gabung-pdf.html'>Bahasa Indonesia (Gabung PDF)</a> and <a href='/ur/pdf-merge-kaise-karein.html'>Urdu (PDF Merge Kaise Karein)</a>.</p>",
    faqs=[
        ("How many PDFs can I merge?", "As many as your browser's memory allows — there is no imposed limit. For very large batches, merging in two steps (merge halves, then merge the results) keeps things smooth."),
        ("Does merging reduce quality?", "No. Pages are copied at original quality — no re-encoding, no compression, no watermark."),
        ("Will page numbers and bookmarks survive?", "Page content is preserved exactly. Some PDFs keep their bookmarks in the merge; very complex cross-reference bookmarks may not."),
        ("Can I merge encrypted PDFs?", "Only after removing a restriction password with <a href='/unlock-pdf.html'>Unlock PDF</a> (you need the password). Owner-password-locked files that block copying cannot be merged until unlocked."),
    ],
    related=[("split-pdf", "Split PDF"), ("compress-pdf", "Compress PDF"), ("reorder-pages-pdf", "Reorder Pages"), ("extract-pages-pdf", "Extract Pages")],
)

C["split-pdf"] = dict(
    title="Split PDF Online Free — Extract Pages | PDFZaap",
    meta="Split a PDF by page ranges in your browser. Pull out single pages or ranges (e.g. 1-3, 5) into a new file. Free, private, no upload, no watermark.",
    h1="Split a PDF — Pull Out Any Pages",
    intro="<p>Extract exactly the pages you need from a PDF. Enter a range like <code>1-3, 5</code> and the tool builds a new PDF containing just those pages — perfect for pulling a single contract page out of a 200-page bundle, or separating one report from a merged document. Everything happens locally in your browser.</p>",
    howto_title="split a PDF by page ranges",
    howto=[
        ("Select the PDF", "Choose the document you want to take pages from."),
        ("Enter your page range", "Use the 'Page Range' field — e.g. 1-3 for pages one through three, or 1,4,7 for individual pages."),
        ("Click Split PDF", "The listed pages are copied into a new document, in order."),
        ("Download the result", "A new PDF with only the selected pages saves to your device."),
    ],
    why_title="extract pages without touching a server",
    why="<p><strong class='subtext'>Fast, lossless, local.</strong> Splitting is a structural copy: the selected pages keep their exact content, text and quality. Because the work happens in your browser, there is no upload wait, no queue, and no third-party copy of a document that may contain sensitive clauses or personal data.</p><p class='subtext'><strong>The honest fine print.</strong> You get a new PDF with the pages you selected — the original file is untouched. Page numbers in the output restart from 1 (that is how PDFs work), and any bookmarks that pointed to unselected pages simply disappear from the new file. If you need every page as its own separate file, the current workflow is to split one range at a time; that is a deliberate simplicity choice rather than a hidden limitation.</p>",
    tips=[
        "Counting pages: open the PDF and use the page indicator, or extract a quick text dump with <a href='/pdf-to-text.html'>PDF to Text</a> to find where sections start.",
        "Need the pages in a different order afterwards? Use <a href='/reorder-pages-pdf.html'>Reorder Pages</a> on the result.",
        "Splitting out a single page for an email? Pair with <a href='/compress-pdf.html'>Compress PDF</a> to keep it small.",
        "Removing unwanted pages entirely? <a href='/delete-pdf-pages.html'>Delete PDF Pages</a> does the inverse operation.",
        "Step-by-step examples in <a href='/blog/how-to-split-pdf-into-single-pages.html'>How to split a PDF into single pages</a>.",
    ],
    when="<p>Use <strong>Split PDF</strong> to <em>extract</em> pages into a new file. To <em>remove</em> pages from the original, use <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>. To save pages and also keep the rest, do both in sequence. To combine several files instead, <a href='/merge-pdf.html'>Merge PDF</a> is the matching tool.</p>",
    faqs=[
        ("What range formats are supported?", "Comma-separated ranges and single pages: 1-3, 5, 8-10. Pages are numbered from 1."),
        ("Is the quality of extracted pages preserved?", "Yes — pages are copied as-is, so there is zero quality loss."),
        ("Can I get each page as a separate PDF?", "The tool outputs one PDF containing your selection. For individual files, split one page range per run — the workflow is quick for small numbers of pages."),
        ("Does it work on encrypted PDFs?", "Only after unlocking with Unlock PDF (password required)."),
    ],
    related=[("delete-pdf-pages", "Delete PDF Pages"), ("extract-pages-pdf", "Extract Pages"), ("merge-pdf", "Merge PDF"), ("reorder-pages-pdf", "Reorder Pages")],
)

C["compress-pdf"] = dict(
    title="Compress PDF Online Free — Reduce File Size | PDFZaap",
    meta="Compress a PDF in your browser. Pick a quality (0.1 to 1.0) or a target size like 200 KB. Files are processed locally, never uploaded. Free, no watermark.",
    h1="Compress PDF — Free, in Your Browser",
    intro="<p>Reduce the size of a PDF without handing the file to a server. This tool re-renders each page at a quality you control — a simple slider from 0.1 to 1.0 — or aims at a specific target size (100 KB, 200 KB, 500 KB, 1 MB or 2 MB) and finds the best quality that fits. The result downloads with an honest report of the actual size, and if the target is unreachable, it tells you instead of faking it.</p>",
    howto_title="compress a PDF file",
    howto=[
        ("Select the PDF", "Choose the file that is too big for its email, portal or attachment limit."),
        ("Pick a mode", "Set the Image Quality slider (0.1–1.0) for manual control, or choose a Target size such as 'Under 200 KB'."),
        ("Click Compress PDF", "Pages are re-rendered and re-encoded locally. Target mode may take a few passes to find the best fit."),
        ("Download and check the note", "The result includes the original vs. final size — and an honest warning if compression could not help."),
    ],
    why_title="shrink files without uploading them",
    why="<p><strong class='subtext'>No upload, no queue, no watermarks.</strong> Upload-based compressors hold your document on their servers (often with a deletion timer you have to trust) and free tiers frequently add watermarks or daily caps. Here the compression runs in your browser's memory: the file is read locally, re-encoded locally, and saved locally. There is no meter and no branding on the output.</p><p class='subtext'><strong>How it works — and its honest limit.</strong> The tool re-renders each page as a JPEG and rebuilds the PDF around those images. That makes it extremely effective on image-heavy PDFs (scans, reports with photos), but it means the output pages are images: <em>selectable text is not preserved</em>. If your recipient needs to copy text or search the document, compressing this way is the wrong trade — keep the original for that use. For text-critical documents, reduce image resolution at the source instead. See <a href='/blog/why-pdf-blurry-after-compression.html'>why compressed PDFs can look blurry</a> for the trade-offs explained.</p>",
    tips=[
        "Job portal or government upload? Pick the target size that matches the portal's limit — see <a href='/compress-pdf-to-200kb.html'>compress to 200 KB</a> and <a href='/compress-pdf-to-1mb.html'>compress to 1 MB</a> guides.",
        "If the honest note says the file was already efficient, it is probably text-only: re-rendering gains little on text. Split out the image-heavy pages or accept the size.",
        "Quality 0.4–0.6 is the sweet spot for most email attachments; go lower only when the limit is tight.",
        "After compressing, verify the result opens correctly and that page count is unchanged.",
        "For email-specific limits, read <a href='/blog/compress-pdf-for-email.html'>How to compress a PDF for email (under 2 MB)</a>.",
    ],
    when="<p>Use <strong>Compress PDF</strong> when the goal is a <em>smaller file to upload or email</em>. To find out what is making a PDF heavy first, read <a href='/blog/why-is-my-pdf-file-so-large.html'>Why is my PDF file so large?</a>. For quality-safe reduction of image-heavy files, this tool is the right answer; for text-critical documents, prefer source-level fixes. Size-specific guides: <a href='/compress-pdf-to-100kb.html'>100 KB</a>, <a href='/compress-pdf-to-200kb.html'>200 KB</a>, <a href='/compress-pdf-to-500kb.html'>500 KB</a>, <a href='/compress-pdf-to-1mb.html'>1 MB</a>, <a href='/compress-pdf-to-2mb.html'>2 MB</a>. Also available in <a href='/id/kompres-pdf.html'>Bahasa Indonesia (Kompres PDF)</a> and <a href='/ur/pdf-compress-kaise-karein.html'>Urdu (PDF Compress Kaise Karein)</a>.</p>",
    faqs=[
        ("Is text still selectable after compression?", "No — pages are re-rendered as images, so the output is picture-based. If the recipient must search or copy the text, do not compress this way; use the original instead."),
        ("What does the quality slider change?", "It sets the JPEG quality used when re-encoding each page. Lower values = smaller files, softer images. 0.6 is a balanced default."),
        ("What if the target size is not reached?", "The tool tells you honestly. It steps down render resolution and quality as far as usable; if the content simply cannot get smaller (common for dense text), it returns the smallest result and explains why."),
        ("Why did my file get bigger?", "Already-efficient files (pure text, already-compressed scans) can grow when re-rendered. The tool flags this in the result note — in that case, keep the original."),
        ("Is there a file size limit?", "No imposed limit. Very large files need more browser memory and time, since all processing is local."),
    ],
    related=[("split-pdf", "Split PDF"), ("merge-pdf", "Merge PDF"), ("jpg-to-pdf", "JPG to PDF"), ("rotate-pdf", "Rotate PDF")],
)

C["rotate-pdf"] = dict(
    title="Rotate PDF Online Free — Rotate PDF Pages | PDFZaap",
    meta="Rotate all pages of a PDF by 90, 180 or 270 degrees in your browser. The rotation is saved permanently in the file. Free, private, no upload.",
    h1="Rotate PDF Pages — 90°, 180° or 270°",
    intro="<p>Fix sideways or upside-down pages the permanent way. Choose 90°, 180° or 270° and the rotation is written into the PDF itself, so every reader, printer and phone shows the correct orientation. The change is made locally in your browser — the file is never uploaded.</p>",
    howto_title="rotate a PDF",
    howto=[
        ("Select the PDF", "Upload the document with the wrong orientation."),
        ("Choose the angle", "Pick 90° Clockwise, 180° Flip, or 270° Counter-Clockwise from the Rotation Angle menu."),
        ("Click Rotate PDF Pages", "All pages get the rotation flag written in."),
        ("Download the corrected file", "Open it in any reader to confirm the pages sit the right way up."),
    ],
    why_title="fix orientation without a server",
    why="<p><strong class='subtext'>Permanent, not cosmetic.</strong> Some viewers let you rotate on screen only — the underlying file is still sideways, and the next person opens it the wrong way. This tool writes the rotation into the page structure, so the fix travels with the document to every device and printer.</p><p class='subtext'><strong>Zero-risk local edit.</strong> Rotation is one of the safest PDF operations: no re-encoding, no quality change, no content touched — only the orientation flag changes. Doing it in your browser means even a sensitive document never leaves the device. Note that the tool rotates every page by the same angle; if only some pages are wrong, rotate those pages first with <a href='/extract-pages-pdf.html'>Extract Pages</a>, fix them, then <a href='/merge-pdf.html'>Merge PDF</a> everything back together.</p>",
    tips=[
        "Scanner output that is consistently 90° off: rotate once and the whole batch is fixed.",
        "Mixed orientation (some pages straight, some sideways) requires the extract–rotate–merge workflow described above.",
        "180° is the go-to for 'upside-down' documents from duplex scanners that picked the wrong side.",
        "Combine with <a href='/resize-pdf.html'>Resize PDF</a> when you need a standard page size at the same time.",
    ],
    when="<p>Use <strong>Rotate PDF</strong> for orientation fixes. If you need to change page <em>order</em>, that is <a href='/reorder-pages-pdf.html'>Reorder Pages</a>; to change page <em>size</em>, <a href='/resize-pdf.html'>Resize PDF</a>; to trim margins, <a href='/crop-pdf.html'>Crop PDF</a>. For a full orientation-and-layout workflow, our guide <a href='/blog/how-to-merge-pdf-files-on-iphone.html'>How to merge PDF files on iPhone</a> covers the mobile angle.</p>",
    faqs=[
        ("Is the rotation permanent?", "Yes — it is stored in the page's rotation field, so it persists in every PDF reader and printer."),
        ("Can I rotate only some pages?", "Not in one pass — the angle applies to all pages. Use Extract Pages, rotate, and Merge PDF to fix a subset."),
        ("Does rotating change file size or quality?", "No. Only the orientation metadata changes; the content bytes are untouched."),
        ("Why does my PDF look rotated in one app but not another?", "Some viewers honor the rotation flag, others render the raw page. Opening the corrected file in any modern reader shows the true orientation."),
    ],
    related=[("merge-pdf", "Merge PDF"), ("split-pdf", "Split PDF"), ("crop-pdf", "Crop PDF"), ("resize-pdf", "Resize PDF")],
)

C["delete-pdf-pages"] = dict(
    title="Delete PDF Pages Online Free — Remove Pages | PDFZaap",
    meta="Remove specific pages from a PDF in your browser. Enter page numbers like 2, 4-6 and download the cleaned file. Free, private, no upload.",
    h1="Delete Pages from a PDF",
    intro="<p>Remove the pages you do not want — a stray cover, a duplicate signature page, a form instruction sheet — and keep the rest. Enter the page numbers to discard (for example <code>2, 4-6</code>), and the tool writes a clean PDF containing everything else. The original file is untouched, and nothing is uploaded.</p>",
    howto_title="delete pages from a PDF",
    howto=[
        ("Select the PDF", "Upload the document with the unwanted pages."),
        ("Enter the pages to remove", "Use the Pages field: 2 for one page, 2,4 for several, or 4-6 for a range."),
        ("Click Discard Pages", "All other pages are copied into a new document, in their original order."),
        ("Download the cleaned PDF", "Open it to confirm the right pages are gone."),
    ],
    why_title="clean documents locally and safely",
    why="<p><strong class='subtext'>No upload, original preserved.</strong> Deleting pages is usually a pre-send cleanup, often for documents with personal data in exactly the pages you are removing. Doing it in your browser means the sensitive file never crosses the network, and because the tool builds a <em>new</em> file, your original stays exactly as it was.</p><p class='subtext'><strong>What to expect.</strong> The output keeps all remaining pages at full quality with their original order. Page numbers in the output restart at 1 (standard PDF behavior), and any bookmarks pointing to removed pages are lost. If you later realize you deleted the wrong range, just run the tool again on the original — that safety net is one reason to keep source files around.</p>",
    tips=[
        "Double-check page numbers before running — the tool deletes exactly what you type, with no undo on the output.",
        "Removed a page by accident? Run Delete again on the original file; the output file cannot be 'un-deleted' from.",
        "Removing a block of pages from a large document? A range like 12-40 is faster to type than individual numbers.",
        "Need the removed pages separately? Extract them first with <a href='/extract-pages-pdf.html'>Extract Pages</a>, then delete them from the main file.",
    ],
    when="<p>Use <strong>Delete PDF Pages</strong> to <em>remove</em> pages. To <em>keep only</em> certain pages as a new file, use <a href='/extract-pages-pdf.html'>Extract Pages</a> (or <a href='/split-pdf.html'>Split PDF</a>). To rearrange rather than remove, <a href='/reorder-pages-pdf.html'>Reorder Pages</a>. For a page-by-page breakdown of what lives inside a PDF, see <a href='/blog/why-is-my-pdf-file-so-large.html'>Why is my PDF file so large?</a>.</p>",
    faqs=[
        ("How do I specify pages?", "Page numbers from 1, comma-separated, with ranges: 2, 4-6 removes pages 2, 4, 5 and 6."),
        ("Is my original file changed?", "No — the tool creates a new file without the selected pages. Your upload stays intact on your device."),
        ("What happens to page numbers?", "The remaining pages keep their content and order; numbering simply restarts at 1 in the new file."),
        ("Can I remove blank pages only?", "There is no auto-detect for blank pages — identify them in your PDF reader and type the numbers here."),
    ],
    related=[("extract-pages-pdf", "Extract Pages"), ("split-pdf", "Split PDF"), ("reorder-pages-pdf", "Reorder Pages"), ("merge-pdf", "Merge PDF")],
)

C["extract-pages-pdf"] = dict(
    title="Extract Pages from PDF Free Online — Pull Pages | PDFZaap",
    meta="Save selected pages as a new PDF in your browser. Choose pages like 1, 4-8 and download just those. Free, private, no upload, no watermark.",
    h1="Extract Pages from a PDF",
    intro="<p>Pull the pages you need out of a large document and save them as their own small PDF. Type the pages to keep — for example <code>1, 4-8</code> — and the tool copies exactly those pages, in order, into a new file. The source document is not modified, and the work happens entirely in your browser.</p>",
    howto_title="extract pages from a PDF",
    howto=[
        ("Select the PDF", "Upload the document you want to pull pages from."),
        ("Enter the pages to keep", "Use the Pages field: 1 for the first page, 4-8 for a range, or 1,3,5 for individual pages."),
        ("Click Extract Selected Pages", "The listed pages are copied into a new document."),
        ("Download the new PDF", "A compact file containing only your selections saves to your device."),
    ],
    why_title="build small documents from big ones, privately",
    why="<p><strong class='subtext'>The everyday workflow, without uploads.</strong> Extracting is how you turn a 300-page manual into the 4 pages a colleague needs, or a full contract bundle into the signature pages for a scan-and-email. Because it runs locally, the source file — often the most sensitive one — never leaves your device.</p><p class='subtext'><strong>Lossless and reversible.</strong> Pages are copied whole: same text, same images, same quality. The original file stays untouched, so extraction is risk-free — if you picked the wrong range, run it again with the correct one. The one behavioral quirk: the new file's pages are numbered from 1, and bookmarks that referenced the unselected pages do not carry over.</p>",
    tips=[
        "Use extraction as the 'keep' half of a delete/keep split: extract what you want, and optionally delete those pages from the original later.",
        "Combining extracted pages from several source documents? Add the results with <a href='/merge-pdf.html'>Merge PDF</a>.",
        "For job applications where only two pages are allowed, extract exactly those pages and check the file size with <a href='/compress-pdf.html'>Compress PDF</a> if needed.",
        "Step-by-step examples in <a href='/blog/how-to-split-pdf-into-single-pages.html'>How to split a PDF into single pages</a>.",
    ],
    when="<p>Use <strong>Extract Pages</strong> when you want to <em>keep</em> a selection as a new file. To <em>discard</em> pages, use <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>. The two tools are mirror images — same range syntax, opposite result. For reordering without removing, see <a href='/reorder-pages-pdf.html'>Reorder Pages</a>.</p>",
    faqs=[
        ("Can I extract non-consecutive pages?", "Yes — separate page numbers or ranges with commas: 1, 4, 7-9 keeps pages 1, 4, 7, 8 and 9."),
        ("Is the original file modified?", "No. A new PDF is created; the source is unchanged."),
        ("What format is the output?", "A standard PDF containing only the selected pages, in the order you listed them."),
        ("Does it work on password-protected PDFs?", "Only after removing the restriction with Unlock PDF (password required)."),
    ],
    related=[("delete-pdf-pages", "Delete PDF Pages"), ("split-pdf", "Split PDF"), ("merge-pdf", "Merge PDF"), ("reorder-pages-pdf", "Reorder Pages")],
)

C["reorder-pages-pdf"] = dict(
    title="Reorder PDF Pages Online Free — Rearrange PDF | PDFZaap",
    meta="Rearrange the page order of a PDF in your browser. Type a new order like 3,1,2 and download the rearranged file. Free, private, no upload.",
    h1="Reorder PDF Pages",
    intro="<p>Fix the page sequence of a PDF without re-exporting anything. Type the new order — every page exactly once, for example <code>3, 1, 2</code> — and the tool rebuilds the document in that sequence. Useful for correcting bad merge orders, moving a signature page to the end, or sorting a scanned batch. All local, no upload.</p>",
    howto_title="rearrange PDF pages",
    howto=[
        ("Select the PDF", "Upload the document whose page order is wrong."),
        ("Type the new order", "List every page number exactly once, in the order you want: 3, 1, 2 puts the third page first."),
        ("Click Reorder Pages", "The tool validates that every page appears once, then rebuilds the document."),
        ("Download the rearranged PDF", "Flip through to confirm the new sequence."),
    ],
    why_title="fix page order without re-doing the work",
    why="<p><strong class='subtext'>The quick fix for sequencing problems.</strong> A merged document came out in the wrong order. A cover page landed in the middle. A scanned batch needs alphabetizing. Reordering avoids the tedious 'split everything, merge it back' loop — one numbered list is the whole workflow.</p><p class='subtext'><strong>Why local matters.</strong> Reordering is typically done on documents mid-flight — drafts, applications, client packets — the kind you would rather not upload. The tool validates your order (every page exactly once) before rebuilding, so a typo gives you an error instead of a broken file. The result is a brand-new PDF with identical pages in your chosen sequence; the original is untouched.</p>",
    tips=[
        "Count pages first: your list must contain every number from 1 to the page count exactly once.",
        "Big swap of two blocks? Type the order in chunks — e.g. a 20-page doc with pages 11-20 first: 11,12,…,20,1,2,…,10.",
        "If you would rather delete than move, <a href='/delete-pdf-pages.html'>Delete PDF Pages</a> is simpler.",
        "After reordering, <a href='/number-pdf-pages.html'>Add Page Numbers</a> refreshes the numbering to match the new sequence.",
    ],
    when="<p>Use <strong>Reorder Pages</strong> to fix <em>sequence</em>. For removing pages, <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>; for pulling pages into a new file, <a href='/extract-pages-pdf.html'>Extract Pages</a>; for combining documents, <a href='/merge-pdf.html'>Merge PDF</a> (whose order you can then fine-tune here).</p>",
    faqs=[
        ("What order format do I use?", "A comma-separated list of page numbers, containing every page exactly once: 3, 1, 2 means 'page 3 first, then 1, then 2'."),
        ("Will I get an error if my list is wrong?", "Yes — the tool checks that every page appears exactly once and tells you if the list does not match the document."),
        ("Is the original file changed?", "No, a new file is created with the rearranged pages."),
        ("Does reordering affect quality?", "No — pages are copied as-is into the new order."),
    ],
    related=[("merge-pdf", "Merge PDF"), ("delete-pdf-pages", "Delete PDF Pages"), ("extract-pages-pdf", "Extract Pages"), ("number-pdf-pages", "Add Page Numbers")],
)

C["number-pdf-pages"] = dict(
    title="Add Page Numbers to PDF Online Free — Number PDF | PDFZaap",
    meta="Insert page numbers into a PDF in your browser. Choose bottom-center or bottom-right placement and font size. Free, private, no upload, no watermark.",
    h1="Add Page Numbers to a PDF",
    intro="<p>Give a document proper pagination. Choose bottom-center or bottom-right placement, pick a font size, and the tool stamps “Page 1 of 12”-style labels onto every page of the PDF — locally, in your browser, with nothing uploaded. The label format (page number plus total) makes it easy for readers to see how long the document is. Ideal for reports, manuals, applications and anything that will be referenced by page.</p>",
    howto_title="add page numbers to a PDF",
    howto=[
        ("Select the PDF", "Upload the document that needs pagination."),
        ("Choose placement", "Bottom Center is the classic choice; Bottom Right suits documents with headers."),
        ("Set the font size", "12pt is a safe default — readable but unobtrusive."),
        ("Click Add Page Numbers", "Every page is stamped and the finished file downloads."),
    ],
    why_title="paginate documents privately",
    why="<p><strong class='subtext'>Small fix, real impact.</strong> Unpaginated documents make references awkward ('the third table from the end'). Numbers make a document professional and easy to cite — and adding them after the fact beats re-exporting from the source app, which may no longer be available or may reflow everything.</p><p class='subtext'><strong>Honest scope.</strong> This tool numbers every page starting at 1 — there is no 'start at page 3' or 'skip the cover' option, because the number is drawn onto the page as a fixed mark. If you need a cover without a number, the workflow is: number pages 2–N of the extracted body with <a href='/extract-pages-pdf.html'>Extract Pages</a> first, then <a href='/merge-pdf.html'>Merge PDF</a> the cover back in front. The numbers are drawn in a standard font, so they render identically everywhere.</p>",
    tips=[
        "Standard practice: bottom-center for formal documents, bottom-right when a footer or logo occupies the center.",
        "Keep the size modest (10–14pt) so numbers read without competing with content.",
        "Numbering after a <a href='/reorder-pages-pdf.html'>Reorder Pages</a> helps ensure the numbers match the final sequence.",
        "For more elaborate footers (headers, document titles, Bates-style numbering), the source app or a dedicated footer tool is the better fit — this tool is deliberately simple.",
        "See <a href='/blog/how-to-add-page-numbers-to-pdf.html'>How to add page numbers to a PDF in order</a> for the full guide.",
    ],
    when="<p>Use <strong>Add Page Numbers</strong> when you need <em>simple, reliable pagination</em>. For custom headers/footers or starting offsets, go back to the source document's app. Before numbering, finalize the page set with <a href='/delete-pdf-pages.html'>Delete PDF Pages</a> or <a href='/reorder-pages-pdf.html'>Reorder Pages</a> so the numbers match the final document.</p>",
    faqs=[
        ("Can I choose where the number sits?", "Two positions are offered: Bottom Center and Bottom Right, with an adjustable font size from 8 to 24pt."),
        ("Can I start numbering at a different page?", "Not directly — numbering starts at 1 on the first page. Extract the body pages first if the cover should be unnumbered."),
        ("What exactly gets written on the page?", "A “Page N of M” label in standard Helvetica, dark gray, at the font size you choose (8–24pt). It is drawn as vector text, so it stays crisp at any zoom in any reader."),
        ("Does it change the document otherwise?", "No — content, images and existing text are untouched; only the number marks are added."),
    ],
    related=[("merge-pdf", "Merge PDF"), ("extract-pages-pdf", "Extract Pages"), ("add-watermark-pdf", "Add Watermark"), ("reorder-pages-pdf", "Reorder Pages")],
)

C["add-watermark-pdf"] = dict(
    title="Add Watermark to PDF Online Free — Stamp Pages | PDFZaap",
    meta="Stamp a text watermark across every page of a PDF in your browser. Set the text and opacity. Free, private, no upload, no signup.",
    h1="Add a Watermark to a PDF",
    intro="<p>Mark documents as DRAFT, CONFIDENTIAL, or with your name and date — on every page, in one click. Type the watermark text, adjust its opacity, and the tool stamps it across each page of the PDF. The processing is local in your browser, so even sensitive drafts never leave your device.</p>",
    howto_title="watermark a PDF",
    howto=[
        ("Select the PDF", "Upload the document you want to mark."),
        ("Set the watermark text", "The field defaults to CONFIDENTIAL — change it to DRAFT, SAMPLE, your name, a date, or any short label."),
        ("Adjust opacity", "Lower values (around 0.2–0.4) keep the watermark subtle; higher values make it assertive."),
        ("Click Add Watermark", "Every page is stamped and the finished file downloads."),
    ],
    why_title="protect drafts without uploading them",
    why="<p><strong class='subtext'>The classic use case is privacy.</strong> Watermarks usually appear on documents you are about to send to people who should not reuse them — proposals, specs, internal data. Stamping them in your browser means the document takes no trip to a third-party server at all.</p><p class='subtext'><strong>What you get, precisely.</strong> A single text string is drawn on each page in a bold 50pt orange typeface, rotated 45°, at the opacity you choose, positioned in the upper-left area of the page. There is no image watermark support and no per-page variation — one label, whole document, which matches how watermarks are actually used. Because the stamp is drawn onto the pages, it cannot be removed by a reader; only the original unwatermarked file remains clean. Keep that original — a watermarked file is a finished state, not an editable one.</p>",
    tips=[
        "Short text works best (CONFIDENTIAL, DRAFT v2, YOUR NAME 2026) — the stamp is a fixed 50pt, so long labels can run off the page edge.",
        "Opacity 0.3 is the usual balance: clearly visible, does not fight the content.",
        "For 'do not print' workflows, a DRAFT watermark plus <a href='/protect-pdf.html'>Protect PDF</a> (password) is a strong pair.",
        "Watermark before distributing — after a file circulates, you cannot pull versions back.",
    ],
    when="<p>Use <strong>Add Watermark</strong> to label whole documents. For security beyond a visual mark, add a password with <a href='/protect-pdf.html'>Protect PDF</a>. For page references, <a href='/number-pdf-pages.html'>Add Page Numbers</a> is the companion tool. To make the stamped document fully static, follow up with <a href='/flatten-pdf.html'>Flatten PDF</a>.</p>",
    faqs=[
        ("Can I use an image or logo as the watermark?", "This tool applies text watermarks. For a logo stamp, you would need a tool with image-watermark support — we keep this one focused and honest."),
        ("Is the watermark permanent?", "Yes — it is drawn onto each page, so readers cannot toggle it off. Only your original file stays unmarked."),
        ("Does it apply to every page?", "Yes, the same text at the same opacity is stamped on all pages."),
        ("Why would I watermark a private document at all?", "Watermarks discourage reuse and identify leaked copies — they are a deterrent and a trace, not an encryption. For true secrecy, use Protect PDF."),
    ],
    related=[("protect-pdf", "Protect PDF"), ("number-pdf-pages", "Add Page Numbers"), ("flatten-pdf", "Flatten PDF"), ("merge-pdf", "Merge PDF")],
)

C["crop-pdf"] = dict(
    title="Crop PDF Online Free — Trim Page Margins | PDFZaap",
    meta="Crop PDF pages by trimming margins as a percentage of the page (0–45% per side) in your browser. Free, private, no upload.",
    h1="Crop PDF Pages — Trim the Margins",
    intro="<p>Cut down oversized margins, black scanner borders, or unwanted page edges. Enter how much to trim from each side — 0 to 45% of the page width or height per side — and the tool sets new page boundaries so only the remaining area shows. The output keeps the original content quality, and everything runs locally.</p>",
    howto_title="crop a PDF",
    howto=[
        ("Select the PDF", "Upload the document with the margins or borders to remove."),
        ("Set the crop amounts", "Enter percentages for Left, Right, Top and Bottom (e.g. 5% each side for a gentle trim, 10–15% for heavy scanner borders)."),
        ("Click Crop Pages", "Every page's visible area is reduced to the remaining rectangle."),
        ("Download the cropped PDF", "Check a corner to confirm the borders are gone."),
    ],
    why_title="fix oversize pages without re-scanning",
    why="<p><strong class='subtext'>The scanner-border fix.</strong> Flatbed and phone scans frequently come back with a dark border or a thick white margin that no one asked for. Re-scanning is slower; cropping in the browser is one minute. The page box is simply changed — no re-encoding, so quality is untouched.</p><p class='subtext'><strong>Know exactly what cropping does.</strong> Cropping changes the <em>visible</em> area of each page: the trimmed content is still inside the file (PDF viewers can 'show all' to reveal it), but the page now displays only your chosen rectangle. That is ideal for layout and appearance, and it is not a way to securely delete content — for that, use a redaction workflow that removes the data itself. Cropping applies the same percentages to every page, which suits uniform scanner output; for page-by-page differences, process the pages separately with <a href='/extract-pages-pdf.html'>Extract Pages</a>.</p>",
    tips=[
        "Start conservative (3–5% per side) and increase — you can always re-crop the original, but over-cropped content is gone from view.",
        "Scanner black borders are usually 5–12% of the page; phone screenshots with system bars need a larger top or bottom trim.",
        "After cropping, <a href='/resize-pdf.html'>Resize PDF</a> can normalize the pages to A4 or Letter.",
        "Remember cropping is visual: the removed areas remain in the file. For sensitive content, use proper redaction instead.",
    ],
    when="<p>Use <strong>Crop PDF</strong> for uniform margin and border trimming. To change the page <em>size</em> (not just the visible area), use <a href='/resize-pdf.html'>Resize PDF</a>. For removing whole pages, <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>. For fixing orientation before cropping, <a href='/rotate-pdf.html'>Rotate PDF</a> first.</p>",
    faqs=[
        ("How precise is the crop?", "Percentages of the page per side, in 1% steps — enough for borders and margins. For pixel-exact trimming, a desktop PDF editor is the right tool."),
        ("Is the cropped content deleted from the file?", "No — the page boundary changes, but the original content remains in the file and can be revealed by 'show all' in most viewers. This is a visual crop, not redaction."),
        ("Does it apply to all pages?", "Yes, the same crop is applied to every page in the document."),
        ("Why 45% as the maximum?", "Cropping more than that leaves a page too small to be useful — the cap keeps you in sensible territory."),
    ],
    related=[("resize-pdf", "Resize PDF"), ("rotate-pdf", "Rotate PDF"), ("delete-pdf-pages", "Delete PDF Pages"), ("extract-pages-pdf", "Extract Pages")],
)

C["resize-pdf"] = dict(
    title="Resize PDF Page Size Online Free — A4, Letter | PDFZaap",
    meta="Scale PDF pages to A4 or US Letter in your browser. Content is fitted to the standard page. Free, private, no upload, no watermark.",
    h1="Resize PDF Pages — A4 or Letter",
    intro="<p>Put a document onto a standard page size. Whether a form must be A4 for a European portal or Letter for a US one, this tool scales the content of every page onto the target size — fitted, centered, and never distorted. The conversion is local in your browser, with nothing uploaded.</p>",
    howto_title="resize a PDF to A4 or Letter",
    howto=[
        ("Select the PDF", "Upload the document with the wrong page size."),
        ("Choose the target size", "A4 (210 × 297 mm) or US Letter (8.5 × 11 in) from the Page Format menu."),
        ("Click Resize Pages", "Each page's content is scaled to fit the standard page."),
        ("Download the resized PDF", "Print-test one page to confirm the fit."),
    ],
    why_title="match a portal's page size in seconds",
    why="<p><strong class='subtext'>The classic problem: the portal says A4.</strong> Job applications, visa forms and government uploads frequently reject PDFs that are not exactly A4 or Letter. Re-exporting from the source app may not be an option — the source may be a scan, a received file, or a closed system. This tool resizes in place, in the browser, so the file never travels anywhere.</p><p class='subtext'><strong>How the scaling works.</strong> Content is scaled uniformly to fit the target page, then centered — aspect ratio is preserved, so nothing stretches. A landscape page on a portrait target is scaled down and centered (not rotated), so it appears as a smaller block on the page; rotate to portrait first if you need it to fill the width. The trade-off to understand: the page's <em>size</em> becomes standard, but the content is scaled, so very different source sizes (e.g. A3 scans) will appear smaller. For pixel-perfect layouts, redo the document in its source app at the target size.</p>",
    tips=[
        "Check the portal's requirement before converting — A4 and Letter differ in both width and height, and some portals check exactly.",
        "After resizing, run <a href='/compress-pdf.html'>Compress PDF</a> if the portal also has a file size limit.",
        "Mixed-size documents (mostly Letter, two A4 pages) resize every page to the target, which normalizes the whole file.",
        "For just trimming margins without changing the page size, <a href='/crop-pdf.html'>Crop PDF</a> is the lighter operation.",
    ],
    when="<p>Use <strong>Resize PDF</strong> when the requirement is a <em>standard page size</em>. For visual margin trimming, <a href='/crop-pdf.html'>Crop PDF</a>; for orientation, <a href='/rotate-pdf.html'>Rotate PDF</a>; for page-count reductions, <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>. A4 vs. Letter context: <a href='/blog/how-to-convert-jpg-to-pdf-on-windows.html'>How to convert JPG to PDF on Windows</a> covers the page-size choice for image PDFs.</p>",
    faqs=[
        ("Will my content be stretched?", "No — scaling is uniform with the aspect ratio preserved, then the result is centered on the page."),
        ("Can I resize to custom sizes?", "This tool targets A4 and US Letter, the sizes that matter for forms and portals. For custom dimensions, a desktop PDF editor is needed."),
        ("What happens to landscape pages?", "They are scaled down to fit inside the portrait target page and centered — not rotated. A landscape page will appear as a smaller, centered block on the new page. If that is not what you want, rotate the pages to portrait first with Rotate PDF."),
        ("Does the file get bigger or smaller?", "Usually similar or slightly larger, since content is re-placed onto new pages. Compress afterwards if size matters."),
    ],
    related=[("crop-pdf", "Crop PDF"), ("rotate-pdf", "Rotate PDF"), ("compress-pdf", "Compress PDF"), ("merge-pdf", "Merge PDF")],
)

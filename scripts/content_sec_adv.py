# Content for Security (3) + Advanced (6) tool pages.

C = {}

C["unlock-pdf"] = dict(
    title="Unlock PDF Online Free — Remove PDF Password | PDFZaap",
    meta="Remove a restriction (open) password from a PDF in your browser — with the password. Your file stays on your device. Free, private, no upload.",
    h1="Unlock a Password-Protected PDF",
    intro="<p>Have the password to a PDF but find it annoying that the file blocks printing, copying or editing? This tool removes the <em>restriction</em> password using the password you provide, and writes an unlocked copy — entirely in your browser. Your file never leaves the device, and the tool is upfront about what it can and cannot do.</p>",
    howto_title="unlock a PDF with a password",
    howto=[
        ("Select the PDF", "Upload the protected document."),
        ("Enter the password", "Use the Password field if the file needs one to open. Leave it empty for files that open but restrict editing/printing."),
        ("Click Unlock PDF", "The tool verifies the password and rebuilds the file without the restriction."),
        ("Download the unlocked PDF", "The new file can be opened, printed and edited without a prompt."),
    ],
    why_title="unlock your own files privately",
    why="<p><strong class='subtext'>The right tool for the right lock.</strong> PDFs have two kinds of passwords. A <em>restriction</em> password limits what you can do with a file you can already open (copy, print, edit) — and if you own the document or were given the password, removing that restriction is legitimate and routine. An <em>open</em> password blocks access itself, and this tool removes it only with the password in hand.</p><p class='subtext'><strong>What we will not do, and why.</strong> This tool does not attempt to crack, bypass or guess passwords you do not know. That is a deliberate choice: bypassing access controls on documents you do not have rights to is neither something we will build nor something you should do. If you have lost a password to your own important document, a professional data-recovery service is the honest route. Because unlocking runs locally, even a sensitive file takes no network trip at all.</p>",
    tips=[
        "If the PDF opens but blocks copying or printing, leave the password field empty — that is a restriction-only file.",
        "Keep the original encrypted file until you confirm the unlocked copy works everywhere you need it.",
        "After unlocking, <a href='/compress-pdf.html'>Compress PDF</a> or <a href='/merge-pdf.html'>Merge PDF</a> will work where they were blocked before.",
        "To re-protect the unlocked result for the next recipient, use <a href='/protect-pdf.html'>Protect PDF</a> with a new password.",
    ],
    when="<p>Use <strong>Unlock PDF</strong> when you have the password and want the restrictions gone. To <em>add</em> protection afterwards, use <a href='/protect-pdf.html'>Protect PDF</a>. If the file is corrupted instead of locked, try <a href='/repair-pdf.html'>Repair PDF</a>. For the privacy angle on why local processing matters with locked files, see <a href='/is-it-safe-to-use-online-pdf-tools.html'>Is it safe to use online PDF tools?</a>.</p>",
    faqs=[
        ("Can it crack a password I don't know?", "No. The tool only works with the password you supply (or with restriction-only files that need no password). Bypassing unknown passwords is not something it does or should do."),
        ("What is the difference between an open password and a restriction password?", "An open password is required just to view the file. A restriction password lets you view the file but blocks printing, copying or editing. Both can be handled here when you have the password."),
        ("Is my file uploaded anywhere?", "No — the file is read and rewritten locally in your browser."),
        ("Will the unlocked file lose anything?", "Content is preserved. You lose only the restriction, which is the point. Metadata is kept."),
    ],
    related=[("protect-pdf", "Protect PDF"), ("repair-pdf", "Repair PDF"), ("compress-pdf", "Compress PDF"), ("merge-pdf", "Merge PDF")],
)

C["protect-pdf"] = dict(
    title="Protect PDF Online Free — Password Encrypt PDF | PDFZaap",
    meta="Encrypt a PDF with a password in your browser. Only people with the password can open it. Free, private, no upload, no watermark.",
    h1="Protect a PDF with a Password",
    intro="<p>Lock a document so only the right people can open it. Enter a password and this tool encrypts the PDF in your browser, writing a protected file you can share by email or upload to a portal. Because encryption happens locally, the document — often the most sensitive version you have — never touches a server.</p>",
    howto_title="password-protect a PDF",
    howto=[
        ("Select the PDF", "Upload the document you want to encrypt."),
        ("Choose a strong password", "Use the Secure Access Password field. Longer and mixed-character passwords are far harder to guess."),
        ("Click Protect PDF", "The file is encrypted and saved with the new protection."),
        ("Download and test", "Open the protected file to confirm it asks for the password — then send it with the password shared separately."),
    ],
    why_title="share sensitive documents safely",
    why="<p><strong class='subtext'>Encryption before sharing is basic hygiene.</strong> Contracts, payroll, medical summaries and client data should not sit unencrypted in an email folder or a portal inbox. Password protection means the content is useless to anyone without the key — and doing it in your browser means the plaintext document never transits a third-party server.</p><p class='subtext'><strong>Set expectations honestly.</strong> This applies standard PDF password encryption (the same mechanism every major PDF tool uses). It protects the file at rest and in transit folders, but it is not a substitute for secure transfer: send the password in a different channel from the file, choose a genuinely strong password, and remember that the person who receives both the file and the password has full access. For high-stakes data, pair this with a secure file-transfer service and an expiry date on the password.</p>",
    tips=[
        "Send the password separately from the file — never in the same email or message.",
        "Use a passphrase (several random words) rather than a short clever password; it is easier to remember and harder to crack.",
        "Tell recipients the password before they need it, so a locked file does not stall a review.",
        "Need to remove protection later? <a href='/unlock-pdf.html'>Unlock PDF</a> does the reverse with the same password.",
    ],
    when="<p>Use <strong>Protect PDF</strong> before sharing sensitive documents. For a visual 'do not reuse' mark instead of (or with) encryption, use <a href='/add-watermark-pdf.html'>Add Watermark</a>. To remove a password you hold, use <a href='/unlock-pdf.html'>Unlock PDF</a>. For making forms static, <a href='/flatten-pdf.html'>Flatten PDF</a>. More on why local processing matters: <a href='/is-it-safe-to-use-online-pdf-tools.html'>Is it safe to use online PDF tools?</a>.</p>",
    faqs=[
        ("What kind of encryption is used?", "Standard PDF password encryption, the same scheme used by mainstream PDF editors. It protects against casual and most automated access."),
        ("Can I protect against printing only?", "The tool applies password protection to opening the file, which covers printing and copying too. Fine-grained permission flags are a feature of desktop editors."),
        ("Is the file uploaded to a server?", "No. Encryption runs in your browser and the protected file is written locally."),
        ("What if I forget the password?", "You will need it to unlock again (Unlock PDF) — store it safely. PDF encryption is deliberately strong, so there is no recovery backdoor."),
    ],
    related=[("unlock-pdf", "Unlock PDF"), ("add-watermark-pdf", "Add Watermark"), ("flatten-pdf", "Flatten PDF"), ("compress-pdf", "Compress PDF")],
)

C["esign-pdf"] = dict(
    title="E-Sign PDF Online Free — Sign PDF Documents | PDFZaap",
    meta="Draw and embed a signature on a PDF in your browser. Free, private, no upload, no watermark. Perfect for forms, receipts and simple agreements.",
    h1="Sign a PDF — Draw Your Signature",
    intro="<p>Sign a PDF without printing, scanning or an account. Draw your signature on the canvas and the tool stamps it onto the first page of the document at a fixed 180 × 90 pt position — locally, in your browser. The signed file downloads ready to send, and the original never left your device. For multi-page documents, the signature lands on page one, which matches how most forms are signed.</p>",
    howto_title="sign a PDF",
    howto=[
        ("Select the PDF", "Upload the document that needs a signature."),
        ("Draw your signature", "Use your mouse, finger or stylus on the canvas. Clear it and redraw until it looks right."),
        ("Click Sign PDF", "The signature is embedded onto the document and saved."),
        ("Download the signed PDF", "Send it out — the signature is part of the file, not a layer."),
    ],
    why_title="sign documents without uploading them",
    why="<p><strong class='subtext'>The privacy case for local signing.</strong> Documents that need a signature are often the most sensitive in your life — leases, medical consent, financial forms, contracts. Upload-based e-sign services store the document (and sometimes your signature image) on their infrastructure. Drawing the signature and embedding it in your browser means the document and the signature both stay on your device end to end.</p><p class='subtext'><strong>Know what kind of signature this is.</strong> This is a <em>visual</em> electronic signature: your drawn mark embedded in the document. It is perfectly appropriate for forms, receipts, simple agreements and internal workflows. It is not a cryptographic digital signature with certificate-based identity — for those, you need a dedicated e-sign platform that issues and verifies certificates. We would rather state that plainly than blur the two.</p>",
    tips=[
        "Draw slowly and keep the signature compact — small, clean marks embed more cleanly than sprawling ones.",
        "Use the Clear Canvas button as often as you like; there is no limit on redraws.",
        "For a consistent signature across many documents, screenshot your best draw and reuse the style each time.",
        "On a phone, a stylus or two-finger smooth drawing gives the neatest result.",
        "For the no-app iPhone workflow in general, see <a href='/blog/how-to-sign-a-pdf-on-iphone-without-app.html'>How to sign a PDF on iPhone without an app</a>.",
    ],
    when="<p>Use <strong>E-Sign PDF</strong> for a quick, private visual signature. For certificate-based digital signatures with legal verification, a dedicated e-sign service is the right tool. After signing, use <a href='/flatten-pdf.html'>Flatten PDF</a> to make the signed form fully static, and <a href='/protect-pdf.html'>Protect PDF</a> to password-lock the signed result.</p>",
    faqs=[
        ("Is this a legally valid signature?", "A signed PDF is generally accepted as an electronic signature for everyday documents. For high-stakes legal or notarized contexts, check the requirements of the relevant authority — some demand certified digital signatures."),
        ("Can I place the signature exactly where I want?", "Not click-to-place — the signature is stamped at a fixed 180 × 90 pt box in the lower-left area of the first page. For precise placement over a specific line, use a desktop editor or a full e-sign platform."),
        ("Is my signature image stored anywhere?", "No — it is drawn in your browser canvas and embedded only into your document. Nothing is uploaded."),
        ("Does it work on mobile?", "Yes, the canvas accepts touch input, so you can sign directly on a phone or tablet."),
    ],
    related=[("flatten-pdf", "Flatten PDF"), ("protect-pdf", "Protect PDF"), ("add-watermark-pdf", "Add Watermark"), ("merge-pdf", "Merge PDF")],
)

C["repair-pdf"] = dict(
    title="Repair PDF Online Free — Fix Corrupted PDF Files | PDFZaap",
    meta="Attempt to rebuild a corrupted PDF in your browser. Recovers what it can from damaged files and re-saves a clean version. Free, private, no upload.",
    h1="Repair a Corrupted PDF",
    intro="<p>When a PDF will not open — a download cut off mid-transfer, a sync conflict, a flaky save — this tool attempts to read the file's structure, rebuild what it can, and write out a clean version. It runs locally in your browser, so a broken file that contains sensitive data still never leaves your machine. Results depend on how much of the file is intact, and the tool is honest about that.</p>",
    howto_title="repair a corrupted PDF",
    howto=[
        ("Select the damaged PDF", "Upload the file that will not open (or opens only partially)."),
        ("Click Repair PDF", "The tool reads the structure with lenient parsing, skipping broken objects where possible."),
        ("Watch the result", "If the core structure is intact, pages are recovered and re-saved."),
        ("Download the repaired file", "Open it and check that the important pages survived."),
    ],
    why_title="recover files without sending broken data away",
    why="<p><strong class='subtext'>Corrupted files are often sensitive ones.</strong> The file that corrupts is frequently a half-downloaded contract or a partially synced report — exactly what you would not want uploading to a 'repair' service. Local repair keeps that boundary intact.</p><p class='subtext'><strong>Honest about recovery odds.</strong> PDF repair works when the document's internal catalog and page tree are salvageable; a file truncated in the middle often loses its later pages no matter what. This tool uses permissive parsing to recover as much as possible and re-writes a standard file. If it cannot open the file at all, the error says so — at that point, re-downloading the source or using a professional recovery tool is the next step. There is no magic that restores bytes that are simply gone.</p>",
    tips=[
        "Keep the original corrupted file untouched — work on a copy so a failed repair cannot make things worse.",
        "If the file came from a download, re-downloading is often faster than repairing; try that first for small files.",
        "Repaired files may be missing trailing pages; compare the page count against what you expected.",
        "For scanned files that are blurry rather than corrupt, compression or re-scan is the real fix — see <a href='/blog/why-pdf-blurry-after-compression.html'>why PDFs look blurry</a>.",
    ],
    when="<p>Use <strong>Repair PDF</strong> when a file is damaged and will not open. If the file opens but has wrong pages, <a href='/reorder-pages-pdf.html'>Reorder Pages</a> or <a href='/delete-pdf-pages.html'>Delete PDF Pages</a> is the tool. If it is password-locked, <a href='/unlock-pdf.html'>Unlock PDF</a>. For understanding what corruption looks like internally, <a href='/blog/why-is-my-pdf-file-so-large.html'>Why is my PDF file so large?</a> covers file structure.</p>",
    faqs=[
        ("Will it always fix the file?", "No. Recovery depends on how much of the file's structure is intact. The tool reports if it cannot open the file rather than guessing."),
        ("Is my broken file uploaded?", "No — parsing and re-saving happen entirely in your browser."),
        ("What kinds of damage can it handle?", "Common ones: truncated downloads, minor object corruption, broken cross-reference tables. Severely damaged or encrypted-corrupt files may not be recoverable in a browser."),
        ("Does the repaired file lose content?", "It may lose the parts that were unrecoverable. Always compare the result against your expected page count and key pages."),
    ],
    related=[("unlock-pdf", "Unlock PDF"), ("compress-pdf", "Compress PDF"), ("merge-pdf", "Merge PDF"), ("pdf-metadata-editor", "PDF Metadata Editor")],
)

C["ocr-pdf"] = dict(
    title="OCR PDF Free Online — Extract Text from Scans | PDFZaap",
    meta="Run OCR on scanned PDFs and images in your browser with Tesseract.js. File is processed locally; only the public language model downloads. Free, no signup.",
    h1="OCR a Scanned PDF — Get the Text",
    intro="<p>Scanned PDFs and photo documents look like text but contain none — they are images. This tool runs OCR (optical character recognition) on them using Tesseract.js right in your browser, producing a real, copyable text file. Your document is processed locally and never uploaded; the only network fetch is the public English language model on first run.</p>",
    howto_title="extract text from a scan with OCR",
    howto=[
        ("Select a scanned PDF or image", "Upload the document. Clear, printed English text gives the best results — it also accepts JPG, PNG and WebP images."),
        ("Click Extract Text (OCR)", "On first use, the language model loads (a few MB, once). Then each page is rendered and recognized."),
        ("Follow the progress", "A percentage shows as pages are recognized. Larger scans take longer."),
        ("Download the .txt", "The recognized text arrives with page markers, ready to paste or edit."),
    ],
    why_title="make scans searchable without uploading them",
    why="<p><strong class='subtext'>The privacy difference is real.</strong> OCR services are notorious upload sinks — you send the scan to their server, they process it, and you trust their deletion policy. Here the recognition runs in a local Web Worker on your device. The file's pixels never cross the network; the only download is the same public English model everyone using Tesseract gets.</p><p class='subtext'><strong>Know what OCR does well and where it fails.</strong> Clean, high-contrast, printed English text is converted accurately. Small fonts, skew, shadows, low-light photos, columns and handwriting degrade accuracy — and OCR errors are silent, so always proofread important output. This tool gives you a .txt file, not a searchable PDF overlay, because building a reliable text-overlay PDF in the browser is not something we can promise; the text file is the honest, useful deliverable.</p>",
    tips=[
        "Scan at 300 dpi or higher, straight on, with good contrast — image quality is the single biggest accuracy factor.",
        "Deskew the scan first (rotate with <a href='/rotate-pdf.html'>Rotate PDF</a>) if pages are tilted; OCR dislikes skew.",
        "For a long document, OCR a page or two first to check quality before committing to the whole file.",
        "After OCR, feed the text into <a href='/pdf-to-word.html'>PDF to Word</a> workflows or paste it into your document of choice.",
        "Full walkthrough in <a href='/blog/how-to-make-pdf-searchable-from-scanner.html'>How to make a scanned PDF searchable</a>.",
    ],
    when="<p>Use <strong>OCR PDF</strong> when your source is a <em>scan or image</em> and you need the words. For PDFs that already have a text layer, <a href='/pdf-to-text.html'>PDF to Text</a> is faster and exact. To turn recognized text into an editable document, pair with <a href='/pdf-to-word.html'>PDF to Word</a>. For the no-upload verification method, see <a href='/is-it-safe-to-use-online-pdf-tools.html'>Is it safe to use online PDF tools?</a>.</p>",
    faqs=[
        ("Does it need internet?", "Only the first time, to download the public English language model. Your document is never sent anywhere — recognition is local."),
        ("How accurate is it?", "Very good for clean printed English; noticeably worse for small type, skew, photos and handwriting. Always proofread critical results."),
        ("Why not a searchable PDF output?", "A proper text-overlay PDF is hard to produce reliably in a browser, so we output clean text instead of promising a half-working overlay. Paste the text where you need it."),
        ("What languages are supported?", "English in this build. Tesseract supports many languages, but this tool is configured for English to keep the model download small and the results focused."),
    ],
    related=[("pdf-to-text", "PDF to Text"), ("pdf-to-word", "PDF to Word"), ("rotate-pdf", "Rotate PDF"), ("pdf-to-epub", "PDF to EPUB")],
)

C["compare-pdf"] = dict(
    title="Compare PDF Files Online Free — Find Differences | PDFZaap",
    meta="Diff the text of two PDF versions in your browser. Added and removed lines are highlighted in an HTML report. Free, private, no upload.",
    h1="Compare Two PDF Versions",
    intro="<p>Spot what changed between two versions of a document. Upload a draft and a final (exactly two PDFs), and the tool extracts the text from each, diffs it line by line, and gives you an HTML report with additions and removals clearly highlighted plus a summary count. Both files stay on your device the entire time.</p>",
    howto_title="compare two PDF files",
    howto=[
        ("Select two PDFs", "Add Document A (the earlier version) and Document B (the later one) — exactly two files."),
        ("Click Compare Documents", "Text is extracted from both, line by line."),
        ("Watch the diff compute", "The tool aligns the two text streams and marks changes."),
        ("Download the HTML report", "Open it in any browser: green = added, red = removed, with a change count at the top."),
    ],
    why_title="verify revisions without sending either version",
    why="<p><strong class='subtext'>Revisions are sensitive.</strong> The two versions you are comparing are usually a draft and the signed or final document — both potentially containing confidential terms. A local diff means neither file is uploaded, and the report is generated on your machine.</p><p class='subtext'><strong>What the comparison covers.</strong> The diff is text-based: it compares the extractable words, line by line, and reports what was added or removed. It is ideal for catching changed numbers, renamed parties, or edited clauses. It does not compare layout, formatting, images or embedded objects — if two versions differ only visually, a text diff will say they are the same. And because it works on the text layer, both documents need real text (run <a href='/ocr-pdf.html'>OCR PDF</a> first on any scans).</p>",
    tips=[
        "Use it on redlined contracts: the removed/added lines show exactly what moved between versions.",
        "Very large documents (hundreds of pages) may exceed the in-browser diff limit; compare a narrower section with <a href='/extract-pages-pdf.html'>Extract Pages</a> first.",
        "Save the HTML report alongside the final document as an audit artifact.",
        "For a quick 'did anything change?' check, the summary count at the top of the report is the fastest answer.",
    ],
    when="<p>Use <strong>Compare PDFs</strong> to verify text changes between two versions. To isolate the pages that differ, extract ranges first with <a href='/extract-pages-pdf.html'>Extract Pages</a>. To pull the full text of either version for a deeper read, use <a href='/pdf-to-text.html'>PDF to Text</a>. For scanned sources, <a href='/ocr-pdf.html'>OCR PDF</a> comes first.</p>",
    faqs=[
        ("How exactly are the files compared?", "Visible text is extracted from each PDF and diffed line by line. The alignment finds which lines are shared, added, or removed."),
        ("What does the report look like?", "A standalone HTML file: a summary count of additions and removals, then a line-by-line list with green (added) and red (removed) highlights."),
        ("Does it compare formatting or images?", "No — text only. Visual or layout changes are not detected."),
        ("Why exactly two files?", "A line diff is defined between two documents. To compare more versions, run pairwise comparisons."),
    ],
    related=[("pdf-to-text", "PDF to Text"), ("extract-pages-pdf", "Extract Pages"), ("ocr-pdf", "OCR PDF"), ("pdf-metadata-editor", "PDF Metadata Editor")],
)

C["pdf-metadata-editor"] = dict(
    title="PDF Metadata Editor Free Online — Title & Author | PDFZaap",
    meta="Edit a PDF's Title, Author, Subject and Keywords in your browser. Changes only the metadata, not the pages. Free, private, no upload.",
    h1="Edit PDF Metadata",
    intro="<p>Fix the document's identity: title, author, subject and keywords. PDFs carry a small metadata block that file managers, search and archive systems read — and it is frequently wrong or empty. This tool lets you set or overwrite those fields in your browser and save a corrected file. Pages are untouched; only the metadata changes.</p>",
    howto_title="edit PDF metadata",
    howto=[
        ("Select the PDF", "Upload the document whose metadata you want to change."),
        ("Fill in the fields", "Set Title, Author, Subject and Keywords in the panel. Leave a field blank to leave it as-is where the tool supports it."),
        ("Click Update Metadata", "The fields are written into the document."),
        ("Download the updated PDF", "Check the properties in your PDF reader to confirm the changes stuck."),
    ],
    why_title="clean up document identity locally",
    why="<p><strong class='subtext'>Metadata is how documents get found.</strong> A file called 'scan_0042.pdf' with an empty title is hard to find, cite or archive. Correct metadata makes your documents searchable in file managers and archive systems, and gives them a professional identity in properties dialogs.</p><p class='subtext'><strong>Surgical and safe.</strong> The tool writes only the metadata fields you set — the pages, text and images are byte-for-byte unchanged. Because it runs locally, you can fix metadata on sensitive documents without any upload. Note that metadata is descriptive, not security: it is visible to anyone who opens the file's properties, so do not put secrets in the Keywords or Subject fields.</p>",
    tips=[
        "Use a consistent title scheme (e.g. 'Client — Report — 2026-Q3') so files sort and search predictably.",
        "Set the Author to the real author or team, not a tool name — it helps with provenance later.",
        "Keywords are for searchability; a handful of precise terms beat a long list.",
        "For long-term archiving with dates and subject set automatically, use <a href='/pdf-to-pdfa.html'>PDF Archival Prep</a>.",
    ],
    when="<p>Use <strong>PDF Metadata Editor</strong> for full manual control over identity fields. For a one-click archival preset (dates, subject, producer), use <a href='/pdf-to-pdfa.html'>PDF Archival Prep</a>. To add visible page references, <a href='/number-pdf-pages.html'>Add Page Numbers</a>. For locking down a finished document, <a href='/protect-pdf.html'>Protect PDF</a>.</p>",
    faqs=[
        ("Which fields can I edit?", "Title, Author, Subject and Keywords — the standard document information fields."),
        ("Are the pages changed?", "No. Only the metadata block is written; all visible content is preserved exactly."),
        ("Is metadata private?", "No — anyone who opens the file can view its properties. Treat metadata as public descriptive data, not a place for secrets."),
        ("Why not edit metadata in a PDF reader?", "Many readers allow it, but not all, and it is easy to miss. This tool makes the four key fields explicit and consistent."),
    ],
    related=[("pdf-to-pdfa", "PDF Archival Prep"), ("flatten-pdf", "Flatten PDF"), ("protect-pdf", "Protect PDF"), ("add-watermark-pdf", "Add Watermark")],
)

C["flatten-pdf"] = dict(
    title="Flatten PDF Free Online — Lock Form Fields | PDFZaap",
    meta="Flatten a PDF in your browser: form fields and annotations merge into static pages so nothing can be edited. Free, private, no upload.",
    h1="Flatten a PDF — Make It Static",
    intro="<p>Turn an interactive PDF into a fixed one. Flattening merges form fields, filled-in answers and annotations into the page itself, so the document can no longer be edited as a form — it becomes a static record. This is the standard final step after filling or signing a form, and it all happens locally in your browser.</p>",
    howto_title="flatten a PDF",
    howto=[
        ("Select the PDF", "Upload the form or annotated document you want to make static."),
        ("Click Flatten PDF", "Interactive elements are merged into the page content."),
        ("Download the flattened file", "Open it and confirm the fields are now fixed text, not editable boxes."),
    ],
    why_title="lock in filled forms permanently",
    why="<p><strong class='subtext'>The last step of a form workflow.</strong> After someone fills in or signs a PDF form, the fields are still interactive — a recipient could accidentally change an answer. Flattening bakes the entered values into the page so the document is a true record. Sending a flattened form is the professional habit for contracts, applications and receipts.</p><p class='subtext'><strong>One-way, and that is the point.</strong> Flattening is not reversible — once the fields are merged, you cannot 'un-fill' the form from the flattened file. Always keep the original blank (or pre-fill) version before flattening. Because it runs locally, a filled form containing personal data never uploads anywhere in the process.</p>",
    tips=[
        "Keep the original fillable form — flattening is a finishing step, not an editing one.",
        "Flatten after <a href='/esign-pdf.html'>E-Sign PDF</a> to lock a signature into the page permanently.",
        "Flatten after <a href='/add-watermark-pdf.html'>Add Watermark</a> or <a href='/number-pdf-pages.html'>Add Page Numbers</a> to make the marks part of the static page.",
        "If a flattened file still has editable boxes, it may contain features beyond simple fields — a desktop tool is needed for those.",
    ],
    when="<p>Use <strong>Flatten PDF</strong> to finalize filled or signed forms into static records. To fill and sign first, use <a href='/esign-pdf.html'>E-Sign PDF</a>. For password-locking the result, <a href='/protect-pdf.html'>Protect PDF</a>. For archival metadata on the flattened record, <a href='/pdf-to-pdfa.html'>PDF Archival Prep</a>. Guide: <a href='/blog/how-to-fill-out-pdf-form-without-printing.html'>How to fill out a PDF form without printing</a>.</p>",
    faqs=[
        ("What exactly does flattening do?", "It converts interactive form fields and annotations into static page content, so they can no longer be edited or filled."),
        ("Is it reversible?", "No. Keep the original file if you may need to edit the form again. The flattened file is the finished, static version."),
        ("Will it remove my filled-in answers?", "No — the answers are preserved, they just become fixed text/images on the page instead of editable fields."),
        ("Does it change the appearance?", "It should look the same. The values you entered remain visible; they are no longer interactive."),
    ],
    related=[("esign-pdf", "E-Sign PDF"), ("protect-pdf", "Protect PDF"), ("add-watermark-pdf", "Add Watermark"), ("pdf-to-pdfa", "PDF Archival Prep")],
)

C["grayscale-pdf"] = dict(
    title="Grayscale PDF Online Free — Black and White PDF | PDFZaap",
    meta="Convert PDF pages to black and white in your browser. Reduces color for print and archiving. Free, private, no upload, no watermark.",
    h1="Convert a PDF to Grayscale",
    intro="<p>Strip the color out of a PDF. Converting to grayscale (black, white and shades of gray) is useful for saving ink on printing, meeting a document's monochrome requirement, or normalizing colorful scans before archiving. The conversion renders in your browser and the file is never uploaded.</p>",
    howto_title="turn a PDF grayscale",
    howto=[
        ("Select the PDF", "Upload the color document you want to convert."),
        ("Click Convert to Grayscale", "Each page is re-rendered without color."),
        ("Download the grayscale PDF", "Print a test page to check contrast before committing."),
    ],
    why_title="monochrome output without a server",
    why="<p><strong class='subtext'>Practical, not just aesthetic.</strong> Grayscale saves ink and toner, satisfies 'black and white only' submission rules, and makes mixed-color documents look consistent. It can also shrink file size, since color images re-encode more compactly in grayscale. For print shops and high-volume offices, the toner savings across a long document add up quickly, and a monochrome file behaves more predictably across different printers and paper stocks than a color one does.</p><p class='subtext'><strong>What to expect.</strong> The tool re-renders pages to grayscale, so the result is visually faithful — colors map to their brightness. Very light pastels can become hard to see, and color-coded information (red vs. blue categories) loses its distinction, which is the fundamental trade-off of any grayscale conversion. If your document relies on color to convey meaning, keep a color master and check a test print of the grayscale version first. Because pages are re-rendered at 1.5× scale (the same mechanism as the compressor), the output is image-based: the grayscale file looks right but its text is not selectable, so keep the color original for anything that needs copyable text.</p>",
    tips=[
        "Print one test page before converting a long document — light grays are the usual surprise.",
        "Grayscale before <a href='/compress-pdf.html'>Compress PDF</a> for the smallest print-ready file.",
        "If only some pages need monochrome, extract them first with <a href='/extract-pages-pdf.html'>Extract Pages</a>.",
        "For pure two-tone (no gray shades), a threshold/dither step in an image editor is a separate, heavier operation — this tool produces true grayscale.",
    ],
    when="<p>Use <strong>Grayscale PDF</strong> for monochrome output and print savings. For size reduction specifically, <a href='/compress-pdf.html'>Compress PDF</a> is more direct. To remove pages instead, <a href='/delete-pdf-pages.html'>Delete PDF Pages</a>. For normalizing scans before archiving, follow with <a href='/pdf-to-pdfa.html'>PDF Archival Prep</a>.</p>",
    faqs=[
        ("Does it reduce file size?", "Often yes, because color images compress more compactly as grayscale — but the main purpose is appearance and ink savings, not size."),
        ("Can light colors disappear?", "Very light pastels can map to near-white and become hard to read. Test-print to check."),
        ("Is it reversible?", "No — color information is discarded in the re-render. Keep the original color file if you may need it."),
        ("Is text still selectable afterwards?", "No — like the compressor, this tool re-renders each page (at 1.5× scale, JPEG quality 0.85) with the color removed, so the output pages are images. Text looks the same, but it is not copyable in the result. Keep the original for any use that needs selectable text."),
    ],
    related=[("compress-pdf", "Compress PDF"), ("pdf-to-pdfa", "PDF Archival Prep"), ("extract-pages-pdf", "Extract Pages"), ("rotate-pdf", "Rotate PDF")],
)

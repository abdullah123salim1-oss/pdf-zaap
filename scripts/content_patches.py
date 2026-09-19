# Depth patches: one extra tip, one extra FAQ, and an extra 'when' sentence per thin page.
# Format: tool -> (tip_html, (faq_q, faq_a), when_sentence_html)

P = {}

P["grayscale-pdf"] = (
    "After converting, <a href='/pdf-to-jpg.html'>PDF to JPG</a> is unnecessary — grayscale PDFs print directly and stay editable as PDFs.",
    ("Can I convert back to color?", "No. Grayscale discards the color channels during the re-render, so the original color file is the only way back to color. That is why keeping the color master matters."),
    "Grayscale is also a preprocessing step before <a href='/ocr-pdf.html'>OCR PDF</a>, since monochrome input often recognizes slightly cleaner than color scans.",
)

P["reorder-pages-pdf"] = (
    "Keep a plain-text note of the original order before a big rearrangement — it is the fastest undo if the new sequence is wrong.",
    ("Can I move just one page to the end?", "Yes — list all the other pages in their current order and put the target page number last, e.g. for a 10-page document moving page 1 to the end: 2, 3, 4, 5, 6, 7, 8, 9, 10, 1."),
    "If the document is a merge you just made, it is often cleaner to <a href='/merge-pdf.html'>Merge PDF</a> again in the right order than to reorder.",
)

P["pdf-to-epub"] = (
    "Import the EPUB into your e-reader before sharing it — a 30-second read-through catches ordering surprises early.",
    ("What happens to headers and footers on each page?", "They become part of the page's text flow, so running heads and page numbers appear as lines within each chapter. For a cleaner book, remove them from the source document first with <a href='/delete-pdf-pages.html'>Delete PDF Pages</a> or a text pass."),
    "For longer works, converting per volume (using <a href='/split-pdf.html'>Split PDF</a>) gives you separate EPUB files that match the way people actually read them.",
)

P["pdf-metadata-editor"] = (
    "Batch workflow: fix metadata on each new export immediately — metadata debt accumulates faster than file debt.",
    ("Will changing metadata break links or references to the file?", "No. Metadata is descriptive information; the document's content and structure are unchanged, so bookmarks and references to the file keep working."),
    "If you manage many documents, consistent Title and Author conventions double as a lightweight filing system — pair them with <a href='/pdf-to-pdfa.html'>PDF Archival Prep</a> for long-term storage.",
)

P["flatten-pdf"] = (
    "Flatten the final version only — flatten after all edits, signatures and watermarks are in place, not before.",
    ("Does flattening reduce file size?", "Not reliably. It removes the form structure but keeps the rendered content, so size may stay the same or shift slightly. Compress afterwards if size matters."),
    "For forms you will reuse, flatten a copy for each submission — the original fillable form stays available for the next recipient.",
)

P["extract-pages-pdf"] = (
    "Extracting for a specific recipient? Name the output file after them or the purpose — extracted pages are easy to misfile.",
    ("What if I type a page number that does not exist?", "Out-of-range numbers are ignored, so the extraction still succeeds with the valid pages you listed. Double-check your list to avoid silent gaps."),
    "A common pair: extract the pages you need, then <a href='/compress-pdf.html'>Compress PDF</a> the result if the recipient has a size limit.",
)

P["png-to-pdf"] = (
    "Screenshots of code or UI? Keep them at the display's native resolution so text stays sharp on the PDF page.",
    ("Why does my PNG look pixelated on the page?", "If the source image is small but the page is large, the image simply has fewer pixels than the page needs — capture at higher resolution rather than letting the tool stretch it."),
    "For mixed content (photos plus graphics), convert the photos with <a href='/jpg-to-pdf.html'>JPG to PDF</a> in a separate file and keep the crisp graphics in their own PNG PDF.",
)

P["pdf-to-png"] = (
    "Annotating? PNGs open in any image editor — draw your marks, then recombine with <a href='/png-to-pdf.html'>PNG to PDF</a>.",
    ("Why are my PNG files so much bigger than JPGs?", "PNG is lossless, so it stores every pixel exactly — that is the quality win and the size cost at the same time. For web sharing, the JPG version is usually the practical choice."),
    "If you only need a few pages, extract them first with <a href='/extract-pages-pdf.html'>Extract Pages</a> instead of converting the whole document.",
)

P["excel-to-pdf"] = (
    "For recurring reports, keep a 'PDF-ready' sheet with only the columns stakeholders see — converting it every period becomes trivial.",
    ("Why are my column widths different in the PDF?", "The converter lays out columns from the data as it finds them; very narrow or very wide Excel columns can look different once paginated. Adjust widths in Excel for the best print fit."),
    "When a workbook has more than 10 sheets, convert the sheets that matter — recipients rarely need the data-prep sheets in a shared document.",
)

P["pdf-to-text"] = (
    "Keep the .txt alongside the PDF in the same folder — it is your quick-search copy of the document.",
    ("Why does some text come out with odd spacing?", "PDFs store text positions, not spaces, so the tool reconstructs spacing from gaps. Dense or justified text may show extra spaces — a quick edit in any text editor cleans it up."),
    "If the text looks scrambled, the PDF likely uses floating text boxes; extracting a cleaner re-export or using OCR on a rendered copy often works better.",
)

P["pdf-to-html"] = (
    "After downloading, open the file with the browser's developer tools to confirm the structure before uploading it to your site.",
    ("Can I add my own navigation or links later?", "Yes — the output is plain semantic HTML, so adding a table of contents, anchors or internal links is a normal HTML edit."),
    "For a document you will publish and update regularly, converting the text and rebuilding the page in your site's template gives you the most control over the final design.",
)

P["rotate-pdf"] = (
    "After rotating, print a single test page before sending the whole document — orientation bugs are cheapest to catch early.",
    ("Can I rotate pages in different directions at once?", "Not in one pass — every page gets the same angle. To fix a mix, use <a href='/extract-pages-pdf.html'>Extract Pages</a> to separate the groups, rotate each, and <a href='/merge-pdf.html'>Merge PDF</a> them back together."),
    "Rotating is also the first fix for scanner feeds that grabbed the wrong edge — one 90° pass straightens the whole batch.",
)

P["number-pdf-pages"] = (
    "For documents over 50 pages, test the number size on one page first — 10pt is often more proportionate than 12pt on dense pages.",
    ("Will the numbers print clearly?", "Yes — the numbers are drawn as vector text in a standard font, so they print crisp at any size, unlike a scanned-in number."),
    "If your organization requires a specific footer format (document codes, Bates numbers), that is beyond this tool's scope — use the source app's header/footer features instead.",
)

P["delete-pdf-pages"] = (
    "Before deleting, extract the pages you are removing with <a href='/extract-pages-pdf.html'>Extract Pages</a> — a small archive of 'removed' pages is cheap insurance.",
    ("Can I delete pages and keep the file name the same?", "The download keeps a generated name; rename the file to match your filing convention immediately so the cleaned version is easy to find."),
    "For a document with many scattered unwanted pages, typing all ranges in one go (2, 5, 9-11, 14) is faster than multiple runs.",
)

P["add-watermark-pdf"] = (
    "Version your watermarks (DRAFT v1, DRAFT v2) so leaked copies can be traced to a specific send.",
    ("Can different pages have different watermarks?", "No — one text, applied to every page. For per-page marks, watermark each extracted section separately and merge them back with <a href='/merge-pdf.html'>Merge PDF</a>."),
    "If the document is headed to many recipients, pair the watermark with <a href='/protect-pdf.html'>Protect PDF</a> so the marked copy is also password-locked.",
)

P["compare-pdf"] = (
    "Run the comparison right after receiving the final version, while the differences are still fresh in your memory.",
    ("The files look identical but the report shows changes — why?", "Whitespace, hyphenation or invisible characters can differ between versions even when the visible words match. Check the flagged lines — often they are formatting artifacts rather than real edits."),
    "If both versions are scanned images, extract their text with <a href='/ocr-pdf.html'>OCR PDF</a> first and compare the recognized text instead.",
)

P["ppt-to-pdf"] = (
    "Before converting, delete any slides that are placeholder 'coming soon' pages — they become PDF pages you have to live with.",
    ("Why are my slide images missing from the PDF?", "The converter re-lays out slide text and does not render embedded background images or charts. For a visual-identical export, use PowerPoint's own 'Export as PDF'. This tool is for clean, searchable text pages."),
    "For a deck that must circulate read-only, the PDF output is the distribution format — keep the .pptx as the master for future edits.",
)

P["html-to-pdf"] = (
    "Save a copy of the HTML next to the PDF you generate, so the source for a future re-render is always at hand.",
    ("Why is my PDF text not selectable?", "The converter renders each page as an image, which makes the layout exact but the text non-selectable. If you need selectable text, use your browser's built-in 'Print → Save as PDF' on the HTML file instead."),
    "For long HTML documents, check pagination on the last page — content that runs short can look unfinished and is easy to fix with a bit more content or a page break in the markup.",
)

P["word-to-pdf"] = (
    "Convert, then open the PDF and scroll to the last page — pagination surprises hide at the end of documents.",
    ("Why did my headings change font in the PDF?", "The converter maps standard Word styles to standard PDF fonts; custom or embedded fonts that the browser cannot match fall back to a similar standard face. Standard documents are unaffected."),
    "For documents with tables, check one table page after converting — column widths are preserved but very wide tables can reflow across pages.",
)

P["split-pdf"] = (
    "Keep a note of the original page count before splitting — it is the fastest sanity check on your range syntax.",
    ("Can I split into several ranges in one go?", "The tool creates one output PDF containing everything you list. For separate files per range, run one split per range — each run is quick and local."),
    "Splitting is also a prep step for <a href='/compress-pdf.html'>Compress PDF</a>: shrink only the image-heavy section of a mixed document instead of the whole thing.",
)

P["pdf-to-pdfa"] = (
    "Store the prepared file in a stable location with a stable name — archival value comes from the file staying findable, not just from its metadata.",
    ("Does the tool validate whether a file is already PDF/A?", "No. It writes archival metadata but does not run PDF/A validation. To check an existing file's PDF/A status, use a dedicated PDF/A validator."),
    "For a batch of records, prep each file, then record the file names and dates in a simple index sheet — metadata plus an index is a complete mini-archive.",
)

P["resize-pdf"] = (
    "After resizing, compare one page against the portal's sample format if one is provided — page size plus margins is what portals actually check.",
    ("Why did my page get a white border after resizing?", "Content is scaled to fit the target page with a margin and centered, so a source that was smaller than the target shows white space around it — the page size is now standard, which is the goal."),
    "If the portal also limits file size, follow the resize with <a href='/compress-pdf.html'>Compress PDF</a> targeting the stated limit.",
)

P["pdf-to-powerpoint"] = (
    "Before converting, remove appendices you will never present — every PDF page becomes a slide you must manage.",
    ("Can I edit the text on a slide after converting?", "No — each slide is a rendered image of the page. You can reorder, duplicate, annotate and add new text boxes over it, but the page's own text stays as part of the image."),
    "For decks that alternate text slides and image slides, converting the text slides with this tool and the image slides as <a href='/pdf-to-jpg.html'>PDF to JPG</a> exports gives you a mixed deck with the best of both.",
)

P["crop-pdf"] = (
    "Crop a single test page first (extract it with <a href='/extract-pages-pdf.html'>Extract Pages</a>, crop, inspect) before applying settings to the whole document.",
    ("Can I crop different amounts for different pages?", "The tool applies the same crop to every page. For page-specific trimming, extract the affected pages, crop separately, and merge back with <a href='/merge-pdf.html'>Merge PDF</a>."),
    "If the goal is a standard page size rather than just less white space, <a href='/resize-pdf.html'>Resize PDF</a> is the more direct tool.",
)

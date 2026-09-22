// ==========================================================================
// DATA CONFIGURATION & DATABASES
// ==========================================================================

// Configure the pdf.js worker to match the loaded library version (required for reliable rendering)
if (typeof pdfjsLib !== 'undefined' && pdfjsLib.GlobalWorkerOptions) {
  pdfjsLib.GlobalWorkerOptions.workerSrc = new URL('pdfjs-worker.js', document.currentScript.src).href;
}

const TOOL_DATABASE = {
  "pdf-to-word": {
    title: "PDF to Word",
    emoji: "📝",
    subtitle: "Extract PDF text into an editable Word (.docx) document",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert to Word",
    outputExt: ".docx",
    category: "convert",
    metaDesc: "Turn a PDF into an editable Word document in your browser. Text-based conversion: words and reading order are kept, layouts simplified. Free and private.",
    steps: [
      { title: "Upload PDF", desc: "Select or drag the PDF document." },
      { title: "Convert", desc: "The browser extracts text and builds a .docx file." },
      { title: "Download Word", desc: "Save the editable Word document." }
    ],
    features: [
      { title: "Editable Output", desc: "Every word lands in a real .docx you can edit." },
      { title: "Reading Order", desc: "Lines are grouped into paragraphs top to bottom." },
      { title: "No Server Upload", desc: "Processing runs entirely on your device." },
      { title: "No Watermark", desc: "No limits, branding, or signups added." }
    ],
    faqs: [
      { q: "Is the layout preserved perfectly?", a: "No — this is a text-based conversion. Words and reading order are kept, but multi-column layouts, tables, and images are simplified. That is the honest trade-off of doing this entirely in the browser." },
      { q: "Can I convert scanned PDFs?", a: "Scanned pages contain no real text, so run OCR PDF first to get the words, then convert the result." },
      { q: "Are files private?", a: "Yes. The file never leaves your device; the .docx is built in your browser." }
    ],
    related: ["pdf-to-text", "pdf-to-jpg", "word-to-pdf", "ocr-pdf"]
  },
  "pdf-to-jpg": {
    title: "PDF to JPG",
    emoji: "🖼️",
    subtitle: "Convert PDF pages to JPEG format images",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert PDF to JPG",
    outputExt: ".zip",
    category: "convert",
    metaDesc: "Convert each PDF page layer into a separate flat JPG image container inside your browser quickly.",
    steps: [
      { title: "Select PDF", desc: "Upload a standard document container." },
      { title: "Page Render", desc: "Render individual vectors as canvas objects." },
      { title: "Save Images", desc: "Extract files as a sequential download ZIP." }
    ],
    features: [
      { title: "High Resolution", desc: "Pages are exported with clear rendering quality." },
      { title: "Zip Compression", desc: "Packs multiple pages into a neat zip container." },
      { title: "Quick Processing", desc: "Instant extraction using local resources." },
      { title: "100% Private", desc: "All files remain strictly local." }
    ],
    faqs: [
      { q: "What format are the images in?", a: "Standard high-quality .jpg format." },
      { q: "How are multiple files packaged?", a: "If the PDF contains multiple pages, they will be bundled inside a ZIP." }
    ],
    related: ["pdf-to-png", "pdf-to-text", "jpg-to-pdf", "pdf-to-word"]
  },
  "pdf-to-excel": {
    title: "PDF to Excel",
    emoji: "📊",
    subtitle: "Turn PDF text lines into spreadsheet rows (.xlsx)",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Extract to Excel",
    outputExt: ".xlsx",
    category: "convert",
    metaDesc: "Extract the text of a PDF into an editable Excel sheet in your browser. Each text line becomes a row. Free, private, no signup.",
    steps: [
      { title: "Select PDF", desc: "Upload the report or statement PDF." },
      { title: "Extract", desc: "Text lines are read and split into cells where columns are clear." },
      { title: "Export XLSX", desc: "Download the .xlsx file and tidy up as needed." }
    ],
    features: [
      { title: "Real .xlsx Output", desc: "A standard Excel file you can filter and sort." },
      { title: "Column Splitting", desc: "Tabs and wide gaps become separate cells." },
      { title: "Local Processing", desc: "No data is sent over the network." },
      { title: "Free & Unlimited", desc: "No subscription or file caps." }
    ],
    faqs: [
      { q: "Does it rebuild the exact table layout?", a: "Not perfectly — it extracts text lines and splits cells where the PDF has tabs or clear column spacing. Complex merged tables may need light manual cleanup in Excel." },
      { q: "Are formulas included?", a: "No. You get the visible numbers and text as values, which you can then work with." }
    ],
    related: ["excel-to-pdf", "pdf-to-word", "pdf-to-text", "pdf-metadata-editor"]
  },
  "pdf-to-powerpoint": {
    title: "PDF to PowerPoint",
    emoji: "📈",
    subtitle: "Convert page vectors into presentation slides",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert to PowerPoint",
    outputExt: ".pptx",
    category: "convert",
    metaDesc: "Convert layout design patterns back into standard presentation slide matrices.",
    steps: [
      { title: "Upload PDF", desc: "Select files to restructure." },
      { title: "Process Slides", desc: "Build sequential matrix nodes on the slide canvas." },
      { title: "Retrieve Slide Deck", desc: "Download presentation slides." }
    ],
    features: [
      { title: "Slide Layouts", desc: "Treats pages as design boards." },
      { title: "Editable Vectors", desc: "Extracts structured objects to coordinate grids." },
      { title: "Free Processing", desc: "No license required for browser conversions." },
      { title: "Local Conversion", desc: "Data processed securely on device." }
    ],
    faqs: [
      { q: "Can I edit shapes after converting?", a: "Yes, shapes are mapped as distinct objects." }
    ],
    related: ["ppt-to-pdf", "pdf-to-word", "pdf-to-jpg", "pdf-to-png"]
  },
  "pdf-to-text": {
    title: "PDF to Text",
    emoji: "📝",
    subtitle: "Isolate and copy characters to plain text files",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Extract Plain Text",
    outputExt: ".txt",
    category: "convert",
    metaDesc: "Extract clean, copyable text characters directly from PDF page indexes in seconds.",
    steps: [
      { title: "Select Document", desc: "Load structured text documents." },
      { title: "Isolate Characters", desc: "Extract strings page by page." },
      { title: "Save Document", desc: "Retrieve a clean text file." }
    ],
    features: [
      { title: "Plain Layout", desc: "Exports raw text without formatting hurdles." },
      { title: "Fast Scraping", desc: "Processes dense files quickly." },
      { title: "Zero Uploads", desc: "All files remain local for complete security." },
      { title: "Unlimited Pages", desc: "Process extensive documents smoothly." }
    ],
    faqs: [
      { q: "How does text matching work?", a: "The tool targets character coordinates inside the PDF vector map." }
    ],
    related: ["pdf-to-word", "pdf-to-jpg", "ocr-pdf", "pdf-metadata-editor"]
  },
  "pdf-to-html": {
    title: "PDF to HTML",
    emoji: "🌐",
    subtitle: "Extract PDF text into a clean, readable HTML page",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Generate HTML",
    outputExt: ".html",
    category: "convert",
    metaDesc: "Turn a PDF into a clean HTML page in your browser. Text is kept in reading order; page graphics are not embedded. Free and private.",
    steps: [
      { title: "Upload PDF", desc: "Select the document to convert." },
      { title: "Extract", desc: "Text is read page by page and grouped into lines." },
      { title: "Download HTML", desc: "Save a self-contained .html file." }
    ],
    features: [
      { title: "Readable Output", desc: "Each page becomes a labeled section of paragraphs." },
      { title: "Self-Contained", desc: "The .html file needs no external assets to open." },
      { title: "Local Processing", desc: "The PDF never leaves your device." },
      { title: "Free & Unlimited", desc: "No signups or page limits." }
    ],
    faqs: [
      { q: "Does it recreate the visual design?", a: "No — this extracts the text content in reading order, not the visual layout. Multi-column pages may read out of order. It is a content conversion, not a design clone." },
      { q: "Are images included?", a: "No. For page images, use PDF to JPG or PDF to PNG and embed them yourself." }
    ],
    related: ["html-to-pdf", "pdf-to-text", "pdf-to-word", "ocr-pdf"]
  },
  "pdf-to-png": {
    title: "PDF to PNG",
    emoji: "🖼️",
    subtitle: "Export pages as transparent PNG images",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert PDF to PNG",
    outputExt: ".zip",
    category: "convert",
    metaDesc: "Extract pages as high-quality transparent PNG formats instantly.",
    steps: [
      { title: "Upload PDF", desc: "Select your document." },
      { title: "Render Options", desc: "Output page layers on clean canvas formats." },
      { title: "Download Output", desc: "Retrieve a zipped set of files." }
    ],
    features: [
      { title: "Transparent Render", desc: "Keeps page background properties clear." },
      { title: "High Fidelity", desc: "Saves design elements with excellent resolution." },
      { title: "Local Speed", desc: "Converts pages instantly using browser memory." },
      { title: "Completely Free", desc: "Export unlimited page configurations." }
    ],
    faqs: [
      { q: "Are individual files bundled?", a: "Yes, multiple pages are bundled in a ZIP." }
    ],
    related: ["pdf-to-jpg", "png-to-pdf", "pdf-to-text", "pdf-to-word"]
  },
  "pdf-to-epub": {
    title: "PDF to EPUB",
    emoji: "📚",
    subtitle: "Turn a PDF's text into a reflowable EPUB e-book",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert to EPUB",
    outputExt: ".epub",
    category: "convert",
    metaDesc: "Convert a PDF into a reflowable EPUB e-book in your browser. Each page becomes a chapter of selectable text. Free, private, no upload.",
    steps: [
      { title: "Select PDF", desc: "Upload the book or long document." },
      { title: "Build Chapters", desc: "Text is extracted and each page becomes a chapter." },
      { title: "Download EPUB", desc: "Import the .epub into your e-reader." }
    ],
    features: [
      { title: "Reflowable Text", desc: "Read on any screen size with adjustable fonts." },
      { title: "Real EPUB 3", desc: "Valid package structure with a table of contents." },
      { title: "Local Processing", desc: "Your book never leaves your device." },
      { title: "Free & Unlimited", desc: "No accounts or page caps." }
    ],
    faqs: [
      { q: "Does it preserve images in EPUBs?", a: "No — this converts the text only. Images and complex layout are not embedded, so it works best on text-based books and documents." },
      { q: "Will the chapter structure be correct?", a: "Each PDF page becomes one chapter in the table of contents. Headings inside the pages are not detected, so the structure is page-based." }
    ],
    related: ["pdf-to-text", "pdf-to-word", "pdf-metadata-editor", "ocr-pdf"]
  },
  "pdf-to-pdfa": {
    title: "PDF Archival Prep",
    emoji: "💾",
    subtitle: "Embed archival metadata for long-term storage (not a certified PDF/A conversion)",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Prep for Archiving",
    outputExt: ".pdf",
    category: "advanced",
    metaDesc: "Prepare a PDF for long-term archiving: embeds title, subject and date metadata in your browser. Honest note: not a certified PDF/A conversion.",
    steps: [
      { title: "Select PDF", desc: "Upload the document to archive." },
      { title: "Embed Metadata", desc: "Title, subject and creation/modification dates are written in." },
      { title: "Download PDF", desc: "Save the archival-prepared file. For certified PDF/A, run a validator (see the guide)." }
    ],
    features: [
      { title: "Real Metadata", desc: "Writes standard PDF info fields used by archive systems." },
      { title: "Honest Scope", desc: "This is preparation, not certified PDF/A validation." },
      { title: "100% Client-Side", desc: "Files never leave your machine." },
      { title: "High Fidelity", desc: "Pages and content are untouched — only metadata changes." }
    ],
    faqs: [
      { q: "What is PDF/A?", a: "An ISO-standardized (ISO 19005) version of PDF designed for long-term archiving, requiring things like embedded fonts and an XMP metadata block." },
      { q: "Does this produce a certified PDF/A file?", a: "No. A browser cannot run the full PDF/A validation required for certification. This tool prepares the metadata; to certify a file, convert it with dedicated tooling such as LibreOffice, Ghostscript, or an online validator, then verify it." }
    ],
    related: ["pdf-metadata-editor", "flatten-pdf", "protect-pdf", "compress-pdf"]
  },
  "word-to-pdf": {
    title: "Word to PDF",
    emoji: "📄",
    subtitle: "Convert standard Word documents into web-friendly portable PDFs",
    accept: ".docx",
    multiple: false,
    execBtnText: "Convert to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Convert DOCX files to clean portable documents directly in your browser.",
    steps: [
      { title: "Select DOCX", desc: "Upload Word documents." },
      { title: "Process Vector", desc: "Read document structures and typography layers." },
      { title: "Download PDF", desc: "Get high-quality PDF files instantly." }
    ],
    features: [
      { title: "Vector Preservation", desc: "Keeps fonts and graphical elements clear." },
      { title: "Fast Processing", desc: "Direct browser rendering without delay." },
      { title: "Safe & Local", desc: "Data remains on your device throughout." },
      { title: "Free Forever", desc: "No license fees or user limitations." }
    ],
    faqs: [
      { q: "Are DOC files supported?", a: "Please convert DOC files to standard DOCX formats before processing." }
    ],
    related: ["pdf-to-word", "jpg-to-pdf", "png-to-pdf", "html-to-pdf"]
  },
  "jpg-to-pdf": {
    title: "JPG to PDF",
    emoji: "🖼️",
    subtitle: "Convert your JPEG images into a single PDF document in seconds",
    accept: ".jpg,.jpeg",
    multiple: true,
    execBtnText: "Convert JPG to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Convert JPEG files to clean PDF pages instantly with our private converter.",
    steps: [
      { title: "Upload JPGs", desc: "Drag and drop one or more images." },
      { title: "Arrange Pages", desc: "Configure page layouts." },
      { title: "Export PDF", desc: "Generate your cohesive document." }
    ],
    features: [
      { title: "No Compression", desc: "Maintains original image quality." },
      { title: "Combine Files", desc: "Combines multiple images into one clean document." },
      { title: "Completely Private", desc: "All files are processed locally on your machine." },
      { title: "Fast Execution", desc: "Get converted files instantly." }
    ],
    faqs: [
      { q: "Can I adjust page margins?", a: "Yes, pages automatically scale to match image dimensions." }
    ],
    related: ["png-to-pdf", "pdf-to-jpg", "word-to-pdf", "merge-pdf"]
  },
  "excel-to-pdf": {
    title: "Excel to PDF",
    emoji: "📊",
    subtitle: "Convert Excel spreadsheets to clean portable documents",
    accept: ".xlsx,.xls",
    multiple: false,
    execBtnText: "Convert Excel to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Convert an Excel (.xlsx/.xls) workbook to a PDF in your browser. Sheets render as bordered tables. Free, private, no upload.",
    steps: [
      { title: "Select File", desc: "Upload your .xlsx or .xls workbook." },
      { title: "Render Sheets", desc: "Each sheet becomes bordered tables on landscape A4 pages (up to 10 sheets, 5,000 rows each)." },
      { title: "Download PDF", desc: "Save the document." }
    ],
    features: [
      { title: "Table Layout", desc: "Cells render as bordered tables, headers included." },
      { title: "Client Security", desc: "The workbook never leaves your device." },
      { title: "Honest Limits", desc: "Charts, formulas-as-results and merged cells may simplify; very wide sheets paginate." },
      { title: "Always Free", desc: "No signup, no watermark, no caps." }
    ],
    faqs: [
      { q: "Does it support multiple sheets?", a: "Yes — up to the first 10 sheets are exported, each labeled with its sheet name. Large sheets are limited to 5,000 rows per export." },
      { q: "Are charts included?", a: "No. This renders cell values as tables; embedded charts and images are not drawn. Print from Excel if you need the chart visuals." }
    ],
    related: ["pdf-to-excel", "word-to-pdf", "png-to-pdf"]
  },
  "ppt-to-pdf": {
    title: "PowerPoint to PDF",
    emoji: "📈",
    subtitle: "Convert presentation slide decks to PDF format",
    accept: ".pptx",
    multiple: false,
    execBtnText: "Convert PPT to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Convert PPTX slide structures into vector presentation pages.",
    steps: [
      { title: "Upload PPTX", desc: "Select slide decks from your device." },
      { title: "Fidelity Check", desc: "Map slide elements to PDF page margins." },
      { title: "Save Slide PDF", desc: "Retrieve your portable presentation files." }
    ],
    features: [
      { title: "Keep Styling", desc: "Preserves fonts, vector graphics, and image qualities." },
      { title: "Local Convert", desc: "Converts slides in memory on your device." },
      { title: "Fast Turnaround", desc: "Generates files in seconds." },
      { title: "Free of Use", desc: "No watermarks or subscription models." }
    ],
    faqs: [
      { q: "Are slide animations kept?", a: "PDF is a static format, so animations are rendered as fixed pages." }
    ],
    related: ["pdf-to-powerpoint", "word-to-pdf", "jpg-to-pdf", "png-to-pdf"]
  },
  "html-to-pdf": {
    title: "HTML to PDF",
    emoji: "🌐",
    subtitle: "Convert an HTML file to a printed-style PDF in your browser",
    accept: ".html,.htm,.txt",
    multiple: false,
    execBtnText: "Convert HTML to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Turn an HTML file into a PDF in your browser. Common styles render; keep assets inline for the best result. Free, private, no upload.",
    steps: [
      { title: "Select HTML", desc: "Upload a single .html file (inline styles work best)." },
      { title: "Render", desc: "The browser lays out the markup on A4 pages." },
      { title: "Download PDF", desc: "Save the resulting document." }
    ],
    features: [
      { title: "Inline CSS Works", desc: "Fonts, colors, borders and basic layout render as printed." },
      { title: "100% Private", desc: "Your markup never leaves your machine." },
      { title: "A4 Output", desc: "Content flows across standard A4 pages." },
      { title: "Free & Unlimited", desc: "No account, no file caps, no watermark." }
    ],
    faqs: [
      { q: "Are linked stylesheets supported?", a: "Styles in <style> blocks and inline attributes render reliably. External stylesheets and images need to be reachable from your browser; inlining everything gives the most predictable result." },
      { q: "Is the PDF text selectable?", a: "No — the page is rendered as an image per page, so it looks exactly like the layout but the text is not selectable. Use a print-to-PDF from your browser if you need selectable text." }
    ],
    related: ["pdf-to-html", "word-to-pdf", "png-to-pdf", "jpg-to-pdf"]
  },
  "png-to-pdf": {
    title: "PNG to PDF",
    emoji: "🖼️",
    subtitle: "Convert PNG images into a clean PDF document",
    accept: ".png",
    multiple: true,
    execBtnText: "Convert PNG to PDF",
    outputExt: ".pdf",
    category: "convert",
    metaDesc: "Combine multiple transparent or flat PNG files into a single PDF document in your browser.",
    steps: [
      { title: "Select PNGs", desc: "Upload your image files." },
      { title: "Page Map", desc: "Scale layouts dynamically in the workspace." },
      { title: "Export PDF", desc: "Download your cohesive document instantly." }
    ],
    features: [
      { title: "Transparency Kept", desc: "Preserves your original transparency parameters." },
      { title: "Combine Files", desc: "Easily combines several images into one document." },
      { title: "Fast & Free", desc: "Instant local processing with zero costs." },
      { title: "Secure Processing", desc: "Your images are processed entirely on your device." }
    ],
    faqs: [
      { q: "Does converting change dimensions?", a: "Pages are automatically sized to match original image dimensions." }
    ],
    related: ["jpg-to-pdf", "pdf-to-png", "word-to-pdf", "merge-pdf"]
  },
  "merge-pdf": {
    title: "Merge PDF",
    emoji: "🔗",
    subtitle: "Combine multiple PDF documents into one single file",
    accept: ".pdf",
    multiple: true,
    execBtnText: "Merge PDFs",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Combine multiple PDF documents into a single, organized file. Fully free, local browser-based execution with no limits.",
    steps: [
      { title: "Upload PDFs", desc: "Select or drag multiple PDF files." },
      { title: "Order Files", desc: "Arrange files in the order you want." },
      { title: "Merge & Download", desc: "Click merge and download your combined PDF." }
    ],
    features: [
      { title: "Unlimited Files", desc: "Merge as many PDFs as you need at once." },
      { title: "Preserve Quality", desc: "No quality loss during merging." },
      { title: "Fast Processing", desc: "Merges in seconds in your browser." },
      { title: "100% Private", desc: "Files never leave your device." }
    ],
    faqs: [
      { q: "How many PDFs can I merge?", a: "You can merge unlimited PDFs at once." },
      { q: "Does merging reduce quality?", a: "No, quality is fully preserved." },
      { q: "Is it free?", a: "Yes, completely free forever." }
    ],
    related: ["split-pdf", "compress-pdf", "reorder-pages-pdf", "extract-pages-pdf"]
  },
  "split-pdf": {
    title: "Split PDF",
    emoji: "✂️",
    subtitle: "Extract specific pages or page ranges from a PDF document instantly",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Split PDF",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Extract specific pages or page ranges from a PDF document instantly in your browser. Complete local client-side PDF splitter.",
    steps: [
      { title: "Upload PDF", desc: "Select the PDF file." },
      { title: "Define Range", desc: "Input desired page ranges (e.g. 1-3, 5)." },
      { title: "Download", desc: "Download the extracted page PDF." }
    ],
    features: [
      { title: "Range Support", desc: "Splits ranges and individual pages." },
      { title: "Client Processing", desc: "Processed instantly in browser." },
      { title: "Fully Secure", desc: "Files do not upload to any server." },
      { title: "Free of Cost", desc: "No restrictions or hidden charges." }
    ],
    faqs: [
      { q: "What ranges are supported?", a: "You can define simple ranges like '1-3' or comma-separated lists like '1,3,5'." },
      { q: "How fast is splitting?", a: "Splitting is processed instantly using local resources." }
    ],
    related: ["merge-pdf", "delete-pdf-pages", "extract-pages-pdf", "reorder-pages-pdf"]
  },
  "compress-pdf": {
    title: "Compress PDF",
    emoji: "📉",
    subtitle: "Reduce the size of your documents while maintaining text accuracy and format",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Compress PDF",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Compress a PDF in your browser: pick a quality from 0.1 to 1.0, or choose a target size like 100 KB, 200 KB or 2 MB. Files are processed locally, never uploaded.",
    steps: [
      { title: "Upload PDF", desc: "Drag and drop the document to shrink." },
      { title: "Pick a Mode", desc: "Set a quality from 0.1 to 1.0, or choose a target size (e.g. under 200 KB) and the tool finds the best fit." },
      { title: "Download", desc: "Save the compressed file — with an honest report of the final size." }
    ],
    features: [
      { title: "High Compression", desc: "Reduces file size dramatically." },
      { title: "Adjustable Quality", desc: "Control target properties using visual sliders." },
      { title: "No Server Lag", desc: "Processed entirely inside local memory spaces." },
      { title: "Uncompromised Text", desc: "Text vectors remain clear and legible." }
    ],
    faqs: [
      { q: "What does the slider change?", a: "The compression slider adjusts embedded image resolution and quality profiles." }
    ],
    related: ["merge-pdf", "split-pdf", "rotate-pdf", "flatten-pdf"]
  },
  "rotate-pdf": {
    title: "Rotate PDF",
    emoji: "🔄",
    subtitle: "Rotate individual or all page layers permanently by selected angle variants",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Rotate PDF Pages",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Rotate PDF documents 90, 180, or 270 degrees permanently. Processing runs fully on client browser.",
    steps: [
      { title: "Upload PDF", desc: "Select files for rotation." },
      { title: "Select Angle", desc: "Choose clockwise rotation configurations." },
      { title: "Download File", desc: "Retrieve your rotated PDF instantly." }
    ],
    features: [
      { title: "Page Control", desc: "Rotates all page vectors at once." },
      { title: "Instant Rotation", desc: "Executes in memory inside your browser." },
      { title: "Safe & Private", desc: "Data is processed locally and securely." },
      { title: "Completely Free", desc: "No licensing barriers or limitations." }
    ],
    faqs: [
      { q: "Is rotation permanent?", a: "Yes, rotation is written directly to the page metadata." }
    ],
    related: ["merge-pdf", "split-pdf", "crop-pdf", "resize-pdf"]
  },
  "delete-pdf-pages": {
    title: "Delete PDF Pages",
    emoji: "❌",
    subtitle: "Discard unwanted page layers within structural documents",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Discard Pages",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Remove unwanted pages from your PDF documents securely within your web browser.",
    steps: [
      { title: "Upload PDF", desc: "Choose documents to clean." },
      { title: "Identify Pages", desc: "Enter page indexes to discard." },
      { title: "Save PDF", desc: "Download the updated document." }
    ],
    features: [
      { title: "Accurate Removal", desc: "Removes only specified index pages." },
      { title: "Private Operations", desc: "Processing runs entirely in browser memory." },
      { title: "Quick Processing", desc: "Generates files in seconds." },
      { title: "100% Free", desc: "Unlimited uses with zero watermarks." }
    ],
    faqs: [
      { q: "How do I specify pages?", a: "Enter comma-separated values like '2, 4, 6' to remove those specific pages." }
    ],
    related: ["extract-pages-pdf", "split-pdf", "reorder-pages-pdf", "merge-pdf"]
  },
  "extract-pages-pdf": {
    title: "Extract Pages",
    emoji: "📤",
    subtitle: "Isolate structural select page frames from multi-page documents",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Extract Selected Pages",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Extract specific page arrays to save them as a new, organized PDF document instantly.",
    steps: [
      { title: "Select PDF", desc: "Upload files for processing." },
      { title: "Identify Pages", desc: "Enter page indexes to keep." },
      { title: "Download", desc: "Save your extracted page PDF." }
    ],
    features: [
      { title: "Accurate Selection", desc: "Extracts target pages cleanly." },
      { title: "Safe Processing", desc: "All files remain securely on your local device." },
      { title: "Fast Execution", desc: "Instant local extraction with zero delays." },
      { title: "Free to Use", desc: "Process unlimited documents with no limitations." }
    ],
    faqs: [
      { q: "Can I extract non-consecutive pages?", a: "Yes, enter list selections like '1, 4, 7' to keep only those pages." }
    ],
    related: ["delete-pdf-pages", "split-pdf", "reorder-pages-pdf", "merge-pdf"]
  },
  "reorder-pages-pdf": {
    title: "Reorder Pages",
    emoji: "🔀",
    subtitle: "Rearrange specific layouts cleanly before saving",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Reorder & Save",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Rearrange page sequences easily inside your PDF documents with our private, local editor.",
    steps: [
      { title: "Upload PDF", desc: "Choose files to rearrange." },
      { title: "Reorder Index", desc: "Define your new page order sequence." },
      { title: "Save Layout", desc: "Get your updated document instantly." }
    ],
    features: [
      { title: "Complete Flexibility", desc: "Set any custom page order." },
      { title: "Safe Processing", desc: "Data is processed strictly in your local browser." },
      { title: "Fidelity Preserved", desc: "No quality loss during structure updates." },
      { title: "Always Free", desc: "Unlimited use with zero registration requirements." }
    ],
    faqs: [
      { q: "How do I input the sequence?", a: "Enter the new order as a list of numbers, e.g., '3, 2, 1, 4'." }
    ],
    related: ["split-pdf", "merge-pdf", "delete-pdf-pages", "extract-pages-pdf"]
  },
  "number-pdf-pages": {
    title: "Add Page Numbers",
    emoji: "🔢",
    subtitle: "Apply position-customized page counts to document pages",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Add Page Numbers",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Apply clean, customizable page counts to your PDF document headers or footers instantly.",
    steps: [
      { title: "Upload PDF", desc: "Select document files." },
      { title: "Position Settings", desc: "Choose bottom-center or bottom-right options." },
      { title: "Save PDF", desc: "Retrieve your numbered document." }
    ],
    features: [
      { title: "Adjustable Settings", desc: "Position page numbers exactly where you need them." },
      { title: "Vector Output", desc: "Text maps cleanly over existing elements." },
      { title: "Secure Processing", desc: "All files are processed privately on your machine." },
      { title: "Free Always", desc: "No watermarks or subscription models." }
    ],
    faqs: [
      { q: "Where are numbers positioned?", a: "Choose bottom-center or bottom-right options." }
    ],
    related: ["add-watermark-pdf", "merge-pdf", "split-pdf", "rotate-pdf"]
  },
  "add-watermark-pdf": {
    title: "Add Watermark",
    emoji: "🏷️",
    subtitle: "Apply customizable text watermarks to your PDF pages",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Apply Watermark",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Protect your PDF documents by drawing secure diagonal text watermarks across pages instantly.",
    steps: [
      { title: "Upload PDF", desc: "Select your target document." },
      { title: "Set Properties", desc: "Input watermark text and select opacity values." },
      { title: "Save Output", desc: "Retrieve your protected PDF instantly." }
    ],
    features: [
      { title: "Adjustable Opacity", desc: "Set background text transparency from 0.1 to 1.0." },
      { title: "Secure Protection", desc: "Apply protective text layers to all pages." },
      { title: "Fast Execution", desc: "Instant local processing in browser memory." },
      { title: "100% Free", desc: "No limitations or watermark branding." }
    ],
    faqs: [
      { q: "What styling is used?", a: "Standard diagonal transparent Orange typography is used." }
    ],
    related: ["protect-pdf", "number-pdf-pages", "compress-pdf", "flatten-pdf"]
  },
  "crop-pdf": {
    title: "Crop PDF",
    emoji: "📐",
    subtitle: "Adjust visual margins or crop boundaries on your PDF pages",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Crop Document",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Adjust bounding boxes and crop PDF pages cleanly using client-side tools.",
    steps: [
      { title: "Upload PDF", desc: "Select document files." },
      { title: "Set Margins", desc: "Define crop boundary dimensions." },
      { title: "Download PDF", desc: "Get your cropped document." }
    ],
    features: [
      { title: "Accurate Cropping", desc: "Define crop areas with precise dimensions." },
      { title: "Safe Processing", desc: "Files are processed entirely on your local machine." },
      { title: "Fidelity Preserved", desc: "No image compression or text rasterization." },
      { title: "Always Free", desc: "Unlimited document crops at zero cost." }
    ],
    faqs: [
      { q: "Does cropping delete text?", a: "No, cropping simply adjusts the visible boundaries of your pages." }
    ],
    related: ["resize-pdf", "rotate-pdf", "add-watermark-pdf", "number-pdf-pages"]
  },
  "resize-pdf": {
    title: "Resize PDF",
    emoji: "🔲",
    subtitle: "Scale page dimensions to standard sizes like A4 or Letter",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Resize Pages",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Scale layout coordinates to A4, Letter, or custom page sizes directly in your browser.",
    steps: [
      { title: "Select PDF", desc: "Upload target files." },
      { title: "Define Layout", desc: "Choose standard dimensions from the options." },
      { title: "Save PDF", desc: "Retrieve your resized document." }
    ],
    features: [
      { title: "Standard Sizes", desc: "Easily scale pages to standard A4, Letter, or Legal sizes." },
      { title: "Vector Scaling", desc: "Preserves layout text and vector scales cleanly." },
      { title: "Completely Private", desc: "All conversions are processed locally on your machine." },
      { title: "Always Free", desc: "No payment gateways or subscription requirements." }
    ],
    faqs: [
      { q: "Does content auto-fit?", a: "Yes, elements scale proportionally to match new page dimensions." }
    ],
    related: ["crop-pdf", "rotate-pdf", "compress-pdf", "flatten-pdf"]
  },
  "unlock-pdf": {
    title: "Unlock PDF",
    emoji: "🔓",
    subtitle: "Remove restriction passwords from your PDF files",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Unlock PDF",
    outputExt: ".pdf",
    category: "security",
    metaDesc: "Remove editing or viewing passwords from secure PDFs. Processed entirely on your device.",
    steps: [
      { title: "Select PDF", desc: "Upload your locked document." },
      { title: "Input Password", desc: "Provide the correct authorization password." },
      { title: "Download", desc: "Get an unlocked, restriction-free PDF." }
    ],
    features: [
      { title: "Instant Decryption", desc: "Removes restriction structures quickly." },
      { title: "Fidelity Kept", desc: "No content or quality is modified." },
      { title: "Safe & Local", desc: "Password stays in browser memory only." },
      { title: "Free Always", desc: "Process secure files without fees." }
    ],
    faqs: [
      { q: "Do I need to know the password?", a: "Yes, you must provide the password to authorize unlocking." }
    ],
    related: ["protect-pdf", "flatten-pdf", "esign-pdf", "pdf-metadata-editor"]
  },
  "protect-pdf": {
    title: "Protect PDF",
    emoji: "🔒",
    subtitle: "Secure your PDF documents with a user password",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Encrypt PDF",
    outputExt: ".pdf",
    category: "security",
    metaDesc: "Encrypt your PDF documents with secure access passwords directly within your web browser.",
    steps: [
      { title: "Select PDF", desc: "Upload files you wish to protect." },
      { title: "Input Password", desc: "Enter your desired security password." },
      { title: "Save Secure", desc: "Retrieve your newly encrypted PDF." }
    ],
    features: [
      { title: "Secure Encryption", desc: "Applies standard password protection to your files." },
      { title: "Local Safety", desc: "All encryption is performed locally on your device." },
      { title: "Fast Execution", desc: "Encrypts documents in seconds." },
      { title: "No Watermark", desc: "No limitations or brand logos are added." }
    ],
    faqs: [
      { q: "Is the password secure?", a: "Encryption is done directly in browser memory; the password is never sent online." }
    ],
    related: ["unlock-pdf", "add-watermark-pdf", "flatten-pdf", "esign-pdf"]
  },
  "esign-pdf": {
    title: "E-Sign PDF",
    emoji: "✍️",
    subtitle: "Draw and place your digital signature securely onto PDF pages",
    accept: ".pdf",
    multiple: false,
    execBtnText: "E-Sign PDF",
    outputExt: ".pdf",
    category: "security",
    metaDesc: "Draw your signature and embed it onto PDF pages securely with our local, client-side signature pad.",
    steps: [
      { title: "Select PDF", desc: "Upload your target document." },
      { title: "Draw Signature", desc: "Use our visual canvas pad to draw." },
      { title: "Place & Export", desc: "Generate your signed document." }
    ],
    features: [
      { title: "Interactive Canvas", desc: "Draw clear signature paths with ease." },
      { title: "No Signature Uploads", desc: "All signature drawings stay strictly private in the browser." },
      { title: "Fast Processing", desc: "Generates signed documents instantly." },
      { title: "100% Free", desc: "Sign unlimited documents with no brand limits." }
    ],
    faqs: [
      { q: "Where does the signature go?", a: "The signature is embedded cleanly onto the first page of your document." }
    ],
    related: ["protect-pdf", "unlock-pdf", "add-watermark-pdf", "number-pdf-pages"]
  },
  "repair-pdf": {
    title: "Repair PDF",
    emoji: "🛠️",
    subtitle: "Rebuild corrupt document file streams to recover readable data",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Repair PDF",
    outputExt: ".pdf",
    category: "advanced",
    metaDesc: "Fix damaged or corrupt PDF documents and recover readable text streams in your browser.",
    steps: [
      { title: "Select PDF", desc: "Upload corrupt or damaged files." },
      { title: "Rebuild PDF", desc: "Analyze page trees and restructure corrupt elements." },
      { title: "Download", desc: "Retrieve the repaired PDF document." }
    ],
    features: [
      { title: "Data Recovery", desc: "Restores broken structures to extract legible pages." },
      { title: "Fast Analysis", desc: "Scans file headers and reconstructs them instantly." },
      { title: "100% Private", desc: "All recovery is performed locally on your device." },
      { title: "No Watermark", desc: "No limitations or brand markers added." }
    ],
    faqs: [
      { q: "Can all corrupt PDFs be repaired?", a: "It recovers files with readable page matrices, though severe corruption may affect results." }
    ],
    related: ["flatten-pdf", "ocr-pdf", "pdf-metadata-editor", "compress-pdf"]
  },
  "ocr-pdf": {
    title: "OCR PDF",
    emoji: "👁️",
    subtitle: "Recognize text in scanned PDFs and images (English)",
    accept: ".pdf,.jpg,.jpeg,.png,.webp",
    multiple: false,
    execBtnText: "Extract Text (OCR)",
    outputExt: ".txt",
    category: "advanced",
    metaDesc: "Run OCR on scanned PDFs and images right in your browser with Tesseract.js. Your file is processed locally; only the public language model is downloaded.",
    steps: [
      { title: "Upload Scan", desc: "Select a scanned PDF, JPG, PNG or WebP (clear, printed English text works best)." },
      { title: "Run OCR", desc: "Tesseract.js recognizes the text locally in a browser worker." },
      { title: "Save Text", desc: "Download the recognized text as a .txt file." }
    ],
    features: [
      { title: "Local Recognition", desc: "Tesseract.js runs in your browser; the file is never uploaded." },
      { title: "PDF + Images", desc: "Works on whole PDFs (page by page) or single image files." },
      { title: "Honest Limitations", desc: "English, printed text performs best; handwriting and photos are not reliable." },
      { title: "Always Free", desc: "No subscriptions or page limits." }
    ],
    faqs: [
      { q: "Does this require a network connection?", a: "Only for the first run, when Tesseract.js downloads the public English language model (a few MB) from the Tesseract project's CDN. Your document is processed entirely on your device and is never sent anywhere." },
      { q: "How accurate is the output?", a: "Accurate for clear, printed, high-contrast text. Expect errors with small fonts, skew, low-light photos and handwriting — always proofread important results." },
      { q: "Why a .txt file and not a searchable PDF?", a: "Building a fully searchable (text-overlay) PDF reliably in the browser is not something we can guarantee, so we give you clean extracted text you can paste anywhere. That is the honest output." }
    ],
    related: ["pdf-to-text", "pdf-metadata-editor", "pdf-to-word", "pdf-to-epub"]
  },
  "compare-pdf": {
    title: "Compare PDFs",
    emoji: "⚖️",
    subtitle: "Diff the text of two PDF versions and download an HTML report",
    accept: ".pdf",
    multiple: true,
    execBtnText: "Compare Documents",
    outputExt: ".html",
    category: "advanced",
    metaDesc: "Compare two PDF versions in your browser: text is extracted line by line and additions/removals are highlighted in an HTML report. Private, free, no upload.",
    steps: [
      { title: "Select Two PDFs", desc: "Add Document A and Document B (exactly two files)." },
      { title: "Run Compare", desc: "Text is extracted and diffed line by line." },
      { title: "Download Report", desc: "Open the HTML report with highlighted changes." }
    ],
    features: [
      { title: "Line-Level Diff", desc: "Added and removed lines are clearly marked." },
      { title: "Summary Counts", desc: "Instant count of what changed between versions." },
      { title: "Private Processing", desc: "Both files stay on your device." },
      { title: "Free & Unlimited", desc: "Compare as often as you need." }
    ],
    faqs: [
      { q: "How are files compared?", a: "Visible text is extracted from each PDF and diffed line by line. Scanned pages without a text layer won't be compared — run OCR first if that applies." },
      { q: "What does the report look like?", a: "A standalone HTML file: green lines are additions in Document B, red lines are removals from Document A, and a summary counts the changes." }
    ],
    related: ["pdf-to-text", "pdf-metadata-editor", "flatten-pdf", "repair-pdf"]
  },
  "pdf-metadata-editor": {
    title: "PDF Metadata Editor",
    emoji: "🏷️",
    subtitle: "Adjust document title, author, and keyword parameters",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Update Metadata",
    outputExt: ".pdf",
    category: "advanced",
    metaDesc: "Edit PDF properties like Title, Author, Subject, and Keywords directly in your browser.",
    steps: [
      { title: "Upload PDF", desc: "Select files to modify." },
      { title: "Set Metadata", desc: "Edit Title, Author, and Keywords in the panel." },
      { title: "Save PDF", desc: "Retrieve updated document files instantly." }
    ],
    features: [
      { title: "Complete Control", desc: "Easily modify Title, Author, Subject, and Keywords." },
      { title: "No Server Uploads", desc: "All adjustments are processed on your local device." },
      { title: "Fidelity Preserved", desc: "Updates only the metadata properties, keeping pages unchanged." },
      { title: "Always Free", desc: "No licenses or limitations on modifications." }
    ],
    faqs: [
      { q: "What fields can I edit?", a: "You can modify standard fields including Title, Author, Subject, and Keywords." }
    ],
    related: ["pdf-to-pdfa", "flatten-pdf", "protect-pdf", "add-watermark-pdf"]
  },
  "flatten-pdf": {
    title: "Flatten PDF",
    emoji: "🥞",
    subtitle: "Merge form fields, layers, and annotations down to a single surface",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Flatten PDF",
    outputExt: ".pdf",
    category: "advanced",
    metaDesc: "Flatten interactive fields, layers, and annotations into static PDF pages instantly in your browser.",
    steps: [
      { title: "Upload PDF", desc: "Select forms or layered documents." },
      { title: "Flatten Elements", desc: "Merge forms and layers into a single static page surface." },
      { title: "Download PDF", desc: "Retrieve your flattened, read-only document." }
    ],
    features: [
      { title: "Lock Form Fields", desc: "Converts fillable fields into static text to prevent changes." },
      { title: "100% Private", desc: "All rendering is performed locally on your device." },
      { title: "Wide Compatibility", desc: "Ensures pages render consistently on all readers." },
      { title: "Free Always", desc: "Flatten unlimited documents with no limitations." }
    ],
    faqs: [
      { q: "Can flattened forms be edited?", a: "No, flattening merges inputs into static vector shapes to prevent editing." }
    ],
    related: ["pdf-metadata-editor", "compress-pdf", "protect-pdf", "add-watermark-pdf"]
  },
  "grayscale-pdf": {
    title: "Grayscale PDF",
    emoji: "🎨",
    subtitle: "Convert all page colors and image layers to black & white",
    accept: ".pdf",
    multiple: false,
    execBtnText: "Convert to Grayscale",
    outputExt: ".pdf",
    category: "edit",
    metaDesc: "Convert PDF colors and images to black and white inside your browser to save printing ink.",
    steps: [
      { title: "Upload PDF", desc: "Select files to convert." },
      { title: "Render Pages", desc: "Process and map vector colors to grayscale values." },
      { title: "Download PDF", desc: "Retrieve your black & white document." }
    ],
    features: [
      { title: "Save Printer Ink", desc: "Ideal for drafts, reports, and monochrome printing." },
      { title: "Instant Conversion", desc: "Converts pages in memory using browser resources." },
      { title: "Secure Processing", desc: "All files remain safely on your local device." },
      { title: "Fully Free", desc: "No watermarks or subscription limitations." }
    ],
    faqs: [
      { q: "Are text properties kept?", a: "Yes, text is preserved while all colors and images convert to grayscale." }
    ],
    related: ["compress-pdf", "flatten-pdf", "rotate-pdf", "add-watermark-pdf"]
  }
};

const HOMEPAGE_FAQS = [
  { q: "Is PDFZaap really free?", a: "Yes. All 35 tools are free with no account, no subscription and no paid tier." },
  { q: "Are my files uploaded to a server?", a: "No. Every tool runs in your browser using client-side WebAssembly and JavaScript libraries." },
  { q: "How do I merge PDF files?", a: "Open the Merge PDF tool, upload your PDF documents, arrange them in order, and click Merge." },
  { q: "How do I split a PDF?", a: "Use the Split PDF tool to extract specific pages or page ranges into a new document." },
  { q: "How do I compress a PDF?", a: "Upload your PDF to the Compress PDF tool and reduce its size while keeping clear formatting." },
  { q: "How do I convert PDF to Word?", a: "Use the PDF to Word converter to extract text into an editable .docx file." },
  { q: "Can I use PDFZaap without creating an account?", a: "Yes. PDFZaap works instantly with no signup or registration required." }
];

// ==========================================================================
// GLOBAL STATE VARIABLES
// ==========================================================================

let uploadedFileArray = [];
let activeTool = null;
let fabricCanvas = null;
let processingController = null;
let activeDownloadURL = null;
let processingClientPromise;
const progressUI = { timer: null, pending: null, lastTime: -Infinity, percent: null, text: null };

function getProcessingClient() {
  if (!processingClientPromise) {
    processingClientPromise = import('./processing-client.js').catch(error => {
      processingClientPromise = null;
      throw error;
    });
  }
  return processingClientPromise;
}

// ==========================================================================
// PRIVACY-FRIENDLY ANALYTICS HOOK
// ==========================================================================
const ZAAP_ANALYTICS = {
  ga4Id: null,
  plausible: null
};

function zaapTrack(event, props) {
  const payload = Object.assign({ event: event, tool: activeTool || 'home', ts: Date.now() }, props || {});
  window.__zaapEvents = window.__zaapEvents || [];
  window.__zaapEvents.push(payload);
  try {
    window.dispatchEvent(new CustomEvent('zaap:track', { detail: payload }));
  } catch (e) { /* no-op */ }
}

// ==========================================================================
// APPLICATION INITIALIZATION
// ==========================================================================

window.addEventListener('DOMContentLoaded', () => {
  setupNavbarScroll();
  setupMobileHamburger();
  setupSearchAndFilters();
  setupDropzone();
  initCookieBanner();
  
  const toolPage = document.querySelector('main[data-tool]');
  if (toolPage) {
    activeTool = toolPage.getAttribute('data-tool');
    if (typeof setupOptionsPanel === 'function') setupOptionsPanel(activeTool);
    zaapTrack('tool_open', { tool: activeTool });
  }
});

// ==========================================================================
// WORKSPACE OPTIONS PANEL FORM GENERATOR
// ==========================================================================

function setupOptionsPanel(toolId) {
  const panel = document.getElementById('ws-options-panel');
  const canvasWrapper = document.getElementById('ws-canvas-wrapper');
  
  if (!panel) return;
  panel.innerHTML = '';
  panel.classList.add('display-none');
  canvasWrapper?.classList.add('display-none');

  if (toolId === 'compress-pdf') {
    panel.innerHTML = `
      <h4>Compression Adjustments</h4>
      <div class="option-row">
        <label for="compress-target">Target size (optional)</label>
        <select id="compress-target" class="option-field" aria-label="Target compressed file size">
          <option value="0">Manual — choose quality below</option>
          <option value="100">Under 100 KB</option>
          <option value="200">Under 200 KB</option>
          <option value="500">Under 500 KB</option>
          <option value="1024">Under 1 MB</option>
          <option value="2048">Under 2 MB</option>
        </select>
        <p class="subtext-muted margin-top-1">In target mode the tool finds the best quality that fits the limit, and tells you honestly if the limit cannot be reached.</p>
      </div>
      <div class="option-row">
        <label for="compress-slider">Image Quality (0.1 to 1.0) — used in manual mode</label>
        <input type="range" id="compress-slider" class="option-field" min="0.1" max="1.0" step="0.1" value="0.6" aria-label="Image Quality Slider">
        <p id="compress-val-label" class="subtext-muted margin-top-1">Value: 0.6</p>
      </div>
    `;
    panel.classList.remove('display-none');
    document.getElementById('compress-slider').addEventListener('input', (e) => {
      document.getElementById('compress-val-label').textContent = `Value: ${e.target.value}`;
    });
  }
  else if (toolId === 'jpg-to-pdf' || toolId === 'png-to-pdf') {
    panel.innerHTML = `
      <h4>Page Layout</h4>
      <div class="option-row">
        <label for="img-page-size">Page size</label>
        <select id="img-page-size" class="option-field" aria-label="Select image page size">
          <option value="fit">Fit page to each image</option>
          <option value="a4">A4 (210 × 297 mm) — image centered</option>
          <option value="letter">US Letter (8.5 × 11 in) — image centered</option>
        </select>
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'split-pdf') {
    panel.innerHTML = `
      <h4>Splitting Ranges</h4>
      <div class="option-row">
        <label for="split-pages-input">Page Range (e.g. 1-3, 5, 7-9)</label>
        <input type="text" id="split-pages-input" class="option-field" placeholder="e.g. 1-2, 4" aria-label="Page range input">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'rotate-pdf') {
    panel.innerHTML = `
      <h4>Rotation Degrees</h4>
      <div class="option-row">
        <label for="rotate-select">Rotation Angle</label>
        <select id="rotate-select" class="option-field" aria-label="Rotation angle selection">
          <option value="90">90° Clockwise</option>
          <option value="180">180° Flip</option>
          <option value="270">270° Counter-Clockwise</option>
        </select>
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'add-watermark-pdf') {
    panel.innerHTML = `
      <h4>Watermark Parameters</h4>
      <div class="option-row">
        <label for="watermark-text">Watermark Text</label>
        <input type="text" id="watermark-text" class="option-field" value="CONFIDENTIAL" aria-label="Watermark text input">
      </div>
      <div class="option-row">
        <label for="watermark-opacity">Opacity (0.1 to 1.0)</label>
        <input type="number" id="watermark-opacity" class="option-field" min="0.1" max="1.0" step="0.1" value="0.4" aria-label="Watermark opacity input">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'number-pdf-pages') {
    panel.innerHTML = `
      <h4>Position Parameters</h4>
      <div class="option-row">
        <label for="pagenum-pos">Select Placement Alignment</label>
        <select id="pagenum-pos" class="option-field" aria-label="Page number position selection">
          <option value="bottom-center">Bottom Center</option>
          <option value="bottom-right">Bottom Right</option>
        </select>
      </div>
      <div class="option-row">
        <label for="pagenum-size">Font Size (px)</label>
        <input type="number" id="pagenum-size" class="option-field" value="12" min="8" max="24" aria-label="Page number font size">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'protect-pdf') {
    panel.innerHTML = `
      <h4>Lock Configuration</h4>
      <div class="option-row">
        <label for="protect-pass">Secure Access Password</label>
        <input type="password" id="protect-pass" class="option-field" placeholder="Enter secure password" aria-label="Secure access password">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'esign-pdf') {
    canvasWrapper?.classList.remove('display-none');
    initFabricCanvas();
  }
  else if (toolId === 'delete-pdf-pages' || toolId === 'extract-pages-pdf') {
    panel.innerHTML = `
      <h4>Page Selection</h4>
      <div class="option-row">
        <label for="pages-range-input">Pages (e.g. 1-3, 5, 8-10)</label>
        <input type="text" id="pages-range-input" class="option-field" placeholder="e.g. 1-3, 5" aria-label="Page selection range">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'reorder-pages-pdf') {
    panel.innerHTML = `
      <h4>New Page Order</h4>
      <div class="option-row">
        <label for="pages-order-input">New order using every page exactly once (e.g. 3,1,2)</label>
        <input type="text" id="pages-order-input" class="option-field" placeholder="e.g. 3,1,2" aria-label="New page order input">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'crop-pdf') {
    panel.innerHTML = `
      <h4>Crop Margins (%)</h4>
      <div class="option-row">
        <label for="crop-left">Left %</label>
        <input type="number" id="crop-left" class="option-field" value="5" min="0" max="45" aria-label="Crop left margin percentage">
      </div>
      <div class="option-row">
        <label for="crop-right">Right %</label>
        <input type="number" id="crop-right" class="option-field" value="5" min="0" max="45" aria-label="Crop right margin percentage">
      </div>
      <div class="option-row">
        <label for="crop-top">Top %</label>
        <input type="number" id="crop-top" class="option-field" value="5" min="0" max="45" aria-label="Crop top margin percentage">
      </div>
      <div class="option-row">
        <label for="crop-bottom">Bottom %</label>
        <input type="number" id="crop-bottom" class="option-field" value="5" min="0" max="45" aria-label="Crop bottom margin percentage">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'resize-pdf') {
    panel.innerHTML = `
      <h4>Target Page Size</h4>
      <div class="option-row">
        <label for="resize-size">Page Format</label>
        <select id="resize-size" class="option-field" aria-label="Target page size format">
          <option value="a4">A4 (210 &times; 297 mm)</option>
          <option value="letter">US Letter (8.5 &times; 11 in)</option>
        </select>
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'pdf-metadata-editor') {
    panel.innerHTML = `
      <h4>Document Metadata</h4>
      <div class="option-row">
        <label for="meta-title">Title</label>
        <input type="text" id="meta-title" class="option-field" placeholder="Document title" aria-label="Document title">
      </div>
      <div class="option-row">
        <label for="meta-author">Author</label>
        <input type="text" id="meta-author" class="option-field" placeholder="Author name" aria-label="Author name">
      </div>
      <div class="option-row">
        <label for="meta-subject">Subject</label>
        <input type="text" id="meta-subject" class="option-field" placeholder="Subject" aria-label="Document subject">
      </div>
      <div class="option-row">
        <label for="meta-keywords">Keywords</label>
        <input type="text" id="meta-keywords" class="option-field" placeholder="keyword1, keyword2" aria-label="Document keywords">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'unlock-pdf') {
    panel.innerHTML = `
      <h4>Protection Removal</h4>
      <div class="option-row">
        <label for="unlock-pass">Password (leave empty for restriction-only protection)</label>
        <input type="password" id="unlock-pass" class="option-field" placeholder="Optional password" aria-label="Unlock password">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else {
    panel.innerHTML = '<h4>Processing information</h4>';
    panel.classList.remove('display-none');
  }

  const limitNote = document.createElement('p');
  limitNote.className = 'subtext-muted margin-top-1';
  panel.appendChild(limitNote);
  getProcessingClient().then(({ LIMITS, supportsTool }) => {
    if (!supportsTool(toolId)) {
      limitNote.textContent = 'This tool is not implemented yet.';
      return;
    }
    const raster = ['compress-pdf', 'grayscale-pdf', 'pdf-to-jpg', 'pdf-to-png', 'pdf-to-powerpoint', 'ocr-pdf'].includes(toolId);
    if (toolId === 'word-to-pdf') {
      limitNote.textContent = `Up to ${LIMITS.maxWordFileBytes / 1048576} MB. Very long documents must be split to fit browser canvas limits.`;
    } else {
      limitNote.textContent = `Up to ${LIMITS.maxFileBytes / 1048576} MB per file and ${raster ? LIMITS.maxRasterPages : LIMITS.maxPages} pages.`;
    }
  }).catch(() => { limitNote.textContent = 'Engine ready.'; });
}

function initFabricCanvas() {
  if (typeof fabric === 'undefined') return;
  if (fabricCanvas) fabricCanvas.dispose();
  fabricCanvas = new fabric.Canvas('esign-fabric-canvas', { isDrawingMode: true });
  fabricCanvas.freeDrawingBrush.width = 3;
  fabricCanvas.freeDrawingBrush.color = '#C73E00';
}

function clearSignatureCanvas() {
  if (fabricCanvas) fabricCanvas.clear();
}

// ==========================================================================
// FILE HANDLERS & UPLOAD DRAG/DROP
// ==========================================================================

function setupDropzone() {
  const wsDropzone = document.getElementById('ws-dropzone');
  const wsFileInput = document.getElementById('ws-file-input');

  if (!wsDropzone || !wsFileInput) return;

  wsDropzone.addEventListener('click', () => wsFileInput.click());
  
  // Keyboard activation (Enter / Space) for Accessibility 100
  wsDropzone.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      wsFileInput.click();
    }
  });

  wsDropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    wsDropzone.classList.add('dragover');
  });

  wsDropzone.addEventListener('dragleave', () => wsDropzone.classList.remove('dragover'));
  
  wsDropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    wsDropzone.classList.remove('dragover');
    handleUploadedFiles(e.dataTransfer.files);
  });

  wsFileInput.addEventListener('change', (e) => {
    handleUploadedFiles(e.target.files);
  });
}

async function handleUploadedFiles(files) {
  if (processingController || !files.length || !activeTool) return;
  const tool = activeTool;
  const incoming = Array.from(files);
  try {
    const { validateFiles } = await getProcessingClient();
    if (processingController || tool !== activeTool) return;
    const isMultiple = TOOL_DATABASE[tool] ? TOOL_DATABASE[tool].multiple : false;
    const nextFiles = isMultiple ? [...uploadedFileArray, ...incoming] : [incoming[0]];
    validateFiles(nextFiles, tool);
    uploadedFileArray = nextFiles;
    zaapTrack('file_selected', { files: incoming.length });
    renderWorkspaceFileList();
  } catch (error) {
    document.getElementById('ws-progress-container').style.display = 'block';
    setProgressUI(0, `Error: ${error.message}`, true);
  }
}

function renderWorkspaceFileList() {
  const listElement = document.getElementById('ws-file-list');
  if (!listElement) return;
  listElement.innerHTML = '';
  
  uploadedFileArray.forEach((file, index) => {
    if (!file) return;
    const icon = setFileIconByExtension(file.name);
    listElement.innerHTML += `
      <div class="file-row">
        <div class="file-row-info">
          <span>${icon}</span>
          <span>${file.name} (${(file.size / 1024).toFixed(1)} KB)</span>
        </div>
        <button type="button" class="file-row-remove" onclick="removeWorkspaceFile(${index})" aria-label="Remove ${file.name}">Remove</button>
      </div>
    `;
  });

  const hasFiles = uploadedFileArray.filter(f => f).length > 0;
  const btn = document.getElementById('ws-process-btn');
  if (btn) btn.disabled = !hasFiles || !!processingController;
}

function removeWorkspaceFile(index) {
  if (processingController) return;
  uploadedFileArray.splice(index, 1);
  renderWorkspaceFileList();
}

function setFileIconByExtension(fileName) {
  const ext = fileName.split('.').pop().toLowerCase();
  if (ext === 'pdf') return '📄';
  if (['jpg', 'jpeg', 'png'].includes(ext)) return '🖼️';
  if (ext === 'docx') return '📝';
  return '📁';
}

function clearWorkspaceFile() {
  cancelWorkspaceProcessing();
  releaseDownloadURL();
  resetProgressUI();
  uploadedFileArray = [];
  const input = document.getElementById('ws-file-input');
  if (input) input.value = '';
  
  const list = document.getElementById('ws-file-list');
  if (list) list.innerHTML = '';
  const btn = document.getElementById('ws-process-btn');
  if (btn) btn.disabled = true;
  const prog = document.getElementById('ws-progress-container');
  if (prog) prog.style.display = 'none';
  const out = document.getElementById('ws-output-box');
  if (out) { out.style.display = 'none'; out.innerHTML = ''; }
}

// ==========================================================================
// WORKSPACE EXECUTION & PDF ENGINES
// ==========================================================================

function readProcessingOptions(tool) {
  const value = id => document.getElementById(id)?.value || '';
  switch (tool) {
    case 'split-pdf': return { range: value('split-pages-input') };
    case 'extract-pages-pdf':
    case 'delete-pdf-pages': return { range: value('pages-range-input') };
    case 'reorder-pages-pdf': return { order: value('pages-order-input') };
    case 'compress-pdf': return { quality: value('compress-slider'), targetKB: Number(value('compress-target')) || 0 };
    case 'jpg-to-pdf':
    case 'png-to-pdf': return { pageSize: value('img-page-size') };
    case 'rotate-pdf': return { angle: value('rotate-select') };
    case 'add-watermark-pdf': return { text: value('watermark-text'), opacity: value('watermark-opacity') };
    case 'number-pdf-pages': return { position: value('pagenum-pos'), fontSize: value('pagenum-size') };
    case 'resize-pdf': return { format: value('resize-size') };
    case 'crop-pdf': return { left: value('crop-left'), right: value('crop-right'), top: value('crop-top'), bottom: value('crop-bottom') };
    case 'pdf-metadata-editor': return { title: value('meta-title').trim(), author: value('meta-author').trim(), subject: value('meta-subject').trim(), keywords: value('meta-keywords').trim() };
    default: return {};
  }
}

function setWorkspaceBusy(busy) {
  const processButton = document.getElementById('ws-process-btn');
  if (processButton) processButton.disabled = busy || !uploadedFileArray.some(Boolean);
  const fileInput = document.getElementById('ws-file-input');
  if (fileInput) fileInput.disabled = busy;
  document.querySelectorAll('#ws-options-panel input, #ws-options-panel select').forEach(field => { field.disabled = busy; });
  const cancelButton = document.getElementById('ws-cancel-btn');
  if (cancelButton) cancelButton.style.display = busy ? 'inline-block' : 'none';
}

function cancelWorkspaceProcessing() {
  processingController?.abort();
  processingController = null;
  setWorkspaceBusy(false);
}

document.getElementById('ws-process-btn')?.addEventListener('click', async () => {
  const files = uploadedFileArray.filter(Boolean);
  if (!files.length || processingController) return;
  const tool = activeTool;
  zaapTrack('process_click', { tool, files: files.length });
  const options = readProcessingOptions(tool);
  const controller = new AbortController();
  processingController = controller;
  const progressContainer = document.getElementById('ws-progress-container');
  if (progressContainer) progressContainer.style.display = 'block';
  const progressBar = document.getElementById('ws-progress-bar');
  if (progressBar) progressBar.style.backgroundColor = '';
  const outputBox = document.getElementById('ws-output-box');
  if (outputBox) { outputBox.style.display = 'none'; outputBox.replaceChildren(); }
  
  releaseDownloadURL();
  resetProgressUI();
  setProgressUI(0, 'Initializing engine...', true);
  
  let cancelButton = document.getElementById('ws-cancel-btn');
  if (!cancelButton && progressContainer) {
    cancelButton = document.createElement('button');
    cancelButton.id = 'ws-cancel-btn';
    cancelButton.className = 'btn btn-secondary btn-sm';
    cancelButton.textContent = 'Cancel processing';
    cancelButton.type = 'button';
    cancelButton.addEventListener('click', () => processingController?.abort());
    progressContainer.appendChild(cancelButton);
  }
  setWorkspaceBusy(true);
  try {
    const { runTool, canvasToBlob } = await getProcessingClient();
    if (controller.signal.aborted) throw new DOMException('Processing cancelled.', 'AbortError');
    if (tool === 'esign-pdf') {
      if (!fabricCanvas) throw new Error('Signature canvas is not initialized.');
      const signatureCanvas = fabricCanvas.toCanvasElement();
      try { options.signature = await (await canvasToBlob(signatureCanvas, 'image/png')).arrayBuffer(); }
      finally { signatureCanvas.width = signatureCanvas.height = 0; }
    }
    const result = await runTool(tool, files, options, {
      signal: controller.signal,
      onProgress: (percent, text) => {
        if (processingController === controller && !controller.signal.aborted) setProgressUI(percent, text);
      }
    });
    if (processingController !== controller || controller.signal.aborted) return;
    setProgressUI(100, 'Processing completed!', true);
    createDownloadLink(result.data, result.filename, result.type, result.note);
  } catch (error) {
    if (processingController !== controller) return;
    if (controller.signal.aborted) setProgressUI(0, 'Processing cancelled. No output was saved.', true);
    else {
      setProgressUI(0, `Error: ${error.message}`, true);
      if (progressBar) progressBar.style.backgroundColor = '#DC2626';
    }
  } finally {
    if (processingController === controller) {
      processingController = null;
      setWorkspaceBusy(false);
    }
  }
});

function releaseDownloadURL() {
  if (activeDownloadURL) URL.revokeObjectURL(activeDownloadURL);
  activeDownloadURL = null;
}

function createDownloadLink(data, filename, type, note) {
  releaseDownloadURL();
  const blob = data instanceof Blob ? data : new Blob([data], { type });
  activeDownloadURL = URL.createObjectURL(blob);
  const container = document.getElementById('ws-output-box');
  if (!container) return;
  container.innerHTML = `
    <div class="download-box">
      <h4>🎉 Document Processed Successfully!</h4>
      <p>Your document is ready to download.</p>
      <a id="direct-dl-link" class="btn btn-primary" href="#">Download file</a>
    </div>
  `;
  const link = document.getElementById('direct-dl-link');
  link.href = activeDownloadURL;
  link.download = filename;
  link.textContent = `Download ${filename.split('.').pop().toUpperCase()}`;
  if (note) {
    const message = document.createElement('p');
    message.className = 'output-note';
    message.textContent = note;
    link.before(message);
  }
  container.style.display = 'block';
  link.addEventListener('click', () => zaapTrack('download_click', { tool: activeTool, ext: (type || '').split('/')[1] || '' }));
  link.click();
}

function resetProgressUI() {
  clearTimeout(progressUI.timer);
  Object.assign(progressUI, { timer: null, pending: null, lastTime: -Infinity, percent: null, text: null });
}

function flushProgressUI() {
  clearTimeout(progressUI.timer);
  progressUI.timer = null;
  if (!progressUI.pending) return;
  const { percent, text } = progressUI.pending;
  progressUI.pending = null;
  const bar = document.getElementById('ws-progress-bar');
  const status = document.getElementById('ws-progress-status');
  if (bar && progressUI.percent !== percent) bar.style.width = `${percent}%`;
  if (status && progressUI.text !== text) status.textContent = text;
  Object.assign(progressUI, { percent, text, lastTime: performance.now() });
}

function setProgressUI(percent, text, force = false) {
  percent = Math.max(0, Math.min(100, Math.round(percent)));
  progressUI.pending = { percent, text };
  const elapsed = performance.now() - progressUI.lastTime;
  if (force || percent === 100 || elapsed >= 100) flushProgressUI();
  else if (!progressUI.timer) progressUI.timer = setTimeout(flushProgressUI, 100 - elapsed);
}

window.addEventListener('pagehide', () => {
  cancelWorkspaceProcessing();
  releaseDownloadURL();
  resetProgressUI();
  const output = document.getElementById('ws-output-box');
  if (output) { output.replaceChildren(); output.style.display = 'none'; }
  const progress = document.getElementById('ws-progress-container');
  if (progress) progress.style.display = 'none';
});

// ==========================================================================
// INTERACTIVE UI & NAVIGATION HELPERS
// ==========================================================================

function toggleAccordion(trigger) {
  const parent = trigger.parentElement;
  if (parent) {
    parent.classList.toggle('active');
  }
}

function setupNavbarScroll() {
  const nav = document.getElementById('main-nav');
  const scrollTopBtn = document.getElementById('scroll-top');
  
  // Passive scroll listener for smooth 60fps performance and high Lighthouse score
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav?.classList.add('scrolled');
    } else {
      nav?.classList.remove('scrolled');
    }

    if (window.scrollY > 400) {
      scrollTopBtn?.classList.add('visible');
    } else {
      scrollTopBtn?.classList.remove('visible');
    }
  }, { passive: true });
}

function setupMobileHamburger() {
  const btn = document.getElementById('hamburger-btn');
  const menu = document.getElementById('mobile-menu');

  if (!btn || !menu) return;

  function setMenu(open) {
    btn.classList.toggle('active', open);
    menu.classList.toggle('active', open);
    document.body.classList.toggle('no-scroll', open);
    btn.setAttribute('aria-expanded', String(open));
  }

  btn.addEventListener('click', () => {
    setMenu(!menu.classList.contains('active'));
  });

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setMenu(false));
  });

  menu.addEventListener('click', (e) => {
    if (e.target === menu) setMenu(false);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setMenu(false);
  });
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function scrollToToolsGrid() {
  const target = document.getElementById('tools-anchor');
  if (target) target.scrollIntoView({ behavior: 'smooth' });
}

function setupSearchAndFilters() {
  const input = document.getElementById('tool-search');
  if (input) {
    input.addEventListener('input', runSearchFilter);
  }
}

function runSearchFilter() {
  const queryInput = document.getElementById('tool-search');
  if (!queryInput) return;
  const query = queryInput.value.toLowerCase().trim();
  const activeBtn = document.querySelector('.filter-tab.active');
  const activeTab = activeBtn
    ? (activeBtn.getAttribute('data-tab') || activeBtn.textContent.toLowerCase())
    : 'all';
  const cards = document.querySelectorAll('#main-tools-grid .tool-card');

  cards.forEach(card => {
    const titleEl = card.querySelector('h3');
    const descEl = card.querySelector('p');
    const title = titleEl ? titleEl.textContent.toLowerCase() : '';
    const desc = descEl ? descEl.textContent.toLowerCase() : '';
    const category = card.getAttribute('data-category');

    const matchQuery = !query || title.includes(query) || desc.includes(query);
    const matchTab = (activeTab === 'all' || category === activeTab);

    if (matchQuery && matchTab) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });

  document.querySelectorAll('#main-tools-grid .tools-group').forEach(group => {
    const anyVisible = Array.from(group.querySelectorAll('.tool-card')).some(c => c.style.display !== 'none');
    group.style.display = anyVisible ? '' : 'none';
  });
}

function applyFilterTab(tabCategory, btnElement) {
  document.querySelectorAll('#filter-tabs-container .filter-tab').forEach(t => t.classList.remove('active'));
  btnElement.classList.add('active');
  runSearchFilter();
}

function initCookieBanner() {
  const consent = localStorage.getItem('cookie-consent-pdfzaap');
  if (!consent) {
    const banner = document.getElementById('cookie-banner');
    if (banner) banner.style.display = 'flex';
  }
}

function acceptCookies(state) {
  localStorage.setItem('cookie-consent-pdfzaap', state ? 'accept' : 'decline');
  const banner = document.getElementById('cookie-banner');
  if (banner) banner.style.display = 'none';
}

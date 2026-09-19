// ==========================================================================
// DATA CONFIGURATION & DATABASES
// ==========================================================================

// Configure the pdf.js worker to match the loaded library version (required for reliable rendering)
if (typeof pdfjsLib !== 'undefined' && pdfjsLib.GlobalWorkerOptions) {
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/' + pdfjsLib.version + '/pdf.worker.min.js';
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
    {
        q: "What is a PDF?",
        a: "A PDF (Portable Document Format) is a file format developed to preserve document formatting across all devices and operating systems."
    },
    {
        q: "What does PDF stand for?",
        a: "PDF stands for Portable Document Format. It allows documents to keep the same layout, fonts, and images regardless of the device used."
    },
    {
        q: "How do I merge PDF files?",
        a: "Open the Merge PDF tool, upload your PDF documents, arrange them in the correct order, and download the merged file in seconds."
    },
    {
        q: "How do I split a PDF?",
        a: "Use the Split PDF tool to extract specific pages or divide a PDF into multiple smaller documents quickly and securely."
    },
    {
        q: "How do I compress a PDF?",
        a: "Upload your PDF to the Compress PDF tool and reduce its file size while maintaining the best possible quality."
    },
    {
        q: "How do I convert PDF to Word?",
        a: "Use the PDF to Word converter to transform PDF documents into editable Word files while preserving formatting whenever possible."
    },
    {
        q: "Can I use PDFZaap without creating an account?",
        a: "Yes. PDFZaap works instantly in your browser with no signup, no registration, and no software installation required."
    }
];
const BLOG_POSTS = {

  "what-is-a-pdf": {
    title: "What Is a PDF? Meaning, Format & Uses Explained (2026)",
    category: "PDF Basics",
    date: "August 01, 2026",
    iso: "2026-08-01",
    readTime: "6 min read",
    excerpt: "Wondering what a PDF is? Learn what PDF stands for...",
    content: `
      <div class="quick-answer-box">
        <strong>Quick Answer:</strong> A PDF (Portable Document Format) is a file format developed by Adobe that preserves the layout, fonts, images, and formatting of a document across different devices.
      </div>

      <h1>What Is a PDF? A Simple Guide to the Portable Document Format</h1>

      <p>PDF (Portable Document Format) is one of the world's most widely used file formats...</p>
    `
  },

  "free-pdf-tools-online": {
    title: "Free PDF Tools Online — Convert, Compress, Merge & Edit PDFs | PDFZaap",
    category: "Reviews",
    date: "June 14, 2026",
    iso: "2026-06-14",
    readTime: "4 min read",
    excerpt: "Looking for free PDF tools online?",
    content: `
      <p>Finding secure and reliable free PDF tools online...</p>
    `
  },

  "how-to-save-google-doc-as-pdf": {
    title: "How to Save a Google Doc as a PDF",
    category: "Tutorial",
    date: "June 12, 2026",
    iso: "2026-06-12",
    readTime: "5 min read",
    excerpt: "Learn how to save a google doc as a pdf.",
    content: `
      <p>Whether you need to submit a resume...</p>
    `
  }

};

// ==========================================================================
// GLOBAL STATE VARIABLES
// ==========================================================================

let uploadedFileArray = [];
let activeTool = null;
let fabricCanvas = null;

// ==========================================================================
// PRIVACY-FRIENDLY ANALYTICS HOOK
// Events: tool_open, file_selected, process_click, download_click.
// No file names, contents, or personal data are ever included.
// To enable a real provider, set ga4Id or plausible below (see SEO-CHANGELOG.md).
// ==========================================================================
const ZAAP_ANALYTICS = {
  ga4Id: null,        // e.g. 'G-XXXXXXX' once the owner adds a GA4 property
  plausible: null     // e.g. 'https://analytics.pdfzaap.online' once Plausible is installed
};

function zaapTrack(event, props) {
  const payload = Object.assign({ event: event, tool: activeTool || 'home', ts: Date.now() }, props || {});
  window.__zaapEvents = window.__zaapEvents || [];
  window.__zaapEvents.push(payload);
  try {
    window.dispatchEvent(new CustomEvent('zaap:track', { detail: payload }));
  } catch (e) { /* no-op */ }
  if (ZAAP_ANALYTICS.ga4Id && typeof gtag === 'function') {
    gtag('event', event, props || {});
  } else if (ZAAP_ANALYTICS.plausible && window.plausible) {
    window.plausible(event, props || {});
  }
}

function loadAnalyticsVendor() {
  if (ZAAP_ANALYTICS.ga4Id) {
    const s = document.createElement('script');
    s.async = true;
    s.src = `https://www.googletagmanager.com/gtag/js?id=${ZAAP_ANALYTICS.ga4Id}`;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ZAAP_ANALYTICS.ga4Id, { anonymize_ip: true });
  } else if (ZAAP_ANALYTICS.plausible) {
    const s = document.createElement('script');
    s.defer = true;
    s.src = ZAAP_ANALYTICS.plausible + '/script.js';
    document.head.appendChild(s);
  }
}

// ==========================================================================
// APPLICATION INITIALIZATION & LISTENERS
// ==========================================================================

window.addEventListener('DOMContentLoaded', () => {
  loadAnalyticsVendor();
  buildToolsGrid();
  buildHomepageFAQs();
  buildBlogList();
  setupNavbarScroll();
  setupMobileHamburger();
  setupSearchAndFilters();
  setupDropzone();
  initCookieBanner();
  router();
  // Tool pages declare their tool on <main data-tool="...">; their inline
  // script performs the options-panel setup. We only track the pageview.
  const toolPage = document.querySelector('main[data-tool]');
  if (toolPage && activeTool === toolPage.getAttribute('data-tool')) {
    zaapTrack('tool_open', { tool: activeTool });
  } else if (toolPage) {
    activeTool = toolPage.getAttribute('data-tool');
    if (typeof setupOptionsPanel === 'function') setupOptionsPanel(activeTool);
    zaapTrack('tool_open', { tool: activeTool });
  }
});

// ==========================================================================
// ROUTER & VIEW MANAGEMENT
// ==========================================================================

function oldRouter() {
  // Legacy support only: the homepage is now fully static and every tool and
  // blog post has its own .html URL. If an old hash URL arrives (e.g.
  // index.html#merge-pdf or index.html#blog/some-post), send the visitor to
  // the real page instead of a JS view.
  const hash = window.location.hash.substring(1);
  if (!hash || hash.indexOf('#') === 0) return; // plain anchor (scroll) — nothing to do
  if (TOOL_DATABASE[hash]) {
    window.location.replace(hash + '.html');
    return;
  }
  if (hash === 'blog' || hash === 'blog/' || hash === '') {
    window.location.replace('blog/');
    return;
  }
  if (hash.startsWith('blog/')) {
    window.location.replace('blog/' + hash.substring(5) + '.html');
    return;
  }
  // Unknown hash — leave the page as-is.
}

function router() {
  // Applies to the homepage document only; standalone pages return early.
  if (!document.getElementById('homepage-dashboard')) return;
  oldRouter();
}

window.addEventListener('hashchange', router);

function showDashboard() {
  document.getElementById('homepage-dashboard').classList.add('active');
  
  document.title = "PDFZaap — 35+ Free Online PDF Tools | No Signup Required";
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) {
    metaDesc.setAttribute('content', "PDFZaap offers 35+ free online PDF tools. Convert, compress, merge, split PDF files instantly. No signup, no watermark, 100% free forever.");
  }
  
  const blogSchema = document.getElementById('blog-schema');
  if (blogSchema) blogSchema.remove();

  scrollToTop();
}

function showBlogList() {
  document.getElementById('blog-section').classList.add('active');
  document.title = "Blog - PDFZaap Knowledge Base";
  scrollToTop();
}

function showBlogPost(slug) {
  const post = BLOG_POSTS[slug];
  if (!post) {
    window.location.hash = 'blog';
    return;
  }

  document.getElementById('blog-post-view').classList.add('active');
  
  document.getElementById('post-category').textContent = post.category;
  document.getElementById('post-title').textContent = post.title;
  document.getElementById('post-meta-details').textContent = `${post.date} • ${post.readTime}`;
  document.getElementById('post-content').innerHTML = post.content;

  document.title = `${post.title} | PDFZaap Blog`;
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) metaDesc.setAttribute('content', post.excerpt);

  let schemaScript = document.getElementById('blog-schema');
  if (schemaScript) schemaScript.remove();
  
  schemaScript = document.createElement('script');
  schemaScript.type = 'application/ld+json';
  schemaScript.id = 'blog-schema';
  
  const schemaData = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": post.title,
    "description": post.excerpt,
    "datePublished": post.date,
    "image": "https://pdfzaap.online/logo.png",
    "publisher": {
      "@type": "Organization",
      "name": "PDFZaap",
      "logo": {
        "@type": "ImageObject",
        "url": "https://pdfzaap.online/logo.png"
      }
    },
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": window.location.href
    },
    "articleSection": post.category,
    "wordCount": post.content.replace(/<[^>]*>/g, '').split(/\s+/).length
  };
  
  schemaScript.text = JSON.stringify(schemaData);
  document.head.appendChild(schemaScript);

  scrollToTop();
}

function showWorkspace(toolId) {
  activeTool = toolId;
  const toolData = TOOL_DATABASE[toolId];
  
  document.getElementById('tool-workspace').classList.add('active');
  
  document.title = `${toolData.title} Online Free | PDFZaap`;
  const metaDesc = document.querySelector('meta[name="description"]');
  if (metaDesc) {
    metaDesc.setAttribute('content', toolData.metaDesc);
  }

  document.getElementById('ws-title').textContent = `${toolData.emoji} ${toolData.title}`;
  document.getElementById('ws-subtitle').textContent = toolData.subtitle;
  document.getElementById('ws-dropzone-ext').textContent = `Accepted formats: ${toolData.accept}`;
  document.getElementById('ws-process-btn').textContent = toolData.execBtnText;

  const breadcrumb = document.getElementById('ws-breadcrumb');
  breadcrumb.innerHTML = `
    <span class="link" onclick="window.location.hash = ''">Home</span>
    <span>&gt;</span>
    <span>${toolData.title}</span>
  `;

  clearWorkspaceFile();
  setupOptionsPanel(toolId);

  // Populate Steps
  const stepsContainer = document.getElementById('ws-steps');
  stepsContainer.innerHTML = '';
  toolData.steps.forEach((step, index) => {
    stepsContainer.innerHTML += `
      <div class="step-item">
        <div class="step-num">${index + 1}</div>
        <h3>${step.title}</h3>
        <p>${step.desc}</p>
      </div>
    `;
  });

  // Populate Features
  const featuresContainer = document.getElementById('ws-features');
  featuresContainer.innerHTML = '';
  toolData.features.forEach(feat => {
    featuresContainer.innerHTML += `
      <div class="feature-card">
        <h3>${feat.title}</h3>
        <p>${feat.desc}</p>
      </div>
    `;
  });

  // Populate FAQs
  const faqContainer = document.getElementById('ws-faqs');
  faqContainer.innerHTML = '';
  toolData.faqs.forEach(item => {
    faqContainer.innerHTML += `
      <div class="faq-item">
        <button class="faq-trigger" onclick="toggleAccordion(this)">
          <span>${item.q}</span>
          <span class="faq-icon">▼</span>
        </button>
        <div class="faq-content">
          <p>${item.a}</p>
        </div>
      </div>
    `;
  });

  // Populate Related Grid
  const relatedGrid = document.getElementById('ws-related-grid');
  relatedGrid.innerHTML = '';
  toolData.related.forEach(relId => {
    const relData = TOOL_DATABASE[relId];
    if (relData) {
      relatedGrid.innerHTML += `
        <article class="tool-card" onclick="window.location.hash = '${relId}'">
          <div class="tool-icon-wrapper">${relData.emoji}</div>
          <h3>${relData.title}</h3>
          <p>${relData.subtitle}</p>
          <span class="tool-card-link">Use Tool ➔</span>
        </article>
      `;
    }
  });

  scrollToTop();
}

// ==========================================================================
// DYNAMIC COMPONENT BUILDERS
// ==========================================================================

function buildToolsGrid() {
  const grid = document.getElementById('main-tools-grid');
  if (!grid) return;
  // The homepage ships the full tools grid as static HTML (SEO). Only fill
  // the grid if it is empty, so we never replace the indexable markup.
  if (grid.children.length > 0) return;
  grid.innerHTML = '';

  for (const [key, value] of Object.entries(TOOL_DATABASE)) {
    grid.innerHTML += `
      <article class="tool-card" data-category="${value.category}" onclick="window.location.href = '${key}.html'">
        <div class="tool-icon-wrapper">${value.emoji}</div>
        <h3>${value.title}</h3>
        <p>${value.subtitle}</p>
        <span class="tool-card-link">Use Tool ➔</span>
      </article>
    `;
  }
}

function buildHomepageFAQs() {
  const parent = document.getElementById('homepage-faqs');
  if (!parent) return;
  parent.innerHTML = '';
  HOMEPAGE_FAQS.forEach(faq => {
    parent.innerHTML += `
      <div class="faq-item">
        <button class="faq-trigger" onclick="toggleAccordion(this)">
          <span>${faq.q}</span>
          <span class="faq-icon">▼</span>
        </button>
        <div class="faq-content">
          <p>${faq.a}</p>
        </div>
      </div>
    `;
  });
}

function buildBlogList() {
  const mainGrid = document.getElementById('main-blog-grid');
  const homeGrid = document.getElementById('homepage-blog-grid');
  if (!mainGrid || !homeGrid) return;

  mainGrid.innerHTML = '';
  homeGrid.innerHTML = '';

  Object.entries(BLOG_POSTS).forEach(([slug, post], index) => {
    const cardHtml = `
      <article class="blog-card" itemscope itemtype="https://schema.org/Article" onclick="window.location.hash = 'blog/${slug}'">
        <div class="blog-card-share-icon" aria-label="Share Post">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"></circle>
            <circle cx="6" cy="12" r="3"></circle>
            <circle cx="18" cy="19" r="3"></circle>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
          </svg>
        </div>
        
        <span class="blog-post-category blog-card-tag">${post.category}</span>
        <h3>${post.title}</h3>
        <time class="blog-card-date" datetime="${post.iso || ''}" itemprop="datePublished">${post.date}</time>
        <p class="blog-card-excerpt">${post.excerpt}</p>
        
        <div class="blog-card-footer">
          <div class="blog-card-comment">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>Post a Comment</span>
          </div>
          <span class="blog-card-readmore">Read More</span>
        </div>
      </article>
    `;
    
    mainGrid.innerHTML += cardHtml;
    if (index < 3) homeGrid.innerHTML += cardHtml;
  });
}

// ==========================================================================
// WORKSPACE OPTIONS PANEL FORM GENERATOR
// ==========================================================================

function setupOptionsPanel(toolId) {
  const panel = document.getElementById('ws-options-panel');
  const canvasWrapper = document.getElementById('ws-canvas-wrapper');
  
  panel.innerHTML = '';
  panel.classList.add('display-none');
  canvasWrapper.classList.add('display-none');

  if (toolId === 'compress-pdf') {
    panel.innerHTML = `
      <h4>Compression Adjustments</h4>
      <div class="option-row">
        <label for="compress-target">Target size (optional)</label>
        <select id="compress-target" class="option-field">
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
        <input type="range" id="compress-slider" class="option-field" min="0.1" max="1.0" step="0.1" value="0.6">
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
        <select id="img-page-size" class="option-field">
          <option value="fit">Fit page to each image</option>
          <option value="a4">A4 (210 × 297 mm) — image centered</option>
          <option value="letter">US Letter (8.5 × 11 in) — image centered</option>
        </select>
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'compare-pdf') {
    panel.innerHTML = `
      <h4>Compare Setup</h4>
      <p class="subtext-muted">Select exactly two PDF files above (the first is "Document A", the second "Document B"). The tool compares extracted text line by line and downloads an HTML report.</p>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'ocr-pdf') {
    panel.innerHTML = `
      <h4>OCR Setup</h4>
      <p class="subtext-muted">Recognition runs locally in your browser via Tesseract.js. On the first run the public English language model (a few MB) is downloaded from the Tesseract project's CDN — your file is never sent anywhere. Best results: clear, printed English text.</p>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'pdf-to-pdfa') {
    panel.innerHTML = `
      <h4>Archival Prep</h4>
      <p class="subtext-muted">This tool embeds archival metadata (title, subject, creation/modification dates) so the document is ready for long-term storage. It is <strong>not</strong> a certified PDF/A conversion — read the guide below for why and for the proper next step.</p>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'split-pdf') {
    panel.innerHTML = `
      <h4>Splitting Ranges</h4>
      <div class="option-row">
        <label for="split-pages-input">Page Range (e.g. 1-3, 5, 7-9)</label>
        <input type="text" id="split-pages-input" class="option-field" placeholder="e.g. 1-2, 4">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'rotate-pdf') {
    panel.innerHTML = `
      <h4>Rotation Degrees</h4>
      <div class="option-row">
        <label for="rotate-select">Rotation Angle</label>
        <select id="rotate-select" class="option-field">
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
        <input type="text" id="watermark-text" class="option-field" value="CONFIDENTIAL">
      </div>
      <div class="option-row">
        <label for="watermark-opacity">Opacity (0.1 to 1.0)</label>
        <input type="number" id="watermark-opacity" class="option-field" min="0.1" max="1.0" step="0.1" value="0.4">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'number-pdf-pages') {
    panel.innerHTML = `
      <h4>Position Parameters</h4>
      <div class="option-row">
        <label for="pagenum-pos">Select Placement Alignment</label>
        <select id="pagenum-pos" class="option-field">
          <option value="bottom-center">Bottom Center</option>
          <option value="bottom-right">Bottom Right</option>
        </select>
      </div>
      <div class="option-row">
        <label for="pagenum-size">Font Size (px)</label>
        <input type="number" id="pagenum-size" class="option-field" value="12" min="8" max="24">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'protect-pdf') {
    panel.innerHTML = `
      <h4>Lock Configuration</h4>
      <div class="option-row">
        <label for="protect-pass">Secure Access Password</label>
        <input type="password" id="protect-pass" class="option-field" placeholder="Enter secure password">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'esign-pdf') {
    canvasWrapper.classList.remove('display-none');
    initFabricCanvas();
  }
  else if (toolId === 'delete-pdf-pages' || toolId === 'extract-pages-pdf') {
    panel.innerHTML = `
      <h4>Page Selection</h4>
      <div class="option-row">
        <label for="pages-range-input">Pages (e.g. 1-3, 5, 8-10)</label>
        <input type="text" id="pages-range-input" class="option-field" placeholder="e.g. 1-3, 5">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'reorder-pages-pdf') {
    panel.innerHTML = `
      <h4>New Page Order</h4>
      <div class="option-row">
        <label for="pages-order-input">New order using every page exactly once (e.g. 3,1,2)</label>
        <input type="text" id="pages-order-input" class="option-field" placeholder="e.g. 3,1,2">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'crop-pdf') {
    panel.innerHTML = `
      <h4>Crop Margins (%)</h4>
      <div class="option-row">
        <label for="crop-left">Left %</label>
        <input type="number" id="crop-left" class="option-field" value="5" min="0" max="45">
      </div>
      <div class="option-row">
        <label for="crop-right">Right %</label>
        <input type="number" id="crop-right" class="option-field" value="5" min="0" max="45">
      </div>
      <div class="option-row">
        <label for="crop-top">Top %</label>
        <input type="number" id="crop-top" class="option-field" value="5" min="0" max="45">
      </div>
      <div class="option-row">
        <label for="crop-bottom">Bottom %</label>
        <input type="number" id="crop-bottom" class="option-field" value="5" min="0" max="45">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'resize-pdf') {
    panel.innerHTML = `
      <h4>Target Page Size</h4>
      <div class="option-row">
        <label for="resize-size">Page Format</label>
        <select id="resize-size" class="option-field">
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
        <input type="text" id="meta-title" class="option-field" placeholder="Document title">
      </div>
      <div class="option-row">
        <label for="meta-author">Author</label>
        <input type="text" id="meta-author" class="option-field" placeholder="Author name">
      </div>
      <div class="option-row">
        <label for="meta-subject">Subject</label>
        <input type="text" id="meta-subject" class="option-field" placeholder="Subject">
      </div>
      <div class="option-row">
        <label for="meta-keywords">Keywords</label>
        <input type="text" id="meta-keywords" class="option-field" placeholder="keyword1, keyword2">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  else if (toolId === 'unlock-pdf') {
    panel.innerHTML = `
      <h4>Protection Removal</h4>
      <div class="option-row">
        <label for="unlock-pass">Password (leave empty for restriction-only protection)</label>
        <input type="password" id="unlock-pass" class="option-field" placeholder="Optional password">
      </div>
    `;
    panel.classList.remove('display-none');
  }
  // All other tools need no extra options — the panel stays hidden.
}

// Fabric canvas helper
function initFabricCanvas() {
  if (fabricCanvas) {
    fabricCanvas.dispose();
  }
  fabricCanvas = new fabric.Canvas('esign-fabric-canvas', {
    isDrawingMode: true
  });
  fabricCanvas.freeDrawingBrush.width = 3;
  fabricCanvas.freeDrawingBrush.color = '#FF5200';
}

function clearSignatureCanvas() {
  if (fabricCanvas) {
    fabricCanvas.clear();
  }
}

// ==========================================================================
// FILE HANDLERS & UPLOAD DRAG/DROP
// ==========================================================================

function setupDropzone() {
  const wsDropzone = document.getElementById('ws-dropzone');
  const wsFileInput = document.getElementById('ws-file-input');

  if (!wsDropzone || !wsFileInput) return;

  wsDropzone.addEventListener('click', () => wsFileInput.click());
  
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

function handleUploadedFiles(files) {
  const toolData = TOOL_DATABASE[activeTool];
  if (!toolData.multiple) {
    uploadedFileArray = [files[0]];
  } else {
    for (let file of files) {
      uploadedFileArray.push(file);
    }
  }
  zaapTrack('file_selected', { files: files.length });
  renderWorkspaceFileList();
}

function renderWorkspaceFileList() {
  const listElement = document.getElementById('ws-file-list');
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
        <div class="file-row-remove" onclick="removeWorkspaceFile(${index})">Remove</div>
      </div>
    `;
  });

  const hasFiles = uploadedFileArray.filter(f => f).length > 0;
  document.getElementById('ws-process-btn').disabled = !hasFiles;
}

function removeWorkspaceFile(index) {
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
  uploadedFileArray = [];
  const input = document.getElementById('ws-file-input');
  if (input) input.value = '';
  
  document.getElementById('ws-file-list').innerHTML = '';
  document.getElementById('ws-process-btn').disabled = true;
  document.getElementById('ws-progress-container').style.display = 'none';
  document.getElementById('ws-output-box').style.display = 'none';
  document.getElementById('ws-output-box').innerHTML = '';
}

// ==========================================================================
// WORKSPACE EXECUTION & PDF ENGINES
// ==========================================================================

const _processBtn = document.getElementById('ws-process-btn');
if (_processBtn) {
_processBtn.addEventListener('click', async () => {
  const validFiles = uploadedFileArray.filter(f => f);
  if (validFiles.length === 0) return;
  zaapTrack('process_click', { tool: activeTool, files: validFiles.length });

  const progressContainer = document.getElementById('ws-progress-container');
  const progressBar = document.getElementById('ws-progress-bar');
  const progressStatus = document.getElementById('ws-progress-status');

  progressContainer.style.display = 'block';
  progressBar.style.width = '10%';
  progressStatus.textContent = 'Initializing engine...';

  try {
    switch(activeTool) {
      case 'merge-pdf':
        await runMergePDF(validFiles);
        break;
      case 'split-pdf':
        await runSplitPDF(validFiles[0]);
        break;
      case 'compress-pdf':
        await runCompressPDF(validFiles[0]);
        break;
      case 'rotate-pdf':
        await runRotatePDF(validFiles[0]);
        break;
      case 'pdf-to-jpg':
        await runPDFToImage(validFiles[0], 'image/jpeg', 'jpg');
        break;
      case 'pdf-to-png':
        await runPDFToImage(validFiles[0], 'image/png', 'png');
        break;
      case 'pdf-to-text':
        await runPDFToText(validFiles[0]);
        break;
      case 'jpg-to-pdf':
        await runImageToPDF(validFiles, 'jpg');
        break;
      case 'png-to-pdf':
        await runImageToPDF(validFiles, 'png');
        break;
      case 'word-to-pdf':
        await runWordToPDF(validFiles[0]);
        break;
      case 'add-watermark-pdf':
        await runAddWatermark(validFiles[0]);
        break;
      case 'number-pdf-pages':
        await runAddPageNumbers(validFiles[0]);
        break;
      case 'delete-pdf-pages':
        await runDeletePages(validFiles[0]);
        break;
      case 'extract-pages-pdf':
        await runExtractPages(validFiles[0]);
        break;
      case 'reorder-pages-pdf':
        await runReorderPages(validFiles[0]);
        break;
      case 'crop-pdf':
        await runCropPDF(validFiles[0]);
        break;
      case 'resize-pdf':
        await runResizePDF(validFiles[0]);
        break;
      case 'flatten-pdf':
        await runFlattenPDF(validFiles[0]);
        break;
      case 'pdf-metadata-editor':
        await runMetadataEditor(validFiles[0]);
        break;
      case 'repair-pdf':
        await runRepairPDF(validFiles[0]);
        break;
      case 'unlock-pdf':
        await runUnlockPDF(validFiles[0]);
        break;
      case 'ppt-to-pdf':
        await runPPTtoPDF(validFiles[0]);
        break;
      case 'pdf-to-powerpoint':
        await runPDFToPowerPoint(validFiles[0]);
        break;
      case 'protect-pdf':
        await runProtectPDF(validFiles[0]);
        break;
      case 'esign-pdf':
        await runESignPDF(validFiles[0]);
        break;
      case 'grayscale-pdf':
        await runGrayscalePDF(validFiles[0]);
        break;
      case 'ocr-pdf':
        await runOCRPDF(validFiles[0]);
        break;
      case 'compare-pdf':
        await runComparePDF(validFiles);
        break;
      case 'html-to-pdf':
        await runHTMLToPDF(validFiles[0]);
        break;
      case 'excel-to-pdf':
        await runExcelToPDF(validFiles[0]);
        break;
      case 'pdf-to-html':
        await runPDFToHTML(validFiles[0]);
        break;
      case 'pdf-to-epub':
        await runPDFToEPUB(validFiles[0]);
        break;
      case 'pdf-to-word':
        await runPDFToWord(validFiles[0]);
        break;
      case 'pdf-to-excel':
        await runPDFToExcel(validFiles[0]);
        break;
      case 'pdf-to-pdfa':
        await runArchivalPrep(validFiles[0]);
        break;
      default:
        throw new Error('This tool is not available. Please use the link from the homepage grid.');
    }
  } catch (err) {
    progressStatus.textContent = `Error: ${err.message}`;
    progressBar.style.backgroundColor = '#EF4444';
  }
});
}

function createDownloadLink(data, filename, type, note) {
  const blob = new Blob([data], { type: type });
  const container = document.getElementById('ws-output-box');
  const noteHtml = note ? `<p class="output-note">${note}</p>` : '';

  container.innerHTML = `
    <div class="download-box">
      <h4>🎉 PDF Processed Successfully!</h4>
      <p>Your document is ready to download.</p>
      ${noteHtml}
      <a id="direct-dl-link" href="${URL.createObjectURL(blob)}" download="${filename}" class="btn btn-primary">Download ${filename.split('.').pop().toUpperCase()}</a>
    </div>
  `;
  container.style.display = 'block';
  zaapTrack('download_click', { tool: activeTool, ext: (type || '').split('/')[1] || '' });
  document.getElementById('direct-dl-link').click();
}

function setProgressUI(percent, text) {
  const bar = document.getElementById('ws-progress-bar');
  const status = document.getElementById('ws-progress-status');
  bar.style.width = `${percent}%`;
  status.textContent = text;
}

// 1. Merge PDF
async function runMergePDF(files) {
  setProgressUI(30, 'Parsing PDF elements...');
  const { PDFDocument } = PDFLib;
  const mergedPdf = await PDFDocument.create();

  for (let i = 0; i < files.length; i++) {
    const fileBytes = await files[i].arrayBuffer();
    const srcDoc = await PDFDocument.load(fileBytes);
    const copiedPages = await mergedPdf.copyPages(srcDoc, srcDoc.getPageIndices());
    copiedPages.forEach((page) => mergedPdf.addPage(page));
    
    const progress = Math.round(((i + 1) / files.length) * 60) + 30;
    setProgressUI(progress, `Merging page layouts: file ${i + 1} of ${files.length}...`);
  }

  setProgressUI(95, 'Writing document layers...');
  const mergedPdfBytes = await mergedPdf.save();
  setProgressUI(100, 'Processing completed!');
  
  createDownloadLink(mergedPdfBytes, 'merged.pdf', 'application/pdf');
}

// 2. Split PDF
async function runSplitPDF(file) {
  setProgressUI(30, 'Analyzing PDF page tree...');
  const rangeInput = document.getElementById('split-pages-input').value.trim();
  if (!rangeInput) {
    throw new Error("Please enter a valid page range (e.g. 1-2, 4)");
  }

  const { PDFDocument } = PDFLib;
  const fileBytes = await file.arrayBuffer();
  const srcDoc = await PDFDocument.load(fileBytes);
  const totalPages = srcDoc.getPageCount();

  const targetIndices = [];
  const blocks = rangeInput.replace(/\s+/g, '').split(',');
  
  for (const block of blocks) {
    if (block.includes('-')) {
      const parts = block.split('-');
      const start = parseInt(parts[0], 10);
      const end = parseInt(parts[1], 10);
      if (!isNaN(start) && !isNaN(end)) {
        for (let i = start; i <= end; i++) {
          if (i >= 1 && i <= totalPages) targetIndices.push(i - 1);
        }
      }
    } else {
      const page = parseInt(block, 10);
      if (!isNaN(page) && page >= 1 && page <= totalPages) {
        targetIndices.push(page - 1);
      }
    }
  }

  if (targetIndices.length === 0) {
    throw new Error("Specified pages are invalid or exceed document boundaries.");
  }

  setProgressUI(60, 'Isolating specific pages...');
  const splitPdf = await PDFDocument.create();
  const copiedPages = await splitPdf.copyPages(srcDoc, targetIndices);
  copiedPages.forEach((page) => splitPdf.addPage(page));

  setProgressUI(90, 'Writing output document file...');
  const splitBytes = await splitPdf.save();
  setProgressUI(100, 'Splitting complete!');
  
  createDownloadLink(splitBytes, 'split.pdf', 'application/pdf');
}

// 3. Compress PDF
// Compresses by re-rendering each page to a JPEG in the browser, then rebuilding the PDF.
// Text in the original PDF is NOT preserved as selectable text — the output pages are images.
async function compressOnce(fileBytes, scale, quality, onProgress) {
  const pdf = await pdfjsLib.getDocument({ data: fileBytes }).promise;
  const { PDFDocument } = PDFLib;
  const compressedDoc = await PDFDocument.create();
  for (let i = 1; i <= pdf.numPages; i++) {
    if (onProgress) onProgress(i, pdf.numPages);
    const page = await pdf.getPage(i);
    const viewport = page.getViewport({ scale: scale });
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    await page.render({ canvasContext: ctx, viewport: viewport }).promise;
    const imgBytes = await fetch(canvas.toDataURL('image/jpeg', quality)).then(res => res.arrayBuffer());
    const embeddedImg = await compressedDoc.embedJpg(imgBytes);
    const newPage = compressedDoc.addPage([viewport.width, viewport.height]);
    newPage.drawImage(embeddedImg, { x: 0, y: 0, width: viewport.width, height: viewport.height });
  }
  return { bytes: await compressedDoc.save(), pages: pdf.numPages };
}

function formatKB(bytes) {
  return bytes >= 1048576 ? (bytes / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(bytes / 1024)) + ' KB';
}

async function runCompressPDF(file) {
  const sliderEl = document.getElementById('compress-slider');
  const targetEl = document.getElementById('compress-target');
  const quality = sliderEl ? (parseFloat(sliderEl.value) || 0.6) : 0.6;
  const targetKB = targetEl ? parseInt(targetEl.value, 10) : 0;
  const fileBytes = await file.arrayBuffer();
  const origKB = formatKB(fileBytes.byteLength);

  if (!targetKB) {
    // Manual quality mode
    setProgressUI(20, 'Unpacking document buffers...');
    const { bytes, pages } = await compressOnce(fileBytes, 1.5, quality, (i, n) => {
      setProgressUI(Math.round((i / n) * 80) + 15, `Optimizing pages: ${i}/${n}...`);
    });
    setProgressUI(100, 'Optimization completed!');
    const note = `Original size ${origKB} → compressed to ${formatKB(bytes.byteLength)}. ` +
      (bytes.byteLength >= fileBytes.byteLength
        ? 'Honest note: this file was already very efficient, so compression did not reduce the size. Try a lower quality value or fewer pages.'
        : 'Lower quality values give smaller files but softer images.');
    createDownloadLink(bytes, 'compressed.pdf', 'application/pdf', note);
    return;
  }

  // Target-size mode: step down render scale, then binary-search JPEG quality.
  setProgressUI(5, `Aiming for under ${formatKB(targetKB * 1024)}...`);
  let best = null; // { bytes, scale, quality, size }
  for (const scale of [1.5, 1.0, 0.75, 0.5]) {
    let lo = 0.05, hi = 0.9, passes = 0;
    while (passes < 5 && (hi - lo) > 0.02) {
      passes++;
      const mid = (lo + hi) / 2;
      const { bytes, pages } = await compressOnce(fileBytes, scale, mid, (i, n) => {
        setProgressUI(10 + Math.min(88, Math.round(passes * 16 + (i / n) * 12)), `Pass ${passes}: page ${i}/${n} (scale ${scale}, quality ${mid.toFixed(2)})...`);
      });
      if (bytes.byteLength <= targetKB * 1024) {
        if (!best || bytes.byteLength < best.size) best = { bytes, scale, quality: mid, size: bytes.byteLength };
        hi = mid;
      } else {
        lo = mid;
        if (!best) best = { bytes, scale, quality: mid, size: bytes.byteLength };
      }
      if (best && best.size <= targetKB * 1024 && scale === 1.5 && passes >= 2) break;
    }
    if (best && best.size <= targetKB * 1024) break;
  }

  if (!best) throw new Error('Compression could not run on this file.');
  const reached = best.size <= targetKB * 1024;
  setProgressUI(100, reached
    ? `Target reached: ${formatKB(best.size)} (under ${formatKB(targetKB * 1024)}).`
    : `Smallest result: ${formatKB(best.size)} — target not fully reached.`);
  const note = reached
    ? `Target ${formatKB(targetKB * 1024)} reached: output is ${formatKB(best.size)} (original ${origKB}).`
    : `Honest result: the smallest output this file can reach in your browser is ${formatKB(best.size)} — below ${formatKB(targetKB * 1024)} was not possible without destroying the content. Try the PDF to JPG route or remove pages to get under the limit.`;
  createDownloadLink(best.bytes, `compressed_under_${targetKB}kb.pdf`, 'application/pdf', note);
}

// 4. Rotate PDF
async function runRotatePDF(file) {
  setProgressUI(30, 'Opening PDF parameters...');
  const angle = parseInt(document.getElementById('rotate-select').value, 10) || 90;

  const { PDFDocument, degrees } = PDFLib;
  const fileBytes = await file.arrayBuffer();
  const pdfDoc = await PDFDocument.load(fileBytes);
  const pages = pdfDoc.getPages();

  setProgressUI(60, 'Calculating rotation matrices...');
  pages.forEach((page) => {
    const currentRotation = page.getRotation().angle;
    page.setRotation(degrees(currentRotation + angle));
  });

  setProgressUI(90, 'Writing rotated coordinates...');
  const outBytes = await pdfDoc.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'rotated.pdf', 'application/pdf');
}

// 5. PDF to Images (JPG/PNG)
async function runPDFToImage(file, mimeType, extension) {
  setProgressUI(20, 'Decoding document components...');
  const fileBytes = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: fileBytes }).promise;
  const zip = new JSZip();

  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(Math.round((i / pdf.numPages) * 60) + 20, `Rendering canvas pages: ${i}/${pdf.numPages}...`);
    
    const page = await pdf.getPage(i);
    const viewport = page.getViewport({ scale: 2.0 });
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = viewport.width;
    canvas.height = viewport.height;

    await page.render({ canvasContext: ctx, viewport: viewport }).promise;
    
    const imgDataUrl = canvas.toDataURL(mimeType);
    const base64Data = imgDataUrl.split(',')[1];
    zip.file(`page-${i}.${extension}`, base64Data, { base64: true });
  }

  setProgressUI(90, 'Zipping dynamic assets...');
  const zipBlob = await zip.generateAsync({ type: 'blob' });
  setProgressUI(100, 'Packing complete!');
  createDownloadLink(zipBlob, 'extracted_images.zip', 'application/zip');
}

// 6. PDF to Text
async function runPDFToText(file) {
  setProgressUI(20, 'Reading characters map...');
  const fileBytes = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: fileBytes }).promise;
  let textOut = '';

  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(Math.round((i / pdf.numPages) * 70) + 20, `Extracting strings: page ${i}/${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const content = await page.getTextContent();
    const pageText = content.items.map(item => item.str).join(' ');
    textOut += `--- Page ${i} ---\n${pageText}\n\n`;
  }

  setProgressUI(95, 'Writing string buffers...');
  setProgressUI(100, 'Extraction complete!');
  createDownloadLink(new TextEncoder().encode(textOut), 'extracted_text.txt', 'text/plain');
}

// 7. Image to PDF (optional fixed page size: fit-to-image, A4, or US Letter)
const PAGE_SIZES_PT = {
  a4: [595.28, 841.89],
  letter: [612, 792]
};

async function runImageToPDF(files, extension) {
  setProgressUI(30, 'Opening canvas document...');
  const { PDFDocument } = PDFLib;
  const pdfDoc = await PDFDocument.create();
  const sizeEl = document.getElementById('img-page-size');
  const pageSize = sizeEl && PAGE_SIZES_PT[sizeEl.value] ? PAGE_SIZES_PT[sizeEl.value] : null;

  for (let i = 0; i < files.length; i++) {
    setProgressUI(Math.round(((i + 1) / files.length) * 50) + 30, `Embedding image layouts: ${i+1}/${files.length}...`);
    const buffer = await files[i].arrayBuffer();

    let embeddedImg;
    if (extension === 'jpg' || extension === 'jpeg') {
      embeddedImg = await pdfDoc.embedJpg(buffer);
    } else {
      embeddedImg = await pdfDoc.embedPng(buffer);
    }

    const { width: imgW, height: imgH } = embeddedImg.scale(1.0);
    if (!pageSize) {
      const page = pdfDoc.addPage([imgW, imgH]);
      page.drawImage(embeddedImg, { x: 0, y: 0, width: imgW, height: imgH });
      continue;
    }
    const [pageW, pageH] = pageSize;
    const margin = 24;
    const scale = Math.min((pageW - margin * 2) / imgW, (pageH - margin * 2) / imgH, 1);
    const w = imgW * scale, h = imgH * scale;
    const page = pdfDoc.addPage([pageW, pageH]);
    page.drawRectangle({ x: 0, y: 0, width: pageW, height: pageH, color: PDFLib.rgb(1, 1, 1) });
    page.drawImage(embeddedImg, { x: (pageW - w) / 2, y: (pageH - h) / 2, width: w, height: h });
  }

  setProgressUI(90, 'Compiling coordinate sheets...');
  const pdfBytes = await pdfDoc.save();
  setProgressUI(100, 'Conversion complete!');
  const note = pageSize
    ? `Each image is centered on a ${pageSize === PAGE_SIZES_PT.a4 ? 'A4' : 'US Letter'} page, scaled down to fit with 24pt margins (images are never upscaled beyond their native size).`
    : 'Each image fills its own page at full resolution.';
  createDownloadLink(pdfBytes, 'images_converted.pdf', 'application/pdf', note);
}

// 8. Word to PDF
async function runWordToPDF(file) {
  setProgressUI(30, 'Reading DOCX components...');
  const arrayBuffer = await file.arrayBuffer();
  
  const result = await mammoth.convertToHtml({ arrayBuffer: arrayBuffer });
  const htmlContent = result.value;

  setProgressUI(60, 'Rendering temporary layout context...');
  const opt = {
    margin:       1,
    filename:     'converted.pdf',
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2 },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
  };

  const element = document.createElement('div');
  element.style.padding = '20px';
  element.innerHTML = htmlContent;

  setProgressUI(90, 'Exporting file pages...');
  const pdfBlob = await html2pdf().from(element).set(opt).outputPdf('blob');
  
  setProgressUI(100, 'Process complete!');
  createDownloadLink(pdfBlob, 'converted.pdf', 'application/pdf');
}

// 9. Add Watermark
async function runAddWatermark(file) {
  setProgressUI(30, 'Opening page matrices...');
  const text = document.getElementById('watermark-text').value || 'CONFIDENTIAL';
  const opacity = parseFloat(document.getElementById('watermark-opacity').value) || 0.4;

  const { PDFDocument, rgb, degrees, StandardFonts } = PDFLib;
  const fileBytes = await file.arrayBuffer();
  const pdfDoc = await PDFDocument.load(fileBytes);
  const helveticaFont = await pdfDoc.embedFont(StandardFonts.HelveticaBold);
  const pages = pdfDoc.getPages();

  pages.forEach((page, index) => {
    setProgressUI(Math.round((index / pages.length) * 50) + 30, `Applying watermarks: page ${index + 1}...`);
    const { width, height } = page.getSize();
    page.drawText(text, {
      x: width / 6,
      y: height / 2.5,
      size: 50,
      font: helveticaFont,
      color: rgb(1.0, 0.32, 0.0), // iLovePDF Signature Orange Accent
      opacity: opacity,
      rotate: degrees(45)
    });
  });

  setProgressUI(90, 'Writing modifications...');
  const outBytes = await pdfDoc.save();
  setProgressUI(100, 'Process complete!');
  createDownloadLink(outBytes, 'watermarked.pdf', 'application/pdf');
}

// 10. Add Page Numbers
async function runAddPageNumbers(file) {
  setProgressUI(30, 'Opening document margins...');
  const pos = document.getElementById('pagenum-pos').value || 'bottom-center';
  const fontSize = parseInt(document.getElementById('pagenum-size').value, 10) || 12;

  const { PDFDocument, rgb, StandardFonts } = PDFLib;
  const fileBytes = await file.arrayBuffer();
  const pdfDoc = await PDFDocument.load(fileBytes);
  const helveticaFont = await pdfDoc.embedFont(StandardFonts.Helvetica);
  const pages = pdfDoc.getPages();

  pages.forEach((page, index) => {
    setProgressUI(Math.round((index / pages.length) * 50) + 30, `Drawing page counts: ${index+1}/${pages.length}...`);
    const { width } = page.getSize();
    const numberText = `Page ${index + 1} of ${pages.length}`;
    
    let x = width / 2 - 20;
    if (pos === 'bottom-right') {
      x = width - 100;
    }

    page.drawText(numberText, {
      x: x,
      y: 25,
      size: fontSize,
      font: helveticaFont,
      color: rgb(0.2, 0.2, 0.2)
    });
  });

  setProgressUI(90, 'Writing coordinates metrics...');
  const outBytes = await pdfDoc.save();
  setProgressUI(100, 'Process complete!');
  createDownloadLink(outBytes, 'numbered.pdf', 'application/pdf');
}

// 11. Protect PDF
async function runProtectPDF(file) {
  setProgressUI(30, 'Reading document...');
  const pass = document.getElementById('protect-pass').value.trim();
  if (!pass) {
    throw new Error('Please enter a password to protect this document with.');
  }
  if (pass.length < 4) {
    throw new Error('Please use a password of at least 4 characters.');
  }

  const fileBytes = await file.arrayBuffer();
  const pdfDoc = await PDFLib.PDFDocument.load(fileBytes);

  if (typeof pdfDoc.encrypt !== 'function') {
    throw new Error('Encryption engine failed to load. Please refresh the page and try again.');
  }

  setProgressUI(70, 'Encrypting with AES...');
  pdfDoc.encrypt({
    userPassword: pass,
    ownerPassword: pass
  });
  const outBytes = await pdfDoc.save();

  setProgressUI(100, 'Security locked!');
  createDownloadLink(outBytes, 'protected.pdf', 'application/pdf');
}

// 12. E-Sign PDF
async function runESignPDF(file) {
  setProgressUI(30, 'Extracting signature path...');
  if (!fabricCanvas) {
    throw new Error("Canvas context is not initialized.");
  }

  const sigDataUrl = fabricCanvas.toDataURL({ format: 'png' });
  const response = await fetch(sigDataUrl);
  const sigImgBytes = await response.arrayBuffer();

  const { PDFDocument } = PDFLib;
  const fileBytes = await file.arrayBuffer();
  const pdfDoc = await PDFDocument.load(fileBytes);
  const firstPage = pdfDoc.getPages()[0];

  if (!firstPage) {
    throw new Error("Document is empty.");
  }

  setProgressUI(65, 'Embedding canvas vectors...');
  const sigImg = await pdfDoc.embedPng(sigImgBytes);
  
  firstPage.drawImage(sigImg, {
    x: 50,
    y: 50,
    width: 180,
    height: 90
  });

  setProgressUI(90, 'Writing modified layers...');
  const outBytes = await pdfDoc.save();
  setProgressUI(100, 'Document e-signed successfully!');
  createDownloadLink(outBytes, 'signed.pdf', 'application/pdf');
}

// 13. Grayscale PDF
async function runGrayscalePDF(file) {
  setProgressUI(20, 'Decomposing visual pages...');
  const fileBytes = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: fileBytes }).promise;
  
  const { PDFDocument } = PDFLib;
  const grayscaleDoc = await PDFDocument.create();

  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(Math.round((i / pdf.numPages) * 60) + 20, `Converting pixel metrics: page ${i}/${pdf.numPages}...`);
    
    const page = await pdf.getPage(i);
    const viewport = page.getViewport({ scale: 1.5 });
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = viewport.width;
    canvas.height = viewport.height;

    await page.render({ canvasContext: ctx, viewport: viewport }).promise;

    const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imgData.data;
    for (let j = 0; j < data.length; j += 4) {
      const brightness = 0.34 * data[j] + 0.5 * data[j + 1] + 0.16 * data[j + 2];
      data[j] = brightness;
      data[j + 1] = brightness;
      data[j + 2] = brightness;
    }
    ctx.putImageData(imgData, 0, 0);

    const imgDataUrl = canvas.toDataURL('image/jpeg', 0.85);
    const imgBytes = await fetch(imgDataUrl).then(res => res.arrayBuffer());
    
    const embeddedImg = await grayscaleDoc.embedJpg(imgBytes);
    const newPage = grayscaleDoc.addPage([viewport.width, viewport.height]);
    newPage.drawImage(embeddedImg, { x: 0, y: 0, width: viewport.width, height: viewport.height });
  }

  setProgressUI(95, 'Compiling document sheets...');
  const outBytes = await grayscaleDoc.save();
  setProgressUI(100, 'Monochrome convert complete!');
  createDownloadLink(outBytes, 'grayscale.pdf', 'application/pdf');
}

// Advanced Tools Simulation Handler

// ==========================================================================
// REAL CLIENT-SIDE PDF ENGINES (pdf-lib / pdf.js / JSZip / pptxgenjs)
// ==========================================================================

// Parse "1-3, 5" style selections into a sorted, unique 0-based index array
function parsePageRanges(input, maxPages) {
  const cleaned = (input || '').trim();
  if (!cleaned) throw new Error('Please enter at least one page number (e.g. 1-3, 5).');
  const picked = new Set();
  cleaned.split(',').forEach(part => {
    const chunk = part.trim();
    if (!chunk) return;
    const m = chunk.match(/^(\d+)\s*-\s*(\d+)$/);
    if (m) {
      let a = parseInt(m[1], 10);
      let b = parseInt(m[2], 10);
      if (a > b) { const tmp = a; a = b; b = tmp; }
      for (let i = a; i <= b; i++) {
        if (i < 1 || i > maxPages) throw new Error(`Page ${i} is out of range (this document has ${maxPages} pages).`);
        picked.add(i - 1);
      }
    } else if (/^\d+$/.test(chunk)) {
      const n = parseInt(chunk, 10);
      if (n < 1 || n > maxPages) throw new Error(`Page ${n} is out of range (this document has ${maxPages} pages).`);
      picked.add(n - 1);
    } else {
      throw new Error(`"${chunk}" is not a valid page number or range.`);
    }
  });
  if (picked.size === 0) throw new Error('Please enter at least one page number.');
  return [...picked].sort((a, b) => a - b);
}

async function runDeletePages(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  const total = doc.getPageCount();
  const toDelete = parsePageRanges(document.getElementById('pages-range-input').value, total);
  if (toDelete.length >= total) throw new Error('You cannot delete every page — leave at least one page in the document.');
  setProgressUI(60, 'Removing selected pages...');
  const keep = [];
  for (let i = 0; i < total; i++) if (!toDelete.includes(i)) keep.push(i);
  const out = await PDFLib.PDFDocument.create();
  const copied = await out.copyPages(doc, keep);
  copied.forEach(pg => out.addPage(pg));
  const outBytes = await out.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'deleted-pages.pdf', 'application/pdf');
}

async function runExtractPages(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  const total = doc.getPageCount();
  const picked = parsePageRanges(document.getElementById('pages-range-input').value, total);
  setProgressUI(60, 'Copying selected pages...');
  const out = await PDFLib.PDFDocument.create();
  const copied = await out.copyPages(doc, picked);
  copied.forEach(pg => out.addPage(pg));
  const outBytes = await out.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'extracted-pages.pdf', 'application/pdf');
}

async function runReorderPages(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  const total = doc.getPageCount();
  const raw = (document.getElementById('pages-order-input').value || '').trim();
  if (!raw) throw new Error('Enter the new page order using every page number exactly once, e.g. 3,1,2.');
  const order = [];
  raw.split(',').forEach(part => {
    const chunk = part.trim();
    if (!chunk) return;
    if (!/^\d+$/.test(chunk)) throw new Error(`"${chunk}" is not a valid page number.`);
    const n = parseInt(chunk, 10);
    if (n < 1 || n > total) throw new Error(`Page ${n} is out of range (this document has ${total} pages).`);
    order.push(n - 1);
  });
  if (order.length !== total) throw new Error(`Please list all ${total} pages exactly once (you entered ${order.length}).`);
  setProgressUI(60, 'Rearranging pages...');
  const out = await PDFLib.PDFDocument.create();
  const copied = await out.copyPages(doc, order);
  copied.forEach(pg => out.addPage(pg));
  const outBytes = await out.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'reordered.pdf', 'application/pdf');
}

async function runCropPDF(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  const clampPct = v => Math.min(Math.max(isFinite(v) ? v : 0, 0), 45) / 100;
  const l = clampPct(parseFloat(document.getElementById('crop-left').value));
  const r = clampPct(parseFloat(document.getElementById('crop-right').value));
  const t = clampPct(parseFloat(document.getElementById('crop-top').value));
  const b = clampPct(parseFloat(document.getElementById('crop-bottom').value));
  setProgressUI(60, 'Applying crop boxes...');
  doc.getPages().forEach(page => {
    const { width, height } = page.getSize();
    const newW = width * (1 - l - r);
    const newH = height * (1 - t - b);
    if (newW > 10 && newH > 10) page.setCropBox(width * l, height * b, newW, newH);
  });
  const outBytes = await doc.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'cropped.pdf', 'application/pdf');
}

async function runResizePDF(file) {
  setProgressUI(25, 'Reading document...');
  const bytes = await file.arrayBuffer();
  const format = document.getElementById('resize-size') ? document.getElementById('resize-size').value : 'a4';
  const target = format === 'letter' ? { w: 612, h: 792 } : { w: 595.28, h: 841.89 };
  const doc = await PDFLib.PDFDocument.load(bytes);
  const embedded = await doc.embedPdf(bytes, doc.getPageIndices());
  const out = await PDFLib.PDFDocument.create();
  setProgressUI(60, 'Scaling pages to the selected format...');
  embedded.forEach(ep => {
    const page = out.addPage([target.w, target.h]);
    const scale = Math.min(target.w / ep.width, target.h / ep.height);
    const w = ep.width * scale;
    const h = ep.height * scale;
    page.drawPage(ep, { x: (target.w - w) / 2, y: (target.h - h) / 2, width: w, height: h });
  });
  const outBytes = await out.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'resized.pdf', 'application/pdf');
}

async function runFlattenPDF(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  setProgressUI(60, 'Flattening form fields and annotations...');
  try {
    const form = doc.getForm();
    if (form.getFields().length) form.flatten();
  } catch (e) { /* document has no interactive form — re-serializing is still useful */ }
  const outBytes = await doc.save({ useObjectStreams: false });
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'flattened.pdf', 'application/pdf');
}

async function runMetadataEditor(file) {
  setProgressUI(25, 'Reading document...');
  const doc = await PDFLib.PDFDocument.load(await file.arrayBuffer());
  const title = document.getElementById('meta-title') ? document.getElementById('meta-title').value.trim() : '';
  const author = document.getElementById('meta-author') ? document.getElementById('meta-author').value.trim() : '';
  const subject = document.getElementById('meta-subject') ? document.getElementById('meta-subject').value.trim() : '';
  const keywords = document.getElementById('meta-keywords') ? document.getElementById('meta-keywords').value.trim() : '';
  if (!title && !author && !subject && !keywords) throw new Error('Fill in at least one metadata field before processing.');
  setProgressUI(60, 'Writing metadata...');
  if (title) doc.setTitle(title);
  if (author) doc.setAuthor(author);
  if (subject) doc.setSubject(subject);
  if (keywords) doc.setKeywords(keywords.split(',').map(k => k.trim()).filter(Boolean));
  doc.setModificationDate(new Date());
  const outBytes = await doc.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'metadata-updated.pdf', 'application/pdf');
}

async function runRepairPDF(file) {
  setProgressUI(30, 'Rebuilding document structure...');
  const bytes = await file.arrayBuffer();
  let doc;
  try {
    doc = await PDFLib.PDFDocument.load(bytes, { ignoreEncryption: true, throwOnInvalidObject: false });
  } catch (e) {
    throw new Error('This file is too damaged to recover automatically. Please try obtaining a new copy of the document.');
  }
  setProgressUI(70, 'Re-serializing pages and objects...');
  const outBytes = await doc.save({ useObjectStreams: false });
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'repaired.pdf', 'application/pdf');
}

async function runUnlockPDF(file) {
  setProgressUI(30, 'Reading protected document...');
  const bytes = await file.arrayBuffer();
  const passInput = document.getElementById('unlock-pass');
  const pass = passInput ? passInput.value.trim() : '';

  if (!pass) {
    // No password given: check whether the document is actually encrypted
    const probe = await PDFLib.PDFDocument.load(bytes, { ignoreEncryption: true });
    if (probe.isEncrypted) {
      throw new Error('This PDF is encrypted. Please enter its open password above, then process again to remove protection.');
    }
    setProgressUI(70, 'Re-saving document without restrictions...');
    const outBytes = await probe.save();
    setProgressUI(100, 'Processing completed!');
    createDownloadLink(outBytes, 'unlocked.pdf', 'application/pdf');
    return;
  }

  let doc;
  try {
    doc = await PDFLib.PDFDocument.load(bytes, { password: pass });
  } catch (e) {
    throw new Error('Could not decrypt this PDF — the password looks incorrect or the encryption type is unsupported. Please double-check the password.');
  }

  setProgressUI(70, 'Removing password protection and re-saving...');
  // Copy every page into a brand-new document so no encryption metadata carries over
  const clean = await PDFLib.PDFDocument.create();
  const copied = await clean.copyPages(doc, doc.getPageIndices());
  copied.forEach(pg => clean.addPage(pg));
  const outBytes = await clean.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, 'unlocked.pdf', 'application/pdf');
}

function wrapPdfText(text, font, size, maxWidth) {
  const words = text.split(/\s+/).filter(Boolean);
  const lines = [];
  let line = '';
  words.forEach(w => {
    const test = line ? line + ' ' + w : w;
    if (font.widthOfTextAtSize(test, size) > maxWidth && line) {
      lines.push(line);
      line = w;
    } else {
      line = test;
    }
  });
  if (line) lines.push(line);
  return lines;
}

async function runPPTtoPDF(file) {
  if (typeof JSZip === 'undefined') throw new Error('Conversion engine failed to load. Please refresh the page and try again.');
  if (!/\.pptx$/i.test(file.name)) throw new Error('Please upload a .pptx file. Legacy .ppt files must first be saved as .pptx in PowerPoint.');
  setProgressUI(20, 'Unpacking presentation...');
  const zip = await JSZip.loadAsync(await file.arrayBuffer());
  const slideNames = Object.keys(zip.files)
    .filter(n => /^ppt\/slides\/slide\d+\.xml$/.test(n))
    .sort((a, b) => parseInt(a.match(/(\d+)/)[1], 10) - parseInt(b.match(/(\d+)/)[1], 10));
  if (!slideNames.length) throw new Error('No slides were found inside this PPTX file.');
  const pdfDoc = await PDFLib.PDFDocument.create();
  const regular = await pdfDoc.embedFont(PDFLib.StandardFonts.Helvetica);
  const bold = await pdfDoc.embedFont(PDFLib.StandardFonts.HelveticaBold);
  const decode = t => t.replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&amp;/g, '&');
  for (let i = 0; i < slideNames.length; i++) {
    setProgressUI(20 + Math.round((i / slideNames.length) * 60), `Rendering slide ${i + 1} of ${slideNames.length}...`);
    const xml = await zip.files[slideNames[i]].async('string');
    const texts = [];
    const re = /<a:t>([\s\S]*?)<\/a:t>/g;
    let m;
    while ((m = re.exec(xml)) !== null) {
      const txt = decode(m[1]).trim();
      if (txt) texts.push(txt);
    }
    // 10 x 7.5 inch slide canvas (720 x 540 pt)
    const page = pdfDoc.addPage([720, 540]);
    let y = 492;
    if (texts.length) {
      const title = texts.shift();
      const tSize = title.length > 90 ? 22 : 28;
      wrapPdfText(title, bold, tSize, 620).forEach(line => {
        page.drawText(line, { x: 50, y, size: tSize, font: bold, color: PDFLib.rgb(0.12, 0.12, 0.14) });
        y -= tSize * 1.3;
      });
      y -= 12;
    }
    const bSize = 14;
    texts.slice(0, 22).forEach(t => {
      wrapPdfText('\u2022 ' + t, regular, bSize, 620).forEach(line => {
        if (y < 40) return;
        page.drawText(line, { x: 58, y, size: bSize, font: regular, color: PDFLib.rgb(0.25, 0.25, 0.28) });
        y -= bSize * 1.45;
      });
      y -= 6;
    });
  }
  const outBytes = await pdfDoc.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, file.name.replace(/\.pptx$/i, '') + '.pdf', 'application/pdf');
}

async function runPDFToPowerPoint(file) {
  if (typeof pdfjsLib === 'undefined' || typeof PptxGenJS === 'undefined') throw new Error('Conversion engine failed to load. Please refresh the page and try again.');
  setProgressUI(10, 'Reading PDF...');
  const bytes = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: bytes }).promise;
  const pptx = new PptxGenJS();
  pptx.defineLayout({ name: 'PDFZAAP_SLIDES', width: 10, height: 7.5 });
  pptx.layout = 'PDFZAAP_SLIDES';
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(10 + Math.round((i / pdf.numPages) * 70), `Converting page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const viewport = page.getViewport({ scale: 2 });
    const canvas = document.createElement('canvas');
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    await page.render({ canvasContext: canvas.getContext('2d'), viewport }).promise;
    const slide = pptx.addSlide();
    slide.addImage({ data: canvas.toDataURL('image/jpeg', 0.92), x: 0, y: 0, w: 10, h: 7.5 });
  }
  setProgressUI(95, 'Building PowerPoint file...');
  const blob = await pptx.write({ outputType: 'blob' });
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(blob, file.name.replace(/\.pdf$/i, '') + '.pptx', 'application/vnd.openxmlformats-officedocument.presentationml.presentation');
}

// Helper: render one PDF page to a canvas at a given scale
async function renderPageToCanvas(pdf, pageNum, scale) {
  const page = await pdf.getPage(pageNum);
  const viewport = page.getViewport({ scale: scale });
  const canvas = document.createElement('canvas');
  canvas.width = viewport.width;
  canvas.height = viewport.height;
  await page.render({ canvasContext: canvas.getContext('2d'), viewport: viewport }).promise;
  return canvas;
}

// Helper: extract text lines from a pdf.js page (grouped by Y coordinate)
async function extractPageLines(page) {
  const content = await page.getTextContent();
  const byY = new Map();
  for (const item of content.items) {
    if (!item.str) continue;
    const y = Math.round(item.transform[5]);
    const bucket = byY.get(y);
    if (bucket) bucket.push([item.transform[4], item.str]);
    else byY.set(y, [[item.transform[4], item.str]]);
  }
  const lines = [];
  const ys = Array.from(byY.keys()).sort((a, b) => b - a);
  for (const y of ys) {
    const parts = byY.get(y).sort((a, b) => a[0] - b[0]);
    lines.push(parts.map(p => p[1]).join(' ').replace(/\s+/g, ' ').trim());
  }
  return lines.filter(l => l.length > 0);
}

function escapeXml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// OCR PDF (Tesseract.js — recognition runs in a local Web Worker; only the public language model is downloaded)
async function runOCRPDF(file) {
  if (typeof Tesseract === 'undefined') throw new Error('The OCR engine failed to load. Please refresh the page and try again.');
  setProgressUI(5, 'Preparing OCR engine...');
  const isImage = /\.(jpe?g|png|webp|bmp)$/i.test(file.name);
  const baseName = file.name.replace(/\.[^.]+$/, '');

  const worker = await Tesseract.createWorker('eng', 1, {
    logger: m => {
      if (m.status === 'recognizing text') {
        setProgressUI(10 + Math.round(m.progress * 85), `Recognizing text… ${Math.round(m.progress * 100)}%`);
      }
    }
  });

  try {
    let allText = '';
    if (isImage) {
      setProgressUI(10, 'Loading image...');
      const img = await createImageBitmap(await file.arrayBuffer());
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext('2d').drawImage(img, 0, 0);
      const { data } = await worker.recognize(canvas);
      allText = data.text;
    } else {
      const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
      for (let i = 1; i <= pdf.numPages; i++) {
        setProgressUI(5 + Math.round(((i - 1) / pdf.numPages) * 90), `Preparing page ${i} of ${pdf.numPages} for OCR...`);
        const canvas = await renderPageToCanvas(pdf, i, 2);
        const { data } = await worker.recognize(canvas);
        allText += `--- Page ${i} ---\n${data.text.trim()}\n\n`;
      }
    }
    if (!allText.trim()) {
      throw new Error('No readable text was found. Make sure the document contains clear, printed English text (photos of handwriting are not supported).');
    }
    setProgressUI(98, 'Building text file...');
    createDownloadLink(new TextEncoder().encode(allText), `${baseName}_ocr.txt`, 'text/plain',
      'OCR finished. The output is a plain-text file with the recognized words. Check a few paragraphs — OCR is not perfect, so always proofread before submitting important documents.');
  } finally {
    await worker.terminate();
  }
}

// HTML to PDF (html2pdf.js renders the markup in your browser)
async function runHTMLToPDF(file) {
  if (typeof html2pdf === 'undefined') throw new Error('The PDF rendering engine failed to load. Please refresh the page and try again.');
  setProgressUI(20, 'Reading HTML file...');
  const text = await file.text();
  const baseName = file.name.replace(/\.[^.]+$/, '');

  const container = document.createElement('div');
  container.style.width = '720px';
  container.style.padding = '12px';
  container.style.fontFamily = 'Arial, Helvetica, sans-serif';
  container.style.fontSize = '13px';
  container.style.lineHeight = '1.55';
  container.style.color = '#111';
  container.innerHTML = text;
  // Neutralize scripts inside user markup before rendering
  container.querySelectorAll('script, iframe, object, embed, link[rel="import"]').forEach(el => el.remove());

  setProgressUI(55, 'Rendering pages...');
  const pdfBlob = await html2pdf()
    .from(container)
    .set({
      margin: 10,
      image: { type: 'jpeg', quality: 0.95 },
      html2canvas: { scale: 2, useCORS: true, logging: false },
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
    })
    .outputPdf('blob');

  setProgressUI(100, 'Processing completed!');
  createDownloadLink(pdfBlob, `${baseName}.pdf`, 'application/pdf',
    'Done. Note: images and styles from external URLs may not be embedded — keep assets local or inline for the best result.');
}

// Excel to PDF (SheetJS parses the workbook, html2pdf renders the sheets)
async function runExcelToPDF(file) {
  if (typeof XLSX === 'undefined' || typeof html2pdf === 'undefined') throw new Error('The spreadsheet engine failed to load. Please refresh the page and try again.');
  setProgressUI(15, 'Reading workbook...');
  const wb = XLSX.read(await file.arrayBuffer(), { type: 'array' });
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const sheetNames = wb.SheetNames.slice(0, 10);

  let body = '';
  for (let i = 0; i < sheetNames.length; i++) {
    setProgressUI(20 + Math.round((i / sheetNames.length) * 40), `Rendering sheet ${i + 1} of ${sheetNames.length}: ${sheetNames[i]}`);
    const sheet = wb.Sheets[sheetNames[i]];
    if (!sheet || !sheet['!ref']) continue;
    const range = XLSX.utils.decode_range(sheet['!ref']);
    const maxRow = Math.min(range.e.r, 5000);
    const rows = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '', range: [range.s.r, range.s.c, maxRow, range.e.c] });
    let table = '<table style="border-collapse:collapse;width:100%;font-size:10px;font-family:Arial,sans-serif;margin:8px 0 20px;">';
    table += '<thead><tr>' + rows[0].map(h => `<th style="border:1px solid #999;padding:3px 6px;background:#f0f0f0;">${escapeHtml(h)}</th>`).join('') + '</tr></thead><tbody>';
    for (let r = 1; r < rows.length; r++) {
      table += '<tr>' + rows[r].map(c => `<td style="border:1px solid #ccc;padding:2px 6px;">${escapeHtml(c)}</td>`).join('') + '</tr>';
    }
    table += '</tbody></table>';
    body += `<h3 style="font-family:Arial,sans-serif;font-size:14px;">${escapeHtml(sheetNames[i])}</h3>` + table;
  }
  if (!body) throw new Error('No readable sheets were found in this workbook.');

  const container = document.createElement('div');
  container.innerHTML = body;

  setProgressUI(70, 'Building PDF...');
  const pdfBlob = await html2pdf()
    .from(container)
    .set({
      margin: [8, 6, 8, 6],
      image: { type: 'jpeg', quality: 0.95 },
      html2canvas: { scale: 2, logging: false },
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'landscape' }
    })
    .outputPdf('blob');

  setProgressUI(100, 'Processing completed!');
  createDownloadLink(pdfBlob, `${baseName}.pdf`, 'application/pdf',
    `Done. ${sheetNames.length} sheet(s) exported, up to 5,000 rows per sheet. Very wide columns may be split across pages.`);
}

// PDF to HTML (pdf.js text extraction, grouped into readable lines)
async function runPDFToHTML(file) {
  setProgressUI(15, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  let pagesHtml = '';
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(15 + Math.round((i / pdf.numPages) * 75), `Converting page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    const paras = lines.map(l => `<p>${escapeHtml(l)}</p>`).join('');
    pagesHtml += `<section class="page"><h2>Page ${i}</h2>${paras || '<p><em>(no extractable text on this page)</em></p>'}</section>`;
  }
  const doc = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapeHtml(baseName)} — converted from PDF</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;max-width:800px;margin:2rem auto;padding:0 1.25rem;color:#222;line-height:1.6;}
h1{font-size:1.5rem;} h2{font-size:1.1rem;margin-top:2rem;border-bottom:1px solid #ddd;padding-bottom:.3rem;}
p{margin:.4rem 0;} .meta{color:#666;font-size:.85rem;}
</style>
</head>
<body>
<h1>${escapeHtml(baseName)}</h1>
<p class="meta">Converted from PDF in the browser by PDFZaap. Text is extracted in reading order; complex multi-column layouts may not map perfectly.</p>
${pagesHtml}
</body>
</html>`;
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(new TextEncoder().encode(doc), `${baseName}.html`, 'text/html',
    'Done. The HTML preserves text in reading order. Page graphics are not embedded — use PDF to JPG or PDF to PNG for images.');
}

// PDF to EPUB (minimal valid EPUB 3 built with JSZip)
async function runPDFToEPUB(file) {
  if (typeof JSZip === 'undefined') throw new Error('The EPUB builder failed to load. Please refresh the page and try again.');
  setProgressUI(10, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const bookTitle = baseName.replace(/[_-]+/g, ' ');
  const chapters = [];
  const navItems = [];
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(10 + Math.round((i / pdf.numPages) * 70), `Preparing chapter ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    const paras = lines.map(l => `<p>${escapeXml(l)}</p>`).join('');
    chapters.push(`<section epub:type="chapter"><h2>Page ${i}</h2>${paras || '<p>(no extractable text)</p>'}</section>`);
    navItems.push(`<li><a href="c${i}.xhtml">Page ${i}</a></li>`);
  }
  const id = 'zaap-' + Date.now().toString(36);
  const opf = `<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">${id}</dc:identifier>
    <dc:title>${escapeXml(bookTitle)}</dc:title>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">${new Date().toISOString().replace(/\.\d{3}Z/, 'Z')}</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    ${chapters.map((_, i) => `<item id="c${i + 1}" href="c${i + 1}.xhtml" media-type="application/xhtml+xml"/>`).join('\n    ')}
  </manifest>
  <spine>${chapters.map((_, i) => `<itemref idref="c${i + 1}"/>`).join('')}</spine>
</package>`;
  const nav = `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>Navigation</title></head>
<body><nav epub:type="toc"><h1>Contents</h1><ol>${navItems.join('')}</ol></nav></body>
</html>`;
  const xhtmlFor = (i, body) => `<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>Page ${i}</title></head>
<body>${body}</body>
</html>`;

  const zip = new JSZip();
  zip.file('mimetype', 'application/epub+zip', { compression: 'STORE' });
  zip.file('META-INF/container.xml', `<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>`, { compression: 'STORE' });
  zip.file('OEBPS/content.opf', opf);
  zip.file('OEBPS/nav.xhtml', nav);
  chapters.forEach((c, i) => zip.file(`OEBPS/c${i + 1}.xhtml`, xhtmlFor(i + 1, c)));

  setProgressUI(90, 'Packing EPUB file...');
  const blob = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE' });
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(blob, `${baseName}.epub`, 'application/epub+zip',
    'Done. The EPUB is reflowable text — each PDF page becomes one chapter. Graphics are not embedded; use OCR PDF first if your source is scanned.');
}

// PDF to Word (minimal valid DOCX built with JSZip — text-based conversion)
async function runPDFToWord(file) {
  if (typeof JSZip === 'undefined') throw new Error('The DOCX builder failed to load. Please refresh the page and try again.');
  setProgressUI(10, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  let bodyXml = '';
  let pageBreakCount = 0;
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(10 + Math.round((i / pdf.numPages) * 75), `Converting page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    if (i > 1) {
      bodyXml += `<w:p><w:r><w:br w:type="page"/></w:r></w:p>`;
      pageBreakCount++;
    }
    bodyXml += lines.length
      ? lines.map(l => `<w:p><w:r><w:t xml:space="preserve">${escapeXml(l)}</w:t></w:r></w:p>`).join('')
      : `<w:p><w:r><w:t xml:space="preserve">(no extractable text)</w:t></w:r></w:p>`;
  }
  const documentXml = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>${bodyXml}<w:sectPr><w:pgSz w:w="12240" w:h="15840"/></w:sectPr></w:body>
</w:document>`;
  const contentTypes = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>`;
  const rels = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>`;

  const zip = new JSZip();
  zip.file('[Content_Types].xml', contentTypes);
  zip.file('_rels/.rels', rels);
  zip.file('word/document.xml', documentXml);

  setProgressUI(95, 'Packing Word file...');
  const blob = await zip.generateAsync({ type: 'blob', compression: 'DEFLATE' });
  setProgressUI(100, 'Conversion complete!');
  createDownloadLink(blob, `${baseName}.docx`, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'Done. This is a text-based conversion: all words and the reading order are preserved, but multi-column layouts, tables and images are simplified. For pixel-perfect fidelity, export pages as images instead.');
}

// PDF to Excel (pdf.js text lines → SheetJS worksheet)
async function runPDFToExcel(file) {
  if (typeof XLSX === 'undefined') throw new Error('The spreadsheet engine failed to load. Please refresh the page and try again.');
  setProgressUI(15, 'Reading document...');
  const pdf = await pdfjsLib.getDocument({ data: await file.arrayBuffer() }).promise;
  const baseName = file.name.replace(/\.[^.]+$/, '');
  const rows = [];
  for (let i = 1; i <= pdf.numPages; i++) {
    setProgressUI(15 + Math.round((i / pdf.numPages) * 70), `Extracting rows from page ${i} of ${pdf.numPages}...`);
    const page = await pdf.getPage(i);
    const lines = await extractPageLines(page);
    lines.forEach(line => {
      const cells = line.split(/\t|\s{2,}/).map(c => c.trim()).filter(Boolean);
      rows.push(cells.length ? cells : ['']);
    });
    if (i < pdf.numPages) rows.push([]);
  }
  if (!rows.length) throw new Error('No extractable text was found in this PDF.');
  const ws = XLSX.utils.aoa_to_sheet(rows);
  const wb = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb, ws, 'Page text');
  const out = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
  setProgressUI(100, 'Export complete!');
  createDownloadLink(new Blob([out], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }),
    `${baseName}.xlsx`, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'Done. Each text line becomes a spreadsheet row; cells are split where the PDF used tabs or clear column spacing. Complex tables may need a little manual cleanup.');
}

// PDF archival prep (pdf-lib) — embeds long-term-archiving metadata.
// NOT a certified PDF/A conversion (that requires server-side validation tooling); the page copy says so.
async function runArchivalPrep(file) {
  setProgressUI(25, 'Reading document structure...');
  const { PDFDocument } = PDFLib;
  const bytes = await file.arrayBuffer();
  let doc;
  try {
    doc = await PDFDocument.load(bytes, { ignoreEncryption: true });
  } catch (e) {
    throw new Error('This file could not be opened. If it is corrupt, try the Repair PDF tool first.');
  }
  const now = new Date();
  if (!doc.getTitle()) doc.setTitle(file.name.replace(/\.[^.]+$/, ''));
  doc.setSubject('Prepared for long-term archiving');
  doc.setKeywords(['archival', 'long-term storage']);
  doc.setCreator('PDFZaap (client-side archival prep)');
  doc.setProducer('PDFZaap PDF Archival Prep');
  doc.setCreationDate(now);
  doc.setModificationDate(now);
  setProgressUI(80, 'Writing document...');
  const outBytes = await doc.save();
  setProgressUI(100, 'Processing completed!');
  createDownloadLink(outBytes, file.name.replace(/\.[^.]+$/, '') + '_archival.pdf', 'application/pdf',
    'Archival metadata (title, subject, creation/modification dates) has been embedded. Honest note: this is preparation, not a certified PDF/A conversion — full PDF/A validation requires dedicated server-side tooling (see the guide on this page).');
}

// Compare PDFs (pdf.js text extraction + line diff → HTML report)
function diffLines(a, b) {
  const n = a.length, m = b.length;
  // Guard: DP is O(n*m); cap for very large documents
  if (n * m > 9_000_000) return null;
  const dp = Array.from({ length: n + 1 }, () => new Uint32Array(m + 1));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      dp[i][j] = a[i] === b[j] ? dp[i + 1][j + 1] + 1 : Math.max(dp[i + 1][j], dp[i][j + 1]);
    }
  }
  const out = [];
  let i = 0, j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) { out.push({ t: 'eq', s: a[i] }); i++; j++; }
    else if (dp[i + 1][j] >= dp[i][j + 1]) { out.push({ t: 'del', s: a[i] }); i++; }
    else { out.push({ t: 'add', s: b[j] }); j++; }
  }
  while (i < n) { out.push({ t: 'del', s: a[i] }); i++; }
  while (j < m) { out.push({ t: 'add', s: b[j] }); j++; }
  return out;
}

async function runComparePDF(files) {
  if (files.length < 2) throw new Error('Please select exactly two PDF files to compare.');
  if (files.length > 2) throw new Error('Please select exactly two PDF files to compare.');
  setProgressUI(15, 'Reading first document...');
  const pdfA = await pdfjsLib.getDocument({ data: await files[0].arrayBuffer() }).promise;
  setProgressUI(35, 'Reading second document...');
  const pdfB = await pdfjsLib.getDocument({ data: await files[1].arrayBuffer() }).promise;

  const collect = async (pdf) => {
    const all = [];
    for (let i = 1; i <= pdf.numPages; i++) {
      const page = await pdf.getPage(i);
      const lines = await extractPageLines(page);
      lines.forEach(l => all.push(l));
    }
    return all;
  };
  setProgressUI(55, 'Extracting text...');
  const linesA = await collect(pdfA);
  const linesB = await collect(pdfB);

  setProgressUI(75, 'Computing differences...');
  const ops = diffLines(linesA, linesB);
  const additions = ops ? ops.filter(o => o.t === 'add').length : 0;
  const deletions = ops ? ops.filter(o => o.t === 'del').length : 0;

  let rowsHtml;
  if (ops) {
    rowsHtml = ops.map(o => {
      if (o.t === 'eq') return `<tr class="same"><td>${escapeHtml(o.s)}</td></tr>`;
      if (o.t === 'add') return `<tr class="add"><td>+ ${escapeHtml(o.s)}</td></tr>`;
      return `<tr class="del"><td>- ${escapeHtml(o.s)}</td></tr>`;
    }).join('');
  } else {
    rowsHtml = `<p>The documents are too large for a line-by-line diff in the browser. Both text exports are listed below for manual review.</p>`;
  }

  const report = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Comparison: ${escapeHtml(files[0].name)} vs ${escapeHtml(files[1].name)}</title>
<style>
body{font-family:Arial,Helvetica,sans-serif;max-width:900px;margin:2rem auto;padding:0 1.25rem;color:#222;}
h1{font-size:1.4rem;} .meta{color:#555;font-size:.9rem;}
table{width:100%;border-collapse:collapse;font-size:.85rem;font-family:Consolas,Monaco,monospace;}
td{padding:.2rem .5rem;border-bottom:1px solid #eee;white-space:pre-wrap;}
tr.add td{background:#e6f6e6;color:#145214;}
tr.del td{background:#fdecea;color:#7a1f1f;}
.summary{background:#f7f7f7;border:1px solid #ddd;border-radius:8px;padding:1rem 1.25rem;margin:1rem 0;}
</style>
</head>
<body>
<h1>PDF comparison report</h1>
<p class="meta">Document A: ${escapeHtml(files[0].name)} (${pdfA.numPages} pages, ${linesA.length} lines) &middot; Document B: ${escapeHtml(files[1].name)} (${pdfB.numPages} pages, ${linesB.length} lines) &middot; Generated in the browser by PDFZaap</p>
<div class="summary"><strong>Result:</strong> ${ops ? `${additions} added line(s), ${deletions} removed line(s) compared to document A.` : 'Detailed diff unavailable (documents too large).'}</div>
<table><tbody>${rowsHtml}</tbody></table>
</body>
</html>`;
  setProgressUI(100, 'Report ready!');
  createDownloadLink(new TextEncoder().encode(report),
    `${files[0].name.replace(/\.[^.]+$/, '')}_vs_${files[1].name.replace(/\.[^.]+$/, '')}_report.html`, 'text/html',
    `Done. ${ops ? `Found ${additions} added and ${deletions} removed lines.` : 'Opened as an HTML report you can view in any browser.'}`);
}

// ==========================================================================
// INTERACTIVE UI & NAVIGATION HELPERS
// ==========================================================================

function toggleAccordion(trigger) {
  const parent = trigger.parentElement;
  if (parent.classList.contains('active')) {
    parent.classList.remove('active');
  } else {
    parent.classList.add('active');
  }
}

function setupNavbarScroll() {
  const nav = document.getElementById('main-nav');
  const scrollTopBtn = document.getElementById('scroll-top');
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }

    if (window.scrollY > 400) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }
  });
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

  // Close after navigating from the menu
  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setMenu(false));
  });

  // Close when clicking the menu background (not a link)
  menu.addEventListener('click', (e) => {
    if (e.target === menu) setMenu(false);
  });

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setMenu(false);
  });
}

function closeMobileNav(hash) {
  const btn = document.getElementById('hamburger-btn');
  const menu = document.getElementById('mobile-menu');
  if (btn) btn.classList.remove('active');
  if (menu) menu.classList.remove('active');
  window.location.hash = hash;
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
  const query = document.getElementById('tool-search').value.toLowerCase().trim();
  const activeBtn = document.querySelector('.filter-tab.active');
  const activeTab = activeBtn
    ? (activeBtn.getAttribute('data-tab') || activeBtn.textContent.toLowerCase())
    : 'all';
  const cards = document.querySelectorAll('#main-tools-grid .tool-card');

  cards.forEach(card => {
    const title = card.querySelector('h3').textContent.toLowerCase();
    const desc = card.querySelector('p').textContent.toLowerCase();
    const category = card.getAttribute('data-category');

    const matchQuery = !query || title.includes(query) || desc.includes(query);
    const matchTab = (activeTab === 'all' || category === activeTab);

    if (matchQuery && matchTab) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });

  // Hide group sections whose cards are all filtered out
  document.querySelectorAll('#main-tools-grid .tools-group').forEach(group => {
    const anyVisible = Array.from(group.querySelectorAll('.tool-card')).some(c => c.style.display !== 'none');
    group.style.display = anyVisible ? '' : 'none';
  });
}

function applySearchTag(tagText) {
  const input = document.getElementById('tool-search');
  if (input) {
    input.value = tagText;
    runSearchFilter();
    scrollToToolsGrid();
  }
}

function applyFilterTab(tabCategory, btnElement) {
  document.querySelectorAll('#filter-tabs-container .filter-tab').forEach(t => t.classList.remove('active'));
  btnElement.classList.add('active');
  runSearchFilter();
}

// ==========================================================================
// COOKIE & LEGAL MODAL CONTROLS
// ==========================================================================

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

function toggleLegalModal(type) {
  const modal = document.getElementById('legal-modal');
  const title = document.getElementById('modal-title');
  const body = document.getElementById('modal-body');

  if (!modal) return;

  if (!type) {
    modal.style.display = 'none';
    return;
  }

  if (type === 'privacy') {
    title.textContent = "Privacy Policy";
    body.innerHTML = `
      <p style="margin-bottom:1rem;">At PDFZaap, accessible from https://pdfzaap.online, protecting user privacy is our top priority.</p>
      <p style="margin-bottom:1rem;"><strong>100% Secure Client-Side Execution:</strong> All tools provided operate exclusively on your local computer using standard browser scripts. None of your document files, metadata contents, signatures, or personal records are ever uploaded to external servers.</p>
      <p style="margin-bottom:1rem;"><strong>Cookies Policy:</strong> We do not deploy advertising trackers or compile tracking profiles. Simple browser values are kept in local storage solely to remember user system interface preferences.</p>
      <p>Should you have questions regarding these guidelines, please contact us at contact@pdfzaap.online.</p>
    `;
  } else {
    title.textContent = "Terms of Service";
    body.innerHTML = `
      <p style="margin-bottom:1rem;">Welcome to PDFZaap!</p>
      <p style="margin-bottom:1rem;">By accessing this single-page web application, you agree to these Terms of Service. If you do not accept these terms, please discontinue use of the platform.</p>
      <p style="margin-bottom:1rem;"><strong>License &amp; Usage:</strong> PDFZaap provides completely free client-side utility services. There are no registration forms, file count constraints, or monthly fees. The software is provided 'as is' without warranties of any kind.</p>
      <p>All processing calculations run strictly inside your local browser container. You retain full ownership and liability for all documents processed on this platform.</p>
    `;
  }
  modal.style.display = 'flex';
}

// Same-origin entry avoids PDF.js's blob-worker shim, which the site's CSP blocks.
// Keep this version in sync with LIBRARIES.pdfjs and the static page script tags.
importScripts('https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js');

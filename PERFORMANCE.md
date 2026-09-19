# Large-document processing

PDFZaap remains a static, client-side application. No build step or document-upload service is required. Serve the repository over HTTP(S); the new ES modules and workers must be served alongside `script.js` with JavaScript MIME types.

## Execution and ownership

- `script.js` owns form values, a single active job, cancellation, progress and the current download URL. It prevents concurrent submissions, ignores stale job callbacks and revokes old output URLs on replacement, reset, navigation and page exit.
- `processing-client.js` starts a dedicated worker per job. Files are sent as `File` objects, not pre-read and copied `ArrayBuffer`s. Page image/pixel buffers and final output buffers use transferable ownership. Workers are terminated on success, failure and cancellation.
- `processing-worker.js` loads only the required conversion libraries and delegates to the DOM-free `processing-core.js`. PDF-Lib edits/parsing/serialization, image embedding, PPTX XML inflation/text conversion, DOCX-to-HTML conversion, ZIP creation, grayscale pixel conversion and PowerPoint serialization run here.
- `pdfjs-worker.js` is a **same-origin** entry for PDF.js parsing. It avoids the cross-origin blob-worker shim blocked by the existing page CSP. The entry, lazy loader and static PDF.js tags all use version 3.11.174. Keep them in sync when upgrading. PDF.js dynamic evaluation is disabled.
- If workers are unavailable or fail during startup, the same core runs cooperatively on the browser thread. It yields between page batches, every five simple page edits, and between grayscale pixel chunks. A failure **after** work starts is reported, never automatically replayed with another full copy of the input.

### Raster workflow

PDF.js canvas drawing still uses the browser thread for compatibility; its parser runs in the PDF.js worker. Rendering is sequential, with one reusable canvas. Each page is encoded with asynchronous `toBlob()` instead of a data-URL/fetch round trip, sent to the output worker and released before the next page. `page.cleanup()`, zero-sized canvases and loading-task destruction run in `finally` blocks, including on rendering/encoding errors. The source PDF.js document is destroyed **before** final output serialization.

Compression/grayscale use scale 1.25; image and PowerPoint export use 1.5. Dimensions are further reduced to fit the canvas ceilings below. JPEG quality defaults to 0.85 (compression keeps its existing user-controlled quality). PDF output retains the original physical page dimensions, independent of raster resolution. PowerPoint page images are fitted without stretching.

Raster output is still raster output: text/searchability/vector fidelity is not preserved, and a vector-heavy source may become larger. PptxGenJS still requires base64 image strings internally, but they are created and retained in the processing worker rather than the UI.

### Vector and presentation workflow

A PDF is read and parsed once per input. Copying/resizing uses batches of 10 pages and one shared PDF-Lib object copier per source/destination pair. This deliberately uses PDF-Lib's exported `PDFObjectCopier`/`PDFPage` APIs: separate public `copyPages()`/`embedPages()` calls for each batch would duplicate shared images/fonts. Resizing embeds into the destination document's context, never reparses the original bytes or embeds into the source document. Regression tests cover destination references and shared resources across batches.

PPTX slide numbers are extracted once before sorting. Only required slide XML is inflated, serially, through a byte-limited stream. Parsed XML and text are scoped to one slide, and the archive is released before saving the PDF. The existing converter remains **text-only**, not a complete PowerPoint layout renderer.

Normal PDF saves, including flattening, use object streams. Only the repair path explicitly disables them for compatibility. Flattening errors are reported instead of returning an unflattened PDF as success.

### Word and currently unavailable tools

Mammoth DOCX parsing/HTML conversion runs in a worker, which is terminated before DOM construction so its ZIP/parser structures do not coexist with the document canvas. The HTML result also has a size limit. html2pdf layout/rasterization still requires the browser DOM and remains on the browser thread. It uses scale 1.25 and JPEG quality 0.85, measures the attached document after images load, reduces the scale within safe bounds, and rejects overly long documents rather than allocating an unbounded canvas. Its temporary overlay and full-document canvas are released on success/failure. Cancellation takes effect at asynchronous boundaries; it cannot preempt a synchronous DOM-library call.

OCR and several other advertised advanced tools were placeholders in this checkout, not Tesseract processing implementations. They now report that they are unavailable immediately, rather than waiting two seconds and downloading the original bytes with a different extension. Password encryption/decryption is not supported by the pinned PDF-Lib engine; encrypted inputs are rejected rather than reserialized as if they had been decrypted. Adding real OCR with a reused Tesseract worker is a separate feature.

## Safety limits

Constants live in `processing-core.js` (`LIMITS`). Limits use binary megabytes (MiB), labelled MB in the UI.

| Resource | Ceiling |
| --- | --- |
| One input file | 100 MB; 20 MB for Word |
| One multi-file job | 100 files, 200 MB combined |
| Vector/text PDF or text-only PPTX conversion | 2,000 pages/slides (also the aggregate merge output) |
| Raster workflow | 200 pages |
| One PDF page canvas | 4,000,000 pixels and 4,096 pixels per dimension |
| Accumulated encoded raster assets | 100 MB before ZIP/PDF/PPTX serialization |
| Word converted HTML, including embedded images | 8,000,000 characters |
| Word full-document canvas | 8,000,000 pixels and 8,192 pixels per dimension; reject if scale would fall below 0.75 |
| Page selection input | 20,000 characters, 2,000 comma-separated parts |
| PPTX ZIP directory | 10,000 entries |
| PPTX inflated slide XML | 2 MB per slide, 32 MB cumulatively |
| PPTX visible slide text | 20,000 characters per slide |

Page-range endpoints and safe integers are checked before expansion. Overlapping intervals are merged and expanded only once. Reordering rejects duplicate page numbers during parsing, before copying any pages. Progress DOM writes are coalesced to at most one update per 100 ms, with immediate completion/errors and no stale trailing updates.

These are guardrails, **not a guarantee of a fixed peak memory footprint**. PDF-Lib/JSZip/PptxGenJS still retain output structures and serialize complete documents; complex or compressed input objects can require much more memory than their file size. The fallback and DOM-based drawing may still have long individual tasks. Low-memory devices may require smaller files than these ceilings.

## Verification

Node 20+ is required for the tests. Runtime deployment needs none of the npm packages; dev dependencies mirror the site's existing pinned CDN bundles. Their broader dependency/security upgrades are not part of this performance change.

```sh
npm ci
npm test
npx playwright install --with-deps chromium
npm run test:browser
```

`BROWSER_EXECUTABLE=/path/to/chromium npm run test:browser` uses an existing Chromium installation. Browser tests start and close their own static server and intercept CDN URLs with matching local npm fixtures; they don't depend on external CDNs or send document contents anywhere.

Coverage includes bounds/range parsing, duplicate validation, shared-resource preservation, real PDF edits, PPTX decompression limits, object streams, event-loop yielding, throttling, buffer transfer, worker startup/runtime failures, cancellation, fallback, canvas/loader cleanup on errors, and actual browser downloads for resize, grayscale, compression, image/PowerPoint/PPTX and Word conversion. A browser smoke check also exercises the placeholder-tool error and download URL cleanup.

# Trust & legal pages: about, contact, privacy, terms.
# Note: contact email and author name come from the only public identifiers on
# the site (contact@pdfzaap.online in existing copy; GitHub owner handle).
# Owner should confirm both in SEO-CHANGELOG.md before launch.

TRUST = {}

TRUST["about"] = dict(
    title="About PDFZaap — Free Browser-Based PDF Tools | PDFZaap",
    meta="Who makes PDFZaap, why it exists, and how local (client-side) PDF processing works. A free, privacy-first collection of 35 browser-based PDF tools.",
    h1="About PDFZaap",
    schema='''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "AboutPage",
    "mainEntity": {
      "@type": "Organization",
      "@id": "https://www.pdfzaap.online/#org",
      "name": "PDFZaap",
      "url": "https://www.pdfzaap.online/",
      "logo": "https://www.pdfzaap.online/og-image.png",
      "founder": {"@type": "Person", "name": "Abdullah Salim"}
    }
  }
  </script>''',
    body="""<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">What PDFZaap is</h2>
<p>PDFZaap is a free collection of 35 PDF tools that run entirely in your web browser: conversion (PDF to Word, JPG, Excel and more), editing and organization (merge, split, compress, rotate, watermark), security (protect, unlock, e-sign) and advanced operations (OCR, repair, compare, metadata). Everything is free — no account, no subscription, no watermark, no daily limits.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Why it exists</h2>
<p>Most online PDF tools work by uploading your document to a server, processing it there, and deleting it after a stated delay. That model is convenient for the provider and adds a step of trust for you — and for the documents that are most sensitive (contracts, IDs, financial records, client work), that step of trust is exactly what you would rather not take. PDFZaap is built around the opposite decision: <strong>run the processing on the device that owns the document</strong>. Modern browsers can execute real document engines locally, and that makes a fully private, free PDF toolkit possible. If a capability is not possible in the browser (certified PDF/A validation, layout-perfect PDF-to-Word, for example), the relevant tool page says so instead of pretending.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">How local processing works</h2>
<p>When you open a tool page, the browser downloads the page's assets — styles, scripts, and the processing libraries (PDF parsing and manipulation compiled to WebAssembly/JavaScript, image encoding, and for OCR, the Tesseract.js engine). From that moment on, your document takes no network path:</p>
<ul style="margin:0.75rem 0 1rem;padding-left:1.4rem;line-height:1.8;">
  <li>Your file is read from disk by the browser's file API — it never leaves the device.</li>
  <li>The processing libraries read the file in your tab's memory and perform the operation there.</li>
  <li>The result is handed back to you as a download, written to your device by the browser.</li>
</ul>
<p>The only documented exception is the OCR tool's first run, which downloads the public English language model from the Tesseract project's CDN — the same model file every Tesseract user downloads. Your document is not part of that download and is never transmitted. You can verify the no-upload behavior yourself with the Network-tab test described on our <a href="/is-it-safe-to-use-online-pdf-tools.html">privacy explainer</a>.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;" id="team">Who runs it</h2>
<p>PDFZaap is built and maintained by <strong>Abdullah Salim</strong>, an independent developer. The project is open source on <a href="https://github.com/abdullah123salim1-oss/pdf-zaap" rel="noopener">GitHub</a>, where the code for every tool can be inspected — including the client-side processing path described above. Questions, corrections and feature ideas are welcome via the <a href="/contact.html">contact page</a>.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">What we do not do</h2>
<ul style="margin:0.75rem 0 1rem;padding-left:1.4rem;line-height:1.8;">
  <li>We do not store your files — there is no server storage to store them in.</li>
  <li>We do not sell data — there is no third-party advertising or data broker on the site.</li>
  <li>We do not claim capabilities the tools do not have. Each tool page states its real behavior and real limits.</li>
</ul>""",
)

TRUST["contact"] = dict(
    title="Contact PDFZaap — Feedback, Corrections & Ideas",
    meta="Contact PDFZaap: report a bug, request a feature, correct an error in a guide, or ask a privacy question. Email: contact@pdfzaap.online.",
    h1="Contact PDFZaap",
    schema='''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ContactPage",
    "name": "Contact PDFZaap",
    "url": "https://www.pdfzaap.online/contact.html",
    "contactPoint": {
      "@type": "ContactPoint",
      "email": "contact@pdfzaap.online",
      "contactType": "customer support"
    }
  }
  </script>''',
    body="""<p>Questions, bug reports, corrections or feature ideas — email <a href="mailto:contact@pdfzaap.online"><strong>contact@pdfzaap.online</strong></a>.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">What to include</h2>
<ul style="margin:0.75rem 0 1rem;padding-left:1.4rem;line-height:1.8;">
  <li><strong>Bug reports:</strong> which tool, what you expected, what happened, and your browser and device (e.g. "Chrome 126 on Windows 11"). Do not send the contents of any document — a description is enough.</li>
  <li><strong>Corrections:</strong> the page URL and what is wrong. Accuracy of the guides matters more than anything else on this site, and corrections get fixed quickly.</li>
  <li><strong>Privacy questions or requests:</strong> see the <a href="/privacy.html">Privacy Policy</a> for the details of what the site does and does not collect, and how to reach us about data.</li>
  <li><strong>Feature ideas:</strong> what the tool would do and for whom. Local, browser-based ideas fit the project best.</li>
</ul>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">What to expect</h2>
<p>This is a small project. Most messages get a reply within a few days; bug fixes and corrections land in the next update to the site. If you report a bug with a document, please do not paste confidential content into the email — a summary is all that is needed.</p>""",
)

TRUST["privacy"] = dict(
    title="Privacy Policy | PDFZaap",
    meta="Your PDF files are processed in your browser and never uploaded. What PDFZaap collects, cookies, analytics, and how to contact us.",
    h1="Privacy Policy",
    schema='''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "PDFZaap Privacy Policy",
    "url": "https://www.pdfzaap.online/privacy.html",
    "inLanguage": "en"
  }
  </script>''',
    body="""<p><strong>Last updated:</strong> September 19, 2026</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">The short version</h2>
<p>PDFZaap's tools process your files <strong>in your browser</strong>. Your documents are read from your device, processed in your browser's memory, and written back to your device by a download. They are not uploaded to any server, because the site has no file-upload endpoint and no file storage. This is an architectural property of the site, not a policy promise — the processing simply does not have a network path.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">What we do collect</h2>
<ul style="margin:0.75rem 0 1rem;padding-left:1.4rem;line-height:1.8;">
  <li><strong>Your file contents, names and sizes:</strong> never. No tool, no script on the site transmits any part of a document you select.</li>
  <li><strong>Optional event counts:</strong> the site includes a small, privacy-friendly analytics hook (documented in the source). When the site owner enables a provider (GA4 or Plausible), it records only counts and coarse events — for example that a tool was opened or a file was selected — with no file names, document contents, or personal data. Until a provider is configured, no analytics events leave your browser at all. You can inspect the exact events in the <code>ZAAP_ANALYTICS</code> configuration in the site's source code.</li>
  <li><strong>OCR language model download:</strong> the OCR tool, on its first run, downloads the public English language model from the Tesseract project's public CDN (tessdata.projectnaptha.com). That is the same public model file used by every Tesseract deployment; it contains no information about you, and your document is not part of it.</li>
</ul>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Cookies and local storage</h2>
<p>PDFZaap does not set advertising or third-party tracking cookies. It uses one value in your browser's <em>local storage</em> (not a cookie) to remember whether you accepted or declined the cookie banner, so the banner does not repeat. You can remove it any time by clearing your browser's site data; nothing else on the site depends on it.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Advertising</h2>
<p>The site currently serves no advertising and has no ad cookies. If that changes, this policy will be updated before any ad system is enabled.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Third-party services the page loads</h2>
<ul style="margin:0.75rem 0 1rem;padding-left:1.4rem;line-height:1.8;">
  <li><strong>Fonts</strong> (Google Fonts) and <strong>processing libraries</strong> (pdf-lib, pdf.js, Tesseract.js, html2pdf.js, SheetJS, PptxGenJS, Fabric.js, JSZip, Mammoth) are loaded from public CDNs (unpkg, cdnjs, jsdelivr) when you open a page. These are standard public software libraries; the libraries themselves do not receive your documents — they operate on data in your browser.</li>
  <li><strong>Search Console verification</strong>: the homepage carries a Google Search Console verification meta tag used only to verify site ownership for search indexing; it transmits no visitor data by itself.</li>
</ul>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Your rights and requests</h2>
<p>Because the site does not collect personal data through its tools, there is generally nothing to access, correct or delete on our side. If you believe any data associated with you exists (for example, from a contact email you sent us), or if you have any privacy question, contact us at <a href="mailto:contact@pdfzaap.online">contact@pdfzaap.online</a> and we will respond within a reasonable time.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Honest limits</h2>
<p>Client-side processing means the website cannot see or keep your files — it does not mean your device is safe from everything. Your operating system, browser and any software on your machine still have normal access to your files. PDFZaap reduces exposure to the website; it does not replace basic device security.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">Changes to this policy</h2>
<p>If the site's data practices change (for example, enabling an analytics provider or adding advertising), this page will be updated and the 'Last updated' date changed before the change takes effect.</p>""",
)

TRUST["terms"] = dict(
    title="Terms of Service | PDFZaap",
    meta="PDFZaap terms of service: free use of browser-based PDF tools, the 'as is' disclaimer, and limitation of liability. Read before using the tools.",
    h1="Terms of Service",
    schema='''  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "PDFZaap Terms of Service",
    "url": "https://www.pdfzaap.online/terms.html",
    "inLanguage": "en"
  }
  </script>''',
    body="""<p><strong>Last updated:</strong> September 19, 2026</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">1. Use of the service</h2>
<p>PDFZaap provides free, browser-based PDF tools. You may use the tools for any lawful purpose. You are responsible for having the right to process any document you run through the tools — for example, you should only remove a password from a PDF you own or are authorized to modify, and you should not use the tools to bypass access controls on documents you do not have rights to.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">2. Your files stay on your device</h2>
<p>The tools are designed to process files entirely in your browser. You retain full ownership of any document you process. Because the site has no file storage, we cannot recover a file for you after you close the page — keep your own copies of anything important.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">3. The service is provided 'as is'</h2>
<p>The tools are provided without warranties of any kind, express or implied, including but not limited to merchantability, fitness for a particular purpose, or non-infringement. We do not warrant that every document will convert, compress, or repair successfully — PDF files vary widely, and the tool pages describe each tool's real capabilities and limits. Output files may differ from your expectations, particularly for conversions (for example, PDF-to-Word is a text-based conversion) and for repairs of damaged files. Always check the result before sending a processed document anywhere, and keep your original file until you are confident in the output.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">4. Limitation of liability</h2>
<p>To the maximum extent permitted by law, PDFZaap and its author shall not be liable for any damages — direct, indirect, incidental, consequential, or otherwise — arising from your use of, or inability to use, the site or its tools, including lost data, lost profits, or documents that do not meet a third party's requirements. Your remedies for problems with the software are to stop using it or to report the problem via the <a href="/contact.html">contact page</a>.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">5. Third-party libraries and CDNs</h2>
<p>The site loads publicly available software libraries from public CDNs, and the OCR tool may download a public language model. These components are governed by their own licenses and terms; your use of them is subject to those terms. We do not control third-party CDNs, and their availability may affect the tools.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">6. Changes to the terms</h2>
<p>These terms may be updated from time to time; the 'Last updated' date above reflects the current version. Continued use of the site after a change constitutes acceptance of the updated terms.</p>

<h2 style="color:var(--text);font-size:1.3rem;margin:1.75rem 0 0.75rem;">7. Contact</h2>
<p>Questions about these terms can be sent to <a href="mailto:contact@pdfzaap.online">contact@pdfzaap.online</a>.</p>""",
)

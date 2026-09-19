# Off-page & launch copy — PDFZaap

Drafts for owner use. All of these are written to disclose affiliation where
required, make no ranking/traffic claims, and name no competitors.

Rules baked into every draft:
- No purchased links, PBNs, or comment/forum spam — only real launches,
  directories that allow free submissions, and communities where the project
  is genuinely on-topic.
- Affiliation disclosed in every community/launch post ("I built this").
- No "best #1" claims; the one factual claim is the architecture: files are
  processed in the browser and never uploaded.

---

## 1. Product Hunt — Launch (main post)

**Title:** PDFZaap — 35 free PDF tools that run in your browser (no uploads)

**Tagline:** Compress, merge, convert, sign and repair PDFs without your file
ever leaving your device.

**Description:**
PDFZaap is a free toolkit of 35 PDF tools — compress, merge, split, convert
(PDF↔Word/JPG/Excel and more), protect, e-sign, OCR and repair. The part I
care most about: every tool runs client-side. Your file is read by your
browser, processed in your tab's memory, and written back as a download.
There is no upload endpoint, no account, no watermark, and no limit on uses.

If you want to verify the no-upload claim yourself: open DevTools → Network,
select a file, run a tool, and watch — no requests carry your document. The
same test is written up on the site's privacy explainer, and the code is
public on GitHub (link in the comments) so the processing path can be
audited directly.

Honest limitations, because they matter: PDF-to-Word is a text-based
conversion (complex layouts won't be pixel-perfect), and the OCR tool
downloads a public English language model on first use — stated on the tool
page, never your document.

I built and maintain this. Feedback, bug reports, and "you should add X"
ideas all welcome below.

**First comment (from the maker):**
I'm Abdullah, the maintainer. A few things worth knowing:

- The repo is public: github.com/abdullah123salim1-oss/pdf-zaap — the
  processing code for every tool is in there (pdf.js + pdf-lib + Tesseract.js
  for OCR, running in your browser).
- The privacy explainer walks through a 5-minute DevTools test you can run on
  *any* online PDF tool to see whether it uploads your file:
  https://www.pdfzaap.online/is-it-safe-to-use-online-pdf-tools.html
- If a tool misbehaves on your document, please report it with the tool name
  and browser — not the document itself.

Disclosure: I built PDFZaap; all links here are mine.

---

## 2. Show HN

**Title:** Show HN: PDFZaap – 35 PDF tools that run entirely in your browser

**Body:**
I built PDFZaap: https://www.pdfzaap.online

It's 35 free PDF tools (compress, merge, split, convert to/from Word/JPG/
Excel/PPT, watermark, protect, e-sign, OCR, repair, compare, and more). The
design constraint I care about: all processing is client-side. pdf.js reads
and renders, pdf-lib writes, Tesseract.js does OCR — in the browser. Files
are read via the file API, processed in tab memory, and exported through
`URL.createObjectURL`. There is no upload endpoint on the site at all.

Why I think the local-only constraint is worth having:
- Sensitive documents (IDs, contracts, payroll) don't depend on a third
  party's retention policy.
- The site works offline-ish once loaded (CDN caches permitting) and on
  networks that block file-upload services.
- The architecture is verifiable: Network tab → no file traffic. The site
  has a guide with the exact 5-minute test.

Trade-offs I'll state up front:
- Re-rendering-based compression rasterizes pages (text no longer
  selectable) — the tool says so on the page.
- Browser PDF-to-Word is text-extraction quality, not layout-perfect.
- OCR downloads a ~public English model from the Tesseract CDN on first use
  (documented on the tool page and in the privacy policy).

Stack: plain HTML/CSS/JS, no build step, static hosting. The repo is public
if anyone wants to audit the processing path:
github.com/abdullah123salim1-oss/pdf-zaap

Feedback welcome — especially "this tool did the wrong thing on my file"
reports (tool + browser is enough; please don't paste document content).

Disclosure: I'm the author; the links are mine.

---

## 3. Dev.to article pitch (short)

**Title:** Building a 35-tool PDF suite that never uploads a file

**Outline (expand to a 1,000–1,500 word post):**
1. The problem: online PDF tools = upload trust; most users can't tell the
   architectures apart.
2. The constraint: make "no upload" an architectural fact, not a policy
   promise — no endpoint, no storage, nothing to leak.
3. How: pdf.js (read/render), pdf-lib (write), Tesseract.js (OCR); canvas
   re-encode for compression with an honest "target not reachable" report.
4. Hard parts: target-size compression quality search; A4 image centering
   without upscaling; why browser PDF→Word is text-based.
5. Verifiability: the 5-minute Network-tab test (link to the site's guide).
6. Limits I refuse to hide: rasterized text after compression, OCR first-run
   model download, no certified PDF/A validation.
7. What I'd do next (open to suggestions).

Disclosure line in post footer: "I built PDFZaap (pdfzaap.online); links are
my own."

---

## 4. Directory submissions (free tiers only)

For each: fill in name, URL, category, and the one-line description.
No paid placements.

| Directory (example) | Category | One-liner |
|---|---|---|
| AlternativeTo (free submit) | PDF tools / Office | Free browser-based PDF toolkit; 35 tools; files processed locally, never uploaded |
| Toolify / Futurepedia-type AI/tool directories (free tier) | Productivity / Document tools | 35 free PDF tools that run in your browser with no file uploads |
| Product Hunt (via the launch above) | Developer Tools / Productivity | see launch post |
| SaaSHub / There's An AI For That (if free submit) | Document processing | Client-side PDF compression, conversion, editing — no account, no watermark |

Consistent description for all:
"PDFZaap is a free, browser-based collection of 35 PDF tools — compress,
merge, split, convert, sign, protect, OCR, repair. All processing happens in
your browser; files are never uploaded to a server. No account, no watermark,
no limits. Open source."

---

## 5. Community posts (with disclosure, on-topic subreddits/forums)

Use only where PDF/document tooling is on-topic. Post the *useful part*
(the knowledge), with the tool mentioned as one option — never paste the
same text into multiple places.

**Template A — r/Adobe, r/PDF, r/MSOffice-style "how do I shrink a PDF" threads (reply, not post):**
> Quick one: if your document isn't sensitive, anything works. If it is
> (contracts, IDs, financials), one option is a fully local tool — I built
> one (PDFZaap, free, files never leave the browser):
> https://www.pdfzaap.online/compress-pdf.html
> The general trick regardless of tool: a photo is almost always the size
> problem — export the headshot/photo smaller and the file often drops most
> of the way.
>
> Disclosure: I'm the maintainer of PDFZaap.

**Template B — privacy-focused community (r/Privacy, security forums):**
> Thread-relevant: if you want to check whether *any* online PDF tool
> uploads your file, there's a 5-minute DevTools test: Network tab →
> select a throwaway file → process → look for a POST carrying your file
> (server tool) vs. no new requests (local tool). I wrote it up with
> screenshots of both patterns:
> https://www.pdfzaap.online/is-it-safe-to-use-online-pdf-tools.html
> The site itself is one example of the local architecture (open source:
> github.com/abdullah123salim1-oss/pdf-zaap).
>
> Disclosure: I built that site.

**Template C — show/build threads (r/SideProject, Indie Hackers, X build-in-public):**
> Built PDFZaap: 35 PDF tools, all client-side (pdf.js + pdf-lib +
> Tesseract.js). The fun problem was target-size compression — searching
> for the best quality that fits a hard limit (e.g. "under 200 KB") and
> reporting honestly when the limit isn't reachable for that document.
> Feedback on the OCR tool especially welcome (it's the one with a
> first-run model download, which I document).
> https://www.pdfzaap.online — disclosure: I'm the author.

**Never:** comment-spam on unrelated threads, buy "top comment" packages,
create accounts solely for link posting, or post the same text verbatim in
multiple places.

---

## 6. Outreach emails (partnerships/content only, no link requests)

**Template A — PDF-adjacent newsletter (e.g. document-workflow newsletters):**
Subject: A browser-only PDF toolkit (no uploads) — would your readers care?

> Hi [name],
>
> I'm Abdullah Salim, maintainer of PDFZaap (pdfzaap.online) — a free
> collection of 35 PDF tools where all processing runs in the browser, so
> files are never uploaded. I'm reaching out because [their newsletter]
> regularly covers document workflows, and the "no upload" angle (plus a
> 5-minute test readers can run to verify *any* tool's upload behavior)
> seems like a fit for a brief feature or resource-list mention — not
> advertising, just a resource.
>
> Happy to provide: the privacy explainer URL, the public repo, or a
> sample test walkthrough for your readers.
>
> Best, Abdullah Salim — https://www.pdfzaap.online

**Template B — education/careers resource page (CV upload limits):**
Subject: Resource on fitting CVs under 200 KB upload limits

> Hi [name],
>
> I maintain PDFZaap (pdfzaap.online). Many of your readers hit "file must
> be under 200 KB" on job portals; we wrote a practical guide on fitting a
> CV under that limit (size budget, photo handling, what rejections usually
> mean): https://www.pdfzaap.online/blog/compress-pdf-under-200kb-job-application.html
>
> If it's useful for a resources page or newsletter, it's free to link.
> No strings — and no, I don't need a specific placement.
>
> Best, Abdullah Salim

**Template C — open-source/developer blog (guest post offer):**
Subject: Guest post idea: verifying no-upload behavior in browser tools

> Hi [name],
>
> I write about the architecture of client-side document tools (I built
> PDFZaap, a 35-tool PDF suite that processes files entirely in the
> browser). I'd be glad to write a guest post for [their blog] on
> verifying upload behavior in web tools with DevTools — a practical,
> testable writeup with reproducible steps. Draft outline available on
> request.
>
> Best, Abdullah Salim

---

## 7. Link-earning notes (what we do NOT do)

- No link packages, PBNs, guest-post farms, or "submit to 500 directories"
  services.
- No paid placements in tool directories (free tiers only).
- No self-voting or engagement manipulation on Product Hunt/HN.
- Community value first: the DevTools test guide and the compression guides
  are the linkable assets; the tool pages follow.
- Every mention in a community context carries the disclosure: "I built
  this / I'm the maintainer."

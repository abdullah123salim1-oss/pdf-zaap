# `/pdf-to-word.html` — Semrush On-Page SEO Checker: disposition & shipped changes

> Date: 2026-09-25 · Branch: `arena/01a0d874-pdf-zaap` · Page audited: https://www.pdfzaap.online/pdf-to-word.html
> Report fingerprint: `fid=12235390` · Checker project: 30034895
> Benchmark: the page's "top 10-ranking rivals" set supplied by Semrush (iLovePDF, Smallpdf, PDF24, Adobe, SodaPDF, …).

Every line of the report is dispositioned below. Nothing was applied blindly: two of the
six recommendations are **declined or re-scoped**, with the reason stated, because acting on
them as written would either publish a false claim or buy a rich-result feature this site is
not eligible for.

---

## 0. Scorecard

| Section | Report verdict | Our action | State |
|---|---|---|---|
| **St** Strategy | "no improvements", no keyword cannibalization | none needed | ✅ closed |
| **Sf** SERP Features | "Mark up your aggregate rating" | **declined** — see §1 | ⛔ declined with reason |
| **Co** Content | 11 checks, all pass | none needed (title/meta/H1 untouched) | ✅ closed |
| **Se** Semantic | 17 related words missing → "Enrich your page content" | **adopted** — all 17 covered, +600 words, engine-verified | ✅ shipped |
| **Ba** Backlinks | 17 domains to earn links from | **re-scoped** — see §3 | 🔶 owner action, filtered |
| **Te** Technical | all pass | none needed | ✅ closed |

Verification after the change: `npm run audit:seo` **PASS 80/80**, `npm run audit:a11y` **0 new
violations** (the one reported violation is pre-existing, on `what-is-a-pdf.html`),
`npm test` **37/37**, all three JSON-LD blocks parse, `pdf-to-word.html` is byte-identical to
`python3 scripts/gen_tool_pages.py` output (generator ↔ file back in sync — see §4).

---

## 1. SERP Features — "add an aggregate rating": declined, and what would change that

Semrush's suggestion: *"You may increase your click-through rate if you add an aggregate rating
to this page using the WebPage markup code."*

**Not implemented. Three independent reasons:**

1. **There is nothing to mark up.** `/pdf-to-word.html` shows zero reviews and zero ratings, and
   the site has no review-collection mechanism. Review/`aggregateRating` markup must describe
   content that is visible on the page; a rating that exists only in JSON-LD is fabricated data.
   The previous SEO engagement removed the site's star ratings and named testimonials for exactly
   this reason (`SEO-CHANGELOG.md` §S5 — "Removed named testimonials + star ratings").
2. **Self-serving rule.** Google does not display review rich results when the entity being
   reviewed controls the reviews on its own site — a rating PDFZaap gives PDFZaap on
   pdfzaap.online is the textbook case (guideline introduced September 2019, restated in the
   December 2025 review-snippet documentation update). So even a *real* on-page rating of the
   company would not earn the stars; the exception is ratings of a distinct *product/service*
   entity built from genuine user reviews.
3. **The downside is asymmetric.** Ineligible-but-honest markup is simply ignored; markup that
   overstates or invents is "misleading structured data" and is a documented manual-action
   trigger — which would cost rich results site-wide, on a domain with ~0 authority that cannot
   afford the trust hit.

**What would make it worth doing (owner prerequisite list, in order):**

- [ ] Get reviews on a platform Google treats as independent: Product Hunt launch
      (`seo-deliverables/off-page-copy.md` has the ready-to-post copy), G2 / SaaSWorthy /
      AlternativeTo listings, a TrustedShips-style widget is **not** needed.
- [ ] Publish ≥ 5 genuinely user-written reviews on a real page (`/reviews.html`), each with
      author name, date and the reviewed product, and keep them updated — never write them
      ourselves, never seed the count.
- [ ] Only then mark up `SoftwareApplication` (not `Organization`, not the `WebPage`) with
      `aggregateRating` + nested `review` objects, and validate with the Rich Results Test.
- [ ] Note the honesty constraint: ratings collected only from our own audience are still
      self-selected; the copy must say so ("reviews from PDFZaap users").

**The SERP work we did do instead — extractability, which this page *can* win.**
The report also says: *"If there is a high probability that your page may appear in a featured
snippet, we'll tell you how to improve your chances."* No probability was reported, so the
snippet fight is ours to set up:

- A **49-word quick-answer block** (`.quick-answer`, the same pattern that shipped on
  `/what-is-a-pdf.html`) answering "how do I convert a PDF to a Word document?" in step form,
  directly under the tool and above the fold. Google's featured snippets run ~40–60 words; the
  block is a single self-contained paragraph, which is what both the classic snippet and AI
  Overviews lift.
- A **"what the conversion keeps / drops" table** with `scope="col"` + `scope="row"` headers —
  table-snippet eligible for "does pdf to word keep formatting" style queries.
- The `FAQPage` markup is **kept** (it is still parsed for comprehension and cited by AI answer
  engines) but it is no longer a SERP feature: Google restricted FAQ rich results to
  authoritative government/health sites in August 2023 and removed them entirely on 7 May 2026.
  That applies to all 35 tool pages, not just this one — it is why the plan does not spend more
  schema effort here. Do not add FAQ/HowTo markup to new pages *for SERP purposes*; keep it for
  extraction and machine reading.

---

## 2. Semantic — all 17 related words, none of them bolted on

The report asked for these 17 terms (competitor-derived). Counts below are case-insensitive
substring counts on the rendered visible text of `<main>` (site footer excluded), same method
before and after:

| Term | Before | After | Where it landed |
|---|---|---|---|
| word converter | 0 | 3 | step 3, FAQ (scanned), "Nothing to unlock" |
| pdf to word tool | 0 | 1 | intro |
| microsoft word | 0 | 5 | intro, step 4, tip, FAQ ×2 |
| editable word documents | 0 | 2 | intro, "when to use" |
| converting pdf | 0 | 1 | "Nothing to unlock" paragraph |
| google docs | 2 | 4 | step 4, tip, FAQ ×2 |
| convert scanned | 0 | 1 | tip |
| click convert | 0 | 1 | step 2 heading "Click Convert to Word" |
| convert pdfs | 0 | 1 | "when to use" |
| free pdf to word | 0 | 2 | intro, FAQ |
| word formats | 0 | 2 | tip, FAQ |
| unlocks unlimited | 0 | `unlock` 0→4, `unlimited` 0→2 | "Nothing to unlock" paragraph + FAQ (used only to say no paywall exists) |
| pdf to word conversion | 0 | 2 | "Privacy first", FAQ |
| word file | 4 | 4 | retained (step 4 heading, tips, FAQ) |
| scanned pdfs | 1 | 4 | tips, FAQ, table |
| pdf tools | 1 | 1 | already present ("Related PDF Tools", "Nothing to unlock") |

17/17 covered, 0 forced. Visible body copy went **739 → 1,339 words** (the site's tool-page band
is 600–950; this page is a deliberate exception as one of the four Tier-1 hero pages —
`seo/SEO-STRATEGY.md` §2 — and its sibling intent page `/pdf-to-word-without-losing-formatting.html`
was already 1,030).

**Three terms were handled as truthful-adjacent rather than literal.** "unlocks unlimited" is a
competitor paywall phrase (`upgrade to unlock unlimited conversions`); it appears here only as a
statement that no such paywall exists. "click convert" is the real button label, so it is used in
step 2 as `Click Convert to Word`. "word formats" is answered with the actual formats involved
(`.docx` out, `.doc` not produced), not as a generic phrase.

**Accuracy debt found and fixed while writing** (every claim re-checked against the engine in
`processing-advanced.js` / `processing-core.js` before it went in):

| Old copy | Problem | New copy |
|---|---|---|
| FAQ: "There is no imposed limit." | **False.** `validateFiles` caps the file at `LIMITS.maxFileBytes` (100 MB) and `validatePageCount` caps `pdf.numPages` at 2,000; `extractPageLines` throws when extracted text exceeds the `maxRasterBytes` text guard. | FAQ now states 100 MB / 2,000 pages / "split it" behaviour, and frames them as device-memory guards, not a paywall. |
| Step 3: "groups the words into lines and paragraphs" | `extractPageLines` buckets text items by rounded baseline Y and emits **one `<w:p>` per visual line** — no paragraph reconstruction. | "reads each page's text layer, joins the words that share a line, and writes one Word paragraph per line." |
| Intro: "paragraph order" | The order is **reading order by Y position**; the paragraph structure is per line. | "editable text in reading order", plus a table row explaining that same-height columns merge into one line. |
| Engine completion note: "tables and images are simplified" | Images are **not** in the output at all (`runPDFToWord` writes text runs only). | New table states plainly: images/charts/signatures → nothing; fix with `/pdf-to-jpg.html`. |
| `llm.txt`: "Convert PDF to editable DOCX documents, preserving layout and formatting" | Flatly wrong for this engine, and it is the file AI answer engines quote. | Rewritten: words and reading order preserved; fonts, styles, tables and images not carried over; scans need OCR first. Same treatment for the `/pdf-to-excel.html` line ("Extract PDF tables" → line-based, not table detection) and for the Mac-guide blog line ("full layout and table preservation" → what the post actually teaches). |

Two new FAQs carry the same load as keywords: "Will my fonts, bold text and headings survive the
conversion?" and "Which Word formats will open the downloaded file?" — both honest, both
PAA-shaped, both things a user of this exact tool needs before they start.

---

## 3. Backlinks — 17 suggested domains, most of them a liability

Semrush lists the rivals' referring domains and says "earn links from more sources". Sorted by
what they actually are:

| Class | Domains from the list | Verdict |
|---|---|---|
| Not acquirable — they *are* products/platforms | `bing.com`, `yahoo.com`, `wps.ai`, `signnow.com`, `glarity.app`, `dochub.com` | A link here requires a real partnership, listing or editorial mention. Nothing to "optimise". Bing/Yahoo arrive via Webmaster Tools submission, not links. |
| Link farms / low-quality directories | `pakmcqs.com.pk`, `bookshub.co.in`, `blogsky.com`, `bagofnothing.com`, `growthzoneapp.com` | **Do not pursue.** Bulk directory/comment links from MCQ farms and free-blog hosts are the pattern spam brainlifts penalize; on a zero-authority domain they are net negative. |
| Foreign public bodies, unrelated to us | `camarauniaopaulista.sp.gov.br`, `camaramacaubal.sp.gov.br` (Brazilian town councils), `tyc.edu.tw` (a Taiwanese college), `srch.fi`, `tidsmagasinet.se`, `violet.vn` | These links exist because competitors have localized pages and regional partnerships. We have 4 localized pages; an unsolicited .gov/.edu pitch in Portuguese or Chinese to a municipal council is a wasted week with a spam-report downside. Pursue only if a genuinely relevant resource need appears. |
| Actually worth doing | — | Everything in `seo-deliverables/off-page-copy.md` (Product Hunt, Show HN, Dev.to, free-tool directories) — **none of it has been published yet.** |

**The honest read of this module:** this page's constraint is not on-page content, it is that the
domain has ~0 referring domains and nothing has been launched. The checker cannot fix that; the
owner's 90-day plan does. No link was bought, requested from a farm, or exchanged.

---

## 4. How the page was changed (so it survives the next regen)

Tool pages are generated. `pdf-to-word.html` was therefore changed at the source and re-rendered,
not hand-patched:

1. `scripts/content_convert.py` → `C["pdf-to-word"]` (intro + quick answer, 4 steps, `why` with
   the keeps/drops table, 6 tips, `when`, 6 FAQs — FAQ HTML and `FAQPage` JSON-LD both render from
   the same list, so they cannot drift).
2. `scripts/templates.py` → `footer()` now emits the `/what-is-a-pdf.html` "What Is a PDF?" link.
   It had been added to 78 pages by hand in the previous session; without this the next
   regeneration would have silently deleted every one of them.
3. `style.css` → `.quick-answer`, `.table-scroll`, `.post-table` promoted from the inline block on
   `what-is-a-pdf.html` into the shared stylesheet (page-local rules still win by cascade order,
   so the guide pages render exactly as before).
4. `python3 scripts/gen_tool_pages.py` for this page only — sibling pages were deliberately not
   re-rendered, because of the pre-existing drift below.

**Known drift, not caused and not fixed here:** the other 34 generated tool pages still differ from
generator output by one attribute (`aria-label="Choose file to upload"` on disk vs
`"…to process"` in `templates.py`, left over from the a11y pass) and the extra blank line around
the file input. `pdf-to-word.html` now follows the template ("process" — also the more accurate
label for a tool that uploads nothing). Someone should decide the label once and regenerate all 35.

**Regenerating `sitemap.xml` with `scripts/gen_sitemap.py` would reset every lastmod to the
2026-09-19 release date** (the script's single `SITE_DATE`), including the 2026-09-23 dates from
the last session. `/pdf-to-word.html`'s lastmod was hand-bumped to 2026-09-25 to match the real
content change; fix the script before the next full regen.

---

## 5. What to measure next (before touching this page again)

- Google Search Console, `/pdf-to-word.html` only: impressions and average position for
  `pdf to word`, `convert pdf to word`, `pdf to word free`, `pdf to word converter`; and whether
  any query starts returning the page in the snippet slot (position 0) after re-crawl.
- CTR before/after on the page's three head queries over 4+ weeks — one page, small numbers, so
  treat anything under ~15 % relative change as noise.
- Request a re-crawl of the URL in GSC after deploy (the page changed materially today).
- Do **not** re-run the checker for another 4–6 weeks: it will report the same backlink module and
  the aggregate-rating suggestion, and both answers are already on this page.

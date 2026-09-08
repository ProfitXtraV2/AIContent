# Content Publisher — Design Spec

**Goal:** Let a target website repo automatically pull approved articles from the generic
AIContent factory, render them into the site's own brand-aligned HTML (with internal
backlinks), audit them for SEO, and deploy them live on a schedule — while AIContent itself
stays brand/target-agnostic.

**Status:** Approved design (2026-09-08). Next step: implementation plan (writing-plans).

---

## 1. Overview & principles

Two repos, one contract:

- **AIContent (producer, generic):** already writes/reviews SEO articles. It gains ONE new,
  brand-agnostic thing — a **`published/` feed** exposing approved articles (markdown +
  metadata + images) for any consumer to pull. It knows nothing about any target site.
- **Target site repo (consumer/deployer)** — first target: `ProfitXtraV2/WebPortals`,
  site `VsichkiKazina` (hand-built static HTML, deployed by manual FTP upload today). It gains
  a **scheduled AI-agent publisher** that pulls the feed, renders each article into the site's
  template, brand-aligns it, adds internal backlinks, runs a Gemini SEO inspection, commits,
  and FTP-uploads to production.

Design tenets: keep the producer generic; put all site-specific logic in the target; make the
page **chrome deterministic** (template) and reserve the **AI agent for judgment** (brand
voice, internal links, SEO fixes); every run is idempotent and safe to re-run.

## 2. The contract — `published/` feed (in AIContent)

When an article's content PR is approved and merged, a deterministic step promotes it to the
feed on `main`:

```
published/
  index.json                     # manifest: array of entries (see schema)
  <slug>/
    article.md                   # the final body (markdown)
    meta.json                    # per-article metadata (schema below)
    images/…                     # the article's images (svg/webp), as referenced
```

**`meta.json` schema (the contract — stable, versioned):**

| field | type | notes |
|---|---|---|
| `schema_version` | int | contract version (start at `1`) |
| `slug` | string | url-safe id, stable |
| `title` | string | H1 / title tag base |
| `meta_description` | string | ~120–160 chars |
| `body_path` | string | `article.md` (markdown) |
| `author` | string | `Георги Тодоров` |
| `date_published` | string | ISO date |
| `date_modified` | string | ISO date |
| `keywords` | string[] | target keywords |
| `images` | array | `{path, alt}` per image |
| `section_hint` | string | e.g. `blog` (routing hint; consumer decides final path) |
| `content_hash` | string | sha256 of body+meta; drives idempotency |
| `status` | string | `approved` (only approved articles appear in the feed) |

`index.json` lists every entry with `slug`, `title`, `date_modified`, `content_hash`,
`status` so a consumer can diff cheaply without reading every article.

**Producer component:** `scripts/build_feed.py` (deterministic, stdlib-only) — reads the
approved/merged articles + board, writes `published/` and `index.json`. Runs after approval
(hook into the existing flow or a tiny scheduled step). Unit-tested for schema stability.

## 3. Target publisher (in `WebPortals/VsichkiKazina/_publisher/`)

A **scheduled AI-agent** (cloud routine) orchestration doc `publish-run.md` drives each run:

0. **Sync the target repo FIRST.** Before any change, `git checkout main` and
   `git pull --no-rebase origin main` on the WebPortals repo so rendering/committing starts
   from the latest live state (the site may have hand edits). Abort the run cleanly if the
   pull fails or the tree is dirty — never build on a stale/conflicted base. All later commits
   use the pull-then-push pattern to survive races.
1. **Pull the feed.** Fetch `published/index.json` + any new/changed `<slug>/` from the public
   AIContent repo (raw/API). "New/changed" = `content_hash` differs from `.published-state.json`.
2. **Render each article (hybrid):**
   - **Chrome = deterministic template.** Fill `templates/blog-post.html` (extracted from a
     real post) with head/meta/canonical/OG, **JSON-LD Article + BreadcrumbList**, site
     header/nav, footer. No LLM free-forming the scaffold → zero structural drift.
   - **Body = agent, brand-aligned.** Convert `article.md` → HTML in the site's classes and
     align to `brand-book.md` (voice, terminology, RG/disclosure). **Preserve every number,
     link, RG line, disclosure, date, and byline;** never fabricate.
   - **Internal backlinks = agent.** Using the **link map** (built from the live `sitemap.xml`
     + each page's title/H1), insert **3–6 contextual links**: natural anchors, **≥1 to a
     category/money page**, only to pages that exist (validated), no duplicate targets, no
     over-linking.
   - Copy images into the site (`blog/<slug>/images/` or `/assets/...`) and rewrite paths;
     keep descriptive filenames + Bulgarian alt.
   - Route to `blog/<slug>/index.html` (v1; `section_hint` may route others later).
3. **Update site indexes.** Add the post to `blog/index.html` listing and to `sitemap.xml`.
4. **🔎 Gemini SEO inspection (of the rendered HTML).** Send the built page to the Gemini API
   with an SEO-audit prompt: title tag length (~≤60), meta description (~120–160), exactly one
   H1 + logical H2/H3 order, primary-keyword coverage without stuffing, internal links present
   & non-broken, image `alt` present, valid JSON-LD Article/Breadcrumb, canonical + OG present,
   readability, no thin content. Returns a **0–100 SEO score + concrete fixes**.
   - **PASS ≥ `SEO_TARGET` (80)** → proceed to deploy.
   - Else apply **safe fixes only** (title/meta/headings/alt/link anchors — never facts/RG/
     numbers) and re-inspect, up to `MAX_SEO_PASSES` (2); **keep the best-scoring version**.
   - **Hard block FTP** if the final page fails a floor (score < 60) OR has an integrity fault
     (broken internal link, missing canonical/H1, unresolved `[VERIFY]`). Leave it staged +
     logged for a human.
   - **Graceful skip:** if Gemini is unavailable, deploy anyway with a logged warning (don't
     let detector downtime halt all publishing) — unless a non-Gemini integrity check fails.
5. **Commit** the rendered files to WebPortals (audit trail / versioning).
6. **FTP-upload** only the changed files to production (`ftplib`/`lftp`, creds from secrets).
7. **Update `.published-state.json`** (slug → content_hash → deployed timestamp).

## 4. Components

**AIContent (producer):**
- `scripts/build_feed.py` + `published/` tree + `published/index.json` + a short schema doc.

**Target (`WebPortals/VsichkiKazina/_publisher/`):**
- `brand-book.md` — derived from the live site (CSS/tone/terminology/RG/disclosure/linking
  policy) and codified; the agent aligns to it every run.
- `templates/blog-post.html` — chrome template extracted from an existing post, with
  placeholders (`{{title}}`, `{{meta_description}}`, `{{jsonld}}`, `{{body}}`, `{{date}}`, …).
- `link-map.json` (regenerated each run from `sitemap.xml` + titles) — backlink candidates.
- `publish-run.md` — the agent orchestration (the run in §3), the analogue of `daily-run.md`.
- `seo_inspect.py` — calls Gemini with the SEO-audit prompt (stdlib urllib; graceful exit 2);
  `prompts/seo-inspect.md` holds the verbatim prompt + accept/iterate policy.
- `deploy_ftp.py` — uploads changed files via FTP (creds from env secrets); dry-run flag.
- `.published-state.json` — idempotency state.
- A **scheduled cloud routine** (RemoteTrigger) pointed at WebPortals, running `publish-run.md`.

## 5. Data flow

```
AIContent: article PR approved → merged
        → build_feed.py → published/<slug>/ + index.json on main   (generic feed)
Target (scheduled): pull feed → diff vs state
        → render (template chrome + brand body + backlinks) → update index/sitemap
        → Gemini SEO inspect (fix ≤2, keep-best, block on hard fail)
        → commit WebPortals → FTP upload → update state
```

## 6. Error handling & safety
- **Idempotent:** content-hash state; only new/changed articles render/upload.
- **Never deploy broken:** render/validation failure, broken internal link, missing
  canonical/H1, unresolved `[VERIFY]`, or SEO score < floor → stage + log, skip FTP.
- **Dry-run mode:** render + commit, skip upload — used for first runs and template tuning.
- **Secrets:** FTP host/user/pass and `GEMINI_API_KEY` are target-environment secrets, never
  committed. A `hold` flag pauses publishing without disabling the routine.
- **No fabrication:** the agent may re-style and link, never invent facts/numbers/offers.

## 7. Testing
- `build_feed.py`: unit tests for the `meta.json`/`index.json` schema (stability = the contract).
- Renderer: tests that the template fills with no leftover `{{placeholders}}`, exactly one H1,
  backlink count within 3–6, and all inserted links resolve to existing pages.
- `seo_inspect.py`: graceful-skip on missing key; parse score from verdict.
- **Staging dry-run:** render a known article and diff its HTML shape against an existing live
  post before the first real FTP upload.

## 8. Runtime & schedule
- Target publisher = **AI cloud routine** on a cron (default **daily ~08:00 UTC**, after the
  07:00 UTC AIContent run), laptop-independent. FTP creds + `GEMINI_API_KEY` as env secrets.
- AIContent `build_feed.py` runs at approval/merge (or a tiny daily step) so the feed is fresh.

## 9. Decisions (locked) & open items
- **Locked:** git-native `published/` feed; markdown body in the contract; target pulls +
  renders + FTP-deploys; AI agent for brand/backlinks/SEO; deterministic chrome template;
  brand book derived from the live site; SEO inspection via Gemini before deploy.
- **Defaults (change on request):** route to `blog/<slug>/`; tooling in
  `VsichkiKazina/_publisher/`; schedule daily ~08:00 UTC.
- **To confirm at build time:** exact FTP target dir on the server; whether the AIContent feed
  build is a merge-time hook vs a small scheduled step.

## 10. Decomposition (for the plan)
Two sub-projects, built in order (the contract first, since both depend on it):
1. **AIContent feed** — `build_feed.py` + `published/` contract (+ tests). Small, generic.
2. **VsichkiKazina publisher** — brand-book, template, link-map, `publish-run.md`, `seo_inspect.py`,
   `deploy_ftp.py`, state, and the scheduled routine.

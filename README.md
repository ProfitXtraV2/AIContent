# AIContent — Autonomous SEO Content Pipeline

AIContent is an **autonomous, keyword-driven content factory** for gambling-comparison
websites. A scheduled cloud agent researches real search demand, writes on-brand articles
through a multi-stage editorial pipeline, and delivers each one as a GitHub Pull Request
for a human to review and publish — keeping a **rolling buffer of ready-to-post drafts** at
all times.

It is currently configured for one brand — **Всички Казина** (`vsichkikazina.bg`, an
independent Bulgarian online-casino comparison site) — but the layout is multi-brand by
design (see [Adding a brand](#adding-a-new-brand)).

> **Status:** operational. Daily automation runs in the cloud (laptop-independent). Human
> review + publishing stays manual by design.

---

## Table of contents
1. [What it does](#what-it-does)
2. [How it works (architecture)](#how-it-works-architecture)
3. [The daily lifecycle](#the-daily-lifecycle)
4. [Repository layout](#repository-layout)
5. [Data model & schemas](#data-model--schemas)
6. [Configuration & setup](#configuration--setup)
7. [Human workflow](#human-workflow)
8. [The dashboard](#the-dashboard)
9. [Local development](#local-development)
10. [Operational notes & known limits](#operational-notes--known-limits)
11. [Adding a new brand](#adding-a-new-brand)
12. [Non-negotiable principles](#non-negotiable-principles)

---

## What it does

- **Keeps ≥10 written-but-unposted articles ready.** Each run refills the buffer to a
  target (`BUFFER_TARGET = 10`): post N articles ⇒ the next run writes N.
- **Finds real demand with Ahrefs.** Keyword research pulls Bulgarian (`country=bg`) search
  volume, difficulty (KD), intent and trend, computes a deterministic **Opportunity** score,
  and prioritises high-volume / achievable-difficulty topics. Falls back to web research if
  Ahrefs is unavailable — it never halts.
- **Avoids keyword cannibalization.** Both *during research* and *before writing*, topics
  are clustered by intent; only **one pillar per cluster** is kept/written, and overlaps
  with existing articles are folded in as sections/links.
- **Writes on-brand, humanised content.** A 7-stage fresh-context editorial pipeline
  (Synthesis → Outline → Author → Humaniser → SEO → Brand Gate → light re-check) produces
  Bulgarian copy signed **Георги Тодоров**, with an anti-AI-pattern discipline and a hard
  compliance gate (responsible-gambling lines, disclosures, licence framing).
- **Cross-model AI-detection gate (Gemini, Step 7).** Each finished draft is scored by
  **Gemini** (a different model family) for AI-writing tells. If it's below the target
  ("human-written ≥ 80%"), the run applies Gemini's *style* recommendations through a fresh
  Humaniser pass (facts untouched) and re-checks — up to 2 passes. The verdict shows on the
  dashboard as a per-article rating/approval badge. Skips gracefully if the key is unset.
- **Never fabricates.** Unverifiable facts stay as `[VERIFY]` flags for the human; the run
  refuses to invent operator terms, licences, or figures. Gemini is style-only — it never
  touches facts, RG language, disclosures, or flags.
- **Delivers via PR.** One Pull Request per article (content only), plus a
  `06-verification.md` that makes the human's fact-check fast. Nothing reaches `main` /
  publication without a human.
- **Self-reporting dashboard.** A GitHub Pages board shows the buffer, next run, live
  per-stage progress, articles-for-review, articles-ready-to-deploy, and both keyword
  backlogs with Ahrefs metrics + opportunity ratings.

## How it works (architecture)

```
                          ┌──────────────────────────────────────────────┐
   Scheduled cloud agent  │  CCR routine (Anthropic cloud, cron 07:00 EET)│
   (laptop-independent)   │  executes VsichkiKazina/automation/daily-run.md│
                          └───────────────────────┬──────────────────────┘
                                                  │ clones repo (self-contained)
        ┌─────────────────────────────────────────┼──────────────────────────────────────┐
        │                                          │                                       │
        ▼                                          ▼                                       ▼
  KEYWORD RESEARCH                          WRITE (per article)                       PUBLISH PATH
  Ahrefs API (bg) ── or ── web fallback     pipeline/ 7 fresh-context stages           one PR per article
  → research-topics.md (AI backlog)         → articles/<date-slug>/*                   (content only, to a
  → analyses human topic-backlog.md         + 06-verification.md (human fact-check)     content/* branch)
  → opportunity score + "checked" badge     numbers diffed between every stage
        │                                          │                                       │
        └───────────────► BOARD ON main ◄──────────┘                                       │
              content-queue.md · topic-backlog.md · research-topics.md ·                    │
              run-status.json (heartbeat + live step) · docs/ (dashboard)                   │
                                   │                                                        │
                                   ▼                                                        ▼
                       build_dashboard.py → docs/data/status.json          Human reviews PR → resolves flags →
                       GitHub Pages serves docs/index.html                  approves → merges → posts to the
                       https://profitxtrav2.github.io/AIContent/            live site → marks row `posted`
```

**Key architectural decisions:**

- **Self-contained repo.** Everything the cloud run needs — the pipeline, prompts, brand
  bindings, automation instructions, scripts — lives in the repo, so a run is a clean clone
  with no external skill dependency.
- **Board-on-`main`, content-in-PRs split.** Operational *tracking* (queue, backlogs,
  run-status, dashboard) is committed straight to `main`; article *content* only ever
  reaches `main` through a human-merged PR. This lets the dashboard stay accurate live
  while keeping publishing human-gated.
- **Deterministic where it matters.** The dashboard builder and opportunity scoring are
  plain, tested Python (`scripts/build_dashboard.py`); the creative work is the LLM
  pipeline. The dashboard is static (no server) and data-driven from `status.json`.
- **Fresh context per stage.** Each editorial stage runs as an isolated subagent reading
  only its inputs — this is a deliberate anti-AI-tell and quality measure.

## The daily lifecycle

`VsichkiKazina/automation/daily-run.md` is the single source of truth the agent executes.
Summary of its steps:

1. **Sync + heartbeat.** Pull `main`; write `run-status.json` `state:running` (dashboard
   shows the green banner + live stage tracker).
2. **Measure buffer.** `deficit = min(BUFFER_TARGET − (drafted+approved), MAX_PER_RUN)`.
   If `deficit ≤ 0`, only refresh research + dashboard.
3. **Select topics.** Drain the human backlog first (it's a *commitment* — every open
   keyword must eventually become a written article), then the AI research bank. Apply
   **exact dedup** (queue + sitemap) and **anti-cannibalization** (one pillar per cluster).
4. **Write each article** through pipeline stages 1→5b, diffing all numbers between stages;
   run the **Step-7 Gemini cross-model check** (accept at human-written ≥ 80%, else apply
   recs via a fresh Humaniser pass + re-gate, ≤ 2 passes); assemble `06-verification.md`;
   obey the current **content scope** (guides-only until a BG source route exists).
5. **Record outcome on `main`.** Queue row → `drafted`/`failed` (+ the Gemini verdict in the
   `gemini` column); backlog row → `written`/`failed`; never resolve flags, post, or merge.
6. **Keyword research + analysis.** Ahrefs (or web fallback) refreshes the AI backlog and
   grades the human backlog; dedup applied *here too*. Rebuild the dashboard.
7. **Open one PR per article** (content only) into `main`.
8. **End heartbeat.** `run-status.json` → `idle` with counts.

## Repository layout

```
AIContent/
├── README.md                     # this file
├── SETUP.md                      # one-time setup checklist
├── docs/                         # GitHub Pages dashboard (served from /docs)
│   ├── index.html                #   static, data-driven UI
│   ├── robots.txt                #   noindex (drafts are unpublished)
│   └── data/
│       ├── status.json           #   generated: buffer, queue, backlogs, opportunity
│       └── run-status.json       #   heartbeat: running/idle + live per-stage progress
├── scripts/
│   ├── build_dashboard.py        # deterministic: parses board files → status.json
│   ├── gemini_check.py           # Step-7 external check: POSTs article+prompt to Gemini API
│   ├── AHREFS_ENDPOINTS.md       # recorded working Ahrefs v3 endpoints (for scripting)
│   ├── GEMINI_ENDPOINT.md        # recorded working Gemini model/endpoint
│   └── tests/test_build_dashboard.py
└── VsichkiKazina/                # ── one folder per brand ──
    ├── pipeline/                 # the editorial pipeline (agents, prompts, markets, gate)
    ├── automation/
    │   ├── daily-run.md          # THE run instructions (executed by the cloud routine)
    │   └── build-dashboard.md    # how to rebuild the dashboard
    ├── content-queue.md          # article lifecycle board  (tracking)
    ├── topic-backlog.md          # HUMAN keyword backlog     (you add; run enriches)
    ├── research-topics.md        # AI keyword bank           (Ahrefs-driven)
    ├── affiliate-links.md        # operator → affiliate URL registry (reuse site links)
    └── articles/<YYYY-MM-DD-slug>/# per-article working dir (00-brief … 06-verification, log)
```

## Data model & schemas

**Article lifecycle** (`content-queue.md`): `in-progress → drafted → approved → posted`
(or `failed`). **Buffer** = count of `drafted + approved`. Columns include a **`gemini`**
field holding the Step-7 verdict (`human <conf>` = approved, `ai <conf>` = below target,
`skipped`) — rendered as the rating badge on the article tabs.

**Human backlog** (`topic-backlog.md`) — you fill the first columns; the run enriches the rest:
`priority | type | query | keywords_or_terms | volume | kd | intent | checked | ahrefs_note | status | notes`
Status: `open` (to write) · `written` (done → article in review) · `failed` (blocked, retried).

**AI research bank** (`research-topics.md`):
`type | query | researched_keywords | volume | kd | intent | trend | checked | suggestion | status | date_researched`
Status: `candidate | queued | used`.

- **`checked`** ∈ `ahrefs | web | none` — how the metrics were obtained (indicator on the dashboard).
- **Opportunity** (computed in `build_dashboard.py`): a 0–100 score + band
  (Strong/Good/Moderate/Weak) from `volume` × `(1 − KD)`; higher volume and lower difficulty
  score better. Currently **volume-weighted** — tune `opportunity()` to reweight KD.
- Parsers are **tolerant**: legacy shorter rows still parse (missing metrics render empty).

**Affiliate links** (`affiliate-links.md`): `operator | affiliate_url | landing | status |
source_page | last_checked`. Articles that recommend an operator must link via this registry
(`status: active`); a missing operator becomes a `[LINK NEEDED]` flag — never a fabricated URL.

**Content types:** `review | guide | news | comparison`.

## Configuration & setup

One-time, from a machine with the GitHub CLI (see also `SETUP.md`). Most of these live on
the **cloud environment / routine**, not in the repo.

| # | What | Where | Value |
|---|------|-------|-------|
| 1 | Public repo + push | GitHub | `ProfitXtraV2/AIContent` (public — free-org Pages needs public) |
| 2 | GitHub Pages | repo settings / `gh api …/pages` | source = `main` `/docs` → dashboard URL |
| 3 | Cloud GitHub access | `/web-setup` or Claude GitHub App | grant the org/repo so the cloud agent can clone + open PRs |
| 4 | Cloud environment network | claude.ai/code → routine → env ⚙ | **Network access: Full** (WebFetch/Ahrefs need egress) |
| 5 | Ahrefs key | same env ⚙ → Environment variables | secret **`AHREFS_API_KEY`** (never commit it) |
| 6 | Gemini key (optional) | same env ⚙ → Environment variables | secret **`GEMINI_API_KEY`** for the Step-7 cross-model check (skips gracefully if unset) |
| 7 | Scheduled routine | `/schedule` / routines API | cron **`0 4 * * *`** (07:00 Europe/Sofia), model, run `automation/daily-run.md` |

**Tunable constants** (top of `automation/daily-run.md`):

| Constant | Default | Meaning |
|---|---|---|
| `BUFFER_TARGET` | 10 | desired written-but-unposted articles |
| `MAX_PER_RUN` | 10 | safety cap on articles per run (first backfill) |
| `RUN_TIME` | 07:00 Europe/Sofia | cron fire time (UTC in the routine: `0 4 * * *`) |
| `GEMINI_TARGET_CONFIDENCE` | 80 | Step-7 accepts at "human-written ≥ this" |
| `MAX_GEMINI_PASSES` | 2 | max Humaniser re-passes Gemini can drive before handing to human |
| **Content scope** | guides-only | single switch — see limits below |

## Human workflow

Each morning a PR (or several) is waiting. Per PR:
1. Read `05b-final-draft.md` and `06-verification.md` (surviving flags + primary-source
   links + a recalculated figure).
2. Resolve every `[VERIFY]/[DATA NEEDED]/[CONFLICT]` flag against sources; edit `05b`.
3. Set the queue row `drafted → approved`; merge the PR.
4. **Post the article to the live site manually**, then mark the row `approved → posted`
   (this frees a buffer slot; the next run refills it).
5. Steer future topics by adding rows to `topic-backlog.md` — the run enriches + writes them.

The **Gemini rating** (green `✓ Gemini NN%` = approved, amber `AI-ish NN%` = below target) is
shown per article on the review/deploy tabs — an amber badge is your cue to tighten the copy
(or post as-is). The Step-7 check runs automatically in the pipeline; you don't run it by hand.

## The dashboard

Static, data-driven (`docs/index.html` reads `docs/data/status.json` + `run-status.json`).
- **Buffer gauge**, **next scheduled run** (live countdown), **pipeline status** counts.
- **Live run banner + stage tracker** (reads `run-status.json` fresh via the GitHub API,
  so it isn't delayed by Pages builds).
- Tabs: **Articles ready to deploy** (approved) and **Articles for review** (drafts) — each
  row shows keywords used, source, links (PR + files), and the **Gemini rating badge**;
  **Backlog keywords** (yours, with Ahrefs verdict) and **AI backlog keywords** (sorted by
  opportunity, with Vol/KD/Opportunity + `✓ Ahrefs`/`web` badge).
- Regenerated every run by `build_dashboard.py`.

## Local development

```bash
# run the deterministic dashboard tests
python3 -m pytest scripts/tests -q

# rebuild the dashboard from the board files
python3 scripts/build_dashboard.py

# preview the dashboard locally
python3 -m http.server 8000   # then open http://localhost:8000/docs/
```

`build_dashboard.py` is stdlib-only. Tests cover parsing (incl. legacy rows), buffer
counting, opportunity scoring, and the meta/links block.

## Operational notes & known limits

- **Geo-block (current constraint).** Bulgarian operator T&C pages and the НАП register
  block the cloud's foreign IP (`403` / connection reset) even with Full egress. So
  **reviews/comparisons/news that need operator facts cannot self-source** from the cloud.
  The pipeline is therefore in **guides-only scope** (evergreen education writes fine).
  To lift it: add a BG-geo scraping API / residential proxy (wire it in like Ahrefs), or
  supply human source packs; then flip the content-scope switch in `daily-run.md`.
- **Ahrefs units.** The run checks `subscription-info/limits-and-usage` first; discovery
  (matching-terms) is the expensive call. On a small plan, prefer enriching known keywords.
- **GitHub API rate limit.** The dashboard reads run-status/PRs from the unauthenticated API
  (60/hr per IP); it polls conservatively and falls back to the Pages copy.
- **AI-detectors are noisy.** Detector "confidence" swings on genuinely human-edited copy;
  the pipeline applies concrete humanisation rules but chasing a score to zero is not a goal.

## Adding a new brand

The pipeline is multi-brand (`pipeline/SKILL.md` binds brand-specific gate/author/market
files). To onboard another site:
1. Create a sibling folder (e.g. `NewBrand/`) mirroring `VsichkiKazina/` — its own
   `pipeline/` (or a shared one with brand bindings), `automation/daily-run.md`,
   `content-queue.md`, `topic-backlog.md`, `research-topics.md`, `affiliate-links.md`,
   `articles/`.
2. Set the brand constants in `SKILL.md` (name, market/currency/regulator, content types,
   approved internal-link set, byline, gate + author bindings).
3. Add the brand's seed backlog and its affiliate registry.
4. Point a new scheduled routine at `NewBrand/automation/daily-run.md`; the dashboard can be
   extended to aggregate brands.

## Non-negotiable principles

- **Flags block publish.** Only the human resolves `[VERIFY]/[DATA NEEDED]/[CONFLICT]`.
- **Untouchables at every stage:** facts, odds, currency amounts, RG lines, 18+ markers,
  disclosures, dates, licence framing. Rephrase for voice — never remove.
- **Never fabricate** an operator fact, licence, figure, affiliate URL, comment, or testimonial.
- **Human owns publishing.** Merging a PR ≠ posting; posting to the live site is manual.
- **Brand & byline locked:** output in Bulgarian; brand name exactly *Всички Казина*; byline
  always *Георги Тодоров*; no sports predictions.
- **One run = one buffer refill;** article content only reaches `main` via a human-merged PR.

---
*Design spec & implementation plan: `../docs/superpowers/specs/` and `../docs/superpowers/plans/`
(in the working tree). The pipeline files under `VsichkiKazina/pipeline/` are the deployed,
canonical copy of the "cowork" content-pipeline skill.*

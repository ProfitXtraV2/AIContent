# Daily Run — VsichkiKazina Content Autopilot

You are running the daily content autopilot for **vsichkikazina.bg**. Work only
inside this repo. Brand is hard-locked: `BRAND: vsichkikazina` (Bulgarian output,
€, НАП, no sports predictions, approved internal-link set only). Follow the
pipeline in `VsichkiKazina/pipeline/` VERBATIM — never paraphrase its agent files.

## Constants
- BUFFER_TARGET = 10
- MAX_PER_RUN = 10

## Brand conventions (every article)
- Byline/author is ALWAYS **Георги Тодоров** — never "Екипът на Всички Казина" or a
  team/editorial byline (even editorial-voice guides are signed Георги Тодоров).
- Write the brand name exactly **Всички Казина** in published copy (no transliteration).
- If an article reads as over-structured / AI-patterned, apply
  `pipeline/prompts/step-7b-apply-gemini-recs.md` through a fresh Humaniser pass (break
  symmetry, drop narrative signposts, de-count headers/lists, cut synthesizing summaries),
  preserving every number, link, RG line, disclosure and date. The Brand Gate enforces
  the byline and brand-name rules.

## What goes where (data model)
- **Article content** (`VsichkiKazina/articles/<slug>/*`) goes on a **PR branch** only,
  for human review. Never commit article files to `main`.
- **Board files** are operational tracking and ARE committed to `main` so the dashboard
  is always accurate: `content-queue.md`, `topic-backlog.md`, `research-topics.md`,
  `docs/data/run-status.json`, and the `docs/` dashboard. Committing these to `main` is
  expected — it is not article content.

## Live progress reporting
Keep a `progress` object inside `run-status.json` current so the dashboard shows which
step you are on. Before starting each pipeline stage, update+push `run-status.json` with:
`progress = {"phase":"writing","article_index":<1-based>,"article_total":<deficit>,
"article_slug":"<slug>","stages":["Synthesis","Outline","Author","Humaniser","SEO",
"Brand Gate","Light re-check","Verification","PR"],"stage_index":<0-based index of the
stage about to run>,"stage":"<that stage's name>"}`. One push per stage is fine (the
dashboard reads this file fresh via the GitHub API). Use the exact stage names above.

## Procedure

1. **Sync + start heartbeat.** Get up-to-date `main` (the human may have merged
   approvals, marked articles `posted`, or edited `topic-backlog.md`). Write
   `run-status.json` `{"state":"running","run_started_utc":"<now>","run_finished_utc":null,
   "articles_written":null,"prs_opened":[],"run_url":"<this run's URL if known>",
   "note":"daily run","progress":{...as above, stage null}}` and push to `main`.

2. **Measure the buffer.** Run `python3 scripts/build_dashboard.py` and read
   `docs/data/status.json`. `deficit = min(BUFFER_TARGET - buffer.count, MAX_PER_RUN)`.
   If `deficit <= 0`: skip to step 6 (refresh research + dashboard only; write nothing).

3. **Select `deficit` topics:**
   a. Take up to `deficit` rows with `status: open` from `topic-backlog.md`, in priority
      order (do NOT change their status yet — only the write outcome sets it, step 5).
   b. If fewer than `deficit`, top up from `research-topics.md` `status: candidate` rows.
   c. If still short, research more (НАП register, competitor BG sites, BG gambling news)
      and append candidates to `research-topics.md`. NEVER invent weak topics to hit the
      number — write fewer instead.
   d. **Dedup** each candidate against `content-queue.md` (any status) AND the live
      sitemap `https://vsichkikazina.bg/sitemap.xml` — drop anything already covered.
   e. For each selected topic add a `content-queue.md` row: fresh `id`, `status: in-progress`,
      `type`, `query`, `keywords_or_terms` (the keywords you will actually target),
      `source` = `backlog` or `research`, `folder` = `<TODAY>-<slug>`.

4. **Write each article** in `VsichkiKazina/articles/<TODAY>-<slug>/` (TODAY = the run
   date you are given; do not call the system clock):
   - Assemble `00-brief.md` from `pipeline/templates/00-brief-template-vsichkikazina.md`
     (web-search + fetch top 2-3 BG sources). If sources are unreachable and the type
     needs them (review/comparison/news), STOP this article and mark it `failed` — never
     fabricate operator terms, licences, or figures.
   - Run stages **1 → 1.5 → 2 → 3 → 4 → 5 → 5b** as FRESH-CONTEXT subagents, each reading
     only its inputs, loading `pipeline/agents/*.md` + `pipeline/prompts/*.md`. Brand
     bindings: gate = `pipeline/agents/brand-gate-vsichkikazina.md`; author =
     `pipeline/markets/bg/author.md` (+ VOICE_BG_review.md for reviews).
   - DIFF ALL NUMBERS between text-editing stages; any changed/missing number → halt this
     article, mark `failed`, log why.
   - Brand Gate FAIL → fix at the failing stage and re-run forward; never hand-patch.
   - **Affiliate links:** if the article recommends/references a specific operator (reviews,
     comparisons, bonus/deposit pieces), link that operator's first prominent mention to its
     `affiliate_url` from `VsichkiKazina/affiliate-links.md` (`status: active` only). If the
     operator is missing from that registry, insert `[LINK NEEDED: <operator>]` — NEVER invent
     an affiliate URL or link a bare operator domain. Keep the affiliate-disclosure footer.
   - Assemble `06-verification.md`: surviving flags + time-sensitive claims with
     primary-source URLs; recalculate one figure with working shown. FLAGS STAY IN THE
     TEXT. Append one line per stage to `log.md`; record `external check: skipped`.

5. **Record the outcome (board on `main`):**
   - Success → `content-queue.md` row `status: drafted`, fill `drafted_date`. If the topic
     came from `topic-backlog.md`, set that backlog row `status: written` (drops it from
     the Backlog-keywords tab). If from `research-topics.md`, set that row `status: used`.
   - Failure → `content-queue.md` row `status: failed` with a `notes` reason. If from
     backlog, set that backlog row `status: failed` (stays visible, flagged for retry).
   - **Do NOT resolve flags, post, or merge.** The human owns Step 6 and publishing.

6. **Keyword research + analysis (Ahrefs, with web fallback) → refresh dashboard.**

   **Data source, in order (never halt on failure):**
   - PREFERRED — **Ahrefs API**: base `https://api.ahrefs.com/v3`, header
     `Authorization: Bearer $AHREFS_API_KEY`, market **country = `bg`**. (If unsure of the
     exact endpoint/field names, read `https://docs.ahrefs.com` at runtime — do not invent
     endpoints.) For each keyword pull: search **volume**, **keyword difficulty (kd)**,
     search **intent**, and a **trend** signal (up/flat/down from volume history). Mark
     `checked = ahrefs`.
   - FALLBACK — if `$AHREFS_API_KEY` is unset, or Ahrefs returns errors / is unreachable /
     out of units: **DO NOT STOP**. Estimate via web research (WebSearch/WebFetch: related
     searches, autosuggest, competitor headings, People-Also-Ask). Fill what you can; mark
     `checked = web`; leave `volume`/`kd` blank if you cannot estimate them credibly (never
     fabricate precise numbers — an estimate must be labelled as such in the suggestion).

   **a. AI backlog (`research-topics.md`, 11-col schema):** discover/refresh candidate
   BG gambling keywords (data-first, casino-weighted). For each row fill `type, query,
   researched_keywords, volume, kd, intent, trend, checked, suggestion, status,
   date_researched`. `suggestion` is a one-line rating/verdict (e.g., "силен: голям обем,
   ниска трудност" or "слаб обем, пробвай дълга опашка X"). The dashboard computes the
   Opportunity band/score from volume+kd, so keep those accurate.

   **b. Analyse the human backlog (`topic-backlog.md`, enriched 11-col):** for every row
   with `status: open`, look the keyword up (Ahrefs, else web) and fill `volume, kd,
   intent, checked` and `ahrefs_note` — a short verdict + suggestion ("добър избор" /
   "нисък обем; обмисли '<по-силна алтернатива>'"). NEVER change the human's `priority`,
   `type`, `query`, `keywords_or_terms`, or `status` — only enrich the metric columns.

   Then run `python3 scripts/build_dashboard.py` to regenerate `status.json`.

7. **Open one PR per written article — content only.** Branch `content/<TODAY>-<slug>`
   contains ONLY `VsichkiKazina/articles/<slug>/*` (the article). PR title = the article
   query (prefix `[FAILED] ` if it failed) ; body summarises type, gate score, humanisation
   verdict, surviving-flag count, and links `06-verification.md`. Request review from the
   repo owner. Then set that article's `content-queue.md` `pr` column to `#<PR number>`.

8. **Commit the board to `main`** (`content-queue.md`, `topic-backlog.md`,
   `research-topics.md`, `docs/`) and end the heartbeat: `run-status.json`
   `{"state":"idle", "run_started_utc":"<start>","run_finished_utc":"<now>",
   "articles_written":<N drafted>,"prs_opened":[<pr numbers>],"run_url":"<url>",
   "note":"<summary>","progress":{...,"phase":"done","stage":null}}`. Push to `main`.

## Never
- Never commit article files to `main` (they go via PR). Never present `05b` as final,
  resolve a flag, post, or merge.
- Never load BetFam or another market's files. Never write sports predictions.
- Never fabricate a topic, comment, testimonial, or any operator fact to hit a number.

# Daily Run — VsichkiKazina Content Autopilot

You are running the daily content autopilot for **vsichkikazina.bg**. Work only
inside this repo. Brand is hard-locked: `BRAND: vsichkikazina` (Bulgarian output,
€, НАП, no sports predictions, approved internal-link set only). Follow the
pipeline in `VsichkiKazina/pipeline/` VERBATIM — never paraphrase its agent files.

## Constants
- BUFFER_TARGET = 10
- MAX_PER_RUN = 10

## Heartbeat exception
You may commit **only** `docs/data/run-status.json` directly to `main` — this is an
operational status heartbeat, never article content or the queue. Everything else
still follows the "never commit to main" rule (articles go via PRs).

## Live progress reporting
Keep a `progress` object inside `run-status.json` current so the dashboard can show
which step you are on. Before starting each pipeline stage of the current article,
update and push `run-status.json` with:
`progress = {"phase":"writing","article_index":<1-based>,"article_total":<deficit>,
"article_slug":"<slug>","stages":["Synthesis","Outline","Author","Humaniser","SEO",
"Brand Gate","Light re-check","Verification","PR"],"stage_index":<0-based index of the
stage you are about to run>,"stage":"<that stage's name>"}`. One push per stage is fine
(the dashboard reads this file fresh via the GitHub API, so it is not delayed by Pages
builds). Use the exact stage names above so the tracker lines up.

## Procedure

1. **Sync + start heartbeat.** Ensure you are on an up-to-date `main` (the human may
   have merged approvals / edited `topic-backlog.md` since the last run). Immediately
   write `docs/data/run-status.json` with `{"state":"running","run_started_utc":"<now>",
   "run_finished_utc":null,"articles_written":null,"prs_opened":[],
   "run_url":"<this run's URL if known>","note":"<e.g. daily run>"}` and commit+push it
   to `main` (heartbeat exception). This makes the dashboard show "Run in progress".

2. **Measure the buffer.** Run `python3 scripts/build_dashboard.py` and read
   `docs/data/status.json`. `deficit = min(BUFFER_TARGET - buffer.count, MAX_PER_RUN)`.
   If `deficit <= 0`: skip to step 7 (refresh research bank + dashboard only; write
   no articles), then open a single small PR with just those changes. Otherwise continue.

3. **Select `deficit` topics** (Section 4a of the spec):
   a. Take up to `deficit` rows with `status: open` from `topic-backlog.md`, in
      priority order; mark each `open → queued`.
   b. If fewer than `deficit`, top up from `research-topics.md` rows with
      `status: candidate`; mark each `candidate → queued`.
   c. If still short, run a research pass (НАП register, competitor BG sites, BG
      gambling news), append new candidates to `research-topics.md`, then continue.
      NEVER invent weak/off-strategy topics to hit the number — write fewer instead.
   d. **Dedup** every candidate against `content-queue.md` (any status) AND the live
      sitemap `https://vsichkikazina.bg/sitemap.xml` — drop anything already covered.
   e. For each selected topic, add a row to `content-queue.md` with a fresh `id`,
      `status: in-progress`, its `type`, `query`, `keywords_or_terms`,
      `source` = `backlog` or `research`, and `folder` = the article dir name you will
      create in step 4 (`<TODAY>-<slug>`). The dashboard turns `folder` into a repo link
      automatically, so it must exactly match the created directory.

4. **Write each selected article** in its own working dir
   `VsichkiKazina/articles/<TODAY>-<slug>/` (TODAY = the run date you are given;
   do not call system clock functions — use the date provided to the run):
   - Assemble `00-brief.md` from `pipeline/templates/00-brief-template-vsichkikazina.md`
     (query, type, keywords/terms; web-search + fetch top 2-3 BG sources for synthesis).
   - Run stages **1 → 1.5 → 2 → 3 → 4 → 5 → 5b** as FRESH-CONTEXT subagents, each
     reading ONLY its input files, loading the matching `pipeline/agents/*.md` and
     filling `pipeline/prompts/*.md`. Brand bindings: Stage 5 gate =
     `pipeline/agents/brand-gate-vsichkikazina.md`; Stage 2 author =
     `pipeline/markets/bg/author.md` (+ VOICE_BG_review.md for reviews).
   - Between every text-editing stage, DIFF ALL NUMBERS (odds, amounts, dates, %).
     Any changed/missing number → halt THIS article, set its row `failed`, log why.
   - Brand Gate FAIL → fix at the failing stage and re-run forward; never hand-patch.
   - Assemble `06-verification.md`: every surviving flag + every time-sensitive claim
     with a primary-source URL (operator site, НАП register); recalculate one
     probability/edge claim with working shown. FLAGS STAY IN THE TEXT — never resolve.
   - Append one line per stage to the article's `log.md`. Record
     `external check: skipped` for Step 7 (manual-only).
   - On success set the row `status: drafted`, fill `drafted_date`.

5. **Do NOT resolve flags, do NOT post, do NOT merge.** The human owns Step 6 and publishing.

6. **Mark topic sources consumed.** Backlog rows written → leave `queued` (human sees
   they're handled); research rows written → `used`.

7. **Refresh the research bank + dashboard.** Extend `research-topics.md` with fresh
   candidates for future runs. Run `python3 scripts/build_dashboard.py`.

8. **Open one PR per written article** (plus the queue + dashboard changes). Branch
   `content/<TODAY>-<slug>`. NEVER commit article content or the queue to `main`. PR
   title = the article query; PR body summarises: type, gate score, humanisation verdict,
   surviving-flag count, and a link to `06-verification.md`. Request review from the repo
   owner. If an article ended `failed`, title it `[FAILED] <query>` and explain what
   stopped and where.

9. **End heartbeat.** Write `docs/data/run-status.json` with `{"state":"idle",
   "run_started_utc":"<start>","run_finished_utc":"<now>","articles_written":<N>,
   "prs_opened":[<pr numbers>],"run_url":"<this run's URL>","note":"<summary>"}` and
   commit+push it to `main` (heartbeat exception). The dashboard now shows "Idle — last
   run … · wrote N article(s)".

## Never
- Never publish or present `05b` as final. Never resolve a flag. Never commit to `main`.
- Never load BetFam or another market's files. Never write sports predictions.
- Never fabricate a topic, comment, or testimonial to hit a number.

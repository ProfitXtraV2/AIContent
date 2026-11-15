# Daily Run — BizGrow Page Autopilot

> **MANUAL TRIGGER — NOT SCHEDULED** (even after un-pausing). Trigger: open a Claude Code
> session in this repo and say *run BizGrow/automation/daily-run.md* (optionally naming one
> page, e.g. "for /"). Do not register a routine for it.

You are running the page pipeline for **BizGrow**, an AI and automation consultancy for small
businesses in Bulgaria. Work only inside this repo; never write to the `biz-grow` site repo.
Follow `BizGrow/pipeline/` VERBATIM (SKILL.md, agents, markets/*/author.md, reference/*).

## Constants
- BUFFER_TARGET = 3    (page drafts awaiting porting/owner approval; a soft floor for the
  dashboard, not a quota)
- MAX_PER_RUN = 1      (one page per run)
- GEMINI_TARGET_CONFIDENCE = 80   (Step 7 professional score)
- MAX_GEMINI_PASSES = 2
- IMAGE_MIN_PER_ARTICLE = 0       (no images by default)

## Step 0 — pause and pre-flight (every run)
1. Un-paused for manual runs by the owner on 2026-11-15 ("the seo content need to go through contentai, but the professional version … use that analysis to help redo the content of the site"); still not scheduled. Do not register a routine.
2. If any `BizGrow/content-queue.md` row is `in-progress`, resume it instead of starting a new
   page (never duplicate a drafted/approved/posted page).
3. Read the site sources (`desislavamit/biz-grow`, branch `main` unless the owner names another; for the 2026-11-15 SEO rewrite the owner's session uses branch `feature/seo-improvements` (local worktree `~/Work/biz-grow-seo`);
   local clone `~/Work/biz-grow` if running locally): `docs/ai-consultancy-spec.md`,
   `site/src/i18n/dictionaries/bg.ts`, `en.ts`, `site/src/i18n/types.ts`,
   `site/src/i18n/config.ts`. Diff them against `BizGrow/pipeline/reference/site-rules.md`; on
   any difference the site repo / owner wins; note it in the page's `log.md` and in the PR body.
   If the site repo is unreachable → STOP (no page-rewrite without the current page).
4. Gemini availability: `GEMINI_API_KEY` is set only in the cloud routine environment. In a local
   run Step 7 logs `skipped` (see SKILL.md STEP 7).

## What goes where
- Page work (`BizGrow/articles/<YYYY-MM-DD>-<slug>/*`, including `content/<slug>.md`) goes on a
  PR branch `bz-content/<YYYY-MM-DD>-<slug>` only.
- Board files go to `main`: `BizGrow/content-queue.md`, `BizGrow/topic-backlog.md`,
  `BizGrow/research-topics.md`, `docs/data/bizgrow/` (status + run-status).
  `BizGrow/keyword-map.md` is edited only by the owner's session, never by a run.

## Live progress
Keep `docs/data/bizgrow/run-status.json` current exactly as ELLE Dental does, with
`stages = ["Brief","Synthesis","Outline","Author","Professional edit","SEO","Brand Gate",
"Light re-check","Verification","Gemini","PR"]` and `stage_index` bumped at each boundary.

## Procedure
1. **Heartbeat** → `state: running`.
2. **Select ONE page.** If the human named a page, use it. Otherwise take the lowest-priority-
   number row in `BizGrow/topic-backlog.md` with `status: open`. A row is eligible only if its
   address has a main term in `keyword-map.md`; a `new-page` row also needs keyword-map status
   `planned`. Rows with `paused` or `blocked: …` are never selected. Write a Bulgarian page before
   its English pair. Dedup against `content-queue.md`: a page with an open PR or a
   drafted/approved row is skipped.
   Add the queue row: fresh `bz-NNNN` id, `status: in-progress`, `type`, `query` = the address,
   `keywords_or_terms`, `volume`/`kd` from the backlog row, `source: backlog`,
   `folder: <TODAY>-<slug>`.
3. **Write the page** per `BizGrow/pipeline/SKILL.md`: Step 0 brief (current page + inventory)
   → stages 1 → 1.5 → 2 → 3 → 4 → 5 → 5b as FRESH-CONTEXT subagents, inventory diff between
   editing stages (any missing/weakened item → halt, `failed`) → Step 6 verification +
   `content/<slug>.md` → Step 7 Gemini (`--brand bizgrow`, keep-best, commit trail:
   `content(<slug>): initial draft`, `gemini(<slug>): check N — …`,
   `content(<slug>): edit pass N (apply Gemini recs)`) → Step 8 (no images by default).
4. **Record the outcome on `main`:** success → queue `drafted` + `drafted_date` + `gemini`;
   backlog row → `written` (notes: `drafted <date>, PR #N, awaiting porting + owner approval`).
   Failure → queue `failed` + reason; backlog row stays `open` with `blocked: <reason>` in notes.
5. **Research (only after un-pause, optional):** Ahrefs `country=bg` enrichment of backlog rows
   whose `checked` is `none`; new-page ideas go to `research-topics.md` as `candidate` with
   `suggestion: owner decision needed` and are NEVER written until the owner's session adds them
   to `keyword-map.md` as `planned`. Never fabricate volumes; blank if unknown. Then
   `python3 scripts/build_dashboard.py bizgrow`.
6. **Open the PR** (content only): branch `bz-content/<TODAY>-<slug>`, files under
   `BizGrow/articles/<TODAY>-<slug>/`. Title = `BizGrow: <H1> (<address>)` (prefix `[FAILED] ` if
   failed). Body: page, locale, main term + Ahrefs metrics, gate score + verdict,
   professional-quality verdict, Gemini score (or `skipped`), inventory diff result, new
   sources, owner items added (count + list), REMAINING FOR HUMAN, the site-rule diff, PORTING
   NOTES (dictionary keys to change), and the human's next steps: port `content/<slug>.md` into
   `site/src/i18n/dictionaries/<locale>.ts` and the components, run `npm run lint`,
   `npx tsc --noEmit`, `npm run build`, send the page and its owner items to the owner. State
   plainly: "This is an AI draft. It is not approved by the owner." Set the queue `pr` column.
7. **End heartbeat** → `idle`, counts, note. Push board files to `main`.

## Never
- Never schedule this file; runs are manual.
- Never state a fact about BizGrow outside the canon (prices, team, legal data, address, phone,
  clients, case results are unknown).
- Never invent a number, promise a result, or present an example scenario as a client result.
- Never use „ти“ forms on a Bulgarian page; never use em-dashes.
- Never remove a CTA, token, anchor, example label or FAQ from a page being rewritten.
- Never write to the `biz-grow` repo; never merge; never post to the live site.
- Never load another brand's humaniser, author or gate files (see SKILL.md for why BizGrow uses
  its own professional register).

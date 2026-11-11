# ⏸ PAUSED — by owner on 2026-11-11 — MANUAL TRIGGER ONLY

> **DO NOT RUN. DO NOT SCHEDULE.** The owner asked on 2026-11-11 to add ELLE Dental to the
> AIContent pipeline *but pause it for now*. Until the owner un-pauses it **in writing**, this
> file must not be executed by anyone or anything, and no routine, cron, RemoteTrigger or
> CronCreate may be registered for it. While paused the brand produces nothing: no topic
> selection, no research, no Ahrefs calls, no articles, no PRs, no heartbeat writes.
>
> **If you are an agent asked to run this file:** check for a written un-pause from the owner
> (dated after 2026-11-11, e.g. a message, issue or PR comment saying ELLE Dental may run). If
> there is none, STOP now and reply: "ELLE Dental is paused by the owner (2026-11-11); it needs a
> written un-pause first." Do not continue to the steps below.
>
> **How to un-pause (human, in one PR):**
> 1. Get the owner's written go-ahead and link or quote it in the PR description.
> 2. Delete this banner (down to the line `# Daily Run — ELLE Dental`) and the PAUSED banner in
>    `ElleDental/pipeline/SKILL.md` (and its "PAUSED" wording in the front-matter description).
> 3. Update README.md: brand list, dashboard table, layout tree (remove "PAUSED").
> 4. In `ElleDental/topic-backlog.md` set the rows the owner wants written from `paused` to
>    `open` (leave `blocked: owner decision` rows alone unless the owner approved that page).
> 5. In `scripts/build_dashboard.py` remove `"paused"` from `BRANDS["elledental"]`; update
>    `test_elledental_registered_and_paused` in `scripts/tests/test_build_dashboard.py`; run
>    `python3 -m pytest scripts/tests -q`; run `python3 scripts/build_dashboard.py elledental`.
> 6. Commit `chore(elledental): un-pause per owner <YYYY-MM-DD>`. The brand stays MANUAL
>    TRIGGER ONLY after un-pausing; scheduling it is a separate, explicit owner decision.

# Daily Run — ELLE Dental Page Autopilot

> **MANUAL TRIGGER — NOT SCHEDULED** (even after un-pausing). Trigger: open a Claude Code
> session in this repo and say *run ElleDental/automation/daily-run.md* (optionally naming one
> page, e.g. "for /lechenie-na-pulpiti/"). Do not register a routine for it.

You are running the page pipeline for **elledental.bg**, a dental clinic in ж.к. Света Троица,
София. Work only inside this repo; never write to WebPortals. Follow `ElleDental/pipeline/`
VERBATIM (SKILL.md, agents, markets/bg/author.md, reference/*).

## Constants
- BUFFER_TARGET = 3    (page drafts awaiting doctor review; the doctor is the bottleneck, so this
  is a soft floor for the dashboard, not a quota)
- MAX_PER_RUN = 1      (one page per run; YMYL medical review is slow and must not pile up)
- GEMINI_TARGET_CONFIDENCE = 80   (Step 7 professional score)
- MAX_GEMINI_PASSES = 2
- IMAGE_MIN_PER_ARTICLE = 0       (page-rewrite never adds images)

## Step 0 — pause and pre-flight (every run)
1. If the PAUSED banner above is still in this file → STOP (see banner). Nothing else runs.
2. If any `ElleDental/content-queue.md` row is `in-progress`, resume it instead of starting a
   new page (same idempotency rules as DentalVia: never duplicate a drafted/approved/posted page).
3. Read the WebPortals publisher files (`ProfitXtraV2/WebPortals`, `ElleDental/_publisher/`, on
   `main` if merged, else `feature/elledental-site`): `banned-terms.json`,
   `claim-exceptions.json`, `keyword-map.md`, `clinic.json`, `check_site.py`,
   `tests/test_content.py`. Diff them against `ElleDental/pipeline/reference/site-rules.md`; on
   any difference the publisher wins; note it in the page's `log.md` and in the PR body. If
   WebPortals is unreachable → STOP (no page-rewrite without the current page and rules).

## What goes where
- Page work (`ElleDental/articles/<YYYY-MM-DD>-<slug>/*`, including `content/<slug>.md`) goes on
  a PR branch `ed-content/<YYYY-MM-DD>-<slug>` only.
- Board files go to `main`: `ElleDental/content-queue.md`, `ElleDental/topic-backlog.md`,
  `ElleDental/research-topics.md`, `docs/data/elledental/` (status + run-status).

## Live progress
Keep `docs/data/elledental/run-status.json` current exactly as DentalVia does, with
`stages = ["Brief","Synthesis","Outline","Author","Professional edit","SEO","Brand Gate",
"Light re-check","Verification","Gemini","PR"]` and `stage_index` bumped at each boundary.

## Procedure
1. **Heartbeat** → `state: running`.
2. **Select ONE page.** If the human named a page, use it. Otherwise take the lowest-priority-
   number row in `ElleDental/topic-backlog.md` with `status: open` and `type: page-rewrite`.
   A `new-page` row is eligible only if its notes record the owner's written approval (who,
   date, link). Rows with `paused` or `blocked: …` are never selected. Dedup against
   `content-queue.md`: a page with an open PR or a drafted/approved row is skipped.
   Add the queue row: fresh `ed-NNNN` id, `status: in-progress`, `type`, `query` = the address,
   `keywords_or_terms`, `volume`/`kd` from the backlog row, `source: backlog`,
   `folder: <TODAY>-<slug>`.
3. **Write the page** per `ElleDental/pipeline/SKILL.md`: Step 0 brief (current page +
   inventory) → stages 1 → 1.5 → 2 → 3 → 4 → 5 → 5b as FRESH-CONTEXT subagents, inventory diff
   between editing stages (any missing/weakened item → halt, `failed`) → Step 6 verification +
   `content/<slug>.md` → Step 7 Gemini (`--brand elledental`, keep-best, commit trail as in
   DentalVia: `content(<slug>): initial draft`, `gemini(<slug>): check N — …`,
   `content(<slug>): edit pass N (apply Gemini recs)`) → Step 8 (no images for page-rewrite).
4. **Record the outcome on `main`:** success → queue `drafted` + `drafted_date` + `gemini`;
   backlog row → `written` (notes: `drafted <date>, PR #N, awaiting doctor review`). Failure →
   queue `failed` + reason; backlog row stays `open` with `blocked: <reason>` in notes.
5. **Research (only after un-pause, optional):** Ahrefs `country=bg` enrichment of backlog rows
   whose `checked` is `none`; new-page ideas go to `research-topics.md` as `candidate` with
   `suggestion: owner decision needed` and are NEVER written without approval. Never fabricate
   volumes; blank if unknown. Then `python3 scripts/build_dashboard.py elledental`.
6. **Open the PR** (content only): branch `ed-content/<TODAY>-<slug>`, files under
   `ElleDental/articles/<TODAY>-<slug>/`. Title = `ELLE Dental: <H1> (/<slug>/)` (prefix
   `[FAILED] ` if failed). Body: page, main term + Ahrefs metrics, gate score + verdict,
   professional-quality verdict, Gemini score, inventory diff result, new sources, clinical
   items added (count + list), REMAINING FOR HUMAN, the publisher-rule diff, and the human's
   next steps: copy `content/<slug>.md` to WebPortals `ElleDental/_publisher/content/<slug>.md`,
   run `check_site.py --draft` and the site tests there, send the page and its clinical items to
   Д-р Манолова. State plainly: "This is an AI draft. It is not medically reviewed."
   Set the queue `pr` column.
7. **End heartbeat** → `idle`, counts, note. Push board files to `main`.

## Never
- Never run or schedule while the PAUSED banner is present.
- Never set `reviewed_by` / `reviewed_on`, fill a clinical item's decision, or say a page is reviewed.
- Never remove or weaken a warning, risk, contraindication, source, link, token or the urgent block.
- Never add a price, offer, testimonial, guarantee, invented clinic fact or unsourced medical claim.
- Never change one of the 28 addresses; never write a `new-page` without written owner approval.
- Never write to the WebPortals repo; never merge; never post to the live site.
- Never load another brand's humaniser, author or gate files (see SKILL.md for why ELLE departs).

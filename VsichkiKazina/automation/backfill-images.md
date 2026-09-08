# Backfill Images — VsichkiKazina (one-time catch-up for OLD articles)

You are running the **image backfill** for **vsichkikazina.bg**. Work only inside this repo.
Brand is hard-locked (`BRAND: vsichkikazina`). This job adds images to articles that were
written **before** the Step-8 image flow existed. New articles already get images at creation
(`automation/daily-run.md` Step 8) — this job only fills the gap for the OLD ones, a few at a
time, until every review-ready article has matching imagery. Then it no-ops.

## Constants
- BACKFILL_PER_RUN = 3        (add images to at most 3 articles per run — rate-limit safe)
- IMAGE_TARGET_SCORE = 80     (Gemini image-review PASS threshold; no integrity failure)
- MAX_IMAGE_PASSES = 2        (max regenerate/fix passes per image driven by review)

## Hard boundaries (what this job MUST NOT do)
- **Do NOT create new articles. Do NOT run `daily-run.md`.** Images only.
- **Do NOT change any article prose, number, link, RG line, disclosure, date, or byline.**
  The ONLY text edit allowed in `05b-final-draft.md` is INSERTING image references (and a
  one-line caption under an infographic). Every existing character otherwise stays byte-for-byte.
- **Skip `failed`, `posted`, and `in-progress` rows.** Only touch `drafted`/`approved`
  (articles for review) that still lack images.
- Never resolve flags, post, or merge. Never fabricate a fact or a number.

## Selection (idempotent — safe to re-run)
1. Sync `main` (`git checkout main && git pull --no-edit -q origin main`).
2. Read `VsichkiKazina/content-queue.md`. Build the candidate list: rows with
   `status` ∈ {`drafted`,`approved`} AND a `pr`/`folder` set (they have a `content/<folder>`
   branch) AND **no images yet** — i.e. the article's `images/` folder is missing/empty on its
   branch and `05b-final-draft.md` contains no image reference. Exclude `failed`/`posted`/
   `in-progress`.
3. Order **most valuable first** — by the computed **Opportunity** score DESCENDING. Read it
   from `docs/data/status.json` (each article row carries `opportunity.score`/`band`, derived
   from its target keyword's search volume × ease); Strong before Good before Moderate before
   Weak. Break ties by higher `volume`. Rows with no volume/kd (no Opportunity) go LAST. Take
   the first `BACKFILL_PER_RUN` (3) so the highest-traffic pages get illustrated first. (Every
   review-ready article still eventually gets images across runs — this only sets the order.)
   If the candidate list is empty, write a run-status note
   `backfill: nothing to do (all review-ready articles have images)` and STOP cleanly — the
   job is done (you may leave it to no-op on future fires; the human can disable it).

## Per-article procedure (repeat for each of the ≤3 selected)
The article's branch is `content/<folder>` (from its queue row). Work on that branch so the
images land in the SAME open PR.

1. **Checkout + sync the branch:** `git fetch origin -q && git checkout content/<folder> &&
   git merge --no-edit origin/main` (bring in the latest scripts/prompts). Read
   `VsichkiKazina/articles/<folder>/05b-final-draft.md` end to end.
2. **Decide the image set — it MUST match the text.** Follow
   `pipeline/prompts/step-8-images.md` VERBATIM. You choose how many and which kinds; typical:
   - **≥1 data infographic (hand-authored SVG)** for each distinct data block the article
     actually contains (wagering math, an RTP/volatility comparison, a steps/checklist, a
     small table). EVERY number/label copied VERBATIM from `05b`, matching its exact number
     formatting; nothing introduced that the text doesn't state; illustrative figures labelled
     „примерни". A long, multi-data article may warrant **two** infographics; a short one, a
     single graphic. Do NOT invent data to justify a graphic.
   - **Optional concept-metaphor hero** (Gemini image API) — a textless visual metaphor of the
     article's core idea (see step-8-images.md examples), never generic filler, never text/
     numbers/logos/people. Add it only when it genuinely helps; the infographic is primary.
   Generate rasters with `python3 scripts/gemini_image_gen.py "<english metaphor prompt + the
   hygiene constraints>" VsichkiKazina/articles/<folder>/images/<descriptive-name>.webp 100`
   (WebP < 100 KB). If it prints `GEMINI_UNAVAILABLE`/`GEMINI_ERROR`, ship the infographic(s)
   alone and log it — never block on the hero.
3. **Place + reference.** Save under `articles/<folder>/images/` with descriptive
   lowercase-hyphenated filenames. Insert each image into `05b-final-draft.md` at the natural
   spot (hero under the H1; each infographic beside the data it visualises) with specific
   Bulgarian ALT text and, for infographics, a one-line caption. Change nothing else.
4. **Gemini visual review (per image)** — follow `pipeline/prompts/step-8-image-review.md`
   VERBATIM: `python3 scripts/gemini_image_review.py
   VsichkiKazina/articles/<folder>/05b-final-draft.md <image1> [<image2> …]`.
   - **PASS** at score ≥ IMAGE_TARGET_SCORE (80) AND no integrity failure (fabricated
     logo/number/screenshot, a person/face, or glamorised winning = automatic fail).
   - Else iterate: regenerate the hero with a stronger metaphor, or hand-fix the SVG (numbers
     still trace to `05b`); re-review. Up to MAX_IMAGE_PASSES (2). **Keep the best-scoring
     version.** Integrity failure → drop that image, keep the rest (or ship the infographic
     alone). Unavailable → keep the image(s), log `image review: skipped`.
5. **Commit trail on the PR branch (never squash):** commit the image(s)
   (`content(<folder>): backfill image(s)`); save each verdict verbatim to
   `articles/<folder>/08-image-review-<pass>.md` and commit
   (`image(<folder>): review <pass> — score <n> (<PASS|needs work>)`); commit any fix
   (`content(<folder>): image fix pass <pass>`). Push the branch (updates the open PR):
   `git push origin content/<folder> 2>/dev/null && echo pushed || { git pull --no-rebase
   --no-edit -q origin content/<folder>; git push origin content/<folder>; }`.
6. **Note it on the PR** (a short `gh pr comment` is fine): images added + best review score.

## After the batch (board on `main`)
- For each article backfilled, add a short `notes` mention on its `content-queue.md` row
  (e.g. `img:2`) — do NOT change its `status`, `gemini`, or other columns. Then
  `python3 scripts/build_dashboard.py`, commit the board (`content-queue.md`, `docs/`), and
  push to `main` (pull-then-push on rejection).
- Heartbeat: update `run-status.json` `note` at the start (`backfilling images (0/<n>)`) and
  end (`backfilled images on <n> article(s)`); keep `progress.stage_index` null (this job is
  not the article writer). Push.
- **Record the image model** in the end note AND each PR comment: read the `[model: ...]` tag
  `gemini_image_gen.py` prints and state which model produced the hero(s), e.g.
  `image model: gemini-3-pro-image`; if it fell back, say `image model: gemini-2.5-flash-image
  (fallback from gemini-3-pro-image)`.

## Rate-limit behavior
If a 429 hits mid-run: commit whatever image work is safely complete (pushed to the relevant
PR branches), leave the rest for the next fire, end the heartbeat note, and STOP cleanly. The
job is fully idempotent — the next fire re-selects the still-imageless articles and continues.

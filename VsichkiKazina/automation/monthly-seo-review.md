# Monthly SEO Review — VsichkiKazina

Runs **once per calendar month**, gated from `daily-run.md` (the first daily fire of a
new month triggers it). Idempotent and self-marking. Uses the same Ahrefs key
(`$AHREFS_API_KEY`, `country=bg`) and board-to-`main` flow as the daily run. **Works only
inside this repo** — it cannot touch the WebPortals site repo or Google Search Console, so
anything that lives there is emitted as a MANUAL-ACTIONS list in the report, not applied.

Purpose: keep the content engine fed and DR-aware over time — refresh the competitor gap,
graduate deferred `Pillar` keywords as authority grows, and track whether the off-site
authority work is lifting DR.

## Idempotency marker
- Read `docs/data/seo-review.json` → `{"last_monthly_review":"YYYY-MM"}` (create if absent).
- If `last_monthly_review` == current `YYYY-MM` → **SKIP** (already done this month); return to the normal daily run.
- Otherwise run the steps below, then set the marker to the current month and commit.

## Budget rule
- First call `subscription-info/limits-and-usage`. If remaining units < 20000, run a
  **LIGHT pass**: do steps 2 + 3 only (DR trend + Pillar re-check via the cheap
  `keywords-explorer/overview`), skip the competitor `organic-keywords` discovery (step 4)
  and `matching-terms` (step 5). Never halt — note "light pass (low units)" in the report.

## Steps

1. **Units check** (above). Record units spent/remaining for the report.

2. **DR + footprint trend.** Pull `site-explorer/domain-rating` and `site-explorer/metrics`
   for `vsichkikazina.bg` (`country=bg`). Append one point to the `trend` array in
   `docs/data/seo-review.json` — `{"month":"YYYY-MM","dr":N,"organic_keywords":N,"traffic":N,
   "note":"..."}`. **This JSON is the canonical source the dashboard SEO tab reads**, so it
   must be updated. Mirror the same row into `docs/seo/ahrefs-trend.md` for human reading.
   This is the signal for whether off-site authority is working.

3. **Pillar graduation.** For every deferred row (band `Pillar` / `winnable:false`, i.e. KD
   was above `SITE_MAX_WINNABLE_KD`, default 40) in `research-topics.md` and the
   competitor-gap `Pillar` list in `topic-backlog.md`, re-pull KD via
   `keywords-explorer/overview`. If a pillar's KD now sits **at or under the cap**, move it to
   a writable candidate (`status: open`/`candidate`) and note `graduated YYYY-MM, kd N`. If DR
   rose materially since the last review (e.g. +5), **recommend** bumping
   `SITE_MAX_WINNABLE_KD` in `scripts/build_dashboard.py` in the report's MANUAL-ACTIONS —
   do NOT change the code autonomously.

4. **Competitor content-gap re-pull.** For the known BG casino-content competitors
   (`casinoslots.bg`, `bg.casinority.com`, `7sport.net`, plus any new one you notice), pull
   top `site-explorer/organic-keywords` (`country=bg`, `limit` ~50, `order_by`
   `sum_traffic:desc`, `select` `keyword,volume,best_position,sum_traffic`). **Filter OUT**
   out-of-scope terms: sports betting (футбол/мач/лига/класиране/прогноз/тв/фк…), operator
   brands (елит бет/magic bet/ефбет/betano/winbet/8888/…), and pure navigational. Diff the
   remainder against: our ranked keywords, `content-queue.md` (any status), the live sitemap,
   and existing `topic-backlog.md` + `research-topics.md` rows. Enrich each genuinely NEW
   in-scope gap keyword with `keywords-explorer/overview` (volume/kd/intent). For each
   **winnable** one (`kd <= SITE_MAX_WINNABLE_KD`), append a `status: candidate` row to
   `research-topics.md` with a `cluster:` tag. Apply anti-cannibalization (one pillar per
   cluster; near-duplicates become fold-in notes). Record above-cap heads as deferred `Pillar`
   candidates (tracked, not written).

5. **Discovery top-up.** `keywords-explorer/matching-terms` (small `limit`, ~10-12) around
   the active cluster seeds (licensing, no-deposit-bonus, classic-slots, free-games, plus any
   new cluster) to surface winnable long-tails. Append only measured-volume candidates
   (zero-volume rule from `research-topics.md` applies).

6. **Backlink / disavow ALERT (report-only).** Pull `site-explorer/refdomains` for
   `vsichkikazina.bg` (new since the last review). Flag likely-toxic new referring domains
   (spammy TLDs, PBN patterns, irrelevant/adult/pharma, mass-identical anchors). **This repo
   cannot edit the disavow file or upload to Search Console** — list each flagged domain in
   the report's MANUAL-ACTIONS with the exact `domain:` lines to append to
   `WebPortals/VsichkiKazina/docs/seo/disavow.txt`, and a reminder to re-upload `disavow.txt`
   to Google Search Console.

7. **Report.** Write `docs/seo/monthly-review-YYYY-MM.md`: DR trend row, pillars graduated,
   new gap keywords added (grouped by cluster), discovery results, units spent/remaining, and
   a **MANUAL ACTIONS** section (any recommended `SITE_MAX_WINNABLE_KD` bump + the
   disavow/GSC steps). Keep it scannable.

8. **Commit to `main`.** Commit the board files + trend log + report + updated
   `docs/data/seo-review.json` (marker = current month) to `main` (board-on-main rule from
   `daily-run.md`). Then continue the normal daily run.

## Notes
- This review **adds candidates and tracks signals**; it never writes articles itself — the
  normal daily run drains the refreshed backlog/bank as usual.
- Keep it cheap: `overview` is the workhorse; `organic-keywords`/`matching-terms` are the
  costly calls — bounded `limit`s above keep a monthly pass well under budget.
- Full method + rationale (and the DR-6 KD-gate design): the WebPortals strategy doc
  `VsichkiKazina/docs/seo/keyword-opportunities.md`.

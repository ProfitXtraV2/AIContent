# ONE-OFF — Gemini AI-pattern check of the live FAQ page (added 2026-09-18)

Requested by Georgi: the FAQ page on vsichkikazina.bg was flagged by a third party as
AI-sounding. It has since been rewritten twice locally (editorial rewrite + em-dash/opener
humaniser pass). We need a genuine Gemini verdict on the current text, which is snapshotted
in `oneoff/faq-live-2026-09-18.md` (66 Q&As, extracted from the live page HTML).

## Steps (do this BEFORE step 1 of the daily run; ~2 minutes)

1. Run the standard Step-7 check against the snapshot:
   ```bash
   python3 scripts/gemini_check.py VsichkiKazina/automation/oneoff/faq-live-2026-09-18.md --brand vsichkikazina
   ```
2. Write Gemini's FULL raw output (verdict + confidence + flagged passages +
   recommendations) to `VsichkiKazina/automation/oneoff/faq-gemini-verdict-2026-09-18.md`,
   prefixed with a one-line header noting the model used and the run date.
3. Commit both the verdict file and the cleanup below directly to `main`
   (message: `oneoff: Gemini verdict for live FAQ page`).
4. Cleanup (self-removing): delete this file AND remove the `ONE-OFF` pointer section
   from `daily-run.md`. Keep `oneoff/faq-live-2026-09-18.md` and the verdict file.

## Hard rules
- Recommendations only — do NOT rewrite the FAQ text, do NOT touch the live site or the
  WebPortals repo. The verdict file is the only deliverable; fixes are applied separately.
- If `gemini_check.py` exits 2 (key/API unavailable), write the error into the verdict
  file instead, still do the cleanup, and continue the normal run.
- This does NOT count toward MAX_PER_RUN and must not delay article production.

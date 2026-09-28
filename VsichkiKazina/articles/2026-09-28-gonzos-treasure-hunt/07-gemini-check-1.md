# 07 — GEMINI EXTERNAL CHECK (Step 7), pass 1 · Gonzo's Treasure Hunt (Evolution)

COMMAND: python3 scripts/gemini_check.py articles/2026-09-28-gonzos-treasure-hunt/05b-final-draft.md
RESULT: GEMINI_ERROR — HTTP 402 (RESOURCE_EXHAUSTED: "Your prepayment credits are depleted").
Probed live at run start on 2026-09-28: still down.

DECISION (per daily-run rules): DO NOT HALT. Log `external check: skipped (Gemini unavailable)`.
The single authored draft stands as the final 05b. content-queue `gemini` = `skipped`.

KEEP-BEST: only one version exists (initial authored draft) -> best-and-final by default.
Human-likeness managed in-house at the Humaniser stage (no „не X, а Y" reflex, no signposting,
varied section shapes, illustrative examples marked примерни, 0 em-dashes).

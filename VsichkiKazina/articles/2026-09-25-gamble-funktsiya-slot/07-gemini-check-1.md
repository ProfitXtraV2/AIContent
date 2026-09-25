# 07 — Gemini external check, pass 1 (gamble/double функция)

Command: python3 scripts/gemini_check.py articles/2026-09-25-gamble-funktsiya-slot/05b-final-draft.md

RESULT: GEMINI_UNAVAILABLE (exit 2)
Verbatim error:
  GEMINI_ERROR: HTTP 402 — "Your prepayment credits are depleted... RESOURCE_EXHAUSTED"

Interpretation per daily-run.md Step 7: API down (billing/credits depleted), NOT a content signal.
DO NOT halt. external check: skipped (Gemini unavailable).
KEEP-BEST: only one version exists (initial draft); it stands as final 05b.
content-queue `gemini` column → `skipped`.
Human owns Step-6 human-likeness/style review before publish.

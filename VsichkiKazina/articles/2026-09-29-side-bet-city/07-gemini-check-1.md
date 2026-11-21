# 07 — GEMINI EXTERNAL CHECK (Step 7), pass 1 · Side Bet City (Evolution)

COMMAND: python3 scripts/gemini_check.py articles/2026-09-29-side-bet-city/05b-final-draft.md
RESULT: GEMINI_ERROR — HTTP 402 (RESOURCE_EXHAUSTED: "Your prepayment credits are depleted").
Probed live at run start on 2026-09-29: still down.

DECISION (per daily-run rules): DO NOT HALT. Log `external check: skipped (Gemini unavailable)`.
No Humaniser re-pass is driven by an absent verdict. The single authored draft stands as the
final 05b. Recorded in content-queue `gemini` column as `skipped`.

KEEP-BEST: only one version exists (initial authored draft) → it is the best-and-final by default.
Human-likeness was managed in-house at the Humaniser stage (killed the „не X, а Y" reflex, no
signposting before the RTP twist, varied section shapes without a triple bullet-dump of paytables,
0 em-dashes, asymmetric verdict) rather than by the external detector, which is offline.

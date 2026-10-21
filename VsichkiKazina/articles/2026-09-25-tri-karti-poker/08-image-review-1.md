# 08 — Image review, pass 1 (три карти покер)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/tri-karti-poker-house-edge-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: Ante&Play 3.37%, element of risk 2.01%, Pair Plus 2.32% / 7.28%. No fabricated figure. ✓
- Illustrative €10 stake labelled примерни; strategy rule дама-6-4 matches 05b. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+". ✓
- Rendered mentally/structurally: bars + labels within the 720×410 card, values inside/at bar ends. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

# 08 — Image review, pass 1 (gamble/double функция)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/gamble-riskova-igra-veroyatnost-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Survival-ladder numbers trace to 05b VERBATIM: 50% / 25% / 12,5% / 6,25% / 3,125% (fair 50/50, 0.5^N). ✓
- Labelled математически/примерни (fair 50/50 assumption) — not tied to any real game. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence numbers. ✓
- No people/faces, no glamorised winning; carries „18+". ✓
- SVG well-formed (3.7 KB); bars + labels within the 720×410 card. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

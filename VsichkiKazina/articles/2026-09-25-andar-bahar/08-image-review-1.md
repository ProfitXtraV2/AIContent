# 08 — Image review, pass 1 (Andar Bahar)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/andar-bahar-shansove-i-predimstvo-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 51.5% / 48.5%, 0.90:1 / 2.15%, 1:1 / 3.00%. No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Validated as XML (viewBox 0 0 720 410, #0f172a); bars + labels within the card, no overlap/clip. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

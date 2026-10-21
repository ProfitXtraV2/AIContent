# 08 — Image review, pass 1 (Casino War)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/casino-war-domashno-predimstvo-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 2.88% (война), 3.70% (предаване), 18.65% (залог за равенство), RTP ≈97.12%. No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Validated as XML (viewBox 0 0 720 420, #0f172a); bars + labels within the card, no overlap/clip. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

# 08 — Image review, pass 1 (Pai Gow Poker)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-pai-gow-poker/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-pai-gow-poker/images/pai-gow-poker-dve-ratse-predimstvo-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (both image models). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 7/5/2 card split; 2.84% (≈2.72% house way); 5% commission; ≈40.5% push; RTP ≈97.16%.
  No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Validated as XML (viewBox 0 0 720 470, card #0f172a). Estimated text extents checked: split boxes + right-anchored
  stat values fit inside the card with margin; no overlap/clip; rule box text within its rect. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).

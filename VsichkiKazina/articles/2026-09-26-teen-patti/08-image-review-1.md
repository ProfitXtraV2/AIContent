# 08 — Image review, pass 1 (Teen Patti)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-teen-patti/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-teen-patti/images/teen-patti-pravila-i-rakove-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (both image models). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: RTP на Ante ≈96.63%; домашно предимство ≈3.37%; Pair Plus ≈4.49%; 6 Card Bonus ≈8.56%.
  No fabricated figure; no paytable numbers shown in the SVG (only the ranking order + round flow), so no version-mixing risk. ✓
- Hand-ranking order matches 05b: тройка (trail) → пюр секванс → секванс → цвят → чифт → висока карта. ✓
- Round-flow matches 05b: Ante → виж 3 карти → Play (=Ante) или Fold → дилърът се класира с дама висока. ✓
- No operator logos/names beyond Evolution as the game maker (matches 05b note), no fake screenshots, no invented bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Validated as XML (viewBox 0 0 720 450, card #0f172a, Arial, headers #93c5fd, right-anchored stat values, note box). Rendered
  to PNG at 720px and eyeballed: both columns and all four corners clean, right-anchored values fit, note box two lines within
  its rect, no overlap/clip. Estimated text extents re-checked with the width formula: 0 overflows. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).

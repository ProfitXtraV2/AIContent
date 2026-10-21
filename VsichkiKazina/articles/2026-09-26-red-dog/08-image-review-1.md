# 08 — Image review, pass 1 (Red Dog)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-red-dog/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-red-dog/images/red-dog-izplashtania-predimstvo-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (both image models). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 5:1 / 4:1 / 2:1 / 1:1 / 11:1 payouts; 3.155% (1 тесте) & 2.751% (8 тестета) edges;
  RTP ≈96.85%; „разстояние 7" rule. No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Validated as XML (viewBox 0 0 720 500, card #0f172a). Estimated text extents checked: payout labels + right-anchored
  values fit inside the card with margin; bars (363px @3.155%, 316px @2.751%) end well before the right edge; no overlap/clip. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).

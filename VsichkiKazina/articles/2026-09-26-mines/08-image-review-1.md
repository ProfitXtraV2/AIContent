# 08 — Image review, pass 1 (Mines)

Command: python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-26-mines/05b-final-draft.md \
         VsichkiKazina/articles/2026-09-26-mines/images/mines-kak-raboti-rtp-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted; same billing outage as Step 7).
Also gemini_image_gen.py → HTTP 402 (both image models). AI hero SKIPPED.
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: 5x5 / 25 полета; 1 до 24 mines; RTP ≈97%; домашно предимство ≈3%; таван ≈ x10 000.
  No fabricated figure; NO per-config multiplier shown (only the round-flow). ✓
- No operator logos/names, no fake screenshots, no invented bonus/licence. Spribe named only as the game maker (matches 05b). ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно" + high-volatility note. ✓
- Validated as XML (viewBox 0 0 720 450, card #0f172a). Estimated text extents checked: numbered flow rows + right-anchored
  stat values fit inside the card with margin; connector line aligned; rule box text within its rect; no overlap/clip. ✓
Decision: KEEP (1 infographic). images: 1 (infographic, review skipped — API down).

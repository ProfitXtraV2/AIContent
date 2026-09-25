# 08 — Image review, pass 1 (дракон тигър)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/dragon-tiger-house-edge-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: Dragon/Tiger 3,73% (1:1, tie loses half); Tie 8:1 → 32,77%; Tie 11:1 → 10,36%; Suited Tie 50:1 → 13,98%. No fabricated figure. ✓
- Source conflict resolved before infographic: CoolOldGames' 13,6% for Tie 8:1 fails EV (0,0747×8−0,9253=−0,3277); WoO 32,77% used. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence. ✓
- No people/faces, no glamorised winning; carries „18+". ✓
- SVG well-formed; bars + labels within the 720×410 card, no clipping/overlap. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

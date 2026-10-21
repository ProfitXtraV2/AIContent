# 08 — Image review, pass 1 (Ultimate Texas Hold'em)

Command: python3 scripts/gemini_image_review.py .../05b-final-draft.md images/ultimate-texas-holdem-domashno-predimstvo-infografika.svg

RESULT: GEMINI_UNAVAILABLE (HTTP 402 — prepayment credits depleted, same billing outage as Step 7).
Per daily-run.md Step 8: image review skipped (Gemini unavailable) — DO NOT halt, keep the image.

Manual integrity self-check (author, since automated review is down):
- Numbers trace to 05b VERBATIM: element of risk 0.53%, домашно предимство 2.185% спрямо Антето, RTP ≈99.47%, вдигане 4x/2x/1x. No fabricated figure. ✓
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence beyond the sourced game math. ✓
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". ✓
- Rendered/validated as XML (viewBox 0 0 720 430, #0f172a); bars + labels within the card, no overlap/clip. ✓
Decision: KEEP (1 infographic). AI hero SKIPPED — gemini_image_gen.py also HTTP 402.
images: 1 (infographic, review skipped — API down)

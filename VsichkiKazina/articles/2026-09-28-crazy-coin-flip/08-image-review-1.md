# 08 — Gemini image review (pass 1) · Crazy Coin Flip

Command: python3 scripts/gemini_image_review.py <article>/05b-final-draft.md <images…>
Result: SKIPPED — Gemini image API unavailable (HTTP 402 RESOURCE_EXHAUSTED, same outage as Step 7).

Image shipped: 1 hand-authored SVG infographic (crazy-coin-flip-fazi-i-rtp-infografika.svg).
AI hero: SKIPPED (image gen offline, 402).

Manual integrity check (orchestrator):
- Every SVG number traces verbatim to 05b: 5 барабана/3 реда, 3 скатера, ≈50 сек, до 50x, 5x–100x,
  Normal, 5x, 50x, 2 скатера, 96,05%, 95,06%, 3,95%, 500 000 €. PASS.
- No operator logos/names, no fake screenshots, no invented numbers. PASS.
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". PASS.
- Descriptive lowercase-hyphenated filename + specific Bulgarian ALT + caption. PASS.
Verdict: manual integrity PASS. images: 1 (infographic). Kept.

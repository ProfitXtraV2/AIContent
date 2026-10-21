# 08 — Gemini image review (pass 1) · Lightning Baccarat

Command: python3 scripts/gemini_image_review.py <article>/05b-final-draft.md <images…>
Result: SKIPPED — Gemini image API unavailable (HTTP 402 RESOURCE_EXHAUSTED, same outage as Step 7).

Image shipped: 1 hand-authored SVG infographic (lightning-baccarat-mnozhiteli-taksa-i-rtp-infografika.svg).
AI hero: SKIPPED (image gen offline, 402).

Manual integrity check (orchestrator):
- Every SVG number traces verbatim to 05b: 8 тестета, 20%, 1–5 карти, 2x/3x/4x/5x/8x, 1:1, 0,95:1, 5:1,
  98,59%, 98,76%, 94,51%, 512x, 262 144x, 500 000 €. PASS.
- No operator logos/names, no fake screenshots, no invented numbers. PASS.
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". PASS.
- Descriptive lowercase-hyphenated filename + specific Bulgarian ALT + caption. PASS.
Verdict: manual integrity PASS. images: 1 (infographic). Kept.

# 08 — Gemini image review (pass 1) · Extra Chilli Megaways

Command: python3 scripts/gemini_image_review.py <article>/05b-final-draft.md <images…>
Result: SKIPPED — Gemini image API unavailable (HTTP 402 RESOURCE_EXHAUSTED, same key/outage as Step 7).

Image shipped: 1 hand-authored SVG infographic
(extra-chilli-megaways-rtp-i-feature-buy-infografika.svg).
AI hero: SKIPPED (image gen offline, 402).

Manual integrity check (performed by orchestrator, since Gemini review offline):
- Every number in the SVG traces verbatim to 05b: 6, 117 649, 20 000x, €0,20–€50, 3 скатера,
  8 завъртания, +4, +1 без таван, 24 завъртания, ≈50x, 96,15%–96,41%, 96,26%–96,82%. PASS.
- No operator logos/names, no fake screenshots, no invented RTP/bonus/licence numbers. PASS.
- No people/faces, no glamorised winning; carries „18+ Играйте отговорно". PASS.
- Descriptive lowercase-hyphenated filename + specific Bulgarian ALT + caption. PASS.
Verdict: manual integrity PASS. images: 1 (infographic). Kept.

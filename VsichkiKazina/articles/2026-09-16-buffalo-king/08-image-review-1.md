# Step 8 — Gemini image review (pass 1)

**Result: SKIPPED — Gemini unavailable (same 429 credit depletion as Step-7).**

`python3 scripts/gemini_image_review.py` was not run because the Gemini `generateContent`
endpoint is out of prepayment credits this run (HTTP 429 RESOURCE_EXHAUSTED). Per daily-run.md
Step 8, an unavailable Gemini is the skip path: log `image review: skipped (Gemini
unavailable)` and keep the image(s); do not halt.

## Images shipped (hand-authored SVG, no API needed)
1. `images/buffalo-king-rtp.svg` — RTP versions (96,06% / 95,53% / 94,55%) + €1000→~€961/~€39 split.
2. `images/buffalo-king-besplatni-zavartania.svg` — free-spins trigger table (3/4/5/6 → 8/15/25/100, retrigger up to 200).

## Integrity self-check (the checks the Gemini review would run)
- Every number traces verbatim to 05b: 96,06%, 3,94%, 95,53%, 94,55%, €1000, ~€961, ~€39, 3/4/5/6, 8/15/25/100, 200. No invented figure.
- No operator logos / names / UI, no fake screenshots, no invented bonus/RTP/licence numbers.
- No people / faces, no glamorised winning; both carry „18+ Играйте отговорно".
- Rendered to PNG at display width and visually verified: no overlap, no clipping, ≥8px margins on all four sides (floating „3,94%" bar overlay removed after first render because it collided with the „Домашно предимство" header; the 3,94% figure still appears in the €39 card).

AI decorative hero: NOT generated (gemini_image_gen would 429). Article ships with the two
SVG infographics. Recommend an optional hero + a real Gemini image review once credits reset.

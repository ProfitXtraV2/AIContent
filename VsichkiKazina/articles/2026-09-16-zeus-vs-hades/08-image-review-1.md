# Step 8 — Gemini image review (pass 1)

**Result: SKIPPED — Gemini unavailable (same 429 credit depletion as Step-7).**

`python3 scripts/gemini_image_review.py` was not run because the Gemini `generateContent`
endpoint is out of prepayment credits this run (HTTP 429 RESOURCE_EXHAUSTED). Per daily-run.md
Step 8, an unavailable Gemini is the skip path: log `image review: skipped (Gemini
unavailable)` and keep the image(s); do not halt.

## Images shipped (hand-authored SVG, no API needed)
1. `images/zeus-vs-hades-rtp.svg` — RTP versions (96,07% / 95,05% / 94,05%) + €1000→~€961/~€39 split.
2. `images/zeus-vs-hades-god-mode.svg` — Olympus vs Hades comparison (frequency / average result / cap hit-rate 1 in 1 766 784 vs 1 in 1 335 113; same RTP).

## Integrity self-check (the checks the Gemini review would run)
- Every number traces verbatim to 05b: 96,07%, 95,05%, 94,05%, €1000, ~€961, ~€39,
  1 766 784, 1 335 113. No invented figure.
- No operator logos / names / UI, no fake screenshots, no invented bonus/RTP/licence numbers.
  (OLYMPUS / HADES are the game's own in-game mode names, not operator brands.)
- No people / faces, no glamorised winning; both carry „18+ Играйте отговорно".
- Rendered to PNG at display width and visually verified: no overlap, no clipping, ≥8px
  margins on all four sides (bottom banner font reduced 12,5→11,5 after first render for edge slack).

AI decorative hero: NOT generated (gemini_image_gen would 429). Article ships with the two
SVG infographics. Recommend an optional hero + a real Gemini image review once credits reset.

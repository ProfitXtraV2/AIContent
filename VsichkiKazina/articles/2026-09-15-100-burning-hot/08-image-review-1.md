# Image Review Pass 1 — 2026-09-15-100-burning-hot

Model: gemini-3.1-pro-preview (review, attempted) · image gen: gemini-3-pro-image (attempted)

## Images
- images/100-burning-hot-vs-baza.svg (hand-authored comparison, under H1)
- images/100-burning-hot-rtp.svg (hand-authored RTP infographic, in RTP section)

## Result — SKIPPED (Gemini unavailable)
- gemini_image_gen.py → HTTP 429 RESOURCE_EXHAUSTED for all models. Logged
  `image gen: skipped (Gemini unavailable)`; shipped two hand-authored SVGs (no AI hero).
- gemini_image_review.py → same 429. Logged `image review: skipped (Gemini unavailable)`; kept images.

## Integrity (manual, since automated review unavailable)
Both images are hand-authored SVG; every figure traces VERBATIM to 05b + official Amusnet data:
- Comparison: 5 lines (base, low vol) vs 100 lines (medium/level-3 vol), higher total bet, RTP unchanged, + Jackpot Cards — all stated in 05b.
- RTP infographic: 95.89% RTP, 4.11% house edge, €1000 turnover, ~€959 return / ~€41 split.
No operator logo/name (the four-leaf clover / seven / star are generic slot symbols, not operator
branding), no fake screenshot, no invented bonus/RTP number, no people/faces, no glamorised winning.
Both carry 18+/RG notes. 0 integrity issues.
images: 2 (comparison + RTP infographic, both SVG, review skipped 429, 0 integrity).

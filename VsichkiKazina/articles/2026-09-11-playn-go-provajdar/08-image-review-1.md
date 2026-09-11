# 08 — Gemini image review, pass 1

Model: gemini-3.1-pro-preview · run 11.09.2026
**SCORE: 75/100 — NEEDS WORK** (no integrity failure: no fabricated logos/numbers/screenshots, no people/faces, no glamorised winning)

## Images reviewed
- `images/playn-go-rtp-versii.svg` (infographic — reviewed as source; numbers checked vs 05b)
- `images/playn-go-hero.webp` (hero — reviewed as pixels)

## Gemini verbatim verdict
### Infographic
Problem: the percentage text labels straddle the right edge of the gray background tracks. The gray tracks end at x=560; the first row's label starts at x=549 and crosses the edge (half on gray, half on white). Dynamic placement at each bar's end makes the number column messy/unaligned.
Fix: move all five percentage labels to a fixed x outside/right of the gray tracks (x≈570) for a clean right-aligned column that does not overlap the bars.

### Hero
None. "Excellent, highly relevant image." Perfectly abstracts the two mechanics (3 reel columns = "book" reels; connected squares = Reactoonz cluster grid). High integrity (no fake UI, no faces, no hype), clean quality, filename + Bulgarian ALT accurate. Ready to publish as-is.

## Action
Hero: keep (PASS quality, would score high alone). Infographic: hand-fix label x → 570 (numbers still trace to 05b: 96.21/94.25/91.25/87.25/84.18), then re-review. Pass 2 follows.

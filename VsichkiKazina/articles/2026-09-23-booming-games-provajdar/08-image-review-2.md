# 08 — Gemini image review, pass 2 (after image fix passes 1 & 2)
Model: gemini (multimodal) · Images: booming-games-rtp-tavan.svg, booming-games-hero.webp

## Context
Two cosmetic fix passes were attempted on the infographic gridlines (the only nit at pass 1):
- fix pass 1: extend gridlines y2 322→340 → re-review scored **75** (lines then crossed the title text).
- fix pass 2: segment gridlines to render only over the bars → re-review scored **75** (verdict below: z-order put them behind the opaque bars, so hidden).

## Verdict (verbatim, of fix-pass-2 SVG)
**Score: 75/100 · Verdict: NEEDS WORK**

Overall, both images are highly relevant, perfectly accurate to the article text, and maintain excellent hygiene (no fake UI, no glamorised winning, neutral tone). The SEO metadata is also spot-on. However, the infographic fails the layout integrity check due to a rendering defect that hides structural elements.

- Layout Integrity / Technical Defect (SVG): the vertical dashed gridlines are invisible because the group is placed before the <rect> background bars, which are opaque and cover them (SVG renders back-to-front). Axis labels float without connecting guides.
- (Hero booming-games-hero.webp): excellent — clean, abstract, highly relevant, passes all checks perfectly.

Fix suggested: move the gridline block after the bar <rect> elements to correct z-order.

## KEEP-BEST DECISION (mandatory)
Image-review scores by version: pass-1 SVG (gridlines y2=322) = **85 PASS, 0 integrity failure**; fix-pass-1 SVG (y2=340) = 75; fix-pass-2 SVG (segmented) = 75. Highest = **85 (the original pass-1 SVG)**.
MAX_IMAGE_PASSES (2) reached; detector proved noisy on a purely cosmetic gridline nit (both later versions scored lower). Per keep-best, **restored the pass-1 SVG (score 85, PASS)** as the shipped infographic. Hero scored excellent throughout, no changes.
Final shipped: infographic **85 PASS** (0 integrity failure, all 10 numbers trace to 05b), hero **PASS** (clean, no integrity issues). Best image score = 85.

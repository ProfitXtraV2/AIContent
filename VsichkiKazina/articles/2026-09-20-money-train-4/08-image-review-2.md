# 08 — Gemini image review, pass 2 (gemini_image_review.py, vision)

Applied pass-1 fixes: shortened the two bottom stat-tile subtexts (SVG), and regenerated the AI hero toward the article's sci-fi/neon theme.

## Intermediate re-review (after first fixes)
Score **75/100** NEEDS WORK. Hero: approved (sci-fi theme matched, integrity clean). SVG: descenders of the bottom subtexts in the two middle €-boxes (baseline y=276, box bottom y=279) touched the box's inner edge → layout-integrity defect. Fix applied: raised the two €-box heights 74→84 and re-centred their text (headers y=235, values y=265, subtexts y=281), giving ~5px descender margin.

## Final review (after box fix)
Score: **100/100** · Verdict: **PASS** (both images, zero integrity failures, zero layout defects).
- `money-train-4-rtp-cena.svg` — every number matches 05b exactly (96.10% RTP, ~€961, ~€39, 100×/500× цена, 150 000× таван, €0.10–€6 залог, 5/5 волатилност). Text mathematically centred, no overlap, no clipping, 18+ note present, ALT/aria-label detailed. Ready to publish.
- `money-train-4-hero.webp` — on-theme dystopian sci-fi industrial train (ръждив метал, неон); no fake UI, no fabricated logos, no faces, no glamorised winning; descriptive filename + specific Bulgarian ALT. Ready to publish.

## Keep-best decision
Final versions kept (highest-scoring seen): infographic 100, hero 100. images: 2 (infographic 100, hero 100). Within MAX_IMAGE_PASSES (2 fix passes).

# 08 — Gemini image review, pass 1 (Bell Link)

Command: `python3 scripts/gemini_image_review.py .../05b-final-draft.md images/bell-link-levels.svg images/bell-link-hero.webp`
Model: gemini-3.1-pro-preview · Exit 0

## Verbatim verdict
- **bell-link-levels.svg (infographic): Score 85/100 — PASS.** "Perfectly maps the four jackpot levels (Grand/Major progressive, Minor/Mini fixed at ~50x and ~10x) and the 5-bell trigger exactly as stated in the text." Neutral/RG tone, 18+ line, no fake UI. Specific problems: None. Ready to publish.
- **bell-link-hero.webp (raster): Score 85/100 — PASS.** "5x3 grid with exactly 5 illuminated bells smartly visualizes the '5 or more bells' trigger without a fake screenshot." Abstract, muted, no operator logos / no fabricated UI / no glamorised winning. Specific problems: None.

0 integrity issues on both (no fabricated logo/number/screenshot, no people/faces, no glamorised winning). Both ≥ IMAGE_TARGET_SCORE (80).

## Keep-best
- infographic 85, hero 85 (pass 1). Both PASS on first pass, 0 fix passes. images: 2, best 85.

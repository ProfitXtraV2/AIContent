# Step 8 — Gemini image review, pass 1

Model: gemini vision (scripts/gemini_image_review.py). SVGs rendered to PNG + source; hero as pixels. Reviewed against 05b.

- `images/fruit-party-rtp.svg` — **45/100 NEEDS WORK**. Layout collision: „3.50%" (y=82) overlaps the right-anchored header „Домашно предимство" (y=80). Fix: move the „3.50%" label off that line (below the bar, clear of the header and the dashed divider). No integrity/number problem — figures (96.50%, 3.50%, €1000, €965, €35, 95.50%, 94.50%) all match 05b.
- `images/fruit-party-mnozhiteli.svg` — **75/100**. Reviewer: „None required. Ready to publish." Layout clean, margins respected, data (x2 base, x2/x4 free spins, 256x cap) matches 05b exactly, SEO metadata accurate. Below the 80 target but no actionable critique and no integrity/layout failure → keep-best (no lower-risk edit available).
- `images/fruit-party-hero.webp` — **55/100 NEEDS WORK**. Misleading visual: the prominent connecting line across the grid contradicts the article's core point („тук няма линии на печалба… карта от петна, не пътечки"). Fix: regenerate with a prompt that excludes lines/graphs/connecting paths and instead shows a clean grid with clusters of adjacent matching-colour dots.

Result pass 1: 1 clean-ish (75), 2 need work (45 rtp layout, 55 hero misleading line). No integrity failure on any. → pass 2: hand-fix rtp SVG, regenerate hero; keep mnozhiteli.

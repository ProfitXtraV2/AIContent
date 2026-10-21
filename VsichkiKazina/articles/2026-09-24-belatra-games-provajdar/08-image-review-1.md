# 08 — Gemini image review · pass 1

Model: gemini-3.1-pro-preview. Images: belatra-games-rtp.svg (SVG source), belatra-games-hero.webp (raster).

**Score: 65/100 — NEEDS WORK** (no hard integrity failure; fixable defects)

### Problems flagged
1. **Accuracy (SVG):** footer line invented a source citation (`източник: SlotCatalog / ClashOfSlots / SlotsMate`) the article body does not name. Remove it.
2. **Layout collision (SVG):** subtitle (y=53) descenders clip the `~96%` reference label (y=64).
3. **Raster artifact (hero):** middle reel's third column (crowns) missing its cream background — reads as broken.
4. **Raster framing (hero):** harsh white rectangular corner cutouts bottom-left/right.

### Fixes applied (pass 1)
- SVG: footer reduced to `Скала 95.50%–97.50%` (sources live in 06-verification, not invented on the graphic).
- SVG: `~96%` label moved y=64→76, dashed line y1=70→82 (6px clean gap).
- Hero: regenerated with a prompt enforcing consistent cream background behind all reels, full-bleed dark green, no white borders/corner cutouts.

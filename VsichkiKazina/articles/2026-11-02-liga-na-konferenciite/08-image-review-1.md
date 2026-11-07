# 08 — Image review · pass 1

**Score: 100/100 — PASS** (≥ 80, 0 integrity failures). Pass 1, no iteration needed.

Images reviewed:
1. `images/liga-na-konferenciite-format.svg` — data infographic (hand-authored SVG; reviewed as
   source so numbers are checked).
2. `images/liga-na-konferenciite-hero.webp` — decorative hero (13.6 KB WebP; gemini-3-pro-image
   PNG → ImageMagick `convert` → WebP, Pillow unavailable).

Gemini verdict (verbatim summary):
- **Infographic:** all numbers match the article text exactly (36 отбора, 6 мача, 3+3, класиране
  1–8 / 9–24 / 25–36; „По титли: Англия — 3" correct for West Ham/Chelsea/Crystal Palace). Clean
  design, no fake team/bookmaker logos. „18+ Играйте отговорно" footer present. Descriptive
  lowercase-hyphenated filename; thorough BG ALT + correct aria-label. No element overlap on render.
- **Hero:** vector illustration, no faces, no brands, no fake UI, no glamorised winning; empty
  stadium reads calm/neutral (RG-aligned). Correct filename; literal, accurate BG ALT; 16:9.
- **Integrity / hygiene:** 0 fabricated logos/numbers/screenshots, 0 people/faces, 0 glamorised
  winning. "Не са открити никакви проблеми. Изображенията са напълно готови."

**Keep-best:** both kept (first-pass PASS). Final image count: 2 (infographic 100, hero 100).
Both referenced from 05b-final-draft.md (hero under H1, infographic beside the format section
with a one-line caption). Every figure in the infographic traces verbatim to 05b.

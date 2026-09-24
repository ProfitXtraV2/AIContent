# 08 — Gemini image review · pass 1

Model: gemini-3.1-pro-preview. Images: apollo-games-max-win.svg (SVG source), apollo-games-hero.webp (raster).

**Score: 95/100 — PASS.** No integrity failures. Both images kept (single pass; 95 well above target).

- **Accuracy (SVG):** flawless — every max-win figure matches the article table (2,000x / 500x /
  500x / 500x / 316x / 174x); bar widths correctly scaled (500x = 25% of 2,000x; 316x = 60px).
- **Integrity/hygiene:** no fake logos/UI, no glamorised winning. The stylized Joker is contextually
  a standard game symbol („жокери" is named in the article), NOT a human face → avoids auto-fail.
- **Responsible gambling:** neutral; graphic carries „таванът е рядък резултат, не очаквана печалба"
  + „18+ Играйте отговорно".
- **SEO metadata:** filenames lowercase-hyphenated; ALT/aria specific Bulgarian, matches article.
- **Layout:** no overlaps/clipping; safe margins both sides of the 640px canvas.
- **Optional-only note (not acted on):** hero depicts a 3-reel classic vs the text's 4×3/5×3 mention —
  flagged as „optional perfectionism", not an integrity or quality failure; kept the strong 95 asset.

# Image Review Pass 1 — keno-pravila

**Script:** `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-08-keno-pravila/05b-final-draft.md keno-igra-hero.webp keno-domashno-predimstvo-sravnenie.svg`

**Score: 70/100**
**Verdict:** `NEEDS WORK`

### Specific Problems

*   **Accuracy (Raster Image):** The article explicitly states that Keno is played on a board with 80 numbers ("поле с числа от 1 до 80"), and the provided ALT text claims the image shows exactly that ("решетка с 80 клетки"). However, the generated image clearly depicts a 10x6 grid, which equals only 60 cells. This is a factual misrepresentation of the game's core mechanic.
*   **Visual Clarity (SVG Infographic):** The label `<65%–>96%` for Online Keno is mathematically accurate to the text (which states a house edge from <4% to >35%), but the formatting with opposing less-than/greater-than signs is slightly clunky to read at a quick glance.

### Actionable Fixes

*   **Raster Image (keno-igra-hero.webp):** Regenerate the AI image. Update your prompt to strictly specify the grid dimensions: *"A casino keno grid with exactly 8 rows and 10 columns (80 squares total). Exactly 20 of the squares are glowing/lit."*
*   **SVG Infographic (keno-domashno-predimstvo-sravnenie.svg):** The SVG is excellent, perfectly matches the article's data, and passes all integrity/hygiene checks. No structural changes are needed.

### Pipeline decision

Hero regenerated (pass 2). SVG kept as-is.

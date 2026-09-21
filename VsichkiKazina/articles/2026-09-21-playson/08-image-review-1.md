# 08 — Image review, pass 1 (Playson, vk-0140)

Command: `python3 scripts/gemini_image_review.py 05b-final-draft.md images/playson-hold-and-win.svg images/playson-hero.webp`
Model: multimodal Gemini · Exit: 0
Result: **Score 75 — NEEDS WORK.** No prohibited-content integrity failure (no fake UI, logos, faces, or glamorised winning; SVG layout clean, no overlap/clipping). Two accuracy fixes required → iterate (pass 1 of ≤ 2).

## Verbatim verdict

**Score: 75**
**Verdict: NEEDS WORK**

### Specific Problems

**1. Accuracy / Invented Facts (SVG Infographic) — CRITICAL FAILURE**
The infographic invents descriptions for the Major and Minor jackpots that directly contradict or are unsupported by the article text.
*   **The error:** The SVG labels the Minor jackpot as `среден · по-чест` (medium) and the Major jackpot as `голям · по-рядък` (big).
*   **The text:** The article explicitly states, *"Долните падат по-често и са малки"* (The bottom ones fall more often and are small). By calling Minor "medium" and Major "big", the graphic is inventing tiers that the text does not support, and directly contradicting the fact that the bottom jackpots (plural) are "small".

**2. SEO Metadata Mismatch (WebP Image)**
The ALT text for the raster image (`playson-hero.webp`) describes the visual as accumulating a jackpot *"в долния ъгъл"* (in the bottom corner). However, the actual image depicts a vertical progress meter on the **right side**, not in the bottom corner.

*(Note: The technical layout, margins, and rendering of the SVG are otherwise excellent, with no overlapping text or clipped edges. The raster image is clean, abstract, and free of fake UI or prohibited elements.)*

### Actionable Fixes

**For the SVG Infographic:**
Update the text nodes for the Major and Minor jackpots to strictly align with the article's phrasing, removing the invented "medium" and "big" adjectives.
*   Change `<text x="642" y="296"...>голям · по-рядък</text>` to `<text x="642" y="296"...>по-рядък</text>` (or remove the description entirely).
*   Change `<text x="642" y="348"...>среден · по-чест</text>` to `<text x="642" y="348"...>малък · по-чест</text>`.

**For the WebP Image:**
Update the Bulgarian ALT text in the CMS to accurately reflect the image provided. Change *"трупа нарастващ джакпот в долния ъгъл"* to *"трупа нарастващ джакпот чрез вертикален брояч вдясно"* (accumulates a growing jackpot via a vertical meter on the right).

## Fixes applied (pass 1)
- SVG: Major `голям · по-рядък` → `по-рядък`; Minor `среден · по-чест` → `малък · по-чест`. Now only text-supported wording (Grand = strongest/rare at top; „долните ... са малки"; frequency increases downward). Numbers untouched (6+, 3, 15, four named jackpots).
- Hero ALT in 05b: „...трупа нарастващ джакпот в долния ъгъл" → „...докато вертикален брояч вдясно трупа нарастващ джакпот" (matches the rendered image).

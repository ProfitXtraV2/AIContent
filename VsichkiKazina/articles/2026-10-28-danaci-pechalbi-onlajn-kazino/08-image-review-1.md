# Step 8 — Gemini image review, pass 1 — danaci-pechalbi-onlajn-kazino

Images: danak-pechalba-hazart-hero.webp (18KB, 1280x714) + danak-pechalba-hazart-licenz-reshenie.svg
Result: 75/100 NEEDS WORK — no integrity failure (no fabrication/person/logo/glamorised win). Only flaw: SVG ДА/НЕ branch labels overlapped the arrow lines. Fix applied (nudged labels + white backing).

---
## Gemini verbatim verdict

**Score: 75/100**
**Verdict:** `NEEDS WORK`

Overall, the visual assets are highly relevant, perfectly aligned with the article's neutral YMYL tone, and contain excellent SEO metadata (descriptive, hyphenated filenames and accurate Bulgarian ALT text). The raster image is clean, conceptual, and free of any prohibited elements (no faces, fake UI, or glamorized winning). The SVG infographic is factually flawless and matches the article text exactly. 

However, the SVG fails the strict layout integrity check due to text colliding with structural elements.

### Specific Problems

*   **Layout Integrity / Element Collision (SVG):** The branch labels **"ДА"** and **"НЕ"** are placed directly on top of the diagonal arrow lines, causing a visual overlap. 
    *   The "ДА" text at `x="222" y="204"` sits exactly where the left arrow line passes through (the line's Y-coordinate at `x=222` is roughly `202.5`, cutting right through the bottom half of the letters).
    *   The "НЕ" text at `x="498" y="204"` suffers the exact same collision with the right arrow line.

### Actionable Fixes

*   **For the SVG Infographic:** Nudge the `x` and `y` coordinates of the "ДА" and "НЕ" `<text>` elements so they sit comfortably in the negative space above and to the outside of the arrows, rather than intersecting them. 
    *   Change the "ДА" coordinates to roughly `x="210" y="190"`.
    *   Change the "НЕ" coordinates to roughly `x="510" y="190"`.
    *   *(Alternatively, you can add a white `<rect>` or `stroke` behind the text elements to act as a mask and break the line, but simply moving the text is cleaner).* 
*   **For the Raster Image:** No changes needed. It is ready to publish.

# Step 8 — Gemini image review (pass 1) · vk-0295
Command: `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-10-27-belot-onlayn/05b-final-draft.md images/belot-onlayn-hero.webp images/belot-onlayn-platformi-sravnenie.svg`
Date: 2026-10-27

Score: 75 (NEEDS WORK). Hero: PASS (no fixes). Infographic: one accuracy flag — label "турнири" not stated in 05b. No integrity failure (no fabricated number/logo/face). Fix: remove "турнири" so every label traces to 05b, then re-review.

## Gemini verbatim review

**Score: 75**
**Verdict:** `NEEDS WORK`

**Specific Problems:**
*   **Accuracy (Infographic):** The SVG infographic includes the word **"турнири"** (tournaments) in the Belot.BG card under the "РЕЖИМИ" section (`<text x="40" y="291"...>с приятели, турнири</text>`). The provided article text mentions playing against people, bots, and friends, but it *never* mentions tournaments. This violates the strict rule that every label must match the article text exactly.
*   **Raster Image & Metadata:** The hero image (`belot-onlayn-hero.webp`) is excellent. It perfectly matches the neutral, responsible gambling tone, contains no fake UI or faces, and the ALT text and filename are perfectly optimized and accurate. The layout of the SVG is also technically sound with no overlapping or clipped text. 

**Actionable Fixes:**
*   **For the Infographic (SVG):** Edit line 21 of the SVG code. Change `<text x="40" y="291" fill="#dce8f4" font-size="13">с приятели, турнири</text>` to `<text x="40" y="291" fill="#dce8f4" font-size="13">с приятели</text>`. This will perfectly align the image with the article's supported facts. 
*   **For the Raster Image:** No changes needed. It is ready to publish.


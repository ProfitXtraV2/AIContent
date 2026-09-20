# Step-8 image review — pass 1 (Jackpot Cards)

Reviewed: jackpot-cards-levels.svg (infographic) + jackpot-cards-hero.webp (decorative hero).
Infographic 85/PASS (minor bottom-text margin nit), hero 85/PASS. 0 integrity issues (suit hierarchy matches text, no fabricated logos/UI/amounts, no faces, no glamorised winning).

### Image 1: `jackpot-cards-levels.svg`

**Score:** 85/100  
**Verdict:** PASS  

**Problems:**
*   **Layout / Margins:** The bottom text (`Бонус: 12 обърнати карти...`) is ~73 characters long. At `font-size="12.5"`, it takes up nearly the entire 480px width of its background `<rect>`, risking edge-touching or clipping on systems with wider default sans-serif fonts. 
*   **Visual Consistency:** The label "най-голямото ниво" is placed inside the purple bar, while "най-малкото ниво" is placed outside the blue bar. 

**Fixes:**
*   **SVG:** Reduce the `font-size` of the bottom text to `11.5` or widen its `<rect>` to `520` (`x="40"`) to guarantee safe margins.
*   **SVG:** For consistency, either move the Rung 1 text inside its bar (adjusting `x` and `text-anchor`) or leave as-is if the external placement was an intentional design choice to accommodate the shorter bar.

---

### Image 2: `jackpot-cards-hero.webp`

**Score:** 85/100  
**Verdict:** PASS  

**Problems:**
*   None significant. The image accurately reflects the specific suit hierarchy described in the text (Club lowest -> Spade highest) using a clean, abstract visual metaphor. 
*   SEO metadata (filename and ALT text) is accurate, descriptive, and properly formatted.
*   Tone is neutral and appropriate for responsible gambling (no glamorization, no fake UI).

**Fixes:**
*   None required. Ready to publish.

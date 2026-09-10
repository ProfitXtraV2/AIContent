# Image Review Pass 2 — keno-pravila

**Script:** `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-08-keno-pravila/05b-final-draft.md keno-igra-hero.webp keno-domashno-predimstvo-sravnenie.svg`

## Image 1: Raster hero (`keno-igra-hero.webp`)

**Score: 40/100**
**Verdict:** `NEEDS WORK`

**Problems:**
*   **Factual inaccuracy:** The regenerated image shows a 14-column × 7-row = 98-cell grid instead of 10×8 = 80 cells. Exactly 14 glowing cells instead of 20. AI image generation consistently fails to count grid cells accurately.
*   **SEO metadata:** ALT text claimed "80 клетки" but the visual did not match.

**Pipeline decision:** 2 passes exhausted (best hero score: 70/100 from pass 1). Hero dropped per `keep-best` rule — no version cleared the 80-point threshold. No integrity failure in the strict sense, but AI can't reliably depict correct keno board dimensions. Hero file deleted.

---

## Image 2: SVG Infographic (`keno-domashno-predimstvo-sravnenie.svg`)

**Score: 100/100**
**Verdict:** `PASS`

**Notes:** All numbers match the article text exactly. Clean design, proper hygiene, RG note present, SVG semantics correct. Ready to publish.

---

## Final disposition

- `keno-domashno-predimstvo-sravnenie.svg` — **PASS (100/100)** — shipped
- `keno-igra-hero.webp` — **DROPPED** (best: 70/100, below threshold; AI grid-count hallucination)
- Shipping SVG infographic alone.

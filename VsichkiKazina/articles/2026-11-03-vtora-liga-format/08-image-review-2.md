# Step 8 — Gemini image review — pass 2 (after infographic wording fix)

Command: `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-11-03-vtora-liga-format/05b-final-draft.md images/vtora-liga-piramida-promociq-izpadane.svg images/vtora-liga-piramida-hero.webp`
Date (UTC): 2026-11-03

## Result
**Score: 70 — NEEDS WORK** (< 80). No integrity failure (no fabricated logos/numbers/screenshots, no people/faces, no glamorised winning).
- **SVG infographic: now EXCELLENT** — the pass-1 wording fix resolved the only accuracy issue; facts match 05b, layout clean, no clipping/overlap, SEO metadata accurate. Ready to publish.
- **Hero (raster): flagged** — the sweeping arrows go directly bottom-tier → top-tier (and top → bottom), which visually implies teams bypass the middle tier. Since the article is about the middle tier (Втора лига), the reviewer finds the hero conceptually misleading.

## Keep-best ledger (image set)
- pass 1: score 75 (SVG wording)
- pass 2: score 70 (hero relevance)

## Gemini verbatim verdict

**Score: 70**
**Verdict: NEEDS WORK**

**Specific Problems:**
*   **Accuracy / Relevance (Raster Image):** The hero image (vtora-liga-piramida-hero.webp) is conceptually misleading for this specific article. The illustration shows a green arrow jumping directly from the bottom tier (Third League) to the top tier (First League), and a grey arrow dropping directly from the top to the bottom. This visually implies that teams bypass the middle tier entirely. Since the article is explicitly about the mechanics of the Second League (the middle tier) and how teams must pass through it, this image contradicts the core subject matter.
*   **SVG Infographic:** The SVG is excellent. It perfectly matches the article's facts, the layout is clean with no overlapping or clipped text, the typography has comfortable margins, and the SEO metadata is accurate.

**Concrete, Actionable Fixes:**
*   **For the Hero Image (AI Prompt/Redesign):** Generate a new image specifying step-by-step movement (arrows moving one step at a time between adjacent tiers), and/or highlight the middle platform to anchor the visual to the Second League.
*   **For the SVG Infographic:** No changes required. Ready to publish as-is.

## Action taken
Final image pass (MAX_IMAGE_PASSES=2): regenerate the hero with a step-by-step-arrows prompt that highlights the middle tier. If the regenerated hero still scores below 80 or is not clearly better, keep the best-scoring hero / drop it and ship the excellent infographic alone (never block the PR on a decorative image).

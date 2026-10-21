# Step 8 — Gemini image review, pass 1

Model: gemini-3.1-pro-preview (raster as pixels; SVG as source)
Images: `images/betsoft-rtp.svg`, `images/betsoft-hero.webp`

**Score: 92/100 · Verdict: PASS** · 0 integrity failures. Two minor optional fixes noted → applied a fix pass (see 08-image-review-2.md).

---

Excellent set of visuals. Raster is clean/abstract/relevant (no fake UI, faces, glamorised winning). SVG matches the article math and adds value. SEO metadata and ALT texts spot-on.

Minor notes (fixed in pass 2):
1. **SVG corner glitch:** green bar had `rx="8"` while the adjacent orange segment had square corners → tiny background gap / edge poke. Fix: remove `rx` from the background + green bars (square, flush).
2. **Phrasing:** „не пипат" is slightly informal → „не променят" (aligns with the article's „не мени RTP").

Raster: no changes needed.

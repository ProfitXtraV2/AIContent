# 08 — Gemini image review — pass 2 (after SVG fix 1)

**Score: 75/100 — Verdict: NEEDS WORK. 0 integrity failures.** (2 of MAX_IMAGE_PASSES=2.)

Gemini's verbatim verdict:

---

**Score: 75 — Verdict: NEEDS WORK**

**1. Layout Integrity / Text Collisions (SVG Infographic):** critical layout failure in the right column. The year labels „1980/81" and „1982/83" at x=448 with text-anchor=middle at 23px span ~95–100px (x≈398→498).
*   Left Collision: left edge touches/overlaps the vertical divider at x=400.
*   Right Collision: right edge touches the description labels („първо издание"/„официален статут") starting at x=500, zero margin.

*(Note: the raster hero kupa-na-balgariya-trofej-hero.webp is excellent — relevant, clean, no RG violations or fake UI, ALT/SEO perfect. The failing score is entirely the SVG layout defect.)*

**Fix:** change right-column `.big` x=448→460 and right-column `.lbl` x=500→530 (or left-anchor the years at x=420, labels x=520).

---

**Integrity:** PASS (0 fabricated logos/numbers/screenshots, 0 faces/people, 0 glamorised winning). Still purely a layout issue; numbers trace to 05b.

**Action (fix pass 2):** applied Gemini's exact coordinates with extra margin — right-column `.big` x=448→462 (middle), right-column `.lbl` x=500→532, year font 23px→22px. Years now span ~419–505 (≈19px gap from divider x=400, ≈27px gap from labels x=532). Numbers unchanged. Re-review to confirm.

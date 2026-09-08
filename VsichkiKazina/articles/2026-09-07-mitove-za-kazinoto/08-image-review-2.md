# Image Review Pass 2 — mitove-za-kazinoto

**Script:** `python3 scripts/gemini_image_review.py VsichkiKazina/articles/2026-09-07-mitove-za-kazinoto/05b-final-draft.md mitove-kazino-domashno-predimstvo-hero.webp martingale-progresiya-tavan.svg`

**Combined Score: 45/100 — NEEDS WORK**

### Hero (mitove-kazino-domashno-predimstvo-hero.webp): AUTOMATIC FAIL

**Integrity failure:** The scale weight on the hero image contains a geometric 3D cube/hexagon symbol that looks like a fabricated corporate or crypto logo. Per rules, any fabricated brand/operator logo is an automatic fail regardless of visual polish.

**Pipeline decision:** Hero DROPPED (integrity failure, cannot ship). No further regeneration — 2 passes exhausted.

---

### SVG (martingale-progresiya-tavan.svg): Visual position issue (minor)

**Problem:** "ТАВАН НА МАСАТА €500" label rect was at y=198 (corresponding to ~€572 on the scale), so the 10th bet bar (€512) appeared below the limit visually.

**Fix applied:** Moved label rect from y=198 to y=205, text from y=209 to y=216 — now at true €500 position. No data change; all numbers still trace to 05b.

---

## Final disposition

- `martingale-progresiya-tavan.svg` — **shipped** (SVG label position fixed; all numbers from article text)
- `mitove-kazino-domashno-predimstvo-hero.webp` — **DROPPED** (integrity failure: fabricated logo on scale weight)
- Shipping SVG infographic alone. Best review score for SVG: 100 → note: individual SVG score not isolated in pass 2 combined review; previous pass confirmed SVG accuracy.

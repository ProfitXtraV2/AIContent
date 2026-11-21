# 08 — Gemini image review · pass 1 · vk-0341 Етър Велико Търново
**Image:** images/etar-veliko-tarnovo-v-chisla.svg (data infographic, SVG source reviewed)
**Script:** `python3 scripts/gemini_image_review.py 05b-final-draft.md images/etar-veliko-tarnovo-v-chisla.svg` · exit 0 · GEMINI ONLINE
**Score: 75 · Verdict: NEEDS WORK** (< 80). No integrity failure (no fabricated logos/numbers/screenshots, no people/faces, no glamorised winning).

---

**Score: 75**
**Verdict: NEEDS WORK**

**Specific Problems:**
1. **Layout Integrity (Collision / Margin Defect):** In the right column, the bold text `Г. Василев` (font size 23px, weight 800) is approximately 130-135 pixels wide. Placed at `x="500"`, it extends to `~635`, leaving virtually zero margin before the label `треньор на титлата` at `x="640"`. The text will visually touch or collide, violating the clear margins rule.
2. **Accuracy (Unsupported Fact):** The first line of the footer reads "Виолетово-бели" (Violet-white). The article text only mentions "Виолетовата фланелка" (Violet shirt) and the nickname "Виолетовите" (The Violets). The addition of white ("бели") is an external fact not supported by the provided text.

**Concrete, Actionable Fixes:**
* Increase the margin for "Г. Василев" / its label.
* Change footer "Виолетово-бели" to strictly reflect the article's text.

---

## Fix applied (pass 1 → draft for pass 2)
1. **Layout:** shortened the coach value from `Г. Василев` to `Василев` (narrower big element, r≈598), leaving a clean ~42px gap before the label at x=640; the longest label (Купа на шампионите, Кайзерслаутерн) stays at r≈903, inside the card edge (931). Chromium re-render confirms 0 collision / 0 clip.
2. **Accuracy:** footer `Виолетово-бели` → `Виолетови` (matches the article's „Виолетовата фланелка" / „Виолетовите"; „бели" removed as unsupported).
No number changed (every value still traces 1:1 to 05b). Re-review follows.

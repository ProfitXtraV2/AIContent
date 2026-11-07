# 08 — Image review (pass 2) + final decision — Снукър: правила и точкуване

## Pass 2 (after hero regen) — combined score 45/100 NEEDS WORK

Command: gemini_image_review.py 05b images/snooker-topki-tochki.svg images/snooker-masa-hero.webp, exit 0.
Infographic = PASS/excellent again (numbers 1:1, no overlap/clip). Hero v2 scored LOWER than v1: the reviewer now holds the DECORATIVE hero to strict snooker accuracy (the "D" semicircle vs a full circle, an exact 22-ball count, official colour spots) and says it "cannot be published in a factual guide". An AI decorative hero cannot reliably satisfy strict rules-accuracy; image models garble exact counts/spots.

## Decision (MAX_IMAGE_PASSES=2 reached): SHIP INFOGRAPHIC ALONE, DROP HERO

Per Step-8 keep-best + policy ("an accurate infographic beats a decorative image"; "ship the infographic alone"; "never let images block the PR"): the hero is dropped (removed from 05b + file deleted) rather than ship an image the cross-model reviewer flags as misleading in a factual guide. This is NOT one of the integrity-failure categories (no fake logos/numbers/people/glamorised winning) — it is a factual-looseness call, resolved by dropping. Hero v1=65, v2=45; neither clears the accuracy objection, so keep-best = no hero.

## Final shipped image — infographic-only confirmation review: 100/100 PASS

images: 1 (infographic 100). 0 integrity failures.

---
## Verbatim — pass 2 (two images)

**Score: 45/100**
**Verdict: NEEDS WORK**

The SVG infographic is excellent and perfectly aligned with the text, but the raster hero image (`snooker-masa-hero.webp`) is a hallucinated AI generation that fundamentally contradicts the article's specific rules and dimensions. It cannot be published in a factual guide.

### Specific Problems

1. **Accuracy (Raster Image) — Incorrect Table Markings:** The article explicitly states that behind the baulk line there is a "small semi-circle... called 'D'" (*малък полукръг... наречен „D"*). The image depicts a **full circle** intersecting the line, making it look like a soccer pitch rather than a snooker table.
2. **Accuracy (Raster Image) — Incorrect Ball Count:** The article clearly states there are exactly 22 balls: 15 red, 6 colors, and 1 white. The image shows **23 balls**: the 15 reds in the triangle, plus 8 other balls scattered around (including what appears to be two brown/dark orange balls). 
3. **Accuracy (Raster Image) — Incorrect Ball Placement:** The colored balls are scattered in a random, symmetrical pattern. In snooker, the colors have strict designated spots (e.g., the pink goes at the apex of the red pyramid, the black goes behind it, and the yellow, green, and brown sit on the straight line of the "D"). 
4. **Layout Integrity (SVG Infographic):** No issues found. The SVG is perfectly executed. All numbers match the text exactly (147 calculation, ball values, table dimensions), the layout is clean, and no text overlaps or clips the edges of the 820x470 canvas.

### Concrete, Actionable Fixes

*   **For the AI Raster Image (`snooker-masa-hero.webp`):** You must regenerate or manually edit this image. 
    *   *If regenerating via AI, use this prompt:* "Flat vector illustration of a snooker table from top down. The table must have a straight baulk line with a **semi-circle** (the 'D') on one side, NOT a full circle. Show exactly 22 balls: a triangle of 15 red balls, and exactly 6 colored balls (yellow, green, brown, blue, pink, black) placed on their official spots, plus 1 white cue ball. Minimalist green tones, no people, no text."
    *   *If editing manually:* Erase the right half of the center circle so it becomes a proper "D" semi-circle. Delete the extra colored balls so there are only 6 colors plus the white cue ball, and move them to their correct snooker spots.
*   **For the SVG Infographic (`snooker-topki-tochki.svg`):** No changes required. It is ready to publish as-is.

---
## Verbatim — final infographic-only review

**Оценка: 100/100**
**Присъда:** `PASS`

Инфографиката е изработена безупречно и отговаря на всички изисквания за качество, точност и SEO. 

**Анализ по критерии (няма открити проблеми):**
*   **Релевантност и стойност:** Изображението е изключително полезно, тъй като визуализира най-важната техническа част от статията – стойността на топките и математиката зад максималния брейк от 147 точки.
*   **Точност:** Всички числа (1 до 7 за топките, 15 червени, 120 точки, 27 точки от цветни, общо 147, 22 топки, 12х6 фута маса, фал от 4 точки) съвпадат абсолютно точно с подадения текст.
*   **Интегритет и хигиена:** Напълно изчистен дизайн. Няма фалшиви лога, измислени промоции, лица или елементи, глорифициращи хазарта.
*   **Отговорна игра:** Тонът е неутрален и образователен. Включено е задължителното съобщение „18+ Играйте отговорно“ във футъра.
*   **SEO метаданни:** Името на файла (`snooker-topki-tochki.svg`) е правилно форматирано (малки букви, тирета). ALT текстът в Markdown кода и `aria-label` атрибутът в самия SVG са описателни, точни и на български език.
*   **Техническо качество и лейаут:** SVG кодът е чист и отлично структуриран. Няма припокриващи се текстове. Всички елементи (кръгове за топките, заглавия, изчисления) са перфектно центрирани и подравнени. Отстоянията (margins/padding) до ръбовете на платното са достатъчни, гарантирайки, че нито един символ няма да бъде отрязан при рендиране на различни екрани. Цветовете на топките имат отличен контраст с цифрите в тях.

**Конкретни действия за корекция:**
*   Не са необходими никакви корекции. Изображението е готово за публикуване.

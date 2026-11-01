# Step 8 — Gemini image review, pass 1

**Script:** `python3 scripts/gemini_image_review.py 05b-final-draft.md <hero.webp> <podredba.svg> <tri-igri.svg>`
**Score:** 65/100 — NEEDS WORK (blended; dragged down by the decorative hero only)
**Integrity:** no fabricated logos/numbers/screenshots, no people/faces, no glamorised winning → NO integrity failure.
**Per-image:**
- `nachalna-podredba-tabla.svg` — PASS, "Няма проблеми", numbers match text, no clip/overlap.
- `tri-igri-tabla-tapa-gyulbara.svg` — PASS, "Няма проблеми", facts accurate, clean spacing.
- `tabla-dupka-zar-hero.webp` — NEEDS WORK: wrong geometry (7 triangles/quadrant vs 6), a stray winding white path across board+checkers, blurry/merged checkers bottom-right, a checker sitting on the bar; filename word "dupka" (hole) should be a board word.
**Action:** regenerate the hero with a stricter prompt (exactly 6 triangles per quadrant, no stray path lines, neatly stacked checkers), rename the file, re-review (pass 2). Keep best.

## Gemini verbatim verdict

**Score: 65/100**
**Verdict: NEEDS WORK**

### Специфични проблеми

**1. Изображение `tabla-dupka-zar-hero.webp` (Растер)**
*   **Точност и Техническо качество (AI халюцинации):** Дъската е напълно сгрешена. В реалната табла (и според текста) има 4 групи по 6 полета (триъгълника). В илюстрацията квадрантите имат по 7 триъгълника (напр. горе вляво са 4 червени и 3 сини).
*   **Техническо качество (Дефекти):** През дъската и пуловете минава абсурдна, криволичеща бяла линия, която няма място в играта.
*   **Техническо качество (Детайли):** Пуловете долу вдясно са размазани и се сливат един в друг. Черният пул вляво е стъпил физически невъзможно върху самия бар (разделителя), като бялата линия минава през него.
*   **SEO метаданни:** Името на файла съдържа думата `dupka` (дупка), което най-вероятно е техническа грешка/типографика и е трябвало да бъде `daska` (дъска).

**2. Инфографика `nachalna-podredba-tabla.svg`**
*   Няма проблеми. Изображението е отлично структурирано, числата (15 пула, 24 полета, 2 зара, точните стартови позиции) отговарят напълно на текста. Няма отрязан или припокриващ се текст.

**3. Инфографика `tri-igri-tabla-tapa-gyulbara.svg`**
*   Няма проблеми. Фактологията за трите вида игри (посока, удряне/затискане, каскада на чифта при гюлбара) е абсолютно точна спрямо статията. Отстоянията са чисти и текстът е напълно четим.

### Конкретни стъпки за поправка

*   **За `tabla-dupka-zar-hero.webp`:** Генерирайте ново изображение, като зададете много по-строг промпт на AI: *"A mathematically accurate backgammon board viewed from above, exactly 6 triangles in each of the 4 quadrants, standard dice, neatly stacked wooden checkers, clean vector style, NO random lines or paths on the board"*. Алтернативно – използвайте реална стокова фотография на дъска за табла, тъй като AI често се проваля със специфичната геометрия на настолните игри. Преименувайте файла на `tabla-daska-zar-hero.webp`.
*   **За `nachalna-podredba-tabla.svg`:** Не променяйте нищо. Готово за публикуване (PASS).
*   **За `tri-igri-tabla-tapa-gyulbara.svg`:** Не променяйте нищо. Готово за публикуване (PASS).

# 08 — Gemini image review · pass 1 · vk-0340 · Локомотив София

**Script:** `python3 scripts/gemini_image_review.py 05b-final-draft.md images/lokomotiv-sofia-v-chisla.svg` (online, exit 0; SVG reviewed as source so numbers are checked).

**Score: 100/100 · Verdict: PASS** (≥ IMAGE_TARGET_SCORE 80 AND 0 integrity failure).

Gemini findings (verbatim summary):
- Точност: всяко число/твърдение (титли, купи, капацитет, мачове/голове на легендите, година на основаване) съвпада точно с текста; 0 измислени/разминаващи се факти.
- Интегритет/хигиена: 0 фалшиви оператор-лога, 0 измислени бонуси, 0 лица на хора, 0 глорификация на хазарта; изчистен документален дизайн.
- Отговорна игра: неутрален историко-фактологичен тон; футър „без класирания, резултати или прогнози“ подсилва 18+ подхода.
- SEO: правилно име на файла (lowercase-hyphenated, descriptive); изчерпателен точен BG ALT.
- SVG рендер: чист код, стандартни шрифтове, червено-черна клубна схема; 0 overlap / 0 clipping (>25px отстояние 1979/80↔етикет); футър не се допира до ръбовете.
- Корекции: няма; готово за публикуване.

**Keep-best:** single infographic, score 100 (best). No AI hero generated — this is a data-only article; the infographic alone is on-strategy and the hero would add decorative risk without value. Chromium render pre-checked (deviceScaleFactor 2) = clean before review.

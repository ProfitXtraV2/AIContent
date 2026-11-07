# Step 8 — Gemini image review (pass 1)

Script: `python3 scripts/gemini_image_review.py 05b-final-draft.md <svg> <webp>` · 2026-11-06

## Scores
- `uimbaldon-klyuchovi-fakti.svg` (infographic): **100/100 PASS** — 0 integrity issues.
  All years (1877, 1922, 2009, 2019, 2022) + formats (тайбрек до 10 при 6-6; 3 сета мъже / 2 останали)
  trace exactly to 05b. Neutral tone, no faces/logos/gambling elements, clean SVG, ALT/aria-label good.
- `uimbaldon-treven-kort-hero.webp` (decorative hero): **45/100 NEEDS WORK** — NOT an integrity failure
  (no faces/logos/fabricated numbers/screenshots; good filename + ALT). Flaw is accuracy of the drawn
  court geometry: the center service line wrongly extends to the baseline (splits each half into 4 squares);
  on a rules-adjacent article this is a visible error. → iterate (pass 2) with a more abstract prompt that
  avoids drawing the full-court line layout.

## Verbatim verdict

### Изображение 1: uimbaldon-klyuchovi-fakti.svg — Оценка: 100/100 — PASS
Релевантност/стойност: отлична. Точност: безупречна (всички години 1877, 1922, 2009, 2019, 2022 и
формати тайбрек до 10 при 6-6, 3 сета мъже/2 останали отговарят на текста). Интегритет/RG: неутрален,
без лица, без хазартни елементи, без измислени лога. SEO: правилно име + изчерпателен ALT/aria-label.
Техническо: чист SVG, без припокриване, достатъчен контраст, текстовете се събират в картите.
Препоръки: няма — готов за публикуване.

### Изображение 2: uimbaldon-treven-kort-hero.webp — Оценка: 45/100 — NEEDS WORK
Точност (критична за рисунъка): очертанията на корта са грешни — централната линия продължава до
основната линия и разделя всяка половина на 4 квадрата; реално тя спира до линията за сервис, а на
основната линия има само малък маркер. Релевантност/SEO: стилът и атмосферата са добри; име и ALT
отлични; няма забранени елементи (лица, лога). Проблемът е само във фактологията на рисунъка.
Решение: регенерирай с промпт, който налага коректна геометрия, или направи сцената по-абстрактна,
за да не се чете цялата линия на корта.

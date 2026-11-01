# 06 — Verification · Тенис: правила и точкуване от гейм до мач

Type: guide (evergreen scoring/rules explainer, editorial voice, byline Георги Тодоров) · ~764 words · 0 em-dashes
Flags surviving in text: **0** ([VERIFY] / [DATA NEEDED] / [LINK NEEDED] = none).
Operator/НАП/affiliate facts: **none** (evergreen rules guide; no operator referenced → no affiliate link; no НАП licence № needed — not a review). Guides-only scope respected.
Length note: 764 words sits just under the guide band (1,000–1,800). Kept deliberately lean per
KEEP-BEST + „never pad" — the lean draft scored Gemini human-likeness **90**. Every core rule of
tennis scoring (гейм/деус/предимство, сет, тайбрек, решаващ-сет тайбрек, best-of-3/5, сервис,
корт/настилки) is covered; density-as-padding avoided.

## Time-sensitive / sourced claims (primary sources)
All figures are stable laws of the sport. NO current rankings/results/fixtures/form/odds printed
(evergreen guardrail). No betting tips or predictions.

- Точкуване в гейм: 0 („нула"/„love"), 15, 30, 40, гейм; 40-40 = равенство (деус), печели се с 2
  поредни точки (предимство → гейм, или назад към равенство).
  — ITF Rules of Tennis · https://en.wikipedia.org/wiki/Tennis_scoring_system
- Сервис: 2 опита/точка; двойна грешка → точка за съперника; диагонал в отсрещното поле за сервис;
  редуване дясно/ляво поле; „лет" при закачане на мрежата (повтаря се); редуване на геймовете на
  подаване; смяна на страни след нечетните геймове.
  — ITF Rules of Tennis · https://www.itftennis.com/en/about-us/governance/rules-and-regulations/
- Сет: пръв до 6 гейма с преднина ≥ 2 (6-4, 7-5); при 6-6 → тайбрек.
  — ITF Rules of Tennis
- Тайбрек: пръв до 7 точки с преднина 2; ред на подаване (1 точка, после по 2; смяна на страни на
  всеки 6 точки). Решаващ сет: от 2022 г. четирите турнира от Големия шлем въведоха единен тайбрек
  до 10 точки (преднина 2) при 6-6.
  — ITF · Grand Slam Board (март 2022) · https://www.tennis.com/news/articles/all-grand-slams-to-use-10-point-tiebreaker-in-final-set
  · https://www.nbcsports.com/tennis/news/all-grand-slams-to-use-10-point-tiebreaker-in-final-set
- Мач: best of 3 (2 спечелени сета; женския календар + повечето турнири) / best of 5 (3 сета; мъже
  на Големия шлем).
  — ITF / ATP / WTA / Grand Slam
- Корт/настилки: сингъл в по-тясното поле, дабъл + странични коридори; хард/клей/трева различават
  скорост и отскок. 15-30-40 рамкирано като предание (циферблат на часовник), произходът „не е
  документиран със сигурност" — framed as legend, not asserted fact.
  — https://en.wikipedia.org/wiki/Tennis_scoring_system · https://en.wikipedia.org/wiki/Tie-break

## Recalculation (one figure, working shown)
- Деус логика: от 40-40 се печели с 2 поредни точки → първата дава предимство, втората затваря
  гейма; загуба на точка при предимство връща на 40-40. ✓ Вътрешно последователно с „печели с 2
  поредни точки" в текста и в инфографиката.
- Решаващ сет: „от 2022 г." — Grand Slam Board обяви единния 10-точков тайбрек при 6-6 през март
  2022 г. ✓ Рамкирано като правило от 2022 г., без да се приписва конкретен шампион/резултат.

## Gemini Step-7 (cross-model human-likeness)
- Baseline (initial draft): „Likely human-written, 85%" → HL **85 → PASS**.
- Humaniser pass 1 (apply recs #1+#2: cut intro signpost + rhetorical-question pivot): „Likely
  human-written, 90%" → HL **90 → PASS**.
- KEEP-BEST winner = humaniser pass 1 (HL 90). Final 05b = that state. gemini column: **human 90**.
- Gemini touched style only; every number, link, RG line, 18+, disclosure, date, byline and brand
  preserved verbatim across both passes. Pass-2 recs (further "bow"/"glue" trims) declined per
  keep-best on an already-rising passing draft.

## Step-8 images
- images: **2** — infographic `tenis-tochkuvane-stylba.svg` (стълбица на точкуването, всяко число
  1:1 с 05b; „18+ Играйте отговорно" footer) + decorative hero `tenis-kort-mrezha-hero.webp`
  (flat-vector корт + мрежа + топка; без лица/лога/текст; WebP 43 KB, 1280×714).
- Gemini image review pass 1: **score 100 — PASS**, 0 integrity failures. SVG independently
  rendered + eyeballed (no overlap/clip). Keep-best = current. (Hero generated via gemini-3-pro-image
  as PNG; Pillow broken in env → converted to WebP < 100 KB via Chromium canvas.)

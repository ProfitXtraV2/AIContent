# 06 — Verification (vk-0338 · ПСЖ)

Article: „Пари Сен Жермен (ПСЖ): клубът, който дълго купуваше всичко освен Шампионската лига"
Type: guide (evergreen club profile). Byline: Георги Тодоров. Date: 18.11.2026.

## Surviving flags (handled by careful phrasing; human confirms at Step 6)
No inline [VERIFY]/[DATA NEEDED] markers in the published text. Two uncertain facts were
written around rather than asserted to a precise value (house style, mirrors vk-0337):
1. Парк де пренс capacity — text says „около 48 000 места" (infobox ~47 929, changeable).
   Approximate, not asserted to the seat. Confirm before publish if an exact figure is wanted.
2. Килиан Мбапе голмайстор №1 в историята на клуба; Единсон Кавани преди него. The ranking
   is cross-verified (EN Wikipedia records), but no exact goal tally is printed (counts change).

## Time-sensitive / factual claims with primary sources
- Основан 12.08.1970 (сливане „Пари ФК" + „Стад Сен Жермен"); „Пари ФК" се отделя 1972 г. [wiki][brit]
- „Парк де пренс", дом от 1974 г.; прякори „парижаните"/„червено-сините". [wiki]
- Първа титла на Франция 1985/86 (Жерар Улие). [brit][footballhistory]
- КНК 1996: финал 1:0 срещу „Рапид" Виена, Брюксел, гол Бруно Нготи. [wiki]
- Собственост: QSI мажоритарен дял 2011; преди това „Канал+" 1991, „Колони Капитал" 2008. [wiki]
- Трофеи към 2026 г.: 14 Лига 1, 16 Купа на Франция, 9 Купа на лигата (прекратена), 14 Трофей на шампионите. [wiki][beIN]
- ШЛ 2025: финал 31.05.2025 Мюнхен, 5:0 срещу „Интер" (най-голяма разлика на финал в историята); требъл. [SI][saudigazette][official]
- ШЛ 2026: финал 30.05.2026 Будапеща („Пушкаш Арена"), срещу „Арсенал" 1:1 след продължения, 4:3 дузпи, гол на Дембеле; пръв с поредни титли след „Реал" 2018. [CNN][wiki-2026final]
- Легенди: Мбапе (голмайстор №1), Маркиньос (мачове), Ди Мария (асистенции), Тиаго Силва (капитан), Лама (сухи мрежи); Сушич/Фернандес, Раи/Уеа/Жинола, Роналдиньо. [wiki]

Sources:
[wiki] https://en.wikipedia.org/wiki/Paris_Saint-Germain_F.C.
[wiki-2026final] https://en.wikipedia.org/wiki/2026_UEFA_Champions_League_final
[brit] https://www.britannica.com/topic/Paris-Saint-Germain
[footballhistory] https://www.footballhistory.org/club/psg.html
[SI] https://www.si.com/soccer/psg-5-0-inter-takeaways-champions-league-final-5-31-25
[saudigazette] https://saudigazette.com.sa/article/652351/
[CNN] https://www.cnn.com/2026/05/30/sport/live-news/arsenal-psg-champions-league-final-score

## One recalculated / cross-checked figure (working shown)
Back-to-back span: first UCL final 31.05.2025, second 30.05.2026 = 12 months (364 days),
i.e. exactly one year. Author draft said „тринайсет месеца"; corrected to „в рамките на една
година" at the gate (the only number changed), then that sentence was dropped during the
humaniser pass. Trophy counts stated „към 2026 г." and consistent between prose and the
infographic ALT (14 Лига 1 / 16 Купа на Франция / 14 Трофей на шампионите). 0 number drift.

Note on Gemini knowledge limit: the Step-7 model flagged the 2025/2026 Champions League
titles as „fictionalized". They are REAL, cross-verified (CNN, SI, Ligue1, official PSG,
EN Wikipedia 2026 final); the model's training cutoff simply predates them. Not a fact error.

## Gemini Step-7 TEXT check (cross-model, gemini_check.py — API ONLINE)
- Check 1 (initial 05b): „Shows AI patterns, 80%" → human-likeness 15 → corrected read 20. Below 80.
- Humaniser pass 1 (step-7b: removed thematic bookending, flattened theatrical transitions,
  trimmed paragraph-summary bows, cut brand justification; all untouchables preserved).
- Check 2: „Shows strong AI patterns, 85%" → human-likeness 15. Below 80 (detector noise).
- Humaniser pass 2 (melodrama/metaphor flattening, de-listed player names, deleted signposting
  topic sentence, removed temporal disclaimer, varied founding rhythm).
- Check 3: „Shows AI patterns, 70%" → human-likeness 30. MAX_GEMINI_PASSES (2) reached.
- **Keep-best: pass 2 (HL 30)** — highest of 20/15/30 — kept. Below 80 after cap → gemini = `ai 70`,
  2 passes applied. Flagged for human-editor attention at Step 6. Noisy detector on evergreen
  football-history profiles (same as vk-0314 ai 65, vk-0063 ai 75). Gemini touched style only.

## Step-8 IMAGES (create + Gemini visual review — API ONLINE)
- images: 1 (infographic 100). Hand-authored SVG „pszh-pari-sen-zhermen-v-chisla.svg"
  (клуб накратко + домашни трофеи + европейски път). Every number traced verbatim to 05b;
  0 operator logos, 0 faces, 0 fabricated figures, 0 glamorised winning; 18+ line on the graphic.
  Chromium render checked at deviceScaleFactor 2: no overlap, no clipping, all text within cards.
- Gemini image review pass 1 = 100 PASS, 0 integrity failure. Keep-best = pass 1 (100). No fix needed.
- No decorative AI hero added (data/history article; the infographic is the primary and preferred visual).

## Brand Gate
PASS 95/100, 0 criticals (see 05-gate-report.md). 0 em-dashes (U+2014), 0 en-dashes (U+2013)
in body + meta (and 0 in the infographic SVG). 0 banned AI connectives, 0 promise/hype words.
Byline Георги Тодоров; brand „Всички Казина" exact; verbatim 18+ RG line + /otgovorna-igra/ +
регистър на уязвимите лица; affiliate 1-Aug-2026 footer (status pending, no „issued" claim,
no invented №). 6 in-prose internal links from the real sitemap set (Футбол hub + Меси +
Барселона siblings + спорт money + zakonno + responsible-gambling). ~860 words body.
0 operators / 0 affiliate targets (history guide) → no НАП licence № / [LINK NEEDED] needed.
No predictions, no current standings/results/fixtures/transfers/odds. Real people: only
cross-verified facts, 0 inline flags (2 uncertainties written around, logged above).

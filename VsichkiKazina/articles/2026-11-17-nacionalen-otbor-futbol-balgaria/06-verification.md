# 06 — Verification

Article: „Национален отбор по футбол на България: историята зад „лъвовете" и чудото от САЩ '94"
Type: guide (evergreen national-team history). Byline: Георги Тодоров. Date: 17.11.2026.

## Surviving flags (STAY in the text; human resolves at Step 6)
1. `[VERIFY: точен брой и дали е наравно с Христо Бонев]` — Димитър Бербатов „48 попадения".
   EN Wikipedia infobox showed Berbatov and Bonev both near 48; exact tally and who leads is
   ambiguous from that source. Kept flagged, not resolved. Recommend confirming the current
   all-time top-scorer figure (Berbatov 48 vs Bonev 47 is the commonly cited pair) before publish.

No [DATA NEEDED] flags (nothing blocks publish). 1 surviving flag total.

## Time-sensitive / factual claims with primary sources
- First official international 21.05.1924, Виена, Австрия 6:0 България. [wiki-nt]
- World Cup finals 7×: 1962, 1966, 1970, 1974, 1986, 1994, 1998. [wiki-wc]
- 1994 knockout path: R16 Мексико 1:1, 3:1 на дузпи; 1/4 Германия 2:1 (10.07.1994); 1/2 Италия
  1:2; мач за 3-то Швеция 4:0; крайно 4-то място. [wiki-wc][bta][espn]
- Стоичков голмайстор СП '94, 6 гола (поделен с Олег Саленко); „Златна топка" 1994. [wiki-nt]
- Квалификация: 17.11.1993, Париж, гол на Костадинов в 90-ата мин. [wiki-nt]
- Евро финали: 1996, 2004 (групова фаза и двата пъти). [wiki-nt]
- Рекорди: Стилиян Петров 105 мача; Бербатов 48 гола [VERIFY]. [wiki-nt]
- Олимпийско сребро по футбол 1968. [search]
- Прякор „лъвовете"/„трикольорите"; БФС 1923; стадион „Васил Левски". [wiki-nt]

Sources:
[wiki-nt] https://en.wikipedia.org/wiki/Bulgaria_national_football_team
[wiki-wc] https://en.wikipedia.org/wiki/Bulgaria_at_the_FIFA_World_Cup
[bta] https://www.bta.bg/en/news/927893 — 10.07.1994 Bulgaria 2:1 Germany (QF)
[espn] https://www.espn.in/football/match/_/gameId/198073/germany-bulgaria — Stoichkov 76', Lechkov 79'

## One recalculated / cross-checked figure (working shown)
World Cup finals appearances count: 1962, 1966, 1970, 1974, 1986, 1994, 1998 = 7 distinct years.
Matches the „седем пъти" stated in the text and the „7 участия" tile in the infographic. ✓
(An old mirror infobox listing „8, first 1930" was rejected as an error; all current sources give 7 from 1962.)

## Gemini Step-7 TEXT check (cross-model, gemini_check.py — API ONLINE)
- Pass 1 (initial 05b): „Shows AI patterns, 85%" → human-likeness 15. Below 80.
- Humaniser pass 1 (step-7b: cut signposting/meta-discourse, over-dramatisation, philosophical
  wrapping, formulaic antithesis close; every number/link/flag/RG/date/byline preserved).
- Pass 2: „Likely human-written, 90%" → human-likeness 90. **PASS.**
- Keep-best: 15 → 90; kept the pass-1 version (highest). gemini column = `human 90`, passes applied = 1.
- Optional polish Gemini flagged after PASS (NOT applied, forwarded to human editor; touch no fact):
  „получава своя гръб" (calque), „тема, върху която сядат" (preposition), link-list signposting.

## Step-8 IMAGES (create + Gemini visual review — API ONLINE)
- images: 1 (infographic 98). Hand-authored SVG „balgaria-futbol-sasht-94-putyat.svg"
  (USA '94 knockout path + key numbers). Every number traced verbatim to 05b; 0 operator
  logos/names, 0 faces, 0 fabricated figures, 0 glamorised winning; 18+ line on the graphic.
  Chromium render checked: no overlap, no clipping, all text within cards.
- Gemini image review: pass 1 = 78 (needs work — „Швеция 4:0" was inconsistent with the
  Bulgaria-perspective of the other rows and the ALT). Hand-fixed SVG to „Швеция 0:4" (traces to
  „спечели с 4:0"). Pass 2 = 98 PASS (no integrity failure). Keep-best 78 → 98.
- Applied ALT accuracy fix in 05b (removed „групова фаза, " — the infographic starts at осминафинал).
- No decorative AI hero added (data/history article; infographic is the primary and preferred visual).

## Brand Gate
PASS 95/100, 0 criticals (see 05-gate-report.md). 0 em-dashes (U+2014), 0 en-dashes (U+2013),
0 banned AI connectives, 0 promise/hype words. Byline Георги Тодоров; brand „Всички Казина" exact;
verbatim 18+ RG line + /otgovorna-igra/ + регистър на уязвимите лица; affiliate 1-Aug-2026 footer
(status pending, no „issued" claim). 6 in-prose internal links from real sitemap set.
~990 words body. 0 operators / 0 affiliate targets (history guide) → no НАП licence № / [LINK NEEDED] needed.
No predictions, no current standings/results/fixtures/odds. Real people: only cross-verified facts + 1 [VERIFY].

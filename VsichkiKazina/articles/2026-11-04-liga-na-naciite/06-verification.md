# 06-VERIFICATION — Лига на нациите (формат и как влияе на квалификациите)

## Surviving flags
- [VERIFY]: 0
- [DATA NEEDED]: 0
- [CONFLICT]: 0
All facts are encyclopedic / primary football-governance facts (UEFA regulation + Wikipedia),
verifiable without geo-blocked operator/НАП sources. Nothing asserted that needs a human flag.

## Time-sensitive claims (framed as evergreen; primary sources)
- Team counts per division "от издание 2020/21" (A/B/C = 16 each, D = 7) — framed as the current
  framework, not an eternal law. Source: en.wikipedia.org/wiki/UEFA_Nations_League.
- Finals/quarter-finals "от издание 2024/25" — framed as the format introduced that edition.
  Source: en.wikipedia.org/wiki/UEFA_Nations_League (Finals section).
- Place-allocation into Euro/World Cup play-offs — deliberately NOT printed as fixed numbers;
  the article states the counts change per qualification cycle and points the reader to the
  official UEFA/FIFA regulation. 0 fabricated fixed allocation. Source: uefa.com (official regulation).
- Champions (завършени издания, "към 2026 г."): Португалия 2019, Франция 2021, Испания 2023,
  Португалия 2025; Португалия единствен двукратен победител. Source: en.wikipedia.org/wiki/UEFA_Nations_League
  (finals results) — completed editions, stable historical record.

## Recalculated figure (working shown)
Internal consistency of the stated team totals:
  Лиги A + B + C = 16 + 16 + 16 = 48 отбора; плюс Лига D = 7 → 48 + 7 = **55 отбора**.
This equals the article's stated "55 национални отбора на УЕФА". Internally consistent. ✓

## Step-7 external Gemini (text) — keep-best
- Initial draft: HL 35 (check 1) — fair re-sampling of the SAME initial text returned HL 80 and HL 15.
- Humaniser pass 1: HL 20 (check 2). Humaniser pass 2: HL 30 (check 3).
- Detector is NON-DETERMINISTIC on this dense factual BG content (identical input → 15/35/80), so
  "highest HL seen" is not a reliable selector. Kept the cleanest-prose version (humaniser pass 2):
  it removed genuine AI tells + two awkward BG collocations (товарни→безцелни, нарязана→разделена).
- **gemini = ai 70** (kept version's own check-3 verdict, HL 30). < 80 target → marked for HUMAN REVIEW.
  Style-only across all passes; 0 facts/numbers/links/RG touched. 0 number-drift (02→03→05b).

## Step-8 images
- images: 2 (infographic approved/accurate, hero 85).
- `liga-na-naciite-format.svg` — hand-authored infographic; every number traced VERBATIM to 05b
  (2018/19, 55, 4 дивизии A–D, 16/16/16/7, 3/1/0, финална фаза 4 отбора, шампиони 2019/2021/2023/2025);
  Gemini review final verdict: APPROVED, "absolutely accurate", 0 integrity issue (2 layout fix passes).
- `liga-na-naciite-hero.webp` — decorative empty-stadium hero, 23 KB WebP; Gemini review 85 PASS,
  0 integrity (regenerated once after the first hero showed crowd silhouettes = integrity fail; empty
  stadium, no people/faces/logos/flags/glamorised winning). ALT describes the empty stadium.

## Compliance summary
- Brand Gate 94/100 PASS, 0 critical. Byline Георги Тодоров; brand Всички Казина (×3).
- Guides-only: 0 operator facts, 0 НАП licence data, 0 affiliate links (no operator recommended),
  0 sports predictions, 0 live standings/results/fixtures/odds.
- RG: 18+ verbatim line + /otgovorna-igra/ + регистър на уязвимите лица; „Солидарност" 0888 99 18 66.
- 0 em-dash in body; 5 internal links (4 body + 1 footer RG) from the approved set; ~807 words.

# 06 — Verification · vk-0277 · Евроджакпот и Евромилиони от България

Type: guide (legal/educational) · Byline: Георги Тодоров (editorial voice) · Date: 2026-10-11

## Surviving flags (STAY IN THE TEXT — human resolves at Step 6)
1. **[VERIFY] EuroMillions цени на линия по държави** (таблица, ред „Цена на линия"). Само цената за Обединено кралство (£2.50) е потвърдена; останалите по държави не са извлечени. Източник за проверка: официалните национални оператори / euro-millions.com.
2. **[VERIFY] Точен член от ЗХ за блокиращата процедура** (Раздел „Какво рискувате реално" + инфографика #2). Процедурата (решение → 3 дни → Софийски районен съд → блокиране от доставчиците → „Онлайн хазарт") е потвърдена по новинарски/официален източник, но конкретният член (вероятно чл. 86–87) НЕ е сверен в текста на закона. Източник за проверка: ЗХ, lex.bg / Държавен вестник.
3. **[VERIFY] ЗДДФЛ третиране на печалба от чужда лотария за местно лице** (Раздел „Какво рискувате реално"). Ставка/деклариране не са твърдени; насочено към счетоводител/НАП. Данъкът винаги остава [VERIFY] по бранд-правилата.
4. **[VERIFY] Брой държави-участнички (19 / 9)** (таблица). Дадено с дата „към март 2024 г."; участието се променя — да се свери към датата на публикуване. Източник: eurojackpot.com / euro-millions.com.

Няма [DATA NEEDED] и няма [CONFLICT] в текста.

## Time-sensitive / sourced claims
- **Eurojackpot**: формат 5 от 50 + 2 от 12 (1–12 от март 2022), шанс 1:139 838 160, тиражи вт 21:15 / пт 21:00 (хелзинкско време), €2/линия (Литва €3, Гърция/Словения €2.50, Полша 12.50 PLN), джакпот €10 000 000 → €120 000 000 (таван вдигнат от €90 000 000 през март 2022), от 23.03.2012 (продажби 17.03.2012), 19 държави към март 2024, България липсва. Източник: https://en.wikipedia.org/wiki/Eurojackpot (fetched 2026-10-11).
- **EuroMillions**: 5 от 50 + 2 Lucky Stars от 12, тиражи вт/пт, 9 държави (Австрия, Белгия, Франция, Ирландия, Люксембург, Португалия, Испания, Швейцария, Обединено кралство), претенция само в държавата на покупката, UK £2.50. Източник: https://www.lottery.co.uk/euromillions/how-to-play (2026-10-11).
- **НАП блок-процедура**: публичен списък; решение на изп. директор → 3 дни след публикуване на nra.bg → Софийски районен съд → BG доставчици блокират домейн+поддомейни → „Онлайн хазарт". Източник: https://kik-info.com/novini/nap/ + https://nra.bg/wps/portal/nra/gambling/hazart (2026-10-11).
- **ЗХ рамка**: чл. 3 (лиценз от изп. директор на НАП, за изрично посочена игра), чл. 4 ал. 3 (лотариен лиценз само за държавата, извън томбола/бинго), чл. 13а (БСТ), чл. 41 („залагания върху случайни събития"), надзор към НАП от 08.08.2020. Пренесено от sister-source (консолидиран ЗХ, kik-info.com) и vk-0273.

## Recalculated figure (working shown)
Шансът за големия джакпот на Eurojackpot = комбинации за 5 от 50 × 2 от 12:
- C(50,5) = 2 118 760
- C(12,2) = 66
- 2 118 760 × 66 = **139 838 160** → 1:139 838 160 ✓ (съвпада с текста и инфографика #1).

## External Gemini TEXT check (Step 7) — gemini-3.1-pro-preview
- Check 1: „Shows AI patterns, 75%" → human-likeness **25**.
- Humaniser pass 1 (apply recs): de-announce heading, plainer phrasing, drop 2 signposts, de-metaphor tax lines, trim recap.
- Check 2: „Likely human-written, 85%" → human-likeness **85** = **PASS**.
- KEEP-BEST: highest = pass 1 (25 → 85). Final 05b = pass-1 version. **gemini: human 85.**
- (Endpoint slow; ran with extended 280s read timeout. 1 of MAX_GEMINI_PASSES used.)

## Images (Step 8) — 1 hero + 2 infographics
- `evrodzhakpot-evromilioni-hero.webp` (13.4 KB) — concept metaphor (foreign jackpot beyond a closed border barrier + shield). Review: PASS, 0 integrity issues.
- `evrodzhakpot-evromilioni-sravnenie.svg` — Eurojackpot↔EuroMillions comparison; every number traces verbatim to 05b (incl. 1:139 838 160, €10 000 000 → €120 000 000, 19/9, £2.50, €2). Review: PASS.
- `nap-blokirane-nelicenziran-sait-stapki.svg` — НАП block-procedure flow (решение → 3 дни → съд → блокиране). Review: PASS.
- **images: 3 (hero PASS, 2 infographics; best review score 95/100 PASS).** Review 1 = 75 → fixed ([VERIFY]-note leak removed from block SVG + step-4 alignment) → review 2 = 95 PASS → terminology tweak (Обединено кралство) for 100% match. 0 fabricated logos/numbers/people/faces; no glamorised winning.

## Hygiene confirmed
No reseller / messenger / concierge / betting-on-outcome site named, described identifiably, or linked anywhere. No operator affiliate link (legal guide — none warranted). Byline Георги Тодоров; brand „Всички Казина"; verbatim 18+ RG line + signposting; affiliate-licensing footer in no-affiliate „Разкриване" form. 0 em-dashes.

## Step 6 — human flag resolution (2026-10-11)
All 4 [VERIFY] resolved; 0 flags left in 05b.
1. **EuroMillions цени** — table now: €2.50 Испания/Ирландия/Португалия, £2.50 Обединено кралство, CHF 3.50 Швейцария (https://en.wikipedia.org/wiki/EuroMillions, fetched 2026-10-11). Also filled the „няма данни" jackpot cell: таванът се вдига на стъпки, последно €250 000 000 (достигнат 13.06.2025, same source). SVG #1 updated to match.
2. **Блокиране — FACTUAL FIX, not just the article number.** The 3-day / Софийски районен съд procedure is outdated (NAP page is stale). Current ЗХ (consolidated to ДВ бр. 69/31.07.2026): чл. 17, ал. 1, т. 9 — изп. директор на НАП разпорежда спиране; чл. 17, ал. 6 (от 01.08.2026) — решението се публикува на сайта на НАП, доставчиците спират достъпа до 24 часа, иначе санкция. Source: source-packs/nap-gambling-law-and-rg-2026-10-10.md §4 correction (vk-0265) + identical wording in merged vk-0266 darzhavna-nacionalna-lotaria and zakon-za-hazarta. Text rewritten; SVG #2 redrawn (Решение → Публикуване → До 24 часа → Санкция; „Без съд по средата") + alt text updated.
3. **ЗДДФЛ** — per house precedent (vk-0036, vk-0121): tax assertion removed; text now asserts no rate/exemption, only that the licensed-BG treatment does not apply automatically to foreign/unlicensed winnings → счетоводител/НАП + link to the tax guide.
4. **Брой държави** — Eurojackpot 19 since Greece joined (first draws 08.03.2024; no 2025–2026 joiner found), EuroMillions 9 since 08.10.2004 (Wikipedia, fetched 2026-10-11). Table reworded „от март 2024 г." / „от 2004 г."; standalone flag line removed; SVG footnote → „Цените и участието на държавите се променят."

# 06 — Verification (Step 6, for the human) · vk-0273 · Лотария (hub)

Status: **pre-verification draft — NOT publishable until the flags below are resolved by a human.**
Gate: PASS WITH FIXES 83 → 94/100 (run 2; run 1 FAIL 79 fixed at Stage 2 + re-run 3→5).
Humaniser: Stage 3 45/60 MIXED → light rewrite. Gemini (Step 7): check 1 AI patterns 70% (hl 30) →
humaniser pass 1 → check 2 **human-written 90% (PASS)**; kept best = pass 1 (90). `gemini = human 90`.
Images: **3 (hero 100, infographic „4 вида" 100, infographic „шансове" 100 — joint review 100, PASS)**.

## Surviving flags (3, verbatim in 05b)

| # | Flag | Where | What to check | Primary source |
|---|---|---|---|---|
| 1 | `[VERIFY: действащ частен лиценз за кено след 2020 г. — регистрите на НАП]` | „Кой има право…", кено paragraph | Is any private кено licence (issued pre-2020, saved by § 9 ПЗР ДВ бр. 14/2020) still active? Current чл. 4, ал. 3 (ред. ДВ бр. 14/2021) no longer lists кено among the exceptions. If none is active → drop the flag and say кено is state-only today. | НАП регистри по чл. 20 ЗХ (nra.bg — geo-blocked from cloud); consolidated ЗХ https://kik-info.com/normativna-baza/zakoni/0X2135783265 |
| 2 | `[VERIFY: дата — единствен източник bg.wikipedia]` | „Какви лотарии има…", БСТ start 12 май 1957 г. | Confirm the start date on toto.bg „За нас" (CAPTCHA for scripts). vk-0271 used the same date unflagged. | https://bg.wikipedia.org/wiki/Български_спортен_тотализатор ; toto.bg |
| 3 | `[VERIFY: дали сумата вече е преизчислена в € в консолидирания текст]` | „Къде се играе законна онлайн лотария", глоба 500–2000 лв. (чл. 9, ал. 14 + чл. 97а, ал. 2 ЗХ) | Whether the euro-changeover law restated the fine in €. The consolidated text read 10.10.2026 still shows лв. in the capital rules (чл. 4) — check чл. 97а specifically. | kik-info.com consolidated ЗХ; dv.parliament.bg |

## Time-sensitive claims (non-flag) and their sources

| Claim in 05b | Source (read 10.10.2026) |
|---|---|
| 4 вида лотарийни игри + definitions (чл. 49–59), ≥50% rules (чл. 51, 52, 56, 57, 59), payout logic тото vs лото/кено (чл. 55) | consolidated ЗХ, kik-info.com (primary text, quoted in 00-brief §A) |
| Лиценз за лотарийни игри само на държавата, освен томбола/бинго (чл. 4, ал. 3); БСТ (чл. 13а); томбола само ЮЛНЦ, еднократно, благотворително (чл. 15, 53) | same |
| Онлайн: всички без томбола и моментна (чл. 41, ал. 2) | same + НАП pack §3 |
| Продажба/изплащане само в обявени обекти/банки; 18+ (чл. 9, ал. 9–11) | same |
| НАП блокира нелицензирани сайтове с решение до 24 ч. от 01.08.2026 (чл. 17, ал. 6); глоба за играча | НАП pack §4 (corrected) |
| БСТ: 2 тиража седмично; игри ТОТО 2; БНТ чт/нд 18:45; Рожден ден/Зодиак след 19:00 във Facebook; скреч игри; ePay.bg/БОРИКА; авто-прехвърляне ТОТО 2 + Джокер; сайтът недостъпен чт/нд 18:40–19:10; ПМС № 50/15.02.2021 | БСТ pack (toto.bg, 10.10.2026) |
| НАП: 5% бюджет; регистър чл. 10г от 12.12.2022, ≥12 месеца, nap@nra.bg с КЕП, 0700 18 700; illegal_gambling@nra.bg | НАП pack §4–6 |
| Надзор при НАП от 08.08.2020 | НАП pack §1 |

## Recalculation (one figure, working shown)
C(35,5) = (35·34·33·32·31)/(5·4·3·2·1) = 38 955 840 / 120 = **324 632** ✓ (python3 math.comb).
Also: C(49,6) = 13 983 816, C(42,6) = 5 245 786; 13 983 816 / 324 632 = 43.08 → „над 40 пъти" ✓;
50% × €100 000 = €50 000 ✓ (illustrative); 5% × €1 200 = €60 ✓ (illustrative).

## Editor notes
- Internal links (4, all live in sitemap 10.10.2026): /blog/keno-pravila/, /blog/proverka-licenz-kazino/,
  /zakonno-li-e/, /otgovorna-igra/ (also in RG footer). **Once live, link this hub down to the Тото
  guides (vk-0266..vk-0270), vk-0271 (Държавна/Национална лотария) and vk-0264 (хазартни игри по ЗХ)** —
  sentences promising those guides were deliberately removed because they are not live yet.
- Out of scope by design: ticket prices, prize tiers, BST payout %, tax on winnings (→ /blog/danaci-pechalbi-onlajn-kazino/).
- Slots to fill at publish: „За Всички Казина" boilerplate, author bio.
- No affiliate links; no operator other than БСТ named.

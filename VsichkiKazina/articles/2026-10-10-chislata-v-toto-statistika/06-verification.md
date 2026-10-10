# 06 — Verification checklist (vk-0272, „Числата от тотото")

> FLAGS STAY IN THE TEXT. The human resolves them at Step 6 against primary sources. Nothing below
> has been resolved by the pipeline.

## Surviving flags (6 inline [VERIFY] + 1 bio slot)
| # | Claim in 05b | Flag | Source found / what it shows | Human action |
|---|---|---|---|---|
| 1 | Честотна таблица 6/49, 01.01.2015 – 08.10.2026: 7 572 изтеглени числа → 1 262 тиража | [VERIFY срещу архива на БСТ] | https://www.lotteryextreme.com/toto2/649-statistics (неофициален агрегатор, извлечено 10.10.2026); sum of all 49 counts = 7 572 (python3) | Сверете броя тиражи с архива на toto.bg (CAPTCHA за скриптове) |
| 2 | Най-често 34 (188), 23 (176), 37 (176), 42 (173), 35 (171); най-рядко 25 (132), 7 (131), 41 (129), 40 (117) | [VERIFY срещу архива на БСТ] | същата страница | Spot-check 2–3 числа срещу БСТ или втори агрегатор |
| 3 | 40 не е излизало 33 поредни тиража, последно 18.06.2026 (към 08.10.2026) | [VERIFY срещу архива на БСТ] | същата страница („Повечето просрочени номера") | Time-sensitive: обновете към датата на публикуване или формулирайте „към 08.10.2026" (вече е така) |
| 4 | 2009 повторение — „вероятно в играта 6 от 42" | [VERIFY] | BBC/Reuters (mirrors: sites.oxy.edu …BBC NEWS Europe Bulgarian lottery repeat probed.html; …Reuters.htm) не назовават играта; числата (макс. 42) и „1 към над 4 милиона" ≈ C(42,6) = 5 245 786 | Потвърдете играта от БГ архив/преса 2009 |
| 5 | Хипотеза: мнозина от 18-те са заложили числата от предишния тираж | [VERIFY] | източниците не го казват — изрично е формулирано като наша хипотеза | Оставете като хипотеза или махнете |
| 6 | Печалбите в ТОТО 2 се делят между всички печеливши комбинации в категорията | [VERIFY: точна формулировка в правилата на БСТ] | принципът се вижда в сменящите се суми по тиражи (агрегатор) и в 2009 случая (18 × 10 164 лв.); правилата на БСТ не са извлечени | Сверете с правилата на ТОТО 2 на toto.bg |
| 7 | [AUTHOR BIO SLOT] | slot | — | Вмъкнете стандартната био на Георги Тодоров |

Also noted by SEO stage (not in text): [DATA NEEDED] честотни таблици за 6/42 и 5/35 — future update only.

## Time-sensitive / sourced claims
- Тегления по БНТ четвъртък и неделя 18:45 ч.; два тиража седмично; 5/35 = две тегления — source pack `source-packs/bst-toto-2026-10-10.md` (toto.bg, BG browser 10.10.2026).
- 2009: числа 4, 15, 23, 24, 35, 42 на 06.09 и 10.09.2009; 18 печеливши × 10 164 лв.; Нейков / Симеонов / Константинов цитати — BBC + Reuters (17.09.2009) via mirrors above. € equivalent ≈ 5 197 € = 10 164 / 1,95583 (наша сметка).
- НАП RG: бюджет ≤5% от нетния доход, регистър по чл. 10г ЗХ, 0700 18 700 — `source-packs/nap-gambling-law-and-rg-2026-10-10.md`.
- Солидарност 0888 99 18 66 — brand canon (Brand Gate footer).

## Recalculated figure (working shown)
Expected frequency per number over 1 262 draws of 6/49:
1 262 × 6/49 = 7 572 / 49 = 154,53 → „≈154,5". SD = √(1 262 × 6/49 × 43/49) = √(1 262 × 0,12245 × 0,87755): 1 262 × 0,12245 = 154,53; × 0,87755 = 135,61; √135,61 = 11,65 → „около 11,6". ✔
Also: (43/49)^33 = 0,01343 → „около 1,3%" ✔; C(49,6) = 13 983 816 ✔; C(42,6) = 5 245 786 ✔; C(35,5) = 324 632 ✔.
Simulation (2 000 series × 1 262 fair draws): max count median 181 (5–95%: 174–192), min median 129 (120–135); chi-square p ≈ 0,06 from 3 000 simulated series (python3, 10.10.2026).

## Step 7 — external Gemini check
- Check 1 (initial 05b): „Likely human-written, 85%" → human-likeness 85 → PASS. 0 humaniser passes. Gemini column: `human 85`. Gemini's optional style recs (drop the roadmap sentence in the intro, trim the „ритуал" transition, drop the 2-sentence summary at the end) are in 07-gemini-check-1.md for the editor; not applied (PASS).

## Step 8 — images
images: 2 (infographic 100, hero 100) — review 1 score 75 (infographic label/band edge collisions) → fix pass 1 → review 2 score 100 PASS; 0 integrity issues.
- images/chislata-ot-toto-chestota-6-ot-49-infografika.svg — all numbers verbatim from 05b; rendered via headless Chromium 760×680, no overlap/clipping.
- images/chislata-ot-toto-nezavisimi-tirazhi-hero.webp — 17 KB, gemini-3-pro-image, no text/logos/people.

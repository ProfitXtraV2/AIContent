# 06-VERIFICATION — Всички Казина · 2026-09-30-mustang-gold
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Type: guide (slot explainer) · byline: Георги Тодоров · gate: PASS 94/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 30.09.2026

## Surviving [VERIFY] flags (stay in body)
**1** in-text [VERIFY]: `[VERIFY: един външен източник посочва таван 25 пъти вместо 35]` — стойността на паричния символ в Money Collect. Официалната страница на Pragmatic Play дава 1 до 35× общия залог; VegasSlotsOnline посочва 1 до 25×. Текстът твърди официалната стойност (35×) с ясен [VERIFY] за разминаването. 0 [CONFLICT]/[DATA NEEDED].

Хеджирани (не bare [VERIFY]): дата на пускане („началото на 2019 г." заради конфликт 17.01.2019 vs 29.11.2018); волатилност (представена като рейтинг на игралните бази, не официален); bet range (€0.25–€125, „зависят от оператора и валутата").

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Source | Note |
|---|---|---|
| Provider **Pragmatic Play** | pragmaticplay.com официален | |
| Release **началото на 2019** | SlotCatalog (17.01.2019); VSO | Хеджирано (едно VSO поле 29.11.2018). |
| **5x3, 25 фиксирани линии** | SlotCatalog; VSO | Фиксирани. |
| **RTP 96.53%** (default), конфигурируем | pragmaticplay.com; VSO | Официален. |
| **Алт билд 95.54%** | SlotCatalog | Операторът избира. |
| **Домашно предимство 3.47% / 4.46%** | Изведено (100 − RTP) | Виж RECALCULATION. |
| **€1000 → €965.30 / €34.70** | Recalc от 96.53% | Виж RECALCULATION. |
| **Max win 12 000× залога** | pragmaticplay.com; SlotCatalog; VSO | Таван. |
| **Bet €0.25–€125** | SlotCatalog; VSO | Operator/currency-dependent → хеджирано. |
| **Money символ 1–35× общ залог** → [VERIFY] | pragmaticplay.com (35×); VSO (25×) | Официал vs единичен източник. |
| **Collect символ на барабан 5 събира видимите стойности** | pragmaticplay.com; VSO | Ядро на Money Collect. |
| **4 фиксирани джакпота: Grand 1000× / Major 200× / Minor 100× / Mini 50×** | pragmaticplay.com (стойности); SlotCatalog/VSO (имена) | Фиксирани множители, НЕ прогресив. |
| **Jackpot Reveal (3 еднакви)** | pragmaticplay.com; VSO | Пик-игра. |
| **Free spins: 3 скатера (барабани 2,3,4) → 8 FS, неограничен ретригър** | pragmaticplay.com; SlotCatalog; VSO | Огън-скатер. |
| **Wild = логото, струпан барабани 2–5** | VSO paytable; SlotCatalog | Замества редови, не специални. |
| **Волатилност средно-висока до висока** | SlotCatalog; VSO (Medium-High) | Не на официалната страница → като DB рейтинг. |

## SOURCES REACHED (URLs)
- https://www.pragmaticplay.com/en/games/mustang-gold-slot/ (официален — RTP 96.53%, max 12000×, money 1–35×, jackpots 50/100/200/1000×, 8 FS infinite retrigger, Money Collect) — REACHED
- https://www.vegasslotsonline.com/pragmatic-play/mustang-gold/ (5x3, 25 линии, 96.53%, 12000×, jackpot имена+стойности, bet €0.25–€125, money 1–25×, paytable) — REACHED
- https://slotcatalog.com/en/slots/Mustang-Gold (5x3, 25 линии, 12000×, jackpots, release 17.01.2019, алт RTP 95.54%) — REACHED
- FAILED to load: bigwinboard.com (bot-verification wall); casino.guru (HTTP 403); slotsmate.com (HTTP 400)

## RECALCULATION (worked-€ example + SVG numbers ⊂ body)
- RTP 96.53% на €1000: 0.9653 × €1000 = **€965.30**; казино 0.0347 × €1000 = **€34.70**. ✓ съвпада с текст/инфографика.
- Алт билд: 100 − 95.54 = **4.46%** house edge. ✓
- SVG bar: player 0.9653 × 656 px = 633.24 ≈ **633 px**; house 0.0347 × 656 = 22.76 ≈ **23 px** (x=665..688). ✓ вътре в 32..688.
- Всички числа/етикети в SVG ⊂ тяло (grep-verbatim, проверено): 96.53%, 3.47%, €965.30, €34.70, 95.54%, „5x3", „25 фиксирани линии", „Money Collect", „1000 пъти", „200 пъти", „100 пъти", „50 пъти", „12 000 пъти залога", Grand, Major, Minor, Mini. ✓

## COMPLIANCE SPOT-CHECK (verbatim untouchables)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — тяло + footer. ✓
- RG signposting: /otgovorna-igra/ + регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026, ДВ бр. 69), pending-application, БЕЗ issued-licence, БЕЗ измислен №. ✓
- НЯМА BG оператор, НЯМА НАП лиценз №, НЯМА данъчна секция, НЯМА бонус условия, НЯМА афилиейт линк. ✓
- Byline Георги Тодоров; brand „Всички Казина"; дати 30.09.2026 (DD.MM.YYYY); € валута. ✓
- Em-dashes (—): 0 в тяло/ALT/caption/SVG. En-dash само „10:00–17:00". ✓
- Internal links: 5 от одобрения жив набор (/blog/pragmatic-play-provajdar/, /blog/games-providers/, /kak-ocenyavame/, /slot-igri/, /otgovorna-igra/). ✓

## ANTI-CANNIBALIZATION note
НОВ per-title pillar. Distinct primary kw „mustang gold / мустанг голд". Distinct от Mustang Gold Megaways (2024, 117649 начина) и другите Pragmatic Gold/Collect заглавия (Wolf Gold vk-0048, Wild West Gold, Buffalo King). Котва към Pragmatic профил (vk-0019, /blog/pragmatic-play-provajdar/). Slot explainer → без афилиейт линк; без измислен оператор/лиценз №.

## HUMAN-ACTION LIST (owned by you, Step 6 / Step 8)
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Resolve in-text [VERIFY]: потвърди тавана на паричния символ (1–35× официален vs 1–25× VSO) в live билда на целевия оператор.
3. Потвърди live RTP билда (96.53% default vs 95.54% конфигурация) в инфо-панела на целевия оператор.
4. По желание: потвърди точната дата на пускане (17.01.2019 vs 29.11.2018) и волатилността в официалния инфо-екран.
5. Потвърди афилиейт-лиценз статуса при публикуване (footer казва подадено/очаква; никога „издаден").

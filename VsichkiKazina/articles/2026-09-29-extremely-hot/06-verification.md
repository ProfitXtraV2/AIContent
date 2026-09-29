# 06-VERIFICATION — Всички Казина · 2026-09-29-extremely-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Type: guide (slot explainer) · byline: Георги Тодоров · gate: PASS 94/100 · humanisation: HUMAN-LIKE (external check offline) · run date: 29.09.2026

## Surviving [VERIFY] flags (stay in body)
**1** in-text [VERIFY]: точните множители на звездата скатер (три/четири/пет звезди = 2×/10×/50× общия залог). Присъствието на скатер (звезда) е потвърдено от Amusnet официалния сайт (8 символа, включително Scatter); точните множители се срещат в един достъпен източник (VegasSlotsOnline). Текстът твърди множителите с ясен [VERIFY] маркер, нищо не е фабрикувано. 0 [CONFLICT]/[DATA NEEDED].

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Source | Note |
|---|---|---|
| Provider **Amusnet Interactive** (ex-**EGT Interactive**), rebrand **юни 2022** | Amusnet official; отраслов консенсус | Same company, new name. |
| Release **2016** | Amusnet official (2016-02-20); SlotCatalog (2016-02-20) | VSO казва 2015 — divergence; текстът ползва 2016. |
| **5x3, 5 фиксирани линии** | Amusnet official; SlotCatalog; slotsmate | Fixed, не се избират. |
| **RTP 95.74%** (default), конфигурируем от оператора | Amusnet official; SlotCatalog; slotsmate | Точни алт tiers не листнати публично → хеджирано. |
| **Домашно предимство ~4.26%** | Изведено 100 − 95.74 | |
| **€1000 → €957.40 / €42.60** | Recalc от RTP | Виж RECALCULATION. |
| **Волатилност 3 от 5** | Amusnet official („3 / 5"); SlotCatalog („Med") | |
| **Пет 7-ци = 1000× залога на линия** | VegasSlotsOnline (paytable) | База преди множител. |
| **Максимум 5000× залога на линия** | Amusnet official („5000 x bet per line"); SlotCatalog (x5000) | 1000× × множител ×5 = 5000×. |
| **Мултипликатори ×3 (9) / ×4 (12) / ×5 (15)** | SlotCatalog; slotsmate; VSO | Еднакви символи по 3/4/5 барабана. |
| **Без wild символ** | SlotCatalog; slotsmate; VSO | Distinctive vs роднините. |
| **Звезда скатер, 3/4/5 = 2×/10×/50× total** → [VERIFY] | VSO (множители); Amusnet (наличие) | Single-source точни числа. |
| **Gamble red/black, печалби под 35× total** | VSO | 50/50 double. |
| **Jackpot Cards 4 бои (спатия→каро→купа→пика), reveal 3 same suit, tied to bet** | VSO; SlotCatalog; Amusnet | Random mystery progressive. |
| **8 символа** (череши, лимони, портокали, сливи, звънец, BAR, 7, звезда) | Amusnet official; SlotCatalog; VSO | |

## SOURCES REACHED (URLs)
- https://amusnet.com/games/online-casino/extremely-hot (official — RTP 95.74%, 5 reels / 5 Fixed, volatility 3/5, max 5000× bet per line, release 2016-02-20, 8 symbols incl. Scatter, Gamble, Jackpot Cards, Bonus Spin Mode, multiplier; Game ID 880) — REACHED
- https://slotcatalog.com/en/slots/Extremely-Hot (95.74%, 5-3, 5 fixed, Med, x5000, no wild, star scatter, Jackpot Cards clubs→spades, gamble <35× total, multipliers ×3/×4/×5, 2016-02-20) — REACHED
- https://www.slotsmate.com/software/amusnet-interactive/extremely-hot (95.74%, 5 reels, 5 fixed, 3/5, 5000× line, 2016-02-20) — cited via search snippet (direct fetch returned HTTP 400)
- https://www.vegasslotsonline.com/egt/extremely-hot/ (no wild; star scatter 2×/10×/50×; five 7s 1000× line; multipliers ×3/×4/×5; gamble <35× total; Jackpot Cards clubs lowest → spades highest) — REACHED
- https://wizardofodds.com/games/best-payout-slots/amusnet-interactive/ (Amusnet RTP context; Extremely Hot не листнат там) — REACHED

## RECALCULATION (worked-€ example + SVG numbers ⊂ body)
- RTP 95.74% на €1000: връщане 0.9574 × €1000 = **€957.40**; казино 0.0426 × €1000 = **€42.60**. ✓ съвпада с текст/инфографика.
- Max: пет 7-ци = 1000× залога на линия; пълно поле множител ×5 → 1000 × 5 = **5000× залога на линия**. ✓
- SVG bar: player 0.9574 × 656 px = 628.05 ≈ **628 px**; house 0.0426 × 656 = 27.9 ≈ **28 px** (x=660..688). ✓ вътре в 8..712 рамката.
- Всички числа в SVG (текст + aria-label) ⊂ тяло: 95.74%, 4.26%, €1000, €957.40, €42.60, „5000 пъти залога на линия", „3 от 5", „5 фиксирани". Проверено grep-verbatim. ✓

## COMPLIANCE SPOT-CHECK (verbatim untouchables)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (в заключението + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026, ДВ бр. 69), pending-application wording, БЕЗ issued-licence claim, БЕЗ измислен №. ✓
- НЯМА BG оператор, НЯМА НАП лиценз №, НЯМА данъчна секция, НЯМА бонус условия, НЯМА афилиейт линк. ✓
- Byline Георги Тодоров; brand „Всички Казина"; дати 29.09.2026 (DD.MM.YYYY); € валута. ✓
- Em-dashes (—): 0 в тяло/ALT/caption/SVG. En-dash само footer „10:00–17:00". ✓
- Internal links: 4 от одобрения жив набор (/blog/amusnet-egt-provajdar/, /kak-ocenyavame/, /slot-igri/, /otgovorna-igra/). ✓

## ANTI-CANNIBALIZATION note
НОВ per-title pillar. Distinct primary kw „extremely hot" + „екстримли хот" + „extremely hot egt"; отделен от стълбовете 20 Super Hot / 40 Super Hot / Burning Hot / Sizzling Hot и от Amusnet провайдър профила (към който котвата /blog/amusnet-egt-provajdar/ анкерира естествено). Различаваща се механика (без wild, стълбица мултипликатори) подсилва отделния интент. Игра-обяснение, не оператор review → без афилиейт линк; без измислен оператор/лиценз №.

## HUMAN-ACTION LIST (owned by you, Step 6 / Step 8)
1. Попълни „[About Всички Казина boilerplate]" слота.
2. Resolve in-text [VERIFY]: потвърди точните множители на звездата скатер (2×/10×/50× общия залог) в live билда на целевия оператор; наличието на скатер е потвърдено.
3. Потвърди live RTP билда за Extremely Hot при целевия оператор (95.74% default vs по-ниска конфигурация) в инфо-панела.
4. Потвърди feature wording (звезда скатер, мултипликатори ×3/×4/×5, Jackpot Cards, gamble под 35× total) спрямо live билда при публикуване.
5. Потвърди афилиейт-лиценз статуса при публикуване (footer казва подадено/очаква; никога „издаден").

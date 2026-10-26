# 06-VERIFICATION — Всички Казина · 2026-09-18-spaceman
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot except the non-fabrication corrections below.*

Article: **Spaceman (Pragmatic Play): RTP, cash-out механика и как се играе** · type: **guide (game explainer)** · byline: editorial (signed Георги Тодоров) · gate: PASS 94/100 · humanisation: HUMAN-LIKE · Gemini Step-7: **skipped (429)** · images: 2 SVG (hero + cash-out/key-facts infographic), review **skipped (429)**, manual integrity clean · run date: 18.09.2026
No НАП licence № · no affiliate link · no operator T&C (game explainer, not an operator review).

## Non-fabrication corrections (the #1 rule in action)
- **„ДВА НЕЗАВИСИМИ ЗАЛОГА": заданието описва Spaceman като „supports two independent bets".** Проверката показва друго: три детайлни ревюта (bigwinboard, clashofslots, crashgamblingsites) изрично казват, че Spaceman работи с **един залог на рунд** с двоен cash-out (пълен + 50% частичен) плюс авто-кешаут — „single bet ... rather than two independent bet panels". Двата паралелни панела за залог са сигнатура на **Aviator (Spribe)**, не на Spaceman. Да припиша на Spaceman несъществуващ втори независим залог = измислена механика = CRITICAL. Затова текстът описва механиката точно (един залог + 50% cash-out + авто-кешаут) и изрично разграничава от Aviator.
- **Вътрешен линк за крас игрите.** Заданието предлага `/kazino-igri/krash-igri/`. В живия sitemap (https://vsichkikazina.bg/sitemap.xml, проверено 18.09.2026) тази пътека **НЕ съществува**. Общата крас-страница е **`/blog/krash-igri-aviator/`** (lastmod 2026-09-15). Затова линкът към крас игрите сочи `/blog/krash-igri-aviator/`.

## Conflicts hedged in prose (NOT written as Version A/B)
- **Дата на издаване.** 24.03.2022 (slotcatalog, askgamblers, crashgamblingsites, americancasinoguide) срещу 28.03.2022 (bigwinboard). → В текста „**март 2022 г.**" без ден, за да не се фиксира спорна стойност.
- **RTP.** 96.50% default (bigwinboard, slotcatalog, askgamblers spec table) срещу 95.50% (clashofslots, crashgamblingsites). → „**96.50%** в основната конфигурация" + „по-ниски версии, около 95%, а операторът избира коя да зареди... проверява се в инфо-панела".
- **Макс. залог.** €100 (мнозинство) срещу $1000 (clashofslots, outlier). → **€100**.

## Surviving [VERIFY] flags (hedged in prose)
0 in-text [VERIFY] flags. Всички специфични числа са потвърдени от ≥2 източника (Pragmatic правила + международни бази). Рекламният таван и RTP версиите са хеджирани в прозата („рекламен таван, не очакван изход"; „операторът избира коя да зареди... проверявай в инфо-панела").

## Time-sensitive / factual claims to confirm at publish (source URLs)
| Claim | Source URL | Note |
|---|---|---|
| Провайдър **Pragmatic Play**; издадена **март 2022 г.** | https://www.askgamblers.com/casino-games/online-slots/reviews/spaceman-pragmatic-play ; https://slotcatalog.com/en/slots/Spaceman | Ден хеджиран (24 срещу 28 март). |
| **Crash игра** (без барабани/линии); множител от **1.00x** | https://www.crashgamblingsites.io/en/crash-games/spaceman/ ; https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ | Не е ротативка. |
| **RTP 96.50%** (default); по-ниска версия **около 95%** | https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ ; https://slotcatalog.com/en/slots/Spaceman | Оператор-конфигурируем; потвърди версията на казиното. |
| **Макс. печалба 5000x** (€500 000 при €100) | https://www.askgamblers.com/casino-games/online-slots/reviews/spaceman-pragmatic-play ; https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ | Primary spec + бази. |
| **Залог €1 - €100** на рунд | https://slotcatalog.com/en/slots/Spaceman ; https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ | Outlier $1000 отхвърлен. |
| **Cash-out**: ръчен + 50% частичен + авто (1.01x - 4999.99x) + 50% авто; **един залог** | https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ ; https://clashofslots.com/crash-games/pragmatic-play/spaceman/ | „single bet ... not two independent bet panels". |
| Волатилност — определя се от целта на cash-out (студиото я позиционира като висока) | https://slotcatalog.com/en/slots/Spaceman ; https://www.bigwinboard.com/spaceman-pragmatic-play-slot-review/ | „no artificial volatility". |

## Illustrative numbers used (marked „примерни" in text)
| Where | Figure | Note |
|---|---|---|
| RTP/edge worked example | €1000 → ~€965 / ~€35 | илюстративно, в прозата |
| Cash-out worked example | €10 залог × 2.00x = €20 (€10 печалба); 50% на 2.00x = €10 | означено „примерни числа" |
| SVG RTP бар | 96.50% = 637px от 660px (637+23 flush) | math checked |

## Recalculation shown
- Домашно предимство = 100% − RTP% = 100% − **96.50% = 3.50%**. ✓ (в текста и в подзаглавието на инфографиката).
- RTP 96.50% на €1000: 0,9650 × €1000 = **€965,00** (в текста „~€965"); казино 0,0350 × €1000 = **€35,00** (~€35). ✓ (илюстративно).
- Cash-out пример: 2.00x × €10 = **€20** → печалба €20 − €10 = **€10**. 50% cash-out на 2.00x = €5 залог × 2.00x = **€10** прибрани. ✓ (примерно).
- Макс. печалба: 5000x × €100 = **€500 000**. ✓
- SVG RTP бар: 0,9650 × 660 = **636,9 ≈ 637 px** играч + **23 px** казино = 660 px, flush, без overlap. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — тяло (секция „Таванът 5000x и за кого е играта") + footer RG блок. ✓
- RG signposting: /otgovorna-igra/ (тяло + footer) + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 авг 2026 / ДВ бр. 69 от 31.07.2026), pending-application, NO issued claim, NO invented №. ✓
- Internal links (approved set, 4 distinct): /blog/krash-igri-aviator/ · /kak-ocenyavame/ · /blog/games-providers/ · /otgovorna-igra/. Форма [текст](/път/). Всички проверени в sitemap 18.09.2026. Без афилиейт линк. ✓
- Byline Георги Тодоров + 18.09.2026; brand „Всички Казина". ✓ Zero em-dashes (grep = 0). En-dash само footer „10:00–17:00". ✓ Game explainer → no affiliate link. ✓

## Anti-cannibalization note
Няма Spaceman страница в sitemap (проверено 18.09.2026). Distinct branded kw „spaceman / спейсмен". Общата крас-страница /blog/krash-igri-aviator/ (vk-0018) покрива категорията крас игри и се реферира като линк, НЕ се дублира. Различен от Aviator (Spribe) — тази страница е за брандирания Spaceman на Pragmatic Play.

## Step 7 — external Gemini check
external check: skipped (Gemini unavailable — HTTP 429 credits depleted). content-queue gemini = skipped.

## Step 8 — images
images: 2 (images/spaceman-hero.svg; images/spaceman-cash-out.svg; review skipped 429; manual integrity 0 fabrications). Всички числа в инфографиката съвпадат дословно с 05b (96.50% / около 95% / 3.50% / 5000x / €500 000 / €1 - €100 / crash / множител от 1.00x / авто 1.01x - 4999.99x / 50% cash-out / Pragmatic Play, 2022). Няма оператор лога, фалшив UI, хора/лица или разкрасена печалба. Рендер проверен (cairosvg): без overlap, без изрязване, четимо на дисплейна ширина.

## Brand gate
score: **PASS 94/100** — Personality 19/20 | Tone 14/15 | E-E-A-T 19/20 | Trust 14/15 | Language&Style 14/15 | RG 14/15. 0 criticals.

## Human-action list (Step 6 / publish)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Потвърди RTP версията на конкретното казино (default 96.50%; по-ниска около 95%) и max win 5000x в инфо-панела/играта.
3. Потвърди точната дата на издаване, ако е нужна на ден (DB консенсус 24.03.2022; bigwinboard 28.03.2022 → в текста „март 2022 г.").
4. Потвърди афилиейт-лиценз статуса при публикуване (footer казва подадено/в очакване; никога „издаден").

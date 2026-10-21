# 01 — Synthesis (Step 1)

Query: Spaceman (Pragmatic): RTP, cash-out механика и как се играе | Intent: informational | Market: bg (BG, €, НАП)
Sources: 6 reachable (askgamblers, bigwinboard, slotcatalog, clashofslots, crashgamblingsites, официални правила Pragmatic Play v1.7)
Corroborated facts used: 8 | [VERIFY] flags: 0 (всичко потвърдено от официален източник + ≥2 бази) | [CONFLICT] flags: 3 (хеджирани, вж. по-долу)
Entity union coverage: complete
Byline: editorial (подпис Георги Тодоров) — game explainer, patient-teacher register.

## FACT INVENTORY
CORROBORATED (провайдър + ≥2 бази):
- Провайдър: **Pragmatic Play**. (askgamblers, bigwinboard, slotcatalog)
- Тип: **crash игра**, не ротативка — без барабани, без линии; множител расте от **1.00x** нагоре, докато „спейсменът" отлети и рундът се срине. (всички)
- **RTP 96.50%** (default конфигурация). (bigwinboard, slotcatalog, askgamblers spec table)
- **Макс. печалба 5000x** залога; €500 000 при €100 залог. (всички)
- **Залог €1 - €100** на рунд. (bigwinboard, slotcatalog, askgamblers, crashgamblingsites)
- **Авто-кешаут 1.01x - 4999.99x**; отделно и **50% авто-кешаут**. (bigwinboard, crashgamblingsites)
- **50% частичен cash-out**: осребряваш половината печалба и оставяш другата половина в игра за по-висок множител. (всички)
- Волатилността НЕ е фиксирана — определя се от момента/целта на cash-out на играча; студиото я позиционира като висока. (slotcatalog, bigwinboard)

SINGLE-SOURCE / изведени:
- Домашно предимство = 100% − 96.50% = **3.50%** (изведено).
- Издадена **март 2022 г.** (slotcatalog/askgamblers 24.03; bigwinboard 28.03 → ден хеджиран).

CONFLICTING (хеджирани в текста; НЕ се пишат като „Версия А/Б"):
- Дата: 24.03.2022 (мнозинство) ⟷ 28.03.2022 (bigwinboard). → „март 2022 г." без ден.
- RTP: 96.50% (мнозинство) ⟷ 95.50% (clashofslots, crashgamblingsites). → 96.50% default + „операторът може да зареди по-ниска версия (около 95%)".
- Макс. залог: €100 (мнозинство) ⟷ $1000 (clashofslots, outlier). → €100.

## NON-FABRICATION CORRECTION (resolved at synthesis)
Заданието: „supports two independent bets". Първоизточниците: Spaceman е ЕДИН залог на рунд с двоен cash-out
(пълен + 50% частичен) + авто-кешаут. Двата независими залога са на Aviator (Spribe), не на Spaceman.
→ Текстът описва един залог + 50% cash-out + авто-кешаут; не приписва несъществуващ втори залог. (bigwinboard, clashofslots, crashgamblingsites изрично: „single bet ... rather than two independent bet panels".)

## ENTITY UNION
Pragmatic Play · crash игра · множител · cash-out (ръчен/авто/50%) · RTP · домашно предимство · волатилност ·
таван 5000x · залог €1-€100 · демо режим · Aviator (Spribe) като категориен ориентир · отговорна игра · НАП.

## GAPS CLOSED THAT NO SINGLE SOURCE COVERS
- Честната връзка между „сам определяш волатилността" и НЕподвижното домашно предимство (3.50%): по-агресивна цел = по-редки, по-едри попадения върху същата математика, не по-голям шанс за плюс.
- Реален RTP на конкретното казино срещу рекламния — версиите се различават, проверява се в инфо-панела (мостра към методологията).
- Ясно разграничаване crash игра ≠ ротативка, и Spaceman ≠ Aviator (различен провайдър, различна сигнатура: 50% cash-out).

## SOURCE CLAIMS EXCLUDED AS DUBIOUS
- „Dual bet panel като Aviator" (агрегатор WebSearch) — противоречи на трите детайлни ревюта; изключено.
- „$1 - $1000" залог (clashofslots) — outlier срещу консенсус €1-€100; изключено.

## LOCALISATION
€ навсякъде; DD.MM.YYYY; НАП; native BG casino vocabulary (крас игра, множител, залог, cash-out/осребряване,
демо режим, волатилност, RTP, домашно предимство). Без сравнение с фиатни валути извън €.

SUGGESTED PERSONA: editorial (Екипът на Всички Казина voice), подписан Георги Тодоров — game explainer е
patient-teacher, без протокол на тегленето (няма реален receipt за crash игра).

# 01 — SYNTHESIS · Lightning Blackjack (Evolution)

Query: Lightning Blackjack (Evolution): как се играе, множители и RTP | Intent: informational (how-it-works + RTP) | Market: bg
Sources: 4 (LiveCasinoComparer, Wizard of Odds, Evolution official, casinos.com) | Corroborated facts: 100% Lightning Fee, множители 2x–25x, множител се пренася към следваща печеливша ръка (само до размера на предишния залог), RTP 99,56% optimal-first-hand, ефективно ~82,4% (edge ~17,6% спрямо залога / ~8,82% спрямо всичко заложено), 3:2, 8 тестета | [VERIFY]: 3 | [CONFLICT]: 0 (exact discrete multiplier ladder разминаване → представено като диапазон, не флаг за отделна стойност).
Entity union coverage: complete (блекджек на живо, 8 тестета, 3:2, Lightning такса 100%, светкавична карта/множител 2x–25x, пренос към следваща ръка, RTP, домашно предимство, Evolution).

Gaps closed that no single source foregrounds: the honest €-cost of the 100% fee (you pay double every round; a losing hand burns the fee too), and WHY the flashy 99,56% is misleading (optimal + first-hand only; realistic return ~82% once the fee is priced in). The "multiplier only pays on consecutive wins, only up to the prior bet" nuance is the real trap and is foregrounded.
Source claims excluded as dubious: exact discrete multiplier values (sources disagree — Evolution/LCC list {2,5,8,10,15,20,25}; WoO gives per-total ranges; casinos.com another split) → presented as span 2x–25x rather than a fabricated fixed ladder. Precise operator stake caps (€1–€5000, max win €187,500) → operator/version-dependent, omitted rather than asserted as universal.
Localisation: native BG casino vocabulary (такса, множител, домашно предимство, ръка, тесте); € worked example; no operator/НАП facts (game explainer).

FACT INVENTORY (tagged)
- Обикновен блекджек на живо: 8 тестета, блекджек 3:2, стандартни правила; неограничени места (обща ръка). [CORROBORATED]
- Lightning такса = 100% от залога, добавя се на всяка ръка, не се връща. [CORROBORATED — 3 sources]
- Печеливша ръка → случаен множител 2x–25x; по-високите ръце/блекджек → по-едрите. [CORROBORATED / exact discrete values VERIFY]
- Множителят се пази за следващата печеливша ръка, само до размера на предишния залог; при удвояване върху цялата печалба, при разделяне на двете ръце; валиден до 180 дни. [CORROBORATED]
- RTP до 99,56% (оптимална стратегия, първа ръка); ефективно ~82% (edge ~17,6% спрямо залога / ~9% спрямо залог+такса). [VERIFY — analyst calc, not operator-published]
- Betting window ~15s. [VERIFY — single-source, version-dependent]
- Множителите са платени от таксата (mechanism). [CORROBORATED]

SUGGESTED PERSONA: Георги Тодоров (persona) — numbers-first game explainer, honest-cost angle; matches the live-game-spoke pattern (Lightning Dice/Baccarat/Roulette).

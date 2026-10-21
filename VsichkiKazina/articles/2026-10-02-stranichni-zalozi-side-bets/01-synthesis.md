# 01-SYNTHESIS — vk-0240

## Query / intent
„Странични залози: струват ли си математически?" Информационно търсене; играчът вече е видял „Перфектна двойка"/„21+3"/„Tie" на масата и иска цифра, не мнение.

## Entity union (from sources: Wizard of Odds ×5 pages + PokerNews corroboration)
- Блекджек: Perfect Pairs (смесена/цветна/перфектна двойка), 21+3 (две карти на играча + отворената на дилъра = покер ръка от три карти), основна игра с основна стратегия.
- Бакара: Banker/Player/Tie, Player Pair / Banker Pair, комисиона 5% върху Banker.
- Рулетка: единична и двойна нула (контекст за еднаква цена на всички залози).
- Понятия: домашно предимство, честни коефициенти срещу изплащане, честота на попадение, дисперсия, брой тестета, изплащателна таблица.

## Core claim (the thesis the draft must carry)
Страничният залог е отделен залог върху рядко събитие, платено по фиксиран коефициент, по-нисък от честния. Предимството на казиното е многократно над това на основната игра и зависи силно от таблицата и броя тестета.

## Verified numbers (all long-run, all recomputed; see 00-brief)
См. 00-brief „VERIFIED FIGURES". Резюме: Perfect Pairs 25/12/6: 22.33 / 10.14 / 6.11 / 4.10% (2/4/6/8 тестета); 21+3 (всичко 9:1): 13.30 / 7.26 / 4.24 / 3.24 / 2.74% (1/2/4/6/8); 21+3 30/20/10/5 (6 тестета) 13.39%; бакара Banker 1.06 / Player 1.24 / Tie 14.36 / Pair 10.36%; блекджек основна ≈0.5% (0.43% AC, 0.28% Вегас Стрип); рулетка 2.70 / 5.26%.

## Conflicts
- Task brief says „Perfect Pairs ≈ 2–11%, 21+3 ≈ 2–13%". Wizard shows wider range for Perfect Pairs (2.17% best 8-deck table up to 22.33% at 2 decks, up to 26.21% for a weaker table at 2 decks). RESOLVED to the single fact: quote exact paytable+deck pairs, never a loose range. No A/B dilemma in text.
- Blackjack base ≈0.5% vs Wizard 0.28%/0.43%: resolved as „около 0,5%, зависи от правилата" with the Wizard examples named.

## Excluded claims
- Any operator-specific paytable, any provider name/branded game, hit-frequency claims for 21+3 (not sourced), anything about bonus wagering contribution of side bets (unverified → excluded), tax.
- Roulette „side bets" (live bonus multipliers): no verified paytable → not quantified.

## Gaps no source covers (to add as substance)
- Worked € comparison: €10 base vs €1 side over 100 hands; €1 Tie vs €10 Banker.
- Why a small side stake still costs more than the large base stake.
- Honest verdict + RG framing (separate entertainment budget).

## Draft (original expression)
See 02-draft.md (written fresh from the outline, not from this synthesis wording).

## Suggested persona
Георги Тодоров, persona voice, no anecdotes, no receipts block (guide).

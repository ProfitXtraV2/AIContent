# 06-VERIFICATION — vk-0240 · 2026-10-02-stranichni-zalozi-side-bets

## Surviving flags
[VERIFY] / [DATA NEEDED] / [CONFLICT] in text: 0. Residual caveats written as plain text: (a) paytables of any specific table differ, figures are „примерни при посочената изплащателна таблица"; (b) blackjack ≈0,5% is rule-dependent (0,28%-0,43% examples named). No tax, licence or operator claims in the article.

## Sourced claims (all long-run house edge, primary = Wizard of Odds, accessed 02.10.2026)
- Perfect Pairs 25/12/6: 22,33 / 10,14 / 6,11 / 4,10% (2/4/6/8 decks); other 8-deck tables 2,17% (25/15/5), 7,95% (25/12/5): https://wizardofodds.com/games/blackjack/side-bets/perfect-pairs/
- 21+3 all-wins-9:1: 13,30 (1d) / 7,26 (2d) / 3,24 (6d) / 2,74% (8d); 30/20/10/5 table 6 decks 13,39%: https://wizardofodds.com/games/blackjack/side-bets/21plus3/
- Baccarat 8 decks: Banker 1,06 / Player 1,24 / Tie 14,36%: https://wizardofodds.com/games/baccarat/basics/ and https://wizardofodds.com/gambling/house-edge/
- Baccarat Pair 11:1 = 10,36%, Tie 8:1 = 14,360%: https://wizardofodds.com/ask-the-wizard/baccarat
- Roulette 2,70% (single zero) / 5,26% (double zero), blackjack liberal Vegas Strip 0,28%: https://wizardofodds.com/gambling/house-edge/
- Blackjack Atlantic City rules 0,43%: Wizard of Odds blackjack house-edge Q&A (https://wizardofodds.com/ask-the-wizard/blackjack/house-edge/; surfaced via search, the fetched page did not restate the figure verbatim). The text says „около 0,5%" and cites 0,43% / 0,28% only as examples; if a stricter check is wanted, treat the 0,43% example as the one item to re-confirm by a human (low risk, not load-bearing).
- Corroboration only (not a numeric source): PokerNews blackjack side-bets page echoes 6,11% (25/12/6, 6 decks) and 3,24% (21+3 at 9:1).

## Recalculation shown (one figure, full working)
Перфектна двойка 25/12/6, 6 тестета (312 карти). Първата карта е фиксирана; остават 311. Същия ранг: 5 карти със същата боя (перфектна), 6 със същия цвят (цветна), 12 с другия цвят (смесена): общо 23 от 311 = 7,40%.
EV на €1 = (5×25 + 6×12 + 12×6)/311 − (1 − 23/311) = 269/311 − 288/311 = −19/311 = −0,0611 → домашно предимство 6,11%. Съвпада с Wizard of Odds (6,11%).
€ пример: 100 × €1 = €100 оборот × 6,11% = €6,11; основна игра 100 × €10 = €1 000 × 0,5% = €5,00; сума €11,11.
Допълнително (Python, точно изброяване): 21+3 9:1 при 1/2/6/8 тестета = 13,30 / 7,26 / 3,24 / 2,74%; двойка в бакарата 31/415 → 10,36%. Всички съвпадат с Wizard.

## Gemini text check
Check 1 on 05b: „Likely human-written, 85% confidence" → human-likeness 85, PASS (≥80). Passes applied: 0 (no humaniser pass needed). Version kept: initial 05b (pass 0), 85%. Recommendations noted but not applied (PASS): link placement, „Вердикт" H2, definition length, ticket metaphor. Verdict: 07-gemini-check-1.md.

## Images
images: 2 (infographic SVG 100, hero WebP 100); one review pass (08-image-review-1.md), no integrity failure, no layout defect; hero is an abstract balance-scale metaphor with no text/people/logos.

## Compliance spot-checks
Byline Георги Тодоров; brand „Всички Казина"; dates 02.10.2026; em-dashes 0; internal links /kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/ (all approved); no affiliate links in body; affiliate footer verbatim; no „Протокол на тегленето" block.

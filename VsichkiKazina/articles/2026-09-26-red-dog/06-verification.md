# 06 — VERIFICATION · vk-0182 · Red Dog (Ред Дог)

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0.

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (payouts by spread + house edge by deck count + raise-on-7 rule;
  numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED.
  images: 1 (infographic, review skipped — API down). See 08-image-review-1.md.

Body word count: 1121 (prose, excluding image ALT/caption and footer blocks). Within the 1000–1500 guide band.

## EVERY SPECIFIC FIGURE → PRIMARY SOURCE
Sources reached and read 26.09.2026.
A = Wizard of Odds — Red Dog — https://wizardofodds.com/games/red-dog/  (math referee)
B = Pagat — In Between — https://www.pagat.com/banking/in-between.html
C = Wikipedia — Red dog (card game) — https://en.wikipedia.org/wiki/Red_dog_(card_game)

| Figure in body | Value | Source |
|---|---|---|
| Тесте | 1 × 52 карти, асо високо, боята без значение | A,B,C |
| Механика | 2 открити карти; spread = рангове строго между тях | A,B,C |
| Последователни карти (spread 0) | push (залогът се връща) | A,B,C |
| Чифт → трета карта | съвпадение → 11:1; иначе push | A,B,C |
| Ход при spread ≥1 | call или raise (до първоначалния залог); трета строго между → печели | A,B,C |
| Изплащане spread 1 | 5:1 | A,B,C |
| Изплащане spread 2 | 4:1 | A,B,C |
| Изплащане spread 3 | 2:1 | A,B,C |
| Изплащане spread 4–11 | 1:1 | A,B,C |
| Домашно предимство — 1 тесте (правилна игра) | 3.155% (спрямо първоначалния залог) | A |
| Element of risk — 1 тесте | 2.672% (спрямо реално рискуваното) | A |
| Домашно предимство — 2 тестета | 3.077% | A |
| Домашно предимство — 4 тестета | 2.884% | A |
| Домашно предимство — 6 тестета | 2.798% | A |
| Домашно предимство — 8 тестета | 2.751% | A |
| Посока на ефекта | повече тестета → по-НИСКО предимство | A |
| Стратегия | вдигай само при spread ≥ 7 | A |
| RTP — 1 тесте | ≈96.85% (= 100% − 3.155%) | derived from A |
| RTP — 8 тестета | ≈97.25% (= 100% − 2.751%) | derived from A |

Note: the €10 example is labelled примерни. „Разстояние 6 → 1:1" in the example is consistent with the „4 до 11 → 1:1" band.

## RECALCULATION (with working)
- RTP(1 тесте) = 100% − 3.155% = 96.845% → body states ≈96.85%. ✓
- RTP(8 тестета) = 100% − 2.751% = 97.249% → body states ≈97.25%. ✓
- Label distinction: 3.155% = house edge per INITIAL wager; 2.672% = element of risk per money ACTUALLY at risk (accounts
  for raised bets). Different denominators, not mixed in the body. ✓
- Deck-count direction: verified against Wizard table (1→8 decks: 3.155 → 2.751). Body states more decks = slightly lower
  edge (the counter-intuitive point), matching A. ✓

## INTERNAL LINKS USED (5 anchors, all live in sitemap 26.09.2026)
1. /kazino-igri/ — anchor „казиното"
2. /kazino-igri/kazino-na-zhivo/ — anchor „казиното на живо"
3. /kazino-igri/blakdzhak/ — anchor „блекджека" (contrast: blackjack has strategy, Red Dog barely does)
4. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG touch)
5. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- Confirm single-deck edge 3.155% / element of risk 2.672% and the deck-count table vs the live Wizard of Odds page.
- Confirm the raise-on-spread-7+ threshold and the 5:1/4:1/2:1/1:1 + 11:1 payout table vs the target operator's felt
  (payouts and raise rules can vary by house).
- No operator named, no НАП/tax claim, no affiliate — correct for an educational guide.
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.

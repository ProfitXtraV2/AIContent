# 01 — SYNTHESIS · vk-0181 · Pai Gow Poker (Пай Гоу покер)

## Sources fetched + read (26.09.2026)
- A (PRIMARY, all math): Wizard of Odds — Pai Gow Poker — https://wizardofodds.com/games/pai-gow-poker/
  (+ play page for the ≈2.84% headline: https://wizardofodds.com/play/pai-gow-poker/ ; FAQ; side-bet appendix)
- B (rules corroboration): Pagat — Pai Gow Poker — https://www.pagat.com/partition/paigowp.html
- C (rules corroboration + card-vs-tile distinction): Wikipedia — Pai gow poker — https://en.wikipedia.org/wiki/Pai_gow_poker

## Resolved facts (single value each)
- 53-card deck (52 + joker); joker rules per A,B,C (5-card: ace/straight/flush/straight-flush/royal; 2-card: always ace).
- 7 cards each; 5-card back + 2-card front; back > front or foul. Both hands beat dealer to win; split = push; copy → dealer.
- Commission 5% on winning bets. [A,C]
- House edge non-banking: headline ≈2.84% (A play page); house-way ≈2.7212% (A analysis). Push ≈40.4958% house-way (A).
- Strategy: house way is near-optimal; general split principle (strong 5 back, next two front). [A,B,C]

## Conflicts / flags
- 2.84% (rounded headline) vs 2.7212% (precise house-way) vs 2.5122% (optimal): NOT a conflict — same source, different
  granularity. Body uses 2.84% headline + 2.72% house-way. Wizard is referee.
- Push 40.4958% (house-way) vs 41.48% (raw banker-vs-player tie rate): use ≈40.5% (house-way) in the body.
- [VERIFY] element of risk ≈2.73% — could not be reproduced from a reachable page → NOT stated in body.
- [VERIFY] exact per-holding house-way splits — Wizard house-way sub-page 404'd → body gives only the general principle.
- Side-bet edges (Emperor's Challenge 4.171%, Progressive 11.5428% etc., A appendix) → body states "several times the base,
  often above 4% and double-digit for progressives" without pinning a single number as universal.

Surviving flags in body: [VERIFY] 0 · [DATA NEEDED] 0 · [CONFLICT] 0 (uncertain figures were omitted, not flagged into prose).

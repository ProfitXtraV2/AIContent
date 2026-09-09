# 06 — Verification · Live game shows (Crazy Time, Monopoly Live, Lightning Roulette)

vk-0025 · type: guide (live game-show format explainer, public game data) · byline: Георги Тодоров · brand: Всички Казина

## Surviving flags
**1 in-text `[VERIFY]`** (Monopoly Live, §"Monopoly Live"): the exact *lower* RTP bound by bet. The top figure (~96.23% on the number bets) is solidly corroborated across sources; public game databases diverge on the bonus-bet floor (some cite low-90s, others the ~80s). The text states "по публични оценки към 80-те процента" and flags the ambiguity for the human team. Crazy Time and Lightning Roulette figures are fully verified (no flags). No operator T&C / НАП data used (format explainer on public game data).

## Time-sensitive / factual claims + sources (web-verified, Evolution titles)
- **Crazy Time:** 54-segment wheel; numbers 1/2/5/10; number 1 on 21 segments; 4 bonus games (Cash Hunt = 108 hidden multipliers, Pachinko, Coin Flip, Crazy Time); Top Slot multiplier up to 50x; top multiplier up to 20 000x; RTP by bet ~94.33% (bonus bets) to ~96.08% (number 1) — Evolution public game info + game databases.
- **Monopoly Live:** money wheel with numbers 1/2/5/10 + 2 Rolls / 4 Rolls bonus; Chance card adds multipliers; top RTP ~96.23% (number bets); bonus-bet floor lower (~80s) [VERIFY] — game databases.
- **Lightning Roulette:** single-zero European roulette with 1–5 lucky numbers per round carrying 50x–500x random multipliers; straight-number payout reduced to 29:1 (vs 35:1) to fund the multipliers; RTP even-money bets ~97.30%, straight-number bets ~97.10% — Evolution public game info + game databases.

## Recalculation (working shown)
**Lightning Roulette straight-bet trade-off.** Standard single-zero roulette: straight pays 35:1 on 37 pockets → EV = (1/37)(+35) + (36/37)(−1) = −1/37 = −2.70% (RTP 97.30%). Lightning reduces the base straight payout to 29:1 and adds occasional 50x–500x multipliers on lucky numbers; the reduced base funds the rare multipliers, leaving the straight-bet RTP slightly below the even-money ~97.30% (≈97.10% per public data). This matches the text's "подаръкът е по-скоро счетоводство" framing. Even-money bets never light up, so they keep the ~97.30% European figure.

## Gemini Step-7 (text, cross-model)
Model gemini-3.1-pro-preview. Initial draft **HL 85 ("Likely human-written 85%") — PASS on the first check**; initial kept (no Humaniser pass needed). content-queue `gemini` = **human 85**. Trail: 07-gemini-check-1.md.

## Images (Step 8)
**2 images.** Infographic `live-game-shows-rtp-sravnenie-infografika.svg` (RTP ranges per title; every figure traces to 05b) + decorative hero `live-game-show-koleloto-hero.webp` (37.3 KB WebP, gemini-3-pro-image). Gemini visual review **95/100 PASS**, no integrity failures; applied two cosmetic fixes (dropped "множители" from the hero alt since the wheel shows empty segments; nudged one SVG bar's x for scale precision — no data value changed). `images: 2 (infographic + hero, best 95)`.

## Brand gate
Gate report 05-gate-report.md: **94/100**, PASS WITH FIXES, 0 surviving criticals. Byline Георги Тодоров, brand "Всички Казина", verbatim 18+/RG/affiliate footer, zero em-dashes in body+footer, 3 approved internal links (/kak-ocenyavame/, /kazino-igri/, /otgovorna-igra/). Honest angle: there is no single RTP per game, only RTP per bet; the most spectacular bonus bets return the least; game-show house edge exceeds basic roulette/blackjack; high volatility. Anti-cannibalization: format explainer (prose), distinct from — and not linking — the live-casino listing /kazino-igri/kazino-na-zhivo/.

**Human owns Step 6 (resolve the Monopoly Live [VERIFY], approval) and publishing. Do not merge/post automatically.**

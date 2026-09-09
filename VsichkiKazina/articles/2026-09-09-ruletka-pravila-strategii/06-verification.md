# 06 — Verification · Рулетка: правила и популярни стратегии (вкл. Мартингейл)

vk-0024 · type: guide · byline: Георги Тодоров · brand: Всички Казина

## Surviving flags
**None.** All figures are standard, evergreen roulette mathematics — no operator-specific facts, no НАП licence data, no tax claims, no [VERIFY] flags left in the text.

## Time-sensitive / factual claims + primary sources
Roulette rules and edges are not time-sensitive; figures verified against reputable references:
- European roulette 37 pockets (0–36), house edge **2.70%**; American 38 pockets (adds 00), house edge **5.26%** — Wizard of Odds (wizardofodds.com/games/roulette/), Wikipedia "Roulette".
- French roulette with **la partage / en prison** drops even-money house edge to **~1.35%** — Wizard of Odds, Wikipedia "Roulette" (la partage rule).
- Payout ratios straight 35:1, split 17:1, corner 8:1, dozen/column 2:1, even-money 1:1 — standard European payout table (Wizard of Odds, PokerNews roulette guide).
- Martingale (double-after-loss), table-limit + bankroll failure, negative-EV invariance, gambler's fallacy (independent spins) — Wikipedia "Martingale (betting system)", standard probability.

## Recalculation (working shown)
1. **European house edge.** A straight-up win pays 35:1 but there are 37 pockets. Expected value per €1 on one number = (1/37)·(+35) + (36/37)·(−1) = (35 − 36)/37 = −1/37 = **−0.0270 = −2.70%**. Matches the text.
2. **Martingale cumulative loss before the 7th bet.** Base €10, doubling: 10 + 20 + 40 + 80 + 160 + 320 = **€630** staked and lost across six consecutive losses; the seventh bet needed to continue is €640; a win there returns €640 stake + €640 profit = recovers the €630 and nets the original **+€10**. Matches the text ("рискуваш €630 натрупани загуби, за да гониш печалба от €10").

## Gemini Step-7 (text, cross-model)
Model gemini-3.1-pro-preview. Initial HL 25 ("Shows AI patterns 75%") → Humaniser pass 1 HL 25 (same verdict; detector pinned on BG content). Kept **pass 1** (tied-highest HL, removed genuine tells). Loop stopped at MAX_GEMINI_PASSES. content-queue `gemini` = **ai 75**. Trail: 07-gemini-check-1.md, 07-gemini-check-2.md.

## Images (Step 8)
**2 images.** Infographic `ruletka-domashno-predimstvo-infografika.svg` (every figure traces to 05b) + decorative hero `ruletka-koleloto-i-zalozite-hero.webp` (35.7 KB WebP). Gemini visual review: pass 1 score 70 (grammar "нула" + hero-alt mismatch) → fixed → pass 2 **score 90 PASS**, no integrity failures. `images: 2 (infographic ~100, hero ok — best 90)`.

## Brand gate
Gate report 05-gate-report.md: **96/100**, PASS WITH FIXES, 0 surviving criticals. Byline Георги Тодоров, brand "Всички Казина", verbatim 18+/RG/affiliate footer, zero em-dashes in body+footer, 3 approved internal links (/kak-ocenyavame/, /kazino-igri/, /otgovorna-igra/). Anti-cannibalization: prose-led rules+strategy guide, distinct from the listing /kazino-igri/ruletka/ (not linked).

**Human owns Step 6 (approval) and publishing. Do not merge/post automatically.**

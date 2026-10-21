# 06 — Verification — Extra Stars (vk-0082)

**Type:** guide (game explainer). **Byline:** Георги Тодоров. **Date:** 15.09.2026.

## Surviving flags
- 0 [VERIFY], 0 [DATA NEEDED], 0 [CONFLICT]. No operator/НАП primary sources required (public game data only).
- Max-win figure DELIBERATELY OMITTED: sources conflict (x1,000 vs x20,000 vs observed ~100x). Per spec, top prize described qualitatively (Jackpot Cards progressive + stacked expanded stars), no number stated → no fabrication, no surviving [VERIFY] needed.

## Time-sensitive / factual claims + sources (public game databases — Amusnet public game data; NOT operator T&C / НАП)
- Provider Amusnet Interactive (ex-EGT); 5 reels, 3 rows, 10 paylines, pays both directions (L-R and R-L).
- Expanding star wild on reels 2/3/4 → expands full reel, pays, grants respin; extra stars in respin → more respins, up to 2–3 simultaneous wild reels.
- Jackpot Cards: 4-level progressive by suit (clubs/diamonds/hearts/spades), random after any paid spin; pick from 12 face-down cards until 3 matching suits.
- Gamble: guess red/black to double a line win. Volatility: medium.
  Sources: slotcatalog.com (Extra-Stars), askgamblers.com, slotsup.com, casino.team, clashofslots.com, slotsmate.com.
- RTP: 95.78%. Sources as above (consistent across databases).

## Recalculated figure (working shown)
- RTP 95.78% → house edge = 100 − 95.78 = **4.22%**.
- On €1000 turnover: player return = €1000 × 0.9578 = **€957.80**; casino = €1000 × 0.0422 = **€42.20**. €957.80 + €42.20 = €1000. ✓ (matches 05b text + RTP infographic)

## External Gemini check (Step 7)
- **Skipped — Gemini unavailable** (`gemini_check.py` → GEMINI_ERROR HTTP 429, prepayment credits depleted). Does NOT halt per daily-run.md; `gemini` column = `skipped`. Brand-Gate PASS 95/100, 0 surviving CRITICAL.

## Step 8 — images
- **images: 2** — infographic `extra-stars-rtp.svg` (RTP/€1000 split) + `extra-stars-jackpot-cards.svg` (4-level Jackpot Cards flow, no invented € amounts — suits + „12 карти → 3 еднакви бои" only). Both hand-authored SVG, numbers verbatim from 05b, no operator logos/names, no people, no invented figures.
- Gemini visual review **skipped — Gemini unavailable** (429). Images kept per playbook. 0 integrity concerns.

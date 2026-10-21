# 06 — Verification (видеопокер)

## Surviving flags
None. 0 × [VERIFY], 0 × [DATA NEEDED], 0 × [CONFLICT]. Pure game-math guide; no operator/НАП facts.

## Time-sensitive / factual claims → primary sources
All figures from Wizard of Odds (public game-math authority), verified 25.09.2026:
- Jacks or Better full-pay 9/6 RTP 99.54%; 9/5 98.45%; 8/5 97.30%; SD 4.42; paytable (250/50/25/9/6/4/3/2/1 per coin):
  https://wizardofodds.com/games/video-poker/tables/jacks-or-better/
- Mechanics (5 cards, draw from remaining 47, RNG) + max-coin royal:
  https://wizardofodds.com/games/video-poker/basics/
- Deuces Wild full-pay 100.76% (most tables lower):
  https://wizardofodds.com/games/video-poker/tables/deuces-wild/
- Bonus Poker 8/5 ≈ 99.17%: https://wizardofodds.com/games/video-poker/tables/bonus-poker/
- Double Bonus 10/7 ≈ 100.17%: https://wizardofodds.com/games/video-poker/tables/double-bonus/
- Basic-strategy EV (low pair 0.8237 > single high card ~0.47):
  https://wizardofodds.com/games/video-poker/strategy/jacks-or-better/9-6/optimal/
Note: the exact phrase "RTP realized over millions of hands" is NOT sourced verbatim; article uses
the neutral, universally accepted "дългосрочна статистика над много изиграни ръце".

## Recalculation with working shown (max-coin royal bonus)
Claim in text: royal pays 250/coin at 1–4 coins, but 4000 on 5 coins (=800/coin).
- Linear expectation on 5 coins at the 1–4-coin rate: 250 × 5 = 1,250.
- Actual 5-coin payout: 4,000.
- Bonus factor: 4,000 ÷ 1,250 = 3.2× (per-coin jumps 250 → 800, i.e. ×3.2).
- Every other hand scales exactly ×5 (e.g. full house 9 → 45; flush 6 → 30). Only the royal breaks
  linearity, and ONLY at the 5th coin. Working confirms the article's max-coin advice. ✓
CORRECTION LOG: initial draft mis-stated royal as "800 на 1 монета"; fixed to 250 (1 coin) / 4000
(5 coins) in table + prose at Step-6 verification. All other numbers unchanged across stages.

## External checks
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, credits depleted). gemini=skipped.
- Images (Step 8): 1 infographic (RTP по платежна таблица; numbers verbatim to 05b). AI hero SKIPPED
  (gemini_image_gen.py HTTP 402). Image review SKIPPED (HTTP 402); manual integrity check passed.
  images: 1 (infographic, review skipped — API down)

## Length / style
Body ≈ 1,152 words (guide range 1,000–1,800). 0 em-dashes. Byline Георги Тодоров. Brand „Всички Казина".
4 internal links (/kazino-igri/, /blog/kak-se-igrae-poker-kazino/, /kak-ocenyavame/, /otgovorna-igra/).

# 06 — Verification · vk-0262 · Как се играе онлайн бинго

**Type:** guide (game-type pillar) · **Scope:** guides-only (0 operator T&C, 0 НАП, 0 affiliate link)
**Byline:** Георги Тодоров · **Brand:** Всички Казина

## Brand Gate
PASS — 94/100 (see `05-gate-report.md`). Byline, brand name, RG footer, 18+ markers, affiliate
disclosure footer all present and verbatim.

## Step-7 external Gemini text check (cross-model, human-likeness)
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| initial draft | Likely AI-written, 80% | 20 |
| humaniser pass 1 | Shows AI patterns, 65% | 35 |
| humaniser pass 2 | Likely human-written, 85% | **85 — PASS, KEPT** |

Result: **PASS** at human-likeness 85 (≥80), reached within MAX_GEMINI_PASSES=2. Keep-best = the
pass-2 version (highest HL seen). Trail: `07-gemini-check-1..3.md`. `gemini` column → `human 85`.

## Step-8 images
images: 2 (infographic 100, hero 100) — Gemini image review score **100 PASS**, no integrity failure.
- `images/bingo-nagraden-fond-dyal-na-zalata.svg` — data infographic; every number traces to 05b.
- `images/onlayn-bingo-nagraden-fond-hero.webp` — decorative concept hero, 14.6 KB, textless.
Trail: `08-image-review-1.md`. Both kept at pass 1.

## Surviving flags (stay in the text — human owns resolution)
1. `[VERIFY: конкретният дял такса за участие спрямо награден фонд при онлайн бинго се разминава
   между източниците и зависи от залата; дадените по-долу проценти са примерни, не са данни на
   конкретен оператор.]` — the exact participation-fee / prize-fund split for online bingo is not
   a single published figure; the article resolves this honestly by describing the rake mechanic
   rather than quoting a fixed "RTP", and labels its worked example as примерни. Count: **1 flag.**

## Time-sensitive claims
- Affiliate-licensing footer: "От 1 август 2026 г. … Закон за държавния бюджет за 2026 г. (ДВ, бр.
  69 от 31.07.2026 г.)" — standard brand footer boilerplate; no new operator/licence claim made in
  body. Pub/updated dates 09.10.2026.
- No operator-specific, НАП-register, tax-rate, or affiliate-licence-issued claim in the body
  (guides-scope compliant).

## Figure recalculation (working shown)
- Full room: 100 карти × €1 = €100 продажби. Залата задържа 20% → 100 × 0.20 = €20 задържани →
  наградният фонд = 100 − 20 = **€80**. ✓ (matches 05b)
- Half-empty room: 20 карти × €1 = €20 продажби. 20 × 0.20 = €4 задържани → фонд = 20 − 4 = **€16**. ✓
- Chance ≈ share of cards: 10 от 100 = 10/100 = **1 на 10**. ✓
- Format facts: 90-ball = 27 полета (9×3), 15 числа/билет, 1–90, лента от 6; 75-ball = 5×5 = 25
  полета, 24 числа, 1–75, B-I-N-G-O обхвати 1–15/16–30/31–45/46–60/61–75. ✓ (match brief/sources)

## Numbers integrity across stages
04→05→05b→humaniser×2: number set identical (diffed each humaniser pass; 0 changed/missing).

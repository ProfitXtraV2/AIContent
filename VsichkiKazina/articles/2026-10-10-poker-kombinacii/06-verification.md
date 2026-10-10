# 06 — Verification · vk-0263 · Покер комбинации

**Type:** guide (reference pillar) · **Scope:** guides-only (0 operator T&C, 0 НАП, 0 affiliate)
**Byline:** Георги Тодоров · **Brand:** Всички Казина

## Brand Gate
PASS — 95/100 (see `05-gate-report.md`). Byline, brand name, RG footer, 18+ markers, affiliate
disclosure footer all present and verbatim. 0 criticals.

## Step-7 external Gemini text check (human-likeness)
| version | verdict (verbatim) | human-likeness |
|---|---|---|
| initial draft | Shows AI patterns, 75% | 25 |
| humaniser pass 1 | Shows AI patterns, 75% | 25 |
| humaniser pass 2 | Likely human-written, 90% | **90 — PASS, KEPT** |

Result: **PASS** at human-likeness 90 (≥80), within MAX_GEMINI_PASSES=2. Keep-best = pass-2 version.
Trail: `07-gemini-check-1..3.md`. `gemini` column → `human 90`.
(One pass-3 rec — „домашното предимство → предимството на казиното" — rejected: brand's own native-
vocabulary guide sanctions „домашно предимство"; see 07-gemini-check-3.md.)

## Step-8 images
images: 2 (infographic 100, hero 100) — Gemini image review score **100 PASS**, no integrity failure.
- `images/poker-kombinacii-podredba-na-racete.svg` — hand-ranking ladder; every example card traces to
  05b where stated (royal A♠K♠Q♠J♠10♠; straight flush 6♥7♥8♥9♥10♥; flush K♦9♦7♦4♦2♦; straight
  5♣6♦7♠8♦9♣; каре four queens; фул three kings + two sevens; два чифта two jacks + two fives), and the
  graphic is labelled „примерни карти" for the illustrative rows.
- `images/poker-kombinacii-podredba-hero.webp` — abstract ascending-cards hero (4.0 KB), textless, no
  suit pips (regenerated pass 2 after a suit-hallucination defect at pass 1).
Trail: `08-image-review-1.md` (70, hero defect) → `08-image-review-2.md` (100, fixed).

## Surviving flags
None in-text. No [VERIFY], no [DATA NEEDED].

## Fact sourcing (standard public game rules — no operator T&C / НАП)
- 5-card hand hierarchy (royal flush → … → high card): universal standard; confirmed web 2026-10-10
  (pokernews/wikipedia/BG poker references all agree). Flush outranks straight in 5-card poker
  (5,108 flushes vs 10,200 straights in C(52,5)=2,598,960 — flush is rarer, ranks higher).
- Three-card poker reversal (straight beats flush): standard rule — with 3 cards, straights
  (3,120 ways) are rarer than flushes (1,096 ways), so the straight ranks higher. (Wizard of Odds /
  standard Three Card Poker rules.)
- Ace high or low in straights (10-J-Q-K-A high; A-2-3-4-5 „колело" low).
- Dealer-qualify minimums: Casino Hold'em = pair of fours or better; Caribbean Stud = Ace-King or
  better; Three Card Poker = Queen-high or better. Standard published game rules, not operator T&C.

## Figure / fact recheck (working shown)
- Flush vs straight ordering (5-card): flushes 5,108 < straights 10,200 ⇒ flush ranks above straight. ✓
- 3-card poker: straights 3,120 > flushes 1,096 ⇒ straight ranks above flush (reversal). ✓
- Ladder completeness: 10 distinct ranks, strictly decreasing strength, matches 05b order. ✓

## No maths of the €/превъртане/RTP kind in this piece (card-ranking reference) → none to recalc.

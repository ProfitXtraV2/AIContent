# 06 — VERIFICATION · vk-0189 · Casino Hold'em

STATUS: for human sign-off before publish.
Surviving flags: [VERIFY] 3 · [DATA NEEDED] 0 · [CONFLICT] 0.
1. [VERIFY] Ante-bonus paytable coefficients (100:1 / 20:1 / 10:1 / 3:1 / 2:1 / 1:1) — version-dependent — §„Бонусът към Ante-то".
2. [VERIFY] House edge ≈2,16% on the Ante — paytable-dependent — §„Домашното предимство е около 2,16%".
3. [VERIFY] AA side-bet house edge ≈6% — paytable-dependent — §„Страничният AA залог е скъп".
All three are intentionally left IN the body per house rules (a [VERIFY] does not block publish; human resolves at Step 6).

## External checks (finalized by orchestrator)
- Gemini text check (Step 7): SKIPPED — GEMINI_UNAVAILABLE (HTTP 402, prepayment credits depleted). gemini=skipped.
  Initial draft stands as final 05b. See 07-gemini-check-1.md.
- Images (Step 8): 1 hand-authored SVG infographic (sequence + dealer-qualification outcomes + Ante paytable +
  house edges; numbers verbatim to 05b). AI hero SKIPPED (402). Image review SKIPPED (402); manual integrity PASSED.
  images: 1. See 08-image-review-1.md.

Body word count: 1015 (prose, excluding Title/Meta, image ALT/caption, footer blocks). Within the 1000–1800 guide band.

## SOURCES REACHED (26.09.2026)
- Wizard of Odds — Casino Hold'em: https://wizardofodds.com/games/casino-hold-em/
- Wikipedia — Casino hold 'em: https://en.wikipedia.org/wiki/Casino_hold_%27em
- Wizard of Odds — Ultimate Texas Hold'em (contrast): https://wizardofodds.com/games/ultimate-texas-hold-em/
- Wizard of Odds — Three Card Poker (contrast): https://wizardofodds.com/games/three-card-poker/

## EVERY SPECIFIC FIGURE → SOURCE
| Figure in body | Value | Source / status |
|---|---|---|
| Hole cards each | 2 | WoO |
| Flop community cards | 3 | WoO |
| Call bet size | 2× Ante | WoO |
| Worked example | Ante €10 → Call €20 → €30 in play | derived (10 + 2×10 = 30) |
| Dealer qualifies | двойка четворки (pair of 4s+) | WoO; Wikipedia |
| Ante bonus: Royal flush | 100:1 | WoO Pay Table 3 — [VERIFY] version |
| Ante bonus: Straight flush | 20:1 | WoO — [VERIFY] |
| Ante bonus: Four of a kind | 10:1 | WoO — [VERIFY] |
| Ante bonus: Full house | 3:1 | WoO — [VERIFY] |
| Ante bonus: Flush | 2:1 | WoO — [VERIFY] |
| Ante bonus: Straight or less | 1:1 | WoO — [VERIFY] |
| House edge (Ante) | ≈2,16% | WoO — [VERIFY] version |
| AA side-bet edge | ≈6% | WoO Pay Table 1 = 6,40% — [VERIFY] per table |
| Optimal Call rate | ~82% (fold worst ~18%) | WoO |

## NOT USED (avoid fabrication)
- Element-of-risk ≈0,82%: could NOT be confirmed on WoO for this game → OMITTED, not stated.
- The ~30% fold-rate figure (circulating but contradicted by WoO's raise-82% strategy) → NOT used.
- Exact AA paytable rows: multiple versions in circulation → only the headline ~6% edge stated, [VERIFY]-flagged.

## RECALCULATION (with working)
- Money in play: Ante €10; Call = 2 × €10 = €20; total at showdown = €10 + €20 = €30. ✓ Matches body.
- Dealer non-qualify: Call returned (push), Ante paid per bonus table → confirmed against WoO payout rules. ✓
- Edge context: 2,16% (Ante) < AA ≈6% → "several times more expensive"; 6 / 2,16 ≈ 2,8× → "няколко пъти по-скъп". ✓

## INTERNAL LINKS USED (4, all live in sitemap 26.09.2026)
1. /blog/kak-se-igrae-poker-kazino/ — anchor „една от вариациите на казино покера" (§1) and „Ultimate Texas Hold'em" (§8) [hub/overview]
2. /blog/rechnik-kazino-termini/ — anchor „дефинициите в речника на казино термините" (§6)
3. /otgovorna-igra/ — anchor „инструментите за отговорна игра" (RG)
4. /kak-ocenyavame/ — anchor „публична методика, а не на усещане"

## HUMAN CHECK BEFORE PUBLISH
- CONFIRM the Ante-bonus paytable, the Ante house edge (~2,16%), and the AA side-bet edge (~6%) on the
  specific Casino Hold'em version/table served in BG — resolve the three [VERIFY] flags.
- No operator named, no НАП/tax claim, no affiliate — correct for a game explainer.
- This is the dedicated deep-dive pillar; it links to the casino-poker overview (vk-0008) and does not
  duplicate it, and is distinct from Ultimate Texas Hold'em (vk-0178) and Three Card Poker (vk-0176).
- Fill [About Всички Казина boilerplate] + [author-bio] at publish.

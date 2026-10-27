# 06 — Verification — 2026-10-27-karibski-poker

## Surviving flags
- [VERIFY]: 0
- [DATA NEEDED]: 0
- [CONFLICT]: 0
Nothing blocks publish. No operator facts, no licence №, no tax claim, no affiliate operator link
(the guide recommends no specific operator → none required).

## Time-sensitive / variable claims (sourced; handled in-prose, not as flags)
- Raise pay table (100:1 роял … 1:1 чифт) is the standard U.S. table; the article states explicitly
  „стойностите варират по маси и някои оператори слагат таван", so it is not asserted as universal.
- Progressive side-bet fixed prizes (каре $500, фул $100, флош $50) are labelled „примерни стойности
  при някои американски маси" and „варират по маси" — sources disagree, so they are presented as
  illustrative, not fixed facts. Side-bet edge „често надхвърля 25%" is given as a range, not a point.
- Affiliate-licensing footer (1 август 2026 г., ДВ бр. 69 от 31.07.2026 г.) is verbatim brand canon;
  site licence stated as pending (application filed), never as issued.

## Recalculated figure (working shown)
House edge in euro at €10 ante:
  5,224% × €10 = €0,5224 ≈ 52 цента на ръка спрямо анте. ✓ (matches „около 52 цента")
Bet exposure when playing:
  анте €10 + залог 2× анте (€20) = €30 общо в игра = трикратно анте. ✓
Element of risk 2,555% ≈ „към 2,6% от всичко, което минава през масата". ✓
Average total bet ≈ 2,045 единици анте на ръка. ✓
All figures match the text and both infographics.

## Source trail (all figures)
- https://wizardofodds.com/games/caribbean-stud-poker/ — rules, raise pay table (100:1/50:1/20:1/7:1/
  5:1/4:1/3:1/2:1/1:1), house edge 5,224% of the ante, element of risk 2,555%, average total bet
  2,045 units, simple strategy (raise on a pair+, fold below ace-king; refined 5,225% vs 5,224%).
- https://en.wikipedia.org/wiki/Caribbean_stud_poker — played vs the house, no bluffing, no community
  cards, 5 cards each with one dealer card face up, fold-or-raise (2× ante), dealer qualifies on A-K+,
  non-qualification → ante 1:1 + raise pushes, progressive side-bet payouts (royal = full meter,
  straight flush ~10%, fixed lower prizes vary by location).

## Gemini Step-7 (text, cross-model)
- Baseline (initial draft): "Shows AI patterns 75%" → human-likeness 25.
- Humaniser pass 1: "Shows AI patterns 75%" → human-likeness 25.
- Humaniser pass 2: "Likely human-written 75%" → human-likeness 75 (verdict flipped; +50).
- MAX_GEMINI_PASSES (2) reached. KEEP-BEST = pass 2 (highest, HL 75). Still 5 below the 80 PASS
  threshold → content-queue gemini = `ai 25`. Remaining notes are didactic-signposting / rhythm nits
  for a human editor at Step 6; none touch facts, numbers, links, RG, dates, byline or brand.

## Step-8 images
- images: 3 (hero webp 22 KB + flow infographic SVG + house-edge infographic SVG).
- Gemini image review pass 1: score 100/100 PASS, 0 integrity failures — every infographic number
  traced verbatim to 05b; no operator logos/UI, no people/faces, no glamorised winning; „18+ Играйте
  отговорно" marker on the house-edge infographic. All rendered to PNG and eyeballed (no clip/overlap).
- Images do not block the PR.

## Brand Gate: PASS WITH FIXES 95/100, 0 criticals (05-gate-report.md). Byline Георги Тодоров;
## brand Всички Казина; 0 em-dash; verbatim 18+ RG line; /otgovorna-igra/ + НАП регистър + Солидарност
## 0888 99 18 66; affiliate footer verbatim; 6 approved internal links.

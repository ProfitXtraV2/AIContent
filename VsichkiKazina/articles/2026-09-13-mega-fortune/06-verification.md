# 06-VERIFICATION — Всички Казина · 2026-09-13-mega-fortune
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Mega Fortune: как работи прогресивният джакпот на NetEnt** · type: guide (specific-game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS 93/100 · Gemini Step-7: human 95 (PASS pass 1, initial kept) · images: 2 (infographic 98, hero 82; best 98) · run date: 13.09.2026

## Surviving flags
**0 surviving flags in 05b.** No [VERIFY] / [DATA NEEDED] / [CONFLICT] markers. Specific-game explainer: no BG operator, no licence number, no bonus terms, no affiliate link. Every € figure in the RTP example is ILLUSTRATIVE (marked as such in the infographic caption). Two facts that reachable pages do NOT publish were deliberately NOT stated (so no flag is needed):
- exact per-tier reset seeds — omitted; ~€4 милиона is NetEnt's estimated Mega LEVEL, not a seed.
- a Mega Fortune-specific Mega-tier win probability — omitted; the text points to the concept hub for the general lottery-scale odds framing.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **NetEnt**; release **2009** (23.01.2009) | netent.com/games/mega-fortune | Provider page. |
| Grid **5×3**, **25** fixed paylines | netent.com; bigwinboard; mvideoslots | Web-verified. |
| Overall RTP **96.6%**; max win (excl. jackpot) **1700×** | netent.com (official) | Provider page. |
| RTP split: base **~89%** (base 62.8% / free spins 16.8% / bonus wheel 9.3%) + **7.6%** jackpot contribution = 96.6%; house **3.4%** | fruityslots.com (FAQ) | Third-party breakdown; core of the honest angle. Confirm if a primary NetEnt math sheet is reachable. |
| Volatility **low** | bigwinboard; mvideoslots | NetEnt's „53%" figure is hit frequency, not a volatility rank. |
| Three tiers **Rapid / Major / Mega**; Mega = network/global (~**€4 милиона** estimated) | mvideoslots; netent.com | Web-verified; NetEnt gives ~€4m estimated global jackpot. |
| Bonus wheel: 3 wheel symbols on a line → 3 concentric wheels; arrow = advance inward, coin = cash + end | netent.com; mvideoslots; bigwinboard | Web-verified. |
| Free spins: 3+ champagne scatters → pick a scatter for spins + multiplier | pokernews; netent.com | Web-verified. |
| Record **€17 861 813** on **20.01.2013**, Paf, **€0.25** bet, Guinness record at the time | netent.com record page; megafortunemobile | VERIFIED historical context. Held until Oct 2015. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP headline / base / pool / house | 96.6% / ~89% / 7.6% / 3.4% | provider + fruityslots breakdown |
| Worked example | €1000 оборот → ~€890 base / ~€76 pool / ~€34 house; headline ~€966 = €890 + €76 | illustrative |
| Max win (excl. jackpot) | 1700× bet | provider |
| Mega jackpot level | ~€4 милиона | NetEnt estimate (level, not seed) |

## Recalculation shown (per Step-6 requirement)
- RTP split: 89% + 7.6% = **96.6%** ✓ (matches provider headline). Feature allocation 62.8% + 16.8% + 9.3% = **88.9% ≈ 89%** ✓.
- On €1000 оборот: base 0.89 × €1000 = **€890**; pool 0.076 × €1000 = **€76**; house (1 − 0.966) × €1000 = 0.034 × €1000 = **€34**; headline return 0.966 × €1000 = **€966** = €890 + €76 ✓. Total €890 + €76 + €34 = **€1000** ✓.
- SVG bar (640px, €1000): base 0.89 × 640 = **569.6px**; pool 0.076 × 640 = **48.64px**; house 0.034 × 640 = **21.76px**; sum = **640px** ✓.
- Honesty claim: the 96.6% headline is padded by the 7.6% that is skimmed from players' wagers into a pool almost nobody wins, so the return experienced in normal play is ~89%. The pool is player-funded; the Mega tier is lottery-scale; spins are independent. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text „Преди да завъртиш" + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/blog/progresivni-dzhakpoti/, /blog/games-providers/, /slot-igri/, /otgovorna-igra/), 4 distinct, in-context. Concept hub referenced (not duplicated). ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. title/meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; the record framed as historical context + immediately balanced by the odds reality; RTP as long-run statistic. ✓ Specific-game explainer, not an operator review → no affiliate link, no НАП licence №, no „Протокол на тегленето". ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **95** („Highly likely human-written, 95% confidence", PASS on pass 1). Kept the initial draft (no Humaniser pass; HL 95 is already very high and a pass risks lowering it — keep-best keeps the highest). content-queue gemini = `human 95`. Gemini praised the native BG syntax („Паднеш ли на стрелка…"), the grounded/cynical tone, and the clear RTP maths; offered 3 optional style nits (internal-link phrasing, the „уловка" hook, one balanced sentence) that do not threaten the gate or score. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images (gemini-3.1-pro-preview review):
- `images/mega-fortune-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.6% / 89% / 7.6% / 3.4% / €1000 / €890 / €76 / €34 / €966); 18+/RG note. Pass 1 **72** (corner-bleed), fixed with a clipPath → pass 2 **98** PASS. Data accuracy „безупречна".
- `images/mega-fortune-hero.webp` — decorative network-progressive-pool AI hero (gemini-3-pro-image, 44.9 KB); coin/chip streams converging into a central glowing wheel; no fabricated UI/logos/numbers/people/winning. **82** PASS on pass 1. 08-image-review-1.md / -2.md persist.
- Best image-review score **98**. No integrity failures.

## Anti-cannibalization note (Step-6 human check)
Specific-game pillar (branded „mega fortune" intent), distinct from the general progressive-jackpots concept hub (/blog/progresivni-dzhakpoti/). The hub is referenced twice for the general pool mechanics and the lottery-scale odds rather than duplicated; this piece stays on Mega Fortune specifics (tiers, wheel, RTP split, 2013 record). NetEnt anchored via /blog/games-providers/. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. (Optional) Confirm the RTP breakdown (base ~89% + 7.6% jackpot = 96.6%) against a primary NetEnt math sheet if one becomes reachable; the third-party breakdown (fruityslots) is the current source.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

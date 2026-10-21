# 06-VERIFICATION — Всички Казина · 2026-09-12-hold-and-win
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Hold & Win (Hold and Spin): как работят респините с монети и джакпоти** · type: guide ·
byline: editorial voice (signed Георги Тодоров) · gate: PASS WITH FIXES 95/100 · Gemini Step-7:
human 80 (PASS, kept pass 2) · images: 2 (infographic 100, hero 100) · body ~902 words · run date: 12.09.2026

## Surviving flags
**0 [VERIFY] / [CONFLICT] / [DATA NEEDED].** Evergreen game-mechanic explainer. No BG operator T&C,
no НАП licence number, no tax claim, no live jackpot amount. Every € / multiplier in the text is
explicitly ПРИМЕРНИ (illustrative), so nothing points at a primary source that could drift.

## Sources for the mechanic (public, reachable — verified 12.09.2026)
| Claim in text | Source |
|---|---|
| Монети/кеш символи (често 5–6) заключват рунда; 3 респина, нулиране на 3 при нова монета | BGaming „Hold & Win mechanics explained"; VegasSlotsOnline „Hold and Spin" feature guide |
| Монетите носят фиксиран кеш ИЛИ джакпот тир (Мини/Минор/Мейджър/Гранд; или Мини/Мейджър/Мега) | BGaming; VegasSlotsOnline |
| Пълна решетка = горен джакпот; всички стойности се сумират в едно плащане | BGaming; VegasSlotsOnline (Wolf Gold: 6+ moons, 3 respins reset, 15 positions, top jackpot) |
| Джакпотите почти винаги ФИКСИРАНИ (кратни на залога, вградени в RTP), не мрежови прогресивни | BGaming; 1spin4win; GameTyrant „progressive vs fixed" |
| При фиксиран нищо не се отклонява в пул → базов RTP обикновено по-висок от прогресивна | GameTyrant; SportsLine (fixed vs progressive RTP) |
| Wolf Gold използва механиката под името „Money Respin"; RTP 96.00%, 5×3=15 | VegasSlotsOnline Wolf Gold review; PokerNews |
| The Dog House = лепкави wild-ове (НЕ hold-and-win) — контраст | repo model article 2026-09-10-the-dog-house (Pragmatic sticky-wild mechanic) |
| Playson популяризира брандираната серия „Hold and Win" | Playson.com; Yogonet/NEXT.io studio coverage |

Wolf Gold and The Dog House are named in PLAIN TEXT only (no link — not yet live). No specific
unverified jackpot multiples of any real game are cited; the jackpot ladder in text/graphic is
generic and marked примерни.

## Illustrative numbers used (all hypothetical, none sourced to a specific game)
| Where | Figure | Note |
|---|---|---|
| Респини | обикновено 3, нулиране на 3 при нова монета | genre-standard, source-backed as typical |
| Монети стойности | 1x / 2x / 5x кеш (пример) | illustrative |
| Джакпот стълбица | Мини 20x, Минор 50x, Мейджър 500x, Гранд 2000x | explicitly „Например"/„примерни" |
| Worked sum | 5x + 2x + 500x = 507x залога | illustrative |
| Решетка | пример 5×3 = 15 позиции | illustrative generic grid |

## Recalculation shown (per Step-6 requirement)
- Combined coin payout: 5x + 2x + 500x = **507x** залога. ✓ matches text „тоест 507x залога".
- Grid size: 5 колони × 3 реда = **15** позиции. ✓ matches text and the SVG infographic.
- RTP framed as a long-run statistic over millions of spins, never a session promise. ✓
- Independence of spins stated („всяко завъртане е независимо", „не е по-вероятно да падне"). ✓
- „По-голямото число не подобрява шанса ти" and „механиката не пипа домашното предимство" stated. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker line „18+ Хазартът може да пристрасти. Играйте отговорно." — inline (§7) + footer. ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност
  0888 99 18 66 (делнични 10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO
  invented site licence number. ✓
- Byline Георги Тодоров ✓ · brand „Всички Казина" exact ✓ · dates 12.09.2026 (pub + updated) ✓
- Internal links (4, all confirmed-LIVE): /blog/progresivni-dzhakpoti/, /blog/rechnik-kazino-termini/,
  /slot-igri/, /otgovorna-igra/. ✓
- Zero em-dashes in body. ✓ No operator names linked, no fake UI, no promise/hype/FOMO, no tax
  figures, no sports. „хазартът не е финансова стратегия" doctrine present (§7 „декор, не план"). ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by pass: **25 → 25 → 80**.
- Check 1 (as-delivered 05b): „Shows AI patterns 75%" → hl 25 (flagged repeated „(пример)" hedging,
  poetic wrap-up, summary pivot, strawman transition, rigid „Или…Или…").
- Humaniser pass 1 → Check 2: „Shows AI patterns 75%" → hl 25 (noisy detector, new nitpicks).
- Humaniser pass 2 → Check 3: **„Likely human-written, 80%" → hl 80 → PASS.**
KEPT pass 2 (highest hl seen). All numbers, 4 links, RG/18+, disclosures, dates, byline, brand
UNTOUCHED across passes; illustrative figures stayed MARKED via natural language (brand rule).

## Images (Step 8)
**2 images. Best review scores: infographic 100, hero 100.**
- SVG infographic `hold-and-win-respin-flow.svg`: lock→respin→fill flow + примерна fixed jackpot
  ladder; every number traces to 05b (3 респина, 5×3=15, 20x/50x/500x/2000x), marked примерни;
  18+ footer; layout verified (rendered to PNG, no overlap/clip). Reviews: 92 (as part of pass 1
  set) then 100 — flawless both times.
- Hero WebP `hold-and-win-moneti-zakljuchvane-hero.webp`: decorative metaphor (coins locking with
  padlocks into a grid, respin arrows, fixed-prize disc). Review 1 flagged a real ETH crypto logo
  on the coins (brand-mark hygiene) → regenerated with blank coins (fix pass 1) → Review 2 = 100.
  **No integrity drop** (the fabricated/brand mark was removed, not shipped).

## Anti-cannibalization note (Step-6 human check)
No sitemap page exists for this mechanic — clean pillar for „Hold & Win / Hold and Spin / lock and
respin / респин механика / монети джакпот". Distinct from `/blog/progresivni-dzhakpoti/`: that pillar
explains PROGRESSIVE pools (a growing network/local pool funded by a share of each bet); this one
explains the lock-and-respin GAME mechanic with FIXED coin jackpots. They contrast and cross-link,
they do not compete. Branded Hold & Win slots (Wolf Gold etc.) would link UP into this hub.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

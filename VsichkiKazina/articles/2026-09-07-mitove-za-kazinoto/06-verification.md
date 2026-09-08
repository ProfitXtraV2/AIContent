# 06-VERIFICATION — Всички Казина · 2026-09-07-mitove-za-kazinoto
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Митове за казиното: какво наистина можете да очаквате от печалбите** · type: guide (myth-busting / RG-aligned) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 92/100 · humanisation: HUMAN-LIKE 52/60 · Gemini Step-7: human 85 (PASS) · run date: 07.09.2026

## Surviving flags
**0.** No [VERIFY], [CONFLICT], or [DATA NEEDED] flags. Evergreen concept/myth-busting guide; no claim
about any real operator, game, licence number, or tax. Every € figure is ILLUSTRATIVE. The one dated
historical reference (Монте Карло 1913) is a well-documented public statistics anecdote, not an
operator/time-sensitive claim.

## Time-sensitive claims needing a primary-source check
**None.** No operator terms, no live offers, no НАП licence numbers, no tax thresholds. Dated strings
are the run date 07.09.2026, the historical "1913" anecdote, and the verbatim affiliate footer citation.

## Illustrative / standard numbers used (none operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RNG независимост | завъртане 301 = завъртане 1 по вероятност | standard RNG fact |
| Монте Карло 1913 | черно 26 пъти подред; ~50/50 всяко завъртане | documented public anecdote |
| Мартингейл | €1→€2→€4→€8; таван €500; 10 загуби → €1 024 за 11-ия залог | illustrative |
| Expected-loss формула | среден залог €2 × 500 залога = €1 000; при 4% → ~€40 | illustrative |
| RTP | 96% → домашно предимство 4%; €1 000 → ~€40 | illustrative |
| Бонус | €100 + €100, превъртане 35x върху депозит+бонус = €7 000 оборот; при 4% → ~€280 | illustrative; base stated |
| Стратегия | блекджек с базова стратегия < 1%; европейска рулетка ~2,7% | standard, computable |

## Recalculation shown (per Step-6 requirement)
- Martingale wall: base €1 doubling 10 losses → 11th stake = 2^10 × €1 = €1 024 > €500 table cap. ✓
- Expected loss: €2 avg stake × 500 bets = €1 000 turnover; 4% × €1 000 = **€40**. ✓ matches text.
- RTP: 100% − 96% = 4% edge; 4% × €1 000 = **€40**. ✓
- Bonus: €100 + €100 = €200; 35 × €200 = **€7 000** wagering (base: депозит+бонус, explicitly
  stated); 4% × €7 000 = **€280** expected cost. ✓ matches text; превъртане base stated. ✓
- Strategy: blackjack basic strategy долгосрочно < 1%; European roulette single-zero ~2.7% flat —
  reduces but never reverses the edge (stated). ✓
- Core doctrine: short-run wins possible via variance; edge asserts with volume; „хазартът не е
  финансова стратегия". ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker line "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline RG touch + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност
  0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented number. ✓
- Internal links: only the approved set (/kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/), 3 distinct. ✓
- Zero em-dashes (incl. meta). ✓ No operator names, no promise/hype words (this is a myth-busting
  piece: the „как да спечелим" intent is answered honestly, no winning system implied), no FOMO, no
  tax figures. ✓ Card counting explicitly stated NOT a viable online winning system. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Pass 1 (as-delivered 05b): "Shows strong AI patterns 85%" → hl 15
(flagged "не X, а Y" antitheses, „има име:"/„две стени" signposts, narrated evaluations, the
"honest answer" hook). Humaniser pass 1 → pass 2 check "Likely AI-written 80%" → hl 20. Humaniser
pass 2 (fix two translated idioms, combine antithesis pairs, delete pop-psychology + meta-commentary,
cut circular RTP restatements) → pass 3: **"Likely human-written, 85%"** → hl 85 → **PASS**.
MAX_GEMINI_PASSES=2 reached; kept pass 2 (highest). All numbers, links, RG lines, 18+, dates, byline,
brand and the превъртане base UNTOUCHED across passes.

## Anti-cannibalization note (Step-6 human check)
No "myths" page exists on the live site — this takes the open niche for „как да спечелим от казино"
reframed as reality/myth-busting. /otgovorna-igra/ (RG tools) is a distinct page, linked not
duplicated. The RTP-as-myth section overlaps intentionally-lightly with the standalone RTP guide
(vk-0006); it stays a single myth here and points there conceptually (not linked — same approved-set
discipline).

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

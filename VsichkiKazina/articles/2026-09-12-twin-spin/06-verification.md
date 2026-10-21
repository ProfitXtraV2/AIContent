# 06-VERIFICATION — Всички Казина · 2026-09-12-twin-spin
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Twin Spin: RTP, свързани барабани и как се играе** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 95/100 · humanisation: Gemini Step-7 human 85 (PASS on pass 1, 0 Humaniser passes applied, initial kept) · images: 3 (infographic 100, infographic 100, hero 100) · run date: 12.09.2026

## Surviving flags
**0 in-text [VERIFY] flags.** Game explainer on public provider/game-DB data; no BG operator, no licence №, no bonus terms. Every specific figure verified from a reachable page (below). Ahrefs units exhausted (reset 2026-10-02) → vol/kd web-estimated, not fabricated.

## Time-sensitive / game claims to confirm at publish
| Claim | Source (fetched 12.09.2026) | Note |
|---|---|---|
| NetEnt; released **21.12.2013** (2013) | netent.com/games/twin-spin; slotcatalog.com | Official + DB. |
| **5x3**, **243 начина**, плащат **отляво надясно**; неонова Vegas тема | netent.com/games/twin-spin; pokernews.com | Primary + review. SlotCatalog tags "bothway" — rejected (primary + PokerNews: "wins pay left to right across all 243 ways"). |
| **RTP 96.55%** (official NetEnt) | netent.com/games/twin-spin | Primary. PokerNews rounds 96.6%; SlotCatalog 96.56%. Used official 96.55%. Confirm operator's build at publish. |
| RTP **конфигурируем** (SlotCatalog изброява напр. 94.04%) | slotcatalog.com/en/slots/Twin-Spin | Supports "check real RTP in info panel" angle. |
| **Волатилност: ниска до средна** | pokernews.com ("medium"); slotcatalog.com ("med-high"); web aggregate ("low-to-medium") | Sources vary; presented honestly as "ниска до средна" with the modest ceiling as the concrete anchor. |
| **Залог €0.25 – €125.00** | netent.com/games/twin-spin; pokernews.com | Primary + review. |
| **Twin Reel**: всяко завъртане ≥2 свързани идентични барабана → 3, 4 или всичките 5 | netent.com ("twin, triplet, quadruplet or even a quintuplet"); pokernews.com; slotcatalog.com | Confirmed across 3 pages. |
| **Обикновен wild**; **БЕЗ** фрий спинове, **БЕЗ** бонус игра, **БЕЗ** скатери | pokernews.com ("no dedicated free spins feature", "no bonus round", "no scatter symbols") | Core simplicity angle. |
| **Максимална печалба**: NetEnt поле "Max Win" **1 000х**; game DBs **1 080х** (= **270 000** монети) | netent.com; slotcatalog.com; pokernews.com | See note below — presented honestly in-text, not flagged. |

## Max-win discrepancy (handled honestly in-text, NOT a [CONFLICT] for the human)
NetEnt's own "Max Win" spec field lists **1 000х**, while international game DBs cite **1 080х** (= **270 000** монети). These are different spec fields/measures, not a Version A/B fact conflict. The article states both and stresses the ceiling is modest vs high-volatility slots (the brand's honest angle: "банерът е реклама"). Confirm at publish if desired.

## Illustrative numbers used (labelled примерно)
| Where | Figure | Note |
|---|---|---|
| RTP/edge worked example | €1000 → ~€965.50 / ~€34.50 | illustrative, labelled „Пример"/„илюстративен" |
| House edge | ~3.45% | direct complement of official 96.55% (100−96.55); €34.50/€1000 |
| SVG house bar | 3.45% = 17px of 500px (player 483 + house 17, clipPath) | math checked |

## Recalculation shown
- RTP 96.55% on €1000: 0.9655 × €1000 = **€965.50** (играч); house 0.0345 × €1000 = **€34.50 (3.45%)**. ✓ (illustrative).
- House edge check: 100 − 96.55 = **3.45%**; €34.50 / €1000 = 3.45%. Internally consistent. ✓
- SVG player/house bar: 0.9655 × 500 = **482.75 ≈ 483 px** player; 0.0345 × 500 = **17.25 ≈ 17 px** house (483 + 17 = 500, single clipped track, no seam). ✓
- Honesty claims: свързаните барабани вдигат шанса за съвпадения, не променят домашното предимство/RTP; базовата игра е цялата игра (no bonus/free spins/scatters); таван 1 000х/1 080х скромен. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — body + footer. ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 / ДВ бр. 69), pending-application, NO issued claim, NO invented №. ✓
- Internal links (approved set, 5): /kak-ocenyavame/, /slot-igri/, /blog/netent-provajdar/, /blog/games-providers/, /otgovorna-igra/. NetEnt hub linked per confirmed sibling pattern (Dead or Alive 2 → /blog/netent-provajdar/). Starburst + Dead or Alive 2 named in plain text, NOT linked (siblings do not cross-link individual slots). ✓
- Byline Георги Тодоров; brand „Всички Казина". ✓ Zero em-dashes in article. En-dash only footer „10:00–17:00". ✓ Game explainer → no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial draft **85** ("Likely human-written, 85% confidence") → **PASS** (≥80) on pass 1. **0 Humaniser passes applied**; initial 05b kept (keep-best). content-queue gemini = `human 85`. 07-gemini-check-1.md persists. Residual style recs at 85 (calque „живототпроменящ", thesis opener, recycled „без/няма" list) NOT applied — PASS reached on pass 1 and keep-best forbids risking a lower score; Step-6 human may polish if desired. Untouchables (numbers/links/RG/18+/disclosure/date/byline/brand) intact.

## Images (Step 8)
3 images, all PASS pass 1 (review 100, no integrity failure, no layout defect):
- `images/twin-spin-rtp.svg` — RTP infographic (96.55%; €1000 → ~€965.50/~€34.50; ~3.45%); figures trace to 05b; clipPath track; 18+/RG note.
- `images/twin-reel-mehanika.svg` — Twin Reel mechanic (2→3→4→5 свързани барабана; „не променят домашното предимство"; „без фрий спинове, без бонус игра"); figures trace to 05b; 18+/RG note.
- `images/twin-spin-hero.webp` — decorative mirrored/twin-symmetry gem AI hero (gemini-3-pro-image, 11.2 KB); no UI/logos/numbers/people/winning. 08-image-review-1.md persists.

## Anti-cannibalization note
No Twin Spin page in the sitemap (checked 12.09.2026). Distinct branded kw „twin spin" / „туин спин". Distinct from Gonzo's Quest (Avalanche/cascades, средна вол.) and Dead or Alive 2 (екстремна вол., 3 режима фрий спинове): Twin Spin has NO free spins / NO bonus, modest ceiling — the hook is the Twin Reel mechanic + simplicity. Near Starburst by temperament (ниска-средна вол., base game only) but different mechanic; Starburst named in plain text only. NetEnt profile linked (in sitemap). Game explainer → no affiliate link; no operator/licence № invented.

## Human-action list (Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the operator's RTP version at publish (NetEnt ships configurable builds; SlotCatalog lists lower variants).
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: apply Gemini's pass-1 style recs (calque „живототпроменящ" → „за огромна печалба"; soften thesis opener) — left as-is in the 85-scoring version (keep-best).

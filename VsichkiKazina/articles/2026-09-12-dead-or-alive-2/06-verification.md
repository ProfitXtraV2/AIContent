# 06-VERIFICATION — Всички Казина · 2026-09-12-dead-or-alive-2
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Dead or Alive 2: RTP, висока волатилност и как се играе** · type: guide (game explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 95/100 · humanisation: Gemini Step-7 human 85 (PASS, pass 2, 2 Humaniser passes applied, initial NOT kept) · images: 3 (infographic 100, infographic 100, hero 100) · run date: 12.09.2026

## Surviving flags
**0 in-text [VERIFY] flags.** Game explainer on public provider/game-DB data; no BG operator, no licence №, no bonus terms. Every specific figure verified from a reachable page (below). Ahrefs units exhausted (reset 2026-10-02) → vol/kd web-estimated, not fabricated.

## Time-sensitive / game claims to confirm at publish
| Claim | Source (fetched 12.09.2026) | Note |
|---|---|---|
| NetEnt; released **23.04.2019** (продължение на Dead or Alive, 2009) | netent.com/games/dead-or-alive-2; slotcatalog.com | Official + DB. |
| **5x3**, **9 фиксирани линии**; уестърн тема | netent.com/games/dead-or-alive-2; slotcatalog.com | Official + DB. |
| **RTP 96.80%** (official NetEnt) | netent.com/games/dead-or-alive-2 | Primary. slotcatalog cites 96.82%; used official 96.80%. Confirm operator's build at publish. |
| RTP split **68.6% основна игра + 28.2% фрий спинове** (= 96.8%) | askgamblers.com/.../dead-or-alive-2-netent | Game-DB. Internally consistent. |
| **Волатилност: екстремно висока** | askgamblers.com ("extremely volatile"); slotcatalog.com ("High") | Web-verified; core honest angle. |
| **Залог €0.09 – €9.00**; скатер до **2 500х** | netent.com/games/dead-or-alive-2 | Primary. |
| **3 режима** (3 скатера → всеки **12 завъртания**): Old Saloon **2x** sticky; High Noon **2x/3x** sticky; Train Heist множител **до 16x** (+1 на wild) | netent.com; slotcatalog.com; askgamblers.com | Confirmed across 3 pages. |
| **Максимална печалба ~100 000х** (askgamblers/slotcatalog: **111 111х**), само в Train Heist; NetEnt поле „Max Win" изписва **1 600х** | netent.com; askgamblers.com; slotcatalog.com | See note below — presented honestly in-text, not flagged. |

## Max-win discrepancy (handled honestly in-text, NOT a [CONFLICT] for the human)
NetEnt's structured "Max Win" spec field lists **1 600х**, while the theoretical ceiling in the Train Heist feature is cited **~100 000х** (NetEnt's own free-spins text) / **111 111х** (askgamblers, slotcatalog). These measure different things (a modest spec field vs the feature's theoretical ceiling), so it is NOT a Version A/B conflict. The article states both and stresses the ceiling is astronomically rare — this IS the brand's honest angle ("банерът е реклама"). Confirm at publish if desired.

## Illustrative numbers used (labelled примерно)
| Where | Figure | Note |
|---|---|---|
| RTP/edge worked example | €1000 → ~€968 / ~€32 | illustrative, labelled „Пример"/„илюстративен" |
| House edge | ~3.2% | direct complement of official 96.80% (100−96.80); €32/€1000 |
| SVG house bar | 3.2% = 16px of 500px (player 484 + house 16, clipPath) | math checked |

## Recalculation shown
- RTP 96.80% on €1000: 0.9680 × €1000 = **€968** (играч); house 0.0320 × €1000 = **€32 (3.2%)**. ✓ (illustrative).
- RTP split check: 68.6% + 28.2% = **96.8%** = обявеният RTP 96.80%. ✓
- SVG player/house bar: 0.9680 × 500 = **484 px** player; 0.0320 × 500 = **16 px** house (484 + 16 = 500, single clipped track, no seam). ✓
- Honesty claims: основната игра сама връща ~68.6%; екстремна вол. = дълги сухи серии + повечето сесии на загуба; таван 100 000х само в Train Heist, астрономически рядко; NetEnt поле 1 600х. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — body + footer. ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 / ДВ бр. 69), pending-application, NO issued claim, NO invented №. ✓
- Internal links (approved set, 5): /kak-ocenyavame/, /slot-igri/, /blog/netent-provajdar/, /blog/games-providers/, /otgovorna-igra/. NetEnt hub linked per confirmed sibling pattern (book-of-dead → /blog/playn-go-provajdar/). Starburst + Gonzo's Quest named in plain text, NOT linked (siblings do not cross-link individual slots). ✓
- Byline Георги Тодоров; brand „Всички Казина". ✓ Zero em-dashes in article. En-dash only footer „10:00–17:00". ✓ Game explainer → no affiliate link. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness progression: initial **70** → Humaniser pass 1 **75** → Humaniser pass 2 **85** → **PASS** (≥80). 2 Humaniser passes applied (cap = 2); highest-HL version (pass 2, 85) KEPT (it is the checked-out 05b). content-queue gemini = `human 85`. 07-gemini-check-1/2/3.md persist. Residual style recs at 85 not applied (cap reached + PASS; keep-best forbids risking a lower score). "менуш" (should be "меняш") left in the 85-scoring version; Step-6 human may correct.

## Images (Step 8)
3 images, all PASS pass 1 (review 100, no integrity failure, no layout defect):
- `images/dead-or-alive-2-rtp.svg` — RTP infographic (96.80%; 68.6%/28.2% split; €1000 → ~€968/~€32); figures trace to 05b; clipPath track; 18+/RG note.
- `images/dead-or-alive-2-frii-spinove-rezhimi.svg` — 3-mode comparison (12 завъртания each; Old Saloon 2x, High Noon 2x/3x, Train Heist до 16x, таван 100 000х); figures trace to 05b; 18+/RG note.
- `images/dead-or-alive-2-hero.webp` — decorative wild-west desert/canyon dusk AI hero (gemini-3-pro-image, 10.3 KB); no UI/logos/numbers/people/winning. 08-image-review-1.md persists.

## Anti-cannibalization note
No Dead or Alive 2 page in the sitemap (checked 12.09.2026). Distinct branded kw „dead or alive 2". Distinct from Gonzo's Quest (vk-0044): sticky wilds + екстремна вол. vs Avalanche/cascades + средна вол. Distinct from Starburst: екстремна вол. + фрий спинове vs ниска вол. + wild+respin. NetEnt profile linked (in sitemap); Starburst + Gonzo's Quest plain text only. Game explainer → no affiliate link; no operator/licence № invented.

## Human-action list (Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm the operator's RTP version at publish (NetEnt ships configurable builds).
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
4. Optional: correct the colloquial "менуш" → "меняш" (left as-is in the 85-scoring Gemini version).

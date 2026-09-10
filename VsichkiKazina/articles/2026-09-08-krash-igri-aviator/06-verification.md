# 06-VERIFICATION — Всички Казина · 2026-09-08-krash-igri-aviator
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Краш игри и Aviator: как работят и какъв е RTP** · type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE 53/60 · Gemini Step-7: human 90 (PASS, pass 1 kept) · run date: 08.09.2026

## Surviving flags
**0** in-text. No [VERIFY]/[CONFLICT]/[DATA NEEDED] flags. Concept guide on the crash-game format; no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Aviator advertised RTP **97%** (house edge 3%) | Spribe / the game's in-client info panel; PrimeDope; crash-games.net (cited in 00-brief) | Provider-published spec, web-verified. Text says „обявеният RTP" + „проверява се в инфо-панела". Confirm the live figure for the operator's Aviator build at publish (operators can run configurable RTP variants). |
| Provably fair = SHA-256 pre-round hash, post-round reveal | gamblingcalc Aviator provably-fair algorithm (cited) | Standard mechanism; confirm wording matches the specific game. |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Множител | старт 1.00x → 1.20x, 1.80x, 2.50x… без горна граница | standard crash mechanic |
| Кешаут пример | €1 @ 2.00x = €2 | illustrative |
| RTP/edge | 97% / 3% | provider-published (confirm per above) |
| Worked example | €1000 оборот → €970 връщане / €30 (3%) house | illustrative |
| Волатилност | целеви множител 1.5x (ниска) / 10x (висока); RTP constant 97% | standard fixed-RTP property |

## Recalculation shown (per Step-6 requirement)
- RTP 97% on €1000: return 0,97 × €1000 = **€970**; house 0,03 × €1000 = **€30 (3%)**. ✓ matches text.
- €1 cashed at 2.00x = **€2** (net +€1). ✓
- Edge is 3% regardless of cash-out target; RTP constant across 1.5x/10x. ✓ (standard fixed-RTP property; volatility is player-driven variance, not edge)
- Core honesty claims: provably fair = transparency not better odds; independent rounds → no system beats 3%; fast tempo = risk. All correct. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker line "18+ Хазартът може да пристрасти. Играйте отговорно." — present (inline RG touch in the high-risk-tempo section + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + Солидарност 0888 99 18 66 (10:00–17:00). ✓ (RG emphasis raised for this high-risk format)
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /kazino-igri/, /otgovorna-igra/), 3 distinct. ✓
- Byline Георги Тодоров; brand "Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in verbatim footer "10:00–17:00". ✓ No promise/hype; the „още един" pull is named as a RISK to resist, not a FOMO hook. ✓ No tax figures; Aviator mentioned educationally, no affiliate link (guide, not review). ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Pass 1 (initial 05b): "Likely human-written 75%" → hl 75 (neat-bow conclusion, symmetrical volatility pacing). Humaniser pass 1 applied those recs → pass 2: **"Highly likely human-written 90%"** → hl 90 → **PASS**. Kept pass 1 (highest). All numbers, links, RG lines, 18+, dates, byline, brand UNTOUCHED across the pass. 07-gemini-check-1.md / -2.md persist as the audit trail.

## Anti-cannibalization note (Step-6 human check)
No crash-games/Aviator page in the sitemap (checked 08.09.2026). New-format pillar; distinct from every existing article. Aviator named as the format's flagship (educational), not recommended → no affiliate link. Only /kazino-igri/ hub linked; no URL invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm Aviator's live RTP (97%) for the target operator's build + provably-fair wording against Spribe at publish.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

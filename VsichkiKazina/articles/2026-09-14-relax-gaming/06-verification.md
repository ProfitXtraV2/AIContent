# 06-VERIFICATION — Всички Казина · 2026-09-14-relax-gaming (vk-0068)
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Relax Gaming: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: Gemini Step-7 human 85 (HL 20 → 25 → 85, kept pass 2, PASS) · images: 2 (infographic + hero; review 82 PASS, best 82) · body ~885 words · run date: 14.09.2026

## Surviving flags (both [VERIFY] — STAY in 05b)
**1** [VERIFY] „точните числа за студия и оператори варират по източник" (Section 1 — Silver Bullet / Powered By scale). Sources disagree: relax-gaming.com/partner pages and industry write-ups quote different counts („50+ студия / 250+ оператори" vs „7 000+ игри / 900+ оператори"), and these change over time. Text hedges to „десетки студия … стотици оператори"; confirm the current figure at publish or keep the hedge.
**2** [VERIFY] „точният актуален списък с лицензи към датата на публикуване" (Section 5). UKGC + MGA are stated and current; the full list („сред други регулатори") is not enumerated. Confirm the live list at publish.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Founded **2010** by Patrik Österåker & Jani Tekoniemi | relax-gaming.com/about; iGaming Express; CB Insights | Web-verified 14.09.2026. |
| HQ **Malta**; studios/offices Sweden (Malmö/Stockholm), Estonia (Tallinn), Serbia (Belgrade/Novi Sad), Gibraltar | relax-gaming.com/about | Web-verified. |
| Owner **Kindred Group**, acquisition completed **1 October 2021** | Kindred press release; Gaming Intelligence; PRNewswire; European Gaming | Web-verified. Kindred held 33.4%, bought the remaining 66.6%; deal valued Relax up to €320m. **NB: original brief guessed „Kambi" — that is WRONG; verified owner is Kindred.** (Kindred was itself acquired by FDJ United in 2024 — deliberately left out of the copy to avoid over-claim; verify separately if the site wants current ultimate parent.) |
| **Dream Drop** launched **March 2022**; 5 tiers Rapid/Midi/Maxi/Major/Mega; must-hit; Mega up to **€10 000 000**; 20+ Mega winners | relax-gaming.com/products/dream-drop; iGamingBusiness; Gaming Intelligence | Web-verified. First game Temple Tumble 2 (May 2022). |
| **Money Train 2** (2020): max win **50 000x**, RTP **96.40%**, high volatility | bigwinboard; clashofslots; SlotsWise; relax-gaming.com | Web-verified. RTP is the base build; operators may ship other builds → per-casino check. |
| **Money Train 3** (2022): max win **100 000x**, RTP **96.10%** | relax-gaming.com/products/casino/moneytrain3; clashofslots; fruityslots | Web-verified. |
| **Money Train 4** (2023): max win **150 000x** | relax-gaming.com/products/casino/moneytrain4; aboutslots | Web-verified. RTP not stated in article (avoid unsourced precision). |
| Original **Money Train** released **2019** | SlotsWise; bigwinboard | Web-verified. |
| **Feature buy / Bonus Buy** on the Money Train line (e.g. 100x / 500x stake) | bigwinboard; relax-gaming product pages | Web-verified as a range; buying the bonus does not change the game's maths (standard fact). |
| Licences: **UKGC** (GB #37462), **MGA**, + Gibraltar/Romania/Canada/eCOGRA | relax-gaming.com/about; UKGC public register | UKGC + MGA stated in copy; full list [VERIFY] at publish. |

## Illustrative / interpretive framing (nothing BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Max-win caps | 50 000x / 100 000x / 150 000x | Theoretical maxima at near-impossible symbol alignment, stated as such in copy + infographic — not expected values. |
| RTP variance | „една и съща игра може да ти връща различно в различни казина" | Standard fact: many titles ship in multiple RTP builds; operator chooses → check the info panel. |

## Recalculation shown (per Step-6 requirement)
Infographic bar widths (max-win caps scaled to a 380 px track, MT4 = 150 000x = full):
- MT2: 50 000 / 150 000 × 380 = 0.3333 × 380 = **126.7 ≈ 127 px** ✓ (SVG uses 127)
- MT3: 100 000 / 150 000 × 380 = 0.6667 × 380 = **253.3 ≈ 253 px** ✓ (SVG uses 253)
- MT4: 150 000 / 150 000 × 380 = **380 px** ✓ (SVG uses 380)
Honesty logic checks: certification proves fairness-to-rules, not player edge ✓; house edge stays built in ✓; Dream Drop pool funded from turnover, tiny odds, does not lower house edge ✓; feature buy pays in advance for on-average the same, faster ✓; popularity does not change a title's RTP/volatility ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text close + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /blog/games-providers/, /otgovorna-igra/), 4 distinct, in context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓
- No promise/hype words; certification, progressive and feature buy framed as mechanics, not hooks. ✓
- Provider profile → no affiliate link, no НАП licence № (correct — not an operator review). ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **20** („Shows AI patterns 80%"); humaniser pass 1 **25** („Shows AI patterns 75%"); humaniser pass 2 **85** („Likely human-written 85%", PASS). Per keep-best, kept **pass 2** (highest HL). content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across every pass. 07-gemini-check-1/-3.md persist as the audit trail.

## Images (Step 8)
2 images:
- `images/money-train-serija-tavani.svg` — hand-authored infographic; every figure traces to 05b (50 000x / 96.40% / 100 000x / 96.10% / 150 000x); RTP-in-info-panel caveat; 18+ note. Gemini review **82/100 PASS** pass 1, no layout defect.
- `images/relax-gaming-hero.webp` — decorative flat-vector hero (gemini-3-pro-image, 23 KB): a train on a looping track with one rare towering peak = high volatility. No fabricated UI/logos/numbers/people/winning. Part of the same 82 PASS review.
08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
7th provider profile after Pragmatic (vk-0019), Amusnet/EGT (vk-0021), Novomatic/Greentube, NetEnt, Play'n GO, Hacksaw. Distinct primary kw „relax gaming" vs the /blog/games-providers/ listing hub (linked prose-only). Anchors a Relax cluster (Money Train 2 sibling queued vk-0069). Siblings mentioned in plain text only — no invented /blog/ slugs. Not an operator review → no affiliate link, no operator/licence № invented.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve [VERIFY] #1: confirm the current Silver Bullet / Powered By studio+operator counts, or keep the „десетки … стотици" hedge.
3. Resolve [VERIFY] #2: confirm the exact live licence list at publish (UKGC + MGA stated; full list open).
4. Optional: decide whether to state the current ultimate parent (Kindred → FDJ United, 2024); left out on purpose.
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

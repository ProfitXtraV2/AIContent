# 06-VERIFICATION — Всички Казина · 2026-09-09-amusnet-egt-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Amusnet (EGT): профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (HL 15 → 75 → 85, kept pass 2, PASS) · images: 2 (infographic 100, hero 82; best 100) · run date: 09.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact founding year of the online arm (EGT Interactive) and the precise corporate relationship to the EGT group are described differently across sources (≈2008–2010 vs ≈2016; subsidiary vs separately-owned licensor). The text hedges to "исторически произход" and does not assert a fixed corporate structure. No [CONFLICT]/[DATA NEEDED]. Provider profile: no BG operator, no licence number, no bonus terms.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Bulgarian origin; Sofia; EGT group founded **2002** | amusnet.com/our-group; egt.com/about-us; Crunchbase | Web-verified. |
| Rebrand EGT Interactive → Amusnet, **2022** | amusnet.com/news; Yogonet; iGamingBusiness | Announced March 2022, completed 1 June 2022. |
| Online-arm founding year + corporate relationship | — | Sources conflict → in-text [VERIFY]; hedged wording used. |
| Portfolio **200+** slots + live casino, video poker, roulette, keno | amusnet.com | Own-site floor; third-party counts higher (not stated). |
| Certifications: GLI + BMM Testlabs; MGA/Romania/Italy **supplier** licences | europebestcasinos; MGA register; amusnet.it | B2B supplier, NOT an operator licence. No licence № stated/invented. |
| Jackpot Cards: **4** suit levels (spades/hearts/diamonds/clubs), random trigger | amusnet.com/jackpots | Funding-from-bets framed as standard industry description (own page states only that higher bets raise odds). |
| RTP: Shining Crown **96.37%**, 40 Super Hot **95.81%**, 20 Super Hot **95.79%**, Flaming Hot **95.53%** | wizardofodds.com Amusnet payout page | Web-verified. At/below the ~96% modern average. Multiple builds exist (some ~90%) → operator chooses → confirm per casino. |
| Mechanics: fruits; 7 = wild (not scatter); star = scatter; gamble red/black | casino.guru; bestcasinosites; vegasslotsonline | Web-verified, generic to the classic line. |

## Illustrative / interpretive figures (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Low-RTP variants | "в порядъка на 90%" | Wizard of Odds lists ~90% variants for some titles (e.g. Burning Hot 90.02%); stated as a band, not per-casino. |
| Infographic scale | 95.00%–96.50% | visual scale only; the four RTP labels are the article's real figures. |

## Recalculation shown (per Step-6 requirement)
- Infographic bar math (Shining Crown 96.37% on a 95.00–96.50% scale over a 400px track):
  width = (96.37 − 95.00) / (96.50 − 95.00) × 400 = 1.37 / 1.50 × 400 = **365.3 ≈ 365 px** ✓ (SVG uses 365).
- 96% reference line: x = 120 + (96.00 − 95.00) / 1.50 × 400 = 120 + 266.67 = **386.67 ≈ 387** ✓ (SVG uses 387).
- Honesty claims: the classic band ~95.5–96.4% sits at/below the ~96% modern average ✓; Jackpot Cards is funded from bets and triggers at random → does not lower the house edge ✓; certification confirms fairness to the stated rules, not a player advantage ✓; the gamble is a coin-flip that adds variance, not value ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /kazino-igri/rotativki/, /blog/games-providers/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype; certificates and the progressive framed as house-edge mechanics, not hooks. ✓ Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **15** ("Shows AI patterns 85%"); Humaniser pass 1 **75** ("Likely human-written 75%"); Humaniser pass 2 **85** ("Likely human-written 85%", PASS). Per keep-best, kept **pass 2** (highest HL). content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across every pass. 07-gemini-check-1/-2/-3.md persist as the audit trail.

## Images (Step 8)
2 images:
- `images/amusnet-egt-rtp.svg` — hand-authored infographic; every figure traces to 05b (96.37 / 95.81 / 95.79 / 95.53 / ~96% / ~90%); source cited; 18+/RG note. Gemini review **100/100 PASS** pass 1.
- `images/amusnet-egt-hero.webp` — decorative flat-vector emblem hero (gemini-3-pro-image, 9.5 KB); no fabricated UI/logos/numbers/people/winning. Regenerated once (3D reels 55 → flat 2D **82 PASS**); kept the higher. 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No Amusnet/EGT provider page in the sitemap (checked 09.09.2026). Clean provider-profile pillar. Provider-hub sibling to Pragmatic (vk-0019). Distinct from the /blog/games-providers/ listing hub (Amusnet-specific profile, distinct primary kw), linked prose-only. Anchors the EGT classic-slot cluster (20 Super Hot vk-0020, 40 Super Hot vk-0023 same batch). Not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the online-arm founding year and the corporate relationship to EGT, or keep the hedged wording.
3. Confirm per-casino RTP builds for the target operator at publish (multiple certified versions exist; some ~90%).
4. If licence numbers are wanted (MGA supplier licence etc.), pull them from the official registers — none invented here.
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

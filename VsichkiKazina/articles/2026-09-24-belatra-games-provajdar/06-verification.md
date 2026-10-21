# 06-VERIFICATION — Всички Казина · 2026-09-24-belatra-games-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Belatra Games: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 92/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 90 (HL 85/75 initial → 90 pass 1, kept pass 1, PASS) · images: 2 (infographic 100, hero 100; best 100) · run date: 24.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact country/registered seat of Belatra today. Founding **year 1993**
is on the official About page; the **Minsk/Belarus origin** comes from secondary review sites and
the official page names no country; some aggregators claim a relocation to **Cyprus** — unconfirmed
on a primary/regulator source. The text hedges to „свързва се с Източна Европа" and asserts no fixed
seat. No [CONFLICT]/[DATA NEEDED]. Provider profile: no BG operator, no licence №, no bonus terms.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Основана **1993**; 30+ години; наземни кабинети; собствена джакпот система | belatragames.com/en/about | Official history page. |
| Онлайн дивизия след **2011**; машини с 3 екрана | belatragames.com/en/about | Official history timeline. |
| Сертификация **GLI** (Gaming Laboratories International) | belatragames.com/en/about | Only certification asserted; NO MGA/Curaçao/UKGC claimed (aggregator-only, unverified → deliberately omitted). |
| Портфолио **130–150** заглавия; slots + poker/roulette/Plinko/Sic Bo/crash/bingo/instant | belatragames.com/en/about; slotcatalog.com/en/soft/Belatra-Games | Official 150+; SlotCatalog 131 slots → stated as a range. |
| Механики: Hold & Win; разширяващи wild-ове с множители; Bonus Buy / нива | slotsmate.com Big Wild Buffalo 2; respinix Big Wild Buffalo 2; clashofslots Mummyland Treasures | Big Wild Buffalo 2 buy tier до 500x залога (to enter). |
| RTP: Beauty and the Beast **97.11%**, Chief's Sticky Fruits **96.56%**, Mummyland Treasures **96.36%**, Voodoo Coins **96.31%**, Make It Gold **96.13%**, Big Wild Buffalo 2 **96.07%** | slotcatalog.com/en/soft/Belatra-Games; clashofslots.com (Mummyland Treasures, Make It Gold); slotsmate.com (Voodoo Coins, Big Wild Buffalo 2) | Database-published defaults; multiple RTP builds exist → confirm per casino. |
| Макс печалби: Mummyland до **5,000x** (25,000x чрез bonus buy); Voodoo Coins **10,000x**; Make It Gold до **25,000x**; Big Wild Buffalo 2 **5,000x** | clashofslots / slotsmate (URLs above) | 25,000x са bonus-buy-gated, не от обикновено завъртане. |
| Диапазон RTP за каталога **~86.19%–97.11%** | slotcatalog.com/en/soft/Belatra-Games | Basis for „проверявай версията"; some titles run well below typical. |

## Illustrative / interpretive figures
| Where | Figure | Note |
|---|---|---|
| Infographic scale | 95.50%–97.50% | visual scale only; the six RTP labels are the article's real figures. |
| „~96%" reference | modern-slot average ~96% | industry reference, stated as ориентир, not a Belatra figure. |

## Recalculation shown (per Step-6 requirement)
- Infographic bar math (Beauty and the Beast 97.11% on a 95.50–97.50% scale over a 380px track):
  width = (97.11 − 95.50) / (97.50 − 95.50) × 380 = 1.61 / 2.00 × 380 = **305.9 ≈ 306 px** ✓ (SVG uses 306).
- 96% reference line: x = 180 + (96.00 − 95.50) / 2.00 × 380 = 180 + 95 = **275** ✓ (SVG uses 275).
- Big Wild Buffalo 2 96.07%: width = (96.07 − 95.50) / 2.00 × 380 = 0.57/2 × 380 = **108.3 ≈ 108** ✓ (SVG uses 108).
- Honesty claims: flagship titles sit at/above the ~96% modern average ✓; whole-catalog range 86–97% means the operator's chosen build decides the real % ✓; GLI confirms RNG fairness to the stated rules, not a player advantage ✓; bonus-buy pays upfront for a rare outcome and does not lower the house edge ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- No affiliate link (provider profile, no operator recommended) — correct; affiliate-disclosure footer kept. ✓
- Internal links: only the approved live set (/kak-ocenyavame/, /slot-igri/visok-rtp/, /kazino-igri/rotativki/, /blog/games-providers/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes in body/meta. En-dash only in the verbatim footer „10:00–17:00" and the SVG scale label. ✓ No promise/hype; certification and bonus-buy framed as house-edge mechanics, not hooks. ✓ Provider profile, not an operator review → no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **85/75** (two identical calls, noisy detector; best 85); Humaniser pass 1 **90** („Вероятно писано от човек, 90%", PASS). Per keep-best, kept **pass 1** (highest HL). content-queue gemini = `human 90`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across the pass. 07-gemini-check-1/-2.md persist as the audit trail.

## Images (Step 8)
images: 2 (infographic 100, hero 100; best 100).
- `images/belatra-games-rtp.svg` — hand-authored infographic; every figure traces to 05b (97.11 / 96.56 / 96.36 / 96.31 / 96.13 / 96.07 / ~96% / 86%–97%); 18+/RG note on-graphic. Gemini review pass 1 **65** (invented source line + label collision) → fixed → pass 2 **100 PASS**.
- `images/belatra-games-hero.webp` — decorative flat-vector hero (gemini-3-pro-image, 29.3 KB); classic→adventure reel motifs; no fabricated UI/logos/numbers/people/winning. Regenerated once (white corner cutouts + missing reel background 65 → clean **100 PASS**); kept the higher. 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No Belatra provider page in the sitemap (checked 24.09.2026, 92 URLs) and none in content-queue.
Clean provider-profile pillar. Provider-hub sibling to Pragmatic (/blog/pragmatic-play-provajdar/)
and Amusnet (/blog/amusnet-egt-provajdar/). Distinct from the /blog/games-providers/ listing hub
(Belatra-specific profile, distinct primary kw „belatra"). Not an operator review → no affiliate link.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm Belatra's current country/registered seat (Belarus origin vs reported Cyprus relocation), or keep the hedged wording.
3. Confirm per-casino RTP builds for the target operator at publish (multiple certified versions exist; catalog spans ~86%–97%).
4. If B2B licence numbers are wanted, pull them from official registers — none invented here (only GLI certification asserted).
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

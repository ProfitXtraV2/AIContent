# 06-VERIFICATION — Всички Казина · 2026-09-24-apollo-games-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Apollo Games: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 90 (HL 85 initial → 90 pass 1, kept pass 1, PASS) · images: 2 (infographic 95, hero 95; best 95) · run date: 24.09.2026

## Surviving flags
**1** in-text [VERIFY]: the exact portfolio count. Sources conflict — casino.guru ~60, SlotCatalog
103 (96 slots), other aggregators ~90. The text hedges to „около 100 заглавия" and asserts no exact
number. No [CONFLICT]/[DATA NEEDED]. Provider profile: no BG operator, no operator licence №, no bonus terms.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Основана **2007**; Прага, Чехия; фирма **Apollo Soft**; наземни VLT кабинети | slotcatalog.com/en/soft/Apollo-Games; apollogames.com | Founder identity NOT asserted (unverified snippet; /about-us returned 503). |
| Силна в Чехия (SlotCatalog #1), Словакия, Белгия | slotcatalog.com/en/soft/Apollo-Games | Market strength. |
| Сертифициран/лицензиран в 10+ юрисдикции: Чехия, Словакия, Гърция, Латвия, Литва, **България**, Румъния, Словения, Малта, Италия | apollogames.com | **B2B software certification, explicitly distinguished in-text from an operator licence / НАП operator register.** |
| MGA B2B лиценз **MGA/CRP/523/2018**, издаден **29.03.2019**; **ISO/IEC 27001** | apollogames.com; casino.guru/apollo-games-casino-review | Supplier licence ref verbatim; no operator № claimed/invented. |
| Портфолио **около 100** | slotcatalog.com (103; 96 slots); casino.guru (60) | Hedged with [VERIFY] — sources conflict. |
| Стил: класически/наземен — плодове, жокери, прости 4×3/5×3 | slotcatalog.com/en/soft/Apollo-Games | Old-school design. |
| Механики: разширяващи/верижни wild-ове, множители на цял барабан; **без прогресивни джакпоти** | slotcatalog.com/en/slots/Blood; /Pandora | Blood = Expanding Wild + Full Reel Multiplier; Pandora = chaining wilds + key/box. Progressive jackpot NOT evidenced on reachable sources → stated as „почти не се срещат". |
| RTP: Mad Mechanic Deluxe **95%**, Pandora **95%**, Turbo Slots **95%**, Blood **92%**, Four Fruits 2 **92%**, Midnight Fruits **92%** | slotcatalog.com/en/soft/Apollo-Games; /Mad-Mechanic-Deluxe; /Pandora; /Blood; /Four-Fruits-2 | Database defaults; RTP configurable → confirm per casino. |
| Макс печалби: Mad Mechanic Deluxe **2,000x**, Pandora **500x**, Turbo Slots **500x**, Blood **500x**, Four Fruits 2 **316x**, Midnight Fruits **174x** | slotcatalog.com pages above | Modest ceilings; 2,000x the outlier. |
| Конфигурируем RTP диапазон **85%–99%** | slotcatalog.com/en/soft/Apollo-Games | Basis for „проверявай версията". |

## Deliberately EXCLUDED (name-collision guard — NOT Apollo Games titles)
- „Apollo Rising" = **IGT**; „Apollo Pays" / „Apollo Pays Megaways" = **Big Time Gaming**;
  „Amazing Link Apollo" / „Age of Olympus: Apollo" = other studios. None attributed to Apollo Games.
- Unverified founder name and „first HTML5 at ICE 2017 / rebrand" claims — omitted (snippet-only).

## Illustrative / interpretive figures
| Where | Figure | Note |
|---|---|---|
| Infographic scale | 0–2,000x | linear scale; the six max-win labels are the article's real figures. |
| „между 174x и 500x" | range of the non-outlier titles | 174x (Midnight Fruits) to 500x (Pandora/Turbo/Blood); correct. |

## Recalculation shown (per Step-6 requirement)
- Infographic bar (Mad Mechanic Deluxe 2,000x on a 0–2,000x scale over a 380px track):
  width = 2000 / 2000 × 380 = **380 px** ✓ (SVG uses 380, full track).
- Pandora 500x: width = 500 / 2000 × 380 = **95 px** ✓ (SVG uses 95; = 25% of the 2,000x bar).
- Four Fruits 2 316x: width = 316 / 2000 × 380 = **60.04 ≈ 60 px** ✓ (SVG uses 60).
- Midnight Fruits 174x: width = 174 / 2000 × 380 = **33.06 ≈ 33 px** ✓ (SVG uses 33).
- Honesty claims: B2B certification tests the software, is not an operator licence / НАП listing ✓;
  RTP defaults 92–95% sit below the ~96% modern average ✓; max-win ceilings modest, 2,000x the
  exception ✓; RTP configurable 85–99% so the operator's version decides the real % ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- No affiliate link (provider profile, no operator recommended); affiliate-disclosure footer kept. ✓
- Internal links: only the approved live set (/blog/proverka-licenz-kazino/, /blog/rotativki-s-plodove/, /kak-ocenyavame/, /blog/games-providers/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" (footer). ✓
- Zero em-dashes in body/meta. En-dash only in the verbatim footer „10:00–17:00" and SVG scale label. ✓
- B2B certification NOT presented as an operator licence / НАП listing (explicit distinction). ✓ No foreign „Apollo" title attributed to Apollo Games. ✓ Provider profile → no operator licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **85** („Likely human-written, 85%") →
Humaniser pass 1 **90** („Likely human-written, 90%", PASS). Per keep-best, kept **pass 1** (highest HL).
content-queue gemini = `human 90`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand
UNTOUCHED across the pass. 07-gemini-check-1/-2.md persist as the audit trail.

## Images (Step 8)
images: 2 (infographic 95, hero 95; best 95).
- `images/apollo-games-max-win.svg` — hand-authored infographic; every figure traces to 05b (2,000x /
  500x / 500x / 500x / 316x / 174x); 18+/RG note on-graphic; clarifies RTP is a separate configurable
  (85–99%) metric. Gemini review **95 PASS** pass 1 (SVG „no changes required").
- `images/apollo-games-hero.webp` — decorative flat-vector hero (gemini-3-pro-image, 17.1 KB); classic
  land-based fruit-machine motif (fruits, joker, seven as game symbols); no fabricated UI/logos/numbers/
  people/winning (Joker = standard game symbol, not a human face). Review **95 PASS**; only an optional
  „4×3/5×3 vs 3-reel" perfectionism note, not a defect → kept. 08-image-review-1.md persists.

## Anti-cannibalization note (Step-6 human check)
No Apollo Games provider page in the sitemap (checked 24.09.2026, 92 URLs) and none in content-queue.
Clean provider-profile pillar. Sibling to Belatra (vk-0163) and Swintt (vk-0164) same batch, plus
Amusnet/Pragmatic profiles. Distinct primary kw „apollo games". Not an operator review → no affiliate link.

## Human-action list (owned by you, Step 6)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the exact portfolio count (~60 vs 103), or keep „около 100".
3. Confirm per-casino RTP builds at publish (RTP configurable 85–99%; defaults 92–95%).
4. If B2B licence numbers beyond MGA/CRP/523/2018 are wanted, pull from official registers — none invented.
5. Note the BG-relevance carefully at publish: Apollo lists Bulgaria among its certified jurisdictions,
   but that is the software provider's B2B certification, NOT an operator licence / НАП operator listing.
6. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

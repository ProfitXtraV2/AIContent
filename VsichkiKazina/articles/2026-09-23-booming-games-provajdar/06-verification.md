# 06-VERIFICATION — Всички Казина · 2026-09-23-booming-games-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Booming Games: профил на доставчика, механики и топ слотове** · type: guide (provider profile / provider-hub) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: Gemini Step-7 human 85 (HL 15 → 85, kept pass 1, PASS) · images: 2 (infographic 85, hero PASS; best 85) · body ~727 words · run date: 23.09.2026

## Surviving flags
**1** in-text [VERIFY]: точното текущо седалище и юридическа структура на Booming Games. Основана 2014 г. с регистрация в Дъглас, остров Ман (Crunchbase/ZoomInfo, съосновател/CEO Max Niehusen), но официалният сайт днес посочва адрес на седалището в Малта (Birkirkara). Източниците се разминават дали текущото седалище/юрисдикция е остров Ман или Малта. Текстът е хеджиран („основана 2014 на остров Ман, оперира и от Малта") и не твърди фиксирана структура. No [CONFLICT]/[DATA NEEDED]. Провайдър профил: няма BG оператор, няма лиценз №, няма бонус условия.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Основана **2014**, Дъглас/остров Ман; CEO Max Niehusen | crunchbase.com/organization/booming-games; zoominfo (Booming Games Ltd); worldcasinodirectory | Web-verified. |
| Текущ адрес на седалището — Малта (Birkirkara) | booming-games.com | На официалния сайт → оттам [VERIFY] за структурата IoM vs MT. |
| Доставчически лицензи: **MGA + Италия 2018, Швеция 2019, UKGC 2021** (+ др.) | booming-games.com; worldwidegamblers.com; online.worldcasinodirectory.com | Web-verified. B2B доставчик, НЕ оператор/казино лиценз. Няма лиценз № твърдян/измислен. |
| Собствен **Remote Gaming Server (In-House RGS)** | booming-games.com | Собствена технология на доставчика. |
| Механики: **Hold and Win** (монети + респини, множители се сумират), **Megaways**, безплатни завъртания | casitsu.com; slotcatalog.com | Web-verified, generic to the studio's line. |
| RTP/тавани: Booming Seven Deluxe **96.55% / 2,422x**; Buffalo Hold and Win **95.91% / 1,200x**; Buffalo Hold and Win Extreme **95.50% / 4,000x**; TNT Bonanza **96.60% / 6,500x**; Blockchain Megaways **96.50% / 40,320x** | slotcatalog.com/en/soft/Booming-Games; casitsu.com/slots-by-provider/booming-games | Cross-checked (2 незав. бази). Multiple RTP builds may exist per title → operator chooses → confirm per casino. |

## GUARDRAIL — excluded title (Step-6 human check)
**Wild Wild Duck** беше seed-кандидат, но верификацията показва, че е слот на **Popiplay**, НЕ на Booming Games (bigwinboard.com/wild-wild-duck-popiplay-slot-review/). Изключен от статията — не се приписва чужда игра на Booming Games. Проверете при желание, но НЕ добавяйте като заглавие на Booming Games.

## Illustrative / interpretive figures (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Portfolio size / cadence | (умишлено НЕ е даден твърд брой) | Каталозите се разминават (SlotCatalog ~250–331; собствен сайт по-малко; cadence 2 vs 4/месец) → хеджирано в прозата, без твърдо число, за да не се фабрикува. |
| Infographic scale | 95.00%–97.00% | само визуална скала; петте RTP етикета и петте тавана са реалните числа на статията. |

## Recalculation shown (per Step-6 requirement)
- Инфографика, ширина на бара за Booming Seven Deluxe (RTP 96.55% на скала 95.00–97.00 върху 340px track, 170px на 1.00%):
  width = (96.55 − 95.00) × 170 = 1.55 × 170 = **263.5 ≈ 264 px** ✓ (SVG използва 264).
- Референтна линия 96.0%: x = 40 + (96.00 − 95.00) × 170 = 40 + 170 = **210 px** ✓ (SVG използва 210).
- Honesty claims: RTP-тата клъстерират около 96% и са дългосрочна статистика, не сесийно обещание ✓; таваните (до 40,320x) са редки крайни изходи, не очаквани стойности ✓; сертификат = честност спрямо правилата (писани в полза на казиното), не предимство ✓; Hold and Win/Megaways функциите менят темпото/размера, не базовата математика ✓. Всички коректни.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/kak-ocenyavame/, /slot-igri/, /kazino-igri/rotativki/, /blog/games-providers/, /otgovorna-igra/), 5 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes in body/meta. En-dash only in verbatim RG footer „10:00–17:00" and the infographic scale „95.00%–97.00%". ✓ No promise/hype; certificates and mechanics framed as house-edge, not hooks. ✓ Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **15** ("Shows AI patterns 85%"); Humaniser pass 1 **85** ("Likely human-written 85%", PASS). Per keep-best, kept **pass 1** (highest HL). content-queue gemini = `human 85`. All numbers, links, RG lines, 18+, [VERIFY], dates, byline, brand UNTOUCHED across passes. 07-gemini-check-1/-2.md persist as the audit trail.

## Images (Step 8)
2 images:
- `images/booming-games-rtp-tavan.svg` — hand-authored infographic; every figure traces to 05b (96.55 / 95.91 / 95.50 / 96.60 / 96.50 RTP; 2,422x / 1,200x / 4,000x / 6,500x / 40,320x макс.); scale + source note; 18+/RG line. Gemini review **85/100 PASS** pass 1, 0 integrity failure. Two cosmetic gridline fix passes each re-scored 75 → kept the pass-1 version (keep-best). 08-image-review-1/-2.md persist.
- `images/booming-games-hero.webp` — decorative flat-vector concept hero (gemini-3-pro-image, 21.9 KB): reel + gears + magnifying glass over a blank gauge = mechanics + fairness check. No fabricated UI/logos/numbers/people/winning. Reviewed PASS (excellent), no changes.

## Anti-cannibalization note (Step-6 human check)
No Booming Games provider page in the sitemap (checked 23.09.2026). Distinct primary kw („booming games"). Provider-hub sibling to Amusnet (vk-0021) и Pragmatic (vk-0019). Distinct from the /blog/games-providers/ listing hub (this is a Booming-Games-specific profile), linked prose-only. Not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm Booming Games' current registered seat / structure (Isle of Man 2014 registration vs Malta HQ address), or keep the hedged wording.
3. Confirm per-casino RTP builds for the target operator at publish (a title may ship in more than one certified RTP version).
4. If licence numbers are wanted (MGA supplier licence etc.), pull them from the official registers — none invented here.
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).
6. GUARDRAIL confirmed: Wild Wild Duck is a Popiplay title and is intentionally NOT in this article — do not add it as a Booming Games slot.

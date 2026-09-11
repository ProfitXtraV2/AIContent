# 06-VERIFICATION — Всички Казина · 2026-09-11-playn-go-provajdar
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Play'n GO: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 95/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 90 (HL 35 → 90, kept pass 1, PASS) · images: 2 (infographic 85, hero 85; best 85) · run date: 11.09.2026

## Surviving flags
**0** in-text [VERIFY] / [DATA NEEDED] / [CONFLICT]. Founding year 1997 is well-sourced; the "own slots from mid-2000s" framing is hedged and asserts no contested precise year, so it carries no flag. Provider profile → no BG operator, no licence number, no bonus terms.

## Provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Founded **1997**, Векшьо (Växjö), Sweden; independent Swedish company | playngo.com/about-us; casino.org; softswiss.com | Web-verified. Own proprietary slots from ~mid-2000s (sources frame 1997 founding vs ~2004 studio start → text hedged, no hard year asserted for the pivot). |
| Offices Malta + Gibraltar (+ more) | playngo.com/about-us; softswiss.com | Malta (Valletta) + Gibraltar registered offices; also Hungary/Philippines reported (not stated in text). |
| B2B software **supplier**, not an operator; slots-focused | playngo.com/about-us | Core = video slots. No notable live/bingo. |
| **400+** titles; ~2-3 new games/month | playngo.com/about-us; casinos.com | "More than 400"; text says „по две-три… месечно" (source range 2-4). |
| Independent testing: **GLI + BMM Testlabs** | playngo.com/about-us | Logos on own site. eCOGRA/iTech NOT confirmed → deliberately not stated. |
| B2B supplier licences: **Malta (MGA), UK (UKGC), Gibraltar** | playngo.com/about-us; gamblingcommission.gov.uk (UKGC acct 55949) | Numbers not quoted in body (profile, not review). MGA/B2B/225/2012 + Gibraltar RGL 131 verified but not printed. |
| Iconic titles: Book of Dead, Reactoonz, Rich Wilde series, Moon Princess, Fire Joker, Legacy of Dead, Rise of Olympus | playngo.com/post/top-series-slots-at-play-n-go; casinos.com | Web-verified. |
| **Book of Dead RTP ladder**: 96.21 / 94.25 / 91.25 / 87.25 / 84.18 | slotcatalog.com/en/slots/Book-of-Dead | Full configurable range; operator selects the build. All 5 stated in 05b + the infographic. |
| **Reactoonz RTP**: 96.51 default, ~94.51 / ~91.49 lower | slotcatalog.com/en/slots/Reactoonz | Text hedges the lower configs with „около". Some review sites round to 94.2/91.2. |
| Mechanics: expanding book-symbol free spins; cluster grid + cascades; charge-up meter | casinobeats.com; pokernews.com; olbg.com | Web-verified, generic to the respective title families. |

## Illustrative / interpretive figures
| Where | Figure | Note |
|---|---|---|
| Infographic scale | 80%–97% | Visual scale only; the five RTP labels are the article's real figures. |
| Bar math | see below | Recalculated. |

## Recalculation shown (per Step-6 requirement)
- Infographic bar (Book of Dead 96.21% on an 80.00–97.00 scale over a 410px track from x=150):
  width = (96.21 − 80.00) / (97.00 − 80.00) × 410 = 16.21 / 17 × 410 = **390.9 ≈ 391 px** ✓ (SVG uses 391).
- Lowest bar (84.18%): (84.18 − 80.00) / 17 × 410 = 4.18 / 17 × 410 = **100.8 ≈ 101 px** ✓ (SVG uses 101).
- Honesty claims: only the 96.21% build sits above the ~96% modern average; every other build is below ✓. Certification confirms fairness to the stated rules, not a player advantage ✓. Supplier ≠ operator ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker "18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: /blog/book-of-dead/ + /blog/reactoonz/ (same-batch spokes) + /blog/games-providers/ (hub) + /blog/pragmatic-play-provajdar/ + /blog/amusnet-egt-provajdar/ + /kak-ocenyavame/ + /slot-igri/ + /otgovorna-igra/ — 8, hub-and-spoke, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00" and the infographic scale „80%–97%". ✓ No promise/hype. Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness by version: initial **35** ("Shows AI patterns 65%"); Humaniser pass 1 **90** ("Likely human-written 90%", PASS). Per keep-best, kept **pass 1** (highest HL). content-queue gemini = `human 90`. 07-gemini-check-1/-2.md persist as the audit trail. Post-check accuracy edit (image review): added the two lower verified RTP figures 87.25/84.18 to the existing list and dropped the SVG's inline SlotCatalog citation — factual/accuracy only, no stylistic change, numbers verified above.

## Images (Step 8)
2 images:
- `images/playn-go-rtp-versii.svg` — hand-authored infographic; every figure traces to 05b (96.21/94.25/91.25/87.25/84.18); 18+/RG note; no source-name in graphic. Review 75 → (label column fix) → 65 (figure-support) → (state full ladder in 05b) → **85 PASS**.
- `images/playn-go-hero.webp` — decorative flat-vector metaphor hero (gemini-3-pro-image, 16.7 KB): abstract reel columns + cluster grid; no fabricated UI/logos/numbers/people/winning. **85 PASS**.
0 integrity failures. Both ride the content PR; referenced from 05b (hero under H1, infographic beside the RTP data). 08-image-review-1/-2.md persist.

## Anti-cannibalization note (Step-6 human check)
No Play'n GO provider page in the sitemap (checked 11.09.2026). Clean provider-profile pillar — the 4th after Pragmatic (vk-0019), Amusnet (vk-0021), Novomatic via Book of Ra (vk-0035) and NetEnt (vk-0042). Distinct from the /blog/games-providers/ listing hub (Play'n GO-specific profile, distinct primary kw „play'n go"), linked hub-and-spoke. Anchors this batch's two Play'n GO games (Book of Dead vk-0046, Reactoonz vk-0047). Not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6)
1. Fill the "[About Всички Казина boilerplate]" slot.
2. Confirm per-casino RTP build for the target operator at publish (multiple certified versions exist; Book of Dead down to 84.18%).
3. If B2B supplier licence numbers are wanted (MGA/UKGC/Gibraltar), pull them from the official registers — none printed here.
4. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

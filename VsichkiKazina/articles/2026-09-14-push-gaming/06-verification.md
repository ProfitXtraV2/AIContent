# 06-VERIFICATION — Всички Казина · 2026-09-14-push-gaming
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Push Gaming: профил на доставчика, механики и топ слотове** · type: guide (provider profile) · byline: editorial (signed Георги Тодоров) · gate: PASS WITH FIXES 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 85 (HL 85 on pass 1, PASS, kept original — no humaniser pass needed) · images: 2 (infographic 100, hero 85; best 100) · word count: 771 (main body) · em-dashes: 0 · run date: 14.09.2026

## Surviving flags
**0 in-text [VERIFY] / [CONFLICT] / [DATA NEEDED].** Provider profile: no BG operator, no licence number, no bonus terms. All specific figures are web-verified public provider / international game-DB data (table below); none is a blocking in-text flag. Two items were deliberately EXCLUDED rather than flagged, to avoid fabrication:
- „Dynamic Payways" as a Push-named mechanic — could not be confirmed by that exact name on any reachable page (multiple game DBs explicitly did not list it). Omitted; the verified mechanics (Mystery Stacks + Nudge & Reveal, Razor Reveal, cluster pays, каскади, Bonus Buy) are used instead.
- Exact catalogue size — sources conflict (SoftGamings „22 video slots" vs third-party „80+"). No count stated; described as a small, focused catalogue.

## Time-sensitive / provider claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Founded **2010**; HQ London; office in Malta | softgamings.com/...push-gaming; fruityslots.com/slots/providers/push-gaming | Web-verified, two sources agree. |
| Licences **UK Gambling Commission + Malta Gaming Authority** | softgamings; fruityslots; UKGC/MGA public registers | Both sources list UKGC+MGA (some add Alderney/Gibraltar → not asserted). Testing labs eCOGRA + BMM Testlabs (SoftGamings). No licence № stated/invented. |
| Small high-volatility studio; доставчик ≠ оператор | softgamings ("adrenaline-rush high-volatility titles") | Framing, not a hard count. |
| Razor Shark: RTP **96.70%**, 5x4 grid, **20** lines, very high vol., max **85,475x** | askgamblers / cryptogamble.com/games/slots/reviews/razor-shark / adventuregamers.com/online-slots/razor-shark | Web-verified across sources. Mystery Stacks + Nudge & Reveal + Razor Reveal (coin **1x–2,500x**) + Bonus Buy confirmed on same pages. |
| Jammin' Jars: RTP **96.83%**, cluster pays, max **20,000x** | fruityslots; jamminjars-slot.com | Web-verified. |
| Fat Rabbit: RTP **96.45%** | fruityslots (Push provider RTP table) | Web-verified. |
| Big Bamboo: RTP **96.13%**, high vol., max **50,000x** | fruityslots; mintyslots/big-bamboo; cercyon.eu | Web-verified across sources. |
| Modern-slot RTP baseline ~**96%** | industry-standard, generic | Used as an orienting reference, not an operator claim. |

## Illustrative / interpretive figures (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| Infographic scale | 95.50%–97.00% | Visual scale only; the four RTP labels are the article's real web-verified figures. |
| „около и малко над средното" | ~96% | All four cited RTPs sit at/above the ~96% modern baseline (96.13–96.83). |

## Recalculation shown (per Step-6 requirement)
Infographic bar math (Jammin' Jars 96.83% on a 95.50–97.00% scale over a 400px track from x=120):
- width = (96.83 − 95.50) / (97.00 − 95.50) × 400 = 1.33 / 1.50 × 400 = **354.7 ≈ 355 px** ✓ (SVG uses 355).
- ~96% reference line: x = 120 + (96.00 − 95.50) / 1.50 × 400 = 120 + 133.3 = **253** ✓ (SVG uses 253).
- Honesty logic: all four cited RTPs (96.13–96.83) sit at/above the ~96% baseline ✓; RTP is configurable and the operator picks the build ✓; very high volatility means the declared average is a long-run figure, not a session promise ✓; certification confirms fairness to the stated rules, not a player advantage ✓; a Bonus Buy changes how you pay for entry, not the RTP ✓. All correct.

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text closing + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 Aug 2026 regime), pending-application wording, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/blog/razor-shark/, /kak-ocenyavame/, /blog/games-providers/, /slot-igri/, /otgovorna-igra/), 5 distinct, in-context. /blog/razor-shark/ is the same-batch spoke (vk-0072). ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly (×3). ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00" and the SVG scale range. ✓ No promise/hype; certificate/licence framed as house-edge mechanics, not hooks. ✓ Provider profile, not an operator review → no affiliate link, no НАП licence №. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Pass 1 verdict: „Likely human-written, 85% confidence" → human-likeness **85** → PASS on the first check. No Humaniser pass applied (keep-best = the original 05b, highest HL seen). content-queue gemini = `human 85`. Gemini's style suggestions (colon rhythm, softer imperatives, drop one topic sentence) were NOT applied because the draft already PASSES and one suggestion proposed inserting an em-dash (brand hard rule: zero em-dashes). All numbers, links, RG lines, 18+, dates, byline, brand UNTOUCHED. 07-gemini-check-1.md persists as the audit trail.

## Images (Step 8)
2 images:
- `images/push-gaming-rtp.svg` — hand-authored RTP infographic; every figure traces to 05b (96.83 / 96.70 / 96.45 / 96.13 / ~96%); scale + source noted; 18+/RG note. Gemini review: pass 1 **72** (reference-line overlapped footer text) → fix → **85** → applied Gemini's layering + label-alignment fixes → **100/100 PASS**. Best 100.
- `images/push-gaming-hero.webp` — decorative flat-vector deep-sea / high-volatility metaphor (gemini-3-pro-image, 11.1 KB); no fabricated UI/logos/numbers/people/winning. Gemini review **85 PASS** pass 1. 08-image-review-1/-2.md persist.
No integrity failures on either image.

## Anti-cannibalization note (Step-6 human check)
No Push Gaming provider page in the sitemap. Clean provider-profile pillar (8th in the series; Pragmatic vk-0019 + Amusnet vk-0021 live; NetEnt/Play'n GO/Novomatic/Hacksaw/Relax queued). Distinct primary kw „push gaming". Razor Shark (vk-0072) is written in the SAME batch as its spoke → /blog/razor-shark/ linked as the hub's anchor to the flagship title (precedented same-batch hub-spoke). Other Push titles (Jammin' Jars, Fat Rabbit, Big Bamboo) mentioned plain-text, no link. Not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Confirm the provider facts above against the cited sources at publish (founding year, HQ/office, UKGC+MGA licences, per-title RTPs, Razor Shark 85,475x max win). None invented.
3. If licence numbers are wanted (UKGC/MGA supplier licences), pull them from the official registers — none stated or invented here.
4. Confirm per-casino RTP builds for the target operator at publish (configurable versions exist; the operator chooses).
5. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

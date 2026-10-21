# 06-VERIFICATION — Всички Казина · 2026-09-13-sizzling-hot
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here has been resolved by the autopilot.*

Article: **Sizzling Hot: RTP и характеристики на класиката от Novomatic** · type: guide (slot explainer) · byline: editorial (signed Георги Тодоров) · gate: PASS 93/100 · humanisation: HUMAN-LIKE · Gemini Step-7: human 95 (PASS, pass 2; kept over initial 75) · images: 2 (infographic 92, hero 92; best 92) · run date: 13.09.2026

## Surviving flags
**1** in-text [VERIFY]: точната максимална печалба на Sizzling Hot и коя версия. Източниците се разминават: SlotCatalog (Sizzling Hot Deluxe) цитира ~1000x залога, AskGamblers (оригиналния Sizzling Hot) цитира ~5000x залога. Затова 05b НЕ посочва твърдо число, а флагва [VERIFY] — без структура „Версия А/Б" в текста. No [CONFLICT]/[DATA NEEDED]. Slot explainer: no BG operator, no licence number, no bonus terms. Every € figure is ILLUSTRATIVE.

## Time-sensitive / game claims to confirm at publish (source URLs below)
| Claim | Source to confirm | Note |
|---|---|---|
| Provider **Novomatic**; онлайн разпространение чрез **Greentube** | askgamblers; slotcatalog; slotsmate | Web-verified. |
| Grid **5 барабана × 3 реда**, **5 фиксирани линии** | askgamblers; slotcatalog | Web-verified (fixed lines, left-to-right from reel 1). |
| Default RTP **95.66%** (house ~**4.34%**) | slotcatalog (95.66%); askgamblers (оригинал 95.65%); slotsmate/fruityslots | Web-verified default/headline build; оригиналът се цитира 95.65% → същият ~95.66% headline. |
| По-ниски конфигурируеми билдове | slotcatalog (изброява ~92.28% / ~90.02%) | Описано в текста без твърди числа + насока към инфо-панела. |
| Волатилност **ниска до средна** | askgamblers (low-medium); slotcatalog (medium) | Web-verified. |
| Символи: плодове + огнена седмица (топ) + **звезда-скатер**; **няма wild, няма безплатни завъртания, няма бонус рунд** | askgamblers; slotcatalog (8 symbols) | Web-verified. |
| **Гамбъл** функция (удвояване, познай червено/черно, 50/50) | askgamblers; slotcatalog | Web-verified; edge-неутрална. |
| Deluxe онлайн версия от **2007 г.** | slotcatalog (release 13.11.2007) | Web-verified. |
| Максимална печалба | slotcatalog ~1000x (Deluxe) / askgamblers ~5000x (оригинал) | **Конфликт → [VERIFY]; НЕ е посочено число в 05b.** |

## Illustrative numbers used (none BG-operator-sourced)
| Where | Figure | Note |
|---|---|---|
| RTP/edge | 95.66% / ~4.34% | provider default (confirm live build) |
| Worked example | €1000 оборот → ~€957 / ~€43 | illustrative, long-run |
| Gamble example | €10 → €40 | illustrative (два верни удвоявания) |

## Recalculation shown (per Step-6 requirement)
- RTP 95.66% на €1000: връщане 0,9566 × €1000 = **€956,60 ≈ €957**; за казиното 0,0434 × €1000 = **€43,40 ≈ €43**. ✓ съвпада с текста и инфографиката.
- SVG house bar: 0,0434 × 500 = **21,7 ≈ 22 px**. ✓
- Core honesty claims: RTP 95.66% е дългосрочна статистика, не обещание; конфигурируемо RTP → операторът избира билда → инфо-панел; гамбълът е чиста 50/50 и НЕ мени домашното предимство (усилва волатилността на резултата); ниска до средна волатилност = по-чести дребни попадения, не по-добър шанс. Всичко коректно. ✓

## Compliance spot-check (verbatim untouchables present)
- RG marker „18+ Хазартът може да пристрасти. Играйте отговорно." — present (in-text + footer). ✓
- RG signposting: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) + „Солидарност" 0888 99 18 66 (10:00–17:00). ✓
- Affiliate footer (1 август 2026 regime), заявление подадено/очаква издаване, NO issued-licence claim, NO invented №. ✓
- Internal links: only the approved set (/slot-igri/, /blog/games-providers/, /kazino-igri/rotativki/, /otgovorna-igra/), 4 distinct, in-context. ✓
- Byline Георги Тодоров; brand „Всички Казина" spelled correctly. ✓
- Zero em-dashes (incl. meta). En-dash only in the verbatim footer „10:00–17:00". ✓ No promise/hype. Slot explainer, not an operator review → no affiliate link, no НАП licence №, no Протокол. ✓

## External check (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Human-likeness: initial **75** („Likely human-written 75%"), after humaniser pass 1 **95** („Highly likely human-written 95%", PASS). Kept the pass-1 version (95 > 75). Passes applied: 1 humaniser pass (combined the „Няма" staccato triple; trimmed the philosophical intro wrapper; replaced a preachy line with a plain fact). Gemini left the [VERIFY] flag intact (agrees it stays until verified). content-queue gemini = `human 95`. 07-gemini-check-1.md / -2.md persist as audit trail.

## Images (Step 8)
2 images, best review score **92** (gemini-3.1-pro-preview):
- `images/sizzling-hot-rtp.svg` — hand-authored infographic; every figure traces to 05b (95.66% / 4.34% / €1000 / ~€957 / ~€43); „18+ Играйте отговорно" note; „RTP е дългосрочна статистика" disclaimer. Reviewer: „math, figures, and claims perfectly match… Ready to publish." Applied a trivial bottom-margin y-shift after review.
- `images/sizzling-hot-hero.webp` — decorative retro fruit-slot AI hero (gemini-3-pro-image, 19.2 KB); five symbols in a row (cherries, lemon, grapes, watermelon, flaming seven + star) matching the 5-reel game; no fabricated UI/logos/numbers-as-data/people/winning. Regenerated once (pass 1 65 → pass 2 92) to fix a 3-reel vs 5-reel mismatch.
No integrity failures on either image.

## Anti-cannibalization note (Step-6 human check)
No Sizzling Hot page in the sitemap (checked 13.09.2026). Clean slot-explainer pillar. Novomatic/Greentube cluster (anchors the providers hub /blog/games-providers/). Explicitly separated from the EGT/Amusnet fruit classics (Burning Hot / 20 Super Hot — a different provider) inside the text. Game explainer, not an operator review → no affiliate link; no operator/licence № invented.

## Human-action list (owned by you, Step 6 / Step 8)
1. Fill the „[About Всички Казина boilerplate]" slot.
2. Resolve the in-text [VERIFY]: confirm the exact maximum win and which version (Deluxe ~1000x vs original ~5000x) against Greentube's official page / the in-game info panel; insert data and delete the bracket, or keep hedged.
3. Confirm the site's affiliate-licence status at publish (footer says filed/awaiting; never claim issued).

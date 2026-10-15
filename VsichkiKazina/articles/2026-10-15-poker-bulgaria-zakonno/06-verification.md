# 06-VERIFICATION — vk-0281 — Законно ли е да играете покер в България

## Surviving flags (stay in text, human owns resolution)
1. **[VERIFY] данъчно третиране на печалбите от покер.** Tax is never asserted as fact per brand bible. Routed to счетоводител/НАП + linked to /blog/danaci-pechalbi-onlajn-kazino/. Human to confirm vs actual ЗКПО/ЗДДФЛ before any rate/threshold is ever stated. (1 surviving flag, by design.)

## Time-sensitive / primary-sourced claims
- Надзор при НАП от 08.08.2020 (ДВ бр. 69/04.08.2020). Source: ЗХ pack §1.
- Видове игри по чл. 41, ал. 1 ЗХ; покер = т. 5 (игри в казино). Source: pack §3.
- Чл. 3, ал. 1 и ал. 3 (лиценз от НАП, един лиценз за една игра). Source: pack §2.
- Чл. 41, ал. 2 (онлайн допустим, без томбола/моментна лотария). Source: pack §3.
- Чл. 6, ал. 1 (регистрация/идентификация, реално време към НАП). Source: pack §4.
- Игрално казино капитал мин. 1 500 000 лв. (чл. 4, ал. 2). Source: pack §2.
- Чл. 9, ал. 14 + чл. 97а, ал. 2: глоба 500–2000 лв. (ДВ бр. 42/2024). Source: pack §4.
- Чл. 17, ал. 6: блокиране до 24 ч. от 01.08.2026 (ДВ бр. 69/31.07.2026). Source: pack §4.
- Чл. 9, ал. 13: затворени платежни канали. Source: pack §4 / zakon-za-hazarta sibling.
- Чл. 2, ал. 3: 18+ (ДВ бр. 42/2024). Source: ЗХ / sibling.
- illegal_gambling@nra.bg; анонимни сигнали не се разглеждат. Source: pack §4.
- Бюджет ~5% от нетните доходи (препоръка на НАП). Source: pack §6.
- **Context (non-primary, dated):** онлайн покер лицензиран в България от 2014 г. Source: PokerNews/PokerFuse 08.2014 (journalistic). Presented as historical context only, no operator named, no reliance for a regulated claim.

## Figure recalculated (working shown)
Глоба в евро по фиксирания курс 1,95583 лв. за 1 €:
- 500 лв. ÷ 1,95583 = 255,6469… → **255,65 €**
- 2000 лв. ÷ 1,95583 = 1022,5876… → **1022,58 €**
Matches the text and the infographic. Курсът е посочен в текста като база.

## Gemini Step-7 (text, human-likeness)
- Pass 1 (baseline draft): Shows AI patterns, 70% → human-likeness 30. Needs changes. (07-gemini-check-1.md)
- Humaniser pass 1: applied all 5 flagged recs (removed 2 signposting lead-ins, cut 1 translated metaphor, de-hyped 2 headings), numbers/links/RG untouched.
- Pass 2 (after humaniser pass 1): Likely human-written, 85% → human-likeness 85. **PASS** (≥ 80). (07-gemini-check-2.md)
- KEEP-BEST: HL 30 → 85; winner = current 05b (humaniser pass 1). gemini column = `human 85`.

## Images (Step-8)
images: 1 (infographic) — Gemini review unavailable (endpoint timed out ×2); manual integrity PASS (08-image-review-1.md). Hand-authored SVG, every figure traced verbatim to 05b (1 500 000 лв.; 500–2000 лв.; 255,65–1022,58 €; 24 ч.; чл. 41/4/9/97а/17/2 refs; 18+). No operator logos/names, no people/faces, no glamorised winning. No decorative AI hero added (optional; not needed for a legal guide).

## Anti-cannibalization / scope
- DISTINCT legal-status pillar; no poker-legality URL in the live sitemap (checked 15.10.2026). vk-0008 (gameplay), vk-0263 (hands), vk-0264 (ЗХ taxonomy) do not cover it.
- Guides-only scope respected: all legal facts from ЗХ/НАП pack (no geo-blocked operator/register data). No operator facts, no bonus/licence numbers invented.

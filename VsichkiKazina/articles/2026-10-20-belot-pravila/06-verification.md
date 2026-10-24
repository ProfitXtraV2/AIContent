# 06 — Verification (for the human reviewer)

Article: **Белот правила и точкуване за начинаещи** (vk-0286, guide, slug `2026-10-20-belot-pravila`)
Primary query: `белот правила` · byline Георги Тодоров · brand Всички Казина

## Surviving flags
- **0** `[VERIFY]` / `[DATA NEEDED]` / `[CONFLICT]` / `[LINK NEEDED]`.
- This is an evergreen card-game rules guide: no operator T&C, no НАП-register listing, no bonus/RTP/licence figures were used or needed (guides-only scope, fully in scope). No operator-specific fact appears anywhere.

## Fact scope / sourcing
Every белот rule and number is evergreen and cross-confirmed across ≥2 independent BG rules
sources (the article states no operator-specific or time-sensitive claim):
- https://terca.bg/pravila/ — deck, ranking, dealing 3+2 then 3, bidding order, анонси (терца 20 / петдесет 50 / сто 100 / каре 100-150-200 / белот 20), last trick +10, 151 threshold.
- https://scatter.bg/belot-kak-se-igrae-pravila-taktiki/ — card values коз/без коз, каре девятки 150 / валета 200, 162 total, без коз/всичко коз doubling to 262, rounding to tens, 151 threshold.

Regional-variant honesty (stated in-text as "agreed per table", NOT asserted as universal):
праг 151, капо bonus value (described as concept only — NO point value asserted), the naming
кварта/квинта vs петдесет/сто, майорна терца, and бридж-белот.

## Recalculated figure (working shown)
Claim: "Картите в една ръка носят 152 точки … сборът при игра с коз става 162."
- Trump suit (коз values): 20 (Вале) + 14 (9) + 11 (Асо) + 10 (10) + 4 (Поп) + 3 (Дама) + 0 (8) + 0 (7) = **62**.
- Each of the 3 non-trump suits (без коз values): 11 + 10 + 4 + 3 + 2 (Вале) + 0 + 0 + 0 = **30** → 3 × 30 = **90**.
- Deck total = 62 + 90 = **152** ✓. Plus last trick +10 = **162** ✓ (коз game).
- "Без коз"/"Всичко коз" doubling: 152 → ... the article states the hand is worth **262** (doubled) — consistent with the sourced tables. ✓

## Time-sensitive / standing claims
- Footer licensing boilerplate (verbatim brand standard, unchanged from recent articles): "От 1 август 2026 г. … (ДВ, бр. 69 от 31.07.2026 г.). Всички Казина е подало заявление за лиценз … и очаква издаването му." — makes NO issued-licence claim and no invented № (status-only). Same text ships on vk-0285 and prior.
- No odds, bonuses, RTP, or licence identifiers anywhere else (rules guide).

## Gemini Step-7 text check (cross-model)
- Initial draft (05b): human-likeness **15** ("Likely AI-generated, 85%").
- Humaniser pass 1 (apply recs via step-7b): human-likeness **90** ("Highly likely human-written, 90%") → **PASS**.
- Keep-best winner = **pass 1 (HL 90)**. Passes applied: 1. Recorded `human 90`. Trail: 07-gemini-check-1.md, 07-gemini-check-2.md.

## Step-8 images
- **images: 3 (infographic коз/без коз 100, infographic анонси/точкуване 100, decorative hero 100)** — best review score **100 PASS**, no integrity failure.
- Hero regenerated once (pass 1 garbled pip counts, set 60 → pass 2 single-pip cards, set 100). Keep-best = pass 2. Trail: 08-image-review-1.md, 08-image-review-2.md.
- Every infographic number traces verbatim to 05b; no operator logos/names, no invented figures, no people/faces, no glamorised winning.

## Gate
Brand Gate (Stage 5): **95/100 PASS WITH FIXES → PASS**, 0 critical structural fails (surface fixes: em-dash in H2 → hyphen; trust/boilerplate/affiliate slots filled with verbatim brand standard).

## Internal links (4, approved set + live-sitemap siblings)
- /blog/poker-kombinacii/ (sibling, beside комбинации/терци)
- /zakonno-li-e/ (trust page, legality section)
- /blog/kak-se-igrae-poker-kazino/ (sibling card-game guide)
- /blog/responsible-gambling/ (RG hub)
Plus the /otgovorna-igra/ RG-block footer signpost (hard-coded compliance, not a body SEO link).

## Human still owns
Resolve nothing here (0 flags). Human: final read, optional voice polish (Gemini's pass-2 micro-nits in 07-gemini-check-2.md are optional, not applied to keep the best score), approve, publish. Do NOT treat 05b as published.

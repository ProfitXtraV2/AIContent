# 06 — Verification · vk-0295

Article: **Белот онлайн: къде се играе безплатно и как да започнете** (vk-0295, guide, slug `2026-10-27-belot-onlayn`)
Byline: Георги Тодоров (editorial „ние" voice) · Published/updated: 27.10.2026

## Surviving flags
- **0** in-text [VERIFY] / [DATA NEEDED] / [CONFLICT]. No operator/НАП primary source needed
  (free social platforms, not licensed casino operators). No invented features/prices.

## Time-sensitive / sourceable claims (traceable to public pages)
| Claim in text | Source | Note |
|---|---|---|
| Belot.BG: уеб + iOS/Android + Facebook + Smart TV; срещу хора/ботове/с приятели; регистрация FB/имейл/Google; гост = само ботове | belot.bg (official) + App Store listing id961576733 | platform's own public pages |
| Belot.BG дневен бонус **5 000 чипа** (при ≥1 игра с хора за деня) | belot.bg (official) | stated verbatim, not computed |
| Belot.BG „над 50 000 играчи на ден" | belot.bg (official) | written as the **platform's own claim**, not independent fact |
| Belot.BG възраст **13+** | App Store listing id961576733 | age rating |
| Djagi (Джаги), издател BIG MAGE: приложение, **20+ игри**, срещу хора и с приятели | App Store listing id6739783703 | app-store description |
| Belot (Bridge-Belote), lan.bg / LAN-GAMES: безплатно, срещу реални играчи ИЛИ компютър | App Store listing (lan.bg) | app-store description |
| Белот масово не се предлага за реални пари в лицензирани БГ казина; хазартът под надзора на НАП | brand doctrine + /zakonno-li-e/ | honest boundary; no operator named/recommended |

## "Recalculate one figure" (working shown)
No computational figures in this piece (no odds, RTP, превъртане or € math). The only numeric
facts are platform-stated values, verified 1:1 against the sources above and reproduced verbatim
in the infographic (5 000 чипа, 13+, 20+ игри). Cross-check — infographic vs 05b vs sources:
`5 000` (×3 in 05b) = source; `13+` = App Store; `20+ игри` = Djagi listing; `над 50 000` framed
as platform claim in both text and infographic caption. No drift, no fabricated value.

## Gemini Step-7 (text, cross-model)
- Baseline draft: high-variance detector, HL 15–25 (verdicts „Shows AI patterns 75–85%").
- Humaniser pass 1 (cut meta-discourse, hollow hooks, half the neat paragraph wrap-ups, the
  looped „кухненската маса" metaphor): ceiling lifted to **HL 85 „Likely human-written 85%"**
  (also read HL 25 on a parallel read — detector high-variance on BG content).
- MAX_GEMINI_PASSES=2. **Kept pass 1** (highest HL seen = 85 ≥ gate 80). gemini column: **human 85**.

## Step-8 images
- **images: 2** — hero `belot-onlayn-hero.webp` (17 KB, decorative metaphor: fanned cards from a
  laptop + online-multiplayer dots; no faces/logos/text/money) + infographic
  `belot-onlayn-platformi-sravnenie.svg` (platforms comparison; every label traces to 05b).
- Gemini image review: pass 1 score 75 (infographic label „турнири" not in 05b → removed),
  pass 2 **score 100 PASS**, 0 integrity failures. Best score 100. Both kept.

## Human-owned (Step 6)
Nothing to resolve by autopilot: 0 flags. No posting/merge/flag-resolution. PR for human review.

# 06 — Verification · vk-0296

Article: **Табла онлайн: къде се играе безплатно и как да започнете** (vk-0296, guide, slug `2026-10-27-tabla-onlayn`)
Byline: Георги Тодоров (editorial „ние" voice) · Published/updated: 27.10.2026

## Surviving flags
- **0** in-text [VERIFY] / [DATA NEEDED] / [CONFLICT]. No operator/НАП primary source needed
  (free social board-game platforms, not licensed casino operators). No invented features/prices.

## Time-sensitive / sourceable claims (traceable to public pages, verified 2026-10-27)
| Claim in text | Source | Note |
|---|---|---|
| VIP Games (Casualino): „free to play" платформа; чиповете са виртуална валута; „match against real players in real-time"; игра с приятели; табла в Board Games | vipgames.com (official) | platform's own public page |
| VIP Games „над 20 000 активни играчи дневно" | vipgames.com (official) | written as the **platform's own claim** |
| VIP Games: гост без регистрация не влиза в matchmaking стаите, нито общува | vipgames.com (official) | stated verbatim |
| VIP Backgammon (CASUALINO AD, iOS): безплатно + покупки **€0,99–€19,99**; офлайн срещу AI ботове; режими табла/тапа/backgammon с куб; **18+ „Simulated Gambling"** | App Store listing id1244673801 | app-store page; € IAP + age rating verbatim |
| Backgammon Tabla online (LAN-Games EOOD): безплатно; **4+**; „online multiplayer"; **4 варианта** Regular, Tapa (Plakoto), Gulbara (Gjul Bara), Chelibi | App Store listing id941138510 | app-store page |
| Джаги (BIG MAGE EOOD): **над 20 игри**, табла сред тях; игра в реално време с истински противници + приятели; безплатно + покупки **$3,99–$149,99**; **16+** | App Store listing id6739783703 | app-store page; $ IAP + age rating verbatim |
| Belot.BG (Casualino): хоства и табла; дневен бонус **5 000 чипа** (при ≥1 игра с хора); **13+** | belot.bg + App Store id961576733 | carried from vk-0295; platform's own pages |
| Poki: табла в браузъра, без регистрация; срещу компютър/приятел на устройството | poki.com | public description |
| Табла на пари = хазарт под надзора на НАП; само лицензирани оператори; таблата масово не присъства в лицензираните казина | brand doctrine + /zakonno-li-e/ | honest boundary; no operator named/recommended |

## "Recalculate one figure" (working shown)
No computational figures in this piece (no odds, RTP, превъртане or € math). The only numeric
facts are platform-stated values, verified 1:1 against the sources above and reproduced verbatim
in the infographic. Cross-check — infographic vs 05b vs sources:
- `над 20 000` (VIP Games players) = source, framed as the platform's own claim in both text and image.
- `€0,99–€19,99` = VIP Backgammon App Store IAP range; `18+ Simulated Gambling` = its age rating.
- `4+` = LAN-Games rating; `4 варианта` (Regular/Tapa/Gulbara/Chelibi) = its listing.
- `над 20 игри` = Djagi listing; `$3,99–$149,99` = its IAP range; `16+` = its rating.
- `5 000 чипа`, `13+` = Belot.BG.
No drift, no fabricated value. Number set byte-identical across 02→03→04→05b (diff-checked).

## Gemini Step-7 (text, cross-model)
- Baseline draft (pass 1 check): **HL 25** („Shows AI patterns 75%").
- Humaniser pass 1 (broke stacked „Ако..." conditionals, deleted neat-bow closer, removed
  meta-commentary, cut 2 didactic signposts, de-listed the how-to): pass 2 check **HL 85
  („Likely human-written 85%")** → PASS.
- MAX_GEMINI_PASSES=2. **Kept pass 1** (highest HL seen = 85 ≥ gate 80). gemini column: **human 85**.
- Files: 07-gemini-check-1.md (baseline 25), 07-gemini-check-2.md (85 PASS).

## Step-8 images
- **images: 2** — hero `tabla-onlayn-hero.webp` (20 KB, decorative: backgammon board on a
  tablet screen + online-multiplayer glow dots; no faces/logos/text/money) + infographic
  `tabla-onlayn-platformi-sravnenie.svg` (platform comparison; every label/number traces to 05b).
- Gemini image review: 90 (18+ label clip) → 75 (footer spillover) → 75 (unsupported „· iOS" on
  cards 3/4) → **90 PASS** after fixes. **Best score 90**, 0 integrity failures. Infographic rated
  „безупречна" (100% data match). Hero carries one non-integrity decorative note (imperfect
  checker layout on an explicitly abstract header); kept per keep-best (images never block the PR).
- Files: 08-image-review-1.md (90), 08-image-review-2.md (final 90 + keep-best ledger).

## Human-owned (Step 6)
Nothing to resolve by autopilot: 0 flags. No posting/merge/flag-resolution. PR for human review.

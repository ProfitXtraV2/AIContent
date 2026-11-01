# 06 — Verification · vk-0297

Article: **Проверка на фиш Тото: как да проверите печалба онлайн, в приложението и на гише**
(vk-0297, guide, slug `2026-10-27-proverka-na-fish`)
Byline: Георги Тодоров (editorial „ние" voice) · Published/updated: 27.10.2026

## Surviving flags (STAY IN THE TEXT for human Step 6 — not resolved by autopilot)
- **4 [VERIFY]**, all pointed at a primary source, none fabricated:
  1. [VERIFY] whether the „Спорт Тото" app checks a specific фиш in-app (scan/manual) vs. only results.
  2. [VERIFY] prize-size threshold above which a win is paid at централа instead of any тото пункт.
  3. [VERIFY] exact prize-claim deadline (срок за получаване) — only a stale 2013 „weeks"-order datum exists.
  4. [VERIFY] the пункт-issued бон as the valid payout document (2013 source — confirm current rule).
- Plus a TAX [VERIFY] handled verbatim brand-doctrine (lottery-winnings tax → счетоводител/НАП, no figure).
- **0** [DATA NEEDED]/[CONFLICT]. No draw numbers or jackpot sums printed (brand doctrine).

## Time-sensitive / sourceable claims (traceable to public pages, verified 27.10.2026)
| Claim in text | Source | Note |
|---|---|---|
| Онлайн „Проверка на фиш" е отделна форма за всяка игра: 6 от 49, 6 от 42, 5 от 35, Зодиак, Рожден ден | info.toto.bg (/check/6x49, /6x42, /5x35, /zodiak, /rojdenden) | official site |
| На формата маркирате числата **по области** + избирате **ТИРАЖ**, после „ПРОВЕРИ ФИШ" / „Изчисти"; абонамент → последния включен тираж | info.toto.bg/check/6x49 | verbatim instructions on the page |
| Няма баркод/QR/сериен номер — ръчно въвеждане | info.toto.bg/check/6x49 | stated/observed on the form |
| Системен фиш → поле „СИСТЕМА"; Джокер се проверява с номера на фиша | info.toto.bg/check/6x49 | official site |
| Официални резултати/печеливши групи по тиражи на `/results/<game>`; моментни игри — отделна проверка на toto.bg | info.toto.bg | official site |
| Втори тото шанс = жребий между касовите бележки, обявяван официално | info.toto.bg + carried vk-0268 | not a number check |
| Официално приложение „Спорт Тото" за Android/iOS, линкнато от info.toto.bg | info.toto.bg | app-check capability → [VERIFY] |
| На гише терминалът проверява фиша; пунктовият бон = документ за изплащане | Capital.bg 2013 | HISTORICAL → [VERIFY current] |
| Печалба над праг → централа; срок за получаване | Capital.bg 2013 (45 дни, стар) | both → [VERIFY] (no number asserted) |

## "Recalculate one figure" (working shown)
No computational figures in this piece — no odds, RTP, превъртане or € math. The only literal
numbers are game names (6 от 49, 6 от 42, 5 от 35) and the footer RG line/date, reproduced
verbatim. Infographic ↔ 05b cross-check: every infographic label traces to a 05b sentence
(online по области + тираж; no баркод/QR; безплатно/без акаунт; „СИСТЕМА"; „Спорт Тото"
Android/iOS; терминалът чете фиша; пазете фиша чист и здрав; пунктов бон = документ за
изплащане; info.toto.bg /results/; моментни → toto.bg; Втори тото шанс = жребий). No number
introduced that the text does not state. Number set byte-identical 02→03→04→05b (diff-checked).

## Gemini Step-7 (text, cross-model)
- Baseline draft (check 1): **HL 15** („Shows AI patterns 85%") — over-hedging around [VERIFY] +
  meta-commentary on not printing numbers + metaphor heading.
- Humaniser pass 1 (killed „не твърдим…" over-hedging, removed „няма да ги изписваме/нарочно не
  ги преписваме" meta-commentary, neutralized heading → „Цената на играта и отговорността"):
  check 2 **HL 90 („Likely human-written 90%")** → PASS.
- MAX_GEMINI_PASSES=2. **Kept pass 1** (highest HL = 90 ≥ gate 80). gemini column: **human 90**.
- Files: 07-gemini-check-1.md (15), 07-gemini-check-2.md (90 PASS + keep-best ledger).

## Step-8 images
- **images: 2** — infographic `proverka-na-fish-tri-nachina.svg` (3-method comparison; every label
  traces to 05b) + decorative hero `proverka-na-fish-hero.webp` (16.5 KB, 1200×670: paper ticket +
  magnifier + check mark; no faces/logos/numbers/money/euphoria).
- Gemini image review: **100/100 PASS** pass 1, **0 integrity failures**. Infographic 100% data
  match; layout clean (0 overlaps, no clipping). **Best score 100.**
- Files: 08-image-review-1.md.

## Human-owned (Step 6)
Resolve the 4 [VERIFY] (app check; централа threshold; claim срок; пункт-бон rule) + the tax
[VERIFY] against БСТ primary sources / official game rules before publish. No posting, no merge,
no flag-resolution by autopilot. PR for human review.

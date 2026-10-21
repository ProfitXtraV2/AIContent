# 06 — Verification (for the human reviewer, Step 6)

Article: **Електронна рулетка: как работи (RNG и автоматни рулетки)** (vk-0280)
Type: guide · Byline: Георги Тодоров · Date: 14.10.2026 · Scope: guides-only (no operator/НАП-register data)

## Surviving flags
**NONE.** 0 × [VERIFY], 0 × [DATA NEEDED], 0 × [CONFLICT]. Every figure traces to a reachable
source (Wikipedia roulette math + the НАП/ЗХ source pack); none depends on geo-blocked operator
T&C or the НАП register. No specific-operator or named-product RTP was used, so nothing was
fabricated and nothing needs a flag.

## Time-sensitive / checkable claims + primary sources

### A. Roulette math (evergreen; derivable — show the working)
Source: https://en.wikipedia.org/wiki/Roulette (canonical house-edge figures), cross-checked by derivation.
- **Европейска (едно зеро), домашно предимство 2,70% / RTP 97,30%.** Recalc:
  single-number bet pays 35:1; true chance 1/37. EV per 1 unit staked =
  (1/37)(+35) + (36/37)(−1) = (35 − 36)/37 = −1/37 = **−0,027027 = −2,70%** → RTP = 36/37 = **97,2973% ≈ 97,30%**. ✓
  Fair (zero-edge) payout would be **36:1** (36 losing numbers to 1 winner); the casino pays **35:1** and keeps the 1-unit gap — this IS the edge. ✓
  Worked example in text: 2,70% × 100 € = **2,70 €** held on average, long-run. ✓
- **Американска (две зера), 5,26% / RTP 94,74%.** Recalc: edge = 2/38 = **5,2632% ≈ 5,26%**; RTP = 36/38 = **94,7368% ≈ 94,74%**. US/EU ≈ 1,95× → "почти се удвоява". ✓
- **Френска „la partage", ≈1,35% на равните залози.** Recalc: on even-money bets the zero returns half → edge = (1/37)×½ = 1/74 = **1,3514% ≈ 1,35%**. ✓ (applies ONLY to червено/черно, чет/нечет, 1–18/19–36.)

### B. BG legal + RG frame
Source: VsichkiKazina/source-packs/nap-gambling-law-and-rg-2026-10-10.md (ЗХ consolidated to ДВ бр. 69/31.07.2026; НАП RG pages).
- Рулетката = игра в игрално казино; **чл. 41, ал. 1 ЗХ** — начинът/техническите средства не променят вида на играта (онлайн/електронна = игра в казино). ✓ [human: confirm ал. wording in consolidated ЗХ]
- Онлайн лиценз **чл. 6 ЗХ** — софтуер/ЦКС през регистрирана лаборатория + вписване в регистър + реално-времево подаване към сървър на НАП. ✓ (current-law term „регистрирана лаборатория", NOT „БИМ")
- Нелицензирани сайтове: от **01.08.2026** достъп спрян с решение на НАП до **24 часа** (**чл. 17, ал. 6 ЗХ**); играч санкциониран с глоба **500–2000 лв.** (**чл. 9, ал. 14** във връзка с **чл. 97а, ал. 2 ЗХ**). ✓ [human: these are the resolved values used across vk-0271/0279; re-confirm if the ЗИД bill status changed after 23.10.2026]
- RG: бюджет ≤ **5%** от нетния доход; **регистър на уязвимите лица (чл. 10г ЗХ)**; линия „Солидарност" **0888 99 18 66**. ✓

### C. Game mechanics (evergreen, non-operator)
- RNG independence (each spin independent, no memory); auto/airball = physical wheel + air/mechanical ball release + sensors, no dealer; live casino = human dealer (distinct). General casino-game knowledge; no specific provider figure claimed. ✓

## Numbers diff across stages
Synthesis → Author → Humaniser → SEO → Gate → 5b: every figure preserved exactly. One SME
addition in Author (fair payout **36:1** vs paid 35:1) is mathematically correct (see A) and
was verified by the Brand Gate maths recalc — not a corruption.

## Gemini Step-7 (text)
Pass 1 / baseline: **"Likely human-written, 80%"** → human-likeness **80 ≥ 80 → PASS**. No Humaniser
pass applied; baseline 05b is keep-best (highest HL seen). `07-gemini-check-1.md` holds the verbatim
verdict + style recs (not applied — PASS reached; style-only; human may optionally apply).

## Step-8 images
**2 images, both Gemini-review 100/100 PASS** (`08-image-review-1.md`):
- `images/domashno-predimstvo-po-vid-ruletka.svg` — house-edge infographic; every number verbatim from 05b.
- `images/elektronna-ruletka-rng-hero.webp` — textless RNG/circuit metaphor hero (24,2 KB).
No fabricated logos/numbers/people/glamorised winning.

## Human to do at Step 6
1. Confirm the ЗХ article wordings in B against the consolidated law (same citations already used in vk-0271/0279).
2. Optionally apply Gemini's style recs from `07-gemini-check-1.md` (style-only; PASS already at 80).
3. Nothing else blocks — 0 flags, gate PASS 96/100, images PASS.

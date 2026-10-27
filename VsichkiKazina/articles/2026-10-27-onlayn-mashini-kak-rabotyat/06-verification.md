# 06 — Verification — Онлайн машини: как работят слотовете (vk-0294)

**Date:** 2026-10-27 · **Type:** guide (game-mechanics explainer) · **Byline:** Георги Тодоров

## Surviving flags
- **0** `[VERIFY]` / `[DATA NEEDED]` / `[CONFLICT]` flags in 05b.
- Guides-only scope held: NO operator T&C figures, NO НАП-register data, NO specific-operator/slot exact RTP asserted as fact. All RTP figures framed as типични/примерни диапазони and labelled („Диапазонът е примерен").

## Time-sensitive / factual claims + primary sources (general-education, non-operator)
All slot-mechanics facts are evergreen/general and sourced from reachable educational references (NOT geo-blocked BG operator/НАП pages):
- RNG makes each spin independent; fairness tested by independent labs (eCOGRA, iTech Labs).
  Source: https://untamedscience.com/blog/online-casino-slot-mechanics-rtp-rng-volatility-house-edge/ · https://gauravtiwari.org/rng-rtp-code-behind-online-slots/
- RTP = theoretical long-run return (averaged over very large spin counts, often 1M+); 96% ≈ €96 per €100 over the long run; house edge = 100% − RTP.
  Source: https://www.track360.io/glossary/slot-rtp · untamedscience (above)
- Typical online-slot RTP ~92–97% (most 95–97%); progressive jackpots lower (~92–94%) because part of each stake feeds the jackpot pool. Presented as типичен/примерен диапазон.
  Source: https://www.track360.io/glossary/slot-rtp (corroborated by general industry consensus; labelled illustrative in copy).
- Volatility (low/high) describes payout evenness; same RTP feels different. Qualitative only — no fabricated figures.

## Recalculated figure (working shown)
- **House edge from RTP:** 100% − 96% = **4%** → on €100 turnover the house keeps €100 × 0.04 = **€4**, player gets back €96. ✓ (matches 05b)
- Cross-check with the 94% example: 100% − 94% = **6%** → €100 × 0.06 = **€6**. ✓ (matches 05b)
- No other numbers invented; „243 начина" and „над милион" симулирани завъртания are illustrative/standard and carried verbatim through all stages (number-diff clean author→humaniser→SEO→05b; the only tokens removed between stages were scaffolding `/10` and `[18+ / RG LINE]`).

## Gemini Step-7 (text, human-likeness) — keep-best
| version | verdict | human-likeness |
|---|---|---|
| baseline 05b | Shows AI patterns, 75% | 25 |
| humaniser pass 1 | Shows AI patterns, 80% | 20 |
| **humaniser pass 2 (KEPT)** | **Likely human-written, 75%** | **75** |
- MAX_GEMINI_PASSES (2) reached; kept-best = pass 2 (HL 75, highest seen AND the only "human-written" verdict). HL 75 < 80 gate → handed to human reviewer (noisy detector: score moved 25→20→75, complaints relocated each pass). gemini column recorded as `ai 25` (winning verdict's complement scale). Facts/numbers/links/RG never touched (style-only). Audit: 07-gemini-check-1/2/3.md.

## Step-8 images
- images: **3** — hero (onlayn-mashini-hero.webp, 22 KB) + RTP infographic (rtp-domashno-predimstvo.svg) + volatility diagram (volatilnost-niska-visoka.svg).
- Gemini visual review: **100/100 PASS**, first pass, 0 integrity failures; every infographic number traces 1:1 to 05b; hygiene clean (no logos/faces/fake UI/glamorised winning); SVG layout verified (Chromium render) — no overlap/clipping. Audit: 08-image-review-1.md. Hero WebP conversion done via Chromium canvas (Pillow `_imaging` unavailable in env).

## Brand Gate
- Gate PASS **89/100**, 0 critical flags (05-gate-report.md). Byline Георги Тодоров; brand not in body (allowed), byline-only; 5 internal links from approved set (1 money page `/slot-igri/visok-rtp/`); RG line verbatim.

## Internal links (5, all from approved set / live sitemap 2026-10-27)
/blog/proverka-licenz-kazino/ · /slot-igri/visok-rtp/ (money) · /blog/linii-na-pechalba/ · /blog/progresivni-dzhakpoti/ · /otgovorna-igra/ (RG)

## Anti-cannibalization
Head pillar for the „онлайн машини / слот машини" cluster. No existing article owns it (`/slot-igri/` is a money/listing page, linked not duplicated). RTP/volatility/paylines/jackpots each held to ~one section and linked OUT to the dedicated pages — no second RTP/paylines/jackpots pillar created.

## Outcome
Drafted → PR. Flags left in text (0 here). Nothing posted/merged; no flag resolved. Human owns Step 6 + publishing.

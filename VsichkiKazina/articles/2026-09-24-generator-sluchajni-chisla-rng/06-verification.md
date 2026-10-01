# 06 — Verification (for the human) · vk-0167
Article: „Генератор на случайни числа (RNG): как казино игрите постигат случайност" · type guide · byline Георги Тодоров (editorial voice) · 24.09.2026.
STOP: 05b-final-draft.md is NOT publishable until the human resolves the flag below and says „verified".

## SURVIVING FLAGS (stay in the text until confirmed against a primary source)
1. **[VERIFY] iTech Labs ISO/IEC 17025 & 17020 accreditation** (Section „Кой проверява, че генераторът наистина е случаен").
   - Claim in text: „iTech Labs пък е акредитирана по стандартите ISO/IEC 17025 и ISO/IEC 17020".
   - Primary source to check: iTech Labs' own site (https://www.itechlabs.com/ → About / Accreditation). Secondary corroboration seen in research: safeonlinecasino-uk.com article on eCOGRA/iTech/GLI testing.
   - Current status from research: multiple third-party references state iTech Labs holds ISO/IEC 17025 and 17020 accreditation, but the exact scope/certificate was not confirmed from the lab's own page during drafting. Confirm on the lab page, then the human may drop the flag (or keep the standard names but soften „акредитирана" if the scope differs).

## TIME-SENSITIVE / SOURCEABLE CLAIMS (no flag, but confirm before publish)
- „eCOGRA работи по методология, призната от регулатори като британския, нидерландския и испанския." → confirm on eCOGRA's site (https://ecogra.org/ — jurisdictions/approvals). Research source: ecogra.org RNG-testing page (fetched 24.09.2026). Regulator lists can change.
- Lab names GLI / eCOGRA / iTech Labs / BMM Testlabs as independent RNG testing labs → widely documented; stable. Sources: softswiss.com KB, next.io guide, ecogra.org.
- Concept facts (PRNG deterministic-from-seed; TRNG physical entropy; RNG runs continuously; independence of outcomes / gambler's fallacy; RNG≠RTP) → concept-level, corroborated across softswiss.com KB + bgaming + next.io. No operator/НАП data used.

## RECALCULATION (one figure, working shown)
Illustrative RTP example (marked примерни in text + infographic):
- Stake total €1000, RTP 96% → expected return = €1000 × 0.96 = **€960**.
- House edge = €1000 − €960 = **€40** = 40/1000 = **4%**.
Internally consistent; matches 05b body and rng-vs-rtp-primer.svg exactly.

## COMPLIANCE SPOT-CHECK
- Byline Георги Тодоров ✓ · brand „Всички Казина" exact ✓ · verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." ✓ (body + footer).
- RG block: /otgovorna-igra/ + национален регистър на уязвимите лица (НАП, самоизключване) + Солидарност 0888 99 18 66 (делнични дни 10:00–17:00) ✓.
- Zero em-dashes ✓ · no banned promise/hype/AI connectives ✓ · currency € ✓ · dates DD.MM.YYYY ✓.
- No tax claim asserted (none needed) ✓ · no operator recommended → no affiliate link, affiliate footer intentionally omitted ✓ · no invented licence № ✓.
- Internal links (live sitemap 24.09.2026): /slot-igri/visok-rtp/, /blog/games-providers/, /blog/rechnik-kazino-termini/, /otgovorna-igra/ ✓.

## EXTERNAL CHECK (Gemini, Step 7)
Model gemini-3.1-pro-preview. 3 checks + 2 fresh Humaniser passes (step-7b). Human-likeness: v0=25, v1=15, v2=15. KEEP-BEST = v0 (25). Detector stuck ~85% AI for this concept-explainer shape (noisy over-editing case flagged by the Step-7 policy); every untouchable preserved across passes. Verdict logged for human; below the 80 target — human may accept as-is or request a further manual voice pass.

## IMAGES (Step 8)
3 images, all referenced from 05b. Best Gemini image review = **100/100 PASS** (pass 2, after a clipPath layout fix). No integrity failure, no fabricated numbers/logos, no drops. Hero: generator-sluchajni-chisla-rng-hero.webp (decorative). Infographics: seed-algoritam-izhod-rng.svg, rng-vs-rtp-primer.svg (all numbers trace to 05b).

## HUMAN ACTION LIST
1. Resolve flag #1 (iTech Labs ISO accreditation) against the lab's own page; drop the flag if confirmed.
2. Confirm the eCOGRA jurisdictions line is still current.
3. Decide whether the Gemini human-likeness score (25, below 80) warrants a further manual voice edit, or accept v0.
4. Fill the [About Всички Казина boilerplate] slot with the standard block, then say „verified" to publish.

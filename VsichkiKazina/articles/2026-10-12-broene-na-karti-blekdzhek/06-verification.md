# 06 — Verification — „Броене на карти в блекджек: работи ли и защо не онлайн"

Type: guide (neutral game-mechanics + math explainer, card-counting intent). Byline: Георги Тодоров (editorial voice).
Scope: NO operator facts, NO licence/bonus data, NO НАП register lookup, NO affiliate link. Facts from international
game-mechanics + blackjack-math references (reachable), not from geo-blocked BG operator pages. Flags STAY in the text
for the human (Step 6). Body ~1,300 words + boilerplate, 0 em-dashes.

## SURVIVING FLAGS (5 — publish-blocking until the human resolves them)
1. **[VERIFY] Едуард Торп, „Beat the Dealer", 1962** — card counting is proven maths, originated by Thorp.
   · Source: https://en.wikipedia.org/wiki/Beat_the_Dealer and https://en.wikipedia.org/wiki/Edward_O._Thorp
     („Beat the Dealer", first ed. 1962, first mathematically-proven card-counting system). Canonical fact; confirm
     year/edition. The article keeps it generic („още преди десетилетия").
2. **[VERIFY] Домашно предимство ~0,5% при 4+ тестета и стандартни правила** (section „Колко голямо е предимството").
   Rule-dependent (S17/H17, double-after-split, surrender, брой тестета).
   · Source: https://en.wikipedia.org/wiki/Card_counting („blackjack played with a perfect basic strategy offered a
     house edge of less than 0.5%"); Las Vegas Advisor / Arnold Snyder column (≈ −0,5% at 4+ decks). Time-insensitive
     but rules-dependent; human confirms the exact % for the rule set the article's reader faces.
3. **[VERIFY] ~0,57% при осем тестета.**
   · Source: Las Vegas Advisor / Snyder deck-count table (≈ −0,57% at 8 decks, standard Strip rules). Single secondary
     source; confirm.
4. **[VERIFY] ~1% предимство на опитен брояч при шест тестета и правилно вариране на залога.**
   · Source: https://en.wikipedia.org/wiki/Card_counting („A typical card counter who ranges bets appropriately in a
     game with six decks will have an advantage of approximately 1%"). Rule/penetration-dependent; confirm.
5. **[VERIFY] Общо право на оператор в България да откаже обслужване на играч, който брои** (section „Законно ли е").
   Kept GENERAL, no operator/licence named (guides-only scope). The international point — counting in one's head is not
   a crime, but a casino is a private business and may refuse service — is sourced to
   https://en.wikipedia.org/wiki/Card_counting (legality section). Human to confirm the precise BG-specific wording
   (private-premises access right) from a reachable BG legal source before publish, or soften to the general statement.

## OTHER CLAIMS TO SPOT-CHECK (sourced, not flagged)
- Hi-Lo card values (2–6 = +1; 7,8,9 = 0; 10,J,Q,K,A = −1), balanced level-1 count summing to 0; true count = running
  count ÷ decks remaining; penetration „almost directly" affects exploitable advantage; CSMs „essentially force minimal
  penetration" and „greatly reduce the advantage"; most online casinos reshuffle at the start of each round so the house
  retains its edge; counting in the head (no device/helper) is legal in Western jurisdictions, casinos may still ban/refuse.
  · https://en.wikipedia.org/wiki/Card_counting (fetched 2026-10-12).
- Dispersion / variance point (a counter can play perfectly and still lose for long stretches; the edge shows over a very
  large number of hands): standard blackjack math, consistent with the ~1% edge + high standard deviation.
- No specific operator, licence №, bonus, RTP, or НАП-register claim is made anywhere (correct for guides-only scope).

## FIGURE CHECK (recalculation with working shown)
- **Hi-Lo balances to 0 (52-card deck):** ranks 2,3,4,5,6 = 5 ranks × 4 suits = 20 cards at +1 → +20;
  ranks 10,J,Q,K,A = 5 ranks × 4 = 20 cards at −1 → −20; ranks 7,8,9 = 12 cards at 0 → 0.
  Sum = +20 − 20 + 0 = **0** ✓ (balanced level-1 count, as stated).
- **True count:** running +6 ÷ 3 неизиграни тестета = **+2** ✓ (matches text + infographic).
- **Edge in euros (per €100 staked):** house 0,5% × €100 = **€0,50** average loss ✓; counter 1% × €100 = **€1** in the
  player's favour ✓; 8-deck house 0,57% × €100 = €0,57 (text rounds the €-example to the 0,5% case; consistent).
- Proportional honesty in the infographic: the counter bar (280px, ~1%) is exactly twice the house bar (140px, ~0,5%).

## GEMINI STEP-7 (text, cross-model)
- check 1 (initial 05b): „Shows AI patterns, 75%" → human-likeness **25** → humaniser pass 1 (7b) + quick Brand-Gate
  re-check. check 2: „Shows AI patterns, 85%" → HL **15** (worse). humaniser pass 2 (7b) + re-check. check 3: „Cyborg/
  Hybrid, 70% confidence of AI origins" → HL **30**. MAX_GEMINI_PASSES (2) reached.
- **Keep-best:** pass 2 (HL 30) > initial (25) > pass 1 (15) → final 05b = pass 2 (current file). content-queue `gemini`
  = **`ai 70`** (winning version's own verdict scale, 100 − HL). Detector is noisy and relocates goalposts each pass
  (standard for neutral math-dense explainers; cf. vk-0063, vk-0266). Facts, flags, RG, disclosures untouched throughout.
  **Human editor attention advised** (the piece is below the 80 human-likeness target). See 07-gemini-check-1/2/3.md.

## IMAGES (Step 8)
- images: 2 (infographic 100, hero 100) — Gemini image review PASS, no integrity/layout issue. See 08-image-review-1.md.
  · `images/broene-na-karti-predimstvo-i-zashto-onlajn-e-nula.svg` — hand-authored infographic; every figure traced
    verbatim to 05b (Hi-Lo +1/0/−1, true count +6÷3≈+2, 0,5%/0,57%/1%, €0,50/€1 per €100, penetration live vs online=0);
    rendered to PNG via headless Chromium and eyeballed (no overlap/clip/edge-touch); carries the 18+ RG line.
  · `images/broene-na-karti-pamet-na-testeto-hero.webp` — decorative AI hero (gemini-3-pro-image, 30.3 KB WebP < 100 KB);
    textless visual metaphor (deck memory-trail dissolving + shuffle loop); no logos/faces/UI/glamorised winning.

## BRAND GATE
- PASS WITH FIXES: input 85/100 (Personality 19 · Tone 14 · E-E-A-T 16 · Trust 9 · Lang&Style 15 · RG 12) → **97/100**
  after fixes (dates, „проверени към" line, About boilerplate, author bio, affiliate-licensing footer, RG block with
  национален регистър + Солидарност). 0 CRITICAL remaining. No maths error. 0 em-dashes.
- Internal links (body, 4 from approved set): /kazino-igri/blakdzhak/, /kazino-igri/, /kazino-igri/kazino-na-zhivo/,
  /otgovorna-igra/ (+ /kak-ocenyavame/ in the brand boilerplate). All present in the live sitemap 2026-10-12.

## HUMAN ACTIONS BEFORE PUBLISH
Resolve the 5 [VERIFY] flags (Thorp 1962; the three rule-dependent edge %; BG operator-refusal wording). Confirm the
guide reads correctly for the BG reader on the legality point. Give the text one editor pass for human-likeness (Gemini
`ai 70`). Do NOT publish with live flags.

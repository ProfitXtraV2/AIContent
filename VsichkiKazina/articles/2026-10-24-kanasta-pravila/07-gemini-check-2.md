# 07 — Gemini check, pass 2 (after humaniser pass 1)

Model: gemini (scripts/gemini_check.py) · run 24.10.2026 on 05b-final-draft.md after step-7b humaniser pass 1.

## Verdict (verbatim)
**Verdict: Shows AI patterns, 75% confidence.**

Normalised human-likeness = 100 − 75 = **25** (up from 10 at initial). Still < 80 → one more humaniser pass (pass 2 = MAX_GEMINI_PASSES).

While the Bulgarian phrasing is generally natural and uses correct terminology for the game, the article's underlying skeleton relies heavily on classic LLM structural tropes: forced conversational hooks, blatant signposting, staccato "rule of three" rhythms, and defensive hedging.

### 1. The "Engaging" Metaphorical Intro
Quote: "Дотам се върви през няколко раздавания, не с едно сполучливо тесте."
Recommendation: Delete this sentence entirely. The preceding sentence already explains the 5000-point goal; the poetic filler is not needed.

### 2. Signposting / Forward Referencing
Quote: "Червените тройки са отделен случай, с много по-тежко тегло; за тях малко по-надолу."
Recommendation: Remove the signpost ("за тях малко по-надолу"). State that red threes are a special case with different scoring and let the reader reach the dedicated H2.

### 3. Staccato Rhythm / The "Rule of Three"
Quote: "Теглиш, по избор мелдваш, изхвърляш."
Recommendation: Expand into a natural, fluid sentence describing the turn as a continuous action (draw a card, optionally meld, conclude by discarding).

### 4. Defensive Hedging / Over-clarification
Quote: "Числата 110 и по-високите цели идват от различни справочници, не от едно задължително правило за всяка маса."
Recommendation: Cut this sentence. The H2 is "Разновидности" and the bullets already state these are alternatives.

### 5. Formulaic Transition to Legal/RG Content
Quote: "Обичате ли игрите с карти, вижте и правилата на баккара." (followed by the RG warning).
Note: Per hard rules, DO NOT touch/alter the RG language, 18+ markers, internal links, author bio, or brand boilerplate. Structural observation only; leave exactly as is.

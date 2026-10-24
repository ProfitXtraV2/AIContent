# 07 — Gemini external check, pass 1 (initial draft 05b)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-21-santase-pravila/05b-final-draft.md`
Exit: 0

## Normalized result
Verdict: **Likely human-written, 85% confidence** → **human-likeness = 85**.
PASS test: 85 ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS on pass 1 (initial draft)**.
Keep-best: initial draft is the highest (and only) version → KEPT as final 05b. No humaniser pass applied.
(Gemini's recommendations below are style-only; since the draft already passed ≥80, iterating risks
lowering the score under keep-best, so the initial version is kept unchanged. Recs preserved for the record.)

## Gemini verbatim verdict + recommendations
**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This is a high-quality piece of writing. In Bulgarian, AI tends to default to highly formal, passive, and sterile language (e.g., "Важно е да се отбележи, че..."). This text, however, is full of natural, idiomatic phrasing, cultural card-game slang ("капак", "шнайдер", "шварц", "на две порции", "правилата стягат"), and excellent punchy sentences ("Шейсет и шестте се обявяват, не се случват сами").

However, there are a few structural seams that read like either light AI assistance or a human writer awkwardly fulfilling an SEO content brief. These specific patterns trigger AI/SEO-content detectors.

### Flagged Passages & Patterns

1. **Forced SEO Transition / Tangential Linking** — "Същата логика на силни комбинации от подредени карти ще срещнете и при [комбинациите в покера](/blog/poker-kombinacii/), макар там подреждането да върши друга работа." The "You will see the same logic in [Topic X], although [Topic Y]" formula shoehorns an internal link; comparing Santase's 20/40 declarations to Poker hands is a stretch.

2. **Didactic Signposting** — "Едно предупреждение, което лесно се пропуска:" / "Струва си да се каже направо:" — AI "throat-clearing" that slows the punchy rhythm.

3. **The "Neat Bow" Summary (Formulaic Structure)** — "Затова, преди да седнете срещу непознат противник ... да сверите четири неща: ..." — summarising the points just made in a neat symmetrical list.

4. **Word Echo / Repetition** — "Щом играта наближи края си или някой **затвори**, прозорецът за смяна се **затваря**." — repetitive root words in the same sentence.

### Concrete Recommendations
- Remove the comparative "same logic" framing on the poker link (or make it a brief parenthetical).
- Delete the signposting lead-ins; start directly with the core information.
- Break up the rigid "four things to check" list so it flows into the aphorism "Пет минути уговорка спестяват един спор по средата на играта".
- Change the sentence-final "се затваря" to a synonym ("приключва"/"отпада") to kill the echo.

*Note: Per instructions, the RG language, 18+ markers, legal disclosures and 2026 dates were ignored for stylistic critique and remain unchanged.*

## Decision
PASS at human-likeness 85 on the initial draft. Keep-best → initial 05b retained unchanged.
content-queue `gemini` column: `human 85`.

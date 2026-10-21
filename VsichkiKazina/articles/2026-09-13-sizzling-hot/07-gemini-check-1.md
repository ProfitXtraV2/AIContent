# 07 — Gemini external check, pass 1 (initial 05b) — Sizzling Hot

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py

**Verdict: Likely human-written (or heavily human-edited), 75% confidence.** → human-likeness = **75**. → below GEMINI_TARGET 80 → apply recs via fresh humaniser pass.

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 75% confidence.**

This article reads exceptionally well and features highly idiomatic Bulgarian phrasing ("Разчистено е до кокал", "няма да лепна") alongside deep, accurate contextual knowledge (distinguishing Novomatic's *Sizzling Hot* from Amusnet's *Burning Hot*). These are strong indicators of a human writer or a very meticulously prompted and edited AI.

However, there are a few lingering structural and rhetorical habits that commonly appear in AI-generated text, specifically the use of anaphora (repetitive sentence starters), prescriptive "preachy" advice, and philosophical framing of simple concepts. Additionally, an internal editorial tag has survived into the final draft.

### Flagged Passages & AI Patterns

**1. Pattern: Staccato Rhythm / Anaphora (The Rule of Three)**
- The text: "Няма wild символ. Няма безплатни завъртания. Няма бонус рунд, колело или мини-игра."
- Why it flagged: grouping three "Няма..." sentences in a row feels distinctly like an LLM trying to sound dramatic about a slot game's lack of features.

**2. Pattern: Philosophical Framing / Narrated Purpose**
- The text: "Заради тази оголеност играта е добър повод да се погледне какво всъщност плаща един слот, когато няма бонус механики, зад които да се скрие."
- Why it flagged: framing a basic fruit slot as a "good occasion to look at what a slot actually pays" is a classic AI thematic wrapper.

**3. Pattern: Prescriptive / Preachy Tone**
- The text: "По-полезно е да приемеш играта такава, каквато е: без прогресивен джакпот и без механика, която да натрупа множител в твоя полза през сесията."
- Why it flagged: telling the reader it is "more useful to accept the game as it is" crosses from objective reviewing into unsolicited advice.

**4. Process Issue: Surviving Editorial Tags**
- The text: "[VERIFY: точна максимална печалба на Sizzling Hot / коя версия]"
- Why it flagged: a placeholder/verification flag in the finished article. (Gemini: "Do not remove it yourself until the data is actually verified.")

### Concrete Recommendations
- Combine the repetitive "Няма" sentences into a single, fluid sentence.
- Trim the end of the introductory paragraph (end after "...пет барабана").
- Remove the instruction on how the reader should "accept" the game; state the facts plainly.
- Route the [VERIFY] tag to the editor before publishing (do NOT remove it).

## Decision
HL 75 < 80 → apply recs 1–3 in a fresh humaniser pass (07b/05b). Rec 4: KEEP the [VERIFY] flag — it is an untouchable process marker per pipeline rules (Gemini agrees not to remove it). All numbers/links/RG/18+/dates/byline/brand preserved. Re-run gemini_check after the pass; keep-best.

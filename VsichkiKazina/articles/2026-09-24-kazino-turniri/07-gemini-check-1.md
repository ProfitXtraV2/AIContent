# Gemini Step-7 external check — pass 1 (initial draft)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`

**Verdict: Shows AI patterns, 85% confidence.** → human-likeness = 100 − 85 = **15**

Excellent Bulgarian and accurate, but classic LLM structural rigidity: formulaic enumeration, robotic signposting, synthesizing transitions, overly philosophical metaphors.

### 1. Filler Openings & Metaphorical Framing
> *"Форматът е прост по замисъл."* → delete; start with the action ("Операторът обявява период...").
> *"Точката е валутата на турнира, а начинът, по който се начислява, определя кой печели."* → drop the "currency" metaphor; state the mechanic directly.
> *"Казино турнирът е най-честен със себе си, когато е freeroll..."* → reframe from the player's perspective (freeroll = most risk-free format), no personification.

### 2. Robotic Signposting & Meta-Commentary
> *"Пример прави схемата по-ясна (числата са примерни)."* → delete; jump straight into the example. (Keep the „примерни" label on the numbers elsewhere.)
> *"Разликата има значение:"* and *"Всеки модел възнаграждава различно поведение."* → cut the didactic transitions; let the contrast speak.

### 3. Formulaic Enumeration (First/Second/Third)
> *"Няколко неща решават... Първо... Второ... Трето... И най-важното:"* → break the ordinal structure; use narrative transitions or a genuine bullet list.

### 4. Synthesizing Summaries
> *"Общото между тях е, че времето или броят спинове са ограничени. Затова темпото натиска..."* → drop the "what they have in common" framing; state directly.

*Note (Gemini): RG language, 18+ warning, affiliate disclosure are perfectly placed and compliant — do not touch. Edits focus on structural flow of the H2 sections only.*

---
Decision: human-likeness 15 < 80 → apply step-7b Humaniser pass 1 (surgical; preserve every untouchable, keep „примерни" labels + all numbers verbatim). Keep-best tracked (initial HL 15).

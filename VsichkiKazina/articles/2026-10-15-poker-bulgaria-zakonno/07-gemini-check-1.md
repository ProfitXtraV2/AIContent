# 07 — GEMINI CHECK — pass 1 (baseline draft)

Command: python3 scripts/gemini_check.py 05b-final-draft.md
Normalized HUMAN-LIKENESS = 100 − 70 = **30** (verdict: Shows AI patterns, 70% confidence). Below target 80 → iterate (Humaniser pass applying recs).

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns (Hybrid / AI-assisted), 70% confidence.**

This article is highly factual, well-researched, and contains excellent localized legal citations. The core information reads like it was compiled by a human expert. However, the "glue" holding these facts together—the transitions, paragraph openers, and subheadings—relies heavily on classic LLM stylistic tropes. It reads like a human provided a detailed factual outline and asked an AI to "turn this into an article," or a human writer leaned on AI to polish their transitions. 

*(Note: The [VERIFY] tag, 18+ markers, and responsible gambling boilerplates were noted and are excellent process markers. Per your instructions, they have been completely ignored in the critique below and should remain exactly as they are).*

Here is the breakdown of the specific AI patterns detected and how to fix them.

### 1. The "Didactic / Preachy" Opener
**Flagged text:** *"Лицензът не е формалност на хартия."* (The license is not a formality on paper.)
**Pattern:** **Rhetorical Framing / Truism.** AI models love to open paragraphs by stating an obvious moral or practical absolute before delivering the actual fact. It creates a slightly patronizing, lecturing tone.
**Recommendation:** Delete this sentence entirely. Start the paragraph directly with the factual requirement: *"Чл. 6, ал. 1 изисква онлайн операторът да регистрира..."* This makes the text punchier and more authoritative.

### 2. The "Meta-Commentary" Transition
**Flagged text:** *"Оттук следва практическият извод."* (From here follows the practical conclusion.)
**Pattern:** **Signposting.** AI frequently tells the reader what it is about to do rather than just doing it. Human writers usually just state the conclusion.
**Recommendation:** Remove this sentence. The transition between the legal definition in the previous paragraph and the licensing requirement in the next paragraph is already logical; it doesn't need a signpost. 

### 3. The "Translated Idiom" Setup
**Flagged text:** *"Рискът при нелицензиран покер сайт обикновено се свежда до въпроса „ще ми изплатят ли печалбата". Законът гледа и от другата страна на екрана."*
**Pattern:** **Contrast Setup / Translated Metaphor.** AI often sets up a "common misconception" and contrasts it with a clever metaphor. "The other side of the screen" feels like a direct translation of an English AI prompt output, which sounds slightly unnatural in a Bulgarian legal context.
**Recommendation:** Cut the metaphor. You can keep the first sentence about the player's primary concern, but transition directly into the legal reality. For example, suggest changing the second sentence to simply state that the law penalizes the player as well.

### 4. The "Hyperbolic / Clickbait" Subheading
**Flagged text:** *"Данъци и частни игри - двата въпроса, които всички задават"* (Taxes and private games - the two questions everyone asks)
**Pattern:** **Formulaic Structure (The "Everyone is wondering" trope).** LLMs frequently use absolute statements ("everyone asks," "the ultimate guide") in H2s to simulate engagement. 
**Recommendation:** Change the H2 to be purely descriptive and objective, matching the dry, legal tone of the rest of the article. A simple "Данъчно третиране и статут на домашните игри" (Tax treatment and status of home games) would sound much more like a human expert.

### 5. The "Wrap-Up" Subheading and Rhythmic Summary
**Flagged text:** 
* *"Ако решите да играете"* (If you decide to play)
* *"Изводът е тесен, но ясен."* (The conclusion is narrow, but clear.)
**Pattern:** **The "In Conclusion" Variant / Staccato Rhythm.** AI struggles to end articles without a dedicated summary section. "If you decide to play" is a classic AI wrap-up header. "Тесен, но ясен" is a rhythmic, almost poetic staccato phrase that LLMs use to sound authoritative at the end of a text.
**Recommendation:** 
* Change the H2 to something more specific to the actual advice being given (e.g., focusing on budget or final checks). 
* Remove *"Изводът е тесен, но ясен."* and merge the core message directly into the text. Just state what legal poker means in Bulgaria without announcing that it is a "narrow but clear conclusion."
EXIT=0

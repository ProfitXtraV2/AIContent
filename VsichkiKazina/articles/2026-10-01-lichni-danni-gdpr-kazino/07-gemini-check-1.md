# 07-GEMINI-CHECK — pass 1 (initial draft) — lichni-danni-gdpr-kazino
# Model: gemini-3.1-pro-preview · run 2026-10-01 (3rd fire)
# Normalized human-likeness = 100 − 75 = 25 (Shows AI patterns, 75%). Below 80 → Humaniser pass (step-7b), re-check.

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While the article features excellent localization, accurate Bulgarian legal context (ЗЗЛД, КЗЛД, НАП), and a distinct first-person perspective ("Разписвам ги тук", "проверявам"), the underlying structural scaffolding heavily relies on classic Large Language Model (LLM) writing tropes. It reads like a "cyborg" text—a highly specific, human-directed prompt that generated a draft, which was then lightly edited, but the AI’s transitional phrases, rhythmic repetitions, and formulaic structures were left intact. 

Here is the breakdown of the specific patterns that triggered this assessment and how to fix them.

### 1. The "First, Second, Third" Formulaic Structure
**The Passage:** *"Данните падат в три групи. Първата е самоличността: име... Втората е финансовата: картата... Третата е поведенческата, която се трупа тихо..."*
**The Pattern:** Robotic enumeration. LLMs love to categorize concepts into exactly three buckets and introduce them with rigid, ordinal signposting ("The first is... The second is..."). It creates a stiff, textbook-like rhythm.
**The Recommendation:** Break the rigid numbering. You can either convert this into a fluid, single-sentence list, or use bullet points. For example, suggest blending them naturally: *"Казината събират няколко вида данни: базова самоличност (име, ЕГН), финансова информация за плащанията и поведенчески данни, които се трупат тихо на заден фон (история на залози, IP адрес)."*

### 2. The Classic AI Cliché Transition
**The Passage:** *"Тук е мястото, където очакванията често се разминават с реалността."*
**The Pattern:** Filler transition / The "Expectation vs. Reality" trope. This is one of the most common LLM transitional phrases across all languages. AI uses it to pivot from a general rule to an exception without actually adding informational value.
**The Recommendation:** Delete this sentence entirely. Start the paragraph directly with the substantive point: *"GDPR дава право на изтриване, но в хазарта то не е абсолютно. Правилата срещу изпирането на пари задължават..."* This makes the text punchier and more human.

### 3. Overuse of the "Not A, but B" Contrast
**The Passages:** 
* *"Причината не е маркетингов каприз. Голяма част от това събиране е законово задължение..."*
* *"Регламентът ти дава конкретни лостове, не просто принципи."*
* *"Това не е вратичка на оператора, а сблъсък между две задължения..."*
**The Pattern:** Contrastive signposting. AI models frequently use this rhetorical device to sound authoritative, setting up a "strawman" negative just to knock it down with the affirmative truth. Using it once is fine; using it three times in a short article establishes a recognizable AI cadence.
**The Recommendation:** Keep the one you like best (the "вратичка на оператора" is quite good), but flatten the others to state the facts directly. For example, change *"Причината не е маркетингов каприз. Голяма част..."* to simply *"Това събиране на данни е строго законово задължение..."*

### 4. Repetitive Syntax (Anaphora)
**The Passage:** *"Имаш право на достъп... Имаш право на корекция... Можеш да възразиш... Можеш да поискаш..."*
**The Pattern:** Staccato rhythm. LLMs often struggle with sentence variety when listing features or rights, resulting in a repetitive Subject-Verb-Object loop that sounds like a machine reading a manual.
**The Recommendation:** Vary the sentence structure to create a more natural human flow. Group some of the rights together. Suggestion: *"Имаш право да поискаш копие на данните си, както и тяхната корекция или преносимост в използваем формат. Освен това можеш да възразиш срещу профилирането за маркетинг или да поискаш временно ограничаване на обработката при спор."*

### 5. The "Philosophical" Wrap-Up
**The Passage:** *"Личните данни са цената, която плащаш освен депозита, и тя също заслужава внимание."*
**The Pattern:** Narrated emotion / Forced profound conclusion. LLMs are programmed to wrap up articles with a neat, often metaphorical bow that summarizes the "moral of the story." 
**The Recommendation:** Remove the metaphor about data being a "price you pay." Let the practical advice stand on its own. You can transition straight from checking the privacy policy into the final thought about licensed operators offering real protection.

***

**A Note on Process:** 
The responsible gambling language, 18+ markers, affiliate disclosures, and author boilerplate at the bottom are perfectly formatted and placed. Do not touch or alter these elements, as they are critical for compliance.

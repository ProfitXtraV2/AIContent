# 07 — Gemini External Check · Pass 1 (gemini-3.1-pro-preview, 2026-10-11)

Normalized human-likeness: 100 minus 75 = **25** (verdict: „Shows AI patterns, 75% confidence").
Below GEMINI_TARGET_CONFIDENCE (80) -> iterate via step-7b humaniser pass 1, keep-best.
NOTE: [VERIFY] flags STAY per pipeline (FLAGS STAY IN THE TEXT). Gemini's 'leak' note does not apply; they are intentional human-action flags.

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly informative, factually dense, and well-adapted to the Bulgarian legal context, its structural skeleton and transitional phrases strongly echo Large Language Model (LLM) writing patterns. It reads like a high-quality AI draft that has been carefully prompted or lightly edited by a human, rather than a piece written organically from scratch. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

***

### 1. The "Short Answer" Hook (Formulaic Opening)
**The Pattern:** LLMs are heavily trained to be helpful and direct, which often results in them literally announcing that they are giving you the short answer before doing so.
**The Quote:** *"Краткият отговор: не през лицензиран организатор"* (Heading)
**The Recommendation:** Drop the meta-announcement. Human writers usually just state the answer. Change the heading to something direct, such as *"Може ли да се играе през лицензиран организатор?"* or simply state the fact: *"Игрите не се предлагат от лицензиран организатор"*.

### 2. Symmetrical/Over-polished Phrasing
**The Pattern:** AI tends to use slightly unnatural, overly poetic, or perfectly symmetrical phrasing to describe mundane things (like lottery rules).
**The Quote:** *"Механиката е почти огледална."*
**The Recommendation:** Replace this with standard, conversational Bulgarian. A human would more likely say *"Правилата на двете игри са много сходни"* or *"Двете игри имат почти еднакъв формат"*.

### 3. Didactic Signposting (Hand-holding the reader)
**The Pattern:** LLMs frequently use meta-commentary to explain *why* they are telling you something or to artificially bridge two paragraphs. It feels like a lecturer talking down to the audience.
**The Quotes:** 
* *"Оттук следва нещо съвсем практично за Eurojackpot и EuroMillions."*
* *"Двата пътя стигат до едно и също."*
**The Recommendation:** Delete the filler transitions. 
* Instead of *"Оттук следва нещо съвсем практично..."*, just start the next sentence directly: *"Чужд лотариен оператор не може да вземе..."* 
* Instead of *"Двата пътя стигат до едно и също. Играете с оператор, който..."*, combine them into a punchy, direct statement: *"И при двата варианта играете с оператор, който България не лицензира..."*

### 4. The "Misty" Metaphor
**The Pattern:** When discussing complex, unclear, or regulatory topics, AI models default to a specific set of metaphors—most notably "navigating the maze," "the landscape," or "the fog/mist." 
**The Quote:** *"Данъкът е другата мъгла."*
**The Recommendation:** Ground the language. Replace the metaphor with a direct, professional statement about the ambiguity. For example: *"Данъчното облагане също е неясно"* or *"Плащането на данъци крие други неизвестни"*.

### 5. The "In Conclusion" Wrap-Up (Formulaic Structure)
**The Pattern:** Unless explicitly forbidden in the prompt, an LLM will almost always generate a final section that summarizes the entire article, repeats the main points, and ends with a neat, philosophical bow. 
**The Quote:** The entire *"Накратко"* section, specifically the summarizing sentence: *"Да играете Евроджакпот или Евромилиони „от България“ на практика значи оператор извън българския лиценз, с всичко отгоре: никаква защита от НАП, риск сайтът да осъмне блокиран, мъглив данък, сайтове-имитации наоколо."*
**The Recommendation:** Human readers don't need a 600-word article summarized for them at the bottom. Remove the *"Накратко"* heading and the summary sentence entirely. Keep the excellent responsible gambling point at the end (*"И в двата случая това си остава лотария... таванът на разхода тежи повече от размера на джакпота"*), but integrate it into the previous section or make it a standalone "Съвет" (Tip) without the repetitive recap.

***

### Process Note regarding Hard Rules:
As requested, I have not touched or suggested removing any of the responsible gambling language, the 18+ markers, or the disclosures at the bottom. 

**Process Issue Flag:** I must note that several `[VERIFY: ...]` tags have survived into this "finished, human-verified" draft (e.g., `[VERIFY: точни цени по държави]`, `[VERIFY: броят участнички се променя...]`, `[VERIFY: точният член на ЗХ...]`, `[VERIFY: точно ЗДДФЛ третиране...]`). If this article is meant to be in its final state for publishing, your editorial pipeline is leaking editor notes into the production copy. These need to be resolved by your fact-checker before going live.

[exited with code 0]

# Step 7 — Gemini check, pass 7 (after Humaniser pass 5)

Model: gemini-3.1-pro-preview
Normalized: **"Shows AI patterns, 75% confidence"** → human-likeness = **100 − 75 = 25**.

## Decision — KEEP BEST (stop; noisy detector)

Fourth consecutive flat 75%-AI read (HL 25) in this one-off run. Human-likeness by version:
- pre-run baseline 05b (this run's pass 4): **25**
- after Humaniser pass 3 (pass 5): **25**
- after Humaniser pass 4 (pass 6): **25**
- after Humaniser pass 5 (pass 7): **25**

The detector returns an immovable 75%-AI verdict on every read while relocating the flagged passages each pass, and its recommendations now openly contradict earlier passes: pass 4 asked to merge and KEEP the conclusion, passes 6–7 demand deleting it wholesale; pass 7 re-flags the search-intent intro that passes 4–6 left untouched, and flags lines ("Изкушението е разбираемо") the prior passes themselves introduced. It continues to praise the article's substance, RG/18+ boilerplate, affiliate disclosure and specific dates/acts, asking only for stylistic cuts. This is the documented high-variance / whack-a-mole behavior of the Gemini heuristic across this queue (e.g. vk-0008, vk-0015, vk-0018, and this article's own prior nightly run). Attempts used: 4 of 5. Further passes (deleting the intro and the whole conclusion CTA) would strip voice and substance to chase a score that has not moved one point across four reads.

**Kept: Humaniser pass-5 version** (current 05b-final-draft.md). All four versions score 25, so none is lower than any prior version; per KEEP-BEST the tie is resolved in favor of the most-flattened version, which is pass 5 — it has the most AI-tells removed (concession bow-tie, spec data-dump, "Заключение" header, repeated НАП re-explanation, "Изводът е кратък" / "Изкушението е разбираемо" lead-ins, "Затова"/"За сравнение" connectors and repeated "Ако" framing all reduced). Final human-likeness logged for the human: **25** (below the 80 target; noisy detector, do not loop further).

All numbers, links, RG/18+ lines, the affiliate disclosure, byline (Георги Тодоров) and brand (Всички Казина) preserved verbatim across all humaniser passes. The article carries no [VERIFY]/[DATA NEEDED] flags (a prior human edit cleared them); none were introduced or resolved.

---

**Verdict: Shows AI patterns, 75% confidence.**

While this article is highly factual, well-researched, and clearly follows strict editorial guidelines (likely the result of excellent prompting or a human working from a rigid SEO template), its structural skeleton and syntactic rhythm give it away as AI-assisted or AI-generated. It suffers from textbook LLM habits: meta-commentary on the user's search intent, perfectly parallel sentence structures, didactic over-explanation, and a neat "in conclusion" summary paragraph that repeats the thesis. 

Here is the breakdown of the specific patterns and how to fix them.

### 1. The "Search Intent" Meta-Commentary (Signposting)
**The Pattern:** AI models instructed to be "helpful" or "authoritative" often start by narrating the user's search journey or contrasting themselves with other search results. 
**The Quote:** *"Ако сте търсили „NV Casino законно ли е", вероятно вече сте попаднали на десетки страници, представени като „официален партньор 2026", които подминават правния статус напълно; тук той е самата тема."*
**The Recommendation:** Delete this sentence entirely. You already answered the question perfectly in the first sentence ("Не. NV Casino няма лиценз..."). Narrating the user's Google search breaks the fourth wall unnecessarily and sounds like an SEO bot trying to prove its worth. 

### 2. Didactic "Textbook" Explanations (Over-contextualizing)
**The Pattern:** LLMs struggle to weave context naturally into a narrative; instead, they stop the article to deliver a Wikipedia-style definition before making their point.
**The Quote:** *"Онлайн хазартът в България е под надзора на Националната агенция за приходите по Закона за хазарта, а право да приема залози от играчи в страната има само оператор, вписан в регистъра на НАП. Регистърът е публичен и всеки може да провери дали даден сайт присъства в него, преди да си направи сметка."*
**The Recommendation:** Condense this. You don't need to explain that the register is public and anyone can check it. Merge the premise directly into the finding. For example, advise the writer to combine these sentences to simply state that because Bulgarian gambling is overseen by the NRA, only registered operators can legally accept bets—and NV Casino is not on that list. 

### 3. Staccato Rhythm and Parallelism (Formulaic Syntax)
**The Pattern:** AI loves to create contrast by starting consecutive sentences or clauses with the exact same prepositional framing. It creates a robotic, predictable rhythm.
**The Quote:** 
* *"**При лицензиран оператор** има конкретен адрес за жалба."*
* *"**При NV Casino** такъв адрес липсва..."*
* *"**При отказано или забавено теглене** оставате зависими..."*
**The Recommendation:** Break the repetitive "При [X]..." structure. Advise the writer to vary the syntax. For instance, the second sentence could be restructured to focus on the player's experience (e.g., "Since NV Casino lacks this address, your only option during a dispute is..."). 

### 4. Narrated Transparency / Melodramatic Tone
**The Pattern:** When instructed to include affiliate disclosures naturally, AI often overcompensates, making it sound like a dramatic confession rather than a standard editorial note.
**The Quote:** *"Казваме го открито: връзката към Betano е партньорска и приходите от нея финансират сайта, но това не мени факта, който стои над всичко: Betano е в регистъра на НАП, а NV Casino не е."*
**The Recommendation:** Soften the phrasing. Advise the writer to remove the dramatic "Казваме го открито" (We say it openly) and "факта, който стои над всичко" (the fact that stands above all). A simpler, more professional transition (e.g., "While our link to Betano is an affiliate link that supports this site, the regulatory difference remains: Betano is NRA-registered, NV Casino is not.") will sound much more like a human editor.

### 5. The "Tidy Bow" Summary (Formulaic Structure)
**The Pattern:** Even without using the words "In conclusion," AI almost always generates a final paragraph before the disclaimers that summarizes the entire article, repeating points already made.
**The Quote:** *"NV Casino не е законно за българския пазар. Липсата на лиценз от НАП и на защита по Закона за хазарта тежи повече от реалния каталог и удобните плащания, а кюрасаоският лиценз не замества нито едно от двете. Ако решите да играете, направете го при оператор, който можете да намерите в регистъра на НАП."*
**The Recommendation:** Cut this entire paragraph. The preceding paragraph already concludes the argument perfectly by comparing the two options and explaining the methodology. This summary adds zero new information and slows down the reader right before the mandatory responsible gambling text.

*(Note: As per your rules, the responsible gambling language, 18+ markers, and affiliate licensing boilerplate at the very end are untouched and should remain exactly as they are.)*

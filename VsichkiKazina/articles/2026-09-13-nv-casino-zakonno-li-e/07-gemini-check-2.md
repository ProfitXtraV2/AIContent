# Step 7 — Gemini check, pass 2 (after Humaniser pass 1)

Model: gemini-3.1-pro-preview
Normalized: **"Shows strong AI patterns, 85% confidence"** → human-likeness = **100 − 85 = 15** → still below target (80); unchanged from baseline. This is the high-variance detector behavior documented across the VsichkiKazina queue (scores swing widely between reads on the same text). Gemini now names *new* body-prose targets (neat-bow metaphor summaries, smooth-vs-sudden em-dash contrasts, a philosophical dichotomy, a semicolon-balanced clause, grandiose absolutes) and explicitly praises the surviving [VERIFY]/[DATA NEEDED] tags, RG/18+ boilerplate and affiliate disclosure — "keep all of these exactly as they are." One more Humaniser pass (pass 2, MAX_GEMINI_PASSES=2) on the new targets, then final re-check (07-gemini-check-3.md). Keep-best tracked (baseline 15, after pass 1: 15).

---

**Verdict: Shows strong AI patterns, 85% confidence.**

While this article is exceptionally well-prompted and contains excellent human-driven elements (like the direct "Не." opening, the transparent affiliate disclosure, and the rigorous use of [VERIFY]/[DATA NEEDED] tags), the underlying prose relies heavily on classic LLM rhetorical devices. The text frequently uses balanced clauses, dramatic metaphors, and "neat bow" summary sentences at the end of paragraphs—all hallmarks of GPT-4 and Claude when writing in Bulgarian. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the text.

### 1. The "Neat Bow" Metaphorical Summary
AI models struggle to just state a fact and move on; they feel compelled to wrap up paragraphs with a philosophical or metaphorical summary sentence.
*   **Flagged text:** *"Лицензът чертае линията между оператор, който отговаря пред българска институция, и такъв, който не отговаря пред никого тук."* (The license draws the line between...)
*   **Flagged text:** *"При NV Casino тази врата е затворена..."* (With NV Casino this door is closed...)
*   **Recommendation:** Delete these sentences entirely, or strip the metaphors ("чертае линията", "врата е затворена"). Human writers usually let the preceding facts speak for themselves without needing to summarize the "moral of the story" at the end of the paragraph.

### 2. The "Smooth vs. Sudden" Dramatic Contrast (with Em-dash)
LLMs love to contrast a false sense of security with a sudden negative outcome, frequently using an em-dash to pivot the sentence. 
*   **Flagged text:** *"Достъпът може да изчезне за една нощ, а средствата остават от другата страна на блокирането..."*
*   **Flagged text:** *"Този разход не пише никъде в офертата и изглежда нулев, докато всичко върви гладко — а излиза наяве точно когато трябва да поискате парите си обратно."*
*   **Recommendation:** Tone down the dramatic flair. Instead of "изчезне за една нощ" (disappear overnight) and "от другата страна на блокирането" (on the other side of the block), use dry, literal language (e.g., state simply that if the domain is blocked, accessing funds becomes technically difficult). Remove the em-dash contrast in the second example and state the risk plainly.

### 3. The Philosophical Dichotomy
AI frequently uses "It's not about X, it's about Y" structures to sound authoritative and insightful.
*   **Flagged text:** *"Разликата не е в игрите на екрана, а в това какво се случва, когато нещо се обърка."*
*   **Recommendation:** Cut this sentence. It sounds like a line from a marketing commercial rather than an objective legal/review article. The surrounding sentences already explain the practical difference perfectly well.

### 4. The Semicolon Balance
LLMs use semicolons to create perfectly balanced, rhythmic clauses that sound highly polished but unnatural in standard web copywriting.
*   **Flagged text:** *"Регулаторната защита няма значение при регистрацията; тя започва да тежи, когато теглене заседне или условие се тълкува спорно..."*
*   **Recommendation:** Break this into two separate, shorter sentences. Disrupt the perfect rhythm. You can also remove the slightly poetic "започва да тежи" (starts to weigh) and replace it with a standard verb like "е важна" (is important).

### 5. Grandiose / Absolute Phrasing
AI often uses absolute, slightly grandiose language to emphasize a point, especially in introductions and conclusions.
*   **Flagged text:** *"...и това е фактът над всичко останало."* (and this is the fact above all else.)
*   **Flagged text:** *"Проблемът е чисто правен: нищо от изброеното не заменя липсата на лиценз от НАП."*
*   **Recommendation:** Soften the absolute phrasing. In the conclusion, remove "фактът над всичко останало" and just state the legal reality. In the H2 transition, you can drop the dramatic colon setup and just state that despite the good features, the lack of a license remains the primary issue.

### A Note on Process (Do Not Change):
The inclusion of the **[VERIFY]** and **[DATA NEEDED]** tags, the responsible gambling boilerplate, the 18+ markers, and the transparent affiliate disclosure ("Казваме го открито...") are excellent. They show a rigorous editorial process. Keep all of these exactly as they are. Your focus should solely be on flattening the overly dramatic, rhythmic AI prose in the main body paragraphs.

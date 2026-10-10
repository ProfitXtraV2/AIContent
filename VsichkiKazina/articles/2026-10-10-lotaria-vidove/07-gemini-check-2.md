# 07 — Gemini check 2 (after humaniser pass 1) · 2026-10-10T10:56:17Z

Normalised human-likeness: human-written 90% → **90**. Result: PASS (≥ 80). Quick Brand Gate re-check before this check (mechanical): byline Георги Тодоров ✓, 18+ line ✓, „Солидарност" line ✓, 4 approved live links ✓, 3 [VERIFY] verbatim ✓, 0 [DATA NEEDED]/[CONFLICT] ✓, 0 em-dash outside flags ✓, brand name variants 0 ✓. Remaining recommendations are optional polish — not applied (PASS).

---

**Verdict: Likely human-written (or heavily human-edited), 90% confidence.**

This article reads exceptionally well and bypasses almost all standard AI detection triggers. It contains highly specific localized knowledge, exact broadcast times, and complex mathematical breakdowns that standard LLMs struggle to generate without hallucinating. 

More importantly, it features distinct human stylistic choices: colloquialisms like *„С кеното положението е мътно“* (With keno, the situation is murky) and *„скречът, както всички му казват“* (the scratch, as everyone calls it). The conclusion (*„...ако някога ви се стори, че тото може да е план за пари, препрочетете числото.“*) is a brilliant piece of human rhetorical punchiness that AI almost never produces (AI prefers preachy, summarizing conclusions like "In summary, always remember to play responsibly").

However, there are a few structural and rhythmic patterns that mimic AI or junior SEO writing. Here is what triggered my radar and how to polish them out.

---

### Flagged Passages & Patterns

**1. Pattern: SEO Keyword Shoehorning / Robotic Transition**
*   **Quote:** *„Когато някой търси „бг лотария", почти винаги има предвид игрите на БСТ.“*
*   **Why it flagged:** This is a classic SEO/AI transition. Explicitly stating "When someone searches for [Exact Match Keyword]" is a mechanical way to force a search term into the text. It breaks the fourth wall of the article and feels like an algorithm trying to satisfy a search intent rather than a writer telling a story.

**2. Pattern: Breathless Legal Information Dump (Run-on Sentence)**
*   **Quote:** *„Лотарията е хазартна игра и Законът за хазарта познава четири нейни вида (чл. 41 и чл. 49), а лиценз за почти всички от тях може да получи само държавата, която ги провежда чрез ДП „Български спортен тотализатор" (БСТ) по чл. 4, ал. 3 и чл. 13а.“*
*   **Why it flagged:** When LLMs are prompted to include specific legal citations, they often cram them all into a single, breathless mega-sentence. While factually accurate, the rhythm is exhausting and reads like a summarized legal brief rather than consumer-facing copy.

**3. Pattern: Formulaic "Bold Noun + Colon" List Structure**
*   **Quote:** 
    *   *„**организатора**: за тото, лото...“*
    *   *„**обекта**: продажба само там...“*
    *   *„**изплащането**: печалба само в тези...“*
    *   *„**въпроса за възрастта**: продажбата на лица...“*
*   **Why it flagged:** This specific list format (Bolded Noun/Concept -> Colon -> Explanation) is the default output structure for ChatGPT and Claude when asked to explain a process or give tips. It creates a highly mechanical, staccato visual rhythm.

---

### Concrete Recommendations

*   **For the keyword transition:** Remove the meta-reference to "searching." Recommend rewriting this sentence to state the fact directly—for example, noting that in Bulgaria, the concept of a national lottery is entirely synonymous with the games of the BST, while still naturally using the phrase "бг лотария" as the subject of the sentence.
*   **For the opening legal dump:** Break that massive opening sentence into two or three shorter, punchier sentences. Introduce the four types of lottery first, and then use a separate sentence to explain the state's monopoly and the BST's role. Keep all the legal citations exactly as they are, just give them room to breathe.
*   **For the bulleted list:** Break the AI-style "Noun: Explanation" format. Recommend changing the bolded triggers into actionable phrases or full questions. For example, instead of "**въпроса за възрастта**:", use something like "**Проверяват ли възрастта ви?**" or "**Изискване за пълнолетие**". This makes the list read like human advice rather than a machine-generated taxonomy.

*Note on process: I see several [VERIFY] tags remaining in the text (regarding the Wikipedia date, the Keno license, and the consolidated text fine amounts), as well as intact responsible gambling and 18+ disclosures. Per instructions, I have not touched these, but flagging them for your editorial team to resolve before publication.*

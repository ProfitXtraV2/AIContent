# 07-GEMINI-CHECK — pass 2 (after humaniser pass 1) — chargeback-kazino
# Model: gemini-3.1-pro-preview · run 2026-10-01 (3rd fire)
# Normalized human-likeness = 100 − 75 = 25 (Shows AI patterns, 75%). Up from 15. Still < 80 → one more Humaniser pass (2/2), then keep-best.

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns, 75% confidence.**

While this article contains excellent localized context (НАП, specific timeframes, 3-D Secure) and has clearly been touched by a human (evidenced by the first-person internal linking), the underlying structural skeleton and transitional phrases are classic AI. It reads like a high-quality AI draft that a human editor has polished and injected with "I" statements, resulting in a slight tonal clash between detached, robotic authority and sudden first-person blogging.

Here is the breakdown of the AI patterns and how to fix them.

### Passages and Patterns Flagged

**1. The "Strawman / Misunderstood" Intro**
*   **The text:** *"Chargeback често се разбира погрешно. Мнозина приемат, че банката просто връща парите при поискване, а инструментът е доста по-тесен от това..."*
*   **The pattern:** AI models almost universally open informational articles by claiming the topic is "often misunderstood," "a common misconception," or that "many assume" something incorrect. It’s a lazy rhetorical device to justify the article's existence.

**2. The Micro-Summary (Bow-tying)**
*   **The text:** *"Общото е, че не оспорваш резултата от играта, а дефект в самото плащане. Там банката има какво да разследва."* (Appears immediately after the bulleted list).
*   **The pattern:** AI struggles to let a list stand on its own. It habitually adds a summarizing sentence immediately after bullet points to "tie a bow" on the section before moving to the next heading. 

**3. The Preachy / Moralizing Transition**
*   **The text:** *"Струва си да се каже и нещо извън картите. Хазартът не е финансова стратегия, а chargeback не е предпазна мрежа, която да я направи такава."*
*   **The pattern:** AI models are heavily RLHF-trained (Reinforcement Learning from Human Feedback) to be highly cautious around gambling. This results in sudden, preachy, PSA-style lectures that break the objective, informative tone of the text. Furthermore, "Струва си да се каже" (It is worth noting/saying) is a textbook AI transitional filler.

**4. "Frankenstein" First-Person Insertions**
*   **The text:** *"Дали едно казино изобщо е законно у нас проверявам в страницата..."* and *"как изглежда този път съм описал в раздела..."*
*   **The pattern:** Tonal whiplash. The entire article is written in a detached, authoritative, second-person voice ("Ако сам си депозирал..."). Suddenly dropping into the first person ("I check," "I have described") feels bolted-on—a common footprint of a human editor trying to "humanize" an AI draft by manually inserting personal pronouns near internal links.

**5. The Redundant Conclusion Recap**
*   **The text:** *"Chargeback е предназначен за неоторизирани и неизпълнени транзакции. За загубите от игра той не важи, затова изборът на оператор, пред когото има кой да отговаря, те пази далеч повече от картовия спор."*
*   **The pattern:** AI always writes a concluding paragraph that summarizes the exact points made just paragraphs above. In a short, punchy web article, this is entirely redundant.

### Concrete Recommendations

*   **Cut the intro strawman:** Delete the first two sentences. Start directly with the meat of the issue. For example, start immediately with the distinction: *"При онлайн хазарта е важно да се направи разлика между две ситуации: кога картовото оспорване (chargeback) е твое право и кога..."*
*   **Delete the micro-summary:** Remove the sentence starting with *"Общото е, че не оспорваш..."* right after the bullet points. The bullets are clear enough; trust the reader to understand them without a recap.
*   **Remove the preachy lecture:** Delete *"Струва си да се каже и нещо извън картите. Хазартът не е финансова стратегия, а chargeback не е предпазна мрежа, която да я направи такава."* It sounds like a scolding parent, not a helpful guide. You can jump straight from the 3-D Secure explanation to the budget limits sentence.
*   **Smooth out the first-person links:** Decide on the perspective. If the author is a guide, use first-person plural or keep it objective. Instead of *"Дали едно казино изобщо е законно у нас проверявам в..."*, change it to an actionable reader command: *"Можеш да провериш дали едно казино е законно у нас в..."* Do the same for the other internal links to maintain a consistent second-person ("ти") tone.
*   **Axe the summary conclusion (Process Note on RG):** Delete the first two sentences of the final paragraph (*"Chargeback е предназначен за... далеч повече от картовия спор."*). 
    *   *Important Process Note:* The responsible gambling language (*"18+ Хазартът може да пристрасти..."*) is currently attached to the end of this AI summary paragraph. **Do not delete the RG text.** Simply remove the AI summary sentences and let the RG text stand on its own as the final sign-off before the author bio.

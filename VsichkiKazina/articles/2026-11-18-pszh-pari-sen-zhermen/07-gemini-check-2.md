# 07 — Gemini check, pass 2 (vk-0338 · ПСЖ)

Script: scripts/gemini_check.py 05b-final-draft.md (after humaniser pass 1) · 2026-11-18T07:32:20Z

## Verbatim Gemini verdict + recommendations
```
**Verdict: Shows strong AI patterns, 85% confidence.**

While the article is grammatically flawless, highly informative, and perfectly structured for SEO, it exhibits several classic hallmarks of Large Language Model (LLM) generation. The text relies heavily on cliché dramatic contrasts, encyclopedic "knowledge dumping" disguised as paragraphs, and formulaic transition sentences. It reads exactly like a well-prompted GPT-4 output tailored for an affiliate site. 

*(Note: Per your instructions, I am ignoring the fictionalized 2025/2026 Champions League victories and treating them as verified facts for this exercise. I have also completely bypassed the responsible gambling and disclosure sections at the end, which are standard and should remain exactly as they are).*

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

---

### 1. Melodramatic Metaphors & Cliché Contrasts (Narrated Emotion)
AI loves to build a narrative arc using slightly dramatic, overused metaphors, especially when contrasting domestic success with European struggles. 

*   **Flagged Text:** *"Клубът трупаше звезди и титли във Франция, а нощта, за която плащаше най-много, все му убягваше."* (The club accumulated stars and titles in France, but the night it paid the most for kept eluding it.)
*   **Flagged Text:** *"Купеното печелеше у дома почти всяка година, но в Европа отборът пак спираше преди последната крачка."* (The bought [team] won at home almost every year, but in Europe the team kept stopping before the final step.)
*   **The Pattern:** LLMs frequently use phrases like "eluded them" or "the final step" to create artificial tension. It sounds like a movie trailer rather than sports journalism.
*   **Recommendation:** Tone down the melodrama. Replace the poetic "the night it paid the most for" with a sharper, more grounded observation about the specific financial investments versus the Champions League ROI. Remove the cliché "последната крачка" (final step) and state plainly where they were failing (e.g., quarter-final exits, specific heartbreaking losses).

### 2. The "Knowledge Graph Dump" (Over-polished Lists in Paragraph Form)
When asked to mention historical players, AI tends to group them chronologically and attach their nationalities or titles in a highly robotic, symmetrical way.

*   **Flagged Text:** *"През този период през клуба минаха имена като Сафет Сушич, Луис Фернандес и Доминик Рошто, по-късно бразилецът Раи, либериецът Джордж Уеа и французинът Давид Жинола, а в началото на новия век и младият Роналдиньо."*
*   **The Pattern:** This is a classic AI listicle masquerading as a paragraph. The rigid structure of "[Nationality] [Name]" (бразилецът Раи, либериецът Джордж Уеа, французинът Давид Жинола) is how an LLM retrieves and formats entity data. Humans rarely write with such symmetrical, encyclopedic cadence.
*   **Recommendation:** Break up this grocery list of names. Instead of listing seven players with their passports, focus on one or two and mention a specific, tangible detail about their time there (e.g., Weah's Ballon d'Or era or Ronaldinho's flair). Let the text breathe rather than cramming the paragraph with SEO entities.

### 3. Formulaic Topic Sentences (Signposting)
AI struggles to move organically from one concept to the next, so it relies on generic, sweeping transition sentences to introduce new sections.

*   **Flagged Text:** *"Силата на клуба личи и в рекордните му списъци."* (The strength of the club is also evident in its record lists.)
*   **The Pattern:** This is textbook AI signposting. It’s a hollow sentence that exists solely to bridge the gap between the "Trophies" section and the "Legends" section. 
*   **Recommendation:** Delete this sentence entirely. You don't need to announce to the reader that you are about to talk about records. Start the paragraph directly with the hard facts: *"Килиан Мбапе е голмайстор номер едно..."* The writing will instantly feel punchier and more confident.

### 4. Robotic Disclaimers (Over-explicitness)
Because the AI was likely prompted to write from the perspective of the year 2026, it over-explains the temporal context to ensure it fulfills the prompt's constraints.

*   **Flagged Text:** *"Числата важат към края на 2026 г. и се менят със следващите сезони."* (The numbers are valid as of the end of 2026 and change with subsequent seasons.)
*   **The Pattern:** Humans understand that sports statistics change over time; they don't usually write explicit disclaimers in the middle of an editorial paragraph unless legally required. This reads like an AI covering its bases.
*   **Recommendation:** Remove this standalone sentence. If you must establish the timeline, weave it naturally into the preceding sentence. For example, change the opening of that paragraph to: *"До края на 2026 г. колекцията във Франция достига..."* (By the end of 2026, the collection in France reaches...).

### 5. Staccato Rhythm in Historical Recaps
AI often defaults to a monotonous Subject-Verb-Object or Date-Subject-Verb rhythm when recounting history.

*   **Flagged Text:** *"Основан е на 12 август 1970 г... Бракът се разпадна бързо: през 1972 г. „Пари ФК“ се отдели... От 1974 г. домът му е „Парк де пренс“..."*
*   **The Pattern:** The sentences are all roughly the same length and start with a chronological marker. It feels like reading a timeline rather than a story.
*   **Recommendation:** Combine or restructure these sentences to vary the rhythm. For example, connect the founding and the split into a single flowing thought, emphasizing the irony of how quickly the initial merger failed, rather than just listing the dates sequentially.
```

## Normalization
- Verdict: "Shows strong AI patterns, 85% confidence" → human-likeness = 100 − 85 = **15**. Below target 80, and LOWER than check-1 (20) — documented noisy/whack-a-mole detector on football-history content (cf. vk-0063, vk-0314).
- Note: Gemini flags the 2025/2026 Champions League wins as "fictionalized" — they are REAL, cross-verified (its training cutoff predates them); not a factual error in the article. It treated them as given.
- Action: humaniser pass 2 applied (melodrama/metaphor flattening, de-listed player names, deleted signposting topic sentence, removed temporal disclaimer, varied founding rhythm). Re-check follows.

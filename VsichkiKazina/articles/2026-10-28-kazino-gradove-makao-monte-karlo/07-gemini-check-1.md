# 07 — Gemini check, pass 1 (baseline draft)

Command: python3 scripts/gemini_check.py 05b-final-draft.md
Normalization: "Shows AI patterns, 75%" -> human-likeness = 100 - 75 = **25**.
Result: HL 25 < 80 -> needs humaniser pass (apply recs via step-7b).

---

**Verdict: Shows AI patterns (Human-edited AI), 75% confidence.**

This article is factually dense, well-localized for the Bulgarian market, and avoids the most egregious AI clichés (like "В днешния забързан свят" / "In today's fast-paced world"). However, beneath the polished surface, the structural skeleton is highly characteristic of an LLM. The text relies heavily on symmetrical comparisons, grandiose philosophical framing, and the classic AI habit of tying a "neat bow" at the end of every section to explain the moral or profound meaning of the facts. 

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

---

### 1. Thematic Framing & Over-Synthesizing
AI struggles to simply state facts; it prefers to frame them as profound dichotomies, moral ironies, or grand historical narratives. 

*   **Flagged passage:** *"Зад тях стоят два напълно различни отговора на един и същ въпрос как се строи място около игралната маса."* (Intro)
*   **Flagged passage:** *"Малка държава строи благополучието си върху загубите на пришълците и го пази, като не пуска поданиците си да седнат срещу същата рулетка."* (Monte Carlo section)
*   **Pattern:** **Narrated Irony / Philosophical Framing.** The AI is trying too hard to sound clever by summarizing the facts into a poetic, slightly melodramatic conclusion. 
*   **Recommendation:** Flatten the prose. In the intro, remove the "two different answers to the same question" framing and just state that the article explores how these two distinct hubs developed. In the Monte Carlo section, keep the facts about Princess Caroline's ban and the tax exemptions, but delete the poetic summary about "building prosperity on the losses of newcomers." Let the reader deduce the irony themselves.

### 2. Formulaic Compare & Contrast
When asked to compare items, LLMs almost always default to a highly symmetrical, single-trait categorization structure (e.g., "X is the model of A, Y is the model of B").

*   **Flagged passage:** *"Макао е отговорът на мащаба и приходите... Монте Карло е отговорът на наследството и престижа... Лас Вегас е третият модел, курортно-развлекателният..."*
*   **Pattern:** **Symmetrical Categorization.** This reads exactly like an AI generating a structured summary where every subject gets its own perfectly balanced, neatly labeled box. Human writers rarely write with such rigid symmetry.
*   **Recommendation:** Break the symmetry. Instead of framing them as "three answers to one question," describe their current market realities organically. You can contrast Macau's VIP baccarat volume with Monte Carlo's European roulette tradition without using the repetitive "[City] is the answer to [Concept]" formula.

### 3. Signposting & Metaphorical Clichés
AI uses empty transition sentences to announce what it is about to do, and relies on a specific set of structural metaphors (pillars, balances, landscapes).

*   **Flagged passage:** *"Решаващата промяна за съвременния облик на града идва по-късно."*
*   **Pattern:** **Signposting.** A classic filler sentence used by AI to bridge paragraphs.
*   **Flagged passage:** *"...липсва втори стълб, който да поеме удара."*
*   **Pattern:** **Structural Metaphor.** AI loves "pillars" (стълбове) when discussing economies or arguments.
*   **Recommendation:** Delete the signposting sentence entirely. Just start the paragraph directly with the historical trigger: *"От 1962 г. всички хазартни игри в Макао са под монополния лиценз..."* For the metaphor, replace "втори стълб" with a literal economic term (e.g., "липсва друга развита индустрия, която да компенсира").

### 4. The "Neat Bow" / Didactic Conclusion
LLMs are programmed to be helpful and conclusive, which results in articles ending with a "moral of the story" or a preachy, clever final thought.

*   **Flagged passage:** *"Монте Карло, Макао и Лас Вегас изглеждат като три различни свята, но продават едно и също: усещането, че този път сметката ще излезе в твоя полза."*
*   **Flagged passage:** *"Затова историята на тези градове е по-интересното вложение от билета до тях."*
*   **Pattern:** **The Didactic Wrap-up.** The text shifts from an objective historical/economic overview into a slightly preachy, essay-style conclusion. 
*   **Recommendation:** The transition into the Bulgarian legal reality and responsible gambling is actually very good and necessary—**do not remove any of the RG language, the NAP mentions, or the reality check about gambling math.** However, delete the final sentence (*"Затова историята на тези градове е по-интересното вложение..."*). It sounds like a high school essay sign-off. End the article on the hard, practical note about the mathematics of the game not being on the player's side. It is much punchier and sounds far more like a veteran human writer.

# 07 — Gemini check, pass 1 (on initial 05b)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-29-efbet-liga-format-otbori/05b-final-draft.md`

**Verdict: Shows AI patterns, 75% confidence.** → human-likeness = 100 − 75 = **25** (BELOW 80 → iterate).

---

While the article is factually dense, grammatically flawless, and well-structured, it exhibits several classic hallmarks of AI-generated SEO content. The primary giveaways are the didactic tone (over-explaining universally known concepts), dramatic metaphorical transitions, meta-commentary about search intent, and the classic "bow-tie" philosophical conclusion.

### 1. Meta-Commentary on Search Intent
Passage: „Търсачката връща и двете имена, защото зад тях стои едно състезание."
Pattern: SEO signposting / breaking the fourth wall.
Recommendation: Remove the reference to the search engine; state the name relationship directly.

### 2. Over-Explaining the Obvious (Didactic Tone)
Passage: „Класирането, което хората търсят, е сборът от точки: три за победа, една за равен, нула за загуба…"
Pattern: Over-explaining foundational concepts (basic football points) to pad comprehensiveness.
Recommendation: Delete the win/draw/loss explanation; jump to the league-specific tie-breakers.

### 3. Formulaic Metaphors and Dramatic Transitions
Passages: „Дъното на таблицата има цена."; „Върхът на таблицата отваря вратата към европейските клубни турнири."
Pattern: AI thematic signposting — dramatic metaphorical topic sentences.
Recommendation: Replace with direct, factual statements.

### 4. Pseudo-Conversational Padding
Passage: „Тук няма да намериш актуални резултати, защото те се менят всеки кръг и всяка снимка на таблицата остарява до следващата събота."
Pattern: Over-justification / conversational flair.
Recommendation: Cut the justification; just point to the official live table.

### 5. The "Bow-Tie" Conclusion
Passage: „Форматът на лигата ще се промени пак… Класирането обаче винаги се решава на терена…"
Pattern: Philosophical wrap-up with a preachy moral bow.
Recommendation: Remove the „решава се на терена" cliché; end on the final substantive point or a strict factual summary.

Note (Gemini): the RG language, 18+ markers, and affiliate disclosures are perfectly formatted for compliance and were NOT factored into the score; keep them exactly as they are.

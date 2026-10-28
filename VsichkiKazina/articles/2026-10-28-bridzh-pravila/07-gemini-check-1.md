# 07 — Gemini check, pass 1 (initial draft)

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md`
Normalized human-likeness: **20** ("Shows AI patterns, 80% confidence" → 100 − 80).
PASS test (≥80): FAIL → iterate (humaniser pass 1).

## Gemini verbatim verdict + recommendations

### Verdict
**Shows AI patterns, 80% confidence.**
While the article is highly accurate, well-structured, and clearly human-verified (especially with the localized Bulgarian context and compliance footers), the prose itself exhibits several classic LLM stylistic fingerprints. It relies heavily on translated English idioms, rhetorical antithesis (contrasting two ideas for dramatic effect), grandiose metaphors, and the trademark "neat bow" summary at the end. It reads like a high-quality AI draft that was fact-checked but not heavily line-edited for human voice.

### Flagged Passages and AI Patterns
1. **Rhetorical Antithesis (The "Simple/Complex" contrast)** — "Целта на разиграващия е проста по формулировка и мъчна по изпълнение:" — LLMs love contrasting pairs to sound authoritative ("simple in theory, difficult in practice"); feels like a direct translation of a common GPT-4 trope.
2. **Forced Metaphors / Philosophical Musings** — "Информацията, която минава през обявите и през реда на свалените карти, е истинската валута на играта." — Calling an abstract concept the "true currency" is a massive AI cliché.
3. **Grandiose Absolutes & Hyperbole** — "Наддаването до шлем е върхът на партньорската преценка..."; "Правилото за следването на боята командва всичко останало." — AI resorts to dramatic absolutes ("the peak of," "commands everything else"); out of place in a beginner's rulebook.
4. **Tautological "Conversational" Filler** — "Наддаването е наддаване в буквалния смисъл." — circular, hollow statement; sounds robotic.
5. **The "Neat Bow" Summary Conclusion** — "За първата си вечер на масата обаче стигат четирите стъпки отгоре: раздай, наддавай, изиграй взятките, преброй до манша." — tidy rhythmic list referencing the intro; one of the most reliable AI indicators.

(Note: the responsible-gambling section and footer disclaimers are standard compliance text, ignored for AI-style detection.)

### Concrete Recommendations
- Fix the antithesis: state the declarer's goal directly (collect at least as many tricks as the contract requires).
- Cut the "currency" metaphor: replace with a straightforward statement that information exchange is the most crucial element.
- Tone down grandiosity: "върхът на партньорската преценка" → bidding for a slam requires the most precise communication; "командва всичко останало" → it is the fundamental/primary rule.
- Delete the tautology: remove "Наддаването е наддаване в буквалния смисъл." Start with who begins the bidding.
- Break the summary loop: remove the final summarizing sentence; end on the historical/structural facts (WBF, scoring layers).

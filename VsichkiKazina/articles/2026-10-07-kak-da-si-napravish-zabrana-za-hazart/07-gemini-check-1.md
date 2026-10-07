# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-07

## Verdict (verbatim)

**Verdict: Shows AI patterns, 75% confidence.**
→ Normalized HUMAN-LIKENESS = 100 − 75 = **25**  (PASS threshold = 80)

This is a high-quality text. It avoids the most glaring AI clichés (like "В днешно време..." or "В заключение...") and successfully mimics a modern, conversational copywriting style. However, it reads exactly like an advanced LLM that has been explicitly prompted to "write like a human copywriter, use short sentences, be empathetic, and avoid AI jargon." The giveaway is the density of narrated emotion, forced staccato rhythms, and philosophical dramatization applied to what is essentially a dry, procedural topic.

### 1. Narrated Emotion & Disguised Signposting
Passage: „Такова решение рядко се взема на спокойствие. Понякога го налага близък човек, понякога идва след месеци отлагане. Няма да ви убеждаваме в нищо. Надолу е само процедурата и един упорит мит, който е добре да падне, преди да сте тръгнали да го проверявате."
Pattern: AI psychologizes the reader to build "empathy", then uses a disguised signpost („Надолу е само процедурата...") to outline the article.
Recommendation: Cut the psychological assumptions. Start directly with the purpose of the page: the procedure and debunking the EGN-check myth.

### 2. Over-Dramatization / Poetic Metaphors
Passages: „Тази долна граница стои в закона нарочно, за да издържи точно онзи момент на колебание, в който най-силно ви се връща към играта."; „Механизъм, който гасне в някоя слаба вечер с едно обаждане до поддръжката, не пази никого."; „Мнозина залагат, че това ще им стигне, а виждат дупката чак когато я опитат."
Pattern: AI defaults to cinematic, poetic metaphors for addiction/self-exclusion. Stacking this many dramatic metaphors in a procedural guide feels artificial and slightly patronizing.
Recommendation: Tone down the poetry. Explain the 1-year minimum and strict cancellation in clear, neutral terms; focus on the mechanics of the law.

### 3. Forced Staccato Rhythm
Passage: „Предсрочно не става. Размисъл след седмица не отваря нищо обратно; забраната пада сама, когато изтече срокът, който сте задали."
Pattern: Forced, choppy rhythm (short punchy sentences) to bypass AI detectors; reads like a hardboiled novel rather than a helpful guide.
Recommendation: Combine the fragmented thoughts into a natural flowing sentence; drop the dramatic „Предсрочно не става" preamble.

### 4. The Philosophical Wrap-Up
Passage: „Силна я правят точно нещата, които в началото приличат на неудобство: не се вдига с едно обаждане на сутринта и не зависи от доброто желание на конкретно казино."
Pattern: AI adds a summarizing "moral of the story" before the CTA.
Recommendation: Delete the philosophical summary; jump straight into the actionable advice.

### Process note (Gemini)
Noted the [VERIFY] flags (1-year minimum, 5–7 day processing, exact НАП channel) and did NOT touch them, nor the 18+ RG boilerplate. Editorial team must fact-check the [VERIFY] claims with НАП and remove the tags before publish.

---
RESULT: human-likeness 25 → below 80 → iterate (step-7b humaniser pass 1), then keep-best.

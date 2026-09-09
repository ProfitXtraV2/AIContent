# Step 7 — Gemini check, pass 1 (initial 05b)

Model: gemini-3.1-pro-preview
Normalized: **"Shows AI patterns, 85% confidence"** → human-likeness = **100 − 85 = 15** → far below target (80). Iterate: one Humaniser pass on the flagged patterns, then re-check. Keep-best tracked (baseline HL 15).

---

**Verdict: Shows AI patterns, 85% confidence.**

While this article is highly accurate, well-researched, and avoids the worst AI fluff, its underlying skeleton is textbook LLM. It reads like a very well-prompted AI that was instructed to be analytical and responsible. The primary giveaways are the rhythmic predictability (almost every paragraph ends with a neat, philosophical summary) and the use of classic AI signposting and thematic puns.

### 1. The "Bow-Tie" Paragraph Endings (Summarizing/Moralizing)
- *"Дългата верига е приятна, но не е пробив в математиката."* (end of Tumble)
- *"Точно затова разликата между обикновено завъртане и добър бонус може да е огромна, и точно затова е лесно да гониш бонуса по-дълго, отколкото си планирал."* (end of Free Spins)
- *"Високата волатилност прави играта вълнуваща, но и по-непредсказуема за банката ти от бавен слот с ниска волатилност."* (end of Volatility)
Recommendation: chop the bows; let the factual point be the last thing.

### 2. Formulaic Signposting & Numbering
- *"Важно е да се разбере, че tumble не добавя пари..."*
- *"Тук трябва да си наясно с две неща. Първо... Второ..."*
Recommendation: remove the throat-clearing; state the facts directly.

### 3. The Manufactured Hook
- *"Има обаче уловка, която малцина споменават."*
Recommendation: replace with a plain transition (*"Pragmatic Play обаче доставя играта..."*).

### 4. The Thematic Pun / Over-Polished Conclusion
- *"Вкусът на играта е сладък; сметката отдолу остава сметка."* (thematic „Sweet" pun)
- *"Нищо от това не променя факта, че..."*
Recommendation: delete the final pun sentence; end on the practical advice.

*(Process note: [VERIFY] tag, RG warnings and 18+ markers are correct practice — do not touch.)*

(Applied in Humaniser pass 1 → re-checked in 07-gemini-check-2.md.)

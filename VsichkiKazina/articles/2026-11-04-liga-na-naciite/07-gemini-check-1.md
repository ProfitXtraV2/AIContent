# 07 — Gemini Step-7 check — pass 1 (initial draft)

**Verdict: Shows mild AI patterns, 65% confidence.** → human-likeness = 100 − 65 = **35** (< 80 target).

Gemini (verbatim):

This article is highly factual, well-structured, and avoids the most egregious AI tropes (there are no emojis, no "In today's fast-paced world," and no "In conclusion"). The integration of responsible gambling language is also exceptionally natural. However, a trained eye can spot several classic LLM structural tells—specifically tautological filler sentences, over-stylized semantic bridges, and the tendency to end sections with slightly robotic, philosophical contrasts.

### 1. Formulaic Signposting / Setup Phrase
> Flagged: "Идеята е проста по замисъл: вместо товарни приятелски срещи без залог..."
> Pattern: LLMs frequently use "The idea is simple:" as a crutch to introduce an explanation.
> Recommendation: Delete the setup phrase entirely. Start straight from "Вместо...".

### 2. Over-stylized / Abstract Transitions (Semantic Bridging)
> Flagged: "Тук е и причината турнирът да тежи повече от едно спокойно състезание между почивките." AND "При Световното първенство връзката е подобна по дух:"
> Pattern: Slightly poetic/abstract phrases to glue factual sections. Too theatrical for a sports guide.
> Recommendation: Simplify to direct, sports-focused transitions. First: focus purely on the stakes. Second: remove "подобна по дух", just state the mechanism.

### 3. Tautological Filler (Stating the Obvious)
> Flagged: "Завършените издания имат ясни победители."
> Pattern: Classic AI zero-value topic sentence.
> Recommendation: Cut it. Start directly with "Португалия печели първото издание през 2019 г...".

### 4. The "Profound" AI Contrast Conclusion
> Flagged: "Миналите издания на Лигата на нациите носят точни дати и точни имена. Изходът от следващия мач не се знае предварително и никой залог не го гарантира."
> Pattern: AI loves a philosophical past/future contrast. "carry exact dates and exact names" sounds robotic.
> Recommendation: Keep the RG message, but rewrite in plain language (past stats don't guarantee future outcomes).

Note (Gemini): RG disclosures, 18+ markers, author bio at the bottom are perfectly formatted and compliant. Do not alter or remove any of this language during revisions.

→ Action: apply recs 1–4 via a FRESH Humaniser pass (step-7b), style-only, preserving every number/date/link/RG line/byline/brand. Then re-run gemini_check.py (pass 2).

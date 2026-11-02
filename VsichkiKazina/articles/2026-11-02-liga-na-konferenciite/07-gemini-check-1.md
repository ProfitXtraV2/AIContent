# 07 — Gemini check · pass 1 (initial draft)

**Verdict (verbatim):** Shows AI patterns, 85% confidence.
→ Normalized HUMAN-LIKENESS = 100 − 85 = **15**. Below target 80 → iterate.

Gemini's verbatim evaluation and recommendations:

---

### Verdict
**Shows AI patterns, 85% confidence.**
While the text is highly polished, avoids the most egregious AI buzzwords (like "в днешния забързан свят" / "in today's fast-paced world"), and integrates the responsible gambling messaging quite well, it relies heavily on structural AI tells. The pacing is overly rhythmic, paragraphs consistently end with neat "wrap-up" summaries, the text uses conversational filler to bridge data points, and it features the classic AI "philosophical contrast" conclusion.

### Flagged Passages & AI Patterns
1. **"Consult Official Sources" meta-disclaimer** — *"...затова актуалната разбивка по държави стои на официалния сайт на УЕФА, а не в статия, която бързо остарява."* Pattern: AI inserts self-aware meta-commentary apologizing for the medium. Humans just state the rule + link.
2. **Anthropomorphism & narrated emotion** — *"Тук Лигата на конференциите е щедра по свой начин..."* and *"За краткия си живот турнирът вече има пет имена на трофея."* Pattern: assigning human traits (generosity, having a "life") to a tournament.
3. **Philosophical / poetic conclusion** — *"Трофеите... вече носят точни имена и точни години. Следващият мач не носи такава сигурност..."* Pattern: the "tying the bow" balanced poetic contrast.
4. **Signposting & conversational filler** — *"Едно обаче липсва и е добре да се знае:..."* and *"...а любопитното е, че досега нито един клуб..."* Pattern: "it is good to know" / "the curious thing is" glue phrases.
5. **Paragraph wrap-up (over-explaining)** — *"Шест мача е по-малко от осемте... което е и едно от нещата, които отличават третото ниво."* Pattern: a concluding sentence summarizing its own paragraph.

### Concrete Recommendations
- Remove the self-aware "article ages quickly" justification; state the rule + link UEFA directly.
- Strip anthropomorphism: not "generous in its own way" → state the winner secures a Europa League spot; not "short life" → "Досега" / "От създаването си".
- Cut signposting ("е добре да се знае", "а любопитното е, че") — state facts plainly.
- Trim the six-vs-eight matches wrap-up in Форматът.
- Ground the conclusion: remove the poetic past-vs-future contrast; end on a direct practical RG-aligned note.

(Per instructions: RG language, disclosures, dates and the names/years in "Носителите досега" bypassed — untouched by the style edit.)

---

**Action:** apply recs via a fresh Humaniser pass (pipeline/prompts/step-7b-apply-gemini-recs.md),
preserving every number, link, RG line, date, byline and brand. Then Brand Gate re-check + re-run
gemini_check.py (pass 2). Keep-best currently = initial (HL 15).

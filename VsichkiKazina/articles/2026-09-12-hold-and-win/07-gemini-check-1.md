# 07 — Gemini cross-model check · PASS 1 (on as-delivered 05b)

Model: gemini-3.1-pro-preview · script: scripts/gemini_check.py · exit 0
Verdict raw: **"Shows AI patterns, 75% confidence."**
Normalized HUMAN-LIKENESS = 100 − 75 = **25** → below target 80 → iterate (humaniser pass 1).

## Verbatim Gemini output

Here is my evaluation of the article based on LLM writing patterns and AI text detection.

### **Verdict**
**Shows AI patterns, 75% confidence.**

While the Bulgarian grammar is excellent, the terminology is accurate, and the text flows logically, the underlying structural skeleton and specific stylistic quirks strongly point to an AI generation that has been well-prompted but not heavily human-edited for voice. It suffers from over-cautious disclaimers, a formulaic "summary" conclusion, and a tendency to end on a slightly poetic, philosophical note—all classic hallmarks of ChatGPT or Claude writing SEO content.

---

### **Flagged Passages and AI Patterns**

**1. Pattern: Over-cautious Parenthetical Disclaimers (Robotic Hedging)**
AI models, especially when prompted to be factual or avoid making false promises (common in gambling content), will obsessively flag hypothetical numbers.
*   *Quote:* "...Гранд 2000x залога **(примерни числа)**."
*   *Quote:* "...тоест 507x залога **(пример)**, а не всяка поотделно."
*   *Quote:* "...петнайсет позиции за покриване **(пример)**."
*   *Quote:* "Гранд джакпотът от 2000x залога **(пример)** е точно толкова голям..."

**2. Pattern: The "Philosophical/Poetic" Wrap-Up**
AI struggles to just *end* an article. It almost always attempts to tie the technical explanation to a sweeping, slightly dramatic human emotion or poetic metaphor in the final sentence.
*   *Quote:* "Гранд числото свети еднакво силно за всички, а колко пъти ще светне за теб, го решават респините, не желанието ти да го хванеш."

**3. Pattern: The "In Conclusion" Summary Pivot**
Even when you don't use the header "Заключение", AI will start the final section by summarizing the entire article before moving on to the actual point of the paragraph.
*   *Quote:* "Hold & Win е добре направен бонус рунд, който превръща три завъртания в малък спектакъл със заключени монети и събиращи се числа. Това е и цялата му работа: да задържи вниманието ти, докато математиката тече по познатия начин."

**4. Pattern: The "Insider Secret" Signposting**
AI often tries to sound authoritative by creating a strawman (like "ads" or "myths") to debunk, using very specific, slightly dramatic phrasing.
*   *Quote:* "Тук е разликата, която рекламите обичат да замъглят."

---

### **Concrete Recommendations**

To make this read like it was written by a human expert rather than an LLM, apply the following adjustments:

*   **Scrub the redundant parentheses:** You already use natural human hedging like "да речем" (let's say) and "Илюстративно" (illustratively). Because you've already established these are examples, delete every instance of "(пример)" and "(примерни числа)". A human writer trusts the reader to understand context; an AI does not.
*   **Kill the poetic final sentence:** Delete the sentence starting with "Гранд числото свети еднакво силно...". It sounds like a fortune cookie. *(Note: Do not touch the 18+ warnings, the responsible gambling links, or the advice to set limits right before it—those are perfect. Just remove the poetic metaphor at the very end).*
*   **Trim the summary in the final H2:** In the section "Как да го гледаш разумно", delete the first two sentences that summarize what Hold & Win is. Start the paragraph directly with the actionable advice: "Пусни играта в демо режим и ще видиш..." This breaks the predictable AI essay structure.
*   **Soften the dramatic transition:** Change "Тук е разликата, която рекламите обичат да замъглят" to something more conversational and less cliché, such as "Важно е да се прави разлика между тези механики" or simply start directly with "Джакпотите в Hold & Win почти винаги са фиксирани..."
*   **Vary the sentence rhythm in the "Пълна решетка" section:** The sentences "Или изтичат респините, и тогава... Или монетите запълнят цялата решетка..." use a very rigid, balanced parallel structure that AI favors. Consider combining them into a more fluid, single sentence (e.g., explaining that the round ends either when respins run out or the grid fills up, triggering the top jackpot).

*(Note: The boilerplate disclosures, author tags, and responsible gambling blocks at the bottom are standard compliance elements and do not trigger AI detection in a negative way. Leave them exactly as they are.)*

## Disposition for humaniser pass 1
- Parenthetical hedging: brand REQUIRES illustrative figures to stay MARKED (author.md guardrail).
  So NOT deleted outright — converted to natural in-line hedging („да речем", „илюстративно",
  „например", „в този пример") so each figure stays clearly illustrative while the robotic
  repeated „(пример)" tell is removed. Numbers themselves unchanged (20x/50x/500x/2000x, 507x, 15).
- Poetic final sentence: replaced with a blunt, opinionated, non-poetic verdict (asymmetric,
  no antithesis). RG advice before it untouched.
- Final-H2 summary pivot: first two sentences dropped; section now opens on the demo advice.
- Strawman transition: removed; §5 opens directly on the fact.
- „Или… Или…" parallel: merged into one fluid sentence.
- UNTOUCHED: all numbers, 4 internal links, RG/18+ lines, disclosures, dates, byline, brand.

# 07 — Gemini Step-7 check — pass 1 (initial draft)

Normalized human-likeness: **25** (verdict "Shows AI patterns, 75% confidence" → 100 − 75).
Result: below GEMINI_TARGET_CONFIDENCE (80) → iterate (humaniser pass 1).

## Gemini verbatim verdict + recommendations

**Verdict: Shows AI patterns (Likely AI-generated with strong human editing / Hybrid), 75% confidence.**

This is a highly polished, well-localized text. The Bulgarian is natural, the terminology is accurate, and it successfully avoids the most glaring AI clichés (e.g., "В днешно време", "Нека се потопим", "В заключение"). The author has clearly done a good job guiding the output or editing it post-generation.

However, the underlying skeleton of the article still relies heavily on LLM structural habits. It suffers from compulsive signposting, repetitive contrast patterns ("X looks good, but Y"), generic introductory padding, and the classic AI tendency to wrap up every single section with a neat, moralizing micro-conclusion.

### 1. The "Illusion vs. Reality" Contrast (Formulaic Structure)
AI models love to set up a strawman of "this looks appealing" only to knock it down with a "but actually..." reality check. When used once, it's fine; when used repeatedly, it creates a predictable, robotic rhythm.
- Flagged text 1: "Числата в долния край на таблицата изглеждат примамливо, но зад тях стоят съответно малки вероятности..."
- Flagged text 2: "Изгодно изглежда само докато дилърът се квалифицира."
- Flagged text 3: "Изглежда като шанс за голям удар срещу един залог, но цената е висока..."
- Recommendation: Break this repetitive contrast rhythm. Instead of telling the reader how things "look," just state the reality directly.

### 2. Compulsive Signposting (Hand-holding)
LLMs frequently tell the reader what they are about to read or explicitly instruct them to remember something for later.
- Flagged text 1: "По-нататък са правилата, от раздаването до честната сметка колко струва играта в дългосрочен план."
- Flagged text 2: "Това е важно за сметката по-нататък: когато останете в ръката..."
- Recommendation: Remove the meta-commentary.

### 3. Generic Introductory Padding
When starting a new concept, AI often relies on a broad, universal truth to "warm up" the paragraph before getting to the actual point.
- Flagged text: "Всяка игра в казино е построена така, че операторът печели в дългосрочен план, и карибският покер не е изключение. При правилна игра домашното предимство е 5,224% върху анте."
- Recommendation: Cut the universal generalization; start directly with the specific data.

### 4. Repetitive Micro-Conclusions (The "Wrap-up" Pattern)
AI summarizes the "takeaway" at the end of almost every section; the same point about strategy not overcoming the house edge is made in two consecutive sections.
- Flagged (End of Section 7): "Никаква стратегия не обръща знака: доброто решение смъква част от загубата и дотам."
- Flagged (End of Section 8): "Същественото е, че стратегията ограничава щетата, но не сменя посоката..."
- Recommendation: Choose one place to make this point and delete the other; keep it in the strategy section.

(Note: RG language, 18+ markers and legal disclaimers left entirely out of the critique per the hard rules.)

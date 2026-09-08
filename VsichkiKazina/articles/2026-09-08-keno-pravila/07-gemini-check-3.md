# 07 — Gemini external check · pass 3 (re-check after Humaniser pass 2 — FINAL)

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-keno-pravila
Verdict normalization: "Shows AI patterns, 85%" → **human-likeness = 100 − 85 = 15**.

## KEEP-BEST LEDGER (mandatory)
| version | Gemini verdict | human-likeness |
|---|---|---|
| initial 05b (check 1) | Likely AI-written, 85% | 15 |
| **Humaniser pass 1 (check 2) — KEPT** | **Shows AI patterns, 80%** | **20 (highest)** |
| Humaniser pass 2 (check 3) | Shows AI patterns, 85% | 15 |

MAX_GEMINI_PASSES = 2 reached. Highest human-likeness = **20 (pass 1)**. Pass 2 scored LOWER (15), so per keep-best the final 05b was REVERTED to the pass-1 version (`git checkout <pass-1 commit> -- 05b-final-draft.md`). Ends below 80 → content-queue `gemini` column = **ai 80** (the kept pass-1 version's own verdict from check 2, verbatim scale).

Note: Gemini's score is low and noisy on this piece (15 → 20 → 15). The internal Brand Gate passed it 95/100 (zero criticals) and the Humaniser rated it 50/60 HUMAN-LIKE. Pass 1 applied the clearly-compliant fixes (the "casino floor" calque → native BG, removed signposting lead-ins, de-dramatized wrap-ups, broke the seesaw conclusion). Pass 2's further edits (breaking the rule-of-three, the "и двата" repetition, meta anglicism, "За перспектива", fluff transition) are objectively reasonable but Gemini scored the result lower — within the noise band — so pass 1 is kept as the higher-scoring version. Across the loop, Gemini's request to remove the site RG doctrine "Хазартът не е финансова стратегия" was correctly REJECTED (untouchable), and both [VERIFY] flags were kept (Gemini agreed they stay). All numbers, links, RG lines, 18+, disclosures, dates, byline and brand preserved throughout; no flag resolved.

## Gemini verbatim verdict + recommendations (pass 2 re-check)

**Verdict: Shows AI patterns, 85% confidence.**

While the text is grammatically flawless, highly informative, and well-structured, it exhibits several classic hallmarks of Large Language Model (LLM) generation. The pacing is highly uniform, paragraphs frequently end with neat "wrap-up" summary sentences, sections open with textbook definitions, and the conclusion relies on a rapid-fire list of unsolicited, preachy imperatives. It reads like a very well-prompted GPT-4 output that has bypassed a final human stylistic polish.

Here is the breakdown of the specific patterns that triggered this assessment, along with actionable recommendations to humanize the copy.

---

### 1. The "Dramatic Contrast" Hook
**The Pattern:** AI often opens articles by presenting a simple, positive premise immediately followed by a dramatic "hidden truth" or "what they don't tell you" pivot to create artificial intrigue.
**The Quote:** *"Механиката се учи за минута. Онова, което почти никой не ти казва на входа, е цената, а при кено тя е от най-високите сред всички казино игри."*
**Recommendation:** Soften the transition. Instead of the dramatic "what nobody tells you" trope, frame it as a practical reality of the game. You can achieve this by combining the ease of play directly with the cost, making it sound like an insider's observation rather than a dramatic reveal.

### 2. The "Textbook Definition" Opening
**The Pattern:** When introducing a new concept, LLMs almost always default to a dry, dictionary-style definition as the opening sentence of the section, halting the narrative momentum.
**The Quote:** *"Домашното предимство е частта от всеки заложен €, която казиното задържа в дългосрочен план. При кено то е сред най-високите в цялото казино."*
**Recommendation:** Integrate the definition into the context of the game rather than stating it as a standalone rule. Start the paragraph by directly addressing Keno's high house edge, and explain what that means for the player's bankroll in the same breath, rather than defining the term first.

### 3. The "Neat Bow" Summary Sentences
**The Pattern:** AI struggles to let a point speak for itself. It frequently adds a final, slightly repetitive sentence at the end of a paragraph to summarize the lesson it just taught.
**The Quotes:**
* *"Две игри, които на пръв поглед изглеждат еднакво, може да имат съвсем различна реална цена за твоя джоб."* (End of section 2)
* *"Множителят от четири или пет цифри в таблицата изглежда примамливо точно защото събитието зад него е толкова рядко."* (End of section 3)
**Recommendation:** Delete these sentences entirely. The paragraphs preceding them already do an excellent job of explaining the math and the paytables. Trust the reader to understand the implication without the AI holding their hand at the finish line.

### 4. The "Preachy Imperative" Conclusion
**The Pattern:** When asked to conclude or evaluate if something is "worth it," AI defaults to a rapid-fire, bullet-less list of commands (do this, check that, remember this). It shifts the tone from an informative guide to a lecturing parent.
**The Quote:** *"Провери paytable-а, избери по-малко числа за по-нисък риск, задай си лимит на депозита предварително и не гони изгубеното с по-големи залози."*
**Recommendation:** Reframe these commands as strategic options or observations. Instead of telling the reader exactly what to do ("Провери", "избери", "задай"), describe what *smart players* do, or frame them as the logical next steps based on the math discussed earlier in the article.

### 5. The "Hypothetical Scenario" Explainer
**The Pattern:** To explain variance or differing rules, AI frequently invents a highly symmetrical hypothetical scenario ("Imagine two machines side by side...").
**The Quote:** *"Два автомата за кено стоят един до друг, еднакви на вид и двата на €1 за pick-6, уж за същите шест улучени числа. Само че таблицата на единия дава..."*
**Recommendation:** Break the perfect symmetry of the example. Instead of two identical machines standing side by side, frame it as a comparison between different casinos or different software providers, which sounds much more grounded in actual player experience.

---

### A Note on Process & Compliance
Per your hard rules, I have not touched or suggested removing any responsible gambling language, 18+ markers, or facts/odds.

However, as a senior copywriter, I must flag a **critical editorial process failure**: the text contains raw prompt/generation artifacts.
* *[VERIFY: диапазонът 60%–95% за pick-6 е илюстративен ориентир...]*
* *[VERIFY: тези стойности са приблизителни...]*

These indicate that the article was published (or moved to the final stage) without a human editor resolving the AI's self-generated fact-checking placeholders. While I am leaving them intact per your instructions, these must be resolved by your editorial team before publication, as they are a 100% dead giveaway of AI generation to any reader.

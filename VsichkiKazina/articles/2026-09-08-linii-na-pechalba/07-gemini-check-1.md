# 07 — Gemini external check · pass 1 (initial 05b) — PASS

Model: gemini-3.1-pro-preview · run 2026-09-08 · article: 2026-09-08-linii-na-pechalba
Verdict normalization: "Highly likely human-written, 90% confidence" → **human-likeness = 90 ≥ GEMINI_TARGET_CONFIDENCE (80) → PASS**.

## KEEP-BEST LEDGER
| version | Gemini verdict | human-likeness |
|---|---|---|
| **initial 05b (check 1) — KEPT** | **Highly likely human-written, 90%** | **90 (PASS)** |

PASS on the first read; no Humaniser re-pass run (none needed). content-queue `gemini` column = **human 90**. Gemini's optional style suggestions below were NOT applied (the piece already passed ≥80; changes are not required and each carries regression risk). All numbers, links, RG lines, 18+, disclosures, dates, byline and brand stand as written; 0 in-text flags (all figures are stable game-math — 243=3⁵, 1024=4⁵, 117 649=7⁶ — or cited, web-verified LDW research: Dixon et al. 2010 skin-conductance, Graydon et al. 2018 "58% chose the 115% PB LDW game" [PMC6209046, orchestrator-verified], Jensen et al. 2013 win-overestimation).

## Gemini verbatim verdict + recommendations (optional; not applied — PASS)

**Verdict: Highly likely human-written, 90% confidence.**

This is an exceptionally strong piece of copy. It completely avoids the typical AI hallmarks in Bulgarian (e.g., fluffy intros like "В днешно време...", robotic transitions, or overly enthusiastic adjectives like "вълнуващ" and "незабравим"). The writer uses a cynical, realistic tone ("скучна аритметика", "Загуба, облечена като печалба") and brilliant, natural metaphors ("психологически хлъзгави") that LLMs almost never generate organically.

However, if you run this through a strict AI detector, a few structural choices might trigger false positives because they mimic the organizational patterns of advanced LLMs (especially RAG models like Perplexity or GPT-4 with web browsing).

Here are the specific passages that share structural DNA with AI patterns, along with recommendations to humanize them further.

### 1. Pattern: The "Actionable Pivot" Subheading
* **The Quote:** `## Какво да гледате вместо броя линии`
* **Why it flags:** AI models are programmed to be helpful. After explaining a concept or a problem, they almost always pivot to a neat, actionable "What to do instead," "What to consider," or "Key takeaways" section right before the conclusion. This specific phrasing is a very common LLM structural crutch.
* **Recommendation:** Change the subheading to a declarative statement rather than a "how-to" guide prompt. Make it sound like a continuation of the author's argument rather than a textbook chapter. (e.g., frame it around the reality of RTP and cost per spin, rather than "what to look at").

### 2. Pattern: RAG-Style Parenthetical Citation Clustering
* **The Quote:** `(Dixon и колектив, 2010)` ... `(Graydon и колектив, 2018)` ... `(Jensen и колектив, 2013)`
* **Why it flags:** While the research is excellent (and per your rules, I am not questioning the facts or dates), stacking three parenthetical academic citations in a single paragraph is exactly how AI models with web-browsing capabilities format their summaries. It reads like an AI-generated literature review rather than a journalistic article.
* **Recommendation:** Weave the citations directly into the narrative flow. Instead of using brackets at the end of the sentence, suggest mentioning the researchers or the year naturally within the text (e.g., "As a 2010 study by Dixon and his team showed..." or "Research from 2018 found that..."). This shifts the tone from an academic/AI summary to human journalistic reporting.

### 3. Pattern: The Symmetrical, Aphoristic Closing Sentence
* **The Quote:** `Ако избирате игра по броя линии на банера, избирате по грешното число.`
* **Why it flags:** LLMs struggle to just *stop* talking. They are trained to tie a neat bow on the topic using balanced, symmetrical sentences (If X, then Y) that sound slightly preachy or aphoristic.
* **Recommendation:** Break the symmetry. Suggest ending on a slightly more abrupt, punchy note about the reality of the math, rather than a perfectly balanced "If/Then" proverb. Leave the responsible gambling transition exactly as it is, but make the final sentence of the author's actual copy less neatly packaged.

### 4. Pattern: Didactic Math Explanation Rhythm
* **The Quote:** `Три по три по три по три по три прави 243 възможни комбинации. 1024 начина е същата идея, но с по четири символа на височина, тоест четири на пета степен.`
* **Why it flags:** This is a minor flag, but the staccato, repetitive rhythm of the math breakdown ("Три по три по три...") followed immediately by the "X is the same idea, but Y" formula is a very common way LLMs simplify math for readers.
* **Recommendation:** Suggest combining these two thoughts to make the rhythm less robotic. The math is correct and shouldn't be changed, but the delivery can be smoothed out so it reads less like a step-by-step AI tutorial and more like a casual observation.

*(Note: The responsible gambling boilerplate, 18+ markers, and affiliate disclosures at the bottom are standard compliance text. They are perfectly placed and should remain completely untouched.)*

## Decision
PASS (human-likeness 90 ≥ 80) on pass 1 → keep the initial 05b unchanged. gemini column = human 90. No Humaniser re-pass needed or run.

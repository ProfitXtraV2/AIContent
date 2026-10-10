# Step 7 — Gemini cross-model check — PASS 1 (initial 05b)

Command: `python3 scripts/gemini_check.py 05b-final-draft.md`
Date: 2026-10-10 (cloud reconcile of HANDOFF row)

## Verdict (verbatim)

→ Normalized HUMAN-LIKENESS = 100 − 80 = **20**  (PASS threshold = 80) — needs changes

---

**Verdict: Likely AI-generated or heavily AI-assisted, 80% confidence.**

While the article is highly informative, well-researched, and correctly utilizes Bulgarian legal terminology, its structural and stylistic DNA strongly points to a Large Language Model. The text relies heavily on classic LLM crutches: overt signposting, rhetorical conversational pivots, formulaic bolding, and a slightly preachy, didactic conclusion. 

Additionally, as a process note: there are multiple `[VERIFY: ...]` tags left in the final text. Per your instructions, I am noting this as a workflow/editorial oversight, but my recommendations below will not suggest removing them or the responsible gambling language.

Here is the breakdown of the AI patterns and how to fix them.

### 1. Pattern: Overt Signposting / Meta-discourse
**The Flagged Passage:** 
> "Статията обяснява какво е хазарт според българския закон, кои са петте вида, какво е разрешено онлайн, кой издава лицензите и от колко години се играе. Не покрива данъка върху печалбите, правилата на отделните игри и оценки на конкретни оператори, и не замества правна консултация по конкретен случай."

**Why it reads as AI:** 
LLMs are programmed to be aggressively helpful and structured. They almost always include a "table of contents" paragraph at the end of the introduction telling the reader exactly what the article will do, often using the third person ("This article explains..."). Human writers usually hook the reader and transition naturally into the first point.

**Recommendation:** 
Delete the first sentence of this paragraph entirely. You don't need to tell the reader what the article explains; the headings already do that. Keep the second sentence (the disclaimer about what it *doesn't* cover and the legal disclaimer), but attach it to the end of the first paragraph or frame it as a standard editorial note rather than a summary of the text.

### 2. Pattern: The Rhetorical "Yes" / Conversational Pivot
**The Flagged Passage:** 
> "Да, покерът е хазарт по смисъла на ЗХ." *(Under the heading: Хазартна игра на карти: покерът е игра в казино)*

**Why it reads as AI:** 
AI models frequently use a conversational, rhetorical Q&A style to transition between ideas, even when no question was asked in the preceding text. Starting a paragraph with "Yes, [statement of fact]" is a very common LLM rhythm used to simulate an engaging tone, but in a legal/informational text, it feels forced and robotic.

**Recommendation:** 
Remove the conversational "Да," and state the fact directly with authority. Start the sentence directly with "Покерът е хазартна игра по смисъла на ЗХ." 

### 3. Pattern: The Didactic / Moralizing Wrap-up
**The Flagged Passage:** 
> "Печеливша игра в този списък няма. Като играч разполагате с един лост: знанието какво позволява законът (вид, лиценз, евро, 18+). Струва си да го имате още преди първия залог."

**Why it reads as AI:** 
Because LLMs are heavily aligned with safety guidelines (especially regarding gambling), they tend to end articles with a philosophical, slightly preachy, or moralizing summary. The metaphor of the "single lever" (един лост) and the conclusive "It's worth having before your first bet" is classic AI wrapping up a topic with a neat, cautious bow.

**Recommendation:** 
Tone down the philosophical metaphor. Instead of talking about "levers" and what is "worth having," rephrase this to be strictly objective. State plainly that understanding the legal framework (licenses, currency, age limits) is the primary way players can ensure they are using regulated platforms. 

### 4. Pattern: Formulaic, Echoing FAQs
**The Flagged Passage:** 
> **Какво е хазарт?**
> Всяка игра на случайността...
> **Кои са видовете хазартни игри?**
> Лотарийни игри, залагания на спорт...
> **Кои хазартни игри са разрешени онлайн?**
> И петте вида, без томболата...

**Why it reads as AI:** 
When asked to generate an FAQ section, AI typically just regurgitates the exact H2s from the article and summarizes the paragraphs beneath them. A human writing an FAQ usually addresses long-tail search queries, edge cases, or practical user questions that weren't explicitly the main headers of the text.

**Recommendation:** 
Revise the FAQ questions to sound like actual queries a user would type into Google, rather than academic prompts. For example, instead of "Кои са видовете хазартни игри?" (which just repeats the H2), change it to something more user-centric like "Мога ли да играя легално онлайн лотария в България?". Keep the factual answers exactly the same, just change the framing of the questions so they don't perfectly mirror the article's table of contents.

# 07 — Gemini check, pass 1 (initial draft 05b)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-28-tenis-pravila-tochkuvane/05b-final-draft.md`

Normalized human-likeness: **85** ("Likely human-written, 85% confidence") → **PASS** (≥ 80).

## Gemini verbatim verdict + recommendations

**Verdict: Likely human-written (or heavily human-edited), 85% confidence.**

This article reads exceptionally well and contains highly idiomatic Bulgarian phrasing ("да откъсне два пъти един след друг", "доста по-приземен въпрос") that AI models rarely generate organically. Furthermore, the compliance and responsible gambling sections are deeply localized to Bulgarian law (mentioning НАП and specific 2026 legislation), which points to a human expert.

However, there are a couple of lingering structural "tells" in the introduction and body copy that are classic LLM writing patterns. These minor flaws give the text a slight AI-assisted flavor in specific spots.

### Flagged Passages & AI Patterns

**1. The Formulaic Signpost (Introductory Paragraph)**
> *Flagged text:* "По-долу е как се играе и как се точкува тенис, стъпка по стъпка."
> *Pattern:* **AI Signposting / The "Step-by-Step" Promise.** LLMs are programmed to be relentlessly helpful, which often results in them ending introductions by explicitly announcing what the rest of the article will do. It kills the natural momentum of a good hook.

**2. The Conversational Pivot (Section: Корт, настилки...)**
> *Flagged text:* "А странната стълбица 15-30-40? Най-разпространеното обяснение я свързва с циферблат на часовник..."
> *Pattern:* **The Rhetorical Question Transition.** AI models frequently use rhetorical questions to pivot to a new subtopic or introduce a "fun fact." A synthetic way of creating conversational engagement; reads as a classic trope.

**3. The Didactic "Teacher" Tone (Section: Как се брои един гейм)**
> *Flagged text:* "Дотук е просто броене с необичайни имена. Усложнението идва при 40-40..."
> *Pattern:* **Narrated Explanation.** Not exclusively an AI trait; combined with the signposting above it contributes to a slightly lecture-like rhythm. (Gemini: leave as is once the intro signpost is removed.)

### Concrete Recommendations
- Delete the final sentence of the intro ("По-долу е как се играе и как се точкува тенис, стъпка по стъпка."); end on the punchy hook.
- Convert the rhetorical question into a declarative statement ("Що се отнася до странната стълбица 15-30-40, най-разпространеното обяснение я свързва с...").
- Leave the didactic passage as is.

**Compliance note (Gemini):** RG language, 18+ markers, 2026 budget-law disclosures, and internal links are perfectly integrated. Per hard rules, do not touch or alter any of this text.

## Decision
Pass 1 already PASSES (85). Both flagged items (1 + 2) are genuine anti-AI tells the Brand Gate
itself bans (signposting lead-in + rhetorical-question pivot). Applying ONLY recs #1 and #2 via a
fresh Humaniser pass (step-7b): style-only, preserves every number, link, RG line, date, byline,
brand. Keep-best after re-check. (Fact/RG/link text untouched per the compliance note.)

# 07 — Gemini check, pass 2 (after humaniser pass 1)

Model: gemini-3.1-pro-preview · verdict scale normalized: „Likely AI-written (Heavily Prompted), 85% confidence" = AI-patterns verdict at 85% → **human-likeness = 100 − 85 = 15**. LOWER than pass 1 (HL 25) → detector noise / over-edit risk. Below target 80. One humaniser pass remains (cap 2); attempt structural fix, then keep-best.

## Gemini verbatim verdict + recommendations

**Verdict: Likely AI-written (Heavily Prompted), 85% confidence.**

This article is a classic example of a "high-quality" AI generation. It avoids the usual flowery, hyped-up casino marketing language (which is great), but it falls into a different trap: **structural looping**. It reads exactly like an LLM given a strict system prompt to "be objective, explain the math, avoid hype, and remind the reader of the house edge," applied rigidly to every paragraph → predictable, formulaic rhythm.

### 1. The "Reality Check" Paragraph Closers (Formulaic Structural Looping)
Pattern: almost every section ends on a sobering mathematical reality-check.
Evidence: intro „…математиката отдолу е същата…"; H2-1 „…а казиното е операторът…"; H2-3 „…каквото пише."; H2-4 „…а само добавя резки колебания…"; H2-5 „…към един голям, рядък изход."; H2-7 „…не бива да се планира като реалистичен резултат."
Rec: break the loop — move some disclaimers into paragraph middles; let a few paragraphs end on a neutral/descriptive note.

### 2. The "Assumptive Hook" (Conversational AI Intro)
Evidence: „Ако си въртял ротативки в българско лицензирано казино, почти сигурно си минавал покрай логото на BF Games…"
Rec: cut the hypothetical scenario; open on concrete facts (Book-of line / 2013 UK origins).

### 3. Robotic Data Recitation (List-to-Prose)
Evidence: „…Lucky Tropics връща 97.00%, Aztec Adventure 96.22%, Buffalo Trail 96.16%, Book of Gods 96.12%, Cave of Fortune 96.04%, а Book of Gates 96.03%."
Rec: regroup narratively — most hover around 96%, Lucky Tropics the outlier at 97.00%. Keep all exact numbers; vary the structure.

### 4. Didactic Contrast (Over-explaining / Signposting)
Evidence: „Това не е лиценз за казино и не е лиценз за игра в България; това е лиценз, който позволява…"
Rec: state what the licence IS, not what it isn't.

*Process note: [VERIFY], 18+, RG boilerplate noted and intentionally left untouched.*

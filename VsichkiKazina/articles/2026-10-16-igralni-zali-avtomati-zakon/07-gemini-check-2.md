# 07 — Gemini external check — PASS 2 (after humaniser pass 1)

**Date:** 2026-10-16 · **Script:** `scripts/gemini_check.py 05b-final-draft.md`
**Verdict (verbatim):** Shows strong AI patterns, 85% confidence.
**Normalized human-likeness:** 100 − 85 = **15** (flat vs baseline HL15; detector shifting goalposts — flagged new passages after pass-1 fixes). Below target 80 → one more humaniser pass (cap=2).

---

## Gemini verbatim output (pass 2)

**Verdict: Shows strong AI patterns, 85% confidence.**

Formulaic skeleton: "roadmap" introduction, forced conversational idioms mixed with dry legal text, dramatic anthropomorphizing of the law, "neat-bow" summary at the end.

### 1. The "Neat-Bow" Summary (Formulaic Conclusion)
Flagged: „Петте опорни точки, лиценз от НАП за всеки вид игра, капитал от 750 000 лв. за автоматите, само пълнолетни, 300 метра отстояние и изпитано оборудване, тежат пред закона еднакво. Зала, която ги покрива, е легална. Пропусне ли дори една, вече не е."
Rec: delete the recap; let the final paragraph start directly with the internal-linking sentence.

### 2. Forced Conversational Clichés & Idioms
Flagged: „...липсата му е червен флаг." · „Видите ли точно такава, разположението ѝ куца." · „Нито един от тези белези не е козметичен..."
Rec: replace clichés with straightforward professional language (direct violation of the law; venue operating illegally; remove the "не е козметичен" filler).

### 3. The "Roadmap" Thesis Statement (Signposting)
Flagged: „В Закона за хазарта (ЗХ) изискванията са подредени именно около този въпрос: кой стои зад залата, с какъв капитал, къде е разположена и кого допуска вътре."
Rec: cut this preview sentence.

### 4. Over-Dramatizing Legal Facts
Flagged: „Чл. 3 ЗХ е категоричен:" · heading „Капиталовият праг отсича любителите" · „Това е устойчивото ядро на чл. 44 ЗХ."
Rec: „Според Чл. 3 от ЗХ..."; heading → objective „Изисквания за минимален капитал"; „устойчивото ядро" → „основното правило".

### 5. Over-Explaining the Obvious (Filler Logic)
Flagged: „Зад всяка законна зала трябва да стои дружество с реален капитал на тези нива, а фирма, отворена за месец, просто не стига прага."
Rec: remove the second half ("а фирма, отворена за месец...").

*(Gemini note: [VERIFY] tags, 18+ RG markers, author/affiliate disclosures all intact and correctly formatted; do not touch them.)*

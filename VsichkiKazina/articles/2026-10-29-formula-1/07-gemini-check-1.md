# 07 — Gemini check, pass 1 (initial draft)

Command: `python3 scripts/gemini_check.py VsichkiKazina/articles/2026-10-29-formula-1/05b-final-draft.md`
Exit: 0

Normalized human-likeness = **90** (verdict „Likely human-written, 90% confidence") → **PASS**
(≥ GEMINI_TARGET_CONFIDENCE 80) on the INITIAL draft. No humaniser pass required.
Keep-best = initial draft (HL 90). gemini column = `human 90`.

Recommendations are style-only; Gemini explicitly says to leave the RG section, affiliate
disclosures and footer untouched. Since the draft already PASSES at 90, no changes applied
(applying optional nits risks lowering the score, and keep-best protects the 90 version).

---

VERBATIM VERDICT + RECOMMENDATIONS:

**Verdict: Likely human-written (or heavily human-edited), 90% confidence.**

This article is exceptionally clean and avoids almost all common AI pitfalls. It lacks the typical AI fluff, avoids cliché sports metaphors (no "high-octane thrills," "buckle up," or "roaring engines"), and features a distinct, pragmatic editorial voice.

The strongest human indicators are the meta-commentaries and first-person interventions, such as:
*   *"...затова за актуалната решетка на даден сезон е по-сигурно да се погледне официалният сайт, вместо да се помни наизуст."*
*   *"...затова не ги изписвам тук; за тях официалният сайт винаги е по-точен от която и да е статия."*
*   *"Какво точно е законно е отделен и доста по-приземен въпрос..."*

AI models almost never write with this level of practical, user-focused self-awareness unless heavily prompted. However, there are a few structural and phrasing remnants that still carry a slight "SEO-template" or "Wikipedia-bot" scent.

### Passages and Patterns Flagged

1. Formulaic Structure / Glossary Outline — the sequence of H2s (Какво е Формула 1 / Двете титли /
   Как се точкува / Спринтът / Отборите и болидите) reads as a compartmentalized glossary.
2. Didactic / Wikipedia-Translated Phrasing — „Формула 1 е най-горното ниво на едноместните
   болиди с открити колела…" reads like a literal translation of the EN Wikipedia intro.
3. Signposting / Filler Transition — „Класическият уикенд върви на етапи." announces what it is
   about to do.

### Concrete Recommendations
- Make subheadings more conversational / combine them for flow.
- Soften the „Какво е Формула 1" opening away from the technical-manual definition.
- Delete „Класическият уикенд върви на етапи." and start directly with „В петък има две свободни тренировки…".

(Note: RG section, affiliate disclosures and footer are perfectly integrated and compliant — do not alter.)

---
DECISION: PASS at HL 90 on pass 1. Keep initial. No humaniser pass (keep-best protects 90).

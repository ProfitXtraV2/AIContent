# 07 — Gemini check · pass 2 (after humaniser pass 1 applying check-1 recs)

Model: gemini (cross-model external check) · script: scripts/gemini_check.py
Verdict (verbatim): **Likely human-written, 90% confidence.**
Normalized human-likeness = **90**. ≥ GEMINI_TARGET_CONFIDENCE (80) → **PASS**.

## KEEP-BEST decision
- Baseline (initial draft): „Shows AI patterns 85%" → HL 15.
- Humaniser pass 1 (apply check-1 recs): „Likely human-written 90%" → HL **90**.
- Highest human-likeness seen = **90** (pass 1). Final 05b = pass-1 content. gemini column: **human 90**.
- Loop ends at PASS on the first pass (1 of MAX_GEMINI_PASSES=2 used).

## Gemini verbatim assessment
Verdict: Likely human-written, 90% confidence.
This article reads exceptionally well and avoids almost all typical LLM pitfalls (no „В днешния
забързан свят" intros, no „Важно е да се отбележи" transitions, no overly flowery adjectives).
Natural Bulgarian idioms („не е от вчера", „доста по-приземен въпрос") and a pragmatic, slightly
cynical tone in the gambling section („малко трезва математика", „единствената гаранция в цялата
схема") that AI almost never generates on its own.

Minor residual patterns Gemini noted (NOT blocking — already a PASS; recorded for the trail):
1. „Broader significance" wrap-up: „...присъствие на сцена, запазена обикновено за имена с по-дълга
   история и по-голям бюджет."
2. „Journey/contrast" wrap-up: „По европейските мерки е малка, но се оказа достатъчна... в град,
   който допреди едно поколение не играеше в А група."
3. „Robotic data dumping": the nine-Supercup year list could be grouped.

Gemini explicitly praised the RG/gambling section as „top-tier human copywriting — do not touch"
and confirmed the RG/18+/affiliate blocks compliant and untouched. Style-only recommendations.

## Decision
PASS at HL 90. No further humaniser pass required (would risk lowering HL per keep-best). The minor
year-grouping/wrap-up notes are left as-is: the piece already clears the bar and the facts (every
Supercup year, the capacity, the European context) must stay verbatim and complete. Numbers, links,
RG lines, dates, byline and brand name preserved across all passes.

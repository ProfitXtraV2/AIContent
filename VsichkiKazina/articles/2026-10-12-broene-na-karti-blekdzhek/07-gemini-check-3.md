# 07 — Gemini Step-7 external check — PASS 3 (after humaniser pass 2) + KEEP-BEST decision

Tool: `python3 scripts/gemini_check.py 05b-final-draft.md` · exit 0 · date 2026-10-12

**Normalised result:** Verdict „Likely AI-generated base with heavy human editing (Cyborg/Hybrid), 70% confidence of AI origins." → treated as AI-patterns 70% → HUMAN-LIKENESS = 100 − 70 = **30** (< 80).

## KEEP-BEST (mandatory) — loop ended at MAX_GEMINI_PASSES (2)
| version | human-likeness |
|---|---|
| initial 05b (pass 0) | 25 |
| humaniser pass 1 | 15 |
| **humaniser pass 2 (KEPT)** | **30** |

Pass 2 (HL 30) is the highest human-likeness seen → it is the final 05b (current file). No revert needed.
`content-queue.gemini` = **`ai 70`** (winning version's own verdict, verbatim scale: 100 − HL = 70).

Note: the detector relocates its goalposts each pass (pass-1 flagged signposting/idioms/„Накратко"; pass-2 flagged „ръб"/„Затова"; pass-3 flags „didactic over-explanation"/„symmetrical wrap-ups"). This neutral, math-dense explainer plateaus in the 15–30 band regardless, matching prior guides (vk-0063 flat 15/25; vk-0266 initial 15). Human editor attention advised at Step 6; facts, flags, RG, disclosures all intact and untouched throughout. Recommendations are style-only; Gemini never touched a fact or a flag.

---

## VERBATIM GEMINI VERDICT (pass 3)

**Verdict: Likely AI-generated base with heavy human editing (Cyborg/Hybrid), 70% confidence of AI origins.**

This is a high-quality text. The writer (or prompter) successfully avoided the most egregious AI clichés (there is no "Вълнуващият свят на блекджека..." or "В заключение..."). It even uses excellent, natural-sounding Bulgarian idioms like "размазани в шест неизиграни тестета" and "тестето е олекнало".

However, the underlying skeleton still exhibits classic LLM patterns: structural rigidity, didactic over-explanation (hammering the thesis repeatedly), and symmetrical paragraph wrap-ups. AI treats every H2 as an isolated essay, which causes it to over-explain the same core concept multiple times.

(Recommendations: trim remaining didactic restatement; vary paragraph resolutions further. Not applied — MAX_GEMINI_PASSES reached; further passes risk lowering HL again, as pass 1 did. [VERIFY] tags, RG, 18+, disclosures: keep untouched — confirmed.)

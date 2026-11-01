# 07 — Gemini check, pass 3 (after humaniser pass 2) — PASS

Command: `python3 scripts/gemini_check.py .../05b-final-draft.md`
Exit: 0

**Verdict: Highly likely human-written, 90% confidence.** → normalized human-likeness = **90** (≥ 80 target) → **PASS**.

## KEEP-BEST (loop ended on PASS)
| version | verdict | human-likeness |
|---|---|---|
| initial draft | Shows AI patterns 75% | 25 |
| humaniser pass 1 | Shows AI patterns 80% | 20 |
| **humaniser pass 2 (current 05b)** | **Highly likely human-written 90%** | **90 ← KEPT** |

The current 05b IS the highest-scoring version AND a PASS → kept as-is. gemini column = `human 90`.
Remaining pass-3 recs (below) are minor/optional (heading phrasing, numbered-list → prose, RG transition). NOT applied: the loop ended on PASS at HL90; applying more risks lowering the score (pass 1 already demonstrated a humaniser pass can drop HL), and the numbered betting list is a genuine sequential process the light-recheck rule explicitly allows to keep.

---
(verbatim Gemini output)

**Verdict: Highly likely human-written, 90% confidence.**

Exceptionally well-crafted, reads like a native Bulgarian speaker with lived experience of the game. Lacks typical Bulgarian LLM hallmarks (literal translations, generic vocabulary, repetitive structures). Idiomatic phrasing AI rarely generates: „сядат обикновено от двама до осмина", „банката вече е натежала", slang „Чичо Лари"/„йончо". Smooth transitions; avoids „В заключение…".

Minor SEO/structural patterns (optional polish):
1. SEO-style interrogative H2 „Какво значи „свара" и защо играта носи това име" — could shorten. (Optional.)
2. Numbered betting list intro „по следния ред:" — textbook rhythm; could prose-ify. (Optional; genuine sequential process — kept.)
3. RG tonal shift „Свара не е източник на доход…" — suggest a bridging clause; RG facts/warnings kept exactly as-is per hard rules. (Optional.)

# 07 — Gemini check · pass 3 (after humaniser pass 2)

**Verdict (verbatim):** Shows AI patterns, 75% confidence.
→ Normalized HUMAN-LIKENESS = 100 − 75 = **25**. Same as pass 1. MAX_GEMINI_PASSES (2) reached.

## Score trail (keep-best)
| version | verdict | human-likeness |
|---|---|---|
| initial draft (check 1) | Shows AI patterns 85% | 15 |
| humaniser pass 1 (check 2) | Shows AI patterns 75% | 25 |
| humaniser pass 2 (check 3) | Shows AI patterns 75% | **25 ← kept** |

**KEEP-BEST decision:** highest human-likeness seen = 25 (tie between pass 1 and pass 2).
Pass 2 is NOT lower than pass 1 and is qualitatively better — it fixed the "smoking gun"
image-prompt alt-text and broke the symmetric heading pattern — so the final 05b = humaniser
pass 2. No revert. Recorded in content-queue `gemini` column as **ai 75** (ended below 80 after
the cap → flagged for human; the human owns Step 6 / publishing).

The AI detector is pinned around 75% AI on this dense, factual, encyclopaedic BG tournament
content regardless of style edits (the sibling Лига Европа / Ефбет Лига runs logged the same
instability). The gate passes at 95/100 with 0 criticals; facts, numbers, links, RG and
disclosures are all clean.

Gemini's verbatim check-3 feedback (style-only; RG text + footer explicitly "excellent, must
remain as is"):
1. Personification "Роди се късно, чак през сезон 2021/22" → state establishment plainly.
2. Forced metaphor heading "Нагоре по стълбата" → drop metaphor, keep functional part.
3. Cliché filler "Победителят не си тръгва с празни ръце" → delete, start with the benefit.
4. "Journey" signpost "Пътят дотук минава през квалификации" → rephrase to the mechanism.
5. Over-thematic money heading "На пари, отдалеч: ..." → simpler (e.g. „Спортни залози и
   отговорна игра"). NOTE: kept as-is for brand consistency — the sibling Лига Европа used the
   same heading and passed; it is an established brand section title.

These are reasonable future edits but fall beyond the 2-pass cap (unscored), so per keep-best
discipline the scored pass-2 version is kept rather than an unverified pass-3 edit.

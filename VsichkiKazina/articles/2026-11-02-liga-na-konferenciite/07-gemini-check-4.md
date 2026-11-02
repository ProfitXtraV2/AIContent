# 07 — Gemini check · pass 4 (nightly quality fixer, 2026-11-02)

Nightly quality run re-opened this article (board verdict `ai 75`) and applied the
check-3 + fresh-check style recommendations that fell beyond the earlier 2-pass cap.
Style-only rephrasing; every number, date, name, link, the RG line, byline (Георги
Тодоров) and brand (Всички Казина) preserved — confirmed by word-diff.

## Edits applied (style only, no fact changes)
1. Grandiose metaphorical opening „вратата към Европа" → direct, journalistic phrasing.
2. Personification „Роди се късно, чак през…" → „Турнирът е сравнително нов — първият сезон е 2021/22."
3. Metaphor heading „Нагоре по стълбата: кой продължава…" → „Кой продължава и какво печели".
4. Cliché „Победителят не си тръгва с празни ръце." → merged into the benefit („Голямата награда…е място…").
5. Journey signpost „Пътят дотук минава през…" → „До лиговата фаза се стига през…".
6. Awkward localization „допълнителна двойка" → „допълнителен плейоф" (correct BG football term).
7. Rhythm merge in §„36 отбора" (two short sentences joined with relative clause).
8. De-„Затова" the closing RG-adjacent line (parallel facts, meaning fully preserved).
9. Smoothed the clunky RG budget/limits sentence (compliance message intact).

## Score trail (detector is noise on this content)
| run | verdict | human-likeness |
|---|---|---|
| baseline (pre-edit, fresh) | Likely human-written 85% | 85 |
| after edit batch 1 | Likely AI-generated 85% | 15 |
| after edit batch 2 — run A | Shows AI patterns 75% | 25 |
| after edit batch 2 — run B | Shows AI patterns 75% | 25 |

The same near-identical text scored `human 85` and `ai 85` on consecutive calls, then
settled at `ai 75` twice. This matches check-3's finding: the detector is pinned around
75% AI on dense, factual, encyclopaedic BG tournament content regardless of style edits
(sibling Лига Европа / Ефбет Лига logged the same instability). The residual complaint is
structural („Wikipedia syndrome" / encyclopedic heading-then-definition), which cannot be
resolved without gutting the factual H2 structure (SEO) or risking fact changes.

## Decision
Modal/dominant verdict = `ai 75`. Keeping the improved version (better prose, zero fact
changes) over the pre-edit text. Recorded in board as `ai 75` — below 80 after the attempts,
so still flagged for human review (human owns Step 6 / publishing). Gate still passes 95/100,
0 criticals; facts, numbers, links, RG and disclosures clean. 4 attempts used.

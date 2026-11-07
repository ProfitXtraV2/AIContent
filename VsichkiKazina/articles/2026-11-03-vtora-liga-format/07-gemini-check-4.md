# 07 — Gemini check · pass 4 (nightly quality fixer, 2026-11-03)

Nightly quality run re-opened this article (board verdict `ai 65`) and applied the three
style-only recommendations from check-3 that fell beyond the earlier 2-pass cap and did NOT
require deleting load-bearing facts. Style-only rephrasing; every number, date, name, link,
the RG line, byline (Георги Тодоров) and brand (Всички Казина) preserved — confirmed by
fact-anchor diff (1950, 2016, 2025/26, Берое, девет, Дунав, 3 точки, БФС, ПФЛ, НАП all intact).

## Edits applied (style only, no fact changes)
1. Removed meta-reassurance sentence „Това разделение между носител и администратор е обичайно
   за професионалния футбол и не променя с нищо как изглежда сезонът за зрителя." (check-3 rec 3 —
   reader-reassurance filler; the ownership fact БФС/ПФЛ stays).
2. Trimmed redundant padding: „…се изкачва директно в Първа лига и така излиза на най-високото
   клубно ниво в страната." → „…се изкачва директно в Първа лига." (check-3 rec 4; Първа лига is
   already established as the top tier, so the tail is restatement).
3. Merged the staccato history run (check-3 rec 5): the 2016-name / Берое-record / Дунав-champion
   sentences joined into one flowing sentence; all three facts preserved exactly.

Check-3 recs 1 and 2 (delete the 3/1/0 points values; delete the whole „няма пряк път към Европа"
section) were NOT applied — both are load-bearing facts the pipeline must preserve.

## Score trail (detector is noise on this content)
Fair same-session head-to-head, pre-edit (pass-1, committed) vs post-edit (tonight):
| version | fresh reads | modal |
|---|---|---|
| pre-edit (pass-1, recorded `ai 65`) | ai 75, ai 80, ai 75, human 90 | ai ~75-80 |
| post-edit (this pass) | ai 75, ai 75, ai 80, ai 75, ai 75 | ai 75 |

The recorded `ai 65` was a single lucky-low sample: fresh reads of the identical pass-1 text
tonight ranged ai 75-80 (and once human 90). Pre- and post-edit are statistically
indistinguishable — Gemini anchors ~75% "AI patterns" on dense, factual, evergreen Bulgarian
football-format prose regardless of style (same as siblings vk-0314 efbet, vk-0319 Лига Европа,
vk-0322 Лига на конференциите). The residual complaint is structural („over-explanation" /
„Wikipedia-lite") and the remaining recs demand deleting required facts, so human-likeness
cannot be pushed to 80 without dropping information.

## Decision
Kept the humanised (post-edit) version: identical score distribution to pass-1 but cleaner prose
(three genuine AI tells removed, zero fact changes). Recorded in board as `ai 75` (tonight's
modal fresh read; honest value — the prior `ai 65` was a stale lucky sample). Below 80 after the
attempts → still flagged for human review (human owns Step 6 / publishing). Facts, numbers, links,
RG, 18+, disclosures, byline and brand clean.

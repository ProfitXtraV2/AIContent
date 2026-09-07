# Content Queue — VsichkiKazina (article lifecycle board)

A topic enters this table only once selected to write. Un-started ideas live in
`topic-backlog.md` / `research-topics.md`.

`status` ∈ in-progress | drafted | approved | posted | failed
Buffer = count of rows with status `drafted` or `approved` (target ≥ 10).
`volume`/`kd` are the target keyword's Ahrefs metrics (copied at selection); the dashboard
computes Opportunity from them. `gemini` = Step-7 verdict (`human <hl>` / `ai <Y>`).

| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vk-0001 | drafted | guide | Как работи изискването за разиграване (wagering) | разиграване, wagering, бонус условия | 20 |  | backlog | 2026-09-07 |  | 2026-09-07-kak-raboti-razigravaneto | #1 | human 85 | gate 89/100; HUMAN-LIKE; 0 flags; Gemini Step-7 backfill: Humaniser ×2 → Likely human-written 85% |
| vk-0002 | failed | comparison | Най-добри казино бонуси за добре дошли 2026 | бонус за добре дошли, welcome bonus | 20 |  | backlog |  |  | 2026-09-07-najdobri-bonusi-za-dobre-doshli-2026 | #3 |  | primary sources unreachable: operator T&C 403 geo-block, НАП register conn reset; full egress on but sites block foreign traffic; can't build like-for-like превъртане bases + licence №s without fabricating |
| vk-0003 | drafted | guide | Безплатни казино игри: демо режим, RTP и капаните на „безплатното" | безплатни казино игри, демо режим, RTP, безплатни завъртания | 11000 | 45 | research | 2026-09-07 |  | 2026-09-07-bezplatni-kazino-igri | #4 | ai 60 | gate 90/100; HUMAN-LIKE 51/60; 0 flags; folds „с ротативки"; anti-cannibal note vs /kazino-igri/ /slot-igri/; Gemini Step-7 backfill: Humaniser ×2 → best 60% AI (below-80 target) |
| vk-0004 | drafted | guide | Бонус без депозит 2026: какво наистина получавате | бонус без депозит, казино без депозит, безплатни завъртания без депозит | 5400 | 61 | research | 2026-09-07 |  | 2026-09-07-bonus-bez-depozit-2026 | #5 | human 85 | gate 90/100; HUMAN-LIKE 50/60; 0 flags; no-deposit pillar; folds 3 near-dups; anti-cannibal note vs listing /bonusi/bez-depozit/; Gemini Step-7 backfill: Humaniser ×1 → Likely human-written 85% |
| vk-0005 | drafted | guide | Ново онлайн казино: как да оцените новооткрит оператор | ново онлайн казино, оценка на оператор, лиценз от НАП | 2200 | 57 | research | 2026-09-07 |  | 2026-09-07-novo-onlajn-kazino | #6 | human 85 | gate 91/100; HUMAN-LIKE 51/60; 0 flags; evaluation framework (not a list); anti-cannibal note vs /novi-kazina/ + 2 blog guides; Gemini Step-7 backfill: Humaniser ×2 → Likely human-written 85% |

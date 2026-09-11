# Content Queue — Dentalvia (article lifecycle board)

A topic enters this table only once selected to write. Un-started ideas live in
`topic-backlog.md` / `research-topics.md`.

`status` ∈ in-progress | drafted | approved | posted | failed
Buffer = count of rows with status `drafted` or `approved` (target ≥ 10).
`volume`/`kd` are the target keyword's Ahrefs metrics (copied at selection); the dashboard
computes Opportunity from them. `byline` alternates Georgi Todorov ↔ Mario Yordanov; next
article takes whichever name the most recent row did NOT use; first article → Georgi Todorov.
`gemini` = Step-7 verdict (`human <hl>` / `ai <Y>`).

| id | status | type | byline | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| dv-0001 | drafted | comparison | Georgi Todorov | Veneers-Kosten 2026: Deutschland und Ausland im Vergleich | veneers kosten, veneers kosten deutschland, veneers ausland | 7500 | 30 | backlog | 2026-09-10 |  | 2026-09-10-veneers-kosten-deutschland-ausland | #49 | ai 85 | anti-cannibal vs /veneers/ + /kosten/; dated example prices; gate 93/100 PASS-WITH-FIXES; 28 [VERIFY] +1 [CONFLICT] +1 [DATA NEEDED]; img:3 (hero+2 SVG, best 90); board reconciled post-run (run died before final board commit) |
| dv-0002 | drafted | guide | Mario Yordanov | Festzuschuss und Bonusheft: was die Krankenkasse 2026 beim Zahnersatz zahlt | festzuschuss zahnersatz 2026, bonusheft zahnarzt, festzuschuss tabelle | 3000 | 28 | research | 2026-09-10 |  | 2026-09-10-festzuschuss-bonusheft-zahnersatz-2026 | #50 | ai 75 | GKV basics; links live /ratgeber/zahnersatz-ausland-zuschuss-krankenkasse/; all GKV figures [VERIFY]; gate 96/100 PASS-WITH-FIXES; 30 [VERIFY] (GKV figures); img:2 (SVG 95, hero 72 kept — VK-prompt ALT false positive); board reconciled post-run (run died before final board commit) |
| dv-0003 | drafted | howto | Georgi Todorov | Zahnarztkosten von der Steuer absetzen — auch bei Behandlung im Ausland | zahnarztkosten steuer absetzen, zahnbehandlung steuer | 2500 | 20 | backlog | 2026-09-10 |  | 2026-09-10-zahnarztkosten-steuer-absetzen | #53 | ai 75 | § 33 EStG außergewöhnliche Belastung; all tax figures [VERIFY]; gate 92/100 PASS; 12 [VERIFY] (tax figures); img:2 (72/75 kept — VK-prompt ALT false positive; fix review-prompt binding); board reconciled post-run (run died before final board commit) |

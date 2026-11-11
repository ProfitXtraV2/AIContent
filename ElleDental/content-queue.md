# Content Queue — ELLE Dental (page lifecycle board)

⏸ **PAUSED by owner on 2026-11-11** — no rows are added until the owner un-pauses the brand in
writing (see `ElleDental/automation/daily-run.md`).

A page enters this table only once selected to write. Ideas live in `topic-backlog.md` /
`research-topics.md`.

`status` ∈ in-progress | drafted | approved | posted | failed
`type` ∈ page-rewrite | new-page · `query` = the page address (one of the 28, or an
owner-approved new address) · `folder` = `<YYYY-MM-DD>-<slug>` · `gemini` = Step-7 professional
score (`human <score>` = passed ≥ 80, `ai <100−score>` = below).
`drafted` = AI draft in a PR awaiting the human and the doctor; `approved` = PR merged (draft
accepted for doctor review, NOT medically reviewed); `posted` = copied into WebPortals and
live after Д-р Манолова's review. Buffer = drafted + approved (target 3).

| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

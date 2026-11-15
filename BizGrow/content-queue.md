# Content Queue — BizGrow (page lifecycle board)

⏸ **PAUSED at onboarding on 2026-11-15** — no rows are added until the owner un-pauses the brand
in writing (see `BizGrow/automation/daily-run.md`).

A page enters this table only once selected to write. Ideas live in `topic-backlog.md` /
`research-topics.md`.

`status` ∈ in-progress | drafted | approved | posted | failed
`type` ∈ page-rewrite | new-page · `query` = the page address (`/`, `/en/`, or a `planned`
address from `keyword-map.md`) · `folder` = `<YYYY-MM-DD>-<slug>` · `gemini` = Step-7
professional score (`human <score>` = passed ≥ 80, `ai <100−score>` = below, `skipped` = no
Gemini key in this environment).
`drafted` = AI draft in a PR awaiting the human; `approved` = PR merged (draft accepted for
porting, NOT approved by the owner); `posted` = ported into the site and live after the owner's
approval. Buffer = drafted + approved (target 3).

| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

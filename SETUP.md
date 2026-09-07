# One-time setup (human-owned)

These steps need your GitHub/org access and the Claude Code cloud routine UI.

## 1. Install GitHub CLI (if missing)
    brew install gh
    gh auth login          # choose GitHub.com, HTTPS, authenticate

## 2. Create the public repo under the org and push
From the repo root (`AIContent/`):
    gh repo create ProfitXtraV2/AIContent --public --source=. --remote=origin --push
(Public is required because GitHub Pages on a free org needs a public repo.)

## 3. Enable GitHub Pages
    gh api -X POST repos/ProfitXtraV2/AIContent/pages -f source.branch=main -f source.path=/docs
Then open: https://profitxtrav2.github.io/AIContent/  (dashboard). `robots.txt`
+ noindex meta discourage indexing of drafts.

## 4. Provision a push credential for the cloud routine
Create a fine-grained token scoped to ONLY `ProfitXtraV2/AIContent`, permissions
Contents: Read/Write and Pull requests: Read/Write. Store it as the routine's
secret (used for `git push` + `gh pr create`). This is the one thing that silently
breaks daily pushes if missed.

## 5. Create the scheduled cloud routine
Use the Claude Code `schedule` skill (or `/schedule`) to create a routine:
  - Schedule: 07:00 Europe/Sofia, daily.
  - Working repo: ProfitXtraV2/AIContent.
  - Instruction: run `VsichkiKazina/automation/daily-run.md`.
  - Ensure the routine env has `gh` + Python 3 and the token from step 4.

## 6. First backfill
The first few runs ramp the buffer from 0 → 10 (MAX_PER_RUN caps each run).
Review the PRs, approve, post, and mark `approved → posted` to free slots.

## Dev note
`scripts/tests/` uses `pytest` (dev-only: `python3 -m pip install pytest`).
The cloud routine does NOT need pytest — it only runs `scripts/build_dashboard.py`.

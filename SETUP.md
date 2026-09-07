# One-time setup

Everything the daily automation needs. Do this once; after that, runs are
laptop-independent. See `README.md` for the full architecture.

## 1. GitHub CLI + repo (local machine)
```bash
brew install gh && gh auth login          # GitHub.com, HTTPS
# from the repo root:
gh repo create ProfitXtraV2/AIContent --public --source=. --remote=origin --push
```
Public is required because GitHub Pages on a free org needs a public repo.

## 2. GitHub Pages (dashboard)
```bash
echo '{"source":{"branch":"main","path":"/docs"}}' | \
  gh api -X POST repos/ProfitXtraV2/AIContent/pages --input -
```
Dashboard → https://profitxtrav2.github.io/AIContent/  (drafts carry `noindex`).

## 3. Give the cloud agent GitHub access
Run **`/web-setup`** in Claude Code, or install the **Claude GitHub App**
(https://claude.ai/code/onboarding?magic=github-app-setup) and grant
`ProfitXtraV2/AIContent`. Without this the cloud routine cannot clone or open PRs.

## 4. Cloud environment settings (claude.ai/code → routine → environment ⚙)
- **Network access: Full** — the run needs egress for WebFetch and the Ahrefs API.
- **Environment variable `AHREFS_API_KEY`** (mark as secret) — your Ahrefs API token.
  Never commit it to the repo.

## 5. Scheduled routine
Create a routine (via `/schedule` or the routines API):
- Schedule: **`0 4 * * *`** (07:00 Europe/Sofia).
- Repo: `ProfitXtraV2/AIContent`. Model: Opus (recommended for editorial quality).
- Instruction: run `VsichkiKazina/automation/daily-run.md`.
- Env must have `gh` + Python 3 (standard in the CCR image).

## 6. First backfill
The first runs ramp the buffer from 0 → 10 (capped by `MAX_PER_RUN`). Review the PRs,
approve, post, and mark rows `posted` to free slots.

## Notes
- **Content scope is guides-only** until a BG-reachable source route (proxy/scraping API or
  human source packs) is added — operator content geo-blocks the cloud IP. Flip the switch
  in `automation/daily-run.md` once sourcing is solved.
- Dev only: `scripts/tests/` uses `pytest` (`python3 -m pip install pytest`); the cloud run
  does not need it.

# Rebuild the dashboard

The dashboard is data-driven: a static `docs/index.html` renders `docs/data/status.json`.
Only the JSON is regenerated each run.

## How
From the repo root, run:

    python3 scripts/build_dashboard.py

This parses `VsichkiKazina/content-queue.md` and writes `docs/data/status.json`
(buffer count/target/deficit, per-status counts, and all rows). Commit the
updated `docs/data/status.json` as part of the run's PR.

Do NOT hand-edit `status.json` or `index.html` during a run — change the queue,
then regenerate. If `build_dashboard.py` errors, log it in the run and open the
PR with `[DASHBOARD ERROR]` so a human can look.

# Rebuild the DentalVia Dashboard

The dashboard is data-driven: a static `docs/dentalvia/index.html` renders
`docs/data/dentalvia/status.json`. Only the JSON is regenerated each run.

## How
From the repo root, run:

    python3 scripts/build_dashboard.py dentalvia

This parses `DentalVia/content-queue.md` and writes `docs/data/dentalvia/status.json`
(buffer count/target/deficit, per-status counts, and all rows). Commit the updated
`docs/data/dentalvia/status.json` as part of the run's board commit to `main`.

> Note: the `dentalvia` CLI argument is implemented in Task 7. Until then, run without
> the argument and read from `docs/data/status.json` as a fallback.

Do NOT hand-edit `status.json` or `index.html` during a run — change the queue,
then regenerate. If `build_dashboard.py` errors, log it in the run and open the
PR with `[DASHBOARD ERROR]` so a human can look.

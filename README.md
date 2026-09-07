# AIContent — ProfitXtra AI content workspace

Automated content production. Brand folders hold their own pipeline, topic
inputs, queue, and daily articles. Currently: **VsichkiKazina** (vsichkikazina.bg).

## Daily flow (per brand)
1. A scheduled cloud agent runs `VsichkiKazina/automation/daily-run.md` at 07:00
   Europe/Sofia (laptop-independent).
2. It keeps **≥10 written-but-unposted** articles ready: `deficit = 10 - (drafted+approved)`,
   writes `deficit` new articles (post N ⇒ write N).
3. Each article: runs the pipeline (brand=vsichkikazina) into
   `VsichkiKazina/articles/YYYY-MM-DD-<slug>/`, assembles a verification report,
   and opens **one PR** into `main`. Nothing lands on `main` without a human merge.
4. Dashboard (GitHub Pages, `/docs`) shows the buffer gauge + queue board.

## Human loop
- Review each PR: resolve flags, `drafted → approved`, merge, **post to the site
  manually**, then mark `approved → posted` (frees a buffer slot).
- Steer topics via `VsichkiKazina/topic-backlog.md` (drained first).

See `SETUP.md` for one-time setup and the design spec for full detail.

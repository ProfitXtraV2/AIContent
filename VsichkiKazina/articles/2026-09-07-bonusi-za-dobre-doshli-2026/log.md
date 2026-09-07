# log — 2026-09-07-bonusi-za-dobre-doshli-2026

- 2026-09-07 · Stage 0 (brief): assembled 00-brief.md. Type=comparison, byline=editorial,
  query "Най-добри казино бонуси за добре дошли 2026".
- 2026-09-07 · Dedup: content-queue.md empty (no prior row). Live sitemap
  https://vsichkikazina.bg/sitemap.xml UNREACHABLE (EGRESS_BLOCKED by network policy);
  WebSearch surfaced no existing vsichkikazina.bg page on this exact query. Not a duplicate.
- 2026-09-07 · Stage 0 BLOCKED → article FAILED before drafting. A welcome-bonus
  comparison is a like-for-like, numbers-first type that requires verified per-operator
  terms (bonus %/max €/FS, превъртане multiplier + base, срок, принос, min deposit,
  макс. изтегляема сума) AND a valid НАП licence № per operator, checked in the public
  register (licence-first doctrine). Every source able to supply/verify those facts is
  egress-blocked this run: vsichkikazina.bg, operator T&C pages, the НАП register, and
  competitor BG comparison sites all return EGRESS_BLOCKED; WebSearch returns only vague
  aggregate ranges with no per-operator verified figures and no licence confirmation.
- Decision: per daily-run hard rules — NEVER fabricate operator facts to hit a number;
  write fewer instead; on a blocker set the row to `failed`, log why, open a `[FAILED]` PR.
  Pipeline stages 1→5b were NOT run (no honest source material to synthesise).
- external check: skipped (Step 7 is manual-only; N/A — article not drafted).
- Unblock: human supplies a verified operator dataset/brief, or re-runs in an environment
  whose egress policy permits the casino/regulator domains. See 00-brief.md "HOW A HUMAN
  CAN UNBLOCK IT".

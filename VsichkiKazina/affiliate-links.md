# Affiliate Link Registry — VsichkiKazina

Single source of truth for outbound **affiliate links** used in articles. These are the
SAME links vsichkikazina.bg already uses — reuse the site's own affiliate / redirect URLs
(e.g. an on-site `/go/<brand>` or partner URL) so click tracking and revenue stay intact.

Populated by extracting from the live site (`vsichkikazina.bg`) and human-verified. These
links are already public on the site, so keeping them in this (public) repo is fine.

## Rules (enforced in `automation/daily-run.md` + the Brand Gate)
- When a **review / comparison / bonus / deposit** article references or recommends a
  specific operator, link that operator's first prominent mention to its `affiliate_url`
  from the table below.
- **Never invent an affiliate URL.** If the operator is not in this table, insert a
  `[LINK NEEDED: <operator>]` flag for the human — do NOT link to a bare operator domain
  or guess a partner URL.
- Always keep the affiliate-disclosure footer (the Brand Gate already requires it).
- Guides / news that don't recommend a specific operator need no affiliate link (they use
  the approved internal-link set instead).
- `status`: `active` = safe to use · `paused` = do not link (deal off) · `check` = re-verify.

| operator | affiliate_url | landing | status | source_page | last_checked |
|---|---|---|---|---|---|
| Betano | https://vsichkikazina.bg/go/betano/ | welcome bonus | active | /casino/betano/ | 2026-09-13 |
<!-- Populated by the affiliate-link extraction run from vsichkikazina.bg, then human-verified.
     Example row shape:
     | Spin City | https://vsichkikazina.bg/go/spin-city | welcome bonus | active | /kazino/spin-city/ | 2026-09-07 | -->

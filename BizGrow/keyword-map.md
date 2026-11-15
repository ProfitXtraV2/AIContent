# Keyword Map — BizGrow (one main term per address)

Single source of truth for **which search term each address targets**. Filled by the owner's
session; empty at onboarding (2026-11-15). The pipeline reads it at Step 0 (brief), Step 4 (SEO)
and Step 5 (Brand Gate, one-term-per-page check). A page whose address has no row here is not
written.

Rules:
- One `primary_keyword` per address; no two addresses share a primary keyword.
- `secondary_keywords` are supporting terms for that page only; a term that is another address's
  primary keyword may not appear here.
- `status` ∈ live | planned | parked. A `new-page` is eligible for the pipeline only at `planned`
  (approved by the owner or the owner's session; record who/when in `notes`).
- Bulgarian and English pages are separate rows (`locale`), paired by `pair`.
- `volume`/`kd` from Ahrefs with the date; blank if not measured (never estimated).

| address | locale | pair | slug | primary_keyword | secondary_keywords | h1 | volume | kd | checked | status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

# Ahrefs API v3 — Working Endpoints for VsichkiKazina keyword research

Recorded 2026-09-07 against a live key. All calls verified `HTTP 200`.

- **Base URL:** `https://api.ahrefs.com/v3`
- **Auth header:** `Authorization: Bearer $AHREFS_API_KEY`
- **Accept:** `application/json`
- **Market:** always pass `country=bg` (lower-case ISO-2).
- **Subscription seen:** `Lite 2022, billed yearly`. Check units before a run with the
  usage endpoint below — discovery (`matching-terms`) is the expensive call.

## 1. Units / subscription check
`GET /subscription-info/limits-and-usage`

No params. Returns `limits_and_usage.units_limit_workspace`,
`units_usage_workspace`, `usage_reset_date`, `api_key_expiration_date`.
Call this first; skip discovery if remaining units are low.

## 2. Metrics for known keywords (volume, KD, intent) — CHEAP, primary workhorse
`GET /keywords-explorer/overview`

| param | value |
|---|---|
| `country` | `bg` |
| `keywords` | comma-separated list (batch many in one call) |
| `select` | `keyword,volume,difficulty,cpc,intents` |

`intents` is an object of booleans: `informational, navigational, commercial,
transactional, branded, local`. `difficulty` is Ahrefs KD (0–100). `volume` is
monthly search volume for the country. `cpc` is in cents. Missing metric → `null`.

## 3. Trend signal
`GET /keywords-explorer/volume-history`

| param | value |
|---|---|
| `country` | `bg` |
| `keyword` | a single keyword (one per call) |

Returns `metrics[]` of `{date, volume}` monthly points (~3 years back).
Compute trend by comparing the mean of the last 3 months to the mean of months
9–12 ago: `>+10%` = up, `<−10%` = down, else flat.

## 4. Keyword discovery (find new opportunities) — EXPENSIVE (units per returned row)
`GET /keywords-explorer/matching-terms`

| param | value |
|---|---|
| `country` | `bg` |
| `keywords` | one or more seed terms |
| `select` | `keyword,volume,difficulty,cpc` |
| `match_mode` | `terms` (all seed words appear) or `phrase` |
| `order_by` | `volume:desc` |
| `limit` | keep small (10–15) to conserve units |

Sibling discovery endpoints (same shape): `related-terms`, `search-suggestions`.

## Notes / gotchas
- Use `--data-urlencode` (curl) or a params dict — Cyrillic seeds must be URL-encoded.
- `overview` is the cheap per-keyword metric call; prefer it for enrichment.
- `matching-terms` bills per returned row — batch seeds, small `limit`.
- Not all endpoints on the docs are available on the Lite plan; the four above are.
- Helper script that drives #2 + #3 for a keyword list: `scripts/ahrefs_enrich.py`.

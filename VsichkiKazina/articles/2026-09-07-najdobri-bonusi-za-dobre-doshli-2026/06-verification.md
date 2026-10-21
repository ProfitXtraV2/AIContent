# 06 — Verification / Failure evidence
Article: Най-добри казино бонуси за добре дошли 2026 (comparison)
Run date: 2026-09-07 · Outcome: FAILED (primary sources unreachable)
External check (Gemini): skipped.

## Why this failed
A brand-compliant welcome-bonus **comparison** cannot ship without verified, timestamped
operator terms (превъртане multiplier + base) and НАП licence numbers, sourced from the
operator T&C pages and the НАП register. In this run every such primary source is
unreachable from the execution environment. Only secondary comparison sites are reachable,
and they conflict and omit the wagering base and licence numbers. No operator term,
licence number, bonus figure, or wagering base was invented.

## Primary-source reachability evidence (07.09.2026, ~15:4x UTC)
Method: WebFetch, then curl with a real browser User-Agent and Accept-Language: bg through
the session egress proxy. Egress is enabled (requests reach the hosts); the hosts reject them.

| Source (primary) | URL | Result |
|---|---|---|
| НАП — gambling registers portal | nra.bg/wps/portal/nra/registers-i-spisuci/registers/page.registers-po-zakona-za-hazarta | HTTP 503 (WebFetch); curl (35) Connection reset by peer |
| НАП — register of gambling organizers (direct) | nra.bg/.../registri_po_zakona_za_hazatra/0f4a4514-2da3-4b25-9e09-a1feda27333d | HTTP 503 |
| НАП — root | nra.bg/ | curl (35) Connection reset by peer |
| efbet (official) | www.efbet.com/bg | HTTP 403 "Access Restricted" |
| Winbet (official) | www.winbet.bg/ | HTTP 403 (Cloudflare) |
| Sesame (official) | sesame.bg/ | HTTP 403 (Cloudflare) |
| Palms Bet (official) | www.palmsbet.com/bg/promotions/ | HTTP 403 "Access Restricted" |

Proxy self-diagnosis corroborated the НАП block destination-side:
`ws_closed_mid_exchange — tunnel closed (code 1006) after 12s; 517 B sent, 39 B received`
for host `nra.bg:443`. The request left the environment and reached nra.bg; nra.bg dropped it.

## What this tells the human (the real finding)
The previous attempt (PR #2) failed on BLOCKED egress. This attempt has FULL egress and
still fails, because the blocker moved: it is now DESTINATION-SIDE geo/bot-blocking by the
Bulgarian operator sites and regulator, not the proxy. Enabling full egress alone will not
fix future comparison/review/news runs that need these sources. Options for a real retry:
1. A Bulgaria-resident egress route / residential proxy the operators don't block.
2. An official operator or НАП data feed/API, if one exists.
3. Human-in-the-loop: paste the operator T&C excerpts + НАП licence numbers into 00-brief.md,
   then re-run — the pipeline can then verify and build the like-for-like table.

## Flags
- [DATA NEEDED] operator terms — all operators (primary source unreachable)
- [DATA NEEDED] НАП licence numbers — all operators (register unreachable)
- [CONFLICT] efbet wagering 25x/35x and срок 24h/14/30d across secondary sources
- [CONFLICT] Sesame max bonus €1000/€2000/1200 лв/2000 лв across secondary sources
Flags stay unresolved — the human owns resolution at Step 6.

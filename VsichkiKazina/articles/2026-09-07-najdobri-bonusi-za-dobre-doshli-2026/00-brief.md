# 00-BRIEF — Всички Казина — "Най-добри казино бонуси за добре дошли 2026"

BRAND: vsichkikazina
MARKET: bg
CONTENT TYPE: comparison
BYLINE: Георги Тодоров (comparison → editorial voice, signed Георги Тодоров per brand rule)
TARGET QUERY: Най-добри казино бонуси за добре дошли 2026
SECONDARY TERMS: бонус за добре дошли, welcome bonus, превъртане, начален бонус
LENGTH (planned): comparison 600–1,400 words
RUN: 2026-09-07 · MAX_PER_RUN=1 (validation-retry override)

## OUTCOME: FAILED — primary sources unreachable, comparison cannot be built without fabrication

A like-for-like welcome-bonus comparison for this brand REQUIRES, per the Brand Gate
(comparisons pillar) and the daily-run source rule:
- each operator's **превъртане multiplier stated with its base** (депозит+бонус vs само бонус),
- **timestamped terms** verified on the operator's own T&C page,
- each operator's **НАП licence №** (licence-first doctrine).

Those facts exist only in two primary sources: the **operators' own Terms & Conditions
pages** and the **НАП public register**. In this run BOTH are systematically unreachable
from the execution environment (see 06-verification.md for the raw HTTP evidence). The
only reachable material is secondary comparison/affiliate sites, whose figures **conflict
with each other, never state the wagering base, and never carry НАП licence numbers**.
Building a "like-for-like превъртане base" table from them would require inventing or
guessing the bases and the licence numbers. That is forbidden. Article marked `failed`.

Note: full outbound web egress IS enabled this run (the prior blocker). The remaining
blocker is DESTINATION-SIDE: the Bulgarian operator sites geo/bot-block foreign automated
traffic (HTTP 403 "Access Restricted") and nra.bg resets the connection. Enabling egress
did not resolve it because the wall is at the source hosts, not the proxy.

## OPERATOR FACTS (from operator T&Cs and НАП register ONLY)
All [DATA NEEDED] — no primary source was reachable, nothing verified, nothing invented.
- Casino: [DATA NEEDED — needs НАП register + operator T&C]
- НАП licence №: [DATA NEEDED — регистър на НАП unreachable this run]
- Welcome bonus (%, max €, FS): [DATA NEEDED — operator T&C unreachable]
- Превъртане (multiplier + base депозит+бонус/само бонус): [DATA NEEDED — base never stated in reachable secondary sources]
- Срок за разиграване (дни): [DATA NEEDED]
- Принос на игрите: [DATA NEEDED]
- Min deposit · Withdrawal min/max: [DATA NEEDED]
- Terms verified on: [DATA NEEDED — no operator T&C page reachable on 07.09.2026]

## WITHDRAWAL PROTOCOL RECEIPTS
N/A — comparison type, no persona testing block.

## SOURCES ATTEMPTED
Primary (REQUIRED, all unreachable — evidence in 06-verification.md):
- НАП register of gambling organizers — https://nra.bg/wps/portal/nra/registers-i-spisuci/registers/page.registers-po-zakona-za-hazarta (503 / connection reset)
- НАП register (direct entry) — .../registri_po_zakona_za_hazatra/0f4a4514-2da3-4b25-9e09-a1feda27333d (503)
- efbet — https://www.efbet.com/bg (403 Access Restricted)
- Winbet — https://www.winbet.bg/ (403)
- Sesame — https://sesame.bg/ (403)
- Palms Bet — https://www.palmsbet.com/bg/promotions/ (403 Access Restricted)

Secondary (reachable, SERP research only — NOT usable for verified operator terms):
- casinobg.bg/казино-бонуси/ (bonus amounts, almost no wagering bases)
- soudnzsofia.bg/licensed/ (mixes in non-BG-licensed brands; no licence numbers)
- competitor SERP snippets for efbet / Winbet / Palms Bet / Sesame bonus terms

## INTERNAL LINKS (planned, if it had been written)
/bonus-category/welcome-bonus/ · /kak-ocenyavame/ · /zakonno-li-e/ · /otgovorna-igra/

## NOTES
This is the second consecutive failure on this topic. PR #2 failed on blocked egress;
this run fails on destination-side geo/bot-blocking despite full egress. A future retry
needs a primary source that is actually reachable, e.g. a Bulgaria-resident egress route,
an operator/regulator API, or the human pasting the operator T&C text and НАП licence
numbers directly into this brief. See research-topics.md for guide-type topics that do
NOT depend on the blocked primary sources and can be written under the current constraint.

---

## APPENDIX — UNVERIFIED secondary-source observations (NOT FOR PUBLICATION)
Recorded only as leads for a manual retry. Every line is UNVERIFIED, from affiliate/
comparison sites, and MUST be confirmed against the operator's own T&C + the НАП register
before any use. Conflicts are noted — they are exactly why this cannot be published.
- efbet casino welcome: wagering reported as 35x on депозит+бонус by one source, 25x on
  slots by another → [CONFLICT]; slots-only contribution; срок reported as 24h vs 14/30 days
  → [CONFLICT]. [VERIFY on efbet T&C]
- Winbet casino/live: reported 30x (base reported as депозит+бонус), срок ~14 days, bonus
  valid 30 days. [VERIFY on Winbet T&C]
- Palms Bet casino: reported 100% up to €1000 + up to 300 FS, min deposit €5, 30x, 30-day
  validity; base for the CASINO bonus not clearly stated (the 6x figure was the SPORT bonus
  on депозит+бонус). [VERIFY on Palms Bet T&C]
- Sesame casino: reported 100% up to €1000 (other sources say €2000 / 1200 лв / 2000 лв →
  [CONFLICT]); FS winnings 30x on EGT slots within 2 days; min first deposit ~20 BGN.
  [VERIFY on Sesame T&C]
- No reachable secondary source published a single НАП licence № for any operator.

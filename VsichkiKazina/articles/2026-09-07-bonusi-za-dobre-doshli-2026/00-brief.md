# 00-BRIEF — Всички Казина · article 2026-09-07-bonusi-za-dobre-doshli-2026

BRAND: vsichkikazina
MARKET: bg
CONTENT TYPE: comparison
BYLINE: editorial (Екипът на Всички Казина)
TARGET QUERY: Най-добри казино бонуси за добре дошли 2026
SECONDARY TERMS: бонус за добре дошли, welcome bonus, начален бонус, превъртане (с база), безплатни завъртания
LENGTH: 600–1,400 (comparison)

## OPERATOR FACTS (required for THIS type — comparison)
A welcome-bonus comparison is, by the brand bible, a numbers-first, side-by-side,
like-for-like piece. It CANNOT be written without, per compared operator:
- exact welcome bonus (%, max €, FS),
- превъртане multiplier AND its base (депозит+бонус vs само бонус) — like-for-like,
- срок за разиграване, принос на игрите, min deposit, макс. изтегляема сума,
- a VALID, current НАП licence № checked in the public register at review time
  (licence-first doctrine: no licence → no score, no link, no recommendation).
None of this is available this run — see the blocker below.

## WITHDRAWAL PROTOCOL RECEIPTS
EMPTY.

## SOURCES
BLOCKED. Every source that could supply or verify the required operator facts is
unreachable from this run's environment:
- vsichkikazina.bg (own site / sitemap): EGRESS_BLOCKED by network policy.
- Operator T&C pages and the НАП public register: casino/regulator domains are
  egress-blocked; full-text fetch returns EGRESS_BLOCKED.
- Competitor BG comparison sites (casinobg.bg, casinoslots.bg, etc.): EGRESS_BLOCKED.
- WebSearch works but returns only vague aggregate snippets ("обикновено 100% или
  200%", "без депозит 30–50x") with NO per-operator, verified, timestamped terms
  and NO way to confirm any operator's current НАП licence.

## INTERNAL LINKS (intended, from approved set)
/bonus-category/welcome-bonus/, /kak-ocenyavame/, /otgovorna-igra/, /zakonno-li-e/

## NOTES / DECISION
STATUS: failed (blocked). Reason: writing a specific-operator 2026 welcome-bonus
comparison from this environment would require inventing operator bonus terms and
асserting НАП licences that cannot be verified against any primary source — the
#1 forbidden action (fabricating operator facts) and a licence-first violation.
Per the daily-run hard rules ("NEVER fabricate a topic to hit a number — write
fewer instead"; "If anything blocks an article, set its row to failed, log why,
and open a [FAILED] PR"), this article is stopped at Stage 0 (brief) and NOT drafted.

HOW A HUMAN CAN UNBLOCK IT:
1. Provide a filled brief with verified per-operator terms (a NeuronWriter/T&C
   export or a manually gathered table), each figure timestamped and each НАП
   licence № confirmed in the public register; OR
2. Re-run this topic in an environment whose egress policy permits vsichkikazina.bg,
   the НАП register, and operator T&C domains, so Synthesis can fetch and verify.
The wagering-guide sibling article this run (2026-09-07-kak-raboti-razigravaneto)
was writable because it is evergreen/conceptual and needs no operator facts.

# DentalVia Verification Policy (brand-specific — does NOT apply to VsichkiKazina)

Approved by the site owner 2026-09-11. This file changes HOW MANY flags are born
and WHO resolves them for the Dentalvia brand only. The base principle stays:
nothing publishes with an open flag, and merge (= approve) stays human.

Load this file at Stage 1 (Synthesis), Stage 2 (Author) and Step 6
(verification) — it overrides the generic "flag every unverifiable fact" rule.

## Flag tiers

**Tier A — no flag needed (example-framed figures).**
A price or cost figure explicitly framed as a dated example — „ab X €",
„Beispielpreis(e)", „Stand MM/JJJJ", „Richtwert" — carries its guard in the
framing itself (the Brand Gate already REQUIRES that framing; see
brand-gate-dentalvia.md check 5). Do NOT flag it. The framing must be intact;
an unframed price is not Tier A.
Examples: „Ein Einzelimplantat mit Krone kostet in Sofia ab 900 € (Stand
09/2026, Beispielpreis)." → no flag. „Veneers kosten in Deutschland 800–2.000 €
pro Zahn" (no framing) → NOT Tier A; frame it or flag it.

**Tier B — AI-verifiable against a primary source (verify-assist resolves).**
Factual claims with an official primary source that can be fetched and quoted:
- German law texts → gesetze-im-internet.de (e.g. § 33 EStG)
- GKV Festzuschuss / Bonusheft rules and amounts → KZBV, GKV-Spitzenverband,
  Bundesanzeiger publications
- Medical-society positions and statistics → DGI, DGZMK publications
- Manufacturer specifications → the manufacturer's own site
- EU patient-rights / warranty rules → official EU or BMG pages
During verify-assist (see below): fetch the source, quote the exact passage
next to the claim in 06-verification.md, and if the source CONFIRMS the claim,
RESOLVE the flag — remove the inline marker and append to the entry:
`verified against <URL>, <date> — quote attached`. If the source is
unreachable, ambiguous, or conflicts with the claim, the flag STAYS (Tier C).

**Tier C — human-mandatory (flag always survives to the human).**
- Any Tier-B claim whose source was unreachable/ambiguous/conflicting
- Legal or tax RATES and THRESHOLDS the article states as current law, where
  the fetched source predates the current year or the quote does not match
  verbatim
- Medical claims about outcomes, risks, success rates
- Anything about the partner clinic (prices, equipment, credentials) — only
  the site owner can confirm these
These keep the inline `[VERIFY]`/`[CONFLICT]`/`[DATA NEEDED]` marker, each
with its pre-fetched citation + quote in 06-verification.md so the human
check is confirm-by-reading, not research.

## Verify-assist (run step)

After 05b is final and BEFORE Step 7 (Gemini), run a fresh-context
verification pass over every flag in the article:
1. For each flag, find and fetch the PRIMARY source (official bodies above —
   never blogs, portals, competitors).
2. Classify per the tiers. Tier-A markers that slipped in → remove (fix the
   framing if needed, e.g. add „Stand MM/JJJJ"). Tier B confirmed → resolve
   as described. Everything else → Tier C, stays.
3. Write 06-verification.md with three sections: RESOLVED (claim, source URL,
   quote, date), REMAINING FOR HUMAN (claim, best source found, what to
   check), and a one-line count summary. The PR body cites the counts.
4. NEVER alter the claim itself to match a source — a mismatch is [CONFLICT],
   the human decides.

## Hard limits (unchanged from the base pipeline)

- No flag may be resolved by reasoning, memory, or a secondary source — only
  a fetched primary-source quote resolves, and only for Tier B.
- The compliance lines, risk sections, and example-framing are untouchable.
- Merge = approve stays the human act. This policy reduces the human's
  per-fact workload; it does not remove the human from the loop.

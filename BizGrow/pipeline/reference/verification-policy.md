# BizGrow Verification Policy (brand-specific; does NOT apply to the other brands)

Written 2026-11-15 for the BizGrow onboarding, modelled on ElleDental's policy with the medical
tiers replaced by B2B claim tiers. Load this file at Stage 1 (Synthesis), Stage 2 (Author),
Stage 5 (Brand Gate) and Step 6 (verification + content file).

Base principle: **the AI never closes a business question.** It finds and quotes sources so the
owner's check is confirm-by-reading, but only the owner decides. Merge of the PR stays the human
act and does not mean "approved by the owner".

## Where open questions live

| kind of question | in drafts (01 … 05b) | in the final content file |
|---|---|---|
| external fact or figure (market data, GDPR text, platform feature) | inline `[VERIFY: … — URL]` | source in `[[sources]]` + one `[[owner_items]]` entry; the inline marker is removed |
| fact about BizGrow not in the canon, current-page copy not in the owner list, an H1 change, a „ти“→„Вие“ CTA/heading change, an example scenario kept | inline `[OWNER CONFIRM: …]` | one `[[owner_items]]` entry each, decision fields empty; the text says only what is known |
| missing business data (prices, team, timelines beyond canon, tools used) | `[DATA NEEDED: …]` | one `[[owner_items]]` entry asking the owner; the text is written around the gap |
| non-business (an address that does not exist, a wording choice) | `[LINK NEEDED: …]` | removed from the text; listed in `06-verification.md` REMAINING FOR HUMAN |

The final content file must contain no bracketed marker at all.

## Tiers

**Tier A — canon and current-page facts.** A fact in the BizGrow canon (`markets/bg/author.md`,
owner-confirmed 2026-11-15) or already on the current page and confirmed by the canon. No new
flag.

**Tier B — source-checkable external facts (max 3 per page).** From an authoritative public
source: EUR-Lex / the GDPR text, the European Commission or EDPB, Комисия за защита на личните
данни, НСИ, Eurostat, OECD, the platform's own official documentation (Meta, Google, Microsoft)
about its own product, or a peer-reviewed paper. Step 6 fetches the source, confirms HTTP 200
(`curl -sI`), quotes the supporting passage in `06-verification.md`, adds the source to
`[[sources]]` (empty `checked_by` / `checked_on`) and writes the `[[owner_items]]` entry. A
confirming quote does **not** resolve the item; it makes the owner's check fast. If the source is
unreachable, ambiguous or disagrees, the fact is removed from the text and logged; it is never
kept on the strength of memory, a vendor blog, a listicle or an AI-generated statistic.

**Tier C — owner only, never stated without the owner.** Anything about BizGrow beyond the canon:
prices, team, legal data, address, phone, clients, case results, vendors and AI models used,
data location, turnaround beyond canon, counts of projects or clients, certifications. Stays out
of the text and becomes an `[[owner_items]]` request.

**Examples and estimates.** A hypothetical example or estimate is allowed only if the current
page or the owner already uses it, it is labelled as an example in the same section, and its
numbers are not presented as client results. A new example scenario needs an `[[owner_items]]`
entry; a new number inside it needs Tier B support or is dropped.

## Never

- Never resolve a business question by reasoning, memory, a competitor agency page, a forum or a
  vendor's marketing page. Competitor pages are read for search intent and structure only.
- Never alter a fact to match a source. A mismatch is an `[[owner_items]]` entry.
- Never fill `decision`, `decided_by`, `decided_on`, `checked_by`, `checked_on`.
- Never drop an existing `[[owner_items]]` entry, even one that looks answered.

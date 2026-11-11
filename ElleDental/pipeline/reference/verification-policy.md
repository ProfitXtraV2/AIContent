# ELLE Dental Verification Policy (brand-specific; does NOT apply to VsichkiKazina or DentalVia)

Written 2026-11-11 for the ELLE Dental onboarding. It is STRICTER than DentalVia's policy
because ELLE Dental is the treating clinic itself and every page is YMYL medical content
under a named doctor's review. Load this file at Stage 1 (Synthesis), Stage 2 (Author),
Stage 5 (Brand Gate) and Step 6 (verification + content file).

Base principle: **the AI never closes a medical question.** It finds and quotes sources so the
doctor's review is confirm-by-reading, but only the doctor decides, and only the human sets
`reviewed_by`. Merge of the PR stays the human act and does not mean "reviewed".

## Where open questions live

| kind of question | in drafts (01 … 05b) | in the final content file |
|---|---|---|
| medical fact, risk, contraindication, emergency wording, H1 change, doctor-profile fact | inline `[VERIFY: …]` / `[CONFLICT: …]` | one `[[clinical_items]]` entry each, decision fields empty; the inline marker is removed |
| missing medical data (durations, visit counts, equipment, НЗОК) | `[DATA NEEDED: …]` | one `[[clinical_items]]` entry asking the doctors; the text says only what is known |
| non-medical (address of a page that does not exist, a wording choice for the owner) | `[LINK NEEDED: …]` / `[VERIFY: …]` | removed from the text; listed in `06-verification.md` REMAINING FOR HUMAN |

The final content file must contain no bracketed marker at all (the site gate rejects them).

## Tiers

**Tier A — existing page facts.** A medical fact that is already on the current page, worded
the same, and already backed by the page's `[[sources]]` or an existing `[[clinical_items]]`
entry. No new flag; it stays under the doctor's pending review of the whole page.

**Tier B — source-checkable, still doctor-confirmed.** A new medical fact (max 3 per page)
from an authoritative public source: NHS, Mayo Clinic, Cleveland Clinic, ADA, Cochrane,
European specialist society guidelines (e.g. ESE, EFP), a national regulator, or a
peer-reviewed paper. Step 6 fetches the source, confirms the URL returns HTTP 200 (`curl -sI`),
quotes the supporting passage in `06-verification.md`, adds the source to `[[sources]]` (empty
`checked_by` / `checked_on`) and writes the `[[clinical_items]]` entry. Unlike DentalVia's
Tier B, a confirming quote does **not** resolve the item: it only makes the doctor's check fast.
If the source is unreachable, ambiguous or disagrees, the fact is removed from the text and
logged in `06-verification.md`; it is never kept on the strength of memory or a secondary site.

**Tier C — owner/doctor only, never stated without them.** Anything about the clinic itself:
equipment, materials and brands, years in practice, case counts, visit durations, the number
of visits, НЗОК contract, opening exceptions, prices, guarantees of any kind. Doctor-profile
facts from the Superdoc copy in `markets/bg/author.md` may be stated as written there, each
with a `[[clinical_items]]` confirm entry. Everything else in Tier C stays out of the text and
becomes a `[[clinical_items]]` request.

## Never

- Never resolve a medical question by reasoning, memory, a competitor clinic page, a forum or
  a portal. Competitor pages are read for search intent and structure only, never for facts.
- Never alter a fact to match a source. A mismatch is `[CONFLICT]`, then a clinical item.
- Never set `reviewed_by`, `reviewed_on`, `also_reviewed_by`, or fill `decision`,
  `decided_by`, `decided_on`, `checked_by`, `checked_on`.
- Never drop an existing `[[clinical_items]]` entry, even one that looks answered.

BRAND: vsichkikazina
MARKET: bg
CONTENT TYPE: hub-intro (category-page intro copy — NOT a standalone article; see "Hub-intro rows" in automation/daily-run.md §3.a2)
BYLINE: editorial voice, signed Георги Тодоров (byline override — always his name, never a team byline)
TARGET QUERY: HUB INTRO: Регулации и данъци — интро за /blog/regulations-taxes/
KEYWORDS_OR_TERMS: хазартни закони българия, данък върху хазартни печалби
INTENT: informational
LENGTH: 350-500 words body prose. NO H1 (hub page already renders one). At most TWO ## subheadings. No images, no FAQ, no comparison tables.
TARGET CATEGORY PAGE: https://vsichkikazina.bg/blog/regulations-taxes/
SLUG: hub-intro-regulations-taxes

## SCOPE NOTE (per daily-run.md CURRENT CONTENT SCOPE)
This is generic regulatory/tax education, not an operator-T&C or НАП-register-dependent
claim (no specific operator names' licence status, no live licence numbers looked up).
Content stays at the level of: what a licence from НАП means, that gambling in BG must
be licensed to be legal, that winnings tax treatment falls under ЗДДФЛ and readers should
verify the current rule/rate themselves. No specific tax percentage or rate is asserted as
fact — hedged per the orchestrator's explicit instruction, since tax specifics can change
and this content type must never fabricate a legal/tax fact.

Quick web-search sanity check done (2026-09-19, generic search, not treated as a primary
operator source): a public НАП register of licensed operators exists (nap.bg, "хазарт"
section) where each entry lists company, licence №, category, validity — confirms it's
reasonable to tell readers "provеri в регистъра на НАП" as a real, existing action. Winnings
taxation is governed by чл. 13 ЗДДФЛ — sources disagree/are stale enough on the exact
current treatment that this brief does NOT assert a specific rate or exemption as fact;
the article will name the article (чл. 13 ЗДДФЛ) as the relevant provision and tell the
reader to check the current text / consult an accountant, per house doctrine (tax claims
are always [VERIFY] + референция към счетоводител/НАП).

## CONTENT — what this hub-intro must cover
1. What "регулации и данъци" as a category covers for a BG player: what a НАП licence is
   and why it is the entry ticket (site's own licence-first doctrine), legality of offshore/
   unlicensed casinos operating without a BG licence, and that winnings taxation sits under
   ЗДДФЛ чл. 13 (hedge the specifics, point to verification).
2. What to check before playing anywhere: how to check a casino's licence (register/proverka
   guide), the difference between a licensed and an unlicensed operator (support/complaints/
   consumer protection, blocked domains), and that tax obligations are the player's own
   responsibility to verify.
3. Weave in naturally, NOT as a bare list:
   - Money page (at least 1, required): /casino/betano/ — framed as an example of an
     operator holding a НАП licence ("казино с лиценз от НАП като Betano"), plain on-site
     link, NOT the /go/ affiliate redirect.
   - Category's own articles (weave in 1-2): /blog/danaci-pechalbi-onlajn-kazino/ (данъци
     върху печалби от онлайн казино) and /blog/proverka-licenz-kazino/ (проверка на лиценз
     на казино).
   Use relative paths in Markdown links, matching the site's normal internal-link convention
   (confirmed against 2026-09-19-red-tiger/05b-final-draft.md: plain relative paths like
   /kak-ocenyavame/, /otgovorna-igra/).

## AHREFS / ENRICHMENT
Skipped per explicit orchestrator override for this one-off hub-intro batch.

## DEDUP / ANTI-CANNIBALIZATION
Skipped per explicit orchestrator override — the target category page already exists by
design; this is intro copy for it, not a competing standalone article.

## SOURCES (background only, general/public, not operator-specific)
- https://nra.bg/wps/portal/nra/gambling/licensing.gambling.operators (НАП: лицензиране на хазартни оператори — public register exists)
- https://nra.bg/wps/portal/nra/gambling/Online-hazat (НАП: онлайн хазарт)
- General search confirms чл. 13 ЗДДФЛ (ал.1) is the provision covering tax treatment of
  gambling winnings, with some third-party commentary (kik-info, lex.bg) discussing details
  — NOT treated as verified/citable fact for this article; kept hedged per instructions.

## INTERNAL LINKS TO USE (pre-verified against live sitemap by the orchestrator)
- /casino/betano/ (money page, required, framed as licensed-operator example)
- /blog/danaci-pechalbi-onlajn-kazino/ (category article)
- /blog/proverka-licenz-kazino/ (category article)

## ANECDOTE OPT-IN: no (default — editorial voice, signed Георги Тодоров per byline override)
## NOTES: type=hub-intro; content-queue id vk-0121 (added centrally by orchestrator, not by
this agent). Step 8 (images) skipped entirely — no images/ folder. Skip FAQ/comparison
tables per hub-intro spec.

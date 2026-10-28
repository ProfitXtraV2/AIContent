# ONE-OFF — Refresh 4 live blog posts with zero Google impressions (2026-10-28)

**Owner-requested.** Search Console (90 days to 2026-10-26) shows these four live posts, all
published 6–10 Sept, with **0 impressions** after ~7 weeks, while posts published at the
same time get impressions. The text is not thin (1.0–1.5K words). The problem is
**targeting/intent**: the titles don't match how people search. Re-run the full editorial
pipeline on each, retargeted as specified below, **keeping the exact same slug/URL**.

## How this run differs from the daily run
- **Same URL is intended:** folder = `<TODAY>-<existing-slug>`, so `build_feed.slug_from_folder`
  yields the live slug and the publisher re-renders `/blog/<slug>/` in place (content_hash
  changes). **Skip dedup (3d) and anti-cannibalization (3d2)** for these four, since the
  page already exists by design. Do NOT invent a new slug.
- **Input = the live page.** Fetch `https://vsichkikazina.bg/blog/<slug>/` and use its text
  as source material for Synthesis (keep what's correct and useful; restructure around the
  new target). For `novi-kazino-igri-2026` also read the existing pipeline folder
  `VsichkiKazina/articles/2026-09-08-novi-kazino-igri-2026/`.
- **content-queue.md:** add one NEW row per article (fresh `vk-` id, `type: guide`,
  `source: refresh`, `folder: <TODAY>-<slug>`, volume/kd from below). Note
  `REFRESH of live /blog/<slug>/ (0 GSC impr 90d)`. Leave the old vk-0015 row untouched.
- Everything else is unchanged: stages 1→5b as fresh-context subagents, number diffing,
  Brand Gate, Step 7 Gemini check + keep-best, Step 8 images, 06-verification, one PR per
  article on `content/<folder>`, commit trail. **Do not approve, merge or publish.**
- **Byline:** Георги Тодоров. **No affiliate links** unless the brief says so.
  RG line + 18+ as usual.
- Write all four. If one fails a hard gate, mark it `failed` with a reason and continue.

---

## 1. `danaci-pechalbi-onlajn-kazino` — tax on winnings (YMYL)
- **Primary keywords:** `данък печалба от хазарт` (50/mo), `данък хазарт` (30), plus
  `облагат ли се печалбите от казино`, `данък върху печалба от онлайн казино`,
  `данък печалба тото`. KD ≈ 0–4.
- **Title direction:** „Данък върху печалба от хазарт и онлайн казино в България (2026)".
  H1 close to the title. Meta description answers the question in one line.
- **Answer first:** the first paragraph states the rule plainly: winnings from a game
  organised under a licence (ЗХ or another EU/EEA state) are non-taxable income under
  **чл. 13, ал. 1, т. 20 ЗДДФЛ**, in force since 01.01.2017.
- **Source:** `VsichkiKazina/source-packs/zddfl-gambling-winnings-2026-10-28.md`. This
  pack **explicitly unblocks the tax claim** for this article (the guides-only „0 данък
  claim" rule is lifted ONLY for what the pack states). Anything beyond the pack, such as
  the treatment of unlicensed/non-EU winnings, rates or declaration duties, MUST be
  `[VERIFY]` or omitted. Never state a rate.
- Cover: the rule (licensed BG / EU/EEA), why the licence is the deciding factor (link
  `/blog/proverka-licenz-kazino/`), тото/лотария winnings (same rule, licensed organiser),
  what a bank may ask about large incoming sums (generic, hedged), that losses are not
  deductible (keep only if the live page's wording can be kept hedged), when to ask an
  accountant. FAQ: 3–4 real questions phrased as people search them.
- Internal links: `/blog/proverka-licenz-kazino/`, `/zakonno-li-e/`, `/sravni-kazina/`
  (licensed list), `/blog/regulations-taxes/`.

## 2. `koe-kazino-da-izberete` — how to choose a casino
- **Primary keywords:** `как да изберете онлайн казино` (GSC: 14 impr hitting the HOMEPAGE
  at pos 36, so the intent is unmet), `как да изберем онлайн казино`,
  `кое казино дава най много` (20/mo, GSC shows homepage at pos 21),
  `кое онлайн казино дава най много`. SERP = guide articles from DR 17–45 sites, so winnable.
- **Title direction:** „Как да изберете онлайн казино: кое е подходящо за вас (и кое дава
  най-много)".
- **Must NOT become a toplist.** The homepage and `/sravni-kazina/` own the ranking intent.
  This is the decision guide, so keep the strong „by player type" structure of the live page.
- **Add an honest „Кое казино дава най-много?" section:** what actually differs between
  casinos (game RTP is set per game/version and can differ between operators, wagering
  terms, withdrawal limits and speed, bonus caps) vs what doesn't (no casino „pays more" in
  general). Generic mechanics only, no operator-specific figures (guides-only scope).
- Open with a 5-step checklist (licence → payments/withdrawals → bonus terms → games/RTP →
  mobile/support) that answers the query immediately.
- Internal links: `/sravni-kazina/` (money page, prominent), `/kak-ocenyavame/`,
  `/blog/proverka-licenz-kazino/`, `/slot-igri/visok-rtp/`, `/depoziti-i-teglenia/`.

## 3. `rechnik-kazino-termini` — glossary
- **Keep it a glossary.** Many drafts link here, so it's an internal-link hub. Do NOT
  retarget it to bare `волатилност` (500/mo): that SERP is 100% finance (Tavex, Admiral
  Markets, credit glossaries), so a casino page won't rank there.
- **Primary keywords:** `казино термини`, `казино речник`, `какво означава превъртане на
  бонус`, `какво е RTP`, `волатилност слот значение`, `какво е wager`.
- **Title direction:** „Казино речник: значение на RTP, волатилност, превъртане и други
  термини".
- **Structure for snippets:** one entry per term, `### Термин` + a **one-sentence
  definition first**, then 1–3 sentences of practical meaning, then a link to the deeper
  article where one exists. Add an A–Я jump index at the top. Group sections as now
  (бонуси, игрова математика, ротативки, на живо, плащания/регулация).
- **Expand coverage** to the mechanics our posted articles already explain (scatter, wild,
  Megaways, hold & win, bonus buy, мистерия символи, множители, ретригер, RNG, крах игри,
  live game show…) and link each to its article (pick URLs from the live sitemap; only
  link pages that exist).

## 4. `novi-kazino-igri-2026` — new casino games
- **Primary keyword:** `нови казино игри` (**1,700/mo**, KD 42). That's above the KD cap
  of 40, but this is an owner-approved override because the page already exists and the
  current #1 in BG is a DR 6 site's games listing page.
  Secondary: `нови казино игри 2026`, `нови игри казино`, `нови ротативки` (50),
  `нови казино игри безплатно` (30).
- **Fix the intent mismatch.** Searchers want a **list of new games**; the live post is a
  „how to evaluate a new game" framework, which is why it gets nothing. Rewrite
  **listing-first**: „Нови казино игри 2026" = a roundup of notable 2026 releases across
  **all game types** (slots, crash, plinko-style, live game shows), each with provider,
  type and the key mechanic, plus a link to our own article where we have one (e.g.
  gates-of-olympus-1000, sugar-rush-1000, le-bandit, olympus-glory, plinko, tombstone-rip,
  eye-of-horus; verify in the sitemap). Release dates/RTPs only from the provider's own
  page; otherwise `[VERIFY]`. Keep a SHORT „как да оцените нова игра" section (RTP,
  волатилност, демо) from the old text at the end.
- **Anti-cannibal with `/slot-igri/novi/`:** that page is the slots-only listing. This post
  is the all-game-types roundup and links to it once („всички нови слотове").
- Internal links: `/slot-igri/novi/`, `/kazino-igri/`, `/blog/rechnik-kazino-termini/`,
  `/blog/bezplatni-kazino-igri/`.

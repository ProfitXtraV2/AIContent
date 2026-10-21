# 06-VERIFICATION — vk-0283 · Тото онлайн: как да играете законно на сайта на БСТ (toto.bg)

Type: guide (editorial, procedural/legal) · Byline: Георги Тодоров · Market: bg
Published/updated: 17.10.2026

## Surviving flags (STAY IN TEXT — human owns resolution)
- **1 × [VERIFY]** — данъчен режим на печалбите от ТОТО. Deliberately NOT asserted with any figure; the text routes the reader to счетоводител/НАП. Tax is ALWAYS [VERIFY] per brand rule. → human to confirm current ЗДДФЛ treatment of lottery/тото winnings with an accountant or НАП before resolving.
- **0 × [CONFLICT]**, **0 × [DATA NEEDED]**.

## Time-sensitive / primary-source claims (verify at publish + periodically)
All operational facts about toto.bg were read in a real BG browser session on 2026-10-10 (source pack `source-packs/bst-toto-2026-10-10.md`; toto.bg is Radware-CAPTCHA-gated for scripts, so re-check in a browser):
- Draw schedule, betting-acceptance windows (in effect from 08.12.2022), the 18:40–19:10 ч. Thu/Sun downtime, БНТ live draws 18:45 ч., auto-payout of online ТОТО 1/ТОТО 2/Тото Джокер winnings, ВТШ (6/49, 5/35) email notice, ePay.bg/БОРИКА payments, online@toto.bg — source: toto.bg „Информация" + results board. **Re-check the schedule on toto.bg before publish** (БСТ can change acceptance windows by order of the ИД).
- Registration/identification of participants + real-time data to НАП server: Наредба за регистрация и идентификация (ПМС № 50 от 15.02.2021 г., в сила 21.02.2021 г.) — source pack `nap-gambling-law-and-rg-2026-10-10.md`.
- НАП blocks access to an unlicensed site by decision within 24 часа (чл. 17, ал. 6 ЗХ, in force since 01.08.2026); player fine 500–2000 лв. (чл. 9, ал. 14 + чл. 97а, ал. 2 ЗХ); signals illegal_gambling@nra.bg (no anonymous). Source: nap pack §4 (consolidated ЗХ to ДВ бр. 69/31.07.2026). **Re-check against the current consolidated ЗХ at publish.**
- ТОТО = числова лотарийна игра; хазарт only after лиценз от НАП (чл. 3 ЗХ); 18+ (чл. 2, ал. 3 ЗХ). Source: nap pack §3.
- RG: НАП budget rec ≤ ~5% net income; регистър на уязвимите лица (чл. 10г ЗХ, from 12.12.2022), written filing, срок ≥ 12 м., not public, info 0700 18 700; Линия „Солидарност" 0888 99 18 66. Source: nap pack §5–6.
- БСТ context (state enterprise, operating тото since 1957) — bg.wikipedia „Български спортен тотализатор" (context only; no numbers taken from it).

## „Recalculate one figure" check
This guide deliberately contains NO computed figures — no odds, EV, prize amounts, ticket prices, or payout percentages (out of scope; those did not render even in the browser and are routed to the game-mechanics pillars instead). So there is no derived calculation to re-verify. Instead, a fact-trace was run: every number in the text and in the infographic was matched 1:1 against the two source packs (schedule times, dates, law articles, the 500–2000 лв. statutory fine, the 5% RG recommendation, the 12-месеца register term). The infographic's figures (19:20 / 18:00 / 18:40–19:10 / 08.12.2022 / ТОТО 1+ТОТО 2) all trace verbatim to 05b, confirmed by the Gemini image review (accuracy FLAWLESS, 100/100).

## Number-diff discipline across stages
DIFF ALL NUMBERS was run between every text-editing stage (02→03→04→05→05b and each Step-7 humaniser pass): the article-body numeric multiset was IDENTICAL at every step (the only non-numeric deltas were intended repeat-mention reductions of toto.bg/ePay.bg/БОРИКА when a recap sentence was removed, and the restore to the keep-best pass-0 version). No number was changed, added, or dropped.

## Gemini Step-7 (text, cross-model) — final
- Verdict kept: **ai 65** (human-likeness 35). Keep-best = **pass 0** (baseline post-Brand-Gate).
- Ledger: baseline HL 35 → humaniser pass 1 HL 30 → humaniser pass 2 HL 25 (MAX_GEMINI_PASSES=2 reached). Each pass applied legit style edits (removed the summary/signposting/filler/truism; killed the one „не X, а Y" contrast; reduced colon-gluing; integrated link signposting) but the noisy/adversarial detector lowered the score and relocated flags each pass (it even flagged idioms it earlier praised) — same pattern seen on vk-0063/0264/0279/0282 for dry statute/procedure content. Per the keep-best mandate the highest-HL version (pass 0) is shipped; the lower later passes live in git + checks 1–3 as the audit trail. **Human voice polish advised** (facts/flags/RG/disclosures all correct and untouched).

## Step-8 images
images: 2 (infographic 100, hero 95). Both Gemini-review PASS first time, 0 integrity failures. Infographic numbers all trace to 05b; hero purely decorative (no text/numbers/logos/people). Hero under H1, infographic beside the schedule section, both with specific Bulgarian ALT.

## Brand Gate
PASS WITH FIXES 91/100 (Personality 18 · Tone 14 · E-E-A-T 18 · Trust 13 · Language&Style 14 · RG 14). 2 mechanical criticals (unfilled boilerplate slots) fixed. 0 remaining criticals. Byline Георги Тодоров; brand „Всички Казина"; verbatim 18+ RG line + /otgovorna-igra/ + регистър на уязвимите лица + „Солидарност"; verbatim 01.08.2026 affiliate-licensing disclosure (site licence stated as application-pending, no invented №); tax [VERIFY] not asserted; 0 em-dashes in prose; only toto.bg named; no affiliate link (state operator).

## Scope note
Guides-only autopilot scope respected: state operator БСТ + public law (Наредба ПМС 50/2021, ЗХ, НАП RG framework), no private-operator T&C and no НАП-register query — not geo-blocked. No prize amounts/prices/payout%/odds anywhere. No reseller/mirror/look-alike named or linked.

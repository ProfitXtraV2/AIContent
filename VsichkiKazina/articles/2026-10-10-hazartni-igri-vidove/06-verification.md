# 06 — Verification — „Хазартни игри: какво е хазарт по закон и кои видове са разрешени в България"

Queue id: vk-0264 · Type: guide (legal taxonomy of gambling games under the Закон за хазарта) · Byline: Георги Тодоров (editorial voice)
Scope: guides-only safe — public law text + НАП source pack; NO operator facts, NO licence №, NO affiliate operator, NO sports tips.
Flags STAY in the text for the human (Step 6). Claude did NOT resolve any flag.

Primary law source used: consolidated Закон за хазарта (incl. amendments up to ДВ бр. 69 от 2026 г.) on
https://kik-info.com/normativna-baza/zakoni/0X2135783265/ (fetched 10.10.2026). lex.bg
(https://lex.bg/laws/ldoc/2135680996) returned an „Unauthorized" stub. НАП facts: VsichkiKazina/source-packs/nap-gambling-law-and-rg-2026-10-10.md
(nra.bg pages fetched via a BG browser on 10.10.2026).

## SURVIVING [VERIFY] FLAGS (4 distinct, 5 occurrences)
1. **Срок на лиценза 5 или 10 години** (section „Един лиценз покрива една игра").
   · НАП: https://nra.bg/wps/portal/nra/gambling/licensing.gambling.operators — „5 или 10 години" (source pack §2).
   · Pre-assembled for the human: the kik-info consolidated text, **чл. 26, ал. 3 ЗХ**: „Срокът на действие на издадения
     лиценз е за еднократно организиране, за 5 години или за по-кратък срок, когато заявителят изрично го е поискал";
     **чл. 26, ал. 4**: 10 години само когато предварително доказаните инвестиции надвишават законовите прагове. So the
     unconditional „5 или 10 години" is a simplification — consider „по правило 5 години, а при по-големи инвестиции 10"
     when resolving.
2. **Пълнолетие = 18 години — законова норма** (section „От колко години…" + FAQ; 2 occurrences).
   · ЗХ чл. 2, ал. 3 (изм. ДВ бр. 42/2024): участват само „пълнолетни дееспособни физически лица" (verified, kik-info).
   · Age of majority 18: Закон за лицата и семейството, чл. 2 (human to confirm the citation).
3. **„чл. 10, ал. 11 ЗХ" — забрана за продажба на лотарийни билети на ненавършили 18 г.**
   · ⚠ Pre-assembled finding: in the kik-info consolidated text the provision „Забранява се продажбата на билети, фишове,
     талони или други удостоверителни знаци за участие в лотарийни игри на ненавършили 18-годишна възраст лица и на лица,
     поставени под пълно или частично запрещение" is **чл. 9, ал. 11** (нова ДВ бр. 14/2020, доп. ДВ бр. 42/2024), NOT
     чл. 10. Only the flag text cites the article number (the prose doesn't), but the human should correct it when resolving.
4. **НАП „5% от нетните доходи" + примерът €1 200 → €60/месец** (section „Колко да отделяте…").
   · Source: https://nra.bg/wps/portal/nra/gambling/responsible.gambling/Suveti-za-razumno-zalagane (source pack §6:
     „Бюджетът не бива да надвишава 5% от нетните ви доходи"). The €1 200 salary is illustrative.

## TIME-SENSITIVE CLAIMS (primary-source pointers)
- Петте вида (чл. 41, ал. 1), каналът не сменя вида (чл. 41, ал. 1, изр. 2), онлайн всички без томбола и моментна лотария
  (чл. 41, ал. 2) — verified verbatim in the consolidated ЗХ; also НАП https://nra.bg/wps/portal/nra/gambling/Online-hazat.
- Затворен списък (чл. 3, ал. 2); лицензът само за посочената игра (чл. 3, ал. 3); само евро от 01.01.2026 г. (чл. 3, ал. 4,
  изм. ДВ бр. 70/2024) — verified.
- Държавен монопол върху лотарийните игри без томбола и бинго (чл. 4, ал. 3) — verified.
- НАП е регулатор от 08.08.2020 г. (ДВ бр. 69 от 04.08.2020 г.); преди — ДКХ — https://nra.bg/wps/portal/nra/gambling.
- Списъци на лицензирани/нелицензирани сайтове; СРС спира достъпа (чл. 17, ал. 6); illegal_gambling@nra.bg; БИМ регистър;
  данни в реално време към НАП (чл. 6) — source pack §4.
- Регистър на уязвимите лица (чл. 10г): не е публичен; срок мин. 12 месеца; НАП 0700 18 700 — source pack §5.
- Чл. 10б: предупреждение за хазартна зависимост на сайта — source pack §2.
- Солидарност 0888 99 18 66, делнични дни 10:00–17:00 — brand canon (brand-gate-vsichkikazina.md).
- Affiliate-licensing footer (ДВ бр. 69 от 31.07.2026 г.): brand template; site licence stated as applied for/pending.

## FIGURE CHECK (recalculation with working shown)
- Fixed-odds example (чл. 60, ал. 4, т. 1): залог €10 × коефициент 2,50 = €25,00 общо изплащане (вкл. залога); нетна печалба €15. ✓
- НАП budget rule: 5% × €1 200 = 0,05 × 1 200 = €60 на месец. ✓
- „Правилото за еврото е на по-малко от година": 01.01.2026 → 10.10.2026 = 9 месеца и 9 дни < 12 месеца. ✓

## EXTERNAL CHECK (Step 7, Gemini)
- external check: skipped (Gemini unavailable — cloud backfill pending). `scripts/gemini_check.py` → `GEMINI_UNAVAILABLE: GEMINI_API_KEY not set` (exit 2).
- content-queue `gemini` column → `skipped` (coordinator).

## IMAGES (Step 8)
- images: 1 (infographic; Gemini review skipped — cloud backfill pending).
  `images/hazartni-igri-vidove-zakon-onlajn-infografika.svg`: the 5 types + examples, online yes/no, legal basis (чл. 48–49,
  60, 62, 64, 71), footnotes чл. 41, ал. 1–2 and чл. 3, ал. 3, 18+ line. Every figure/article number traces to 05b.
  No logos, operator names, people or glamorised winning.
- svg_layout_lint.py (from commit 8c0af30e): ✓ no hard defects, no warnings. Rendered to PNG via headless Chrome at 760×580 and
  checked by eye: no clipping, no overlap.
- image review: skipped (Gemini unavailable). AI hero: skipped (needs Gemini).

## BRAND GATE
- PASS WITH FIXES: 84/100 as received → ~93/100 after fixes (Personality 18 | Tone 14 | E-E-A-T 16 | Trust 10→fixed | Lang&Style 12 | RG 14).
- Fixes: pub/updated dates, covers/doesn't framing, em-dash in flag removed, lottery-subtype list → prose, „мнозина пропускат"
  softened, limits-before-first-deposit RG touch, verbatim affiliate-licensing footer.
- Editor decision left open: 8 internal links (brand bible says 2–4; all 8 are approved and live). Consider trimming.

## INTERNAL LINKS (all live in sitemap.xml, checked 10.10.2026)
/zakonno-li-e/ · /otgovorna-igra/ · /kazino-igri/ · /blog/regulations-taxes/ · /blog/proverka-licenz-kazino/ ·
/blog/keno-pravila/ · /blog/kak-se-igrae-poker-kazino/ · /blog/danaci-pechalbi-onlajn-kazino/

## HUMAN TODO (Step 6)
Resolve the 4 [VERIFY] flags above (note the чл. 9 vs чл. 10 finding and the чл. 26 licence-term nuance), fill the
[AUTHOR BIO BLOCK] / [BRAND BOILERPLATE] slots, then approve. Do not publish with flags in the text.

## CLOUD RECONCILE 2026-10-10 — Step 7 + Step 8 (supersedes the „skipped" lines above)
- STEP 7 — external check: check 1 (handed-off 05b) Gemini **Likely AI-generated, 80%** → human-likeness 20. Humaniser pass 1 (7b, fresh context) + quick Brand Gate re-check → check 2 **Shows AI patterns, 75%** → hl 25. Humaniser pass 2 (7b) + Brand Gate re-check → check 3 **Shows AI patterns, 80%** → hl 20. MAX_GEMINI_PASSES (2) reached → **keep-best = pass 1 (hl 25)**, restored as final 05b (`content(...): keep best version (pass 1, 25%)`). Every pass diff-verified: numbers, links, flags, чл./ал. refs, byline, brand, 18+/RG unchanged; 0 em-dashes; H1 unchanged. Did NOT reach 80 → **human editor attention advised** (Gemini's residual critique: conversational asides, signposting before internal links, templated FAQ — see `07-gemini-check-2.md`). content-queue `gemini` → `ai 75`.
- STEP 8 — Gemini image review: score 100 (PASS, no integrity issue) — `08-image-review-1.md`. images: 1 (infographic 100). No AI hero added (review did not ask for one).
- Flags untouched ([VERIFY] ×5 incl. 1 duplicate stay for the nightly fix job / human).

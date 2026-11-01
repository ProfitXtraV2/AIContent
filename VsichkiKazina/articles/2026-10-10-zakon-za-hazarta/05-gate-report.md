# 05 — Brand Gate report (Всички Казина, Step 5)

Gate used: pipeline/agents/brand-gate-vsichkikazina.md + pipeline/prompts/step-5-brand-gate.md
Input: 04-seo.md (title tag + meta + article; SEO AUDIT read as context only)
Fact-tracing against: 00-brief.md, 00-sources.md
Byline: editorial „ние" voice, published byline Георги Тодоров · Content type: guide (no operator, no affiliate link)
Output article: 05-gated-article.md

```
BRAND COMPLIANCE SCORECARD — Закон за хазарта: какво трябва да знае играчът и какво се промени през 2025–2026
Verdict: PASS WITH FIXES
Total: 85/100 (pre-fix; both criticals mechanically fixed, see below)
Personality 18/20 | Tone 13/15 | E-E-A-T 16/20 | Trust signals 13/15 | Language&Style 12/15 | RG 13/15
```

## CRITICAL (blocked publish, now fixed or routed)

1. „Самата НАП съветва този бюджет да не надвишава 5% от нетните ви доходи." → FACT SWEEP: the claim is not in 00-brief.md or 00-sources.md. It may be in the source pack (НАП responsible.gambling page), but this gate was not allowed to read that file, so the claim is unsupported here. → No fix invented. Sentence kept and tagged `[VERIFY: препоръката на НАП за 5% от нетните доходи не е в 00-brief/00-sources; проверете в source pack nap-gambling-law-and-rg-2026-10-10.md или махнете изречението]`. The human confirms it or deletes it at Step 6.
2. Em-dashes (—) inside two [VERIFY] flags (регистър „30 дни" flag and the § 79 flag) → Pillar 5 zero-em-dash rule. → Changed „ — " to „: " inside both flags. The flag wording is otherwise unchanged. The article now has 0 em-dashes. En-dashes in ranges (2025–2026, 10:00–17:00) are allowed and kept.

## MODERATE

- Formulaic two-part colon headings: 4 H2s used the „X: Y" pattern, plus the H1. → Changed the two non-SEO ones. „Лицензът: една игра, един лиценз" became „Един лиценз покрива една игра", and „Пълна забрана на рекламата: проект, не закон" became „Пълната забрана на рекламата е само проект". The two SEO-keyword H2s are unchanged („Забрана за реклама на хазарт: какво важи днес", „Закон за хазарта: промените през 2025 и 2026 г. по дати").
- „Друг регулатор, към когото играчът да се обърне, няма." is an absolute claim that 00-sources.md does not support. 00-sources.md itself shows СЕМ supervising advertising content (чл. 10, ал. 8). → Restated as a plain fact: „За въпроси по лиценза и нелегалния хазарт играчът се обръща към НАП."
- Guide-type trust check: the disclaimer did not say what the article leaves out. → Added one sentence to the disclaimer: „Данъците върху печалбите и стъпките за самоизключване не са тема на този текст." It makes no tax claim and adds no link. This matches the brief's exclusions.
- Grammar in the /zakonno-li-e/ anchor: „законно ли е онлайн хазартът" (gender agreement) → „законен ли е онлайн хазартът". The link target is unchanged.
- NOT FIXED, routed to human: the article links to /zakonno-li-e/, but per 00-sources S5 that page says „Регистрация в нелицензиран сайт не е технически незаконна за самия играч…". This contradicts the article's key point (чл. 9, ал. 14 + чл. 97а, ал. 2). The Stage 1 log says the link was meant to wait until that page is corrected, but the outline added it back. A human must either correct /zakonno-li-e/ before publish or drop the link.
- NOT FIXED (noted only): the lede has 6 sentences, slightly over the ~5 cap. There are 6 body internal links, above the brand's 2–4 but inside the brief's 4–6, which governs here. The чл. 6, ал. 1 list (5 long statutory conditions) is kept as a list because it is a genuine legal enumeration. The table (forbidden vs allowed advertising) is genuinely comparative and kept. „може да бъде блокиран за часове" is loose: the 24 h run from publication of the НАП decision. It is acceptable because it says „може".

## MATHS RECALCULATION (чл. 97а, ал. 2 fine, fixed rate 1,95583 лв./€)

- 500 ÷ 1,95583 = 255,6459… → **255,65 €**. Check: 1,95583 × 255 = 498,737; remainder 1,263 ÷ 1,95583 = 0,6459.
- 2000 ÷ 1,95583 = 1022,5838… → **1022,58 €**. Check: 1,95583 × 1022 = 1998,858; remainder 1,142 ÷ 1,95583 = 0,5838.
- The article states „около 255,65 € до 1022,58 €". **Correct.** The [VERIFY] on how the euro equivalent is applied after 01.01.2026 is kept as the brief requires.
- The article has no other maths claims: no превъртане, RTP or score arithmetic, since it is a guide with no operator.

## FACT TRACE (all supported by 00-brief / 00-sources unless listed above)

НАП supervision from 08.08.2020 (ДВ бр. 69/04.08.2020, earlier ДКХ) · чл. 3, ал. 1/3/4 · licence term (one-off / 5 years / shorter; 10 years only with investments) · чл. 41, ал. 1 five game types + онлайн рулетка = казино · чл. 6, ал. 1 (5 conditions, т. 5 in force from 01.08.2026) · чл. 2, ал. 3 (ДВ бр. 42/2024) · чл. 9, ал. 13/14/16/17/19/20 · чл. 97а, ал. 2 (500–2000 лв.) · чл. 97б (5 000–20 000 евро, ал. 19 only) · чл. 17, ал. 1, т. 9/9а, ал. 6 (24 h, санкция по чл. 97а, ал. 4, per S2) · illegal_gambling@nra.bg, no anonymous reports, two НАП lists · чл. 10б, 10г, 10д, ал. 2/3, 10е (01.01.2025), register restarted 12.12.2022 · 27.03.2025 12-month minimum (ДВ бр. 26) · 17.06.2025 (ДВ бр. 49, 5+ same-type AML breaches) · чл. 10, ал. 1/2/4/6/9 advertising table · 01.08.2026 ДВ бр. 69/31.07.2026, § 34, чл. 30а 6 000 € + 10 на сто · ЗИД draft MoF/strategy.bg 23.09–23.10.2026, official summary goals, § 79 [VERIFY]. No tax claims. Софийски районен съд is not described as the current blocking route. The draft is clearly labelled as a draft.
Unsupported: only the НАП 5% budget advice (CRITICAL 1).

## TRUST / RG CHECKLIST

Byline Георги Тодоров ✔ · „Всички Казина" exact ✔ · Публикувано / Последна редакция 10.10.2026 ✔ · About boilerplate slot ✔ · author bio slot ✔ · verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." ✔ (×2) · RG signposting to /otgovorna-igra/ + национален регистър на уязвимите лица (НАП) ✔ · Солидарност 0888 99 18 66 ✔ · verbatim 01.08.2026 affiliate-licensing footer, licence pending, no licence № ✔ · no operator links, so no affiliate-registry check applies ✔ · natural-voice RG touch (budget before the first deposit, the register section's „издържа и в моментите…") ✔ · no FOMO, no promise or hype words, no BG AI connectives ✔ · no fabricated anecdote ✔ · no [DATA NEEDED] in the text ✔ · no Version A/B dilemma ✔ · Bulgarian jurisdiction named ✔.

## FIXES APPLIED (05-gated-article.md vs 04-seo.md, 8 edits)

1. Disclaimer: added a sentence on what the article does not cover.
2. „Друг регулатор… няма." restated as a plain fact.
3. H2 „Лицензът: една игра, един лиценз" → „Един лиценз покрива една игра".
4. H2 „Пълна забрана на рекламата: проект, не закон" → „Пълната забрана на рекламата е само проект".
5. [VERIFY] „30 дни" flag: em-dash → colon.
6. [VERIFY] § 79 flag: em-dash → colon.
7. НАП 5% sentence: added a [VERIFY] tag (CRITICAL 1).
8. /zakonno-li-e/ anchor grammar fix.

All other text is unchanged: every number, date, чл./ал./ДВ reference, amount and link, the [INFOGRAPHIC] placeholder, the ПРОЕКТ blockquote, 18+/RG lines, disclosure, author block, title tag and meta.

## VERIFY QUEUE (route to human, Step 6)

1. [VERIFY] how the euro equivalent of the чл. 97а, ал. 2 fine is applied after 01.01.2026 (kept).
2. [VERIFY] the earlier 30-day minimum for deletion from the register (kept).
3. [VERIFY] § 79 of the draft: afiliate licences end 01.01.2027 (commenter quote) (kept).
4. [VERIFY] NEW: НАП advice that the budget stay within 5% of net income. Confirm in the source pack or delete the sentence.
5. /zakonno-li-e/ contradicts чл. 9, ал. 14. Correct that page or drop the link before publish.

## VOICE NOTES (protected)

The editorial „ние" register and the dry consumer-protection edge („Законът гледа и от другата страна на екрана", „друга защитима позиция при тази конструкция няма") are kept. The asymmetric, opinionated ending is kept. No re-toning was done.

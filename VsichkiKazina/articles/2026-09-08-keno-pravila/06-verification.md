# 06 — VERIFICATION · vk-0016 · Кено: правила, изплащания и реални шансове
*For the human at Step 6. FLAGS STAY IN THE TEXT — this file only helps you verify fast. Nothing here is resolved by the autopilot.*

Type: guide · byline: editorial (signed Георги Тодоров) · gate: PASS 95/100 · humanisation: HUMAN-LIKE 50/60 · Gemini Step-7: **ai 80** (hl 20, kept pass 1 after MAX_GEMINI_PASSES=2; high-variance reads 15/20/15) · run date: 08.09.2026

## SURVIVING IN-TEXT FLAGS: 2 (both [VERIFY], intentionally left in text — not resolved by the pipeline)
1. Section „Изплащанията" — [VERIFY: диапазонът 60%–95% за pick-6 е илюстративен ориентир от game-education източник и зависи от конкретната таблица]
2. Section „Реалните шансове" — [VERIFY: тези стойности са приблизителни (1 на 4 / 17 / 73), точната зависи от броя избрани числа и от таблицата]
No [DATA NEEDED], no [CONFLICT]. No operator/НАП/tax claim in the article, so no operator [VERIFY].

## TIME-SENSITIVE / CLAIMS-TO-CONFIRM (odds & house-edge figures + sources)
| Claim in text | Stated as | Source to confirm against | Status |
|---|---|---|---|
| Rules: избираш от 1–80, казиното тегли 20, съвпадение = улучване/catch | fact (universal, stable) | Wikipedia — Keno; Wizard of Odds — Keno | Verified, stable game-math |
| Онлайн кено house edge под 4% до над 35% | range | https://en.wikipedia.org/wiki/Keno ("less than 4 percent to over 35 percent") | Verified as range |
| Наземно/живо кено връщане 50%–80% → предимство 20%–40% | range | https://wizardofodds.com/games/keno/ (Vegas survey 65–80%, i.e. edge 20–35%); Wikipedia (in-person 20–40%) | Verified as range |
| Видео кено връщане 84%–95% (≈ на ротативките) | range | https://wizardofodds.com/games/keno/ (San Diego video keno 84–95%; "about as bad as slot machines") | Verified as range |
| Ротативки бенчмарк ~96% RTP; игри на маса под 5% edge | comparison benchmark | Wikipedia (non-slot games <5%); general game-math (~96% slot benchmark) | Verified as typical benchmark |
| Улучиш всичките 10 при pick-10 ≈ 1 на 8,9 милиона | approximate combinatorial fact | Techopedia keno odds; Wizard of Odds keno calculator; recompute C(20,10)/C(80,10) | Recalculated below ✓ |
| Solid 20 (всичките 20) ≈ 1 на 3,5 квинтилиона | approximate scale | https://en.wikipedia.org/wiki/Keno (1 in 3,535,316,142,212,173,800) | Verified; exact C(80,20)=3,535,316,142,212,174,320 (source rounds the tail) |
| Всяко число 1 на 80 на кръг; 20 от 80 = ¼ на теглене | fact | Wizard of Odds — Keno ("every ball has a 1 in 80 chance") | Verified |
| 1 на 4 / 1 на 17 / 1 на 73 (дребни улучвания) | APPROXIMATE, [VERIFY] | Techopedia / general keno tables | Flagged approximate — depends on pick size + paytable |
| pick-6 връщане 60%–95% по таблица | ILLUSTRATIVE, [VERIFY] | game-education (RTP swings by paytable) | Flagged illustrative |

SOURCES (all game-education, NOT operator T&C):
- Wizard of Odds — Keno: https://wizardofodds.com/games/keno/
- Wikipedia — Keno: https://en.wikipedia.org/wiki/Keno
- Techopedia — Keno Odds Explained: https://www.techopedia.com/definition/keno-odds-probability

## ILLUSTRATIVE (HYPOTHETICAL) NUMBERS — clearly generic, not operator data
| Figure | Where | Nature |
|---|---|---|
| pick-8 за €1, „улучиш поне пет" за печалба | S „Как се играе" | illustrative example, generic |
| два автомата, множител 1 000 vs 2 000 за pick-6 шесторка | S „Изплащанията" | illustrative contrast, generic |
| „на всеки €100 … €96 обратно" (96% RTP слот) | S „Домашно предимство" | illustrative long-run, generic |
| „кено с тежка таблица може да върне 70, 60 или по-малко" от €100 | S „Домашно предимство" | illustrative, tied to the cited edge ranges |
| pick-6 връщане 60%–95% | S „Изплащанията" | illustrative range, [VERIFY]-flagged |

## RECALCULATION SHOWN (one, per spec)
Catch all 10 in a pick-10 game = C(20,10) / C(80,10)
 C(20,10) = 184,756
 C(80,10) = 1,646,492,110,120
 184,756 / 1,646,492,110,120 = 1 / 8,911,711.18…
 → „около 1 на 8,9 милиона" ✓ (text figure matches the standard combinatorial value).
Cross-check, house edge from RTP: video keno 84% return → edge = 100% − 84% = 16%; 95% return → edge = 5%. Text „наравно с ротативките" (edge ~5%–16%) internally consistent. ✓

## COMPLIANCE SPOT-CHECK
- Em-dashes (—): 0 in the full 05b file (title, meta, H1, body, all three footer blocks). En-dashes (–) appear only in numeric ranges (60%–95%, 84%–95%) and the „10:00–17:00" hotline line, which are not em-dashes and are permitted (the hotline line is a verbatim untouchable block).
- Banned promise/hype words: none. Banned AI connectives (освен това / в допълнение / в заключение / заслужава да се отбележи / важно е да се отбележи / в днешно време): none.
- Brand exactly „Всички Казина": yes. Byline „Георги Тодоров": yes. Currency €, dates 08.09.2026 (DD.MM.YYYY): yes. Regulator НАП, jurisdiction България named in footers: yes.
- 18+ line „18+ Хазартът може да пристрасти. Играйте отговорно." present inline in body AND in the RG footer: yes. RG signposting to /otgovorna-igra/ + национален регистър на уязвимите лица (НАП): yes.
- Internal links: 3 distinct from approved set in body (/kazino-igri/, /kak-ocenyavame/, /otgovorna-igra/); the footer repeats /otgovorna-igra/ as mandated RG signposting. No non-approved URL, no invented link, no affiliate/operator link (guide, none required).
- Verbatim untouchable blocks (byline+dates, About, RG footer, affiliate-licensing footer): present exactly.
- No site-licence-issued claim; affiliate footer states „подало заявление … очаква издаването му". No НАП licence № needed (no operator reviewed). No tax claim made.

## ANTI-CANNIBALIZATION NOTE
No кено page exists in the vsichkikazina.bg sitemap (confirmed: content-queue.md vk-0016 „no keno page in sitemap"; research-topics.md „чист pillar — няма кено страница"). This is a clean pillar guide. It links out to the games hub /kazino-igri/ and does not compete with or duplicate an existing page. Secondary keyword variants („кено правила", „кено изплащания") are covered by close variants, not exact-match doorways, so no internal competition with future table-games pages.

## EXTERNAL CHECK (Step 7 — Gemini cross-model)
Model gemini-3.1-pro-preview. Three reads (07-gemini-check-1/-2/-3.md persist as the audit trail):
- initial 05b → "Likely AI-written, 85%" → hl 15
- Humaniser pass 1 (fixed the „casino floor" calque → native BG, removed signposting lead-ins, de-dramatized wrap-ups, broke the seesaw conclusion) → "Shows AI patterns, 80%" → **hl 20 (highest) → KEPT**
- Humaniser pass 2 (broke rule-of-three + „и двата" repetition, fixed meta anglicism/„За перспектива"/fluff transition) → "Shows AI patterns, 85%" → hl 15

MAX_GEMINI_PASSES=2 reached; kept the highest-hl version (pass 1) — pass 2 scored lower (noise band), so 05b was reverted to pass 1. Ends below 80 → gemini column `ai 80`. Gemini's score is low and high-variance here (15/20/15) while the internal Brand Gate passed it 95/100 (zero criticals) and the Humaniser rated it 50/60. Gemini's request to remove the site RG doctrine „Хазартът не е финансова стратегия" was REJECTED (untouchable); both [VERIFY] flags kept (Gemini agreed). All numbers, links, RG lines, 18+, disclosures, dates, byline and brand preserved across every pass; nothing here resolved a flag.

## HUMAN-ACTION LIST (before publish)
1. Resolve or replace the two [VERIFY] figures: (a) the pick-6 60%–95% illustrative return range, (b) the small-catch odds 1 на 4 / 17 / 73 — both depend on the exact paytable; keep as approximate or cite a specific verified table. Sources above. Edit 05b in place, then delete the flags.
2. Fill the `[About Всички Казина boilerplate]` placeholder slot at publish (Step 8) with the canonical block.
3. Confirm final published/updated dates (currently 08.09.2026) at publish time.
4. Guide needs no affiliate link and no НАП licence № — confirm none is expected to be added.
5. Do NOT publish 05b as-is: two [VERIFY] flags are still in the text by design.

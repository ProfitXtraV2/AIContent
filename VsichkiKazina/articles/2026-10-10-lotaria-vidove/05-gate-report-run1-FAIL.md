# 05 — Brand Gate report · Всички Казина · vk-0273

Input: 04-seo.md (title/meta + article; "## SEO audit" section ignored for scoring). Fact-tracing against 00-brief.md only.
Content type: guide (lottery-cluster hub). Byline: editorial voice, published signature Георги Тодоров.
Gate date: 10.10.2026.

```
BRAND COMPLIANCE SCORECARD — Лотария: какво е по закона и какви видове лотарии има в България
Verdict: FAIL (publish blocked, route as below)
Total: 79/100  (projected ≈92/100 after the listed fixes + human resolution of flags)
Personality 17/20 | Tone 13/15 | E-E-A-T 15/20 | Trust signals 8/15 | Language&Style 12/15 | RG 14/15
```

## Why FAIL and not PASS WITH FIXES

The gate's verdict rule makes three things FAIL rather than fixable: a surviving Version A/B dilemma, unresolved [DATA NEEDED], and unresolved [VERIFY]. This article has all three. The gate may not rewrite or remove any of these flags (they stay verbatim for the human), so it cannot clear them mechanically. Everything else wrong with the piece is mechanical and is listed below as ready-to-apply fixes. No fixed article is attached, as the FAIL protocol requires.

**Blamed stage: Step 4 (SEO).** Its own audit says it added both [DATA NEEDED] flags, and both go against the brief, which had already said how to handle each topic. The [CONFLICT] flag came in before Step 4 (Step 4's audit says it left "1× [CONFLICT]" unchanged), which puts it in Steps 1–3. That is a second upstream defect: the brief told the writer to use [VERIFY] for кено, not a two-version conflict.

## Maths recalculation (all correct)

| Claim | Recalculation | Result |
|---|---|---|
| C(49,6) = 13 983 816 | 49!/(6!·43!) = 13 983 816 | ✔ correct |
| C(42,6) = 5 245 786 | 42!/(6!·36!) = 5 245 786 | ✔ correct |
| C(35,5) = 324 632; 35·34·33·32·31 = 38 955 840; /120 | 1190·33 = 39 270; ·32 = 1 256 640; ·31 = 38 955 840; /120 = 324 632 | ✔ correct |
| „Шестица в 6 от 49 излиза над 40 пъти по-рядко от петица в едно теглене на 5 от 35" | 13 983 816 / 324 632 = 43.08 | ✔ correct („над 40" holds; "в едно теглене" correctly restricts the base) |
| „10 комбинации = 10 шанса от 13 983 816, на десетократна цена" | 10/13 983 816, linear cost | ✔ correct |
| €100 000 тото постъпления → поне €50 000 печалби (also бинго) | 50% × €100 000 = €50 000; base = постъпления (чл. 56, чл. 57) | ✔ correct; base stated; traditional/моментна base correctly distinguished (стойност на всички билети/талони, чл. 51/59) |
| Нетен доход €1 200 × 5% (НАП) = до €60 | 1 200 × 0.05 = 60 | ✔ correct |

No maths fix needed.

## CRITICAL (blocks publish)

1. **[CONFLICT] in the comparison table (Числова row, "Кой организира" cell):** „кено: [CONFLICT: § 9 ПЗР (ДВ бр. 14/2020) изключва кено от прекратяването на частните лицензи, а действащият чл. 4, ал. 3 (ред. 2021) не го изброява сред изключенията]". This is a surviving Version A/B dilemma, which the gate cannot fix itself. **Route to human (Step 6).** The brief's prescribed handling: "Whether any private кено licence issued before 2020 is still active today → [VERIFY]. Do not claim private кено is available now." Suggested resolution once checked against the НАП registers: cell = „кено: по действащия чл. 4, ал. 3 само държавата (БСТ); действащ частен лиценз отпреди 2020 г. не е потвърден". The body already handles this correctly in the paragraph „Действащ частен лиценз за кено след 2020 г. не успяхме да потвърдим [VERIFY…]" and in the checklist („кеното остава неизяснен случай").
2. **[DATA NEEDED: цена на една комбинация в 6 от 49, 6 от 42 и 5 от 35 и как се натрупва джакпотът]** (section „Какви лотарии има в България"). This blocks publish and goes against the brief: "Prize tiers, ticket prices, BST payout percentages → NOT sourced → do not state them." Required fix (Step 4 re-run): delete the flag. The hub does not need prices; the sibling guides will cover them.
3. **[DATA NEEDED: данъчно третиране на печалбите от лотария по ЗДДФЛ]** (section „Онлайн лотария…"). This blocks publish and goes against both the brief ("Do NOT duplicate tax content → link /blog/danaci-pechalbi-onlajn-kazino/") and the brand's tax rule (always [VERIFY] plus a pointer to счетоводител/НАП, never settled fact or figures). Required fix (Step 4 re-run), replacing the flag: „Дали и как се облагат печалбите от лотария, проверете при счетоводител или в НАП [VERIFY: данъчно третиране на печалбите от лотария]; общата рамка е в [статията за данъците върху печалбите](/blog/danaci-pechalbi-onlajn-kazino/)." That would make 5 internal links, above the maximum of 4, so drop the optional /blog/proverka-licenz-kazino/ link. Keep its sentence as plain text: „…а списъците се проверяват на сайта на НАП."
4. **Missing publication and last-updated dates** (Pillar 4). Mechanical fix, put under the H1: `Георги Тодоров · Публикувано: 10.10.2026 · Последна актуализация: 10.10.2026 · Правната информация е проверена към 10.10.2026 (Закон за хазарта, консолидиран текст до ДВ бр. 69/31.07.2026).` Replace the publish date with the real one at publication.
5. **Byline only appears as a closing signature** (*Георги Тодоров*). There is no byline slot at the top and no **author bio slot** (Pillar 4). Mechanical fix: the byline line above, plus an author-bio slot `[AUTHOR BIO: Георги Тодоров]` before the footer. Keep the closing signature.
6. **Missing "About Всички Казина" boilerplate slot** (Pillar 4). Mechanical fix: `[ABOUT: Всички Казина boilerplate]` in the footer.
7. **Missing affiliate-licensing footer, verbatim** (brand untouchable, required by the orchestrator). Mechanical fix, footer:
   > Тази статия не съдържа партньорски връзки.
   > От 1 август 2026 г. дейността на афилиейт оператори в България се лицензира съгласно Закона за държавния бюджет за 2026 г. (ДВ, бр. 69 от 31.07.2026 г.). Всички Казина е подало заявление за лиценз пред Националната агенция по приходите и очаква издаването му.
8. **RG footer block missing as a block.** The verbatim line, /otgovorna-igra/ and the регистър are currently only in the body paragraph. Keep them there unchanged and add the footer block:
   > 18+ Хазартът може да пристрасти. Играйте отговорно. Ако играта спре да е забавление: [отговорна игра](/otgovorna-igra/) · национален регистър на уязвимите лица в НАП (чл. 10г ЗХ, 0700 18 700) · Национална информационна линия за наркотиците, алкохола и хазарта („Солидарност") 0888 99 18 66, делнични дни 10:00–17:00.

## MODERATE

1. **Em-dashes:** there are none in the body text. Two sit inside flags: „[VERIFY: действащ частен лиценз за кено след 2020 г. — регистрите на НАП]" and „[VERIFY: дата — единствен източник bg.wikipedia]". These are left verbatim as the rule requires, but the human must make sure no em-dash survives when the flags are resolved (zero em-dashes at publish).
2. **Excessive 3-item bullet list** (чл. 54 payout mechanics) should be prose. Fix, preserving every figure and article: „Чл. 54 изброява четири разновидности и всяка плаща по свой начин. При тотото печалбите за всеки тираж са предварително определен процент от постъпленията, не по-малко от 50% (чл. 55, ал. 2 и чл. 56). При лотото и кеното печалбата се смята по предварително зададен коефициент и зависи от залога, без връзка с общите постъпления (чл. 55, ал. 3). Бингото се играе с талони с готови комбинации: поне 50% от постъпленията отиват за печалби и те се изплащат веднага след обявяването им (чл. 57)." Keep the 6-item ТОТО 2 list and the 5-step checklist: one is a 6+ enumeration, the other a genuine checklist.
3. **Checklist section heading and lead-in.** „Пет проверки преди да купите билет" followed by „Пет въпроса преди да платите за билет, фиш или талон:" restates the heading (a signposting tell). Both lines also assume a purchase, and the brief says "NO encouragement to buy tickets". Fix: delete the lead-in sentence. Suggested H2: „Пет проверки за законна лотария". The SEO stage owns the heading choice; the rename keeps it a real reader statement.
4. **Sibling guides that are not live.** „Всяка от основните игри има собствено подробно ръководство на сайта." and „Историята на Национална лотария … е тема на отделно ръководство." are present-tense claims about pages that do not exist yet (vk-0266..0271). The brief asked for the mention, so keep them, but the editor must not publish the hub before the siblings, or must change the tense to future. No links added, which is correct.
5. **RG budget framing.** The NAP 5% figure is there, but the brand's "money you can afford to lose entirely" framing is missing. Fix, appended to the budget paragraph: „Това са пари за забавление, които трябва да можете да загубите изцяло."
6. **Blog hub link /blog/regulations-taxes/ is absent.** The article is at the 4-link maximum, so this is a note only, not a fix.

## VERIFY QUEUE (route to human, Step 6)

- [CONFLICT] кено organiser (table): resolve against the НАП registers (see CRITICAL 1).
- [VERIFY: действащ частен лиценз за кено след 2020 г. — регистрите на НАП]
- [VERIFY: дата — единствен източник bg.wikipedia] (БСТ since 12.05.1957)
- [VERIFY: дали сумата вече е преизчислена в € в консолидирания текст] (глоба 500–2000 лв.; the brand currency is €, so convert only if the law text does)
- [DATA NEEDED] ×2: to be removed or replaced by the Step 4 re-run (CRITICAL 2–3), not filled with guessed data.
- Publication date at publish time.

## Fact trace (brief vs article): clean

Every legal claim traces to brief §A/§B: чл. 3, 4/3, 9/9–11, 9/14, 10г, 13а, 15, 17/6, 41/1–2, 49–59, 97а/2, § 9 ПЗР 2020, 08.08.2020, 01.08.2026 24-hour blocking, 12.12.2022 регистър, 12-month minimum, nap@nra.bg + КЕП, 0700 18 700, illegal_gambling@nra.bg, 5% budget. Every БСТ practice claim traces to §C: two draws a week, the ТОТО 2 games, БНТ Thu/Sun 18:45, Facebook after 19:00, the scratch titles, ePay.bg/БОРИКА, automatic credit of winnings, site down 18:40–19:10, ПМС № 50/15.02.2021. The odds trace to §D. Brief bans respected: no affiliate links, no operator other than БСТ, no number picks, no prices or jackpots, no Софийски районен съд/БИМ, no anecdote (opt-in: no). Jurisdiction (България/НАП) is named on every legal claim. No banned promise, hype or AI-connective words; no FOMO. The tax claim is not asserted. No site-licence claim.

## VOICE NOTES (protect during fixes)

- The dry, exact consumer-protection register: „Минимумът се отнася до целия фонд. На отделния купувач законът не гарантира никаква част от него." Keep.
- The asymmetric ending: „…Ако го купувате като план за пари, сметката не излиза никога." It is the site doctrine in the piece's own voice and also its natural RG touch. Keep verbatim.
- „Тото на хартиен фиш и тото в браузъра са една и съща игра пред закона." and „Продавач, който не пита, е повод за съмнение." are good plain-language translations of the law. Keep.

## Route

1. Step 6 human resolves the [CONFLICT] and the three [VERIFY] flags (CRITICAL 1).
2. Step 4 (SEO) re-runs with only these changes: remove the price [DATA NEEDED]; replace the tax [DATA NEEDED] with the brief-compliant link + [VERIFY] pointer; swap out the /blog/proverka-licenz-kazino/ link (CRITICAL 2–3).
3. Step 5 re-runs and applies the mechanical fixes above (CRITICAL 4–8, MODERATE 2, 3, 5). Expected verdict: PASS (≈92/100).

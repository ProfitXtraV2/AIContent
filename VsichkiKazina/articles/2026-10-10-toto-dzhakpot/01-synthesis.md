# 01-SYNTHESIS — vk-0275 „тото джакпот" (BRAND: vsichkikazina)

Stage 1 (Synthesis), fresh context, 2026-10-10. Inputs read: pipeline/SKILL.md (brand rules),
pipeline/agents/synthesis.md, pipeline/prompts/step-1-synthesis.md, 00-brief.md,
source-packs/bst-toto-2026-10-10.md, source-packs/nap-gambling-law-and-rg-2026-10-10.md.
No web search / fetch performed. All facts come from the brief and the two source packs.

---

## SYNTHESIS REPORT

Query: тото джакпот | Intent: informational (with a navigational „how big is it now" component) | Market: bg, Bulgarian, € (euro since 01.01.2026)
Sources: 12 referenced in the brief (2 human-verified source packs + 10 fetched/secondary URLs summarised in the brief) | Corroborated facts used: 9 | [VERIFY] flags in draft: 10 | [CONFLICT] flags in draft: 2 | [DATA NEEDED]: 0 in draft (1 noted below as deliberately omitted)

### Fact inventory (short)

CORROBORATED (2+ sources or primary pack, used without flag):
- Current jackpots к тираж 79 (08.10.2026): 6/49 5 060 115,42 €; 6/42 1 363 850,28 € (toto.bg pack, human-verified; time-sensitive but date-stamped, so stated with the date).
- Two draws a week (нечетен/четен), live on БНТ Thursday and Sunday from 18:45 ч.; results released for payout within one hour after the broadcast (pack).
- Online winnings for ТОТО 2 credited automatically to the online account (pack).
- Rollover mechanism: unwon jackpot carries into the next draw (novinite 2010 + action.toto.bg 2026).
- Equal split between multiple jackpot winners (action.toto.bg, 2019 case).
- Record list 2019–2025 (action.toto.bg R1); 11 715 401,70 лв. corroborated by profit.bg (Сливен, фиш 1,20 лв.).
- 45-day payout period (paragraf.bg 2026 + novinite 2011 + totogener).
- Instalment payout of large jackpots exists (totogener + fakti.bg comment + old rules mirror + paragraf.bg 2026 „разсрочените джакпоти"). Existence corroborated; exact current figures are NOT → [VERIFY].
- Odds: C(49,6) = 13 983 816; C(42,6) = 5 245 786 (pure combinatorics, rechecked with python3 at this stage).
- НАП RG guidance: budget ≤5% of net income, register under чл. 10г ЗХ, minimum 12 months, 0700 18 700 (НАП pack).
- Lottery/тото = „лотарийни игри" under ЗХ (НАП pack).

SINGLE-SOURCE / TIME-SENSITIVE (used with [VERIFY]):
- Payout thresholds 1 000 лв. / 1 000,01–9 999,99 лв. / ≥10 000 лв. (paragraf.bg, totogener, BST press title) — in лева; € values post-euro unknown.
- 200 000 лв. initial sum + up to 14 years of monthly instalments for prizes over 1 000 000 лв. (totogener + reader comment; low trust).
- 6-month claim lapse (totogener only).
- Prize fund „не по-малко от 50%" of stakes (old undated mirror, low trust) → NOT used in draft at all; rollover explained without a percentage.
- Unclaimed 6,6 млн. лв. jackpot of 2010 (novinite 2011, „reportedly").
- Whether online-credited payout applies to an instalment jackpot (unknown).
- ЗДДФЛ чл. 13, ал. 1, т. 20 current wording (lex.bg not fetched).
- Ranking of the current 6/49 jackpot among historical wins (R1 list predates 2026 draws).
- Our own € conversions of historical лв. amounts at 1,95583 are calculations, labelled „≈" in text (not flagged as facts).

### Conflicts

1. [CONFLICT: dir.bg 19.03.2026 calls the 5 778 403 € win (тираж 21/2026) „вторият най-голям джакпот в историята"; at the fixed rate 5 778 403 € ≈ 11 301 574 лв., which is slightly BELOW the 2025 win of 11 304 948,90 лв. listed by action.toto.bg (R1), so it would rank third.] Draft states both amounts in the table, gives no rank for the 2026 win, and carries the flag. No two-camp debate in the text.
2. [CONFLICT: totogener.com (09.10.2025) claims a „10% окончателен данък" withheld on wins over 10 000 лв., while the same page says the winnings „не се облагат", and НАП opinions on чл. 13, ал. 1, т. 20 ЗДДФЛ list gambling winnings as non-taxable income.] Draft states the ЗДДФЛ position with [VERIFY] and keeps the conflicting claim in the flag only.

### Source claims excluded as dubious
- dir.bg millionaire counts (151-ви vs „142 души от 1957 г.") — internally inconsistent; not cited.
- dir.bg „second biggest ever" ranking — mathematically doubtful (see Conflict 1); not repeated as a rank.
- totogener 10% withholding tax — unsourced and self-contradicting; excluded from text (flag only).
- Old rules mirror (toto2-info.w-bg.net) „≥50% prize fund" and its worked instalment example — undated, partly garbled; not used.
- profit.bg URL date (2024) as the draw year — R1 gives 31-ви тираж на 2022 г.; R1's year used.
- March 2026 temporary suspension of payouts over 5 000 € (paragraf.bg) — kept to ONE neutral sentence per brief, framed as temporary.
- Any cap / forced roll-down rule for 6/49 — no source; deliberately NOT mentioned (would be [DATA NEEDED] if the team wants it).
- 5/35 jackpot amount — pack shows none; no jackpot claimed for 5/35. Zodiac/Джокер/Рожден ден odds not given (owned by siblings).

### Entity union coverage
Complete for jackpot scope: БСТ / „Спорт Тото", ТОТО 2 (6/49, 6/42, 5/35, Зодиак, Рожден ден, Тото Джокер — the last four one sentence max), тираж 79, БНТ, rollover / натрупване, I категория, разделен джакпот, Централно управление (София), искова форма за банково изплащане, 45 дни, разсрочено изплащане, квитанция/фиш, онлайн сметка, ЗДДФЛ чл. 13, ал. 1, т. 20, Закон за хазарта, НАП, регистър по чл. 10г, евро/лев 1,95583, records 1991/2010/2017/2019/2021/2022/2023/2024/2025/2026.

### Gaps closed that no source covered
- One evergreen explainer joining rollover + payout path + tax + verified records in one place (SERP = live-amount pages and news).
- Why a bigger jackpot raises the chance of SHARING it but not of winning it (worked framing).
- C(n,k) working shown, plus the „134 460 години" average-wait illustration and the 10-combination case.
- Leva-to-euro handling of historical records, clearly labelled as our conversion.
- Explicit RG angle: jackpot size is not a reason to buy more combinations; cost scales linearly, odds stay negligible.

### Localisation adjustments
- All current figures in €; historical records in лв. with „≈ €" conversions at 1,95583 (labelled ours).
- Payout thresholds kept in лв. as reported, with [VERIFY] for current € thresholds.
- Regulator НАП; RG resources from the НАП pack only. 18+.
- Bulgarian number formatting (space thousands separator, decimal comma).
- No predictions, number picks, „hot numbers", or winner-story glamour (brand + brief rules).

### Anti-cannibalisation check
- No prize-tier tables, no per-tier odds, no EV maths (vk-0267). Only jackpot odds for 6/49 and 6/42 with working.
- Systems/combinations (vk-0270): only the „10 комбинации" probability line, no system prices.
- „Горещи" числа (vk-0272): one sentence on gambler's fallacy, no statistics deep dive.
- Джокер / Зодиак / Рожден ден: amounts in the table only, plus one sentence that their rules are separate.
- Slot progressives: one link to /blog/progresivni-dzhakpoti/ as contrast, not re-explained.

### Internal links used (4 — max allowed by brief)
/blog/progresivni-dzhakpoti/ · /blog/danaci-pechalbi-onlajn-kazino/ · /zakonno-li-e/ · /otgovorna-igra/
(Hub link /blog/regulations-taxes/ omitted to stay at 4; SEO stage may swap /zakonno-li-e/ for the hub if preferred. No /toto…/ URLs linked.)

### Note for the human verifier
The official BST pages (CAPTCHA) should settle most [VERIFY] flags in one pass:
https://info.toto.bg/news/press/kakvo-tryabva-da-znayat-uchastnitsite-za-izplashtaneto-na-pechalbi-ot-igrite-na-balgarski-sporten-totalizator and https://info.toto.bg/chesto-zadavani-vaprosi ; tax wording on lex.bg (ЗДДФЛ чл. 13, ал. 1, т. 20).

---

## THE ARTICLE (original draft, Bulgarian)

# Джакпотът в Тото: как се натрупва, кога се изплаща и кои са рекордите

Към тираж 79 от 08.10.2026 г. джакпотът в ТОТО 2 – 6 от 49 е **5 060 115,42 €**. За да го спечелите с една комбинация, трябва да познаете 6 числа от 49, а шансът за това е 1 към 13 983 816. Двете числа заедно обясняват почти всичко за тото джакпота: сумата расте, защото почти никой не я печели, а големината ѝ не прави печалбата по-вероятна.

По-долу ще намерите как се натрупва джакпотът, колко е в момента във всяка игра, кои са най-големите джакпоти в историята на Български спортен тотализатор, какво се случва след печалба и дали се плаща данък.

## Как се натрупва джакпотът

Джакпотът е наградата от първа категория: шест познати числа в 6 от 49 или в 6 от 42. Когато в даден тираж никой не уцели и шестте, тази сума не се изплаща. Тя се прехвърля към следващия тираж и към нея се добавя дял от залозите в него. Тиражите са два седмично, така че след няколко седмици без печеливш фиш сумата лесно минава от стотици хиляди към милиони евро.

Точният процент от залозите, който отива в наградния фонд и в първа категория, се определя от правилата на БСТ. [VERIFY: актуални правила на БСТ за 6/49 и 6/42 — % награден фонд и дял на I категория] Затова тук не даваме конкретна цифра.

Ако джакпотът бъде спечелен от повече от един участник, той се разделя поравно. Това е реалният ефект от „големия" джакпот: когато сумата е рекордна, се пускат повече фишове и расте вероятността печелившата комбинация да се окаже у двама или трима души. Вашият шанс с една комбинация остава 1 към 13 983 816, каквато и да е сумата на таблото. През 2019 г. джакпот от 9 501 430,40 лв. беше разделен точно така, между четирима играчи.

Механиката прилича на натрупващите се джакпоти при слот игрите само на повърхността. Как работят [прогресивните джакпоти при слотовете](/blog/progresivni-dzhakpoti/) е отделна тема, защото там фондът се захранва от завъртания, а не от тиражи.

## Колко е джакпотът сега

Сумите се променят след всеки тираж. Данните са от таблото с резултати на toto.bg за тираж 79 от 08.10.2026 г.

| Игра (ТОТО 2) | Джакпот към тираж 79 (08.10.2026) |
|---|---|
| 6 от 49 | 5 060 115,42 € |
| 6 от 42 | 1 363 850,28 € |
| Зодиак | 1 500 000,00 € |
| Рожден ден | 7 353,06 € |
| Тото Джокер | спечелен в тираж 79 |

Зодиак, Рожден ден и Тото Джокер имат собствени правила и не са тема на тази статия. 5 от 35 се тегли два пъти във всеки тираж, но таблото не показва джакпот за тази игра.

Тегленията на 6 от 49, 6 от 42, 5 от 35, Зодиак и Тото Джокер вървят на живо по БНТ в четвъртък и неделя от 18:45 ч. До един час след края на предаването резултатите са обработени и тиражът е пуснат за изплащане.

## Рекордните джакпоти в 6 от 49

До края на 2025 г. сумите се изплащаха в лева. По-долу историческите джакпоти са в лева, както са съобщени, а сумите в евро са наше преизчисление по фиксирания курс 1,95583 и са закръглени.

| Тираж | Джакпот | ≈ в евро (наше преизчисление) | Печеливши |
|---|---|---|---|
| 31-ви тираж, 2022 г. | 11 715 401,70 лв. | ≈ 5 989 990 € | един фиш, пуснат в Сливен |
| тираж 23, 2025 г. | 11 304 948,90 лв. | ≈ 5 780 129 € | един участник |
| тираж 21, 2026 г. | 5 778 403 € (≈ 11 301 574 лв.) | 5 778 403 € | един фиш, пуснат в София [CONFLICT: dir.bg 19.03.2026 го нарича „вторият най-голям джакпот в историята"; при курс 1,95583 сумата е ≈ 11 301 574 лв., малко под 11 304 948,90 лв. от 2025 г. по списъка на action.toto.bg, т.е. би била трета] |
| тираж 39, 2024 г. | 10 095 908,40 лв. | ≈ 5 161 956 € | един играч |
| 76-и тираж, 2023 г. | 9 667 090,20 лв. | ≈ 4 942 705 € | един участник |
| 20-и тираж, 2019 г. | 9 501 430,40 лв. | ≈ 4 858 004 € | разделен между четирима |

Рекордът от 2022 г. е и най-голямата сума, спечелена от един човек в историята на играта, по данни на БСТ и profit.bg. Фишът е струвал 1,20 лв. Джакпотът от тираж 21 на 2026 г. е първият тото джакпот, изплатен в евро.

Ако се върнем по-назад, мащабът се вижда добре. Първият български тото милионер е от 07.04.1991 г., с печалба от 1 000 000 лв. През 2010 г. рекордът е бил около 6,6 млн. лв., а според публикации от 2011 г. тази печалба така и не е била потърсена в срок. [VERIFY: непотърсен джакпот от юни 2010 г., Ловеч] През 2017 г. рекордът е 7 940 616 лв., а през февруари 2021 г. в Пловдив пада джакпот от 8 431 125 лв.

Текущият джакпот от 5 060 115,42 € е около 9 896 726 лв. по фиксирания курс. Ако бъде спечелен в този размер, той ще е сред най-големите в историята на 6 от 49. [VERIFY: класиране на текущия джакпот — списъкът на action.toto.bg е от преди тиражите на 2026 г.]

## Какво става, ако спечелите джакпота

### Пътят на парите

Тук са важни праговете, които БСТ прилага при изплащането. По публикувани данни те са следните, все още в лева: до 1 000 лв. печалбата се получава в брой в пункта; от 1 000,01 до 9 999,99 лв. се изплаща по банков път след попълване на искова форма за банково изплащане; от 10 000 лв. нагоре печалбата се обработва от Централното управление на БСТ в София и също се превежда по банка. [VERIFY: актуални прагове за изплащане в евро след 01.01.2026 г.] Джакпотът винаги попада в последната група.

При хартиен фиш пазете квитанцията. Без нея не можете да предявите печалбата.

Печалбите от онлайн игра на ТОТО 2 се прехвърлят автоматично в сметката на играча. Дали същото важи и за джакпот, който се изплаща на вноски, не е ясно от достъпните източници. [VERIFY: изплащане на онлайн джакпот — автоматично по сметка или по общия ред]

### Срокове

БСТ изплаща печалбите от ТОТО 1 и ТОТО 2 в срок от 45 дни. По информация от вторичен източник правото да предявите печалба се губи след 6 месеца от тиража. [VERIFY: срок за предявяване на печалба — 6 месеца от тиража] Случаят от 2010 г. показва, че пропуснатият срок не е теоретичен риск.

### Наведнъж или на вноски

Голям джакпот не се изплаща наведнъж. Печелившият получава първоначална еднократна сума, а остатъкът идва на равни месечни вноски. Според публикувани описания на правилата първоначалната сума е до 200 000 лв., а разсрочването е за период до 14 години при печалби над 1 000 000 лв. [VERIFY: правила на БСТ — размер на първоначалната сума и срок на разсрочване, в евро] Практическият извод е прост: джакпот от 5 млн. € не означава 5 млн. € по сметката на следващия ден, а много години редовни плащания.

През март 2026 г. изплащането на печалби над 5 000 € беше временно спряно при смяна на ръководството на БСТ.

## Облага ли се печалбата от Тото

Тото е лотарийна игра по смисъла на Закона за хазарта. Според Закона за данъците върху доходите на физическите лица (чл. 13, ал. 1, т. 20) паричните и предметните печалби от хазартни игри са необлагаем доход, а НАП посочва в свои становища, че за тях не е нужно деклариране. Това означава, че печелившият не дължи данък върху джакпота. [VERIFY: актуална редакция на чл. 13, ал. 1, т. 20 ЗДДФЛ] [CONFLICT: totogener.com (09.10.2025) твърди, че се удържа „10% окончателен данък" върху печалби над 10 000 лв., без източник и в противоречие със собственото си твърдение в същия текст, че печалбите „не се облагат"; НАП становищата по чл. 13, ал. 1, т. 20 ЗДДФЛ ги определят като необлагаеми]

Как изобщо се облагат печалбите от хазарт у нас и защо тежестта пада върху организатора, обясняваме подробно в статията за [данъците върху печалбите](/blog/danaci-pechalbi-onlajn-kazino/).

## Какъв е реалният шанс

Шансът за джакпот е чиста комбинаторика. За 6 от 49 броят на възможните комбинации е:

C(49,6) = 49 × 48 × 47 × 46 × 45 × 44 / 6! = 10 068 347 520 / 720 = **13 983 816**

За 6 от 42:

C(42,6) = 42 × 41 × 40 × 39 × 38 × 37 / 6! = 3 776 965 920 / 720 = **5 245 786**

Една комбинация дава шанс 1 към 13 983 816 в 6 от 49 и 1 към 5 245 786 в 6 от 42.

Числата са трудни за представяне, затова ето една илюстрация. Да приемем, че играете една комбинация на всеки тираж, около 104 тиража годишно. Средното очаквано чакане за джакпот в 6 от 49 е около 134 460 години. В 6 от 42 е около 50 440 години. Това е средна стойност, не прогноза, но показва мащаба.

Десет комбинации в един тираж вдигат шанса до около 1 към 1 398 382. Цената се увеличава десетократно, а шансът остава нищожен.

## Защо по-големият джакпот не е по-добър повод да играете

Рекламата на рекорден джакпот действа по един и същ начин: сумата изглежда толкова голяма, че си струва да се пуснат още няколко комбинации. Математиката не се променя. Всяка допълнителна комбинация струва толкова, колкото и предишната, а шансът ви се движи от „почти никакъв" към „почти никакъв". Единственото, което расте заедно със сумата, е вероятността при печалба да делите джакпота с други.

Също толкова подвеждащо е усещането, че „джакпотът отдавна не е падал, значи скоро ще падне". Тегленията са независими. Топките не помнят предишните тиражи.

Ако играете, правете го като забавление с фиксиран бюджет, определен предварително. НАП препоръчва бюджетът за хазарт да не надвишава 5% от нетните ви доходи, а и тук важат същите правила като при всяка друга хазартна игра: не гонете загуби и не играйте с пари за сметки и наем. Платени „системи" и съвети, които обещават джакпота, продават увереност, която математиката не позволява. Ако усещате, че губите контрол, можете да поискате вписване в регистъра на НАП по чл. 10г от Закона за хазарта за срок не по-кратък от 12 месеца. Информационният център на НАП е на 0700 18 700. Повече практически насоки има на страницата ни за [отговорна игра](/otgovorna-igra/), а какво казва законът за легалната игра у нас, обясняваме в [Законно ли е](/zakonno-li-e/). Участието в хазартни игри е забранено за лица под 18 години.

## Често задавани въпроси

### Колко е джакпотът в Тото 6 от 49 сега?
Към тираж 79 от 08.10.2026 г. той е 5 060 115,42 €. Сумата се променя след всеки тираж, затова проверявайте актуалната стойност на toto.bg.

### Кой е най-големият джакпот в историята на Тото?
11 715 401,70 лв. (≈ 5 989 990 €) в 6 от 49, спечелен с един фиш, пуснат в Сливен, в 31-ви тираж на 2022 г.

### Изплаща ли се джакпотът наведнъж?
Не. Големите джакпоти се изплащат с първоначална сума и равни месечни вноски, а печалбата трябва да бъде изплатена в срок от 45 дни. [VERIFY: актуален размер на първоначалната сума и срок на разсрочване в евро]

### Плаща ли се данък върху печалба от Тото?
Според ЗДДФЛ печалбите от хазартни игри, включително тото, са необлагаем доход за играча. [VERIFY: актуална редакция на чл. 13, ал. 1, т. 20 ЗДДФЛ]

---

*Draft word count: ≈1 570 думи (body incl. tables and FAQ, flags excluded); ~70 over the 1 500 upper target, Outline/Author may trim the history paragraph.*

---

## SUGGESTED PERSONA / BYLINE

Persona for the author pass: **Editorial voice** (neutral, explanatory). Reasoning: this is an educational lottery guide with tax, payout and RG content and no product to review, so a persona-driven or opinionated register would add risk without value; the brief specifies editorial.
Published byline: **Георги Тодоров** (mandatory for brand vsichkikazina; never a team/editorial byline).
Brand-name mentions in draft: 0 explicit „Всички Казина" mentions (first-person plural „нашата статия/страница" only); the author/SEO stage may add 1–2 natural mentions, max 3.

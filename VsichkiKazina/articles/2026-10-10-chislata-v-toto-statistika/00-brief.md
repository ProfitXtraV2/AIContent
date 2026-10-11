# 00-BRIEF — Всички Казина

BRAND: vsichkikazina
MARKET: bg
QUEUE ID: vk-0272 (ad-hoc cloud run 2026-10-10, topic-backlog block 2026-10-10c)
CONTENT TYPE: guide
BYLINE: editorial (neutral explainer voice; PUBLISHED byline ALWAYS Георги Тодоров)
WORKING TITLE / H1: Числата в тото — статистика и митът за „горещите" числа
TARGET QUERY: числата от тотото
SECONDARY TERMS: числа за тото, числа за тото 5/35, статистика тото, най-често падащи числа тото — Ahrefs bg 2026-10-10 (head 1300/mo, KD 0; cluster ~2500). NeuronWriter: none provided.
LENGTH: guide — target ~1,200–1,600 думи

## INTENT NOTE
Searchers want either (a) the latest draw numbers (navigational → send them in ONE early line
to the official results on https://www.toto.bg/; we do NOT publish results), or (b) number
„statistics" / „hot numbers" hoping to pick better. Our angle = the HONEST randomness explainer:
every draw is independent; what a frequency table really shows; gambler's fallacy; why
„горещи/студени" and „просрочени" numbers do not change the odds; the ONE thing number choice
does affect — how many people share a prize (popular numbers). NEVER give picks, NEVER promise
a method, no „systems that beat the draw".

## ANTI-CANNIBALIZATION
- Distinct from the open lottery PRs (not live — DO NOT link them, mention at most in passing):
  vk-0267 Тото 2 games/rules/odds tables (do NOT repeat its full odds tables — one line with the
  jackpot odds is enough), vk-0270 системи/комбинации (one sentence max), vk-0275 джакпот
  (rollover mechanics — do not cover), vk-0269 Зодиак, vk-0266 Джокер, vk-0268 ВТШ.
- Distinct from vk-0169 „Психология на хазарта: gambler's fallacy…" (casino-wide psychology,
  not live): here gambler's fallacy is explained ONLY as applied to lottery numbers, in one
  section, not as a psychology pillar.
- No numbers/lottery-statistics page in the live sitemap (108 URLs checked 2026-10-10).

## KEY VERIFIED FACTS

### From source pack bst-toto-2026-10-10.md (toto.bg read in a BG browser on 2026-10-10)
- БСТ провежда два тиража седмично — нечетен и четен; тегленията на ТОТО 2 – 6/49, 5/35, 6/42
  се излъчват на живо по БНТ в четвъртък и неделя от 18:45 ч.
- 6/49: изтеглят се 6 печеливши числа. 6/42: 6 числа. 5/35: две тегления (I-во и II-ро) по
  5 числа в един тираж.
- Резултатите → официално на https://www.toto.bg/ (CAPTCHA за скриптове; не сме го извличали).

### Frequency table — lotteryextreme.com (unofficial aggregator), fetched 2026-10-10
URL: https://www.lotteryextreme.com/toto2/649-statistics — „Таблица за честота на номера",
ТОТО 2 6/49, период 2015-01-01 – 2026-10-08. Label as неофициален агрегатор → [VERIFY срещу
архива на БСТ] wherever its numbers are cited.
- Сборът от всички 49 честоти = 7 572 изтеглени числа → 7 572 / 6 = 1 262 тиража в периода.
- Най-често: 34 — 188 пъти; 23 и 37 — по 176; 42 — 173; 35 — 171.
- Най-рядко: 40 — 117 пъти; 41 — 129; 7 — 131; 25 — 132.
- „Просрочени": към 08.10.2026 числото 40 не е излизало 33 тиража (последно 18.06.2026).

### Statistics computed in python3 on 2026-10-10 (show working; these are OUR calculations)
- Шанс конкретно число да е сред изтеглените в 6/49: 6/49 ≈ 12,24% — във ВСЕКИ тираж,
  независимо от миналото.
- Очаквана честота за 1 262 тиража: 1 262 × 6/49 ≈ 154,5 пъти за всяко число; стандартно
  отклонение ≈ 11,6.
- Симулация (2 000 серии по 1 262 честни тиража 6/49): най-често падащото число обикновено
  излиза около 181 пъти (90% от сериите: 174–192); най-рядкото — около 129 пъти (90%: 120–135).
  → Разлика от 60–70 пъти между „най-горещото" и „най-студеното" число е нормална за чиста
  случайност. Наблюдаваното 188 е в обичайния диапазон; 117 е малко под него.
- Общ тест (хи-квадрат, p-стойност от симулация 3 000 серии): ≈ 0,06 → разпределението НЕ се
  отклонява статистически значимо (при обичайния праг 0,05) от равномерното. Phrase carefully:
  „не показва статистически значимо отклонение" — do not claim „перфектно равномерно".
- Шанс конкретно число да НЕ излезе 33 поредни тиража: (43/49)^33 ≈ 1,3%. При 49 числа е
  нормално поне едно да е „просрочено" толкова дълго. Следващият тираж: пак 12,24%.
- 5/35: шанс конкретно число да е сред 5-те в едно теглене = 5/35 = 1/7 ≈ 14,29%.
- Джакпот (само по един ред, без таблици — vk-0267 ги има): C(49,6) = 13 983 816;
  C(42,6) = 5 245 786; C(35,5) = 324 632. Комбинацията 1-2-3-4-5-6 има точно същия шанс
  1 към 13 983 816 като всяка друга.

### The 2009 repeat draw (real case; independence + prize splitting in one story)
Sources: BBC News „Bulgarian lottery repeat probed" (Sept 2009) and Reuters „Bulgaria's identical
lottery draw was coincidence" (17.09.2009) — mirrored at
https://sites.oxy.edu/lengyel/M150/lotteries/BBC%20NEWS%20Europe%20Bulgarian%20lottery%20repeat%20probed.html
and https://sites.oxy.edu/lengyel/M150/lotteries/Bulgaria's%20identical%20lottery%20draw%20was%20coincidence%20Reuters.htm
- На 6 и 10 септември 2009 г. в два поредни тиража на българската лотария бяха изтеглени
  едни и същи шест числа: 4, 15, 23, 24, 35, 42 (в различен ред), от машина, на живо по телевизията.
- В първия тираж (6.09) никой не позна шестицата; във втория (10.09) рекордните 18 души познаха
  всичките шест и всеки получи 10 164 лв. (≈ 5 197 € по фиксирания курс 1,95583 — наша
  сметка).
- Спортният министър Свилен Нейков разпореди проверка; комисията (председател Константин
  Симеонов) не откри нарушение: „не можем да говорим за манипулация"; организаторите го нарекоха
  „странно съвпадение". Математикът Михаил Константинов оцени шанса на повторението на
  „1 към над 4 милиона".
- Играта не е назована в статиите; числата (най-голямо 42) и „1 към над 4 милиона" съответстват
  на 6/42 (C(42,6) = 5 245 786) → write „вероятно в играта 6 от 42 [VERIFY]".
- Защо 18 печеливши: най-вероятно мнозина просто са повторили числата от предходния тираж →
  this is an INFERENCE, the sources don't say it → [VERIFY] or phrase as hypothesis.

### Popular numbers & prize sharing (principle; BG-specific rule unsourced)
- Lower-tier (and jackpot) prizes in ТОТО 2 are pari-mutuel: сумата за дадена категория се дели
  между всички печеливши комбинации (seen in the per-draw payout amounts that change every draw —
  lotteryextreme results pages); exact БСТ rule wording / prize-fund % NOT sourced → [VERIFY].
- The 2009 case shows it concretely: 18 shared winners → 10 164 лв. each.
- Common human patterns (general knowledge, phrase as „много хора"; no BG survey numbers):
  рождени дати (числата 1–31), „късметлийски" числа, геометрични шарки върху фиша, последователни
  числа, числата от последния тираж. Choosing unpopular numbers does NOT increase the chance to
  win — only (possibly) the share if you win. No fabricated percentages.

### Legal / RG (source pack nap-gambling-law-and-rg-2026-10-10.md)
- Тото/лото = числова лотарийна игра по ЗХ; ЗХ забранява участие на непълнолетни → 18+.
- НАП: бюджет за хазарт ≤5% от нетния доход; „стратегиите за добър късмет" не увеличават
  шансовете; не гонете загубите; регистър по чл. 10г ЗХ; инфо 0700 18 700.

## DO-NOT-FABRICATE
- No number picks, no „hot numbers to play", no „system that beats the draw".
- No current € ticket price, no prize-fund % stated as fact → [VERIFY] if mentioned at all.
- Frequency figures ONLY as quoted above, attributed to the unofficial aggregator, period
  2015-01-01 – 2026-10-08, with [VERIFY].
- No survey percentages about which numbers Bulgarians pick.

## SOURCES
- https://www.toto.bg/ (via source pack, read 2026-10-10)
- https://www.lotteryextreme.com/toto2/649-statistics (fetched 2026-10-10)
- BBC + Reuters 2009 (mirrors above)
- https://bg.wikipedia.org/wiki/Български_спортен_тотализатор (history context only)
- НАП RG via source pack nap-gambling-law-and-rg-2026-10-10.md

## INTERNAL LINKS (all present in live sitemap 2026-10-10; max 4)
- /otgovorna-igra/ (RG — required)
- /blog/responsible-gambling/ (blog hub)
- /blog/keno-pravila/ (sibling: кено — също числова лотарийна игра с теглене на числа)
- /zakonno-li-e/ (optional legal context)
NO affiliate links, NO /sravni-kazina/.

## ANECDOTE OPT-IN: no
## NOTES
Neutral, slightly myth-busting but respectful (people enjoy the ritual of picking numbers — fine
as entertainment). Brand „Всички Казина", byline Георги Тодоров, 18+, RG line. Euro (€). Results → toto.bg.

# 01-SYNTHESIS — vk-0270 — „Системи и комбинации в тото — колко струват и увеличават ли шанса"

BRAND: vsichkikazina · MARKET: bg · TYPE: guide · Published byline: Георги Тодоров · Stage 1 (Synthesis) · 10.10.2026

---

## SYNTHESIS REPORT

**Query:** тото комбинации 6 от 49 цени (+ най добрата система за тото 2; системен фиш тото; пълно комбиниране тото; колко струва система 6 от 49; вероятност за джакпот тото) | **Intent:** informational (cost lookup + „does it help?" evaluation) | **Market:** bg, Bulgarian, €

**Sources:** 2 source packs (bst-toto, nap-gambling-law-and-rg) + the brief's verified secondary set (marica.bg 21.11.2025 and 04.07.2026, sportal.bg 06.07.2026, totosimulator.com EUR tables, bgdnes.bg 28.09.2026, bgprognozi.info, bg.wikipedia БСТ, btvnovinite.bg; info.toto.bg FAQ snippet only). No extra WebFetch was done; every fact in the draft is taken from the brief/packs.
**Corroborated facts used:** 9 (price rise of +0,10 € in 6/49 and 6/42 from тираж 57/2026: marica + sportal; euro-only stakes from 01.01.2026: btvnovinite + info.toto snippet; pre-rise euro prices 0,80/0,70/0,60 €: totosimulator + toto.bg rules snippet; 6/49 current 0,90 €: derived + FAQ snippet; two draws a week, Thursday/Sunday 18:45 on БНТ: toto.bg pack; 5/35 = two draws of 5 numbers: toto.bg pack; prize groups 6/5/4/3 and pari-mutuel payouts: bgdnes + bgprognozi; full-combination cost = combinations × unit price: totosimulator + pure math; НАП RG advice (5% budget, "strategies don't raise chances", register чл. 10г): НАП pack).
**Math:** all combinatorics taken verbatim from the brief's PRE-COMPUTED MATH, re-checked with python3 (`math.comb`) — every figure matches. No new numbers computed beyond the brief (6/42 system-9 odds and 5/35 system-6/7/8 odds intentionally left out of the tables because the brief does not list them).
**[VERIFY] flags:** 4 | **[CONFLICT] flags:** 0 | **[DATA NEEDED]:** 0
1. Current per-combination prices (6/49 0,90 €, 6/42 0,80 €, 5/35 0,60 €) — derived from two secondary sources; toto.bg primary unreachable (CAPTCHA).
2. Special-draw price 6/49 = 1,00 € — info.toto.bg FAQ search snippet only.
3. Whether one 5/35 combination participates in both draws (I и II теглене) — not verified; odds given „за едно теглене".
4. Maximum system size accepted by БСТ on one slip — calculators show up to 14; not verified with БСТ.

**Entity union coverage:** complete for the intent — БСТ (neutral), ТОТО 2: 6/49, 6/42, 5/35; системен фиш / пълно комбиниране; съкратени системи (generic math only, not attributed to БСТ); печеливши групи 6/5/4/3; джакпот; пари-мутюел разпределение; тираж/два тиража седмично; евро от 01.01.2026; поскъпване от тираж 57/2026; очаквана стойност; дисперсия; НАП, ЗХ (лотарийни игри), регистър на уязвимите лица (чл. 10г), 0700 18 700; 18+.

### Gaps closed that no source covered
- Shows the working: C(49,6) = 13 983 816 derived on the page, and C(8,6) = 28 as a hand-checkable example. Competitor pages list tables without the formula.
- Per-euro equivalence: a system buys combinations at a strictly proportional price, so the chance per euro does not change (system 10: 210 combinations for 189,00 € = 1 combination per 0,90 €).
- "Lifetime" framing: system 10 every draw → ≈ 66 590 draws on average ≈ 640 years, total ≈ 12 585 434 €, which equals the cost of buying all 13 983 816 combinations (12 585 434,40 €).
- Multiple-win breakdown inside a system (system 8 at h = 6/5/4; systems 10 and 12 at h = 6) explains *why* systems "win several groups at once", and why that is not free.
- Variance angle: same jackpot probability as the same number of separate random combinations, but small wins cluster.
- Explicit answer to „най-добра система": it does not exist mathematically.

### Source claims excluded as dubious / not used
- Any "best system", "hot/cold numbers" or "winning system" framing common on Bulgarian тото pages: excluded on principle (unsupported, and against НАП's „стратегиите за добър късмет не увеличават шансовете").
- Prize-fund share (% of stakes returned as prizes): not found in any reachable source → not stated; negative EV described qualitatively only.
- Claims that БСТ sells reduced systems (съкратени системи): unsourced → reduced systems explained as generic maths only, without saying БСТ offers them.
- marica.bg 21.11.2025 leva-to-euro conversions (1,60 лв ≈ 0,82 €, etc.) are arithmetic conversions, not the official euro prices; the euro unit prices from 01.01.2026 (0,80/0,70/0,60 €) are used instead. Not a conflict, just a different number type, so not flagged.
- Jackpot sizes at тираж 79 and prize examples from тираж 76: time-sensitive; only the 76 example is used as an illustration of variable payouts, with its date.
- Starting-jackpot rise (1 000 000 → 1 500 000 € in 6/49): accurate but off-intent; omitted.
- Online play via ePay.bg/БОРИКА: context only, omitted (no operator promotion).

### Localisation adjustments
- Currency € only (euro stakes since 01.01.2026); no leva prices in the body.
- Regulator НАП; legal type „лотарийна игра" under ЗХ (числова лотарийна игра).
- Dates DD.MM.YYYY; Bulgarian number formatting (13 983 816; 0,90 €).
- RG per НАП (5% of net income, don't chase losses, register чл. 10г, 0700 18 700) + verbatim 18+ footer.
- Internal links (4, all from the brief's approved list): /blog/progresivni-dzhakpoti/, /blog/danaci-pechalbi-onlajn-kazino/, /blog/responsible-gambling/, /otgovorna-igra/ (footer).

---

## THE ARTICLE (original draft, Bulgarian)

# Системи и комбинации в тото: колко струват и увеличават ли шанса

Система от 10 числа в 6/49 струва 189,00 € и ви дава 210 комбинации. Шансът за джакпот става 1 към около 66 590 вместо 1 към 13 983 816. Звучи като огромен скок, но всяка от тези 210 комбинации е платена на същата цена като единичната. Шансът на всеки похарчен евро остава абсолютно същият. Това е целият отговор накратко. Отдолу са цените, сметките и причината защо „най-добрата система" просто не съществува.

## Какво точно е системен фиш

При пълно комбиниране не отбелязвате 6 числа, а повече, например 8. Фишът автоматично се превръща във всички възможни шестици, които могат да се съставят от вашите 8 числа. Колко са те, казва формулата за комбинации без повторение:

C(N, 6) = N! / (6! · (N − 6)!)

За 8 числа: C(8, 6) = C(8, 2) = 8 · 7 / 2 = 28 шестици. Цената е проста: брой комбинации, умножен по цената на една комбинация. Никаква отстъпка, никаква надценка.

Същата формула дава и общия брой възможни фишове в 6/49:

C(49, 6) = 49 · 48 · 47 · 46 · 45 · 44 / 720 = 13 983 816

Една комбинация е един от тези 13 983 816 варианта. Нищо повече.

## Колко струва система в 6/49

Цената на една комбинация в 6/49 е 0,90 € от тираж 57 на 2026 г. (23.07.2026), след като БСТ я вдигна с 0,10 € спрямо 0,80 € в началото на годината. [VERIFY: текущи цени за една комбинация — 6/49 0,90 €, 6/42 0,80 €, 5/35 0,60 € — изведени от marica.bg 04.07.2026 + sportal.bg 06.07.2026 и евро цените от 01.01.2026; toto.bg недостъпен] При специалните тиражи комбинацията е по-скъпа, 1,00 € [VERIFY: цена за специален тираж 6/49 — само от snippet на info.toto.bg]. Таблицата е за редовен тираж.

| Числа в системата | Комбинации | Цена | Шанс за джакпот |
|---|---|---|---|
| 6 (единичен фиш) | 1 | 0,90 € | 1 към 13 983 816 |
| 7 | 7 | 6,30 € | 1 към 1 997 688 |
| 8 | 28 | 25,20 € | 1 към 499 422 |
| 9 | 84 | 75,60 € | 1 към 166 474 |
| 10 | 210 | 189,00 € | ≈ 1 към 66 590 |
| 11 | 462 | 415,80 € | 1 към 30 268 |
| 12 | 924 | 831,60 € | 1 към 15 134 |

Цената расте много по-бързо от броя числа. От 8 на 12 числа добавяте само четири, но плащате 33 пъти повече. Има и по-големи системи: 13 числа са 1716 комбинации за 1 544,40 €, а 14 числа са 3003 комбинации за 2 702,70 €. Онлайн калкулаторите обикновено стигат до 14 [VERIFY: максимален размер на система, който БСТ приема на един фиш].

## 6/42 и 5/35: същата логика, други числа

В 6/42 една комбинация е 0,80 €, а всички възможни шестици са C(42, 6) = 5 245 786.

| Числа | Комбинации | Цена | Шанс за джакпот |
|---|---|---|---|
| 6 | 1 | 0,80 € | 1 към 5 245 786 |
| 7 | 7 | 5,60 € | 1 към 749 398 |
| 8 | 28 | 22,40 € | ≈ 1 към 187 350 |
| 9 | 84 | 67,20 € | – |
| 10 | 210 | 168,00 € | ≈ 1 към 24 980 |
| 12 | 924 | 739,20 € | ≈ 1 към 5 677 |

5/35 е различна игра. Теглят се пет числа, и то два пъти на тираж: I и II теглене. Системите тук се смятат с C(N, 5), а общият брой петици е C(35, 5) = 324 632.

| Числа | Комбинации | Цена при 0,60 € |
|---|---|---|
| 5 (единичен фиш) | 1 | 0,60 € |
| 6 | 6 | 3,60 € |
| 7 | 21 | 12,60 € |
| 8 | 56 | 33,60 € |
| 10 | 252 | 151,20 € |

Една комбинация има шанс 1 към 324 632 да познае петте числа в едно теглене. Система от 10 числа вдига това до около 1 към 1 288, пак за едно теглене. Дали всяка комбинация участва и в двете тегления, трябва да се провери в правилата на БСТ [VERIFY: участва ли една комбинация 5/35 и в I, и във II теглене], затова тук даваме шанса само за едно теглене.

## Защо системата „печели по няколко групи наведнъж"

В 6/49 се печели с 6, 5, 4 или 3 познати числа. Една комбинация има приблизително такива шансове:

- 6 числа: 1 към 13 983 816
- 5 числа: 258 комбинации, ≈ 1 към 54 201
- 4 числа: 13 545 комбинации, ≈ 1 към 1 032
- 3 числа: 246 820 комбинации, ≈ 1 към 57
- поне 3 числа: ≈ 1 към 54

Системата е друга история, защото шестиците в нея се припокриват. Ако сред вашите N числа има h от изтеглените, броят печалби от група j се дава от C(h, j) · C(N − h, 6 − j). Конкретно:

| Система | Познати от изтеглените (h) | „6" | „5" | „4" | „3" |
|---|---|---|---|---|---|
| 8 | 6 | 1 | 12 | 15 | – |
| 8 | 5 | – | 3 | 15 | 10 |
| 8 | 4 | – | – | 6 | 16 |
| 10 | 6 | 1 | 24 | 90 | 80 |
| 12 | 6 | 1 | 36 | 225 | 400 |

Ето откъде идват историите за „фиш с десетки печалби". Само че всяка от тези печеливши комбинации е била платена, заедно с всички останали, които не са спечелили нищо. Сумите по групи и без това не са фиксирани. В тираж 76 (по данни от 28.09.2026) петица в 6/49 носеше 2211,00 €, четворка 39,20 €, а тройка 4,80 €. Колко ще получите, зависи от това колко залога са събрани и колко души са познали същото. При печалба от няколко групи наведнъж делът ви се дели по същите правила.

## Увеличава ли системата шанса? Сметката на евро

Да, ако гледате само един фиш. Не, ако гледате парите.

Единична комбинация: 0,90 € за шанс 1 / 13 983 816. Система 10: 189,00 € за шанс 210 / 13 983 816. Разделете второто на първото: 210 комбинации за 189 € е точно по 0,90 € на комбинация. Шансът на евро е идентичен. Същото важи за 7, 9 или 12 числа, защото цената на системата е строго пропорционална на броя комбинации.

С очакваната стойност е същото. Всяка комбинация в даден тираж има еднаква очаквана стойност, а системата е просто пакет от комбинации. Затова очакваната стойност на евро също не се мени. И тя е отрицателна: тотото връща под формата на печалби по-малко, отколкото събира като залози. Системата не променя този знак, тя само го умножава.

За мащаб: ако играете система 10 на всеки тираж, средно ще чакате около 66 590 тиража до джакпот. При два тиража седмично, 104 годишно, това е около 640 години. Общият разход за това време е ≈ 12 585 434 €. Колкото да купите всички 13 983 816 комбинации наведнъж (13 983 816 × 0,90 € = 12 585 434,40 €). Системата не е пряк път, а същият път, изминат на по-големи стъпки.

## Тогава с какво се различава от отделни фишове

С две неща, и нито едно не е по-добър шанс.

Удобство: един фиш вместо 28 или 210 ръчно попълнени комбинации, без риск да повторите шестица.

Концентрация. Шансът за джакпот е еднакъв, независимо дали 210 комбинации са от система 10 или са 210 различни произволни шестици, защото всяка комбинация е различна. Разликата е в малките печалби. При системата те идват на купчини: когато уцелите, обикновено печелите по няколко групи наведнъж; когато не уцелите, губите целия фиш. С разпръснати комбинации малките печалби идват по-равномерно. Средното е същото, разпределението е различно.

Съкратените системи са същото в по-малък мащаб. Покриват само част от шестиците на пълната система, плащате по-малко, и шансът на евро отново не се мени. Механиката на голямата награда е разгледана по-подробно в статията ни за [прогресивните джакпоти](/blog/progresivni-dzhakpoti/).

## Има ли „най-добра система"?

Не. Математически няма комбинация от числа или размер на система, която да дава по-добър шанс на похарчен евро. Всяка шестица от 13 983 816 има един и същ шанс във всеки тираж, а тиражите са независими. Предишни резултати, „горещи" и „студени" числа нищо не значат за следващото теглене. Затова във Всички Казина не публикуваме числа, системи „за печалба" или прогнози. НАП казва същото с други думи: стратегиите за добър късмет не увеличават шансовете.

Ако все пак ви се играе система, разумният въпрос не е „коя", а „колко мога да си позволя да загубя". Препоръката на НАП е бюджетът за хазарт да не надвишава 5% от нетния ви доход. Система 12 на всеки тираж е 831,60 € два пъти седмично. Тотото е лотарийна игра по Закона за хазарта и е забавление, не източник на доход. Не гонете загубите с по-голяма система.

Ако печелите, данъчната страна е описана в [данъците върху печалбите](/blog/danaci-pechalbi-onlajn-kazino/). Ако играта е спряла да е забавна, всеки може да се впише в регистъра на уязвимите лица към НАП (чл. 10г ЗХ) за срок не по-кратък от 12 месеца; информация на 0700 18 700. Още материали има в раздела ни за [отговорна игра](/blog/responsible-gambling/).

---

*18+ Хазартът може да пристрасти. Играйте отговорно.* → [/otgovorna-igra/](/otgovorna-igra/)

*Автор: Георги Тодоров*

---

## SUGGESTED PERSONA (author pass)

**Георги Тодоров, editorial voice (bg market author file).** Math-heavy explainer whose value comes from neutral, checkable working rather than a personality, so the guide register fits. The byline is fixed to Георги Тодоров for this brand regardless.

### Notes for downstream stages
- Word count of the article body ≈ 1 450 (inside the 1 200–1 600 target).
- Brand mentions: 1 („Всички Казина", in the „най-добра система" section).
- Em-dashes: none in the body; tables use „–" only as an empty-cell marker.
- 6/42 system 9 jackpot odds shown as „–" on purpose (not in the brief's pre-computed math). The author may compute it only if the brief is updated.

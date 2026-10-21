# 01 — SYNTHESIS · vk-0176 · Три карти покер (Three Card Poker)

## SYNTHESIS REPORT
Query: "Три карти покер (Three Card Poker): правила, залози и стратегия" | Intent: informational (how-it-works + strategy) | Market: bg
Sources: 2 primary (Wizard of Odds; Wikipedia) + corroborating search | Corroborated facts used: all core figures appear in 2+ sources | [VERIFY] flags: 0 (all figures traced to reachable sources) | [CONFLICT] flags: 0
Entity union coverage: complete — Ante, Play, dealer qualification (Queen high), Pair Plus, Ante Bonus, 3-card hand ranking + combinatorics, Q-6-4 strategy, house edge / element of risk, volatility framing, RTP framing.
Gaps closed no single source stresses: (a) the WHY behind straight-beats-flush shown with the actual combination counts a player can verify; (b) side-by-side house-edge comparison of the three bets in one place; (c) the Ante Bonus paying even when the dealer folds, stated plainly as the one genuinely player-friendly quirk.
Source claims excluded as dubious: none. Care taken on Pair Plus: house edge depends on the flush payout, so BOTH common paytables are presented with their own edge (4:1 flush → 2.32%; 3:1 flush → 7.28%) rather than quoting one edge as universal.
Localisation: € currency, BG native casino vocabulary (домашно предимство, кента, флъш, трипс, стрейт флъш), DD.MM.YYYY dates, регулатор НАП context via RG block. No operator names (educational guide, not a review). No tax claims.

## FACT INVENTORY (all CORROBORATED unless noted)
- Играе се срещу дилъра/казиното, не срещу други играчи; тесте 52 карти; всеки получава 3 карти. [Wizard, Wikipedia]
- Основен цикъл: залагаш Анте → виждаш 3-те си карти → или пасуваш (губиш Анте), или добавяш залог Play, равен на Анте. [Wizard, Wikipedia]
- Дилърът се квалифицира с дама-висока (Queen high) или по-добра ръка. [Wizard, Wikipedia]
- Ако дилърът НЕ се квалифицира: Анте се плаща 1:1, а залогът Play няма действие (връща се). [Wikipedia]
- Ако дилърът се квалифицира и загуби: Анте и Play плащат по 1:1. Ако спечели: губиш и двете. [Wizard, Wikipedia]
- Ante Bonus (най-често срещана таблица, Pay Table 1): кента 1:1, трипс 4:1, стрейт флъш 5:1; плаща се НЕЗАВИСИМО дали дилърът се квалифицира или дали печелиш ръката. [Wizard, Wikipedia]
- Pair Plus страничен залог: печели при пара или по-добра ръка, независимо от ръката на дилъра. [Wizard, Wikipedia]
  - Оригинална таблица (флъш 4:1): пара 1:1, флъш 4:1, кента 6:1, трипс 30:1, стрейт флъш 40:1 → домашно предимство 2.32%. [Wizard]
  - Днес най-често срещана (флъш 3:1): пара 1:1, флъш 3:1, кента 6:1, трипс 30:1, стрейт флъш 40:1 → домашно предимство 7.28%. [Wizard]
  - Таблиците ВАРИРАТ по казина. [Wizard]
- Домашно предимство Ante & Play: 3.37% спрямо Анте; element of risk (спрямо общо заложеното) 2.01%. [Wizard]
- Оптимална стратегия: играй (Play) с дама-6-4 или по-добра ръка; под този праг — пасувай. [Wizard, corroborating]
- 3-картова подредба (най-силно→най-слабо): стрейт флъш > трипс > кента > флъш > пара > висока карта. [Wizard, Wikipedia]
- Причина кентата да бие флъша: по-рядка е с 3 карти. Комбинации от C(52,3)=22,100: стрейт флъш 48, трипс 52, кента 720, флъш 1,096, пара 3,744, висока карта 16,440. [Wikipedia; sum verified = 22,100]

## THE ARTICLE (original draft — facts placed, voice to be added downstream)

Три карти покер се играе срещу самото казино, не срещу другите на масата. Тесте от 52 карти, три карти за теб, три за дилъра, и няколко залога, които не работят по един и същ начин. Който сяда с идеята, че познава покера, бързо се сблъсква с два обрата: подредбата на ръцете е разместена, а страничният залог струва в пъти повече от основната игра.

### Как тече една ръка
Залагаш Анте. Получаваш трите си карти открити пред теб. Решаваш: пасуваш и губиш Анте, или добавяш втори залог Play, равен на Анте, за да се мериш с дилъра. Дилърът обръща своите три карти. Тук идва квалификацията: ръката на дилъра трябва да е дама-висока или по-добра. Не се ли квалифицира, Анте плаща 1:1, а Play няма действие и се връща. Квалифицира ли се и губи, Анте и Play плащат по 1:1. Спечели ли, губиш и двете.

### Странната подредба на ръцете
При три карти кентата бие флъша, обратно на класическия покер. Причината е в честотата. От всички 22,100 възможни ръце с три карти кентата се пада 720 пъти, а флъшът 1,096 пъти. По-рядката ръка стои по-високо. Пълната подредба от най-силна към най-слаба: стрейт флъш, трипс, кента, флъш, пара, висока карта.

### Pair Plus: залогът само за твоите карти
Pair Plus не се интересува от дилъра. Печелиш, ако държиш пара или по-добра ръка, и толкова. Една честа таблица плаща: пара 1:1, флъш 4:1, кента 6:1, трипс 30:1, стрейт флъш 40:1, при домашно предимство 2.32%. По-новата и вече по-разпространена версия сваля флъша на 3:1 и вдига предимството до 7.28%. Таблиците се различават по казина, затова първото за проверка е точно колко плаща флъшът.

### Ante Bonus: бонусът, който не пита за дилъра
Освен основната игра, силна ръка носи допълнителен бонус върху Анте, независимо дали дилърът се квалифицира и дори дали печелиш ръката. Честа таблица: кента 1:1, трипс 4:1, стрейт флъш 5:1. Това е рядкото място, където правилата работят за играча.

### Оптималната стратегия: правилото дама-6-4
Едно решение носи почти цялата стратегия: кога да добавиш Play и кога да пасуваш. Прагът е дама-6-4. Държиш ли тази ръка или по-добра, залагаш Play. Под нея пасуваш. Числата: домашно предимство на Ante & Play около 3.37% спрямо Анте, а спрямо всичко заложено (element of risk) около 2.01%.

### Колко струва
Ante & Play с правилна стратегия: 3.37% предимство спрямо Анте. Pair Plus: между 2.32% и 7.28% според таблицата. Основната игра е по-евтина от страничния залог.

(RG touch, links, boilerplate added downstream.)

## SUGGESTED PERSONA
EDITORIAL voice (patient-teacher guide, numbers-first), signed Георги Тодоров per brand rule. Guide type, no persona anecdotes, no Протокол block (no operator tested).

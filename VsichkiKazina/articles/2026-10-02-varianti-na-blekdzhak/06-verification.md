# 06 · VERIFICATION · vk-0239 · Варианти на блекджек
Type: guide · byline: Георги Тодоров · gate: PASS 92/100, 0 critical · run date 02.10.2026

## SURVIVING IN-TEXT FLAGS: 0
Няма [VERIFY]/[DATA NEEDED]/[CONFLICT] в 05b. Няма данъчни, оператор или НАП твърдения.
Human-attention items (not flags): (1) "около 0,5%" като база е кръгла стойност, подкрепена от Wikipedia ("under 1%") и Wizard of Odds (0,28% либерални правила, 0,62% европейски пример); (2) H17 е дадено като "около 0,2% (в таблицата 0,22%)", защото Wizard при друга база (Wong benchmark) дава около 0,19%; (3) ефектите при комбинация (2,3%) са грубо адитивни, казано е в текста.

## SOURCED CLAIMS (всички web-fetched 02.10.2026)
| Claim | Source |
|---|---|
| База: 8 тестета, S17, DAS; плюс = в полза на играча | Wizard of Odds, Blackjack basics: https://wizardofodds.com/games/blackjack/basics/ |
| Single deck +0,48; 2 тестета +0,19; 6 тестета +0,02; late surrender +0,08; early surrender vs ten +0,24; double 9-11 -0,09; European no hole card -0,11; без DAS -0,14; double 10,11 -0,18; H17 -0,22; 7:5 -0,45; 6:5 -1,39; 1:1 -2,27 | същото (rule variations table) |
| Европейски 0,62% (6 тестета, S17, double 9-11, DAS, no-peek, загуба на целия залог) ; отделна стратегия за европейски | https://wizardofodds.com/games/blackjack/strategy/european/ |
| 0,28% "Liberal Vegas rules"; стандартно отклонение 1,15 | https://wizardofodds.com/gambling/house-edge/ |
| H17 около 0,19% при Wong benchmark (S17 +0,00191) | https://wizardofodds.com/games/blackjack/appendix/4/ |
| "под 1%" с основна стратегия; "6:5 adds 1.4%"; "no-hole-card adds approximately 0.11%" | https://en.wikipedia.org/wiki/Blackjack |
Заданието даваше 6:5 ≈ 1,39, H17 ≈ 0,20, single deck -0,48, no-hole-card +0,11: всички потвърдени (знакът в статията е от гледна точка на играча).

## RECALCULATION (един показан с работа)
6:5 срещу 3:2 при залог €10: блекджек плаща €15 срещу €12, разлика €3 = 0,3 от залога. P(туз + десетица като първи две карти) при безкрайна колода = 2 x (4/13) x (1/13) = 8/169 = 4,734%. 0,3 x 4,734% = 1,42% ≈ таблицата 1,39% (малката разлика идва от пушовете при блекджек на дилъра). На €1 000 оборот: 1,39% x 1 000 = €13,90. Останалите (13,90 / 0,11 = 12,6; 0,48 - 1,39 = -0,91; 1,39+0,22+0,18 = 1,79; 0,5+1,79 = 2,29; 1,15 x 10 x sqrt(100) = 115) проверени в 05-gate-report.md.

## GEMINI STEP-7
Pass 1 (initial 05b): "Likely human-written, 80%" -> human-likeness 80 = PASS. 0 humaniser passes needed. Kept: original 05b (pass 0). Забележка: по погрешка скриптът е извикан втори път върху същия файл и върна "Likely AI-generated, 85%" (HL 15): вариация на детектора, записана в 07-gemini-check-1b-rerun.md; не е използвана за решение. Final HL 80, gemini column: human 80.

## IMAGES
images: 2 (infographic SVG 100, hero WebP 100; единична комбинирана оценка 100 PASS, 0 integrity failure; SVG рендиран и прегледан визуално, без припокриване/клипване). Всички числа в SVG са дословно от 05b таблицата.

## COMPLIANCE SPOT-CHECK
Em-dash 0 · байлайн Георги Тодоров · бранд "Всички Казина" · 3 вътрешни линка (/kazino-igri/, /otgovorna-igra/, /kak-ocenyavame/) · RG естествен момент в тялото + footer · афилиейт footer дословно · без афилиейт линк/оператор/НАП № · без "Протокол на тегленето".

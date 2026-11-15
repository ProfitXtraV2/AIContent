# 00-inventory — /diagnostika/ (new-page from the owner's checker)

Every item below must survive every editing stage with the same meaning. Wording is rewritten to
formal „Вие“; structural data (ids, type keys, hours, solution keys, order) is copied EXACTLY.

## A. Structural data (copy exactly, never change)
- Type keys and order: resto, hotel, salon, shop, retail, clinic, auto, estate, b2b (+ "all").
- Group ids and order: g1, g2, g3, g4.
- Solution keys: a, t, c, m. Hrefs (brief, one per key): a → /avtomatizacii/, t → /seo-statii/,
  c → /socialni-mrezhi/, m → /reklama/.
- 29 symptoms in source order; for each: group, types, hours, solution keys exactly as in table D.
- hoursBadge keeps the `{h}` placeholder; summary keeps `{n}` and `{h}`.

## B. Labels (meaning to keep; reword to „Вие“)
- allLabel: „Всички бизнеси“.
- typeNames: resto „Ресторант / кафене“; hotel „Хотел / къща за гости“; salon „Салон / услуги“;
  shop „Онлайн магазин“; retail „Магазин / шоурум“; clinic „Клиника / кабинет“; auto „Автосервиз /
  майстори“; estate „Недвижими имоти“; b2b „B2B / друго“.
- solution titles: a „AI автоматизации“; t „Нашият инструмент за съдържание“ (canon: „Собствен
  инструмент за съдържание“); c „Криейтиви всеки месец“; m „Маркетинг специалист“.
- groups: g1 „Клиенти и комуникация“ / sub „Там, където запитванията се превръщат (или не) в
  клиенти.“; g2 „Админ и документи“ / „Повтарящата се работа, която никой не ти плаща.“; g3 „Онлайн
  присъствие и съдържание“ / „Това, което клиентите виждат, преди да ти се обадят.“; g4 „Реклама и
  растеж“ / „Как те намират нови клиенти.“
- hoursBadge: „~{h} ч/седм.“ (hours are owner estimates; must be labelled „ориентировъчно, на база
  типични случаи“ on the page: in estimateNote and in the lead).
- New UI strings to write (no source wording; TEMP in fixture): filterLabel, pickLabel, summary,
  summaryEmpty, estimateNote, cta (source ctaBtn „Запази безплатна диагностика“ → formal).

## C. Page-level items (from source + canon)
- CTA: booking via `{{BOOKING_URL}}`, wording „Запазете безплатна диагностика“ (source ctaBtn,
  ctaTitle „Позна ли се в нещо?“, ctaText „Запази безплатна диагностика — правим точната сметка за
  твоя бизнес и ти казваме честно какво може да се автоматизира. Или ни пиши на:“ + email).
- Token `{{EMAIL}}` (source ctaText "Или ни пиши на:" → email line).
- Canon: free diagnosis + 30-minute call; report with prioritised fixes and clear one-off prices
  within 48 hours (no price figures); build usually up to 2 weeks (keep „обикновено“); monthly
  support with a short report; no long-term contracts; transparent prices; „Работим по GDPR“;
  the diagnosis commits the client to nothing.
- Source title meaning: how much time the business loses without noticing („Колко време губи
  бизнесът ти, без да забелязваш?“).
- Source lede meaning: examples from different business types: the problem as the owner lives it
  and what BizGrow takes over; hours are rough, based on typical cases. RESTRICTION (brief): "29
  реални примера" may NOT be claimed as client data; say „примери“.
- Estimate label: „ориентировъчно, на база типични случаи“ wherever hours are shown/summed.
- The source footer line is NOT page copy (site footer handles it).

## D. The 29 problems (pain → fix), source order
| # | group | types | hours | solutions | pain (source) | fix (source) |
|---|---|---|---|---|---|---|
| 1 | g1 | all | 3 | a | Клиент пише в 21:30 с въпрос. До сутринта вече е купил от друг. | **AI асистент** отговаря в Messenger, Instagram и WhatsApp денонощно — и събира контакта, когато не може да помогне. |
| 2 | g1 | all | 4 | a | Отговаряш на едни и същи 10 въпроса всеки ден — цени, работно време, доставка, наличности. | **AI помощник**, обучен на твоята собствена информация, поема повтарящите се въпроси вместо теб. |
| 3 | g1 | resto,salon,clinic,auto | 2 | a | Телефонът звъни, докато обслужваш клиент — и обаждането се губи завинаги. | **Онлайн записване** — клиентите сами избират час/маса, без никой да вдига телефона. |
| 4 | g1 | salon,clinic,resto | 3 | a | Часовете и резервациите живеят в тетрадка — разместването им е цял ден по телефона. | **Резервации, синхронизирани с календара**, с автоматични напомняния, които намаляват неявяванията. |
| 5 | g1 | hotel | 3 | a | Турист пише на английски в 23:00 за свободни стаи. Отговорът тръгва чак след закуска. | **AI асистент за гости** отговаря на всеки език, денонощно — с реална наличност и цени. |
| 6 | g1 | resto,salon,clinic | 2 | a | Запазват час или маса — и просто не идват. Прозорецът остава празен. | **Автоматични потвърждения и напомняния** + списък с чакащи, който запълва освободените часове. |
| 7 | g1 | auto | 2 | a | „Готова ли е колата?“ — питат по пет пъти на ден, а ти си под колата. | **Автоматични съобщения за статуса** на ремонта — клиентът знае, без да звъни. |
| 8 | g1 | shop | 3 | a | „Къде ми е поръчката?“ — двайсет пъти на ден, всеки ден. | **AI, свързан с куриера**, отговаря сам — със статус на пратката в реално време. |
| 9 | g1 | estate | 3 | a | Запитване за оглед идва в полунощ от портала. Виждаш го на обяд — заедно с още 40. | **AI квалифицира запитванията** и сам предлага свободни часове за оглед на сериозните. |
| 10 | g2 | b2b,retail,auto,estate | 3 | a | Всяка оферта я пишеш на ръка — и тя тръгва чак вечерта, когато най-после седнеш. | **Автоматични оферти**: от формуляр до готов PDF в пощата на клиента за минути. |
| 11 | g2 | auto,b2b | 3 | a | Оглеждаш, снимаш, обещаваш оферта — и я пращаш чак след два дни. | **Оферта от снимки и кратък формуляр** — готова за минути, не за дни. |
| 12 | g2 | shop,retail,b2b | 3 | a | Прехвърляш едни и същи данни между поръчки, таблици и счетоводство — по три пъти. | **Свързваме системите ти** и данните се попълват сами, без копиране. |
| 13 | g2 | all | 2 | a | Фактури, отчети и Excel таблици ти изяждат неделя вечер. | **Автоматизираме документите** — създават се и се подреждат сами. |
| 14 | g2 | b2b,estate | 2 | a | Договорите се сглобяват с копи-пейст от стари файлове — понякога с чужди имена вътре. | **Шаблони с автоматично попълване** — без грешки от копиране. |
| 15 | g2 | estate | 2 | a | Една обява = ръчно качване в три портала. После ръчно сваляне от трите. | **Публикуваш веднъж** — системата качва, обновява и сваля навсякъде. |
| 16 | g2 | shop | 3 | t | 50 нови продукта чакат описания — и ти ги пишеш вечер, едно по едно. | **Инструментът ни пише SEO описания** на цели колекции за минути — в твоя тон. |
| 17 | g2 | all | 2 | a | Не знаеш кои клиенти се връщат, кое се продава и кое реално носи печалба. | **Табло с показатели** в реално време — виждаш бизнеса си в едно. |
| 18 | g3 | all | 3 | t | Сайтът ти не се е променял от месеци — и Google те подминава за сметка на конкуренцията. | **Готовият ни инструмент** пише SEO статии за твоя бранш и град и ги публикува — ти само одобряваш. |
| 19 | g3 | all | 3 | t | Instagram и Facebook мълчат от седмици, защото „нямаше време“. | **Инструментът ни създава публикации** — текст и изображение — и ги качва по график, всяка седмица. |
| 20 | g3 | shop,retail,resto,salon,hotel | 2 | t,c | Нямаш свежи снимки и визии — и всяка публикация или реклама започва от нулата. | **AI изображения и брандирани криейтиви**, готови за публикуване и за реклама. |
| 21 | g3 | resto,salon,clinic,retail,auto,hotel | 1 | a | Отзивите в Google стоят без отговор — и новите клиенти го виждат. | **Следим отзивите ти** и подготвяме отговор за одобрение с едно докосване. |
| 22 | g3 | resto,salon,clinic,retail,auto | 1 | t,m | Google Business профилът ти е с 3 снимки от 2022 и старо работно време. | **Поддържаме профила жив** — публикации, снимки и актуална информация всеки месец. |
| 23 | g3 | resto,hotel | 1 | a | Менюто и цените се смениха — но в сайта, Google и Facebook стои старото. | **Обновяване от едно място** — навсякъде едновременно, без да обикаляш платформите. |
| 24 | g4 | shop,retail,b2b,salon,estate | 2 | m | Пускал си реклама „да видим дали ще стане“ — и до днес не знаеш какво точно ти донесе. | **Нашият маркетинг специалист** настройва кампаниите и ти показва какво връща всяко вложено евро. |
| 25 | g4 | shop | 2 | a,m | Количката е пълна, клиентът изчезва — и никой не му напомня. | **Автоматични съобщения** връщат изоставените колички — едни от най-лесните продажби. |
| 26 | g4 | retail,shop,resto | 2 | m | Пускаш отстъпки наслуки — и не знаеш кое всъщност връща клиенти. | **Кампании на база данни**: кой какво купува, кога се връща и какво му предложи. |
| 27 | g4 | all | 2 | t,c,m | Конкуренти с по-слаб продукт излизат над теб в Google и в социалните мрежи. | **SEO съдържание + криейтиви всеки месец** — присъствие като на голям бранд, без да наемаш екип. |
| 28 | g4 | b2b | 2 | a | След всяка среща обещаното остава в тефтера — и половината се забравя. | **AI резюме след срещата** — изводи, задачи и следващи стъпки, автоматично. |
| 29 | g4 | all | 4 | m,c,t | Нямаш време да мислиш за маркетинг — камо ли да го правиш всяка седмица. | **Маркетинг специалистът ни поема планирането и изпълнението** — ти получаваш отчет, не задачи. |

Numbers inside pains (21:30, 10 въпроса, 23:00, пет пъти, двайсет пъти, още 40, два дни, три пъти,
три портала, 50 продукта, 3 снимки от 2022) are illustrative scenario details from the owner's
copy, not client data; they may be kept only inside the clearly labelled examples (owner item).
Capabilities in the fixes are canon (markets/bg/author.md "WHAT THE SERVICES CAN DO" list);
nothing beyond them may be added.

## Counts
CTAs 1 (booking) + email line; tokens 2; anchors: none existing (new page); canon facts 8;
numbers: 30 минути, 48 часа, 2 седмици, 29 hours values, the pain-detail numbers above;
example labels: hours estimate label + "examples, not client data"; FAQs: none existing.

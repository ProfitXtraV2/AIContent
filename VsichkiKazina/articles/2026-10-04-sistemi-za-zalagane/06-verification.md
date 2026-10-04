# 06 — VERIFICATION (Step 6, human-owned) · vk-0253
Article: Системи за залагане: защо Мартингейл, Фибоначи и Д'Аламбер не бият казиното · guide · signed Георги Тодоров · checked 04.10.2026
gate: PASS 92/100 · humanisation: 2 humaniser passes (kept pass 1) · Gemini Step-7: **ai 75** (initial HL 25; pass 1 HL 25; pass 2 HL 20 → KEPT pass 1 at HL 25, highest seen) · images: 2 (infographic clean/"ready to publish", hero 60 decorative; 0 integrity failures; kept best after 1 fix pass, MAX_IMAGE_PASSES reached)

## SURVIVING FLAGS
Count: 0. No [VERIFY], [DATA NEEDED] or [CONFLICT] flag remains in the text. Every asserted fact is a
universal probability/mechanic claim from reachable international sources (below). No Bulgarian operator
T&C, НАП register data, operator-specific number, or tax claim appears in the piece. The human confirms
the claims table before publish.

## CLAIMS TO CONFIRM (universal maths/mechanic facts — source URLs)
| # | Claim in text | What the source shows | Source URL |
|---|---|---|---|
| 1 | Никоя система за залагане не променя домашното предимство; очакваната загуба на заложена единица е същата като при плосък залог | "No betting system changes the house edge … the expected loss per dollar wagered is identical to flat betting" | https://wizardofodds.com/gambling/dalembert-betting-system/ · https://www.effortlessmath.com/blog/fibonacci-betting-system-math/ |
| 2 | Мартингейл: удвояваш след всяка загуба; печалбата връща всичко изгубено плюс стартовата единица | "Double your stake after every loss. When you win, you recover everything you lost plus your original stake as profit" | https://gamblingcalc.com/gambling-guides/betting-systems-compared/ |
| 3 | Д'Аламбер: +1 единица след загуба, −1 след печалба (плавна стъпка, не удвояване) | "Increase your bet by one unit after a loss, and decrease it by one unit after a win … a slow, stepped progression" | https://wizardofodds.com/gambling/dalembert-betting-system/ |
| 4 | Фибоначи: редица 1,1,2,3,5,8,13; при загуба крачка напред, при печалба две назад | "Uses the Fibonacci sequence … after a loss you move one step forward; after a win you move back two steps" | https://www.pokernews.com/casino/roulette/fibonacci-strategy-for-roulette.htm · https://www.effortlessmath.com/blog/fibonacci-betting-system-math/ |
| 5 | Паролі (позитивна): удвояваш след печалба, връщаш се на старта при загуба или след серия печалби | "After a win, you double your bet; after a loss, you return to your starting stake … reset after a limit of consecutive wins" | https://gamblingcalc.com/gambling-guides/betting-systems-compared/ |
| 6 | Събитията са независими: колелото/RNG няма памет; миналите резултати не менят вероятността на следващия | "every system is a pattern of stakes sitting on top of independent events" | https://gamblingcalc.com/gambling-guides/betting-systems-compared/ |
| 7 | Провал: краен банкрол + таван на масата спират прогресията при дълга серия загуби → една голяма загуба трие многото малки печалби | Betting systems "can't overcome the house edge"; a long losing streak forces a stake beyond the bankroll/table limit before recovery | https://gamblingcalc.com/gambling-guides/betting-systems-compared/ · https://wizardofodds.com/gambling/dalembert-betting-system/ |

## ILLUSTRATIVE (HYPOTHETICAL) NUMBERS — marked as such in text/graphic, not to be verified against any real table
| Figure in text | Role | Marked illustrative? |
|---|---|---|
| стартова единица €2 | примерен старт на Мартингейл | yes („Числата са примерни") |
| 2, 4, 8, 16, 32, 64, 128, 256 | примерна последователност от удвоявания | yes |
| €510 (сбор залог 1–8) | примерен сбор | yes |
| €512 (деветия залог) / €500 (таван на масата) | примерен залог срещу примерен таван | yes (инфографика „Числата са примерни") |

## RECALCULATION SHOWN (Мартингейл удвояване)
- Сбор залог 1–8: 2+4+8+16+32+64+128+256 = 510 ✓ (геометрична сума 2·(2^8−1) = 2·255 = 510).
- Деветия залог: 2·256 = 512 ✓. Таван €500 < €512 → залогът е невъзможен → сериите спират на −€510 ✓.
- Инфографиката: височини се удвояват като стойностите (3,3,4,8,16,32,64,128,256 px ≈ експоненциално),
  последният (€512) е пунктирен/блокиран; всяко число трасира до 05b; рендер в PNG проверен — без
  застъпване/отрязване, 9 стълба + ос, „18+ Играйте отговорно" + „Числата са примерни" носени.
- Всички числа илюстративни и вътрешно консистентни; няма € бонус/превъртане сметка (не е бонус статия).

## COMPLIANCE SPOT-CHECK
- Em-dashes (—): 0 в title, meta, тяло, ALT, caption, footers (grep 0). Един en dash (–) само в verbatim RG реда „10:00–17:00".
- Byline Георги Тодоров; pub + updated дати 04.10.2026; About boilerplate оставен като именован placeholder.
- Verbatim „18+ Хазартът може да пристрасти. Играйте отговорно." присъства inline в тялото и в RG footer-а (2 пъти).
- RG signposting към /otgovorna-igra/ + национален регистър на уязвимите лица (НАП, писмено, само от засегнатото лице) + Солидарност 0888 99 18 66.
- Affiliate footer verbatim; лиценз на сайта като заявление подадено / очаква издаване (без „издаден"/измислен №). Генеричен guide: няма препоръчан оператор/афилиейт връзка.
- Currency контекст €; регулатор НАП не е нужен (няма оператор/лиценз твърдение); юрисдикция България именувана в affiliate footer-а.
- Няма promise/hype/FOMO думи; няма банирани AI конективи (освен това/в допълнение/в заключение…).
- Internal links: 4, всички от одобрения набор и потвърдени LIVE в sitemap.xml (curl 04.10.2026):
  /kazino-igri/ruletka/, /kazino-igri/blakdzhak/, /kazino-igri/, /otgovorna-igra/.
- RG доктрина „хазартът не е финансова стратегия / платено забавление с известна цена" присъства;
  естествена in-body RG нотка (лимит преди първия залог; прогресията харчи банкрола по-бързо; спри при гонене на загуба).
- Images: 2. Infographic: всяко число трасира до 05b, маркирано примерни, носи „18+ Играйте отговорно",
  0 layout defect (PNG рендер проверен), reviewer „no problems found, ready to publish". Hero: декоративна
  метафора (стълба от чипове, спряна от непокътнат таван = лимит), без текст/числа/логa/лица/слот-UI/
  глорифицирана печалба; reviewer flag е само естетичен (плосък таван над 3D чипове) → 0 integrity failure.

## ANTI-CANNIBALIZATION NOTE
Dedicated cross-game maths/strategy pillar on betting-progression systems and the honest „прогресията не
мести домашното предимство" truth. Owns that class; routes elsewhere in prose instead of duplicating:
- Рулетка: правила и стратегии (вкл. Мартингейл) (vk-0024): game-specific; тук Мартингейл е част от по-широк
  cross-game клас, рулетката е вътрешен линк (/kazino-igri/ruletka/), не фокусът.
- Блекджек (vk-0010/варианти): basic-strategy е отделна тема; тук се ползва само като контраст (стратегията
  в играта свива предимството, прогресията върху залога не) с линк към /kazino-igri/blakdzhak/.
- SITEMAP CHECK (04.10.2026, raw XML via curl, 95 URLs): няма „системи за залагане"/„Мартингейл"/„Фибоначи"/
  „Д'Аламбер"/„betting systems" pillar; тази статия запълва празнината.

## EXTERNAL CHECK (Step 7 — Gemini cross-model)
Gemini (gemini_check.py, ONLINE, gemini-3.1-pro-preview, no 429). Initial 05b → „Shows AI patterns, 75%"
→ HL 25. Humaniser pass 1 (drop tautology-keyword, break 3/5 „не X,а Y" антитези, ground personification,
merge staccato opener) → re-check: „Shows AI patterns, 75%" → HL 25 (flat; detector relocated goalposts,
flagged the pass-1 fix itself). Humaniser pass 2 (flatten reveal, break „макар X,Y" synthesis, drop one
„обаче", de-philosophise outro) → re-check: „Shows AI patterns, 80%" → HL 20 (LOWER). MAX_GEMINI_PASSES (2)
reached. KEEP-BEST: highest HL seen = 25 (initial ties pass 1); pass 1 is cleaner, so the pass-1 wording is
the kept 05b. gemini column = ai 75 (winning version's verdict). Topic is inherently didactic (must state
the house-edge truth repeatedly for accuracy/RG), which caps the detector; facts/links/RG/byline untouched
through every pass. 07-gemini-check-1.md / -2.md persist.

## HUMAN-ACTION LIST (before publish)
1. Confirm claims 1–7 against the source URLs above (universal betting-system mechanics + the house-edge
   invariance; all stable, non-time-sensitive).
2. Fill [About Всички Казина boilerplate] from the live brand boilerplate at publish.
3. Confirm the 4 approved internal-link targets resolve on the live site (all present in sitemap 04.10.2026).
4. No flags to resolve; no operator/НАП/tax data used; no affiliate link / recommended operator (generic guide).
5. Optional: the decorative hero is stylistically weak (image review 60, aesthetic only — not an integrity
   issue); the clean exponential infographic carries the page. Replace the hero later if a better render is wanted.
6. Say „verified" to release 05b-final-draft.md for publish. Do NOT present 05b as publishable until this is done.

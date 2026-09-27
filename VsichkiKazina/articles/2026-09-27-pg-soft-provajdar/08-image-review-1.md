# 08 — IMAGE REVIEW 1 · PG Soft провайдър-профил

STATUS: AI hero SKIPPED (HTTP 402) · Gemini visual review SKIPPED (HTTP 402) · MANUAL INTEGRITY: PASS.

## Images shipped (1)
- **images/pg-soft-portfolio-i-mehaniki-infografika.svg** — hand-authored SVG infographic (portfolio + механики/RTP snapshot). Clones evo.svg style (dark card #0f172a, Arial, blue accent headers #93c5fd, right-aligned bold values).

## AI hero
SKIPPED — Gemini image API offline (HTTP 402). За data/mechanics-heavy провайдър-профил инфографиката е предпочитаната илюстрация; hero не е задължителен. Никакъв gemini_image_gen.py не е извикван.

## Gemini visual review
SKIPPED — HTTP 402. Заменено с ръчна проверка на интегритета по-долу.

## MANUAL INTEGRITY CHECKLIST — PASS
- [x] Всяко число в SVG проследено дословно до 05b: 2015; 96,95%; 96,92%; 96,81%; 96,75%; 96,73%; „около 1% или 2%"; 100 000x; 2 500x; 2 000x. Няма число, което тялото да не заявява.
- [x] Илюстративните/ориентировъчни стойности маркирани: подзаглавие „RTP зависи от версията, не от рекламата" + жълта бележка „Операторът може да пусне версия с около 1% или 2% по-нисък RTP" + footer „RTP зависи от конкретното заглавие/версия".
- [x] Задължителен caveat „RTP зависи от конкретното заглавие/версия" присъства (footer bar).
- [x] „18+ Играйте отговорно" присъства (footer bar).
- [x] „Потенциал" рамкиран като таван: „Mahjong Ways 2: до 100 000x. Таван, не очаквана печалба."
- [x] Няма operator логота/имена, няма лица, няма гламуризирано печелене.
- [x] Filename descriptive, lowercase, hyphenated, топикален: pg-soft-portfolio-i-mehaniki-infografika.svg.
- [x] Специфичен български ALT (описва точно какво показва инфографиката, не „изображение").
- [x] Референция от 05b на естественото място (§„Топ заглавията") с BG ALT + едноредов курсивен caption.
- [x] Валиден standalone SVG (xml.dom.minidom parse OK).
- [x] Layout safety: ≥16px inner padding; card x=8 w=704 (десен ръб 712, viewBox 720); най-дясната стойност завършва при x=688 (24px от ръба на картата); оценени ширини на всеки <text> с формулата chars×font×0,62 — всички се събират в контейнера с ≥8px slack; няма застъпване етикет/стойност (различни колони/редове); нищо не докосва ръба. Долен ръб на картата 434, viewBox 442 → 8px марж.
- Забележка: локален renderer (rsvg/inkscape) липсва в средата; проверката е по width-estimation формулата от step-8-images.md + XML валидация. Всички редове минават с резерв.

images total: 1 (0 hero + 1 infographic). UX cap ≤4 спазен.

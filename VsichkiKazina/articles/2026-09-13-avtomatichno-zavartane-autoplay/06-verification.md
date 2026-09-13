# 06 — Verification (vk-0061 · Автоматично завъртане / autoplay)

## Surviving flags
None. No [VERIFY], no [DATA NEEDED], no [LINK NEEDED]. No operator/НАП/tax claim. No operator
recommended, so no affiliate link required.

## Time-sensitive / factual claims + primary sources
- „autoplay = автоматични завъртания зададен брой пъти на фиксиран залог; настройки: брой, залог,
  стоп при загуба, стоп при единична печалба" — https://casinobeats.com/2021/02/11/ukgc-online-slot-measures-how-the-industry-reacted/ ,
  https://sbcnews.co.uk/igaming/2021/02/02/ukgc-bans-online-slots-autoplay-and-quickspin-features/
- Пример £1 / 50 spins / £30 loss-limit / £100 single-win-limit → conveyed in € as примерни — casinobeats.
- „UKGC забрани autoplay за UK-лицензирани слотове, срок 31.10.2021; + без завъртане <2.5 сек, без
  илюзия за контрол, без фалшиви win-звуци/картини; мотив губене на следа + най-високи средни загуби" —
  https://www.gamblingcommission.gov.uk/news/article/gambling-commission-announces-package-of-changes-which-make-online-games ,
  sbcnews (2021). Jurisdiction named: Обединено кралство (UK). Explicitly NOT presented as a BG rule.
- „autoplay не мени RTP/шанса на завъртане" — general slot math; RTP/house edge are fixed by the
  game config, independent of manual vs automatic input.

## Recalculation shown (one figure)
Твърдение: „по-бързо темпо приближава по-бързо до очакваната загуба." Проверка при примерната
настройка: залог €1 × 50 автозавъртания = €50 оборот за поредицата. При типичен слот RTP ~96%
(домашно предимство 4%) очакваната загуба върху този оборот е €50 × 0.04 = €2 средно за 50-те
завъртания. Autoplay не мени €2-та (същото домашно предимство), а само колко бързо се разиграва
оборотът: ръчно 50 завъртания отнемат минути с паузи, автоматично минават без пауза, затова средната
загуба се материализира по-бързо. (Числата €50/€2 са илюстративни за примерната настройка.)

## Gemini Step-7 (text)
- Initial draft: „Shows AI patterns, 85%" → human-likeness 15.
- Humaniser pass 1 (cut meta-commentary, fixed pause-echo, decoupled link, removed tidy-bow,
  merged/renamed headings): „Shows AI patterns, 75%" → human-likeness 25.
- Humaniser pass 2 (broke intro mirror + double-edged-sword opener, trimmed textbook over-explanation,
  removed „разликата е в" setup, disrupted A/B wrap-up): „Shows AI patterns, 75%" → human-likeness 25.
- MAX_GEMINI_PASSES (2) reached. KEPT best = pass 2 (highest-seen human-likeness 25; ties pass 1 but
  pass 2 is the stylistically cleaner state). Recorded gemini = ai 75.
- Detector floor: consistent with prior BG casino articles where Gemini pins ~75% AI regardless of
  humanisation (e.g. vk-0024). Article is genuinely de-patterned: 0 em-dashes, no signposting, no
  „не X, а Y" habit, asymmetric ending, native idioms. Flagged for the nightly humaniser/human pass
  the same way earlier articles were lifted (e.g. ai 75 → human 85/90 later).

## Step-8 Images
- images: 2 — hero (WebP, autoplay-cycle metaphor) + infographic (SVG, „Панел на автозавъртане").
- Review pass 1: score 85 PASS, 0 integrity failures; both images accurate (€1/50/€30/€100 match 05b).
  Applied the one optional fix (subtitle contrast) as polish. Best/final review score 85.
- Every infographic number traces to 05b.

## Compliance recap
Byline Георги Тодоров · brand „Всички Казина" · verbatim 18+ RG line + /otgovorna-igra/ + национален
регистър на уязвимите лица (НАП) + Солидарност линия · affiliate-licensing footer (pending, no
„issued"/no invented №) · 3 approved internal links · jurisdiction named on the UK legal claim ·
0 em-dashes · RG-forward feature guide (лимити преди старт, no FOMO, loss-chasing handled plainly).

# 00-BRIEF — Всички Казина — REFRESH (one-off 2026-10-28)

BRAND: vsichkikazina
MARKET: bg
CONTENT TYPE: guide
BYLINE: editorial voice, signed Георги Тодоров (ALWAYS — never „Екипът")
TARGET QUERY: данък печалба от хазарт
SECONDARY TERMS: данък хазарт, облагат ли се печалбите от казино, данък върху печалба от онлайн казино, данък печалба тото, данъци върху печалби от онлайн казино
LENGTH: guide, target ~1000–1300 думи (focused YMYL; never pad)

## THIS IS A REFRESH (same slug/URL by design)
- Folder = `2026-10-28-danaci-pechalbi-onlajn-kazino` → publisher re-renders the existing
  `/blog/danaci-pechalbi-onlajn-kazino/` in place. Do NOT invent a new slug.
- The live page gets **0 Google impressions in 90 days**. Root cause = targeting/intent:
  the old title („Данъци върху печалбите от онлайн казино в България") doesn't match how
  people search. Retarget to the exact query **„данък печалба от хазарт"** and the variants
  above. Answer the question in the first paragraph and the H1/title.
- dedup / anti-cannibalization are SKIPPED for this article (same URL is intended).

## TITLE / H1 / META
- Title direction: **„Данък върху печалба от хазарт и онлайн казино в България (2026)"**.
- H1 close to the title. Meta description answers the question in ONE line (напр.
  „Печалбите от лицензирано казино, тото и лотария не се облагат с данък върху дохода на
  физическото лице — решаващ е лицензът на организатора. Ето какво казва законът.").

## ANSWER-FIRST (the single most important paragraph)
The first paragraph must state the rule plainly, as a SOURCED fact (NOT flagged):
> Паричните и предметните печалби от участие в хазартни игри, организирани с лиценз, издаден
> по реда на Закона за хазарта (ЗХ) или съгласно законодателството на друга държава — членка
> на ЕС, или държава по Споразумението за ЕИП, **не са облагаем доход** за физическото лице
> по **чл. 13, ал. 1, т. 20 от ЗДДФЛ** (в сила от 01.01.2017 г.).
Решаващият фактор е **лицензът на организатора** — не размерът на печалбата и не дали играта
е онлайн или наземна.

## SOURCE (tax claim unblocked ONLY to this extent)
Primary source = `VsichkiKazina/source-packs/zddfl-gambling-winnings-2026-10-28.md`
(verbatim ЗДДФЛ чл. 13, ал. 1, т. 20 и т. 21; lex.bg consolidated text, посл. изм. ДВ бр.113/2025).
This pack **explicitly unblocks the tax claim for this article** — the normal guides-only
„0 данък claim" rule is lifted ONLY for what the pack states:
- SAFE to state as fact (cite чл. 13, ал. 1, т. 20 ЗДДФЛ):
  · печалби от хазартна игра с лиценз по ЗХ ИЛИ лиценз от друга държава от ЕС/ЕИП = необлагаем
    доход за физическото лице;
  · освобождаването е обвързано с ЛИЦЕНЗА на организатора, не с размера, не с онлайн/наземно;
  · режимът е в сила от 01.01.2017 г. (ДВ, бр. 97/2016).
  · По същата логика печалбите от **тото/лотария**, организирани от лицензиран организатор,
    попадат под същото правило (хазартни игри по ЗХ).
- MUST stay `[VERIFY]` or be OMITTED (NEVER asserted, NEVER a rate/число/праг):
  · третиране на печалби от **нелицензиран / извън ЕС/ЕИП** организатор (ставка, вид доход,
    задължение за деклариране) → `[VERIFY]` или пропусни; НИКОГА ставка;
  · каквото и да е за данъците, които плаща **организаторът** (ЗХ/ЗКПО) → пропусни;
  · банкови/AML въпроси (произход на средства) → само общо, хеджирано (без конкретни прагове).
- Загуби: по избор, САМО като кратко хеджирано изречение, насочващо към счетоводител/НАП
  (напр. „загубите по принцип не се признават за разход, който намалява данък върху друг
  доход — за конкретен случай питайте счетоводител") маркирано `[VERIFY]`; иначе пропусни.
  Не го представяй като уредено правило.

## WHAT THE LIVE PAGE HAD (reuse only what is correct + pack-consistent; restructure)
Старата страница (Георги Тодоров, 18.08.2026) казваше „данъчното задължение е на оператора,
не на играча" и цитираше „Закон за държавния бюджет 2026 (ДВ бр.69/31.07.2026)" + „афилиейт
лицензиране от 1 август 2026" + пример Betano 100% до €1500 + 150 FS (9.4/10).
→ ИЗХВЪРЛИ всичко извън пакета: НЕ твърди „операторът плаща данъка" (данъците на организатора
не са подкрепени от пакета); НЕ цитирай бюджетния закон/афилиейт лицензиране в тялото;
НЕ давай оператор/бонус пример. Запази само плоската, вярна рамка: за играча печалбата от
лицензиран организатор е необлагаема (чл.13 т.20), решаващ е лицензът.

## SECTIONS TO COVER
1. Answer-first abzац (виж горе).
2. Защо лицензът е решаващ фактор (ЗХ / ЕС/ЕИП) — линк към
   `/blog/proverka-licenz-kazino/` (как се проверява лиценз) и `/sravni-kazina/`
   (списък с лицензирани казина).
3. Тото и лотария: същото правило, щом организаторът е лицензиран.
4. Какво може да попита банката при голяма входяща сума (общо, хеджирано; AML; дръж историята
   на транзакциите и доказателство за лиценза) — без конкретни прагове.
5. (по избор, хеджирано + [VERIFY]) загубите не се приспадат.
6. Кога да питате счетоводител (професионален хазарт като основен доход; данъчна
   регистрация в друга държава; средства от организатор, лицензиран другаде).
7. FAQ: 3–4 реални въпроса, както хората търсят („Трябва ли да декларирам печалба от казино?",
   „Облагат ли се печалбите от онлайн казино?", „Плащам ли данък върху печалба от тото?",
   „Ами ако казиното не е лицензирано в България?"). Отговаряй в рамките на пакета; извън него
   → хеджирано/[VERIFY]/насочи към НАП.

Disclaimer: това не е данъчна консултация; за обвързващ отговор — НАП или счетоводител.

## INTERNAL LINKS (2–4 from approved set; aim 1 hub + 1–2 siblings)
- Hub: `/blog/regulations-taxes/`
- Siblings/trust: `/blog/proverka-licenz-kazino/`, `/zakonno-li-e/`, `/sravni-kazina/`

## SOURCES
- `VsichkiKazina/source-packs/zddfl-gambling-winnings-2026-10-28.md` (ЗДДФЛ чл.13 ал.1 т.20)
- lex.bg ЗДДФЛ consolidated (as cited in the pack)

## NOTES
- YMYL. Tone = patient teacher, plain Bulgarian, understated. Currency €, regulator НАП,
  jurisdiction България named on every legal claim.
- NEVER state a tax rate or threshold. NEVER claim the site's licence is issued.
- Standard footer: About boilerplate slot, verbatim RG line „18+ Хазартът може да пристрасти.
  Играйте отговорно." + signposting to `/otgovorna-igra/` + националния регистър на уязвимите
  лица (НАП), and the verbatim affiliate-licensing disclosure (site = заявление подадено,
  очаква издаване). No affiliate links in the body.
- ANECDOTE OPT-IN: no.

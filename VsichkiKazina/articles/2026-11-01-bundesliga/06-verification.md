# 06 — Verification (vk-0321 Бундеслига)

## Surviving flags
None. No [VERIFY] / [DATA NEEDED] in `05b`. 0 operator/НАП/affiliate facts (guides-only scope).

## Time-sensitive claims (evergreen-framed; primary sources)
All changeable figures carry „към есента на 2026 г." or route the reader to the official source;
none asserted as permanent.
- Byline club record — „Байерн Мюнхен, 34 титли от Бундеслигата (от 1963 г.)", framed „към есента
  на 2026 г.". Source: https://en.wikipedia.org/wiki/Bundesliga (34 Bundesliga titles; 35 national
  incl. pre-1963 — stated as two different measures, not a conflict).
- Европейски квоти (1–4 ШЛ, 5 ЛЕ, 6 плейоф ЛК, носител на Купата → ЛЕ) — explicitly flagged as
  коефициент-dependent → „официалният източник" for the current allocation. Source:
  https://en.wikipedia.org/wiki/Bundesliga (European qualification).
- Посещаемост „над 38 000 зрители на мач (към сезон 2024/25)" — source: EN Wikipedia attendance
  section (~38,652 avg 2024/25) + football-economy / bundesliga.com attendance explainers.
- Индивидуални рекорди: Чарли Кьорбел 602 мача, Герд Мюлер 365 гола „към есента на 2026 г." —
  source: EN Wikipedia (most appearances / top scorer).
- Formati/structural facts (18 отбора, 34 кръга, 306 мача, 3-1-0 от 1995/96, тайбрек по голова
  разлика, изпадане/бараж, 50+1 от 1998, салатиера, зимна пауза) — stable unless a rule reform.
  Sources: en.wikipedia.org/wiki/Bundesliga + bg.wikipedia.org/wiki/Бундеслига (салатиера, Кьолн).

## Recalculated figure (working shown)
Мачове за сезон = (отбори × (отбори − 1)) ÷ 2 × 2 срещи = (18 × 17) ÷ 2 × ... по-просто:
всеки от 18-те отбора играе по 34 мача (2 × 17 съперника); общо мачове = 18 × 34 ÷ 2 = **306**. ✓
Съвпада с „34 кръга и 306 мача" в текста и в инфографиката.

## Gemini Step-7 (text)
Initial draft: „Likely human-written, 85%" → human-likeness **85 = PASS** (≥80). No humaniser pass;
keep-best = initial. Style-only recs logged (07-gemini-check-1.md), not applied (would risk the
passing score). 0 facts/numbers/links/RG lines touched.
→ content-queue `gemini` = `human 85`.

## Step-8 images
2 images, both ship in the PR:
- `images/bundesliga-format.svg` — data infographic, every number traced verbatim to `05b`.
- `images/bundesliga-stadion-hero.webp` — decorative hero (21–25 KB WebP), abstract stadium, no
  text/logos/faces.
Image review: pass 1 = 75 (needs work: hero pitch-line + crowd artifacts), pass 2 = **100 PASS**
after regenerating the hero + nudging SVG labels. Keep-best = pass 2. 0 integrity failures.
→ `images: 2 (infographic 100, hero 100)`.

## Compliance snapshot
Byline Георги Тодоров ✓ · brand „Всички Казина" ✓ · dates 01.11.2026 ✓ · verbatim 18+ RG line ✓ ·
/otgovorna-igra/ + регистър ✓ · affiliate footer (pending-licence) ✓ · 0 em-dash (body) ✓ ·
4 body + 1 footer internal links (approved set) ✓ · no affiliate link (no operator) ✓.
FLAGS STAY IN TEXT: n/a (none). Human owns Step 6 + publishing.

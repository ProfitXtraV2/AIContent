# 08 — Gemini image review, pass 1

Command: `python3 scripts/gemini_image_review.py 05b-final-draft.md images/santase-karti-hero.webp images/stoynost-na-kartite-santase.svg images/tochkuvane-santase.svg`
Exit: 0

## Score: 65/100 — NEEDS WORK  (dragged down entirely by the hero; both SVGs scored perfect)

## Verbatim verdict
**Оценка: 65/100** · **Присъда: NEEDS WORK**

Специфични проблеми:
- **santase-karti-hero.webp (AI халюцинации и фактологична грешка):** боите в ъглите не съвпадат със
  символите в средата (първата карта: пика в ъгъла, сърце в средата; втората: каро в ъгъла, пика в
  средата).
- **santase-karti-hero.webp (Разминаване с текста):** в ръката са нарисувани 5 карти, докато статията
  посочва „Всеки започва с по шест карти в ръка".
- **stoynost-na-kartite-santase.svg:** Перфектна инфографика. Всички стойности отговарят точно на текста,
  няма застъпващи се елементи, цветовият контраст е отличен.
- **tochkuvane-santase.svg:** Отлична инфографика. Шнайдер (2), шварц (3) и обявяванията (20/40) са
  абсолютно точни; подравняването е безупречно.

Корекция: регенерирай хероя с точно 6 карти и консистентни бои; двете SVG — не променяй нищо.

## Decision
- Both SVGs PASS (effectively 100, "ready to publish"). No integrity failure on any image
  (no operator logo/name/screenshot, no invented bonus/RTP/licence number, no person/face, no
  glamorised winning). The hero's issues are cosmetic AI pip-garble + a 5-vs-6-cards mismatch.
- Regenerate the hero (pass 2) with a prompt that minimises pip garble (mostly clean card backs +
  one trump card) and asks for exactly six cards. Keep-best applies.

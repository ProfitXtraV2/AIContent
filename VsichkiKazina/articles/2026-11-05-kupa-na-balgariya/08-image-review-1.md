# 08 — Gemini image review — pass 1

**Score: 65/100 — Verdict: NEEDS WORK. 0 integrity failures.** (1 of MAX_IMAGE_PASSES=2 used.)

Images reviewed:
- `images/kupa-na-balgariya-format.svg` (infographic; reviewed as source so numbers are checked)
- `images/kupa-na-balgariya-trofej-hero.webp` (decorative hero; 8.2 KB, generated via gemini_image_gen.py as PNG then ImageMagick → WebP since Pillow unavailable)

Gemini's verbatim verdict:

---

**ОЦЕНКА: 65/100 — ПРИСЪДА: NEEDS WORK**

Като цяло визуалните материали са релевантни, спазват неутралния тон за отговорна игра и отговарят фактологично на текста. Растерното изображение (WebP) е отлично подготвено. Инфографиката (SVG) обаче има критичен дефект в оформлението.

1. **Нарушена цялост на лейаута (SVG) – Отрязан текст:** в дясната колона етикетът „носителят влиза в Лигата на конференциите" започва от x=556; при 14px и 43 символа излиза извън платното (card свършва на 812px) и ще се отреже.
2. **Риск от докосване на ръба (SVG):** „край на името „Купа на НР България"" (x=556, 35 символа) се долепя до десния ръб без отстояние.
3. **Растерно изображение (WebP):** няма забележки. Чисто, без забранени елементи (лица, лога, фалшив UI), правилно именуван файл, точен описателен ALT.

**Корекция:** преместете дясната колона наляво (години x=476→440, етикети x=556→500) и/или пренесете дългите текстове на два реда (<text>/<tspan>), за да се съберат в 804px картата с 15–20px отстояние. WebP: не са нужни промени.

---

**Integrity:** PASS (0 fabricated logos/numbers/screenshots, 0 faces/people, 0 glamorised winning). Score held down purely by SVG layout (text overflow). SVG numbers all trace to 05b (1, 2, 1; 1980/81, 1982/83, 1990, 2021).

**Action:** hand-fix SVG (Опция А + Б combined): moved right-column years x=476→448 and labels x=556→500; wrapped the two long labels („край на името" / „Купа на НР България"; „носителят влиза в" / „Лигата на конференциите") onto two lines; replaced the left-column em-dash with a colon. Numbers unchanged. Re-review (pass 2).

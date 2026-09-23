# 08 — Gemini image review, pass 1

Model: gemini multimodal · images reviewed: bf-games-rtp.svg (source + rendered), bf-games-book-hero.webp (pixels).

**SCORE: 75/100 · VERDICT: NEEDS WORK**

Single defect: layout — the long footer line at `y="341"` of the SVG („Част от заглавията имат няколко версии с различен RTP (напр. Magic Hunter 94.19%–98.14%) · операторът избира коя да пусне", 120+ chars) overflows the 640px canvas and would clip at the edges. Layout defect = automatic NEEDS WORK even at otherwise-passing quality.

No integrity failures: data accuracy PERFECT (every RTP/title matches 05b exactly); hero WebP „безупречно" — concept-relevant, no fake logos, no faces, no glamorised winning, correct filename + ALT. Only the SVG layout needs a hand-fix.

Fix (applied at pass 2): split the long footer line into two lines; extend the canvas height for a comfortable bottom margin; move the 18+ line down. Numbers unchanged (still trace to 05b).

## Gemini verbatim verdict

**SCORE: 75/100 · VERDICT: NEEDS WORK**

1. Нарушена цялост на лейаута (SVG инфографика) – Изрязан текст. Текстът на предпоследния ред (y="341") е твърде дълъг за ширината на платното (120+ символа при font-size 11, центриран на x=320) → ще надхвърли 640px и ще бъде отрязан. Нарушава правилото за липса на изрязани елементи.
2. Растерно изображение (WebP) – Отлична работа. Концептуално релевантно, без фалшиви лога, без лица, не глорифицира хазарта, перфектни SEO метаданни.
3. Точност на данните (SVG) – Отлична работа. Всички числа/проценти/имена съвпадат точно със статията. Няма измислени данни.

Корекция: раздели дългия ред на два (y≈338 и y≈352), свали 18+ реда по-надолу (y≈366), увеличи height от 372 на ~385.

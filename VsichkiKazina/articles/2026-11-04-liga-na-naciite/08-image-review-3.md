# 08 — Gemini image review — pass 3 (MAX_IMAGE_PASSES cap) + hero regeneration

## Combined review (SVG + hero), after SVG fix pass 2
**Score: 65/100 — NEEDS WORK.**
- **SVG infographic: APPROVED / PERFECT.** Verbatim: „Няма открити проблеми. Всички числа (55 отбора,
  4 дивизии, 16/16/16/7 разпределение, 3-1-0 точки, шампиони и години) отговарят абсолютно точно…
  Няма припокриващ се текст, излизане извън платното или проблеми с контраста… Одобрен е за директно
  ползване." → SVG is final, best state, 0 integrity issues.
- **HERO raster: INTEGRITY FAIL.** The illustration showed stylised crowd silhouettes (heads/shoulders
  in the stands). Any depiction of human figures is an automatic reject under RG image hygiene. Root
  cause: the first hero prompt asked for „пълни трибуни" (full stands) AND „без хора" (no people) — a
  contradiction the model resolved by drawing a crowd.

## Action — hero regenerated (hero fix pass 1)
Deleted the crowd hero; regenerated with a corrected prompt: EMPTY stadium at night, abstract empty
seats + floodlights, explicitly no people/crowd/silhouettes/faces. Converted PNG→WebP via ImageMagick
(Pillow unavailable), 23 KB.

## Re-review (hero alone)
**Score: 85 — PASS.** 0 integrity: „It is clean, relevant, technically sound, and perfectly adheres to
the neutral, responsible gambling tone… no changes needed to the image file." Remaining note was only
about the ALT text (it still said „пълни трибуни" + prompt-artifact negatives) → ALT updated in `05b`
to „Плоска илюстрация на празен футболен стадион вечер, осветен от прожектори в хладни сини и тъмни
тонове" (describes the empty stadium; no negative-constraint artifacts).

## Final image state — KEEP-BEST
- `liga-na-naciite-format.svg` — infographic, APPROVED, every number traced verbatim to 05b, 0 integrity.
- `liga-na-naciite-hero.webp` — decorative empty-stadium hero, **85 PASS**, 0 integrity, 23 KB WebP.
images: 2 (infographic approved/accurate, hero 85). Both ship in the SAME content PR.

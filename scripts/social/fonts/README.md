# Fonts for social images

The Всички Казина site fonts (WebPortals `VsichkiKazina/assets/fonts/`), as full variable TTFs
that hold both Latin and Cyrillic, so Pillow can set mixed text such as „Банко 1:1“ exactly (C3).

| File | Font | Source | Licence |
|---|---|---|---|
| `Onest-Variable.ttf` | Onest (wght) | github.com/google/fonts, `ofl/onest/Onest[wght].ttf` | SIL Open Font License 1.1 (`Onest-OFL.txt`) |
| `Literata-Variable.ttf` | Literata (opsz, wght) | github.com/google/fonts, `ofl/literata/Literata[opsz,wght].ttf` | SIL Open Font License 1.1 (`Literata-OFL.txt`) |

DentalVia uses Noto Sans until its brand fonts are named; until that file is added here,
`compose.py` falls back to Onest, which covers German.

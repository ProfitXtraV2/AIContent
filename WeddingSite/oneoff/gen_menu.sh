#!/usr/bin/env bash
# One-off: three menu illustrations for the RSVP form (meat / vegetarian / vegan), on white for cut-out.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-menu; mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
STYLE='Painted in Indian-miniature-meets-European gouache style with delicate gold-leaf linework and hand-painted texture, soft muted elegant palette (peach, blush, champagne gold, sage and emerald greens, warm browns), matching a high-end illustrated wedding stationery suite. A single elegant fine-dining plate seen from a 3/4 top angle: a round white porcelain plate with a thin gold rim. Isolated and centred on a perfectly flat pure white (#FFFFFF) background, no shadow on the background, nothing else in the frame, no cutlery, no text, no letters. The plate fills about 80% of the frame. Square 1:1.'
run () { echo "== $1" >> "$LOG"; ASPECT=1:1 python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 300 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run meat "On the plate: an elegantly plated tender beef medallion steak with a glossy jus, a few roasted baby potatoes and a sprig of rosemary. $STYLE"
run vegetarian "On the plate: an elegantly plated vegetarian dish, a delicate ricotta and spinach ravioli with shaved parmesan, a few cherry tomatoes and fresh basil leaves. $STYLE"
run vegan "On the plate: an elegantly plated vegan dish, a colourful garden salad bowl-style arrangement of roasted vegetables, chickpeas, avocado slices, quinoa and fresh herbs. $STYLE"
cat "$LOG"

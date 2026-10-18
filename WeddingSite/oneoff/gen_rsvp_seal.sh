#!/usr/bin/env bash
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-rsvp; mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
SEAL='Product photograph, shot straight from directly above, of ONE single round wax seal stamp, centred, on a perfectly flat pure white (#FFFFFF) background with no shadow on the background. Deep burgundy / wine-red glossy sealing wax with soft specular highlights, an organic irregular melted-wax outer edge, a thin raised decorative ring near the rim with a delicate wreath of small leaves and tiny rosebuds. The centre is a smooth, slightly recessed EMPTY disc: absolutely NO letters, NO text, NO monogram, NO symbols in the centre. The seal fills about 70% of the frame width. Square 1:1, ultra detailed, photorealistic.'
run () { echo "== $1" >> "$LOG"; ASPECT=1:1 python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 500 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run rsvp-a "$SEAL"
run rsvp-b "$SEAL Slightly richer, darker wine colour and a more pronounced rim."
cat "$LOG"

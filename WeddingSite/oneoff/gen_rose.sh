#!/usr/bin/env bash
# One-off: a single rose bloom (for the scroll-linked schedule timeline), on white for cut-out.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-rose
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
BASE='A single blush-pink garden rose bloom seen from slightly above (three-quarter view), with two small green leaves, painted in Indian-miniature-meets-European gouache style with delicate gold-leaf linework and hand-painted texture, soft muted blush and dusty-rose petals with cream highlights, matching a high-end illustrated wedding stationery suite. Isolated and centred on a perfectly flat pure white (#FFFFFF) background with no shadow and nothing else. The bloom fills about 70% of the frame. No text, no stem beyond a short piece, no vase, no frame.'
run () { echo "== $1" >> "$LOG"; ASPECT=1:1 python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 400 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run rose-a "$BASE"
run rose-b "$BASE A slightly more open bloom, petals curling outward."
cat "$LOG"

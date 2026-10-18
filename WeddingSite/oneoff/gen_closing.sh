#!/usr/bin/env bash
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-closing; mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
BASE='Wide landscape 3:2 closing vignette for the bottom of a luxury wedding invitation website, painted in the SAME style as the attached-style suite: Indian-miniature-meets-European gouache with fine gold-leaf linework and hand-painted texture, soft muted palette of peach, apricot, champagne gold and blush with a few jewel accents (soft teal water, emerald foliage, rose pink). Scene: on the left the calm Black Sea of Burgas with a slender lighthouse and a small sailboat; on the right the soft blue silhouette of Vitosha mountain with the small golden domes of Alexander Nevsky cathedral below it; in the centre foreground two pink flamingos facing each other, their necks gently forming a heart shape, standing in shallow water among pink Bulgarian roses and reeds. Golden-hour light. The vignette is an oval-ish cloud shape with NO hard border: all edges, especially top and bottom, fade softly into plain warm cream paper colour (#FBEEE3). No text, no letters, no people, no frame.'
run () { echo "== $1" >> "$LOG"; ASPECT=3:2 python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 400 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run closing-a "$BASE"
run closing-b "$BASE More delicate and airy, smaller elements with more empty cream space around them."
cat "$LOG"

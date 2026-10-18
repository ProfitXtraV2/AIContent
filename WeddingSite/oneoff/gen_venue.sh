#!/usr/bin/env bash
# One-off: venue vignette (Terra Residence gardens) for the WeddingSite venue section.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-venue
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"

BASE='Portrait 4:5 vignette illustration for a luxury wedding invitation website, painted in the SAME style as an Indian-miniature-meets-European gouache wedding stationery suite: fine gold-leaf linework, hand-painted texture, soft muted palette of peach, apricot, champagne gold and blush with a few rich accents (emerald green foliage, rose pink flowers, soft teal water). Subject: the romantic gardens of an elegant white neoclassical event residence in Sofia at golden hour: in the centre a tiered stone fountain with gently falling water surrounded by pink roses and clipped boxwood; behind it an arched pergola tunnel covered in climbing greenery and woven with warm glowing string lights; to one side a calm rectangular reflecting water pool framed by stone arches with climbing plants and a few palms; the pale facade of the residence with tall French windows glowing warmly; the soft blue silhouette of Vitosha mountain in the far background under a peach sky. The vignette has NO hard border: all edges fade softly into plain peach paper colour (#F6D5B9). No text, no letters, no people, no frame.'

run () { echo "== $1" >> "$LOG"; ASPECT=4:5 python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 500 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run venue-a "$BASE"
run venue-b "$BASE Composition: the fountain and the string-light pergola tunnel are the clear focal point in the centre, symmetrical, seen slightly from above."
cat "$LOG"

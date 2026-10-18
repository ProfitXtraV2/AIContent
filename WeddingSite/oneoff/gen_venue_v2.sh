#!/usr/bin/env bash
# One-off: venue vignette v2, repainting the REAL Terra Residence courtyard from reference photos.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-venue-v2
REF=WeddingSite/oneoff/ref
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"

BASE='The attached photos show the real courtyard (the "English Court") of Terra Residence in Sofia, where our wedding ceremony will be. Repaint THIS EXACT place as a portrait 4:5 vignette illustration for our luxury wedding invitation website. Keep the architecture and layout faithful to the photos: the long curved white parapet wall with a row of tall dark navy-blue arched mirror-windows with fine black glazing bars; lush climbing vines (wisteria-like) growing up between every window; strings of warm glowing festoon bulbs zig-zagging across the whole courtyard; the stepped, L-shaped two-level pool lined with dark blue-grey mosaic tiles and turquoise water; potted fan palms, agaves and cycads in woven and terracotta pots around the pool; grey cobblestone paving; tall green trees behind the wall. For the wedding, add a circular floral ring arch (white and blush roses with pale blue hydrangeas) standing on the cobblestones, with a few short rows of gold chiavari chairs facing it, like in the second photo. Elevated three-quarter view from above, as in the photos. Golden-hour light with the bulbs glowing warmly. STYLE: Indian-miniature-meets-European gouache painting with fine gold-leaf linework and hand-painted texture, matching a high-end illustrated wedding stationery suite; soft muted palette harmonised to peach, apricot, champagne gold and blush, with emerald foliage, navy windows and teal water as the accents. The vignette has NO hard border: all edges fade softly into plain peach paper colour (#F6D5B9). No people, no text, no letters, no frame.'

run () { echo "== $1" >> "$LOG"; ASPECT="$3" python3 WeddingSite/oneoff/gen_from_ref.py "$2" "$OUT/$1.webp" "$REF/court.jpg" "$REF/ceremony.jpg" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run venue2-a "$BASE" 4:5
run venue2-b "$BASE Frame it slightly closer: the curved wall of arched mirror-windows fills the upper half, the pool and the floral ring arch with chairs fill the lower half." 4:5
run venue2-c "$BASE" 1:1
cat "$LOG"

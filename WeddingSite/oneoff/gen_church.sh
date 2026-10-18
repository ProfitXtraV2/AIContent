#!/usr/bin/env bash
# One-off: St. Nedelya Cathedral (Sofia) vignette from reference photos (Wikimedia Commons, public domain / CC).
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-church; REF=WeddingSite/oneoff/ref
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
BASE='The attached photos show the real St. Nedelya Cathedral (Sveta Nedelya) in the centre of Sofia, where our church wedding ceremony will be. Repaint THIS EXACT building as a portrait 4:5 vignette illustration for our luxury wedding invitation website. Keep the architecture faithful: warm honey-beige stone neo-Byzantine church, the large central drum with a ring of tall arched windows topped by a soft green copper dome with a gold cross, the round rose window on the facade, the arcaded entrance portico with slender white columns and round arches, the smaller side dome. Remove all cars, signs, kiosks and people. Frame it romantically for a wedding: the weeping willow and leafy trees beside it in fresh early-summer green, a few garlands of white and blush roses on the portico, soft rose petals on the paved square, warm golden-hour light, a peach sky. STYLE: Indian-miniature-meets-European gouache painting with fine gold-leaf linework and hand-painted texture, matching a high-end illustrated wedding stationery suite; soft muted palette harmonised to peach, apricot, champagne gold and blush, with emerald foliage and the green-copper dome as accents. The vignette has NO hard border: all edges fade softly into plain peach paper colour (#F6D5B9). No people, no text, no letters, no frame.'
run () { echo "== $1" >> "$LOG"; ASPECT=4:5 python3 WeddingSite/oneoff/gen_from_ref.py "$2" "$OUT/$1.webp" "$REF/church1.jpg" "$REF/church2.jpg" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run church-a "$BASE"
run church-b "$BASE Slightly closer, three-quarter view from the front-left as in the first photo, the dome and portico clearly the focal point."
cat "$LOG"

#!/usr/bin/env bash
# One-off: hero background variants for the WeddingSite second screen ("Sofia meets Burgas").
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-hero
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"

BASE='Vertical 9:16 illustration for a luxury wedding invitation website. Style: Indian-miniature-meets-European gouache painting with fine gold-leaf linework and hand-painted texture, like a high-end illustrated wedding stationery suite. Palette: soft muted peach, apricot, champagne gold and blush, with only a few rich jewel accents (deep teal-blue, rose pink, emerald). COMPOSITION IS CRITICAL: the TOP 50% of the image is an EMPTY, soft, warm peach-to-apricot sky gradient with absolutely nothing in it (no birds, no clouds, no objects) because text will be placed there. The illustration occupies ONLY the BOTTOM half of the image. Scene, painted as one harmonious vignette: on the left, the golden onion domes of the Alexander Nevsky Cathedral of Sofia (neo-Byzantine, gilded domes, pale stone), with the soft blue silhouette of Vitosha mountain behind; on the right, a slender lighthouse and the long wooden sea bridge (pier) of Burgas stretching over calm Black Sea water with a small sailboat; in the foreground, a pair of elegant pink flamingos and one white pelican, lush pink Bulgarian damask roses, pine branches and reeds framing both edges. Delicate gold ornamental details. The very bottom of the image fades softly into plain peach paper colour. No text, no letters, no words, no people, no frame, no border.'

run () { echo "== $1" >> "$LOG"; python3 WeddingSite/oneoff/gen_hero.py "$2" "$OUT/$1.webp" 700 >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run hero-a "$BASE"
run hero-b "$BASE Make the composition more symmetrical: the cathedral domes centred, the mountain softly behind them, the sea bridge and lighthouse to the right, the flamingos to the left."
run hero-c "$BASE Make the flamingos and roses more prominent in the foreground, slightly richer jewel accents, more gold leaf on the domes."
cat "$LOG"

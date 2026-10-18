#!/usr/bin/env bash
# One-off: generate envelope-phase assets for the WeddingSite project via Gemini.
# Outputs to WeddingSite/oneoff/out/ ; log to WeddingSite/oneoff/out/log.txt
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out
mkdir -p "$OUT"
LOG="$OUT/log.txt"; : > "$LOG"

PAPER='Top-down macro photograph of a single sheet of luxurious thick blush-pink cotton paper (colour approximately #F2D6CF) filling the ENTIRE frame edge to edge. The paper carries a dense, elegant BLIND-EMBOSSED tropical pattern: tall palm trees, palm fronds, monstera leaves, hibiscus and frangipani flowers, scallop seashells and starfish, all raised in relief in exactly the same pink tone as the paper (no ink, no print, no colour differences, only relief with soft natural shadows and highlights). Even soft diffused daylight, no vignette, no borders, no envelope edges, no objects, no text, no letters. Portrait orientation, 2:3 aspect ratio, ultra detailed, photorealistic stationery texture.'

SEAL='Product photograph, shot straight from directly above, of ONE single round wax seal stamp, centred in the frame, on a perfectly flat pure white (#FFFFFF) background with no shadow on the background. Realistic metallic antique-gold wax with soft specular highlights, an organic irregular melted-wax outer edge, a raised engraved ring near the rim decorated with a small wreath of tropical flowers (hibiscus, frangipani) and leaves. The centre of the seal is a smooth, slightly recessed EMPTY disc: absolutely NO letters, NO monogram, NO initials, NO text, NO symbols in the centre. The seal fills about 70% of the frame width. Square 1:1, ultra detailed, photorealistic.'

run () { # name prompt out maxkb
  echo "== $1" >> "$LOG"
  python3 scripts/gemini_image_gen.py "$2" "$3" "$4" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"
}
run paper-a "$PAPER" "$OUT/paper-a.webp" 450
run paper-b "$PAPER Slightly finer, more delicate pattern scale." "$OUT/paper-b.webp" 450
run seal-a  "$SEAL" "$OUT/seal-a.png" 3000
run seal-b  "$SEAL Warmer rose-gold tint, slightly glossier wax." "$OUT/seal-b.png" 3000
cat "$LOG"

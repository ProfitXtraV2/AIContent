#!/usr/bin/env bash
# One-off v2: personalised envelope paper (Burgas sea + Vitosha mountain + Sofia city + IT)
# and a matching wax-seal wreath. Outputs to WeddingSite/oneoff/out-v2/
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-v2
mkdir -p "$OUT"
LOG="$OUT/log.txt"; : > "$LOG"

BASE='Top-down macro photograph of a single sheet of luxurious thick blush-pink cotton paper (colour approximately #F2D6CF) filling the ENTIRE frame edge to edge. The paper carries a dense, elegant BLIND-EMBOSSED pattern, every motif raised in relief in exactly the same pink tone as the paper (no ink, no print, no colour differences, only relief with soft natural shadows and highlights). Motifs, evenly scattered and mixed together, roughly equal amounts of each group: SEA (gentle ocean waves, a lighthouse, a small sailboat, seagulls, scallop seashells, a starfish, an anchor); MOUNTAIN (layered mountain peaks with snow caps, pine and fir trees, a small hiking trail); CITY (an Orthodox cathedral with golden-dome silhouette, a classic city skyline with small buildings, a vintage tram); TECH (a laptop, a computer mouse, curly braces and angle-bracket code symbols, a circuit-board trace pattern, a Wi-Fi symbol, a small heart made of circuit lines). Hand-drawn engraving style, consistent line weight, romantic and elegant, not cartoonish. Even soft diffused daylight, no vignette, no borders, no envelope edges, no objects on top, no words, no letters, no readable text. Portrait orientation, 2:3 aspect ratio, ultra detailed, photorealistic stationery texture.'

SEAL='Product photograph, shot straight from directly above, of ONE single round wax seal stamp, centred in the frame, on a perfectly flat pure white (#FFFFFF) background with no shadow on the background. Realistic metallic antique-gold wax with soft specular highlights, an organic irregular melted-wax outer edge, a raised engraved decorative ring near the rim forming a continuous wreath that blends: small ocean waves and a tiny seashell on the bottom half, small mountain peaks and pine sprigs on the top half, joined by delicate leaves. The centre of the seal is a smooth, slightly recessed, DARKER matte EMPTY disc: absolutely NO letters, NO monogram, NO initials, NO text, NO symbols in the centre. The seal fills about 70% of the frame width. Square 1:1, ultra detailed, photorealistic.'

run () { # name prompt out maxkb
  echo "== $1" >> "$LOG"
  python3 scripts/gemini_image_gen.py "$2" "$3" "$4" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"
}
run paper-a "$BASE" "$OUT/paper-a.webp" 450
run paper-b "$BASE Slightly finer, more delicate pattern scale with more motifs." "$OUT/paper-b.webp" 450
run paper-c "$BASE Arrange the motifs as gentle flowing bands: sea waves flowing into mountains flowing into the city skyline, with tech symbols sprinkled between." "$OUT/paper-c.webp" 450
run seal-a  "$SEAL" "$OUT/seal-a.png" 3000
run seal-b  "$SEAL Slightly more detailed and deeper engraving on the wreath." "$OUT/seal-b.png" 3000
cat "$LOG"

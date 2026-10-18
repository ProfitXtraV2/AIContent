#!/usr/bin/env bash
# One-off: thank-you portrait v2 — scene of us-a, groom shirtless in suit trousers, faces closer to the photo.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-us2; REF=WeddingSite/oneoff/ref
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
P='Attached: (1) a real photo of us, the couple getting married, (2) a close crop of our faces from that photo, (3) an illustration whose scene, composition and style we love. Repaint illustration (3) keeping its scene, composition, style, colours and all props (the wooden sea bridge of Burgas over the Black Sea at golden hour, the lighthouse and gulls behind, the groom carrying the laughing bride in his arms, the bride raising a small two-tier homemade wedding cake with pink roses, the kettlebell tied with a silk ribbon and the bunch of peonies on the boards), with these changes: FACES: make both faces much closer to the real people in photos (1) and (2). Georgi: short dark-brown hair, faded short on the sides and slightly longer, textured and swept up on top; a full, neatly trimmed dark beard with a clean cheek line; thick straight dark eyebrows; dark brown eyes; strong straight nose; calm confident slight smile. Marina: oval face, high cheekbones, dark-brown hair pulled back in a sleek high ponytail, softly arched dark eyebrows, brown eyes, natural warm smile, light freckles; she keeps her white wedding gown and veil. GROOM OUTFIT: Georgi is a muscular CrossFit athlete: SHIRTLESS, showing a strong athletic CrossFit physique (broad shoulders, defined chest, arms and abs, tasteful, not exaggerated), wearing tailored charcoal-black suit trousers with a belt and black weightlifting shoes; no logos, no lettering. Keep it elegant and joyful, suitable for a wedding invitation. Portrait 4:5, all edges fade softly into warm cream paper (#FBEEE3). No text, no frame.'
run () { echo "== $1" >> "$LOG"; ASPECT=4:5 python3 WeddingSite/oneoff/gen_from_ref.py "$2" "$OUT/$1.webp" "$REF/us.jpg" "$REF/us-faces.jpg" "$REF/us-a.jpg" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run us2-a "$P"
run us2-b "$P"
run us2-c "$P Paint it with a little more gold-leaf linework and a warmer peach palette."
cat "$LOG"

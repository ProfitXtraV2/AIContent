#!/usr/bin/env bash
# One-off: thank-you portrait v3 — us2-c with both smiling like us2-a, plus jewellery/watch/shoe details.
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-us3; REF=WeddingSite/oneoff/ref
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
P='Attached: (1) the illustration to edit, (2) a second version of it whose SMILES we love, (3) a close crop of our real faces. Edit illustration (1) and keep EVERYTHING the same (scene, composition, style, warm palette, poses, the wooden sea bridge, lighthouse, gulls, cake, kettlebell with ribbon, peonies, his black suit trousers and belt, her gown and veil, the faces resembling photo (3)) with ONLY these changes: (a) both of us smile exactly like in illustration (2): the groom with a big, warm, open smile showing his teeth, the bride laughing joyfully with an open smile; (b) the groom wears a luxury Rolex-style wristwatch with a gold-and-steel bracelet and round dial on his left wrist, clearly visible on the arm holding her; (c) the bride wears a sparkling diamond tennis necklace and a matching diamond tennis bracelet; (d) the groom wears black weightlifting shoes (lifting shoes with a raised solid heel and a velcro strap) with the word "ROGUE" written in small white capital letters on the side of each shoe. Portrait 4:5, edges fading softly into warm cream paper (#FBEEE3). No other text, no frame.'
run () { echo "== $1" >> "$LOG"; ASPECT=4:5 python3 WeddingSite/oneoff/gen_from_ref.py "$P" "$OUT/$1.webp" "$REF/us2-c.jpg" "$REF/us2-a.jpg" "$REF/us-faces.jpg" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run us3-a; run us3-b; run us3-c
cat "$LOG"

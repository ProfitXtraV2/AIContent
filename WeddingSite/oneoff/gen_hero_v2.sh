#!/usr/bin/env bash
# One-off: hero variant with a smaller cathedral and a bigger lighthouse (so the couple on the pier reads better).
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=WeddingSite/oneoff/out-hero-v2; REF=WeddingSite/oneoff/ref
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
BASE='Edit the attached illustration (the hero painting of our wedding invitation). Keep EVERYTHING else exactly the same: the gouache + gold-leaf style, the peach palette, the empty peach sky in the top half, Vitosha mountain, the two pine trees in the top corners, the flamingos, the pelican, the roses and reeds, the sailboat, the gold ornament at the bottom and the soft fade into peach at the bottom edge. ONLY change two things: 1) make the Alexander Nevsky cathedral about 25% smaller, still centred on its little sandy island in the same spot, so more of the sea and the mountain shows around it; 2) make the lighthouse on the right about 45% bigger (taller and wider), standing on its rocks at the start of the wooden pier, with a clearly visible arched door at pier level, and make the near part of the pier where it meets the lighthouse a little wider and more visible. Same 9:16 framing. No people, no text.'
run () { echo "== $1" >> "$LOG"; ASPECT=9:16 python3 WeddingSite/oneoff/gen_from_ref.py "$2" "$OUT/$1.webp" "$REF/hero.jpg" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run hero-v2-a "$BASE"
run hero-v2-b "$BASE Make the change a little stronger: cathedral about 30% smaller, lighthouse about 60% bigger."
cat "$LOG"

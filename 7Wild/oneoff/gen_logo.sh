#!/usr/bin/env bash
# One-off: 7WILD logo set (Street Slang wordmark). Style reference: ref/logo-ref.jpg (owner's example).
set -u
cd "$(git rev-parse --show-toplevel)"
OUT=7Wild/oneoff/out-logo; REF=7Wild/oneoff/ref/logo-ref.jpg
mkdir -p "$OUT"; LOG="$OUT/log.txt"; : > "$LOG"
BASE='The attached image is the brand owner'"'"'s sketch of the 7WILD logo. Redraw it as a clean, final, professional logo. It must read EXACTLY: 7WILD. (the digit 7, then the capital letters W, I, L, D, then a round full stop). Letterforms: ultra-heavy, chunky, slightly bouncy display lettering with a playful, hand-cut street feel: letters lean and bob a little off a straight baseline, soft rounded corners, tight spacing, the 7 has a flared top bar and a curved, tapering stem like a brush-cut 7. The full stop is a perfect solid circle. Perfectly flat vector style: solid fills only, crisp clean edges, no gradients, no shadows, no outlines, no texture, no 3D, no mockup, no extra words, no tagline.'
run () { echo "== $1" >> "$LOG"; ASPECT="$2" python3 7Wild/oneoff/gen_from_ref.py "$3" "$OUT/$1.webp" "$REF" >> "$LOG" 2>&1; echo "exit=$?" >> "$LOG"; }
run wordmark-black-a 16:9 "$BASE Colours: letters solid near-black #111111, the full stop solid orange #FF5A1F, on a plain flat cream background #F3EEE4. The logo is centred with generous empty margin all around."
run wordmark-black-b 16:9 "$BASE Make the bounce slightly stronger and the letters a touch rounder, like a premium skate or streetwear label. Colours: letters solid near-black #111111, the full stop solid orange #FF5A1F, on a plain flat cream background #F3EEE4. Centred with generous margin."
run wordmark-cream 16:9 "$BASE Colours: letters solid cream #F3EEE4, the full stop solid orange #FF5A1F, on a plain flat near-black background #111111. Centred with generous margin."
run wordmark-on-orange 16:9 "$BASE Colours: letters solid near-black #111111, the full stop solid cream #F3EEE4, on a plain flat orange background #FF5A1F. Centred with generous margin."
run icon-7 1:1 "Using the same lettering style as the 7 in the attached sketch (ultra-heavy, flared top bar, curved tapering brush-cut stem), draw an app icon: a single bold near-black #111111 digit 7 centred on a solid orange #FF5A1F rounded square (iOS app icon shape, about 22% corner radius) that fills the frame edge to edge, with a small solid cream #F3EEE4 circle as a full stop at the lower right of the 7. Perfectly flat vector, no gradient, no shadow, no texture, no other text."
run stacked 1:1 "$BASE Layout: STACKED lockup, a very large 7 on top and the word WILD. underneath, centred, the 7 about as wide as WILD. Colours: near-black #111111 letters, orange #FF5A1F full stop, on flat cream #F3EEE4. Centred with generous margin."
cat "$LOG"

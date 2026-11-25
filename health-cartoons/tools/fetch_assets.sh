#!/usr/bin/env bash
# Downloads the shared font, music and sound effects into health-cartoons/assets (git-ignored).
# All Mixkit items are under the Mixkit free licence; Luckiest Guy is SIL OFL (Google Fonts).
set -e
cd "$(dirname "$0")/../assets"
mkdir -p fonts sfx music
UA="Mozilla/5.0 (X11; Linux) AppleWebKit/537.36 Chrome/120 Safari/537.36"
if [ ! -s fonts/LuckiestGuy.woff2 ]; then
  url=$(curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=Luckiest+Guy" | awk '/\/\* latin \*\//{f=1} f&&/src:/{print; exit}' | grep -oE "https://[^)]+")
  curl -s -o fonts/LuckiestGuy.woff2 "$url"
fi
# 009 fonts (SIL Open Font License): Comic Neue for labels, Merriweather Black for captions
[ -s fonts/comic-neue-latin-700-normal.woff2 ] || curl -s -o fonts/comic-neue-latin-700-normal.woff2 https://cdn.jsdelivr.net/npm/@fontsource/comic-neue@5.0.8/files/comic-neue-latin-700-normal.woff2
[ -s fonts/merriweather-latin-900-normal.woff2 ] || curl -s -o fonts/merriweather-latin-900-normal.woff2 https://cdn.jsdelivr.net/npm/@fontsource/merriweather@5.0.8/files/merriweather-latin-900-normal.woff2
# music: Mixkit track id 9 ("Keep Smiling" family, light comedic) - the channel's bed
[ -s music/mixkit-9.mp3 ] || curl -s -o music/mixkit-9.mp3 https://assets.mixkit.co/music/9/9.mp3
# music: Mixkit track id 508 ("Jazz 2": double bass, cello, strings, piano) - the closest measured match to the sleeping-pills reference bed (023)
[ -s music/mixkit-508.mp3 ] || curl -s -o music/mixkit-508.mp3 https://assets.mixkit.co/music/508/508.mp3
# sound effects (Mixkit sfx ids) - see the verified table in PLAYBOOK.md section 3 (titles checked; several old ids are NOT what their old names said)
for id in 92 110 123 324 343 391 473 527 1317 1486 1492 1714 1886 1889 2151 2209 2457 2480 2833 2837 2873 2882 2886 2894 2925 2999 3050 1351 616 3024 2364 2936 414 \
          1060 1789 2268 988 1311 3005 2357 2354 2358 1107 933 951 1464 175 772 2895 2890 2889 2149 3082 2359 746 395 2945 2182 2835 1884 2832 2828 3181 1321 732 3207 2920 1871 2813 2980 1838 2256 937; do
  [ -s sfx/$id.mp3 ] || curl -s -o sfx/$id.mp3 "https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3"
done
ls -la fonts music sfx | head -40

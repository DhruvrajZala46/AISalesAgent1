# Stage 4 - Thumbnails

The thumbnail is half the click. It must look like OUR thumbnails (measured, below), carry words
the title doesn't use, and show real women, never AI.

Read first: the `yt-package` skill (title and thumbnail are one unit).

## The channel's thumbnail DNA (measured from "8 Things Elegant Ladies Never Wear", 1.24M views)

| Part | Exact value |
|---|---|
| Canvas | 1280x720 |
| Photos | 3 real women edge to edge: x 0-401, 403-850, 852-1280, thin light dividers |
| Framing | close, waist-up, faces in the top third, looking natural; different ages and skin tones |
| Grade | slightly warm, slightly darker, gentle contrast |
| Top line | Cormorant SC Regular, cap height 46 px, top at y=200, white |
| Headline | Montserrat Bold 700, cap height 108 px, top at y=296, white |
| Underline | red (150,22,26), under the FIRST headline word, y=418-421 (below any descender) |
| Small line | Cormorant SC, cap height 26 px, top at y=495, like `*avoid these*` |
| Depth | soft drop shadow on all text, gentle darkening behind the text block |
| Logo | CE logo top-left |

For a do / don't topic (rules, mistakes), the winners' format is the same woman twice, red cross on the
mistake and green tick on the fix (8.0M "Dressing Rules EVERYONE Should Learn"): `tools/thumb_xo.py` builds it
in our look from two frames of ONE creator's own before/after video (never put a cross on a woman who did not
present that look as a mistake herself). It erases a burned-in caption line and cuts her out (rembg).

For a body-shape / fit / proportion topic, the winners add **lines drawn on her body** (42 body-shape winners: same
woman mistake -> fix 67.5x her channel's median, same woman + lines on her 56.8x and 1.84M median views, shape icons
14.0x; `videos/body-shape/THUMBNAIL.md`): `tools/thumb_shape.py spec.json` builds it - our look, ✗/✓, dashed lines and
small white labels placed in canvas coordinates (render once with `"grid": true` to read them). Draw only what the
woman shows or explains herself. Frame above a burned-in caption rather than erasing it over a bag or a pattern.

`tools/thumb_spec.py spec.json` is the same look with each panel framed by hand (face box, face height, offset), so a body or
outfit topic keeps the waist and the styling below the words; it also writes an editable SVG with live text and the graded
panels as PNGs. The red underline is used only in her "Elegant Ladies Never..." series (`"underline": false` otherwise),
measured on all 31 thumbnails (`videos/tummy/THUMBNAIL.md`).

`tools/thumb_make.py` builds exactly this (it reproduces the approved French thumbnail pixel for
pixel). Never change the layout to "try something new" without the user asking.

## Words

- Headline 2-3 words, max 3 words in the big line; together with the top line it reads as one
  phrase ("French Women / Never Wear").
- It must not repeat the title's words where it can avoid it - different words, same promise
  (`python3 .claude/skills/yt-package/title.py --title "<title>" --thumb "<big words>"`).
- Make three versions: the channel's #1 format, a variant with other words, and an "at any age"
  (40-70+) version.

## Photos - real, named, verified

```bash
cd <scratchpad>/<slug>-thumb; T=/home/user/AISalesAgent1/classy-academy-test/workflow/tools
python3 $T/real_search.py tag="search words" tag2="..."   # drops AI sizes / AI words / small images -> real/keep.json + sheet
python3 $T/crop.py key1 key2 ...                          # crops.jpg: each photo framed like the channel
python3 $T/thumb_make.py T1.jpg "Top Line" "Big Words" "*small line*" key1 key2 key3
```

Every photo is checked by eye before use:
- real photography (skin texture, real hands, real background text), not AI;
- from a real source (the person's own account, a magazine, a known photographer), not a content
  farm (`zentrosy`-type pins were AI);
- the woman matches the promise (e.g. a real, well-known woman of that style for a culture topic;
  women 40-70+ for the "any age" version);
- sharp at 427x720.
Write each photo's source and creator in the package credits.

## Test at feed size

Make a sheet with the three candidates at 320x180 next to 6 real competitor thumbnails from the
same search. The headline must read in one glance and the faces must still be clear.

## Hand back

The three thumbnails (send the files), the photo sources, and which one is recommended and why.
Last line: **ship it, or change it?**

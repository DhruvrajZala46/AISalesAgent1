# Stage 3 - Build the video

Only after the user approved the script. Quality over speed, always: every clip is looked at
frame by frame against the words it sits under. Never guess.

Read first: `classy-academy-test/edit-style-measured.md` (measured on all 37 uploads) and
`classy-academy-test/how-you-edit.md` (the #1 video, second by second). Where they differ on music
level, `edit-style-measured.md` wins (it is the later, separated-audio measurement: ~12 dB under).

## The rules that never change

- **Real footage only. Never AI clips.** The channel has never used them and never will.
- **Every creator credited** (CREDITS.txt -> description). **Each clip used once** per video.
- **No sound effects.** None were found in any of the channel's videos.
- **Music:** one soft solo-piano bed, steady ~12 dB under the voice, no ducking, no lifts in
  pauses, fades in with the first word and out after the end card. Mixkit "Classical 4/5/9/10" by
  Jonny S. (tracks 711, 712, 716, 717, free licence).
- **Voice:** Kokoro `af_heart`, speed **0.80**. Voice at about -17.7 LUFS before the master;
  master to -14 LUFS, true peak -1 dB.
- 1920x1080, 30 fps, delivered at full 1080p (Gofile link + CREDITS.txt).

## Work folder

Media never goes in git. One folder per video in the scratchpad:

```bash
bash classy-academy-test/workflow/setup.sh <scratchpad>/<slug>     # once per video
cd <scratchpad>/<slug>; T=/home/user/AISalesAgent1/classy-academy-test/workflow/tools
cp /home/user/AISalesAgent1/classy-academy-test/videos/<slug>/beats.txt .
echo "<the video title>" > title.txt
```

## Step 1 - The voice

```bash
cp beats.txt beats_tts.txt     # then fix pronunciations in beats_tts.txt only (e.g. "centimetres" -> "centimeters")
python3 $T/tts.py              # tts/c001.wav ... one file per line
```

Listen to every line that has a name, a foreign word or a number. Re-generate a line by deleting
its wav and running `tts.py` again.

## Step 2 - The shot list

For every beat, write what the viewer must SEE while each noun is said (audio = visual, word by
word). Bad first, good second. Women of different ages, sizes and skin tones in every group.

## Step 3 - Sourcing (Pinterest videos, then TikTok/Instagram try-ons via Pinterest)

```bash
python3 $T/pin_search.py whiteshirt="white shirt jeans ballet flats outfit video" cafe="paris cafe terrace woman video"
#   -> pin/<tag>.json + pin/sheet_<tag>.jpg (contact sheet of every video pin)
```

Open every sheet. Write candidates into `picks.md` (`b11 swaps: loafers37 loafers1 kitten23`),
with `SKIP:` lines for rejects and `DUP:` notes for the same clip found twice. Then:

```bash
python3 $T/dlpicks.py         # downloads every key named in picks.md -> raw/<key>.mp4 + raw/meta.json (creator, user, pin url)
python3 $T/shots.py sh        # scene cuts -> shots.json + sh_N.jpg sheets (one frame per shot, with time ranges)
python3 $T/grid.py x          # contact sheets, one frame per shot, to check content
```

## Step 4 - Checks on every clip (all of them, before it goes in the edit)

1. **AI scan:** `python3 $T/aiscan.py` -> `aiscan.json`. Score >= 0.40 = do not use, unless you
   open the full-size corner frames, see no sparkle, and write the key and why in `aiok.txt`.
   The build refuses any flagged clip that is not in `aiok.txt`.
2. **By eye:** AI tells - waxy skin, morphing hands or jewellery, text that melts, a too-perfect
   cinematic look, "AI" in the pin text, content-farm accounts, uploader names with gemini / veo /
   sora / ai in them (`raw/meta.json`). When in doubt, leave it out.
3. **Content:** frame by frame, the clip shows exactly what the words say (the piece, the colour,
   the action). Write each verified segment in `ok.txt`: `loafers29 1.0-9.2 : camel loafers walking, cobbles (b10)`.
4. **Quality:** no watermarks over the subject, no big text overlays, no low-res (`L` on the grid),
   HDR clips are tone-mapped automatically, no logos of luxury brands.

## Step 5 - The edit (`edit.py`)

`edit.py` is the beat-by-beat edit, executed by `build.py`. Start from
`$T/edit_example_french.py` (the full French video) and keep its grammar:

| Helper | What it is on screen | When the channel uses it |
|---|---|---|
| `card("1. Heels you can't walk in", i)` | white screen, black script wipes in | every new point |
| `canvas_full(C(key,a,b), t0, t1)` | blurred copy fills frame, sharp vertical clip centred | emotion, scene-setting, exits |
| `row([...], [t...], t_end, labels=[...])` | 2-4 clips edge to edge, one appears per spoken item | lists ("beige, sage, navy") |
| `pair([...], [t...], t_end, labels=[...])` | two clips side by side on the caramel backdrop | X vs Y, two swaps |
| `single(C(...), t0, t1)` | one clip grows from the centre on the backdrop | the swap, "instead..." |
| `compare(a, b, 'Heavy', 'Elegant comfort', ...)` | two panels with small headers | before / after |
| `quote_side(C(...), t0, t1, 'line 1', '<i>word</i>', t2)` | clip on the left, the principle line on the right | the principle line |
| `text('walk with <i>ease</i>', 'q1', t0, t1)` | the one line to remember, one word in script | the principle, never captions |

Times come from the voice: `st(i)` start of line i, `en(i)` end, `wd(i, 0.4)` 40% through it.
`C('loafers29', 1.0, 9.2)` = the verified segment from `ok.txt`.

Targets (from the top-5 videos): about **34% caramel-backdrop time**, a layout change about every
**9 seconds** (6.6 per minute), the intro title card with the episode number, the stylist-guide
haze card mid-video, the X checklist recap and the white CE end card.

## Step 6 - Build, look, fix

```bash
python3 $T/build.py        # -> index.html, assets/mix.wav, beats.json, CREDITS.txt; prints SHORT clips and words/min
npx hyperframes lint
npx hyperframes snapshot --at 12.5 --no-end -o snaps     # look at any moment before rendering
```

Fix every line `build.py` prints under `SHORT:` (a clip shorter than the time it must cover).
Check the voice-to-picture sync at every number card and every list.

## Step 7 - Render and QA

Render with the fast renderer (`tools/ffr.py`, ~4.3 min per minute of video here; the browser
renderer takes ~11). It draws the same page with FFmpeg and must match the browser before a full run:

```bash
node $T/ffr_capture.js $PWD $PWD $PWD/ff/sprites       # text + graphics captured once from Chrome (fonts match)
npx hyperframes snapshot --at 5,40,100,200,350,450,530,560 --no-end -o snapcmp   # browser frames: every layout type
python3 $T/ffr_cmp.py                                   # every moment must show a mean diff < 10; look at ffr_cmp_*.jpg
python3 $T/ffr.py . 0 <duration> out/<slug>_v1.mp4 4    # run in the background; <duration> = data-duration in index.html
# fallback only: npx hyperframes render -o out/<slug>_v1.mp4 --workers 4   (~11 min per minute)
python3 $T/qa.py out/<slug>_v1.mp4      # black frames, frozen picture, loudness, silence (music must never drop)
python3 $T/flash.py                     # clips with built-in dark flashes
```

Then a per-second contact sheet of the whole video, looked at end to end: no empty backdrop while
the voice talks about something, no clip that contradicts the words, no repeated clip, no AI.
Fix, rebuild, re-render, re-check until all of it is clean.

## Hand back

Upload the 1080p file and CREDITS.txt to Gofile
(`curl -sS --max-time 1700 -F "file=@out/<slug>_v1.mp4" https://upload.gofile.io/uploadfile`,
then the credits into the same folder), send the link, the runtime, the QA numbers
(LUFS, black frames: 0, freezes: 0), the number of clips and creators. Keep `edit.py`, `picks.md`,
`ok.txt` and `CREDITS.txt` in `classy-academy-test/videos/<slug>/` (text only) and commit them.

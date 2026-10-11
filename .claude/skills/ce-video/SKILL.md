---
name: ce-video
description: >-
  Build a full Classy Elegance video from an approved beats.txt: calm Kokoro
  voice, real Pinterest/TikTok clips chosen line by line (never AI, never
  reused, all credited), product cut-outs, the channel's caramel-backdrop edit
  language in HyperFrames, continuous music + soft SFX, 1080p render, automated
  and visual QA, and a download link. Use for "ce-video", "build the video",
  "edit the video", after ce-script.
---

# ce-video: from beats to a finished 1080p video

Before starting, read `channel/how-you-edit.md` (the measured edit language),
`channel/RULES.md` (visual storytelling rules), and `channel/LESSONS.md` (user feedback).
The working reference is `reference/winter-2026/`, the approved winter video's real build files.
**Copy and adapt it.** Don't start from zero.

## 0. Setup (fresh session)
```bash
W=<scratch>/video-<slug>; bash .claude/skills/ce-video/tools/setup.sh $W
cp .claude/skills/ce-video/reference/winter-2026/{build.py,template.tpl,coat.py} $W/
cp videos/<slug>/beats.txt $W/beats.txt
```

## 1. Voice
```bash
cd $W; n=0; while IFS= read -r line; do n=$((n+1)); npx hyperframes tts "$line" -v af_heart -s 0.80 -o $(printf "tts80/c%03d.wav" $n) </dev/null >/dev/null 2>&1; done < beats.txt
```
Speed 0.80 gives about 126 wpm, the channel's pace (it runs 123-131). In `build.py`, set `gap`: about
0.85 s by default, about 0.45 s between list items, 1.1 s before a new point, 0.8 s after a number
card.

## 2. Shot list: what must she SEE?
For every beat, write one line: the literal visual that teaches it with the sound off.
- A garment or colour named → that exact item on a real elegant woman. One panel per item, each
  in its own colour.
- A mistake → the real bad version first, then the fix (Uncared for / Cared for, Sporty / Polished).
- A principle line → serif text with one script word, beside a clip (`quote_side`) or on the
  backdrop.
- "try this / instead / the secret" → a small script hint on the backdrop, then the recipe.
- Named pieces → product cut-outs floating in, one per spoken item (`cutout`, `recipe`).
- The hook and the emotion → full-screen cinematic walks (`canvas_full`), snow on winter shots.
- Number cards → white screen, black script wipe (`card`).

## 3. Source real clips (Pinterest video pins)
```bash
cd $W; PIN_OUT=$W/pin python3 $SK/ce-video/tools/pin_search.py "p1_coat=camel coat outfit video" "p1_fleece=fleece zip up outfit video" ...
python3 $SK/ce-video/tools/vmosaic.py $W $W/m1.jpg p1_coat p1_fleece   # LOOK at the sheet, pick by index
python3 -I -c "import json,sys; sys.path.insert(0,'$SK/ce-video/tools'); from pin_dl import dl; ..."   # dl(pin['videos'][0], 'dl/<tag>_<i>.mp4')
python3 $SK/ce-video/tools/strips.py $W/dl $W/strip     # 10 frames across EVERY clip: find the clean section
bash $SK/ce-video/tools/cut1.sh <name> dl/<tag>_<i> <start> [len]   # -> assets/<name>.mp4 (720x1280)
```
- Product photos: search `"<item> product photo white background"`, then
  `tools/cutout.py raw.jpg out.png`. For tricky edges (white garments, glass), use rembg
  `isnet-general-use`.
- Keep a `segs.txt` (`name source start`). The credits file is generated from it plus each pin's
  `creator` and `url`.
- Reject clips with burned-in captions or brand text, cuts to unrelated content, the wrong
  colour or item, low resolution, or extreme close-ups of strangers' faces.
- Check every new clip for **HDR**:
  `ffprobe -show_entries stream=color_transfer` (arib-std-b67 / smpte2084). Tonemap it to bt709
  with `zscale…tonemap=hable`. One HDR clip makes HyperFrames render about 10× slower.

## 4. Build the edit (HyperFrames)
Edit the `# the edit` section of `build.py` (and `points.py` / `coat.py` in the reference). The
helpers:
`canvas_full, single, pair, row(labels=…), panel(swaps=[(clip,t)]), quote_side, card, white, text(cls='hint'|'q1'|'q2'),
cutout, recipe, compare2(header…), clabel, header, snow, checklist, guide overlay (haze + gtx1/gtx2), end card (logo_ce_dark)`.
Timing helpers: `st(i)`, `en(i)`, `wd(i, fraction)` for beat i.

Built-in guards, which must end clean:
- `USED`: a clip used twice raises an error.
- `SHORT`: a slot longer than its clip is listed. It must print `SHORT: []`. Fix it with a
  second clip via `swaps`, gentle slow motion (`setpts=1.2*PTS`, at most 1.4×), or a later entry.
  Never let a clip freeze.

Audio (already in `build.py`; keep it):
- Mixkit piano tracks crossfaded to cover the **whole** length. One 5-minute track once left 4
  minutes silent.
- The bed sits about 11 dB under the voice and lifts in the pauses.
- SFX at +7 dB (click-soft on panels, sparkle on cards and hints, whoosh on full-screens and
  white, pop on cut-outs, chime on the guide).
- `loudnorm I=-14`.

## 5. QA before rendering (mandatory)
```bash
python3 -I build.py            # prints total, wpm, elements, sfx, unique clips, SHORT: []
npx hyperframes lint           # 0 errors
npx hyperframes snapshot --at <one time per beat> -o snaps   # make contact sheets with the beat text under each frame and LOOK at every one
```
Fix every frame whose visual doesn't teach its line, and every overlap, stray outline or text
collision.

## 6. Render + verify
```bash
npx hyperframes render -o out/<slug>.mp4 --workers 4   # about 65 min for 9-10 min; check the log says "No HDR sources detected"
ffmpeg -i out/<slug>.mp4 -vf "freezedetect=n=0.003:d=1.5,blackdetect=d=0.3" -an -f null -   # every freeze must be a card, a text line or a diagram
ffmpeg -i out/<slug>.mp4 -af ebur128 -f null -           # about -14 LUFS integrated
```
Fix a real freeze by rebuilding that moment. In a hurry, overlay the gap with ffmpeg.

## 7. Deliver
`curl -F "file=@<file>.mp4" https://upload.gofile.io/uploadfile`. Check that the returned md5
matches `md5sum`, then send the link: full 1080p, never just a compressed preview. Copy the credits
to `videos/<slug>/CREDITS.txt` and commit. Media files stay out of git.

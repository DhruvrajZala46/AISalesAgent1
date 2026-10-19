# Final report: The Classy Elegance, "Why Her Hair Always Looks Expensive (It's Not the Cut)"

## What you get

- **The video**, sent in this chat as `Why_Her_Hair_Always_Looks_Expensive_1080p.mp4`:
  - 1920×1080, 30 fps, H.264, AAC, 10:57;
  - master -18.0 LUFS, true peak -1.0 dBTP.
  - The full-quality master (CRF 17, 462 MiB) is over the chat's 400 MiB upload limit. The copy sent is a two-pass
    H.264 encode at about 4.6 Mb/s of that master: the same picture and the same sound track.
  - Media is never committed, so the file is not in git.
- **The editable project**, sent as `Episode31_project.zip` (start with its `README.txt`). The same text files are in `project/` here.
  - `picks.json`: which clip, which second, crop and speed for every shot.
  - `overrides.json`: the layout of each scene.
  - `scenes.json`: the 84 scenes of the approved plan.
  - `build_timeline.py` turns those into `timeline.json`; `render.py` draws the picture; `mix.py` builds the sound and joins it to the picture.
  - The zip also holds your CE logo, the fonts, music and narration.
- **The footage** (116 clips, 3 photos), sent as `Episode31_footage_part1-3.zip`. Unzip the three parts inside the project folder.
- **Records:**
  - `CREDITS.txt`: every creator, in order of appearance, ready for the description.
  - `SOURCES-LOG.md`: every picture with its scene, creator, original post, the route it was found by, and its permission status.
- **The study the edit is built on:** `../../channel-deep-study-2026-10-19.md`.
  - Your 30 uploads, watched second by second with their sound.
  - The per-video timelines are in `channel-study/`.

## How it follows your videos (each point is in the study, with times)

- **Brand (changed 19 Oct on your instruction):** your CE / The Classy Elegance logo top-left on every picture and on the end card;
  no classyladyacademy.com link anywhere; no Classy Academy episode number, product name or sound.
- **Opening:**
  - your voice-style narration from the first frame, with no music intro and no hook text;
  - one picture per line: hair close-ups, a row of three looks, the tired-cut back view;
  - "In today's video" on a white card;
  - then the script title "Why Her Hair Looks Expensive" over a darkened clip (no episode label);
  - then the first "linked below" mention with the guide call-out ("Check the description for / Personal Stylist Guide", no website).
- **Seven points,** each opening on a white card with the black script title written on in about 1 s.
  The first line of the point is spoken over the card, which leaves with a hard cut, as in your 2026 uploads.
- **Inside each point,** your layouts and nothing else:
  - one vertical clip centred on the caramel (608 px, full height);
  - full-screen clips;
  - rows of 3 (three 608 px panels with 48 px caramel gutters) and rows of 4, built one panel per spoken item;
  - framed pairs;
  - quotes on caramel or cream, and quote splits (clip left, quote right), with the key words in script.
- **The caramel background** has the exact colour spread of your caramel frames, measured pixel by pixel.
- **Pictures:**
  - every picture shows what is being said, at the word it is said;
  - rows show different women, ages, skin tones and hair types (straight, wavy, curly, coily, grey, silver);
  - Andie MacDowell appears on her name (Cannes 2021 red carpet), with no name on screen.
- **Ending:**
  - comment question as a split;
  - thank you, like and comment over calm full-screen clips;
  - the guide call-out;
  - "Until next time. Bye, my loves." over the opening clip (your bookend);
  - the white end card with your CE / The Classy Elegance logo.
- **Sound, as measured on your uploads:**
  - a very soft piano bed 20 dB under the voice, from the first word to the last;
  - no ducking and no sound effects;
  - 0.5 s of silence, then the piano swells on the end card for about 5 s and fades to silence.

## Checks done before you see it

- **Whole video, frame by frame on sheets:** a frame every 2 s with the spoken words, all 10:57, watched end to end twice.
  - The first pass found and fixed:
    - a big TikTok logo in the hook;
    - two shower shots in one row;
    - half-empty pair screens held for 10 s;
    - a guide call-out naming a different guide than the voice;
    - an airport clip cropped to the ceiling;
    - 41 shots that would have run past the end of their clip.
  - Every shot now fits inside its clip; the builder now warns on this automatically.
- **No AI:**
  - the AI watermark scan ran on all 116 clips used: none flagged (highest 0.19; the AI line is 0.40);
  - full-size frames of the most cinematic clips were checked by eye;
  - a frame sheet of all 198 downloads was reviewed, and clips with ads, overlays or off-topic parts were cut around or dropped.
- **The exported file itself** (`tools/final_qc.py`, `tools/empty_check.py`):
  - picture and sound are both 656.83 s;
  - no black frames;
  - -18.0 LUFS, true peak -1.0 dBTP;
  - the only stills over 3 s are the three longest point cards and the end card, as intended;
  - no empty backdrop while the voice talks, apart from the first instant of a white card or a quote as it starts writing on, as in your videos.
  - All 10:57 were watched again on frame sheets taken from the exported file. Two in-points and three timings were corrected
    (a hand at 0:28, a product bottle at 1:10, an empty row opening at 2:14, a product shot at 2:42, quote text appearing late),
    and the video was rendered again before sending.

## What is not 100% yours (said plainly)

- **Voice:** your own narration is not available. The narration is the synthetic voice your pipeline uses (Kokoro af_heart) at your pace.
  If you record the script, I swap your voice in and re-time the cuts.
- **Music and fonts:** your piano bed and font files are not available.
  - The bed is a soft solo piano (Chopin, CC0 recordings) at your measured level.
  - The fonts are the closest look-alikes (Pinyon Script, Playfair Display).
  - The end-card music is the same CC0 piano as the bed (no sound from another channel).
- **Permission:** the clips are used the way your videos use them: creators' TikTok and Instagram reels, Pinterest pins, press photos.
  - **No creator has been asked, and no request has been sent.** Nothing goes out without your OK.
  - The permission message template is in `CLIP-CANDIDATES.md`, and every creator and link is in `SOURCES-LOG.md`.
  - The Andie MacDowell photos are press photographs (the copyright is the photographers'), found via Pinterest like your celebrity photos.
- **Creator credits:** none on screen, as in your 2026 uploads and the Haircuts video. They are in `CREDITS.txt` for the description.
  Your Hairstyles video credits only its 25–44 s tutorials, and this episode has no hold that long.

## Your decision

Ship it, or change it? Tell me any shot, line or moment by its time and I change it in the project and re-render.

# Final report: Episode 31, "Why Her Hair Always Looks Expensive (It's Not the Cut)"

## What you get

- **The video:** `Why_Her_Hair_Always_Looks_Expensive.mp4`, sent to you in this chat.
  - 1920×1080, 30 fps, H.264 (CRF 17), AAC 320 kb/s, 10:57.
  - Master -18 LUFS, true peak -1 dBTP.
  - Media is never committed, so the file is not in git.
- **The editable project:** `project/`. Change any shot, then rebuild and re-render.
  - `picks.json`: which clip, which second, crop and speed for every shot.
  - `overrides.json`: the layout of each scene.
  - `scenes.json`: the 84 scenes of the approved plan.
  - `build_timeline.py` turns those into `timeline.json`.
  - `render.py` draws the picture; `mix.py` builds the sound and joins it to the picture.
  - Commands:
    ```
    python3 -I project/build_timeline.py
    python3 -I project/render.py video --jobs 4
    python3 -I project/mix.py
    python3 -I project/mix.py mux
    ```
- **Records:**
  - `CREDITS.txt`: every creator, in order of appearance, ready for the description.
  - `SOURCES-LOG.md`: every picture with its scene, creator, original post, the route it was found by, and its permission status.
- **The study the edit is built on:** `../../channel-deep-study-2026-10-19.md`.
  - Your 30 uploads, watched second by second with their sound.
  - The per-video timelines are in `channel-study/`.

## How it follows your videos (each point is in the study, with times)

- **Opening:**
  - your voice-style narration from the first frame, with no music intro and no hook text;
  - one picture per line: hair close-ups, a row of three looks, the tired-cut back view;
  - "In today's video" on a white card;
  - then "Episode 31 / Why Her Hair Looks Expensive" over a darkened clip;
  - then the first "linked below" mention with your 3-line guide call-out.
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
  - your white end card with the tan CA / Classy Academy logo.
- **Sound, as measured on your uploads:**
  - a very soft piano bed 20 dB under the voice, from the first word to the last;
  - no ducking and no sound effects;
  - 0.5 s of silence, then your own logo sting on the end card, then silence.

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
- **Final file:** see "Final file checks" below (black frames, loudness, length).

## What is not 100% yours (said plainly)

- **Voice:** your own narration is not available. The narration is the synthetic voice your pipeline uses (Kokoro af_heart) at your pace.
  If you record the script, I swap your voice in and re-time the cuts.
- **Music and fonts:** your piano bed and font files are not available.
  - The bed is a soft solo piano (Chopin, CC0 recordings) at your measured level.
  - The fonts are the closest look-alikes (Pinyon Script, Playfair Display).
  - The end sting is your own, cut from your 8 Classy Habits video.
- **Permission:** the clips are used the way your videos use them: creators' TikTok and Instagram reels, Pinterest pins, press photos.
  - **No creator has been asked, and no request has been sent.** Nothing goes out without your OK.
  - The permission message template is in `CLIP-CANDIDATES.md`, and every creator and link is in `SOURCES-LOG.md`.
  - The Andie MacDowell photos are press photographs (the copyright is the photographers'), found via Pinterest like your celebrity photos.
- **Creator credits:** none on screen, as in your 2026 uploads and the Haircuts video. They are in `CREDITS.txt` for the description.
  Your Hairstyles video credits only its 25–44 s tutorials, and this episode has no hold that long.

## Your decision

Ship it, or change it? Tell me any shot, line or moment by its time and I change it in the project and re-render.

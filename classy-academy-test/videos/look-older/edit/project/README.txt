The Classy Elegance - "8 Things That Make You Look Older: What to Wear Instead" - editable project

What is here
  project/scenes.py        the script-to-visual plan: every sentence -> layout, footage, the word each panel enters on
  project/scenes.json      the same plan as data (written by scenes.py)
  project/picks.json       the footage used: file, in-point, speed, crop focus (written by tools/compile_picks.py)
  project/clock.json       narration timing: every sentence's start and end
  project/timeline.json    the full edit (written by build_timeline.py) - what render.py draws
  project/build_timeline.py, render.py, mix.py, narration.py, records.py   the build
  project/tools/           QC: range_sheet.py (contact sheet of any stretch), final_qc.py, empty_check.py, qc_sheet.py
  picks/<ID>.json          one sourcing record per picture: Pinterest pin, creator, original post, AI checks, rights note
  plan/briefs.json         the visual brief for every asset ID
  tools/                   the sourcing and media tools (search, download, normalise to 30 fps, cut-outs, face framing)
  fonts/, assets/          Pinyon Script, Playfair Display (SIL OFL); your CE logo
  music/                   Chopin, Musopen recordings, CC0 1.0
  audio/voice.wav          the narration (synthetic, Kokoro af_heart); audio/mix.wav the final sound
  media/clips, media/cut   the footage (in the separate footage zips: unzip them into this folder)

How to change something and render again (Python 3 with numpy, opencv-python, pillow, soundfile; ffmpeg)
  1. Change a picture: edit picks/<ID>.json ("in", "speed", "focus") or swap its file, then
       python3 tools/normalize.py          (only for a new video file)
       python3 tools/compile_picks.py
  2. Change a layout or timing: edit project/scenes.py, then  python3 project/scenes.py
  3. Build and check:   python3 project/build_timeline.py      (warns if a shot would run past the end of its clip)
                        python3 project/tools/range_sheet.py 90 150 1.0     (frames every second, with the words, in qc/)
  4. Render:            python3 project/render.py video --jobs 4             (out/video_only.mp4)
  5. Sound + file:      python3 project/mix.py ; python3 project/mix.py mux  (out/8_Things_That_Make_You_Look_Older.mp4)
  To use your own voice: replace tts/s001.wav ... s124.wav (one file per sentence), run project/narration.py, then steps 3-5.

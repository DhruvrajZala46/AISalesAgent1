# health-cartoons/

English health-explainer Shorts in the "talking organs + doctor" cartoon format. Everything is drawn and animated in code (SVG plus Playwright).

**New chat? Read in this order:**
1. `PLAYBOOK.md`: the fixed standard (script beats, voices, music and SFX map, visual rules, retention targets, pipeline, QA).
2. `LEARNINGS.md`: every piece of user feedback and the rule it created.
3. `research/VIRAL-STUDY.md`: what makes the reference channel's Shorts hit 10M-27M (topics, hooks, script, sound, retention).
4. `videos/001-earwax-cotton-buds/`: the quality bar. Copy this folder to start the next video.

Layout:
- `tools/`: fetch_assets.sh, process_voice.sh, words.py, render.js, snap.js, mix.sh, retention_check.py, and the analysis helpers
  (score_voices.py for voice matching, tag_audio.py for music/SFX tagging, music_similarity.py).
- `assets/`: font, music and SFX (git-ignored; `tools/fetch_assets.sh` re-creates it).
- `videos/NNN-slug/`: `scene.html`, `build_audio.py`, `words.json`, `script.md`. Media is never committed.

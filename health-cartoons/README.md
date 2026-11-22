# health-cartoons/

English health-explainer Shorts in the "talking organs + doctor" cartoon format. Everything is drawn and animated in code (SVG plus Playwright).

**New chat? Read in this order:**
1. `PLAYBOOK.md`: the fixed standard (script beats, voices, music and SFX map, visual rules, retention targets, pipeline, QA).
2. `LEARNINGS.md`: every piece of user feedback and the rule it created.
3. `research/VIRAL-STUDY.md`: what makes the reference channel's Shorts hit 10M-27M (topics, hooks, script, sound, retention).
4. `videos/012-why-we-snore/`: **the standard to copy** (the user: "PERFECT, every future video in this style"; recipe at the top of PLAYBOOK.md). `videos/001-earwax-cotton-buds/` is the original engine; `videos/003-food-up-nose/` is history.

**Every video: PLAYBOOK §0 in full, the same effort as 003 or more.** The user asked for this explicitly and it must never be forgotten.

Layout:
- `tools/`: fetch_assets.sh, process_voice.sh, words.py, render.js, snap.js, mix.sh, retention_check.py, and the analysis helpers
  (score_voices.py for voice matching, tag_audio.py for music/SFX tagging, music_similarity.py).
- `assets/`: font, music and SFX (git-ignored; `tools/fetch_assets.sh` re-creates it).
- `videos/NNN-slug/`: `scene.html`, `build_audio.py`, `words.json`, `script.md`. Media is never committed.

New channel (22 Nov 2026, the format clone of @Dr_Healthcare1): **Dr. Mira Explains**. Plan: `research/CLONE-CHANNEL-PLAN.md`; art: `brand/dr-mira/`.
Older channel brand (Nov 2026): name **Giggle MD** (handle @GiggleMD was free when checked). `brand/`: `python3 build.py && node shoot.js`
renders `dp.png` (800×800) and `banner.png` (2560×1440, text inside the 1546×423 safe area) from the same doctor and organ characters as the videos.

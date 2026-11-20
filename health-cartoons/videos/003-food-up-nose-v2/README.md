# 003 v2 - same video (food out the nose when you laugh), re-drawn with AI-illustrated art

Audio, script and timing are reused from `../003-food-up-nose/` (copy its `data.js`, `data.json`, `voice.wav`, `music.wav`, `sfx.wav`).
Only the visuals changed: the user rejected the code-drawn art of 003 as "basic".

Art: Meta Muse Image (`muse-image-1.0`), prompts in `prompts/*.json`, made with `MODEL_API_KEY=... python3 -I ../../tools/meta_art.py prompts/02_batch1.json`
(`src` = edit of an earlier sprite, so the same character keeps the same look). The palate panic pose (`pal_panic`) is an edit of
`sprite_palate` with the prompt in `prompts/04_panic.txt`. Characters are made on flat #00FF00 and keyed by `prep_art.py`;
mouth and eye positions (for lip-sync and blinks) are hand-measured fractions in `prep_art`'s output `art/meta.json`.
Build: `python3 -I prep_art.py && python3 assemble.py && node ../../tools/render.js && bash ../../tools/mix.sh video.mp4 final.mp4`.
Media (art, audio, video) is never committed.

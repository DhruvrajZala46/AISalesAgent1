# 017 - Why Do Blackheads Come Back After a Peel-Off Mask? (GiggleMD)

Status (24 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (016).

## The reference the user sent
A 66.1 s vertical video by @dermiyo.skin (the user's WhatsApp file; views not measured here).
- 0-39 s: one locked cut-away of skin with three pores full of oil: a big smug blackhead and two small ones.
  - A brush spreads a black peel-off mask; it dries; it is ripped off with the small plugs' tops; they fill back up.
  - A salicylic acid dropper bottle arrives ("oil-soluble, actually"); its drops melt the plugs; the pores end up empty.
- 40-61 s: a clinic with a "CHEAT SHEET" board over the doctor and the patient; cards pop in on the doctor's words.
- 62-66 s: an end card with the creator's handle (not copied; we have no outro).

## What we kept, and what is ours
- **Kept:** every scene, its order and staging; each beat and who speaks it; the mask, the ripped tops, the refill, the bottle, the melt, the cheat sheet idea and its three cards.
- **Ours:** all drawings (code), the channel's doctor and patient, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 16 recorded lines, 160 words).
- **Added for clarity (LEARNINGS row 27):** BLACKHEAD, OIL and PORE labels on the first frames.
- Facts stay as in the reference and match standard skin-care guidance: a peel-off mask removes only the surface of the plug; salicylic acid is oil-soluble, so it gets into the pore; results take weeks; do not squeeze.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `TmTu3JZ9t5RiHyVCMedO`, 1 take per line (`takes_manifest.tsv`, `voices.txt`), checked by whisper.
- SFX: Mixkit 1492, 2182, 2357, 2358, 2364; clicks are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_017.js` (skin layers, three pores with a fill level, mask, brush, dropper bottle, cheat-sheet clinic), `parts_017.js` (all motion; `state()` gives each pore's fill level and dark top), `assemble_017.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 16 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_017.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-blackheads-come-back.mp4`)
- Length 60.3 s (reference 66.1 s with its end card); first word at 0.15 s.
- Speech: whisper on the mix 95.0% (152 of 160), measured before the last drawing-only fix. Below the 97% target: 6 of the 8 misses are spellings of the same sound ("pore" as "pour" three times, "Eww", "Aah", "Nooo"); the real ones are "We're" heard as "You're" and "oil" as "oil's".
- Loudness -12.0 LUFS, peak -1.6 dB.
- Frozen frames 8.0% (15.6% before idle motion was added); longest still stretch 0.6 s.
- Checked on 290 px reference-over-ours tiles (14 moments) and at 5 fps for the hook, the rip, the refill, the bottle's entry and the melt.

**Fixed after the first sheets:** the mask was a thin strip; the scene was small; the small pores were cut by the frame edge and had thin walls; the torn-off drop in the small pores was too shallow to read.

## Upload block
**Title:** Why Do Blackheads Come Back After a Peel-Off Mask? 😳

**Cover frame:** the black mask on the skin with the smug big blackhead under it (about 5 s).

**Description:**
Ever ripped off a peel-off mask and watched your blackheads come right back? 😳 The mask only pulls off the top of the plug. The oil deeper in the pore stays, so it fills right back up. Salicylic acid is oil-soluble, so it can get inside the pore and dissolve the oil. Use a cleanser or serum a few times a week, give it a few weeks, and don't squeeze them!

A cartoon for general education, not medical advice.

#shorts #blackheads #skincare #salicylicacid #peeloffmask #acne #healthfacts #animation

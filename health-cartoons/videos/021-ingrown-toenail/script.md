# 021 - How Cutting Your Toenails Can Cause an Ingrown Toenail (GiggleMD)

Status (25 Nov 2026): **built and delivered**. Waiting for the user's verdict. Topic: #10 in `research/NEXT-10.md` (13M on Dr. Healthcare, `5nv9ht6pz38`; views as of 20 Nov, not re-checked).

## The reference the user sent
A 51.7 s vertical video by Dr. Healthcare. Studied at 0.5 s steps (LEARNINGS row 29). Beat list:
- One set: two toes in close-up (a big toe and the second toe, each with a face on its nail) and a nail clipper with a face, top left.
- 0-3 s: the nail is long (white edge); the clipper announces a trim, swoops down and snips.
- 3.5-8.5 s: the nail is now short with rounded corners; a green dashed line shows the rounded edge; the toe complains; the clipper brags.
- 9-11.5 s: the clipper leaves; the second toe says it will grow back; the big toe strains (eyes shut, sparkles) and the nail grows long.
- 12-16 s: the clipper returns and snips again.
- 16.5-22 s: the toe is angry (even shorter); the clipper says shorter is cleaner and leaves.
- 22.5-28.5 s: the second toe says he is messing with you; the big toe decides to grow into the skin; it strains and the sides go red.
- 29 s: a "LATER..." card.
- 30-36 s: the toe is red and swollen with green smell lines; the clipper comes back, recoils and holds its nose.
- 36.5-51.7 s: the clinic: the patient holds his foot, the doctor holds a clipper; a thought bubble shows the right cut.

## What we kept, and what is ours
- **Kept:** every beat above, in order; who speaks each line; the sound moments (swoop, snip, strain, pop, card).
- **Ours:** all drawings (code), the channel's doctor and patient, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 12 lines, 134 words). The reference's voices and music are not reused (copyright and reused-content strikes).
- **Added for clarity (rows 27, 28, 30):** a foot card with a ring on the big toe ("BIG TOE NAIL"); labels CORNERS CUT ROUND, EVEN SHORTER!, GROWS INTO THE SKIN, INGROWN TOENAIL; in the clinic a board instead of the thought bubble: ROUND CORNERS (cross) next to STRAIGHT ACROSS (tick), then "NAIL GROWS OUT, NOT INTO THE SKIN"; a zoom circle on the patient's sore toe.
- **Facts:** cutting toenails too short or rounding the corners lets the edge grow into the skin; cut straight across.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `XohwjpXxzncts3NjXg9o`, 1 take per line (`takes_manifest.tsv`, `voices.txt`).
- SFX: Mixkit 1492, 2182, 1884, 2357, 473; snips are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_021.js` (`toesScene`, `nailD`, `clipperSVG`, `footCard`, `miniToe`, `clinic21`), `parts_021.js` (all motion, `nailState`), `assemble_021.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 12 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_021.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`how-cutting-toenails-causes-ingrown-toenail.mp4`)
- Length 52.9 s (reference 51.7 s); first word at 0.35 s.
- Speech: whisper on the final mix 97.0% (130 of 134; "you'd" heard as "you", "that will" written "that'll", "Eww" written "Ew").
- Loudness -12.0 LUFS, peak -2.2 dB.
- Frozen frames 1.7%; longest still stretch 0.8 s.
- Checked on 22 reference-over-ours pairs of the final render.

Still different from the reference: its toes are rounder with more expressive faces (bigger brows and mouths) and its nail has a curved top, ours is boxier; its patient sits holding his foot, ours sits behind a bed with a zoom circle on the toe.

## Upload block
**Title:** How Cutting Your Toenails Can Cause an Ingrown Toenail 😳

**Cover frame:** the red, swollen toe with the clipper recoiling (about 34 s).

**Description:**
"Why did you round off my corners?" 😳 Cutting your toenails too short, or rounding the corners, lets the edge of the nail grow into the skin. That is an ingrown toenail: red, swollen and painful. The fix is simple: cut straight across and leave the corners alone.

A cartoon for general education, not medical advice. If a toe is very painful, swollen or has pus, see a doctor.

#shorts #ingrowntoenail #toenails #footcare #health #healthfacts #humanbody #animation

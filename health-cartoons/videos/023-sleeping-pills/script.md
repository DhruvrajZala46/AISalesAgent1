# 023 - How Do Sleeping Pills Actually Work? (GiggleMD)

Status (25 Nov 2026): **v3 built and delivered** (see the v3 section). Waiting for the user's verdict. The user's message named "Still craving food when you're full", but the attached mp4 was "How Do Sleeping Pills Really Work" (10M on Dr. Healthcare, `OJS2ONcmZ58`, in `research/NEXT-10.md` reserves; views as of 20 Nov, not re-checked). The video follows the attached file; the user was told.

## The reference the user sent
A 65.0 s vertical video by Dr. Healthcare. Frame 0 compared side by side first (LEARNINGS row 31), then studied at 0.5 s steps (row 29). Beat list:
- 0-0.9 s: the stomach cut open (food pipe from the top, liver behind, acid pool, intestines below) with an angry face; two pills drop down the pipe into the acid.
- 1-5 s: the stomach complains about the sleeping pill, then shouts up to the brain.
- 6-19.5 s: the brain appears in a thought bubble, tired; it has had anxiety for days and asks the stomach to break the pill down faster; the stomach agrees grudgingly.
- 21 s: cut to "Amygdala (Brain's Anxiety Centre)": a police officer walks in to three burning, angry blobs (Cortisol, Glutamate, Adrenaline).
- 22-31 s: the officer tells them to calm down; they calm, then flare up again; he complains.
- 32-33 s: a cloud of smoke (a brawl); the officer comes out with a black eye and a plaster; he quits.
- 37-54 s: a small sleeping pill walks in; the officer tells it to gossip outside; the pill says it is here to calm things down; the officer agrees.
- 54-59.5 s: "quiet down, settle down": the flames go out, the blobs relax.
- 60-65 s: a bedroom: the partner says she finally slept well after the pill. No doctor.

## What we kept, and what is ours
- **Kept:** every beat above, in order; who speaks each line; the sound moments (pills falling, plop, bubble pop, flames, brawl, flames going out).
- **Ours:** all drawings (code); the channel's patient as the husband and our seated woman from 020 as the wife; the wording, one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 15 lines, 147 words). The reference's voices and music are not reused (copyright and reused-content strikes).
- **Added for clarity (rows 27, 28, 31):** body cards "INSIDE THE STOMACH" and "INSIDE THE BRAIN" with a pulsing ring; labels SLEEPING PILLS, PILL DISSOLVES, OFF TO THE BRAIN! (with a dotted arrow up), AMYGDALA: THE WORRY CENTRE, WORRY SIGNALS ON FIRE, THE CALMING SIGNAL, PILL BOOSTS THE CALMING SIGNAL, CALM. TIME TO SLEEP.; a "GABA" badge on the officer (the brain's calming signal, which most sleeping pills strengthen).
- **Facts:** most prescription sleeping pills (benzodiazepines, "Z-drugs") strengthen GABA, the brain's main calming signal, which quiets overactive alarm activity such as in the amygdala. Simplified for a cartoon.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `U8SRkcJWre7Ripf97bky`, 1 take per line (`takes_manifest.tsv`, `voices.txt`).
- SFX: Mixkit 1492, 2357, 2828, 2182, 2364; thuds are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_023.js` (`stomachScene`, `amygScene`, `blob`, `copSVG`, `sleepPill`, `bedroomScene`, `wifeSVG`, `bodyCard`), `parts_023.js` (all motion; `heat()` drives the flames), `assemble_023.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 15 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_023.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`how-sleeping-pills-actually-work.mp4`)
- Length 60.4 s (reference 65.0 s); first word at 0.9 s, pills falling from frame 0.
- Speech: whisper on the final mix 98.6% (145 of 147).
- Loudness -12.0 LUFS, peak -1.9 dB.
- Frozen frames 0.3%; longest still stretch 0.2 s.
- Frame 0 checked at 450 px next to the reference's (the stomach was redrawn once: a thick muscle wall so it reads as a bag); 16 reference-over-ours pairs of the final render.

Still different from the reference: its stomach is drawn at an angle with more wall layers and its liver is larger; its wife sits on the bed, ours sits on a chair beside it; its pill is a small capsule, ours a bigger tablet with legs.

## v2 (25 Nov 2026, after the user's verdict on v1)
The user sent the same reference again: **"VERY BAD VIDEO, 5%... I can't understand what that body part is... compare their visual storytelling with what you made."**

v1 had compared only frame 0. v2 put 12 moments of the reference next to ours at 360 px and found:
1. The stomach was a pink box with a flat top and square corners; it read as a wall, not an organ. **Now:** a bag: the food pipe curves into a body with a round dome on the right, a red muscle wall, acid at the bottom, the small intestine as one coiled tube below, the liver and the yellow bile duct on the left.
2. The brain in the bubble was pale pink with a stem, like a balloon. **Now:** red-brown with deep folds, as in the reference.
3. The body cards were a plain torso with a ring. **Now:** the stomach card shows the stomach shape on the body (moved to the bottom left, clear of the face); the brain card shows the brain inside the head.
4. The worry blobs had thin spikes on top. **Now:** tongues of fire all round each blob, red angry eyes, anger marks and a burning puddle; the fire shrinks as they calm.
5. The sleeping pill in the brain was a square with legs and did not look like the pills in the stomach. **Now:** the same round white tablet, so the viewer links the two.
6. The wife sat on a chair and the husband covered her. **Now:** she sits on the bed, as in the reference, and he stands clear.
7. Captions sat at the bottom edge. **Now:** larger, at the reference's height.

**v2 QA (`how-sleeping-pills-actually-work-v2.mp4`):** 60.4 s; whisper 98.6% (145 of 147); -12.0 LUFS, peak -1.9 dB; frozen 0.3%; longest still 0.2 s. Checked on 16 reference-over-ours pairs of the final render and 3 large pairs of the stomach scene.

Still different from the reference: its stomach is drawn at an angle with more wall layers; its officer is short and stocky, ours is the taller code figure; the audio, wording, husband and wife are ours, as explained above.

## v3 (25 Nov 2026): the hook, after a study of the channel's best videos
The user: **"still no proven hook, no visual hook. Study this channel's best-performing videos, understand their visual hook and animation, then edit the best video."**
The study is in `research/HOOK-STUDY.md` (8 of the channel's top 16 Shorts, first 2.4 s at 0.2 s steps). Applied here:
1. A 2-frame cover with the climax (the worry centre on fire, the bruised officer, the pill), as the #1, 15M and 13M videos do.
2. The stomach's face next to the food pipe, bigger, with thick angry brows; its eyes follow the pills down.
3. A "STOMACH" label box at the top; the body card pops in at 2.0 s, so the first second is clean.
4. A soft opening: music fades in from silence, the whoosh is quieter (first half second -25.6 dB; reference -28.7 dB).

**v3 QA (`how-sleeping-pills-actually-work-v3.mp4`):** 60.4 s; whisper 99.3% (146 of 147); -13.3 LUFS, peak -2.5 dB; frozen 0.3%; longest still 0.2 s. Hook compared at 11 moments (0-2.4 s) against the 27M and 10M videos.

## Upload block
**Title:** How Do Sleeping Pills Actually Work? 😴

**Cover frame:** the officer facing the three burning worry blobs (about 22 s).

**Description:**
"I've been fighting anxiety for days." 😴 How does a sleeping pill actually help you sleep? It is broken down in the stomach, reaches the brain through the blood, and boosts GABA, the brain's own calming signal. That quiets the "alarm" chemicals that keep a worried brain awake.

A cartoon for general education, not medical advice. Only take sleeping pills a doctor has prescribed for you.

#shorts #sleepingpills #insomnia #sleep #anxiety #health #humanbody #animation

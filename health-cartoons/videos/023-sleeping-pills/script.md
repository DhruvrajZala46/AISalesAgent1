# 023 - How Do Sleeping Pills Actually Work? (GiggleMD)

Status (25 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user's message named "Still craving food when you're full", but the attached mp4 was "How Do Sleeping Pills Really Work" (10M on Dr. Healthcare, `OJS2ONcmZ58`, in `research/NEXT-10.md` reserves; views as of 20 Nov, not re-checked). The video follows the attached file; the user was told.

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

## Upload block
**Title:** How Do Sleeping Pills Actually Work? 😴

**Cover frame:** the officer facing the three burning worry blobs (about 22 s).

**Description:**
"I've been fighting anxiety for days." 😴 How does a sleeping pill actually help you sleep? It is broken down in the stomach, reaches the brain through the blood, and boosts GABA, the brain's own calming signal. That quiets the "alarm" chemicals that keep a worried brain awake.

A cartoon for general education, not medical advice. Only take sleeping pills a doctor has prescribed for you.

#shorts #sleepingpills #insomnia #sleep #anxiety #health #humanbody #animation

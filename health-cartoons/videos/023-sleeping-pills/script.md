# 023 - How Do Sleeping Pills Actually Work? (GiggleMD)

Status (25 Nov 2026): **v6 built and delivered** (see the v6 section and `BLUEPRINT.md`). Waiting for the user's verdict. The user's message named "Still craving food when you're full", but the attached mp4 was "How Do Sleeping Pills Really Work" (10M on Dr. Healthcare, `OJS2ONcmZ58`, in `research/NEXT-10.md` reserves; views as of 20 Nov, not re-checked). The video follows the attached file; the user was told.

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

## v4 (25 Nov 2026): exactly the reference's look, only the characters ours
The user, with the reference again: **"5%... I want exactly the same video as this, only the characters mine. Don't change anything else. Keep it the same as the reference... the video editing style, everything."**

Everything the reference does not have was removed, and each scene was laid out from the reference's frames:
1. Removed: the 2-frame cover, the "STOMACH" box, both body cards, all labels (SLEEPING PILLS, PILL DISSOLVES, OFF TO THE BRAIN!, WORRY SIGNALS ON FIRE, THE CALMING SIGNAL, PILL BOOSTS THE CALMING SIGNAL, CALM. TIME TO SLEEP.), the dotted arrow, the "GABA" badge (now a plain police badge).
2. The worry centre's label is now the reference's: a small box at the top left, "Amygdala (Brain's Anxiety Centre)".
3. The intestines under the stomach are lumpy coils, as in the reference, not one long tube.
4. The officer is shorter and stands lower (feet at 86% of the height), as in the reference.
5. The sleeping pill is a small tablet that rolls in at the bottom left, as in the reference.
6. The bedroom: the wife sits on the bed edge, big, the husband stands close on the right, as in the reference.
7. Bug fixed: the husband had an orange glow round his clothes in v1-v3 (his shading clips were made after the picture was written, so the blur was not clipped). He is now built with the rest of the scene.

What stays ours: the drawings (code), the channel's patient as the husband, the voices, the music and the wording (one line of ours per line of theirs, same meaning).

**v4 QA (`how-sleeping-pills-actually-work-v4.mp4`):** 60.4 s; whisper 99.3% (146 of 147); -13.3 LUFS, peak -2.5 dB; frozen 0.3%; longest still 0.1 s. Checked on 16 reference-over-ours pairs of the final render and 8 large (360 px) pairs.

## v5 (25 Nov 2026): the brawl, the sound effects and the music, measured from the reference
The user, with a screenshot of the brawl: **"the police officer is outside, fighting; the sound effect the reference uses for it is not used at all. Watch the video, understand which sound effects there are and how the visuals look; everything exactly the same; no guessing."**

**How the reference's sound was mapped (not guessed):** the reference audio was split with demucs (voice / non-voice), loud moments in the non-voice part were found
(more than 6 dB over a rolling median), and each moment was labelled with an AudioSet classifier (MIT AST). Our own Mixkit library was labelled with the same classifier.

| Reference time | What the classifier hears | What happens | Ours (Mixkit id, same labels) |
|---|---|---|---|
| 0.16 s | Plop, boing | the pills drop | 2925 (Plop 0.77), 0.16 s |
| 21.7 s | Slap, door, whip, whack | the cut to the worry centre | 2151 (Whack, slap, whip), on the cut |
| 32.3-33.4 s | **Bang, gunshot, burst, explosion, slap** (the loudest moment, 4.6 dB over the median, peaks 9 dB) | the brawl cloud | 1714 (explosion, burst) + 8 hits from 2149, 2920, 2151, 772, 2980, 1464 over 1.1 s |
| 34.3 s | Jingle, ding | after the brawl | 1107 (ding, ding-dong, jingle) |
| 36.4 s | Whip, ping | the pill comes in | 2151, soft |
| 59.7 s | weak whoosh | the cut to the bedroom | 175, soft, before the first word |
| whole video | quiet music bed: double bass, cello, bowed strings, piano, organ | | Mixkit 508 "Jazz 2" (instrument-profile match 0.84; our old bed mixkit-9 scored -0.14) |

No fire sound in the reference, so ours has none (v1-v4 had flame flares, drips, a fizz, a bubble pop and a ding that the reference does not have).

**The brawl, from 0.2 s frames:** at "...this job" one big wobbling white cloud swallows the officer and the three blobs for 1.3 s; its outline changes every 0.1-0.2 s and sometimes
a puff stretches to the left; then it vanishes and the officer is back at his spot with a black eye and a plaster. v1-v4 drew small circles while the officer stood outside; v5 does what the reference does.

**Loudness:** the brawl is added after mastering (`post_mix.sh`), so the compressor does not flatten it: brawl 4.5 dB over the median (reference 4.6). The master is -14.5 LUFS (YouTube's own target), peak -1.0 dB.
Build (v5): LIM=0.46, BG=5. (v6: LIM=0.66, BG=12.).

**v5 QA (`how-sleeping-pills-actually-work-v5.mp4`):** 60.4 s; whisper 98.6% (145 of 147; "I'm" heard as "you're", "They" as "I"); frozen 0.3%; longest still 0.1 s. Brawl checked on 6 reference-over-ours pairs; our own SFX labelled by the same classifier (plop / whack-whip / bang-whack-slap / ding / whip, as in the reference).

## v6 (26 Nov 2026): the reference creator's visual DNA applied
The user sent 5 more videos by a creator whose style they love and asked: "decode their complete visual language, write a style guide and a scene-by-scene blueprint, and make my video in that style."
The decode is in `../../research/STYLE-DECODE.md`; the timestamped plan and the measured before/after check are in `BLUEPRINT.md`.

Changed from v5 (story, drawings, voices and SFX map unchanged):
1. **Captions:** Luckiest Guy 50 px (was 58), outline 2.5 px visible (was about 4), a small drop shadow, centred 78% down. They change on the word's first frame and pop 90% -> 125% -> 100% over 3 frames. They are held through pauses under 0.3 s.
2. **Static camera:** the slow breathing zoom on every frame is gone.
3. **Animation on twos:** drawings update 15 times a second (still frames 8.8% -> 51.9%; references 44-85%). Captions stay frame-accurate.
4. **Watermark:** "@GiggleMD" repeated 5 times, faint, 4 of them tilted, as in the references.
5. **Music bed:** 12 dB quieter, now about 17 dB under the voice (was 5.3 dB; references 13-22 dB).
6. **Master:** -12.3 LUFS (was -14.5; references -8.5 to -11.1, clipped); the brawl is still 4.5 dB over the median.
7. **Bug fixed:** a comment in `build_audio.py` had switched off the music's fade-in and fade-out.

**v6 QA (`how-sleeping-pills-actually-work-v6.mp4`):** 60.5 s; whisper 100% (147 of 147); -12.3 LUFS, peak -0.7 dB; still frames 51.9%; 15.6 drawing changes a second; caption timing +0.016 s from the word start (references -0.02 to +0.01 s); checked on 14 reference-over-ours pairs.

## Upload block
**Title:** How Do Sleeping Pills Actually Work? 😴

**Cover frame:** the officer facing the three burning worry blobs (about 22 s).

**Description:**
"I've been fighting anxiety for days." 😴 How does a sleeping pill actually help you sleep? It is broken down in the stomach, reaches the brain through the blood, and boosts GABA, the brain's own calming signal. That quiets the "alarm" chemicals that keep a worried brain awake.

A cartoon for general education, not medical advice. Only take sleeping pills a doctor has prescribed for you.

#shorts #sleepingpills #insomnia #sleep #anxiety #health #humanbody #animation

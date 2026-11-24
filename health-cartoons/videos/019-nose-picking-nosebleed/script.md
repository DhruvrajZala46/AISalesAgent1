# 019 - How Picking Your Nose Can Make It Bleed (GiggleMD)

Status (24 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (018).

## The reference the user sent
A 55.5 s vertical video by Dr. Healthcare, "How picking your nose…" (the user's mp4; views not measured here).
- Inside the nose: a finger picks at dry mucus, the lining (with a face) cries out and starts to bleed.
- The nose from the front: blood runs, the patient wipes it with tissue again and again, then plugs the nostril with a rolled tissue (with a face) that soaks through.
- The side view: the patient leans forward and pinches the nose.
- The clinic: the patient asks why one pick made it bleed; the doctor explains the cause and the first aid.
- It ends on a call to subscribe (not copied; we have no CTA and no outro).

## What we kept, and what is ours
- **Kept:** every scene, their order and staging; each beat and who speaks it; the sound moments (scratch, drip, wipe, plug, pinch).
- **Ours:** all drawings (code), the channel's doctor and patient, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 6 recorded lines, 114 words).
- **Added for clarity (LEARNINGS rows 27, 28):**
  - a body card "INSIDE THE NOSE" with a pulsing ring;
  - labels DRY MUCUS, TINY BLOOD VESSELS, SCRATCH!, IT BLEEDS, TISSUE, STILL BLEEDING!;
  - step labels 1. LEAN FORWARD / 2. PINCH THE SOFT PART / 3. HOLD 10-15 MIN with a clock;
  - a "15 MINUTES LATER" card;
  - a "NOSEBLEED?" board in the clinic whose four rows pop in on the doctor's words.
- **Facts (standard first aid):** lean forward, not back; pinch the soft part of the nose; hold steadily for 10 to 15 minutes; get it checked if it has not stopped.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `vB4Ye6o0li9oOR7xlcEE`, 1 take per line (`takes_manifest.tsv`, `voices.txt`): lining = Goofy Cartoon Kid, tissue = Laura, patient = Chill, doctor = Hope.
- SFX: Mixkit files in `sfxgen/`; clicks and thuds are synthesised in `build_audio.py`. Music: ducked.
- Art, all code: `world_019.js` (`insideNose`, `frontNose`, `profile`, `clinic19`), `parts_019.js` (all motion), `assemble_019.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 6 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_019.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`how-picking-your-nose-makes-it-bleed.mp4`)
- Length 48.3 s (reference 55.5 s with its CTA); first word at 0.45 s.
- Speech: whisper on the final mix 96.5% (110 of 114), below the 97% target. The misses: "Picking" heard as "Kicking"; "nosebleeds" written "nose bleeds"; "ten" and "fifteen" written as digits.
- Loudness -11.8 LUFS, peak -2.0 dB.
- Frozen frames 3.7%; longest still stretch 0.8 s.
- Checked on reference-over-ours tiles (9 moments, first render) and on twenty 330 px frames of the final render.

**Fixed after the first sheets:** the front nose was small; the inside cut did not show a nostril; the lining's face was small; the pinching hand was two plain bars; the step labels were small.

Still different from the reference: its side-view hand is drawn in full, ours shows the two pinching fingers; ours has the body card, labels and board it does not have.

## Upload block
**Title:** How Picking Your Nose Can Make It Bleed 😳

**Cover frame:** the finger at the dry mucus with the lining's worried face (about 0.3 s).

**Description:**
"I only picked my nose once!" 😳 Picking at dry mucus can scratch the lining of the nose and damage the tiny blood vessels inside. Dry air and allergies can cause nosebleeds too. What to do: lean forward, pinch the soft part of your nose, and hold steady for 10 to 15 minutes. If it still hasn't stopped, get it checked.

A cartoon for general education, not medical advice.

#shorts #nosebleed #nosepicking #health #humanbody #healthfacts #firstaid #animation

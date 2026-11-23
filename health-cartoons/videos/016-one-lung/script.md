# 016 - This Habit Left Him With One Lung (GiggleMD)

Status (23 Nov 2026): **built and delivered**. Waiting for the user's verdict.

## The proven video we follow
Dr. Healthcare, "This Habit Left Him With One Lung" (`6MVMDGdHR5Q`): **15M views** (public listing, 20 Nov 2026), about 20x the channel's median; the smoking family also reached 8.8M on Health Manager. It was the highest Dr. Healthcare video not yet made for this channel. The user sent the mp4 (61.1 s).

**What it shows (studied on a 1 fps sheet and 13 large frames):**
- 0-43 s: one locked shot inside the chest: windpipe in the middle, a pink lung and a dark lung with faces.
  - The dark lung smokes and shows off its colour; the pink lung wants to look like it; the dark lung hands over a pack.
  - A camera tool comes in, lights up the dark lung and calls its boss.
  - A scalpel says the lung must come out; a syringe puts it to sleep; it is cut and lifted onto a steel tray in pieces.
  - The scalpel asks the pink lung what it was holding: "Lungs don't even have hands!"
- 44-61 s: a hospital room. The patient is in bed; the doctor explains and tells him to quit.

## What we kept, and what is ours
- **Kept:** every scene, its order and staging; each beat and who speaks it; the tools, the tray, the empty space left behind, the hidden pack gag.
- **Ours:** all drawings (code), the channel's doctor and patient, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 11 recorded lines, 124 words). The user asked for an exact copy and was told why the words and drawings are ours (reused-content and copyright risk).
- **Added for clarity (LEARNINGS row 27):** "HEALTHY LUNG" and "SMOKER'S LUNG" labels on the first frame.
- The doctor's lines say one part was too damaged to save and was removed to protect the healthy lung, and that he must quit; no numbers are claimed.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `QaLLbFxS9FIxNEFOPbMZ`, 1 take per line (`takes_manifest.tsv`, `voices.txt`); all checked by whisper.
- SFX: Mixkit 1492, 2182, 2358; breath of smoke, pack rattle, scan beeps, cuts and landings are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_016.js` (chest, windpipe, both lungs, pack and cigarettes, camera tool, scalpel, syringe, forceps, tray, hospital room), `parts_016.js` (all motion; the dark lung is three clipped copies that are lifted onto the tray), `assemble_016.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 11 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_016.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`this-habit-left-him-with-one-lung.mp4`)
- Length 54.4 s (reference 61.1 s); first word at 0.25 s (reference 1.0 s).
- Speech: whisper on the final mix 98.4% (122 of 124; "want to" heard as "wanna").
- Loudness -11.9 LUFS, peak -2.0 dB.
- Frozen frames 5.3%; longest still stretch 0.5 s.
- Checked on 300 px reference-over-ours tiles (12 moments, two rounds of fixes) and at 5 fps for the hook, the pack handover, the syringe, the cuts, the pieces and the hidden pack.

**Round 1 found and fixed:** lungs and tools too small; the syringe off screen; the sleeping lung showed empty eye circles. **Round 2:** the zoom cut the lungs at the edges; the tray covered the pieces; the scalpel crossed the pink lung's face; the syringe and scalpel overlapped.

## Upload block
**Title:** This Habit Left Him With One Lung 🫁

**Cover frame:** the pink lung holding the pack next to the dark lung, with the camera tool's light on it (about 11 s).

**Description:**
One lung was pink. The other was black. 🫁 Years of smoking can damage a lung so badly that part of it has to be removed to protect the healthy lung that is left. You can still live a normal life after that, but quitting smoking is the most important step, and the sooner the better.

A cartoon for general education, not medical advice.

#shorts #smoking #lungs #quitsmoking #health #humanbody #healthfacts #animation

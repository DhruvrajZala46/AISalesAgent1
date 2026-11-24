# 019 - How Picking Your Nose Can Make It Bleed (GiggleMD)

Status (24 Nov 2026): **v3 built and delivered** (see the v3 section). Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (018).

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

## v2 (24 Nov 2026, after the user's verdict on v1)
The user sent the reference again: **"I want the video exactly the same as the reference: visuals, music, voice, everything."**

What v1 got wrong against the reference (found on large tiles), and what v2 changed (drawings and motion only; the voices are the same takes):
1. The inside-nose cut was a leaf shape with a body card and labels. **Now:** the reference's staging: a large nose from the side, the red cavity filling it, big eyes at the top, the nostril as an oval at the bottom, the finger coming up through it.
2. One hand wiped with a round tissue. **Now:** both hands bring a large tissue up from below.
3. The tissue was a plug pushed into the nostril. **Now:** a hand holds up a small ball of tissue that turns pink and gets a worried face, while the nose keeps bleeding (as in the reference).
4. The side view showed a whole head with hair, labels and a clock. **Now:** a close view of the brow, closed eye, nose and mouth with a hand pinching the nose.
5. The clinic had a board and close busts. **Now:** the reference's two-shot: olive wall, floor, the desk, the doctor behind it, the patient holding up the stained tissue. No board, no labels.
6. Removed in v2: the body card, every label, the clock, the board, and their pop sounds.

Not copied, on purpose: the reference's audio. Its voice recordings and its music track cannot be reused (copyright and reused-content strikes); ours are our own voices of the same character types and a library track of a similar mood. The wording stays ours, line for line the same meaning. The doctor and patient stay the channel's own.

**v2 QA (`how-picking-your-nose-makes-it-bleed-v2.mp4`):** 48.3 s; whisper 96.5% (110 of 114, the same four misses); -11.8 LUFS; frozen 10.4% (the clinic is a still two-shot, as in the reference); longest still 1.1 s. Checked on reference-over-ours tiles (9 moments) of the final render.

Still different from the reference: its clinic shows both people full length, ours shows them from about the knee up; its pinching hand shows curled fingers, ours shows two fingers and part of the palm.

## v3 (24 Nov 2026, after the user's verdict on v2)
The user: **"VERY BAD VIDEO, 5%... I can't understand what that body part is... study that viral video, compare their visual storytelling with what you made."** (the same verdict as 015 v1 and 018 v1).

The cause: v1 and v2 were drawn from a 1 fps sheet, so the reference's acting was missed. v3 was built from sheets at 0.4 to 0.6 s steps. What they showed, and what changed:
1. The reference opens with a fat finger already deep in the nose; it comes out, goes back in and scrapes for 1.6 s before the scream. Ours touched for 0.3 s. **Now:** the same in-out-in-scrape, with the nostril rim drawn over the finger so it reads as going inside.
2. The lining barely reacted. **Now:** eyes squeezed shut and a big open mouth on the rip, a teary look, then wide eyes on the blood.
3. The blood was a straight bar. **Now:** a wobbly stream that wells up in the wound, runs out of the nostril and drips.
4. The front nose was a three-lobed cloud shape. **Now:** a smooth nose outline with wings, nostrils and bridge shading.
5. There were two wipes; the reference has three, with a sniff before the second and third. **Now:** three wipes and two sniffs.
6. The tissue ball was only held up. In the reference a hand rolls it, pushes it into the nostril, and it comes back out pink with a face; the bleeding stops, then starts again on "still bleeding". **Now:** that whole beat.
7. The pinching hand was two bars. **Now:** a fist with thumb and finger; the head leans and moves in, and the mouth opens to breathe.
8. The clinic showed people from the knee up. **Now:** full length, with the desk and the hanging stained tissue.
9. The audio timeline was rebuilt around these beats (51.4 s).

**v3 QA (`how-picking-your-nose-makes-it-bleed-v3.mp4`):** 51.4 s (reference 55.5 s); whisper 97.4% (111 of 114; "Picking" heard as "Kicking", "ten" and "fifteen" written as digits); -11.9 LUFS; frozen 9.0% (the clinic is one still two-shot, as in the reference); longest still 0.8 s. Checked on 16 reference-over-ours pairs of the render and a 6-frame sheet of the tissue beat.

Still different from the reference: its hands are drawn with more detail than ours; the audio, the wording and the doctor and patient are ours, as explained in v2.

## Upload block
**Title:** How Picking Your Nose Can Make It Bleed 😳

**Cover frame:** the finger at the dry mucus with the lining's worried face (about 0.3 s).

**Description:**
"I only picked my nose once!" 😳 Picking at dry mucus can scratch the lining of the nose and damage the tiny blood vessels inside. Dry air and allergies can cause nosebleeds too. What to do: lean forward, pinch the soft part of your nose, and hold steady for 10 to 15 minutes. If it still hasn't stopped, get it checked.

A cartoon for general education, not medical advice.

#shorts #nosebleed #nosepicking #health #humanbody #healthfacts #firstaid #animation

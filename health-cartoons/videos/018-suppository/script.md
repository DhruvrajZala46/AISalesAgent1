# 018 - How Does a Suppository Fix Constipation? (GiggleMD)

Status (24 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (017).

Note: the user first sent a 135 s period/poop video by @humanbodysquad (about 10 sets, no doctor). It was studied but not built; the user sent this shorter reference instead.

## The reference the user sent
A 70.6 s vertical video by @dr_healthsimplified (the user's WhatsApp file; views not measured here).
- 0-24 s: one locked cut-away: the rectum (a red tube with a face) bending right at the top, hard stool lumps stuck in the bend (one with a face), skin, and below it a blue gloved hand with a face holding a white suppository.
  - The rectum protests ("this is an exit"), the glove explains, the suppository goes in and melts, the stool softens and slides out.
- 25-66 s: a hospital room; the patient in bed asks, the doctor explains (melts, draws water in, irritates the wall, works where the problem is).
- It ends on "like and subscribe" and an end card with the creator's handle (neither copied; we have no CTA and no outro).

## What we kept, and what is ours
- **Kept:** both scenes, their order and staging; each beat and who speaks it; the melt, the softening and the exit.
- **Ours:** all drawings (code), the channel's doctor and patient, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 10 recorded lines, 135 words).
- **Added for clarity (LEARNINGS row 27):** RECTUM, HARD STOOL and SUPPOSITORY labels; a "HOW IT WORKS" board in the hospital room whose four rows pop in on the doctor's words (the reference's clinic is a static two-shot for 40 s).
- **Fact changed:** the reference says "sometimes in under 30 minutes"; ours says "often within fifteen minutes to an hour", the usual label range for glycerin suppositories.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `mCRRgSk1gzsI9vOv6Y70`, 1 take per line (`takes_manifest.tsv`, `voices.txt`), checked by whisper.
- SFX: Mixkit 1492, 2182, 2256, 2357, 2358, 2364; clicks and thuds are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_018.js` (body cut-away, rectum, stool lumps with a hard and a soft look, glove, suppository, the board, the hospital room from 016), `parts_018.js` (all motion), `assemble_018.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 10 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_018.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`how-a-suppository-works.mp4`)
- Length 52.3 s (reference 70.6 s with its CTA and end card); first word at 0.2 s.
- Speech: whisper on the final mix 97.8% (132 of 135; "fiber" heard as "fiverr", "Doc" as "Doug", "fifteen" written as "15").
- Loudness -11.9 LUFS, peak -1.8 dB.
- Frozen frames 0.6% (15.1% before idle motion was added); longest still stretch 0.7 s.
- Checked on 290 px reference-over-ours tiles (10 moments), at 5 fps for the hook, the insert, the melt and the exit, and on four 360 px frames of the final render.

**Fixed after the first sheets:** the melted patch covered the rectum's face; the board covered the doctor's head; the caption covered the glove's face; faces were small; long still stretches.

## v2 (24 Nov 2026, after the user's verdict on v1)
The user: **"VERY BAD VIDEO, 5%... I can't understand what that body part is... a 5-year-old or a 60-year-old cannot understand this. I want it easiest to understand VISUALLY... compare their visual storytelling with what you made."** (the same verdict as 015 v1; row 27's rule was not applied well enough).

What the large reference-over-ours tiles showed, and what v2 changed (drawings and motion only; the audio is the same):
1. Nothing showed where in the body this is, and the skin line was a flat wave. **Now:** a small body card with the gut and a pulsing ring ("INSIDE HERE"), and the skin below is drawn as two round cheeks.
2. The stool looked like coffee beans. **Now:** lumpy, shaded poop shapes; dark and cracked when hard, lighter and glossy when soft.
3. The glove was an odd three-finger shape. **Now:** a hand with a cuff, knuckles, and a thumb and finger pinching the suppository.
4. The melt was one pink patch. **Now:** water fills the tube from the suppository up to the stool (as in the reference), with drops.
5. Nothing said what was happening. **Now:** a step label at each beat: IT MELTS, WATER COMES IN, POOP GETS SOFT, OUT IT GOES!
6. The stool fell into empty space. **Now:** a toilet slides in and each piece drops into it with a splash; the glove steps aside.
7. Hard words. **Now:** HARD POOP instead of HARD STOOL; the board says "PULLS WATER INTO THE POOP".
8. The gut ended in a plain pipe. **Now:** scalloped bumps on the part that continues to the right.

**v2 QA (`how-a-suppository-works-v2.mp4`):** 52.3 s; whisper 97.8% (132 of 135); -11.9 LUFS; frozen 0.0%; longest still 0.4 s. Checked on 290 px reference-over-ours tiles (10 moments) of the final render.

Still different from the reference: its faces have larger eyes; ours keep the inset card and labels it does not have.

## Upload block
**Title:** How Does a Suppository Actually Fix Constipation? 😳

**Cover frame:** the rectum looking down at the glove holding the suppository, hard stool above (about 5 s).

**Description:**
"This is an exit!" 😳 So how does a suppository help with constipation? A glycerin suppository melts once it's inside the rectum. It pulls water toward the stool and softens it from the inside, and it gently irritates the rectal wall, which triggers the urge to go. It works right where the problem is, often within 15 minutes to an hour.

A cartoon for general education, not medical advice. If constipation keeps coming back, see a doctor.

#shorts #constipation #suppository #guthealth #health #humanbody #healthfacts #animation

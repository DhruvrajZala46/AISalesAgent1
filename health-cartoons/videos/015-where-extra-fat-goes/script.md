# 015 - Where Does the Extra Fat Go? (GiggleMD)

Status (23 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (014 v2).

## The reference the user sent
An 88.6 s Dr. Healthcare Short (the user's WhatsApp file; views not measured here). Five scenes:
1. 0-13 s: the liver lifts a barbell under a layer of fat and complains.
2. 13-54 s: a corridor labelled "INSIDE THE LIVER". An insulin blob pushes a wheelbarrow of fat past doors FAT STORAGE A, B and C; each gets a "STORAGE FULL" sign. A second insulin arrives and they talk.
3. 54-57 s: they tip the fat into BODY FAT STORAGE.
4. 57-60 s: a body with yellow fat growing on it.
5. 60-88 s: a clinic. The patient stands on a scale; the doctor explains.

## What we kept, and what is ours
- **Kept:** all five scenes, their order and staging, the door labels and the "STORAGE FULL" gag, the speakers of each beat.
- **Ours:** every drawing (code), the channel's doctor and patient, and the wording. One line of ours per beat of theirs; never word for word (`lines.tsv`, 15 recorded lines, 200 words).
- **The doctor's lines were changed for accuracy.** The reference says the liver fills up first and then sends fat to the body, and that the patient "gained three times more". Ours says: more calories than you burn; insulin tells the body to store the extra as fat; it fills the fat cells and can build up in the liver too; cut the extra calories, eat lighter, move every day.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `FFUwsmWO79fR3peXEY7a`, **1 take per line** to save credits (`takes_manifest.tsv`, `voices.txt`); every take was checked by whisper (14 of 15 with no word errors).
- SFX: Mixkit 1492, 2182, 2357, 2358, 2364; steps, knocks, barbell clicks and the wheel squeak are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_015.js` (liver gym, corridor and doors, insulin blobs, wheelbarrow, body, clinic with the scale), `parts_015.js` (all motion), `assemble_015.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 13,15 && python3 -I ../../tools/tighten.py proc 0.3 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_015.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`where-does-the-extra-fat-go.mp4`)
- Length 77.4 s (reference 88.6 s); first word at 0.0 s.
- Speech: whisper on the final mix 97.5% (195 of 200; misses are grunts and "Doc": "Ugh", "Whoa").
- Loudness -11.9 LUFS.
- Frozen frames 8.3%; longest still stretch 0.6 s.
- Checked on a reference-vs-ours sheet (12 frames each) and at 5 fps for the hook, the first knock and the tip into BODY FAT STORAGE.

## v2 (23 Nov 2026, after the user's verdict on v1)
The user: **"VERY BAD VIDEO, 5%... I can't understand what that body part is or what you are talking about. A 5-year-old or a 60-year-old cannot understand this. I want it easiest to understand VISUALLY... compare their visual storytelling with what you made."**

What a large reference-over-ours sheet showed (the main ones):
1. Their liver looks like a liver: a big wedge with the stomach and the intestines under it. Ours was a brown oval floating in pink, with a pink blob and wavy lines.
2. Nothing in ours was labelled.
3. Their fat drips like melted cheese; ours was smooth icing.
4. Their wheelbarrow carries the same lumpy yellow fat that sits on the liver. Ours carried gold balls, so the two never read as the same thing.
5. Their doors fill half the frame and the door name and "STORAGE FULL" can be read at once. Ours were small; the sign could not be read.
6. Their insulin has big eyes high on its body. Ours had small eyes hidden behind the wheelbarrow.
7. The top half of our corridor frame was empty.
8. Our second insulin stood on top of the wheelbarrow and the door.
9. Our liver had long dangling arms; theirs has short arms holding the bar.
10. Our liver and barbell were small; theirs fill the frame.
11. Their patient is clearly overweight (the story's payoff); ours was slim.
12. Nothing told the viewer that the corridor is inside the liver.

What v2 changed (drawings and motion only; the audio is the same):
- Scene 1 redrawn: a liver-shaped liver with its lobe line, dripping lumpy fat, a J-shaped stomach, intestines, the food pipe; labels LIVER, FAT, STOMACH on the first frame; a bigger face and barbell.
- A zoom into the liver before the corridor, and the "INSIDE THE LIVER" tag.
- Corridor redrawn: doors 392 px wide with 54 px names and a 34 px "STORAGE FULL"; a taller insulin with big eyes above the wheelbarrow; the same lumpy, dripping fat in the wheelbarrow; the second insulin stands just behind the first.
- Body scene: the belly grows more and a "BODY FAT" label pops.
- Clinic: the patient has a belly.

**v2 QA (`where-does-the-extra-fat-go-v2.mp4`):** 77.4 s; whisper 97.5% (195 of 200); -11.9 LUFS; frozen 6.9%; longest still 0.6 s. Checked on a reference-over-ours sheet and at 5 fps for the hook, the zoom, the first knock, the second insulin's entry, the tip and the body scene.

## Upload block
**Title:** Where Does All the Extra Fat Go? 🍔

**Cover frame:** insulin with the wheelbarrow of fat in front of the "STORAGE FULL" door (about 17 s).

**Description:**
Ever wondered where the extra calories end up? 🍔 When you eat more than you burn, insulin tells your body to store the extra as fat. It fills up your fat cells, and it can build up in your liver too. That's how the weight creeps up! The good news: you can turn it around. Cut the extra calories, eat lighter, and move every day.

A cartoon for general education, not medical advice.

#shorts #weightloss #bodyfat #insulin #liver #health #healthfacts #animation

# 013 - Why Is Bouncing Your Leg Actually Good for You? (Dr. Mira Explains, video 2)

Status (23 Nov 2026): **built and delivered**. Waiting for the user's verdict.

## The reference the user sent
A 55.4 s vertical video by @insideyou.science (sent as a WhatsApp file on 23 Nov 2026). The user asked for the exact same video.
Its view count was not measured here (the file carries no public numbers).

**How it was studied:** frame sheets at 1, 5 and 30 fps; whisper transcript with timings (27 segments); voice and music split
(demucs); pitch per speaker; loudness; the bounce measured frame by frame.

**What it showed:**
- One set for the whole video: a cut-away lower leg, with camera cuts between a wide shot and close shots (about 1.33-1.4x).
- The leg bounces at 4 taps a second; the heel lifts about 35 px.
- A narrator doctor in a round bubble from 18.6 s, talking over the leg.
- Almost no music: taps, doorbell dings, marimba notes and an end sting. Loudness -17 LUFS.
- An end card with a logo.

## What we took, and what is ours
We did **not** make a word-for-word, frame-for-frame copy. That would be another creator's work under our name, and it risks a
reused-content or copyright strike on a new channel. The user was told this before the build.

| Angle | Reference | Ours |
|---|---|---|
| Topic and science | leg bouncing, the calf muscle pump ("second heart"), one-way valves, the fidgeting study | the same topic and the same facts, checked against the study |
| Story | theirs | **ours: "the elevator in your leg".** Blood cells are passengers stuck at the ankle, the vein is the lift shaft, the calf muscle is the lift ("I only pump when he moves"), the valve is a door guard ("Up only. No exceptions.") |
| Words | theirs | all our own (18 lines, 157 words) |
| Characters and art | theirs | ours, all drawn in code: two blood cells, the calf with a sweatband, the valve guard with a cap, a teal sneaker, Dr. Mira and the patient |
| Format ideas kept | camera cuts between wide and close; a 4 Hz bounce; the explanation shown on the leg itself | the same ideas: wide, two-shot and close shots; a 4 Hz bounce; the doctor's words replayed on the leg |
| Sound | SFX only, -17 LUFS | the 012 recipe: music bed ducked under speech, an SFX on every event, -11.8 LUFS |
| Ending | a logo end card | no outro: Dr. Mira says "Get up and walk", and the patient gets up and walks out |

## The script (final)
See `lines.tsv` (with the voice tags) and `lines.txt`.

1. Cell A: Hey! Is this elevator broken?!
2. Cell B: We've been stuck at the ankle for three hours!
3. Cell A: Yo, Calf! We need a lift up to the heart!
4. Calf: Can't. He hasn't moved in hours. I only pump when he moves.
5. Valve: And I'm a one-way door. Up only. No exceptions.
6. Cell B: Wait... why is the floor shaking?
7. Calf: He's bouncing his leg! That's my cue!
8. Calf: Squeeze! Going up!
9. Cell B: Woo-hoo!
10. Valve: Up only. Door closed.
11. Calf: That's why they call me the second heart.
12. Partner (off screen): Ugh! Can you stop shaking the whole couch?!
13. Cell A: No, no, no! Keep bouncing!
14. Patient: Doc, everyone says stop bouncing my leg. Is it bad?
15. Dr. Mira: Not for your blood flow. Each calf squeeze pushes blood up your veins, back to your heart.
16. Dr. Mira: One-way valves keep it from sliding back down.
17. Dr. Mira: In a small study, people sat for three hours. Blood flow dropped in the still leg and rose in the fidgeting one.
18. Dr. Mira: But the best fix is simple. Get up and walk.

## Shots
| Time | Shot |
|---|---|
| 0-2.5 s | close on the cells piled under the shut valve; cell A jabs the call button (label: VEIN) |
| 2.5-5 s | wide: the whole lower leg, the sneaker flat on the floor, the couch |
| 5-8.9 s | two-shot: the cells below, the sleepy calf above (label: TO THE HEART) |
| 8.9-12.8 s | close on the calf (label: CALF MUSCLE) |
| 12.8-16 s | close on the valve guard (label: VALVE) |
| 16-19 s | wide: the heel starts tapping, 4 times a second; the couch shakes |
| 19-22.4 s | the calf wakes up: "That's my cue! Squeeze!" |
| 22.4-24.3 s | "Going up!": the lift dings, the cells shoot up the vein, the camera follows |
| 24.3-26.3 s | the valve snaps shut behind the last cell |
| 26.3-28.9 s | the smug calf with sparkles (label: SECOND HEART) |
| 28.9-31.8 s | wide: the partner shouts, a "!!" burst |
| 31.8-34.9 s | the leg stops: the cells slide back and the valves catch them; cell A lands on the pile ("Keep bouncing!") |
| 34.9-40.1 s | Dr. Mira's clinic; the patient is still jiggling his leg |
| 40.1-46.4 s | **replay inside the leg on the doctor's words:** the squeeze and a heart at the top, then the valves catching the blood (label: ONE-WAY VALVE) |
| 46.4-52.8 s | clinic; a card pops up: "AFTER 3 HOURS SITTING", still leg (blue arrow down) and fidgeting leg (green arrow up) |
| 52.8-56.6 s | "Get up and walk": the patient stands up and walks out |

## Facts
- **The calf muscle pump:** when the calf contracts, it squeezes the deep leg veins and pushes blood up toward the heart. One-way
  valves in the veins open for that flow and close when the muscle relaxes, so the blood cannot fall back. "Second heart" is a
  nickname for this pump.
- **The study:** Morishima et al., 2016, American Journal of Physiology - Heart and Circulatory Physiology, "Prolonged
  sitting-induced leg endothelial dysfunction is prevented by fidgeting" (https://pmc.ncbi.nlm.nih.gov/articles/PMC4967200).
  - 11 young healthy adults sat for 3 hours. One leg fidgeted (1 minute on, 4 minutes off); the other stayed still.
  - Blood flow in the knee artery fell in the still leg and rose in the fidgeting leg while it moved.
  - The still leg's artery function got worse; the fidgeting leg's did not.
  - The authors say fidgeting does not replace walking. Our last line says the same.
- Limits we keep in the words: "a small study", and "the best fix is ... get up and walk".

## How it was made (media is never committed; this re-creates it)
**Voices:**
- ElevenLabs `eleven_v4`, flow `ZNrvkdwc06K8SFtEm4f7`, 2 takes per line. Session ids are in `takes_manifest.tsv`; the cast is in `voices.txt`.
- `score_takes.py` scored all 36 takes: 33 had no word errors.
- `prep_voice.py` picks the take (line 04 is forced to take b, which keeps "Can't." as its own beat). No pitch shifts; one pace per character.

**SFX:**
- ElevenLabs `eleven_text_to_sound_v2`: an elevator ding and a power-down (in `sfxgen/`, git-ignored).
  - `sfxgen/down_fast.wav` is the power-down sped up about 3.8x.
  - `sfxgen/whistle_down.wav` is Mixkit 616 reversed.
- The heel taps are synthesised in `build_audio.py` (a low thud plus a tiny click), 4 a second.
- Plus Mixkit 2364, 1486, 2357, 1492, 2182 and 2256.
- Music: mixkit-9, ducked 5 dB under speech.

**Art (all code, no AI images):**
- `world_013.js`: the leg cut-away (skin, shin bone, artery, calf muscle, vein, two valves, call panel, sock, sneaker), the room,
  the study card with two small legs, the heart icon, and the teal clinic.
- `parts_013.js`: all motion.
  - The bounce: the heel lifts 21 px, 4 times a second; the sneaker turns about its toes; the couch shakes.
  - The pump: each tap moves the blood column up 62 px; the valves open on the squeeze and shut in between.
  - The stop: the cells slide back and settle on the closed valves.
  - The replay (`renderReplay`): the same leg scene at a remapped time, with mouths and story acting switched off.
- `assemble_013.py`: 001's engine and the doctor/patient.

**Build:** `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.14 15,16,17,18 && python3 -I ../../tools/tighten.py proc 0.22 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_013.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-is-bouncing-your-leg-good-for-you.mp4`)
| Measure | 013 | 012 (the standard) |
|---|---|---|
| Length | 56.6 s | 68.5 s |
| Speech (whisper on the final mix) | **99.4%** (156 of 157 words; only the "Ugh" grunt was missed) | 97.8% |
| Loudness | -11.8 LUFS, peak -2.1 dB | -11.9 LUFS, peak -2.0 dB |
| Frozen frames | 10.5% | 15.1% |
| Longest still stretch | 0.6 s | 1.1 s |
| First word | 0.6 s | 2.45 s |
| Clinic starts at | 61.6% of the runtime | 77% |

Frames were checked on sheets for every shot, and at 5 fps for the hook, "Going up!", the valve shutting, the stop, the cut into
the replay and the ending.

**Honest limits:**
- This is our own video on the reference's topic, not the exact copy the user asked for.
- The reference's view count is unknown, so "proven" rests on the topic and the format, not on a measured number.
- No video is guaranteed to go viral.

## v2 (23 Nov 2026, after the user's verdict on v1: "still 20% there... hook, visuals, engaging elements")
Pair sheets against the reference (hook at 5 fps, whole video every 5 s) showed why v1 was weak:
- **Hook:** the reference bounces from frame 0 and speaks at 0.0 s ("stop bouncing your leg": the viewer's own habit). v1 opened on a still pile of cells, spoke at 0.6 s, and the leg did not move for 16 s.
- **Characters:** theirs are big, every cell has a face. Ours were small, most cells had no face, and half the frame was beige bone.
- **Colour:** theirs is bright (sky blue, orange shoe). Ours was pale mint with a teal shoe on a teal-ish wall.
- **It never leaves the leg:** the doctor talks in a bubble over the action. v1 cut to a static clinic for 22 s.
- **The elevator idea** (button, lift, guard bar across the vein) added a layer the viewer had to decode.

What v2 changed (still our own words, art and characters):
- New order: the partner's line is on frame 0 over the bouncing leg; he stops; the cells slide back and the valve catches them; the calf will not pump; it gets crowded; the leg starts again; "Going up!"; second heart; Dr. Mira.
- 6 new lines recorded (2, 3, 4, 5, 7, 8). The Quibble voice was disabled by its owner, so cell B keeps only its two old lines.
- New set: bright blue wall, yellow couch, coral sneaker, a wide vein, a second muscle instead of bare bone, a big calf face, 30 cells with faces, a small valve guard on the vein wall.
- The cells are a small simulation (`SIM` in `parts_013.js`): they ride up on each squeeze, slide back when the leg stops, and stack on the closed valves.
- Dr. Mira explains from a round bubble; the study card pops over the leg; at "Get up and walk" the leg walks out of frame.

**v2 QA (`why-is-bouncing-your-leg-good-for-you-v2.mp4`):** 50.0 s; first word at 0.0 s; whisper 98.0% (144 of 147; missed "Sorry", and heard "calf"/"can't" as "cat"); -11.9 LUFS; frozen 2.2% (v1: 10.5%); longest still 0.3 s (v1: 0.6 s). The script list, shot table and QA table above describe v1; `lines.tsv` holds the v2 script.

## Upload block
**Title:** Why Is Bouncing Your Leg Actually Good for You? 🦵

Other options: "Your Calf Is Your Second Heart ❤️" / "Why You Shouldn't Stop Bouncing Your Leg".

**Cover frame:** the smug calf muscle with sparkles and the "SECOND HEART" label (about 28 s).

**Description:**
Do you bounce your leg when you sit? 🦵 Your calf muscle works like a pump: every squeeze pushes blood up your leg veins, and
one-way valves stop it from sliding back down. That's why people call the calf your "second heart"! In one small study, people sat
for 3 hours: blood flow dropped in the leg they kept still and rose in the leg they fidgeted with. Fidgeting helps a little, but the
best fix is simple: get up and walk.

A cartoon for general education, not medical advice. Source: Morishima et al., 2016, American Journal of Physiology (fidgeting
during 3 hours of sitting).

#shorts #legbouncing #secondheart #bloodflow #health #humanbody #healthfacts #animation

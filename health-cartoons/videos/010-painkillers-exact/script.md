# 010 - How Do Painkillers Actually Find the Pain? (exact copy)

Status (22 Nov 2026): **built** on the user's order: "NOW EXACTTT THISSS VIDEOOO COPY KREEE.... EXACT SAME VISUALS, EXACT SAME SOUND EFFECTS,
SAME AUDIO, SAMEEEE SCRIPTTTT EVERTHING MUST BE SAMEEEE". Earlier (009) the user also said "ONLYYY JO MERAAA CHARACTERR HONA CHAHEEEEE":
only the characters are ours. Waiting for the user's verdict.

**Reference:** the Dr. Healthcare Short "How do painkillers actually find the pain?" (**21M views**), the same video that 008 remade
in our own words. The user sent it as a WhatsApp file (22 Nov, 5:09 PM; 80.4 s, 720x1280).
- It was studied at 1 fps and 5 fps, with full-size frames for every set.
- Every set was measured in pixels: positions, sizes and colours.
- Every sound moment was mapped.
- Voice pitch was measured for each speaker.

**What is the same as the reference:**
- The script, word for word (36 lines, `lines.tsv`).
- The scene order and every set: the INTRAVASCULAR SPACE wall with its cut, the stomach close-up, the VEIN, the two tunnels, the boarded-up cut, and the clinic.
- Staging and positions, measured on its frames.
- The sound moments.
- The music bed under the voices.
- Captions: one word at a time in white Luckiest Guy caps at y 981-1015. Every word is the same size and pops in. This was measured; the reference has no key-word sizing.
- Labels: only INTRAVASCULAR SPACE and VEIN, as in the reference.

**What is ours:**
- The characters, drawn in code in the 001 / 003-v1 style (user rule, 22 Nov 2026; no image model):
  - the guard is our egg-shaped officer cell (`chars.js`);
  - our capsule painkillers (`chars_010.js`);
  - our red blood cells;
  - our spiky prostaglandin, with the name band from the reference spelled correctly. The reference spells it "PROSTAGLADIN".
  - 001's code doctor and patient.
- The voices: ElevenLabs, pitch-matched to each reference speaker.

## The reference, shot by shot (80.4 s), and where it sits in ours (84.7 s)

| Reference | Set | What happens | Ours |
|---|---|---|---|
| 0.0-21.0 | A: vessel wall, label "INTRAVASCULAR SPACE" | The cut slices open from the top (0.4-0.9 s), with a spark at 1.0 s. Red cells roll along the floor and hop into the cut, the first at 1.6 s (squeak). The guard walks in from the right at about 3.3 s: "Whoa, that's a huge cut!" ... "I need you to send blood platelets and painkillers..." The phone is at his ear from 6.95 s. The brain answers on the phone, shown with yellow sound lines and no inset. | 0.0-21.6 |
| 21.0-39.9 | B: stomach close-up | The stomach is asleep under a blue eye mask. Two pills slide down the food pipe and plop into the juice. It wakes: "Huh? What kind of medicine is this?" It pokes the pills twice. Its eyes go half-shut and annoyed from "Besides, I'm not even feeling pain". "Bro, stir it up": it stirs with a thin stick held in both hands, and the pills jump and spin. | 21.6-42.8 |
| about 40-41.3 | C: VEIN, label top right | The two pills float from left to right. | 42.8-44.2 (1.4 s) |
| 41.3-50 | D: two tunnels | Big pills between two dark caves: "Bro, how do we know which way the pain is?" ... "You go east, I'll go north." The bow pill hops into the right tunnel, then the plain one into the left. | 44.2-53.0 |
| 50-59 | E: the cut, boarded with planks | The prostaglandin stands at the cut. The pills run in from the left: "Aha!" ... "Hey, I'm just doing my job." "Well, we're here to do ours." A big dust-cloud fight, then the prostaglandin is knocked out. | 53.0-62.7 |
| 59-80.4 | F: clinic | Static shot of a plain room: ceiling vent and door frame. The doctor is on the left with a clipboard; the patient is on the right holding a glass of water. Then the doctor's explanation. | 62.7-84.7 |

Ours is 4.3 s longer. The reason is our voices: the slowest lines would lose clarity if sped up more (doctor lines are at most 1.12x).

## Medical facts (checked; the same lines as the reference)
- Painkillers like ibuprofen (NSAIDs) block prostaglandins. These are the chemicals made at an injury that make nerves send pain signals.
- The medicine travels in the blood everywhere. It does not search for the injury, and it does not heal the wound.

Sources: NHS "Ibuprofen for adults"; Cleveland Clinic "Prostaglandins"; NCBI StatPearls "Nonsteroidal Anti-inflammatory Drugs".

## How it was made (media is never committed; this re-creates it)
**Voices:**
- ElevenLabs `eleven_v4`, flow `ugqH3egnLr8PPBgeY7A1`, 2 takes per line. Session ids are in `takes_manifest.tsv`; voice ids and pitch shifts are in `voices.txt`.
- `prep_voice.py`:
  - picks the take with the lowest WER, then the widest pitch range (`takes/scores.json`);
  - applies one fixed pitch shift per role, moving the median f0 of the picked takes to the reference speaker's measured pitch;
  - applies phone EQ for the brain;
  - fits tempo to the reference's slot for each line (at most 1.38x for cartoons, 1.12x for the doctor and patient).
- After that: `tighten.py proc 0.14 30,31,32,33,34,35`, then `tighten.py proc 0.3`, then `words.py`.
- Takes used: 01a 02b 03b 04b 05b 06b 07a 08b 09b 10a 11b 12a 13b 14b 15a 16b 17b 18b 19b 20b 21a 22b 23b 24a 25a 26a 27a 28a 29b 30b 31a 32a 33b 34a 35a 36b.

**Audio timeline (`build_audio.py`):**
- Each scene is a block of lines placed at the reference's start times. A line waits for the previous line when ours runs longer.
- Scene cuts and sound effects sit on the reference's moments, shifted only by those waits.
- SFX are Mixkit, with ids in PLAYBOOK section 3:
  - whoosh as the cut slices; spark click; squeak as a cell hops;
  - swoosh as the guard steps in; a phone tone for the brain's voice;
  - plops as the pills land; clicks as they are poked; plop, squish and bubbles for the stir;
  - a slow whoosh for the vein; a whoosh into the tunnels; boings as the pills hop in;
  - a pop at the boarded cut; a squeak as the pills arrive;
  - punches and a wood hit in the fight; a boing and a fail piano for the knock-out.
- The music is mixkit-9, ducked 5 dB under speech.

**Art (all code):**
- `world_010.js`: the six sets, at the reference's measured positions and colours.
  - The cut's edges were traced row by row.
  - The stomach outline was traced from the reference's outlines.
  - The caves, vein and clinic room were measured on the frames.
- `chars_010.js`: capsules, red cells, and the prostaglandin with its name band.
- `parts_010.js`: all motion, tied to the voice timeline.
- `assemble_010.py`: 001's engine, plus 001's code doctor and patient (clipboard moved to the chest, open hand toward the patient, as in the reference).

**Build:** `python3 prep_voice.py && python3 build_audio.py && python3 assemble_010.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

**Final QA:** see the end of this file.

## Upload block
**Title:** How Do Painkillers Actually Find the Pain? 💊🤕  (the proven 21M wording)

**Cover frame:** the two pills and the prostaglandin at the boarded-up cut (about 57 s), or the stomach asleep under its eye mask (about 22 s).

**Description:**
You cut your foot, swallow a painkiller... and somehow the pain fades. 💊 But does the pill really travel to the injury and "find" the pain?
Here's what actually happens: painkillers like ibuprofen block prostaglandins, the chemicals that send pain signals to your brain.
The medicine never searches for the injury. It just turns the signal down.

A cartoon for general education, not medical advice. Use painkillers only as directed, and see a doctor for deep cuts.
Sources: NHS "Ibuprofen for adults"; Cleveland Clinic "Prostaglandins"; NCBI StatPearls "Nonsteroidal Anti-inflammatory Drugs".

#shorts #health #painkillers #ibuprofen #healthfacts #humanbody #medicine #animation

## Final QA (`how-do-painkillers-find-the-pain-exact.mp4`)

**Length:** 84.7 s. The reference is 80.4 s.

**Side-by-side check** (`compare_1.png` and `compare_2.png`, not committed):
- 24 pairs of our frame next to the reference at the matching moment.
- Before the final render, two rounds of pair sheets found and fixed about 25 differences (see LEARNINGS row 20).

**Speech:**
- Whisper on the final mix: **96.3%** (207 of 215 script words). The same check on the reference scores 100%.
- Misheard because of the pitch-shifted cartoon voices: "nerve's" (heard as "nurse"), "assigned" ("assigns"), "You are" ("You're"), "we" ("you"), "ones" ("one who's"), and "Doc" ("Bro").
- "Aha!" was dropped.
- The captions always show the exact script words.

**Loudness:** -11.8 LUFS, true peak -2.0 dB. The reference is -9.8 LUFS with a true peak of +1.5 dB, which means it clips. YouTube turns both down to -14 LUFS.

**Motion** (`tools/retention_check.py`):

| | Mean motion | Frozen frames | Longest still |
|---|---|---|---|
| Ours | 1.27 | 14.9% | 0.8 s |
| Reference | 1.26 | 27.5% | 1.7 s |

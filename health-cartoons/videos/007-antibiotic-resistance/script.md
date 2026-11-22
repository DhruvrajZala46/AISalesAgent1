# 007 - What Actually Causes Antibiotic Resistance?

Status (22 Nov 2026): **built on the user's direct order** ("generate kr ke hi de"); no Meta image generation (user rule, 22 Nov 2026).

**Proven video we remake (user rule: only proven 10M+ videos):** Dr. Healthcare "What Actually Causes Antibiotic Resistance?"
**17M views** (`W08YsWO93qQ`, 24x its median). The reference file was already downloaded on 20 Nov (`scratchpad/yt/vids`); studied at 1 fps
with its timed transcript. Picked over the others because most of its screen time can be built from our existing art library
(stomach, small-intestine buddy, doctor, hospital patient) and the rest are simple objects (bacteria, a white blood cell, a capsule)
that code can draw well.

**Medical facts (checked):** antibiotics treat bacterial infections only, not headaches or viruses; misuse and overuse drive resistance,
and bacteria (not the person) become resistant; take antibiotics only when prescribed and exactly as told. Sources: CDC "About Antimicrobial
Resistance" / "Be Antibiotics Aware"; WHO "Antimicrobial resistance" fact sheet.

## The reference, shot by shot (97 s)
| Time | Shot | What we copy |
|---|---|---|
| 0-19 | Stomach cross-section, capsules drop in: "Antibiotic? For a little headache?", a small buddy defends the owner, "send it down before it burns the walls" | same: our 004 stomach + our 006 small-intestine buddy, code capsules |
| 20-31 | Skin cross-section with a cut; a police-officer cell with a STOP sign; a green bacterium walks in through the cut, argues, shoves him over | same: code-drawn skin, guard and bacterium |
| 31-41 | The officer calls on the phone: "torn open section in the skin, send white blood cells" | same |
| 41-51 | A white blood cell arrives, argues, they fight in a dust cloud | same |
| 51-59 | The officer calls again: "spreading fast, we need backup" | same |
| 59-61 | Back in the stomach: "Huh? Another one?" (another capsule) | same |
| 62-73 | An ANTIBIOTIC capsule soldier attacks; the bacterium shrugs it off: "I've found a way to resist you" | same |
| 74-97 | Clinic: patient asks, doctor: "You're dealing with antibiotic resistance..." | our hospital room + doctor + patient, bubble replays, tip card, FOLLOW (+ a short stinger) |

## Our lines (`lines.txt`): every beat kept, our own words
26 lines, 215 words (reference 271), doctor 45 words (reference 48). Longest cartoon line split as in the reference's pacing.

## Art (no image model)
Library: 004 plate_abdomen + stomach poses, 006 small-intestine buddy, 004 hospital plate + patient in bed + doctor poses.
Code (`chars.js`): skin cross-section with a cut, the guard cell (cap, badge, mustache, STOP sign, phone), the bacterium (and its
clones), the white blood cell, the antibiotic capsule soldier, capsules, dust cloud, shield glow, bandage. Same outline colour and
thickness as the AI art, soft gradients and highlights, googly eyes with lids and brows, AI-style maroon mouths with tongues.

## Measured against the reference
| | This 17M video | Ours |
|---|---|---|
| Lines (whisper segments) | 27 | 26 |
| Words | 271 | 215 |
| Median words per line | 11 | 7 |
| Lines of 8 words or fewer | 44% | 65% |
| Lines with a question | 41% | 50% |
| Silent visual beats | slip-in through the cut, shove + fall, fight cloud, capsule drop, soldier march, poke bounces off | the same six |
| Clinic starts at | ~76% | 72% |
| Total | 96.7 s | 94.1 s |

## How it was made (media is never committed; this re-creates it)
**Voices:** ElevenLabs `eleven_v4`, flow `qNy6BeCYhIlJVOUZFIXj`, 2 takes per line (session ids in `takes_manifest.tsv`). Stomach = Liam
`TX3LPaxmHKxFdv7VOQHJ`, buddy = My Stephanie `oAoF4NpW2Aqxplg9HdYB` (+5 semitones), guard = Connery `BIDecpCwOWfm9O9hqJ2Q`, bacterium =
Quark Kent `k08SBQOmDEgHRblyb3y4`, white blood cell = Cedric M `5hwrYfkFdtVsiDRs66iv`, antibiotic = Jase `kTSNDDkx34wKsrujmdm1`, patient =
Davis `Z2fsAwk7IblvPhYzfslC`, doctor = Hope `tnSpp4vdxKPjI9w0GnoV`. Picked by `tools/score_takes.py`:
01b 02b 03a 04a 05b 06a 07b 08b 09a 10b 11b 12a 13a 14b 15a 16a 17a 18a 19b 20b 21b 22a 23a 24a 25a 26a.
Then `process_voice.sh`, `tighten.py proc 0.26`, `tempo.txt`, `words.py`; `build_audio.py` levels each line toward -19 dB and places the
silent beats (`GAP`) and the verified Mixkit SFX (PLAYBOOK section 3).
**Art (no image model, user rule 22 Nov 2026):** library sprites copied into `art/` (004 plate_abdomen, stomach base/point/shout/smug/panic,
006 small-intestine buddy, 004 plate_hospital, patient in bed, doctor base/explain/point). Everything in the skin scene is code: `chars.js`
(skin cross-section with a cut, blood vessel, blood drops, the guard cell, the bacterium + clones, the white blood cell, the antibiotic capsule
soldier with spear and helmet, shield glow, dust cloud, capsules, bandage).
Build: `python3 build_audio.py && python3 assemble.py && node ../../tools/render.js && LIM=0.72 bash ../../tools/mix.sh video.mp4 final.mp4`.

## Upload block
**Title:** What Actually Causes Antibiotic Resistance? 🦠💊  (the proven 17M wording, word for word)
**Cover frame:** the bacterium smugly blocking the antibiotic's spear with its shield glow (about 60 s), or the guard falling over (about 31 s).
**Description:**
Antibiotics for a headache? 🤕💊 The stomach can't believe it, a bacterium sneaks in through a cut, and the body's defences fall one by one...
until the antibiotic stops working. Here's what antibiotic resistance really is: antibiotics only work on bacteria, and every time they're
misused, the bacteria that survive learn to resist them. Take antibiotics only when a doctor prescribes them, exactly as told.

A cartoon for general education, not medical advice. Always follow your doctor's instructions.
Sources: CDC "About Antimicrobial Resistance" and "Be Antibiotics Aware"; WHO "Antimicrobial resistance" fact sheet.

#shorts #health #antibiotics #bacteria #healthfacts #humanbody #immunesystem #animation

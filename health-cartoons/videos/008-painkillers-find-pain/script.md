# 008 - How Do Painkillers Actually Find the Pain?

Status (22 Nov 2026): **built** on the user's order ("ak or short create krwe... exact same dr.healthcare... 10M, 20M viral");
waiting for the user's verdict. All code in the 001 / 003-v1 style (user rule, 22 Nov 2026); no image model.

**Proven video we remake (`research/NEXT-10.md` row 5):** Dr. Healthcare "How do painkillers actually find the pain?" **21M views**
(`Sqpn5VTjYV8`, uploaded 7 Nov 2025). The reference file was downloaded on 20 Nov (`scratchpad/yt/vids`). It was studied at 1 fps,
with key frames at full size and its timed transcript.

**Medical facts (checked):**
- Painkillers like ibuprofen (NSAIDs) stop the body making prostaglandins.
- Prostaglandins are chemicals made at an injury that make nerve endings send pain signals.
- The medicine travels in the blood everywhere; it does not seek out the injury, and it does not heal the wound.
- Cartoon logic, said plainly: pills do not "talk" or "walk to the cut". The doctor's lines are the real explanation.

Sources: NHS "Ibuprofen for adults"; Cleveland Clinic "Prostaglandins"; NCBI StatPearls "Nonsteroidal Anti-inflammatory Drugs".

## The reference, shot by shot (80.5 s)
| Time | Shot | What we copy |
|---|---|---|
| 0-3.6 | Tissue wall with a big cut, red blood cells roll past, a police-officer cell walks in | same (code; label "INSIDE THE FOOT") |
| 3.6-21 | Officer: "huge cut", phones the brain, "blood gushing, send platelets and painkillers"; the brain (voice): "the nerve told me" | same + a small round inset of the brain on the phone |
| 21-39 | Stomach asleep under an eye mask; capsules drop in; it wakes up and argues with them; "the more we talk, the more he hurts... stir it up" | same: our 007 code stomach with a mask, Zzz, two capsule characters (one with a bow) |
| 39-42 | The stomach stirs with a stick; the capsules ride a vein | same (they spin and dissolve, then ride a code vein, label VEIN) |
| 42-49 | Two dark tunnels: "which way is the pain?" "split up, you go east, I'll go north" | same |
| 50-58 | Back at the cut, now boarded up with wooden planks (the platelets); a spiky pink PROSTAGLANDIN; "I'm just doing my job" / "we're here to do ours"; dust-cloud fight, it is knocked out | same |
| 58.5-80 | Clinic: patient with a glass of water, "how fast will it work, my foot hurts"; doctor explains; "that makes sense" | 001's code clinic + glass of water, bandaged foot, punch-in on "prostaglandins", 2 replay bubbles, tip card, FOLLOW |

## Our lines (`lines.txt`): every beat kept, our own words
| | This 21M video | Ours |
|---|---|---|
| Lines | 21 | 21 |
| Words | 215 | 198 |
| Median words per line | 10 | 8 |
| Lines with a question | 29% | 33% |
| Silent beats | intro, capsule drop, stir + vein, split + arrival, fight | the same five |
| Clinic starts at | 73% | 74% |
| Total | 80.5 s | 84.7 s |

## How it was made (media is never committed; this re-creates it)
**Voices:**
- ElevenLabs `eleven_v4`, flow `c9130VTrzn3mbf0wTRUz`, 2 takes per line (session ids in `takes_manifest.tsv`, voice ids in `voices.txt`).
- Cast: guard Connery; brain Laura (phone EQ); stomach Liam; pill Jase (+2 semitones); pill2 My Stephanie (+5 semitones); prostaglandin Quark Kent; patient Davis; doctor Hope.
- Picked by `tools/score_takes.py` (`picks.txt`): 01b 02a 03a 04b 05a 06b 07a 08b 09b 10a 11a 12b 13a 14a 15a 16a 17b 18b 19a 20b 21b.
- Processing: `process_voice.sh`, then `tighten.py proc 0.26`, then `tempo.txt`, then `words.py`.

**Art (all code):**
- `world_008.js`:
  - the cut wall (planks later) and red blood cells;
  - the officer cell (`chars.js` guard) and the brain inset with a phone;
  - the stomach with an eye mask and a stirring stick;
  - capsule characters, the prostaglandin, the vein, the two tunnels;
  - clinic extras (poster, glass of water, bandaged foot).
- `assemble_008.py` adds 001's code clinic.

**Build:** `python3 build_audio.py && python3 assemble_008.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

**Final QA (`how-do-painkillers-find-the-pain.mp4`):**
- 84.7 s.
- Final-mix whisper 99.0%: only "uh" and "doc" were dropped.
- -11.8 LUFS, true peak -2.0 dB. At LIM 0.69-0.72 the peak reached 0 dB, so 0.66 is used.
- Motion 3.25, frozen 1.4%, longest still 0.6 s. Same tool on the references: 003 v1 = 3.16 / 1.7%; 001 = 2.52 / 15.3%.

## Upload block
**Title:** How Do Painkillers Actually Find the Pain? 💊🤕  (the proven 21M wording)
**Cover frame:** the two painkillers facing the spiky prostaglandin at the boarded-up cut (about 57 s), or the stomach waking up under its eye mask (about 20 s).
**Description:**
You cut your foot, swallow a painkiller... and somehow the pain fades. 💊 But does the pill really travel to the injury and "find" the pain?
Here's what actually happens: painkillers like ibuprofen stop your body making prostaglandins, the chemicals that make your nerves send
pain signals. The medicine doesn't heal the wound. It just turns the pain signal down.

A cartoon for general education, not medical advice. Use painkillers only as directed, and see a doctor for deep cuts.
Sources: NHS "Ibuprofen for adults"; Cleveland Clinic "Prostaglandins"; NCBI StatPearls "Nonsteroidal Anti-inflammatory Drugs".

#shorts #health #painkillers #ibuprofen #healthfacts #humanbody #medicine #animation

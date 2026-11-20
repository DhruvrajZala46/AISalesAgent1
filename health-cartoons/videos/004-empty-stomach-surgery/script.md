# 004 - Why Your Stomach Must Be Empty Before Surgery

Status (20 Nov 2026): **script approved by the user ("OK DONE"); video built, waiting for the user's verdict.**

**Why this topic (data):** the single biggest hit across both same-format channels: Health Manager "Why Your Stomach Must Stay Empty Before
Surgery" **32M (67x its median)**; the same topic again on Health Manager "Why don't doctors let you eat before surgery?" 3.7M (7.8x) and on
Dr. Healthcare "Why You Should Never Eat Before Surgery" 1.5M (2.1x). Proven three times, on both channels. Eating family + a hospital fear.
Reference videos to study: KW6r3s7OzqU, Mt_NjrZoLx4, GU7Psg-aRp0 (YouTube blocks downloads from this server; the user can send them).

**Medical facts (checked):** fasting before general anaesthesia lowers the risk of pulmonary aspiration (stomach contents entering the
windpipe and lungs); anaesthesia relaxes the muscles and suppresses the protective airway reflexes (cough, gag). ASA-based intervals: solids
6 h, fried/fatty/meat meals 8 h or more, clear liquids up to 2 h. Sources: Wikipedia "Preoperative fasting"; "Preoperative fasting and the risk
of pulmonary aspiration - a narrative review" (PMC11089317, 2024); OpenAnesthesia "NPO guidelines". Aspiration can cause aspiration pneumonia.

## Lines (voices: PLAYBOOK §2; LUNGS = a new 4th cartoon voice)
See `lines.txt` (role|text). Story beats in their voice: intruder arrives (burger at 6 AM) → refusal + reason (surgery) → warning of the
consequence ("if my door falls asleep, you're going up") → outside trigger (Brain on the phone: "Anesthesia's in... lights out") → it happens
(the stomach's door goes limp, the burger floats up the food pipe and drops into the windpipe) → "Why can't I cough?!" → blame/explain line →
clinic "Doc, I only ate one burger..." → doctor "That's called aspiration pneumonia" + mechanism + the 6-8 hour rule → stinger + FOLLOW card.

## Measured against their scripts
| | Theirs | Ours |
|---|---|---|
| Cartoon lines | 14-41 | 18 |
| Median words per line | 4-6 | 6 |
| Lines of 8 words or fewer | 80-100% | 100% |
| Questions | 11-37% | 29% |
| Interjections | 10-43% | 39% |
| Doctor words | ~40-55 | 44 |
| Clinic start | 57-83% | 65% (measured) |
| Total | 52-75 s | 71.7 s (measured) |

## Visual hook from the proven covers (KW6r3s7OzqU 32M, Mt_NjrZoLx4 3.7M, GU7Psg-aRp0 1.5M)
All three open on ONE big stomach cross-section filling the frame, the stomach itself is the character (googly eyes, brows, arms at its top).
32M: the stomach wears a SLEEP MASK (anaesthesia) with a food character inside. 3.7M: the brain in a thought bubble with a megaphone.
1.5M: the stomach eating a tiny burger. We copy that staging: stomach plate first, brain bubble on the phone, stomach falls asleep with a
sleep mask, then the 003 throat plate (burger up the food pipe, down the windpipe), then a lungs plate.

## Art plan (003 v2 pipeline)
Plates: front cut-away of neck + chest + belly (food pipe and windpipe side by side, lungs, stomach with its top valve), a hospital recovery
room, a hospital food tray. Sprites (green screen, edits for poses, AI mouths for lip-sync): STOMACH (shocked, pointing, panicking, worn out),
BURGER (cocky with sunglasses, floating scared, sulking), LUNGS (shocked, coughing strain, inflamed red), BRAIN (reuse + an asleep pose),
the same DOCTOR (brand), a PATIENT in a hospital gown on a bed (weak, coughing).

## How it was made (so it can be re-created; media is never committed)
**Voices:** ElevenLabs `eleven_v4`, flow `wYMF43pImFhcQOShqmm3`, 2 takes per line (session ids in `takes_manifest.tsv`). Voices: stomach
Liam `TX3LPaxmHKxFdv7VOQHJ`, burger My Stephanie `oAoF4NpW2Aqxplg9HdYB`, brain Laura `FGY2WhTYpPnrIDTdsKH5`, lungs Stevie
`IvUJKFyjVb5hItY9dJAT`, patient Davis `Z2fsAwk7IblvPhYzfslC`, doctor Hope `tnSpp4vdxKPjI9w0GnoV`.
Picked by measurement (faster-whisper WER + Praat pitch range, `takes/scores.json`): 01b 02b 03b 04a 05b 06a 07a 08b 09b 10b 11a 12b 13a 14b 15a
16b 17a. Then `tools/process_voice.sh` (role pitch), `tools/tighten.py` (pauses > 0.3 s; line 08 kept), per-line tempo from `tempo.txt`,
`tools/words.py` -> `words.json`, `build_audio.py` -> voice/sfx/music.wav + `data.js` (events, ~30 SFX placements, music mixkit-9).
Speech 61.8 s at 2.73 words/s; video 71.7 s; clinic at 65%.

**Art:** Meta Muse Image (`muse-image-1.0`) via `tools/meta_art.py` (key from `MODEL_API_KEY`, never in a file in the repo).
`prompts_01.json` plates + base sprites, `prompts_02.json` pose edits, `prompts_03_mouths.json` mouth edits, `prompts_04/05_fix.json`
(new stomach talking mouth: the first one looked like lipstick lips and the closed one had no mouth), `prompts_06/07_lungs*.json` (new
lungs mouths: the first open mouth sat on the lobe's bottom edge and the strain pose had none). `prep_art.py` keys the green screen,
`composite_mouths.py` pastes only a feathered ellipse round each AI mouth onto its base, `mouth_overlay.py` makes mouth-only layers so the
stomach's mouth draws over the burger standing inside it. After `composite_mouths.py`, re-set `variants` of `doc_base/explain/point`
to `["c","o"]` in `art/meta.json` (those mouths are copied from 003). The throat plate and the brain and doctor sprites come from 003.

**Scene:** `parts_v4.js` (+ the 001 engine helpers) -> `python3 assemble.py` -> `scene.html`. Five scenes: stomach (burger drops in, the door
ring lights up when it is named and turns red and dashed as it goes limp, sleep mask, lights-out dim, burger floats up the food pipe) ->
003 throat plate (up the food pipe, flips into the windpipe) -> lungs (lands in the windpipe, weak coughs, inflamed + steam) with the
brain inset on the phone -> hospital (push-in on the patient, punch-in on "aspiration", thought bubble cut on the doctor's words: door
limp / can't cough / food comes back up / lands in the lungs, tip card) -> tray stinger + FOLLOW.
Build: `python3 build_audio.py && python3 assemble.py && node ../../tools/render.js && bash ../../tools/mix.sh video.mp4 final.mp4`.

## Upload block
**Title:** Why You Can't Eat Before Surgery 🍔😴  (backup, the proven 32M wording: "Why Your Stomach Must Be Empty Before Surgery")
**Cover frame:** the stomach in the sleep mask with the red door ring, about 28.3 s (the 32M video's cover idea).
**Description:**
A burger sneaks in at 6 AM... one hour before surgery. 🍔 Here's what anesthesia does to your stomach's "door" and your cough reflex,
and why doctors say NO food for 6-8 hours before surgery.

A cartoon for general education, not medical advice. Always follow your own surgical team's fasting instructions.
Sources: Wikipedia "Preoperative fasting"; "Preoperative fasting and the risk of pulmonary aspiration: a narrative review" (2024,
PMC11089317); OpenAnesthesia "NPO guidelines".

#shorts #health #surgery #anesthesia #healthfacts #humanbody #doctor #animation

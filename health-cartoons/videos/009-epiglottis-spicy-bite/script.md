# 009 - The Epiglottis and the Spicy Bite

Status (22 Nov 2026): **v2 built** after the user rejected v1 ("5%... I can't understand what that body part is... confusing"). v1 was first built on the user's order. The user sent the reference file (`WhatsApp_Video_2026-11-22_at_3.21.00_PM.mp4`, a
Dr. Healthcare short, 23.7 s) and asked for the **exact same script and style, only our characters**: "EXACT SAME SCRIPT, SAME VIDEO
STYLE, EVERYTHING SAME... ONLY MERA CHARACTER". So this one keeps the reference's words **word for word**, unlike 004-008, where we
reworded. The user decided this and was told the reused-content/copyright risk.

**Views:** not verified. This video is not in our 20 Nov list of Dr. Healthcare Shorts (probably newer). The nearest listed video is
"What Happens When Food Goes Down the Wrong Pipe?" (1.7M, `itlRHmyO6Ho`), which is a different video.

**Facts (cartoon logic, said plainly):**
- When you swallow, the epiglottis folds down over the windpipe (trachea) so food goes into the food pipe (esophagus).
- If food or spicy bits slip into the airway, you cough and choke.
- Chili's capsaicin irritates the airway.

Sources: Cleveland Clinic "Epiglottis"; NHS "Choking".

## The reference, shot by shot (23.7 s), copied 1:1
| Time (ref / ours) | Shot | Speaker |
|---|---|---|
| 0-1 / 0-1 | Close-up throat cross-section: EPIGLOTTIS (flap with eyes), TRACHEA (eyes), ESOPHAGUS, spine; a piece of food drops into the esophagus | - |
| 1.0 / 1.0 | "Yo, why you always blocking me off?" | trachea |
| 3.2 / 3.2 | "'Cause this lane's for breathing, not food. If that stuff hits you, it's game over." | epiglottis |
| 7.8 / 7.75 | (more food drops) "Man, just let me try a bite. One bite won't hurt." | trachea |
| 10.6 / 10.5 | "No way, too dangerous." | epiglottis |
| 12-12.6 / 12.1-12.9 | The epiglottis folds shut; a crumb slips past; the trachea grabs it with its hands | - |
| 12.7 / 13.0 | "Bro, what did I just say?" | epiglottis |
| 15 / 14.75 | "Whoa! Spicy! Chest on fire! Can't breathe!" (eyes go red, tears, steam, flames) | trachea |
| 18.2 / 18.1 | "See, you're choking. Don't black out on me." | epiglottis |
| 21-23.7 / 20.6-24.4 | Cut to a man at a dinner table with spicy food, red lips, tears, coughing: "Oh... I can't breathe." | man |

The reference's sound was checked with the audio tagger:
- music under the whole video;
- a plop at 12 s, a boing at 16 s, a cough at 21 s.

We copy them. There is no clinic and no doctor, like the reference.

## Voices (pitch matched to the reference, measured with Praat)
Reference: trachea ~450 Hz, epiglottis ~290 Hz, man ~125 Hz.
- **Trachea:** My Stephanie +6 semitones, about 370 Hz. +8 made "blocking" and "chest" unclear.
- **Epiglottis:** Quark Kent +5 semitones, about 295 Hz.
- **Man:** Liam, natural, about 137 Hz.

Generation: ElevenLabs `eleven_v4`, flow `7EI6KSiseFaKHMsGmvmw`, 2 takes per line, picks `01b 02b 03a 04b 05a 06a 07a 08b`.
Lines are sped up 1.15-1.45x (`tempo.txt`) to the reference's fast pace, and the extra coughs at the start of line 6 are trimmed.
Captions use the exact script words, timed by aligning them to whisper's words (`build_audio.py`).

## Art v2 (all code): the reference's anatomy and staging, measured on its 720x1280 frame
**v1 was rejected ("5%")**: the throat could not be read. Mistakes found side by side with the reference:
- the windpipe was a solid striped "can" instead of an open airway;
- the food pipe was a thin rod with no opening;
- the epiglottis was a banana shape on top of the can;
- the anatomy did not join up into one throat;
- eyes and food were half the reference's size;
- one food drop was missing;
- the grab-and-eat moment was too fast;
- I added fire, steam and an epiglottis arm (none in the reference) and a dark dip;
- the man was far away, and the caption style was different.

v2 copies the layout 1:1 in our own code drawing:
- salmon throat, tongue base top-left;
- the epiglottis as a curved flap rising from the front wall, with its face at the base by the yellow hyoid bone;
- the TRACHEA as the open airway behind the cartilage front wall, with the face inside it;
- the ESOPHAGUS as a narrow tube with an opening at the top;
- a thick back wall and big vertebrae.

Same sizes and positions as the reference: eyes r 40-42, a food chunk about 90x190.

The action, beat for beat:
- 3 food drops at 0 / 7 / 11.7 s;
- the flap bends shut at 12.3 s with a worried, teeth-gritting face, while the trachea reaches up with both arms and grabs the chunk;
- it eats it while the epiglottis scolds;
- red glossy eyes with blue tears from "chest on fire".

Other details:
- The man is 001's patient in a medium close-up at the table with big plates of red spicy chicken: he eats calmly with his eyes closed, then gets red eyes, a red mouth and tears.
- Captions are white serif, lowercase.
- Hard cut, no extras.

Build: `python3 build_audio.py && python3 assemble_009.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA v2 (`epiglottis-spicy-bite-v2.mp4`)
- 24.4 s (reference 23.7 s). Every line starts within 0.35 s of the reference.
- Final-mix whisper 95.2%: the high trachea voice makes "chest" sound like "just"; the caption shows "CHEST".
- -11.6 LUFS (reference -11.7), true peak -1.3 dB.
- Motion 1.70, frozen 6.2%, longest still 0.7 s (reference: 1.88, 35.6%, 2.3 s).
- Checked against the reference second by second at 1 fps (24 frames each) before delivery.

## Upload block
**Title:** Why Spicy Food Makes You Choke 🌶️😵  (question style; the reference's own title is unknown to us)
**Cover frame:** the windpipe with red eyes and flames (about 16.5 s).
**Description:**
Your epiglottis has ONE job: keep food out of your windpipe. 🌶️ But what if the windpipe really wants a bite... of spicy chicken?
When you swallow, the epiglottis folds over your airway so food goes down the food pipe. If a bit slips the wrong way, you cough and
choke, and chili makes it burn even more.

A cartoon for general education, not medical advice. If someone can't breathe, call emergency services.
Sources: Cleveland Clinic "Epiglottis"; NHS "Choking".

#shorts #health #spicyfood #choking #epiglottis #humanbody #animation

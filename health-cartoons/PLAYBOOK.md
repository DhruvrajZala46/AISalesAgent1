# Health-cartoon Shorts: the standard (read before every video)

**The bar is video 003 v2/v3** (`videos/003-food-up-nose-v2/`: AI-illustrated art animated by our engine; the user: "GREAT, I LOVED IT"; audio and script from `videos/003-food-up-nose/`, "Why Does Food Come Out Your Nose When You Laugh?"), built on the engine of
video 001 (`videos/001-earwax-cotton-buds/`, which the user called "mind blowing"). After 003 the user said:
**"Save this standard. Every new video: same effort or MORE effort, in editing and scripting. Never forget it."**
**Update (row 9 in LEARNINGS):** the user then rejected 003's visuals as basic. The PROCESS in section 0 stays mandatory; the ART must be upgraded to illustrated assets (section 8) before the next video.
So every new video starts by copying the 003 folder (its `assemble.py` + `parts_*.js` pattern) and goes through **section 0 in full**.
Skipping a step, guessing instead of measuring, or claiming "99%" without proof is a failure of this standard.

The format follows the user's reference channel (dr.healthcare1 on Instagram, 718K followers): body parts and objects with
googly eyes argue during a procedure or problem, and then a doctor explains it in a clinic.
**We copy the format, never their art, mascot, scripts or watermark.** Our doctor, patient, clinic and topics are our own.
Do not clone a real person's voice.

---

## 0. The effort standard (non-negotiable, every video)

Do every step, in order. Each one produced a measured result in 003; the next video must match or beat it.

| # | Step | What 003 did (the minimum) |
|---|---|---|
| 1 | **Topic from data** | `yt-viral` ranking by multiple over each channel's own median, across the reference AND Health Manager. Prefer a topic proven on both channels at 10M+ (003: 22M + 20M). Our own angle on it. |
| 2 | **Study the references again** | Transcribe and contact-sheet the relevant top videos (all the user sends). Write down their hook, acting, camera, art details. |
| 3 | **Script in their voice, measured** | Lines of 3-8 words (median 4-6), 100% of cartoon lines ≤ 8 words, questions 11-37%, interjections 10-43%, arc "wants → no + reason → warning of the consequence → outside trigger → it happens → blame/'See?'", clinic 64-83%, doctor "That's called / You're dealing with X" + 2-sentence mechanism + tip, no spoken CTA. Facts checked against named sources. Show the measured table to the user. |
| 4 | **User approves the script** | Never spend credits before "okay". |
| 5 | **Voices** | eleven_v4, 2 takes per line, pick by whisper accuracy + pitch range (`takes/scores.json`); regenerate any line with a misheard key word; tighten pauses + tempo pass to 2.7-3.0 words/s. |
| 6 | **Audio timeline** | `build_audio.py`: tight gaps (0.12-0.25 s), overlaps where people talk over each other (the palate shouts over the laugh), ≥ 25 SFX tied to words and actions; find missing SFX on Mixkit, identify them with the AST tagger, or synthesize them (003's slurp). |
| 7 | **World art** | One locked wide shot of a real anatomy cross-section that fills the frame (camera zoom so the action area is big); thin dark outlines, flat pink flesh, yellow bone with dots, white labels on the anatomy. Every character: big googly eyes, brows, 5-viseme mouth, white rubber-hose arms with mitten hands. |
| 8 | **Acting timeline** | A pose for every line (point, shove, cross arms, jazz hands, hands on cheeks, fist), expression changes (stern, dramatic, panic + sweat, sleepy, smug, flinch), and a visual for every teaching word (arrows, X, label pops, thought bubble showing the warned consequence, air streaks, "HA!" letters, speed lines, glow). |
| 9 | **Look at frames before rendering** | `snap.js` at 4-9 moments per pass; fix what looks wrong (003 needed 6 passes: boxy brain, small hero, empty lower half, antenna arms, arms over eyes, bubble dots on the doctor's face). |
| 10 | **Full render + QA** | 1 fps contact sheet of the whole video, close-ups of doubtful frames, `retention_check.py`, whisper check of the FINAL mix (≥ 95% word match), loudness about −10 LUFS with true peak ≤ −1 dB. |
| 11 | **Deliver** | The mp4 plus a copy-ready upload block (Question-formula title, description with sources and "education only", hashtags) and the honest list of what is still weak. End with "Ship it, or change it?" |
| 12 | **Save** | Code, `script.md` (all ElevenLabs IDs, picked takes, tempo), docs and LEARNINGS committed and pushed. Media never committed. |

**003's measured numbers (the floor for the next video):** frozen frames 1.7%, longest nearly-static stretch 1.0 s, clinic at 64%,
2.73 words/s, 27 SFX, final-mix word match 96.8%, −10.8 LUFS, true peak −1.0 dB, 70 s.

---

## 1. Script format (fixed)

| Beat | Time | What happens | Rules |
|---|---|---|---|
| Hook | 0.0-1.0 s | Inside the body from frame 1, characters already on screen, the intruder enters by 0.3-0.6 s (001 used a 1 s outside shot first; 003 starts inside) | Big action in the first 0.5 s. The first line starts by 0.6 s. |
| Line 1 | ~0.5 s | Confused or pained line from an organ/object: *"Huh?! What's that … doing in here?"* / *"Ow!"* | It must name or show the weird thing. |
| Inside story | ~1-44 s | 15-22 short lines between 2-3 cartoon characters (003: noodle, soft palate, brain on the phone) | Every joke beat is also a teaching beat (a physical action that shows the cause). |
| Teaching gag | late inside | One line that states the mechanism as a joke (e.g. eardrum: *"I can't vibrate!"*) | |
| Payoff | end of inside | A confused line and a visual of the consequence (e.g. sound waves blocked plus a sad trombone) | |
| Clinic question (starts at **64-83% of the runtime**, like the reference) | ~5 s | Patient: *"Doc, [symptom]? But I [habit]!"* | |
| Doctor | **≤ 15 s** | "That's the problem." → mechanism (2 sentences) → **name of the condition** → what to do | Two thought-bubble replays, a punch-in and a label box on the condition name, then a tip label. |
| Stinger + CTA | ~5 s | The object character sulks (003: the noodle on a tissue, a tear) with one line that repeats the lesson, then the **FOLLOW for more body secrets** card. The CTA is on screen only; the reference never speaks one. | |
| Total | **55-75 s** (their #1 is 75 s) | | Speech about 2.7-3.0 words/s (reference) |

**Topic choice:** follow `research/VIRAL-STUDY.md`, and prefer a topic proven on BOTH same-format channels (§10): one 20M+ hit alone is not proof. Pick a habit almost everyone has, with a famous belief or a mild fear, that can be shown as an object travelling inside the body (eating and swallowing first). Never pick rare surgeries; they get 20K-120K views.

Medical facts must come from a real guideline or review (001: AAO-HNS Clinical Practice Guideline, Cerumen Impaction, 2017).
Say plainly what was not verified.

## 2. Voices (ElevenLabs, model `eleven_v4` from 003; 001 used `eleven_v3`)

| Role | Voice (name / id) | After-processing | Why |
|---|---|---|---|
| Cartoon A (main object, e.g. cotton bud) | My Stephanie / `oAoF4NpW2Aqxplg9HdYB` | +5 semitones (×1.3348) | 0.953 match to the reference "cartoon A" voice when pitched |
| Cartoon B (second character, e.g. earwax) | Liam (premade) / `TX3LPaxmHKxFdv7VOQHJ` | +1.5 st (×1.0905) | Closest to the reference "cartoon B" |
| Cartoon C (third character, e.g. eardrum) | Laura (premade) / `FGY2WhTYpPnrIDTdsKH5` | +2 st (×1.1225) | Distinct third voice |
| Doctor (female) | **Hope - upbeat and clear / `tnSpp4vdxKPjI9w0GnoV`** | speed ×1.08 | **0.984**, practically the reference's own female-doctor voice |
| Patient (male) | Davis / `Z2fsAwk7IblvPhYzfslC` | none | 0.944 |
| Patient (female) | Jessica (premade) / `cgSgspJ2msm6clMCkdW9` | none | 0.966 |
| Doctor (male), if needed | Rowan / `kLhAstPcnnPxqzk6gS5i` | none | 0.948 (no exact match was found in about 200 voices) |

- **From video 003: model `eleven_v4`, 2 takes per line** (paid Starter plan, 40,000 credits/month; 003 cost ~2,400). Put audio tags in the text:
  `[surprised]`, `[shouting]`, `[panicking]`, `[sulking]`, `[laughs harder]`; CAPS for one stressed word.
- **Pick takes by measurement, not by guess:** whisper word accuracy (a misheard key word = regenerate that line) and pitch range in semitones
  (more range = more expressive). Scores are saved in `takes/scores.json`.
- **Pace:** v4 speaks slower than the reference. After `process_voice.sh`, run `tools/tighten.py proc 0.30` (cuts pauses longer than 0.3 s inside a
  line) and an `atempo` pass per line from `tempo.txt` (1.05-1.25, never on laughs or sighs) to reach ~2.7-3.0 words/s.
- Cost: a short line is 40-60 credits; a 17-s doctor part is about 260. Video 001 cost about 680 credits.
  Check the balance with `account_get_usage`.
- `tools/process_voice.sh raw proc` pitches and trims the lines (files are named `NN_role.mp3`).
  Then run `python3 -I tools/words.py proc words.json`.
- **Licence:** the ElevenLabs free plan is, to our knowledge, non-commercial and needs attribution.
  A monetised channel needs a paid plan (Starter); check their terms.

## 3. Music and sound

- **Music:** Mixkit track id 9 (light comedic bed), looped through the whole video at −9.8 dB in the mix
  (≈ −26 LUFS stem, matching the reference at −21 to −33). Final master about **−10 LUFS** (`tools/mix.sh`: compressor, +5 dB, limiter at 0.75). The reference's YouTube uploads measure −8.7 to −10.2 LUFS; the −14 we measured first came from Instagram re-encodes.
- **Muffle gag:** when a character says it got quiet, the music gets a 350 Hz low-pass from that line to the clinic cut.
- **SFX (aim for 18 or more, each tied to a word or action)**, all Mixkit and fetched by `tools/fetch_assets.sh`:

| id | use |
|---|---|
| 1492 | object whooshes into frame (hook) |
| 1714 | zoom-in whoosh, scene transitions |
| 2882 | label box pops (EAR CANAL, EARWAX, condition label, tip label) |
| 2886 | scrubbing or sliding |
| 2151 | ding: arrow or key fact appears |
| 2209 | punch on a shove |
| 92 | splat |
| 324 / 1886 | squish while something is squeezed |
| 473 | boing on impact |
| 391 | dizzy birds after impact |
| 2894 | sad trombone on the payoff ("why'd it get so quiet") |
| 1486 | thought bubble appears |
| 2873 | CTA pop |
| 343, 110, 527, 3050 | spares (falling whistle, fail tone, clown, metal boing) |

## 4. Visual rules

- **Anatomy first.** The scene is a recognisable, real cross-section of the body part (canal, eardrum, ossicles, cochlea, bone),
  never an abstract tube.
- **Objects look real** (cotton bud: oval fibrous tip and thin stick; earwax: glossy amber glob with specks).
- **Lines:** 2.6 px outlines, 1.6-2 px detail, `vector-effect="non-scaling-stroke"`. **Shading:** the `shaded()` helper (soft blurred inner edge).
  **Colours:** muted and natural.
- **Composition:** the subject fills the frame. 001 rotates the world by −55° so the canal runs diagonally across the whole 9:16 frame.
  Faces are counter-rotated so they stay upright.
- **Characters:** googly eyes **with lids, tilt and brows** for every emotion (shocked, annoyed, sarcastic, squeezed, innocent, dizzy).
  Mouths use **5 visemes held at 15 fps** (closed, small, "oo", mid with teeth, wide with tongue). Blink about every 4 s.
- **Effects library:** label boxes (white, black border, Inter 900), yellow direction arrow, red pressure glow, yellow tension ticks,
  impact puff, sweat drops, sparkles and dust, dizzy stars, sound waves blocked by an ❌.
- **Camera (corrected after 002):** one LOCKED wide shot per scene, like the reference (it holds one framing for 10-20 s). The motion comes from
  acting: eyes, lids, brows, mouths, arms, props, sweat, labels. Move the camera only on an impact (punch-zoom plus shake) or a scene change.
  Changing the framing on every line made 002 look "glitchy". "Nothing static for more than 1.5 s" means the characters keep acting.
- **Character size:** the speaking characters fill 30-60% of the frame width, and every organ or object character has arms and hands
  and holds a prop where it fits (the reference stomach holds a fork and knife).
- **Hook:** open INSIDE the body with the talking characters already on screen, and an intruder (food, a needle, an object) enters by 0.6 s.
  At most a 0.5 s outside shot first, as in 001. Never open on a flat human face (002 failed with that).
- **Clinic:** a room with a window and blinds, a poster for the topic, a ticking clock, a desk and monitor, and an exam chair.
  Our doctor is a woman with a dark bun, glasses, teal scrubs, a white coat, a stethoscope and the topic's tool (otoscope in 001).
  The patient is a young man in a mustard hoodie. The patient holds the problem area while asking and reacts (surprised at the
  condition name, nods at the end). The doctor nods with her speech and shakes her head on "That's the problem".
  The camera pushes in on the patient's question, then **punches in on the doctor at the condition name** and shows a label.
  Two thought-bubble replays (`<use href="#world">` replaying earlier scene times).
- **Captions:** one word at a time, Luckiest Guy font, white with a black stroke, 44 px at y = 1110, a pop-in over 0.09 s.
  **Key words are yellow and 56 px.**
- **Stinger:** the object sits outside and sulks, then the **FOLLOW / for more body secrets** card bounces in.

## 5. Retention targets (measured with `tools/retention_check.py`)

| Metric | Reference channel | Video 001 | Target |
|---|---|---|---|
| Frozen frames (%) | 24-44 | 001: 15, **003: 1.7** | ≤ 20 (aim ≤ 5) |
| Longest nearly-static stretch | 1.6-3.0 s | 001: 1.1 s, **003: 1.0 s** | ≤ 1.5 s |
| Median pause between lines | 0.28-0.44 s | 0.35 s | 0.3-0.45 s |
| Doctor section | 13-22 s | 17.5 s | ≤ 18 s |
| SFX count | ~15 | 001: 21, **003: 27** | ≥ 25 |
| Loudness (YouTube) | −8.7 to −10.2 LUFS | 001: −13.6 (too quiet), 002: −10.3 | about −10 |

## 6. Pipeline

1. `bash tools/fetch_assets.sh` (font, music, SFX into `assets/`, which is git-ignored).
2. Write `script.md` from the template in video 001: beats, lines, roles, the medical source.
3. Generate each line in ElevenLabs (one flow per video) and save the raw mp3s as `raw/NN_role.mp3`.
   Record the flow, session and generation IDs in `script.md`.
4. `bash tools/process_voice.sh raw proc`, then `python3 -I tools/words.py proc words.json`.
5. `build_audio.py`: set `SCRIPT`, `GAP` (tight: 0.2 s, longer only after an action) and the event times (`EV`) from words.
   Place the SFX on words. It writes `voice/music/sfx.wav` and `data.js`.
6. `scene.html`: keep the engine sections (helpers, eyes, visemes, labels, humans, clinic, captions, exterior bud, CTA).
   Redraw the topic world (anatomy and objects) and edit `worldState`, the expressions and the camera keys.
7. Spot-check with `node ../../tools/snap.js <times>`. Then run `node ../../tools/render.js` (about 3 min for 1 min of video)
   and `bash ../../tools/mix.sh`.
8. QA (section 7), then deliver `final.mp4` with a title, a caption and the licence note.

`scene.html` layout in 001 (top to bottom): helpers (`shaded`, `smooth`, `limbD`) → object eyes, brows and mouths → data/lip-sync →
SCENE 1 world (topic anatomy) → label boxes → SCENE 2 clinic (`hand`, `humanEye`, `doctorSVG`, `patientSVG`, `earPoster`, furniture, labels) →
SCENE X exterior (`budSVG`, ear, CTA) → assemble → timing (visemes, `worldState`, `renderWorld`, `cameraInside`, `renderInside`, `renderExt`, `renderS2`, `caption`).

## 7. QA checklist (all must pass before delivery)

- [ ] The first frame already shows the body part and the moving object. The first spoken word is at ≤ 0.5 s.
- [ ] Every line has a new framing, an expression change or an effect. Nothing is static for more than 1.5 s (retention_check).
- [ ] Characters never leave the frame by accident. Labels never cover faces or the clock.
- [ ] Captions match the audio word for word; key words are yellow.
- [ ] Every SFX lands on its word or action; there are 18 or more.
- [ ] The doctor part is ≤ 18 s and has the bubble replays, the punch-in, the condition label and the tip label.
- [ ] The medical claims are checked against a named source.
- [ ] Final loudness is about −10 LUFS (true peak below −0.3 dB), the music is audible under the voice, and nothing clips.
- [ ] A 1 fps contact sheet has been looked at end to end, and the 4-6 fps strips around the hook, the impact and the clinic.
- [ ] Whisper on the FINAL mix matches the script ≥ 95% (003: 96.8%); every misheard key word is fixed or regenerated.
- [ ] Thought bubbles are big enough to read on a phone (003 clinic bubble: scale 1.38) and nothing sits on a face.
- [ ] Section 0 was done in full. The effort is the same as 003 or more.

## 8. Honest limits and upgrade path

Everything is drawn in code. The clinic people are the weakest part (about 75-80% of the reference illustrator's quality).
The remaining gap is the illustration hand. The upgrades the user can choose later: an image model (Gemini API key in the environment's
Network secrets, `generativelanguage.googleapis.com`, header `x-goog-api-key`) to draw still assets that we then animate, or an
illustrator's asset pack. Video models are not needed (the format is cut-out animation).

**Tested 20 Nov 2026: Meta Muse Image works** (`muse-image-1.0`, `https://api.meta.ai/v1/images/generations`, OpenAI-compatible, key in
`MODEL_API_KEY`, `tools/meta_image.py`). About 20 s and about 21-23K tokens per image; 9:16 comes back as 1152×2016. Quality: a clean,
professional educational-cartoon look, far above our code drawing. A character on a flat #00FF00 background keys out cleanly for cut-out
animation. Plan: AI background plates + AI character sprites (expressions via `/v1/images/edits` for consistency) + our code engine for
motion, blinks, mouths, effects, captions and sound.

# 012 - Why Do We Snore When We Sleep? (Dr. Mira Explains, video 1)

Status (22 Nov 2026): **built** after the user said "VIDEOOO BANA DE" ("make the video"). Waiting for the user's verdict.

## The proven video we follow
Dr. Healthcare "Why do we snore when we sleep?" (`G6GV0QxR-dY`):
- 11.47M views (15x the channel median), 212K likes, 576 comments.
- 51 s long, uploaded 29 Oct 2025.

The same title hit again on Health Manager: 3.4M.

**How it was studied:**
- YouTube blocked the video download here (HTTP 403), and the user did not send the mp4. We studied what YouTube serves publicly:
  - its words with timings (captions, `ref_transcript.tsv`);
  - its storyboard: one 50x90 frame per second for the whole video;
  - its cover image.
- What that showed:
  - **0-44 s:** one locked side cut of the throat. The skull bone is at the top right, the soft palate and the big tongue with its face sit in the middle, and the throat tube and spine are on the right. It opens close on the sleeping tongue and pulls back at about 1.5 s.
  - **45-51 s:** a bedroom. A man snores on a brown pillow; his partner's arm comes in from the bottom right and slaps him; a red handprint is left on his cheek.
  - The last line is "Snoring every night. So damn unpleasant."
  - It has no doctor.

## What we copied, and what is ours

| Angle | Reference | Ours |
|---|---|---|
| Topic and title | "Why do we snore when we sleep?" | same |
| Sets and order | throat side cut (one locked shot), then the bedroom | same, plus a short clinic at the end |
| Visual hook | close on the sleeping tongue, pull back at about 1.5 s | same (zoom 1.38x, pull back at 1.3-2.1 s), with Z's and a soft snore |
| Voice hook | "Hey, can you move up a bit? I need to pass through." at 2.6 s | "Hey, can you move up a bit? I need to get through." at 2.45 s |
| Beats | the air asks to pass → the tongue refuses (tired, resting) → "go use the other room" → a second one joins → "not moving a muscle" → the sleepy soft palate complains → they force through → "Ow! Watch it!" → "nice vibration… makes me fall asleep" → the slap → "Snoring every night" | the same beats in our words; "the other room" became "the nose", and "breathing is our business" adds the real stake |
| Ending | the partner's line | the partner's line, then **Dr. Mira** (the new channel's doctor) with the real explanation and the sleep apnea warning |
| Captions, music, SFX | one word at a time; music bed; SFX | same; the snore and slap sounds were generated with ElevenLabs |
| Characters | theirs | ours: air puffs, the tongue, the soft palate, 001's patient, and Dr. Mira (001's female doctor) |

**Added for clarity:** small labels (AIR, TONGUE, SOFT PALATE) when each first appears, because the user said viewers must understand the body parts.

## Facts (Mayo Clinic, "Snoring")
- In sleep, the throat muscles relax, so the tongue and soft palate fall back and narrow the airway.
- Air squeezing past makes the relaxed tissue vibrate; that sound is the snore.
- It is worse when sleeping on the back.
- Snoring with breathing pauses or gasping, or with daytime sleepiness, needs a doctor (possible obstructive sleep apnea).

## How it was made (media is never committed; this re-creates it)
**Voices:**
- ElevenLabs `eleven_v4`, flow `nPeSrxC7WIHh4KzHo1D9`, 2 takes per line. Session ids are in `takes_manifest.tsv`; the cast is in `voices.txt`.
- `prep_voice.py` picks takes by `score_takes.py`, forcing a few to keep each character's pitch consistent.
  - It applies one pitch shift per character and a pace per character.
  - It then runs `tighten.py proc 0.14 15,16,17`, `tighten.py proc 0.22`, and `words.py`.

**SFX:**
- Snore, slap and sleeping breath: ElevenLabs `eleven_text_to_sound_v2` (in `sfxgen/`, git-ignored).
- Plus Mixkit 1486, 2364, 2357, 1492, 1464, 2920 and 2894.
- Music: mixkit-9, ducked under speech.

**Art (all code):**
- `world_012.js`: the throat cut, the bedroom and the teal clinic.
- `parts_012.js`: all motion:
  - the soft palate flutters while the air squeezes past = the snore;
  - the air puffs squeeze down the throat tube;
  - the slap arm;
  - the handprint.
- `assemble_012.py`: 001's engine and the doctor/patient.

**Build:** `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.14 15,16,17 && python3 -I ../../tools/tighten.py proc 0.22 && python3 -I ../../tools/words.py proc words.json && python3 build_audio.py && python3 assemble_012.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-do-we-snore.mp4`)
- **Length:** 68.5 s. The cartoon part ends at 52.9 s (reference: 51 s); then 15.6 s of Dr. Mira.
- **Speech:** whisper on the final mix 97.8% (174 of 178 words).
  - Misheard: "palate" as "pallet" (same sound), "arguing", "scoot", and the "Ugh" sigh.
  - The captions always show the exact words.
- **Loudness:** -11.9 LUFS, true peak -2.0 dB.
- **Motion:** mean 1.14, frozen 15.1%, longest still 1.1 s.
- **Side by side:** `compare_ref.png` (not committed): ours next to the reference's storyboard frames.

**Still different from the reference:**
- The reference frames we had were only 50x90, so its drawing details could not be traced the way 010's were.
- The order of who speaks inside the throat is our reading of the dialogue.
- Ours is longer because of the doctor.

## Upload block
**Title:** Why Do We Snore When We Sleep? 😴  (the proven 11M title)

**Cover frame:** the man wide awake with the red handprint on his cheek (about 50 s), as the reference's cover does.

**Description:**
Ever wondered what's actually happening in your throat when you snore? 😴 When you fall asleep, your throat muscles relax, your tongue
and soft palate slump back, and air squeezing past makes them vibrate. That rattling is the snore! Sleeping on your side can help.
Loud snoring with gasping or pauses in breathing? See a doctor: it can be sleep apnea.

A cartoon for general education, not medical advice. Source: Mayo Clinic, "Snoring".

#shorts #snoring #sleep #health #humanbody #healthfacts #animation #sleepapnea

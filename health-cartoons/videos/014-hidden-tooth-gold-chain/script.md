# 014 - Why Did the Dentist Put a Gold Chain on This Tooth? (GiggleMD)

Status (23 Nov 2026): **built and delivered**. Waiting for the user's verdict. The user: "now make the next video as we made the previous one" (013 v2).

## The reference the user sent
A 42.6 s Dr. Healthcare Short about an impacted canine (the user's file `videoplayback.mp4`; views not measured here).
- 0-22 s: one locked shot inside a mouth with braces. A scalpel cuts the gum, a hidden tooth appears, a gold chain goes on, tweezers pull; the teeth talk.
- 23 s: a black "LATER..." card. 24-42 s: a static dental clinic; the doctor explains.
- Words at 0.0 s; loud master (-9 LUFS).

## What we took, and what is ours
We kept the topic, the facts and the beat order (cut, discovery, chain, pulling, the neighbours explain, the doctor). The story, every word and all the art are ours.

| Angle | Reference | Ours |
|---|---|---|
| Hook | scalpel on frame 0, first word at 0.0 s | the same idea: the scalpel is already cutting on frame 0, "Whoa! Why are they cutting the gum?!" at 0.0 s |
| The hidden tooth | wakes up confused | asleep with Z's: "Five more minutes..." |
| Our own gags | none | a "RESERVED" sign on its empty seat; a MONTH 1-12 counter while it comes down; it clicks in and says "Made it!" |
| Doctor part | cut to a static clinic for 19 s | the GiggleMD doctor in a bubble over the mouth; labels pop on her words (IMPACTED CANINE, BUTTON, GOLD CHAIN, BRACES) |
| Ending | the doctor's last sentence | the payoff the reference never shows: the tooth arrives in its seat |

## Script
See `lines.tsv` (14 lines, 107 words).

## Facts
- An impacted canine is a tooth that stays stuck under the gum and bone instead of coming in.
- Treatment: the tooth is uncovered, a small button with a gold chain is bonded to it, and the chain is tied to the braces so light force pulls it into place.
- Time: about a year is a common rule of thumb; one study of 47 teeth averaged 13.9 months, with a wide range.
  Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC6434671 and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9649639/

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `KVhCineBo5QJk2uNFcBS`, 2 takes per line (`takes_manifest.tsv`, `voices.txt`); all 28 takes scored, picked by `prep_voice.py`.
- SFX: Mixkit 1492, 2364, 2357, 2182, 2358, 2256; chain and month clicks are synthesised in `build_audio.py`; the ding is 013's `sfxgen/sfx_dingb.mp3`. Music: mixkit-9, ducked.
- Art, all code: `world_014.js` (mouth, teeth with braces, gum pocket, canine, chain, tools, doctor bubble), `parts_014.js` (all motion), `assemble_014.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.14 10,11,12,13 && python3 -I ../../tools/tighten.py proc 0.22 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_014.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-a-gold-chain-on-this-tooth.mp4`)
- Length 39.2 s; first word at 0.0 s.
- Speech: whisper on the final mix 100% (107 of 107 words).
- Loudness -11.8 LUFS, peak -1.7 dB.
- Frozen frames 6.2%; longest still stretch 0.5 s.
- Frames checked on sheets for the whole video and at 5 fps for the hook, the reveal, the chain, the labels and the ending.

## v2 (23 Nov 2026, after the user's verdict on v1)
The user: **"this video is not the exact same as the reference... the clinic scene from the screenshot is missing... make it in the same style with my channel's characters, no changes to script, visuals, animations, sound effects."**

What v2 does:
- Follows the reference scene for scene: the mouth (one locked shot), a black "LATER..." card, then a dental clinic with the doctor standing beside the patient in the dental chair.
- Our own gags from v1 are gone (the sleeping tooth, the RESERVED sign, the month counter, the doctor bubble, the labels).
- The characters are the channel's: our doctor (with a dental mirror) and our patient, drawn in code (`clinic14` in `world_014.js`).
- **The script is not word for word.** Each of the reference's 10 lines has one line of ours with the same meaning, speaker and order (`lines.tsv`). The user was told why: a word-for-word copy of another creator's script risks a strike.
- Voices: 10 new lines; the right tooth is now Jerry B. (the patient uses Chill). The doctor's three lines have one take each.

**v2 QA (`why-a-gold-chain-on-this-tooth-v2.mp4`):** 36.8 s (reference 42.6 s); whisper 99.2% (117 of 118; "we" heard as "they"); -11.8 LUFS; frozen 10.4%; longest still 0.7 s. The sections above describe v1.

Still different from the reference: our colours (pink gum, mint clinic), a gap in our tooth row under the hidden tooth, our characters and our wording.

## Upload block
**Title:** Why Did the Dentist Put a Gold Chain on This Tooth? 🦷

**Cover frame:** the sleepy tooth in its pocket with the gold chain hanging down (about 11 s).

**Description:**
Ever seen a gold chain hanging from someone's gum? 🦷 Sometimes a canine tooth gets stuck under the gum and bone and never comes down. That's an impacted canine. The dentist uncovers it, glues on a tiny button with a gold chain, and hooks the chain to the braces. Bit by bit, the braces pull the tooth into its seat. It usually takes about a year!

A cartoon for general education, not medical or dental advice.

#shorts #braces #teeth #dentist #impactedcanine #orthodontics #healthfacts #animation

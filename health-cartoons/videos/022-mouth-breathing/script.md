# 022 - Why Mouth Breathing Changes Your Face (GiggleMD)

Status (25 Nov 2026): **built and delivered**. Waiting for the user's verdict. Topic: #8 in `research/NEXT-10.md` ("Why do you get uglier as you grow older?", 13M on Health Manager, `hv6656awMl8`; views as of 20 Nov, not re-checked).

## The reference the user sent
A 42.2 s vertical video by Health Manager. Studied at 0.5 s steps (LEARNINGS row 29). Beat list:
- One set: the head cut from the side, mouth closed: the nose passage on top, the mouth below, the throat going down.
- 0-4 s: the adenoid (a lump at the back of the nose, in sunglasses) complains about being stuck there.
- 4.5-17 s: two air bubbles come in through the nose and stop at the adenoid; they argue; the lungs are rushing them; they decide to take the path below.
- 17.5-19.5 s: the bubbles go back out, the mouth opens, they go in through the mouth and down the throat.
- 20 s: a "LATER..." card.
- 21-38 s: mouth open, a stream of air through it; the roof of the mouth and the tongue (both with tired faces) complain about working overtime and plan a "makeover".
- 38.4-39.2 s: ropes pull the roof of the mouth up and the tongue down.
- 39.6-42.2 s: a man with a long face looks in a hand mirror: "Why am I getting uglier?" The reference ends there, with no doctor.

## What we kept, and what is ours
- **Kept:** every beat above, in order; who speaks each line; the sound moments (whoosh, bump, card, ropes).
- **Ours:** all drawings (code), the channel's patient at the mirror, and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 12 lines, 142 words). The reference's voices and music are not reused (copyright and reused-content strikes).
- **Added, not in the reference:** the channel's doctor at the end (one line and a board: 1. LONG FACE, 2. NARROW JAW, 3. CROWDED TEETH, NOSE ALWAYS BLOCKED? GET IT CHECKED), because every GiggleMD video ends on the doctor and the reference never explains the point. It can be cut at 46.6 s if the user wants the reference's ending.
- **Added for clarity (rows 27, 28, 30):** a closed eye and eyebrow so the cut reads as a face; a red cross on the blocked nose passage; labels ADENOIDS, NOSE BLOCKED!, BREATHING THROUGH THE MOUTH, ROOF OF THE MOUTH, TONGUE, ROOF PULLED HIGH, JAW HANGS OPEN.
- **Facts:** long-term mouth breathing in growing children (often from enlarged adenoids) is linked with a longer face, a narrow upper jaw and crowded teeth. The doctor's line says "while you're growing"; the reference's "uglier as you grow older" is not claimed.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `qCtfcLMASlNKJVM5r0fB`, 1 take per line (`takes_manifest.tsv`, `voices.txt`).
- SFX: Mixkit 1492, 2357, 2828, 1884, 473; clicks are synthesised in `build_audio.py`. Music: mixkit-9, ducked.
- Art, all code: `world_022.js` (`headScene`, `palD`, `bubbleSVG`, `mirrorScene`), `parts_022.js` (all motion), `assemble_022.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 12 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_022.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-mouth-breathing-changes-your-face.mp4`)
- Length 56.5 s (reference 42.2 s; ours has the added doctor part, about 10 s, and slower first lines); first word at 0.3 s.
- Speech: whisper on the final mix 98.6% (140 of 142; an extra "ugh" heard, one "But" missed, "lazybones" written as two words).
- Loudness -11.9 LUFS, peak -1.8 dB (peak measured on the render before the last framing fix; the audio did not change).
- Frozen frames 2.0%; longest still stretch 0.7 s.
- Checked on 18 reference-over-ours pairs (the render before the head was enlarged) and on 22 frames of the later renders.

Still different from the reference: its anatomy is more detailed (jaw muscles, throat layers, a curved soft palate) and its man has a drawn long face with teeth; ours is simpler and the patient's face is only stretched. In our mirror close-up the mirror is partly out of frame.

## Upload block
**Title:** Why Mouth Breathing Changes Your Face 😳

**Cover frame:** the two air bubbles stopped at the adenoid with the red cross (about 7 s).

**Description:**
"Move! You're blocking the way!" 😳 When swollen adenoids block the nose, air has to go through the mouth. Years of mouth breathing while a child is growing can change the face: a longer face, a narrow jaw and crowded teeth. If a nose is always blocked, get it checked.

A cartoon for general education, not medical advice.

#shorts #mouthbreathing #adenoids #breathing #health #healthfacts #humanbody #animation

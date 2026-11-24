# 020 - Why Babies Under 6 Months Shouldn't Drink Water (GiggleMD)

Status (24 Nov 2026): **built and delivered**. Waiting for the user's verdict. Topic: #9 in `research/NEXT-10.md` (13M on Dr. Healthcare, `tg4bhFvYe_M`; views as of 20 Nov, not re-checked).

## The reference the user sent
A 68.0 s vertical video by Dr. Healthcare. Studied at 0.5 s steps (LEARNINGS row 29). Beat list:
- 0-4 s: the baby's stomach (pacifier in its mouth) reads a newspaper; sound arcs at the top of the food pipe as dad speaks.
- 4-5 s: "chow time": the paper flies off.
- 5.5-10 s: milk pours down the food pipe and pools; steam; sparkling eyes.
- 10.5-11.5 s: a ladle comes out and it licks its lips.
- 12-21 s: water pours in; the white milk turns thin and pale and the level rises; the stomach is shocked, then looks down at its ruined food.
- 22-33 s: the stomach phones the intestine; arcs from the phone when the intestine answers.
- 34-36 s: inside the intestine: the watery milk floods in; the intestine strains.
- 36-46 s: the living room: dad holds the baby and a glass of water; mom answers through a speaker on the shelf.
- 46-68 s: the clinic: mom seated with the baby, dad behind her, the doctor explains (one still shot).

## What we kept, and what is ours
- **Kept:** every scene and beat above, in order; who speaks each line; the sound moments (pour, pop, phone, flood).
- **Ours:** all drawings (code), the channel's doctor and patient (as dad), and the wording: one line of ours per line of theirs, same meaning, never word for word (`lines.tsv`, 14 lines, 186 words). The reference's voices and music are not reused (copyright and reused-content strikes).
- **Added for clarity (rows 27, 28):** short labels BABY'S TUMMY, MILK, WATER, TOO WATERY!, INTESTINE; a slow camera drift so no shot is frozen.
- **Facts:** plain water can cause water intoxication (low blood sodium) in babies under about 6 months, whose kidneys are immature; it can cause brain swelling and seizures.

## How it was made (media is never committed)
- Voices: ElevenLabs `eleven_v4`, flow `tfGU0r5eZCtRGa9x76Om`, 1 take per line, every line 0 word errors (`takes_manifest.tsv`, `voices.txt`).
- SFX: Mixkit 1492, 2828, 2357, 1884, 2364, 473, 1351. Music: mixkit-9, ducked.
- Art, all code: `world_020.js` (`stomachScene`, `gutScene`, `babySVG`, `dadSVG`, `momSVG`, `homeBG`, `clinicBG`), `parts_020.js` (all motion), `assemble_020.py`.
- Build: `python3 prep_voice.py && python3 -I ../../tools/tighten.py proc 0.2 14 && python3 -I ../../tools/tighten.py proc 0.28 && python3 -I ../../tools/words.py proc words.json && python3 -I build_audio.py && python3 assemble_020.py && node ../../tools/render.js && LIM=0.66 bash ../../tools/mix.sh video.mp4 final.mp4`

## Final QA (`why-babies-shouldnt-drink-water.mp4`)
- Length 65.9 s (reference 68.0 s); first word at 0.5 s.
- Speech: whisper on the final mix 97.8% (182 of 186; "must have" written "must've", "plain" heard as "clean", "Great" as "bright").
- Loudness -11.8 LUFS, peak -1.9 dB.
- Frozen frames 0.8%; longest still stretch 0.4 s.
- Checked on 16 reference-over-ours pairs (first render) and a 12-frame sheet of the final render.

Still different from the reference: its stomach sits higher with scalloped intestines below, ours is larger with smoother bands; its clinic people are full length and smaller, ours are larger; our baby and mom are simple drawings.

## Upload block
**Title:** Why Babies Under 6 Months Shouldn't Drink Water 😳

**Cover frame:** water pouring into the milk, the stomach shocked (about 12 s).

**Description:**
"Why is he giving me water?" 😳 Babies under six months don't have mature kidneys yet. Plain water can dilute the sodium in their blood. That is called water intoxication, and it can make the brain swell and cause seizures. Breast milk or formula already gives a young baby all the water they need.

A cartoon for general education, not medical advice. If a baby seems unwell, see a doctor right away.

#shorts #baby #newborn #parenting #babycare #health #healthfacts #animation

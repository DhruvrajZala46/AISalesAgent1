# 003 - Why Does Food Come Out Your Nose When You Laugh?

Status (20 Nov 2026): script approved by the user ("now okay"); voices generated, scene built, video rendered (`final.mp4`, not committed).

## Build
`bash ../../tools/process_voice.sh raw proc && python3 -I ../../tools/tighten.py proc 0.30 11` → apply `tempo.txt` (atempo per line, `ffmpeg -nostdin`) →
`python3 -I ../../tools/words.py proc words.json && python3 build_audio.py && python3 assemble.py && node ../../tools/render.js && bash ../../tools/mix.sh video.mp4 final.mp4`

## Voices (ElevenLabs flow `dAzwWvxtZks9zyUEGV20`, model **eleven_v4**, 2 takes per line, ~2,400 credits)
Takes were picked by measurement (`takes/scores.json`: whisper word accuracy + pitch range in semitones), never by guess. The raw takes
are git-ignored; regenerate from the text below. Picked: 01a 02a 03b 04a 05b 06a 07a 08b 09a 10b 11a 12a 13a 14a 15d 16a 17a 18a 19a.
Line 15 was regenerated as `[annoyed] BRAIN! See what you did?!` because whisper heard "Bring" in both first takes.
The laugh (11, Davis) is cut before "Stop it, man" and the palate shouts over its tail. Pace after `tempo.txt`: 2.73 words/s (reference 2.8-3.0).

**Why this topic** (`../../research/VIRAL-STUDY.md` §10): "Why Does Food Sometimes Go Up Your Nose?" is the only topic that hit 20M+ on
BOTH same-format channels (22M = 30.6x median on @Dr_Healthcare1, 20M = 41.9x on Health Manager). Same promise, our own angle
(laughing while eating) and our own story and lines.

**Medical source:** Indiana Public Media, "A Moment of Science: Blowing Milk Out Your Nose" (2019): the soft palate lifts to seal the nose
during swallowing; laughing is breathing out, so it drops into the breathing position and food or drink can go up the nose.
CEENTA, "Water coming out of your nose when you laugh? Here's why". MSD Manual, Velopharyngeal insufficiency: frequent nasal regurgitation
can mean the palate does not close fully (cleft or short palate, after adenoid surgery, neurological causes) and should be checked.

## Lines (voices as in PLAYBOOK §2)
| # | Role / voice | Text |
|---|---|---|
| 01 | noodle / cartoon A (My Stephanie +5 st) | `[curious] Yo, what's behind that door?` |
| 02 | palate / cartoon B (Liam +1.5 st) | `That's the nose.` |
| 03 | palate | `Food goes down. Not up.` |
| 04 | noodle | `Come on. Just one peek.` |
| 05 | palate | `No way.` |
| 06 | palate | `While he's swallowing, this door stays shut.` |
| 07 | noodle | `So what happens if I go up there?` |
| 08 | palate | `You come out his nose. In public.` |
| 09 | noodle | `[bored] Fine. Boring.` |
| 10 | brain / cartoon C (Laura +2 st), on the phone | `Soft Palate, heads up.` |
| 11 | brain | `His buddy's about to tell a joke.` |
| 12 | palate | `[alarmed] What? Not now!` |
| 13 | palate | `He's got a mouth full of noodles!` |
| 14 | brain | `Too late.` |
| 15 | palate | `[shouting] Whoa! He's laughing!` |
| 16 | palate | `He's breathing out. I have to drop!` |
| 17 | palate | `I can't hold the door!` |
| 18 | noodle | `[excited] Wheee! Going up!` |
| 19 | noodle | `Huh? Why's it so hairy in here?` |
| 20 | noodle | `Wait. Is that daylight?` |
| 21 | palate | `[annoyed] Brain, see what you did?` |
| 22 | brain | `Hey, it was a good joke.` |
| 23 | patient / Davis | `Doc, I laughed while eating, and a noodle came out my nose!` |
| 24 | doctor / Hope (x1.08) | `That's called nasal regurgitation. When you swallow, your soft palate seals off your nose. But laughing makes you breathe out, so it drops, and food can shoot right up. Once in a while, it's harmless. If it happens a lot, get it checked.` |
| 25 | noodle | `[sulking] Next time... chew, swallow, then laugh.` |

No spoken CTA (none of their top 10 speaks one). On screen: the FOLLOW card from 001 during line 25.

## Measured against their 9 punctuated top-10 transcripts
| | Theirs (range) | Ours |
|---|---|---|
| Cartoon lines before the clinic | 14-41 | 22 |
| Median words per cartoon line | 4-6 | 5 |
| Lines of 8 words or fewer | 80-100% | 100% |
| Lines that are questions | 11-37% | 27% |
| Lines with an interjection (yo, huh, whoa, hey, wait, see…) | 10-43% | 27% |
| First word | 0.6-1.8 s | ~0.6 s |
| Clinic start | 64-83% (2 of the top 4 have no clinic) | ~62% (estimate, before voicing) |
| Doctor part | 15-17 s | ~15 s (43 words) |
| Pace | 2.8-3.0 words/s | voiced at the same pace |
| Total | 24-97 s, most 52-68 | ~61-65 s (estimate) |

## Beats (one locked wide shot per scene; motion comes from acting)
- 0.0 Head cross-section: mouth with a ramen bowl at the lips, nose cavity above, throat below. Soft Palate is a fleshy flap with googly eyes
  and arms, holding a door up against the nose opening. 0.3 s: a noodle is slurped in (slurp SFX), its tail whipping. Labels SOFT PALATE and NOSE.
- 01-09 The noodle stretches toward the door; Soft Palate pushes it back down (a squeak on each shove); on 08 a thought-bubble shows a noodle
  hanging out of a nostril in a restaurant (sets up the payoff).
- 10-14 A phone rings; the Brain appears in a corner pop-up with a phone; Soft Palate's eyes go wide, sweat drops.
- 15-17 HAHAHA (laugh SFX), the whole frame shakes, air arrows blast up from the throat, the door slams open (Soft Palate drops), red glow.
- 18-20 The noodle rockets up into the nose (whoosh), wiggles through nose hairs, light at the nostril.
- 21-22 Soft Palate glares at the Brain pop-up; the Brain shrugs.
- 23 Clinic: the patient sits with a noodle hanging out of his nostril. 24: the doctor; bubble replay of the drop; punch-in plus the
  NASAL REGURGITATION label; the tip label "OFTEN? GET CHECKED".
- 25 Stinger: the noodle on a tissue, sulking; FOLLOW card.

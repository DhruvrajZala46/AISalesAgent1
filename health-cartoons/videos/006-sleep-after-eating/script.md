# 006 - Why You Shouldn't Sleep Right After Eating

Status (21 Nov 2026): **built** (the user asked "video kha hai?", read as go-ahead); waiting for the user's verdict.

**Proven video we remake (user rule: only proven 10M+ videos, `research/NEXT-10.md` row 2):** Dr. Healthcare
"Why You Shouldn't Sleep Right After Eating?" **26M views** (`zAIArWsRp-E`, 36x its median). The user uploaded the video; it was studied
at 2 fps with whisper timings. Honest note from the data: this topic did not repeat on Health Manager (2.0M for "sleepy after eating"),
so it is proven once, not twice like 004's topic.

**Medical facts (checked):** lying down soon after eating raises the chance of heartburn/reflux; the usual advice is to wait 2-3 hours
(NIDDK: eat at least 3 hours before lying down; Mayo Clinic News Network: stop eating 3 hours before bedtime). Sulfur ("rotten egg")
burps smell of hydrogen sulfide, a gas made during digestion; eggs and meat are common triggers (Healthline, Medical News Today).
**Cartoon logic, said plainly:** organs do not really "decide to sleep". Digestion keeps going at night, only slower. The story's "strike" is
a joke, like the reference's; the on-screen tip at the end is the real advice.

## The reference, shot by shot (60.3 s, no clinic and no doctor)
| Time | Shot | Who talks | What we copy |
|---|---|---|---|
| 0-3.5 | Big stomach cross-section, holding a fork, eggs/burger/drumsticks in its juice | stomach | same (our 004 stomach + fork) |
| 3.5 | **More food drops down the food pipe** | stomach: "Wait, what?" | same |
| 5-12 | "He's still chugging more in?" / "not bad, still some room" | stomach | same |
| 13-23 | Cut: the brain on its brain stem, droopy, yawns ("long day, dozing off") | brain | same, our 003 brain |
| 18-22.5 | The stomach yells from below (yellow sound waves rising) "Brain, don't!" | stomach (off screen) | same |
| 23.5 | **The brain puts on a sleep mask**: "Deal with it tomorrow" | brain | same |
| 25.5-43 | Back in the stomach: a small buddy at the stomach's exit argues with it; the "plan": we sleep too | small buddy + stomach | same; our buddy = a little small-intestine character |
| 43-43.5 | **Both put on sleep masks** | - | same |
| 44-45.5 | Black card "FEW MOMENTS LATER" | - | same idea ("A FEW HOURS LATER") |
| 45.5-54 | **Green gas fills the stomach**, they wake up: "what's that smell?" / "hydrogen sulfide, rotten eggs" | buddy + stomach | same |
| 54.5-60.5 | Cut: the man in pajamas on his bed, burps a green cloud, hand at his mouth | man | same, our 004 patient in pajamas |
| - | (no clinic, no CTA) | - | + the real tip as a label ("WAIT 3 HOURS AFTER EATING BEFORE BED") and our FOLLOW card |

## Our lines (`lines.txt`), beat for beat, in our own words
| Reference beat | Ours |
|---|---|
| "Hmm, it's already late today." | STOMACH: Mmm... late dinner again. |
| "Wait, what?" (more food drops) | STOMACH: Wait, what? MORE food? |
| "I thought Bro was already filled up. He's still chugging more food in?" | STOMACH: I thought we were already full! / He's still shoving more in! |
| "Hmm, not bad. I think I still got some room left." | STOMACH: Hmm... not bad. I've still got some room. |
| "Ugh, it's been a long day. I'm dozing off first." | BRAIN: Yaaawn... long day. I'm going to bed. |
| "Brain, don't do that! You just sent more food down here." | STOMACH: Brain, NO! You just sent down a whole meal! |
| "Why are you sleeping right afterwards?" | STOMACH: Who sleeps right after eating?! |
| "Deal with it tomorrow." | BRAIN: Mmm... deal with it tomorrow. |
| "Maybe he's really exhausted, but we can still digest this food while he's sleeping." | BUDDY: Poor guy, he's exhausted. / We could still digest it while he sleeps. |
| "Yeah, we're all exhausted too, but if we don't act, he'll make this a habit." | STOMACH: We're tired too! / Cover for him, and it becomes a habit. |
| "Always eating late and sleeping right after." | STOMACH: Late dinner, straight to bed. Every single night. |
| "So what are we going to do now?" | BUDDY: So... what do we do now? |
| "I've got a plan. Since he's asleep, we should sleep too. We'll deal with it tomorrow." | STOMACH: Easy. He sleeps, we sleep. / Tomorrow's problem. |
| "Are you sure about this?" / "Totally." | BUDDY: You SURE about this? / STOMACH: Positive. |
| "Hmm, what's that smell?" | BUDDY: Ugh... what is that SMELL? |
| "That's hydrogen sulfide gas. It's the same gas found in rotten eggs. That should be enough sign for him to stop this habit." | STOMACH: Hydrogen sulfide. The rotten egg gas. / Maybe THAT will teach him a lesson. |
| "Ugh, why do I burp so often? Why does it smell this bad?" | MAN: Ugh... why do I keep burping? / And why does it smell like rotten eggs?! |

## Measured against the reference
| | This 26M video | Ours |
|---|---|---|
| Lines | 29 (whisper segments) | 24 |
| Words | 168 | 134 |
| Median words per line | 6 | 5.5 |
| Lines of 8 words or fewer | 89% | 95% |
| Questions | 27% | 29% |
| Silent visual beats | food drop, mask on, masks on, black card, gas fill, burp | the same six |
| Clinic | none | none (same) |
| Total | 60.3 s | ~60-62 s (estimate) |

## Art plan (the 004/005 pipeline: Meta Muse Image + AI mouths + our engine)
- Reuse: 004 stomach plate and stomach sprites (base, point, drowsy, asleep-with-mask + mouths), 005 food heap and items,
  003 brain, the 004 patient's design, 004/005 SFX map.
- New: stomach eating with a fork, stomach yelling up (hands round its mouth), stomach smug ("easy"), stomach holding its nose in green gas;
  the small-intestine buddy (worried, asleep with mask, holding nose); brain yawning on its brain stem, brain asleep with a mask;
  bedroom plate; the man in dark pajamas on the bed (hand at his mouth). Gas, sound waves, Zzz and the black card in code.
- About 30 Muse Image calls.

## Voices (after approval)
eleven_v4, 2 takes per line. Stomach = Liam (our 004 stomach voice), brain = Laura (004 brain), buddy = My Stephanie +5 semitones (high, like
the reference's ~445 Hz buddy), man = Davis (our 004 patient), all picked by whisper accuracy + pitch range.

## How it was made (media is never committed; this re-creates it)
**Voices:** ElevenLabs `eleven_v4`, flow `Og3G8ozKJiQtmoO4aTHk`, 2 takes per line (session ids in `takes_manifest.tsv`). Stomach = Liam
`TX3LPaxmHKxFdv7VOQHJ`, brain = Laura `FGY2WhTYpPnrIDTdsKH5`, buddy = My Stephanie `oAoF4NpW2Aqxplg9HdYB` (+5 semitones), man = Davis
`Z2fsAwk7IblvPhYzfslC`. Picked by `tools/score_takes.py`: 01b 02b 03a 04b 05b 06b 07b 08a 09a 10a 11a 12a 13b 14b 15b 16b 17a 18a 19b 20a 21a 22a 23a 24a.
Then `process_voice.sh`, `tighten.py proc 0.26`, `tempo.txt` (faster than 005 to match the reference's pace), `words.py`; `build_audio.py`
levels each line to -19 dB, shows the long yawn as one caption word "YAAAWN" and the man's burps as "*BURP*".
**Art:** Meta Muse Image via `tools/meta_art.py`: `prompts_01.json` (stomach poses as edits of our 004 stomach, the small-intestine buddy,
brain yawning/masked as edits of our 003 brain, bedroom, the man as an edit of our 004/003 patient), `prompts_02.json` (buddy poses + open
mouths), `prompts_03_closed.json` (closed mouths made FROM the open edits). `composite_mouths.py` uses the closed edit as the base
(`BASE_FROM_C`), and `yawn_closed.py` hand-draws the closed yawn mouth (the AI edit shifted the whole brain). Reused: 004 stomach plate and
stomach point/panic/asleep sprites, 005 food heap and items. Code-drawn: brain stem and background, sound waves, Zzz, the black card
with a spinning clock, green gas, burp clouds and stink lines.
Build: `python3 build_audio.py && python3 assemble.py && node ../../tools/render.js && LIM=0.72 bash ../../tools/mix.sh video.mp4 final.mp4`.

## Upload block
**Title:** Why You Shouldn't Sleep Right After Eating 😴🍔  (the proven 26M wording, word for word: "Why You Shouldn't Sleep Right After Eating?")
**Cover frame:** the stomach and the small intestine asleep in sleep masks (about 46 s), or the brain putting on its sleep mask (about 23 s).
**Description:**
Late dinner... straight to bed. 😴 The brain clocks out, the stomach and gut go on strike, and by morning: rotten-egg burps. Here's why
lying down right after a big meal is a bad habit, and the simple rule: wait about 3 hours after eating before you lie down.

A cartoon for general education, not medical advice. If you get heartburn or reflux often, talk to a doctor.
Sources: NIDDK "Eating, Diet & Nutrition for GER & GERD"; Mayo Clinic News Network "Timing snacks to avoid heartburn"; Healthline "Sulfur burps".

#shorts #health #digestion #heartburn #healthfacts #humanbody #sleep #animation

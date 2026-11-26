# Editing blueprint: "How Do Sleeping Pills Actually Work?" (GiggleMD 023 v6)

A timestamped plan that an editor can follow, built in the decoded reference style (`../../research/STYLE-DECODE.md`).
The finished video is `how-sleeping-pills-actually-work-v6.mp4` (60.5 s, 720 x 1280, 30 fps). Times are from its real timeline (`data.json`).

## Global settings (apply to every scene)
| Element | Setting |
|---|---|
| Canvas | 720 x 1280, 30 fps |
| Camera | locked: no zooms, no shakes, no drift |
| Cuts | hard cuts only, 2 in the whole video (21.79 s, 54.40 s) |
| Drawing rate | characters and props update 15 times a second (held 2 frames); captions update every frame |
| Ink | near-black `#1b1b1b`, 3.4-3.6 px lines, flat fills with soft shading |
| Watermark | "@GiggleMD", Comic Neue Bold 23 px, white at 42% opacity, thin black stroke at 25%; 5 copies: (360, 46) straight; (560, 330), (150, 620), (575, 860), (170, 1180) tilted -28 deg |

## Caption specification (every word in the video)
| Property | Setting |
|---|---|
| Text | the spoken word, UPPER CASE, apostrophes kept (WE'RE, CAN'T), other punctuation removed |
| Font | Luckiest Guy, 50 px (cap height about 36 px = 5% of the width), letter spacing 0.5 px |
| Colour | fill `#FFFFFF`; outline `#141414`, 5 px stroke drawn under the fill (2.5 px visible) |
| Shadow | drop shadow 2 px right, 3 px down, blur 1 px, black at 50% |
| Position | centred at x = 360; baseline y = 1018 (centre about 1000 = 78% down), one line, no box |
| In | on the word's first frame (word timestamps from the voice track) |
| Pop | frame 1: 90%; frame 2: 125%; frame 3 onward: 100% (scale round the caption centre, no easing) |
| Hold | until the next word if the pause is under 0.3 s; otherwise it disappears 0.1 s after the word ends |
| Never | no highlight colours, no second line, no background, no fade |

## Music and mix
| Element | Setting |
|---|---|
| Music | Mixkit 508 "Jazz 2" (double bass, cello, strings, piano), looped, about 17 dB under the voice, ducked 5 dB more while someone speaks; fades in from silence over 1.6 s, out over the last 1.0 s |
| Voices | 5 characters (stomach, brain, officer, pill, husband), one take per line |
| Brawl | the brawl SFX are laid on after mastering (`post_mix.sh`, +12 dB) so they hit 4.5 dB over the median, like the reference |
| Master | -12.3 LUFS integrated, peak -0.7 dBFS (`LIM=0.66 bash ../../tools/mix.sh video.mp4 tmp.mp4 && BG=12 bash post_mix.sh video.mp4 final.mp4`) |

## Scene-by-scene timeline
| Time (s) | Speaker | Narration | On screen | Caption | Animation / effect | Transition | Sound |
|---|---|---|---|---|---|---|---|
| 00.00-00.90 | - | (no line) | Stomach cross-section fills the frame: food pipe from the top (light pink with a darker inner wall), liver (`#e2533a` / `#b9463f`) and yellow bile duct on the left, domed stomach (`#f7a29c`, thick red wall `#d24d50`), orange acid (`#efa874`) at the bottom, small-intestine coils below. Big angry face (eyes r 60, thick brows) next to the pipe. Two white tablets drop down the pipe into the acid (0.05-0.85 s); the eyes follow them. | none | tablets fall on twos; eyes track; static camera | - | plop (Mixkit 2925) at 0.16 s; music fades in from silence over 1.6 s |
| 00.90-04.51 | stomach | A sleeping pill? Today? I never said we're going to sleep. | Same shot. Stomach complains; tablets bob in the acid. | one word at a time, upper case (see caption spec) | mouth on visemes, brows down, held on twos | - | - |
| 04.81-06.05 | stomach | Hey, up there! | Stomach looks up to the top left, shouting up. | one word at a time, upper case (see caption spec) | eyes up; mouth open wide | - | - |
| 06.65-08.26 | brain | What's going on down there? | At 6.25 s a white thought bubble pops in at the top left (pointed tail to the stomach) with a red-brown folded brain inside, half-closed eyes. | one word at a time, upper case (see caption spec) | bubble pops 0 -> 110% -> 100% in 0.3 s; brain bobs | - | - |
| 08.48-10.43 | stomach | You just swallowed a sleeping pill. | Stomach answers, looking up at the bubble. | one word at a time, upper case (see caption spec) | talk; eyes up-left | - | - |
| 10.65-17.53 | brain | I can't take it anymore. I've been fighting anxiety for days. I can't sleep at all. Please, break it down faster. | Brain pleads; tired eyes, small pupils; slight shake on stressed words. | one word at a time, upper case (see caption spec) | brain mouth on visemes; 2 deg wobble | - | - |
| 17.75-19.99 | stomach | Fine. But you owe me one. | Stomach grumbles; acid sloshes harder. | one word at a time, upper case (see caption spec) | acid wave amplitude up; brows down | - | - |
| 20.19-21.79 | - | (no line) | Bubble gone at 20.19 s. Tablets fizz: white bubbles rise from them and they shrink away (20.19-21.39 s). | none | fizz bubbles rise; tablets scale to 10% | **hard cut at 21.79 s** | whip (Mixkit 2151) at 21.69 s, on the cut |
| 21.79-22.39 | - | (no line) | Amygdala set: dark rose wall with a soft lighter centre, orange ground with ink squiggles. Top-left tag "Amygdala (Brain's Anxiety Centre)" (white box, thin navy border, Comic Neue Bold 24 px, stays the whole scene). Three blobs on fire on the right: CORTISOL (green), GLUTAMATE (blue), ADRENALINE (yellow), with red angry eyes and anger marks. The officer walks in from the left. | none | officer walks in 0.6 s; flames flicker | - | - |
| 22.39-26.43 | officer | Everyone, calm down! We're not dying. Nothing is wrong! | Officer waves his arms at the blobs. Flames shrink as they calm (about 24-25 s). | one word at a time, upper case (see caption spec) | arm swing on twos; flames scale with "heat" | - | - |
| 27.58-31.13 | officer | Why do you never listen? I'm so tired of this job. | At 26.58 s the flames burst back up (no sound, as in the reference). Officer frustrated. | one word at a time, upper case (see caption spec) | flames jump to 125% | - | - |
| 31.33-32.63 | - | (no line) | Brawl: one big white cloud with an ink outline swallows the officer and the blobs for 1.3 s; its outline changes every 0.1 s and sometimes stretches left. | caption continues ("...JOB") | cloud redrawn every 3 frames | - | burst (1714) + 8 hits (2149, 2920, 2151, 772, 2980, 1464) every 0.14 s + burst at 32.33 s; laid on after mastering, 4.5 dB over the median |
| 32.83-35.03 | officer | They never listen. I quit. | Cloud gone: the officer is back with a black eye and a plaster, flames still burning. | one word at a time, upper case (see caption spec) | beaten face, half-closed eyes | - | ding (1107) at 33.53 s |
| 35.33-35.93 | - | (no line) | A small round white tablet with a face rolls in at the bottom left (the same tablet as in the stomach). | none | rolls in 0.7 s | - | soft whip (2151) at 35.33 s |
| 35.93-37.81 | pill | Hey, what's going on in here? | Tablet asks what is going on. | one word at a time, upper case (see caption spec) | talker's mouth on visemes; listener blinks | - | - |
| 38.03-41.08 | officer | Why do you care? If you came to gossip, do it outside. | Officer grumpy, turned to the tablet. | one word at a time, upper case (see caption spec) | talker's mouth on visemes; listener blinks | - | - |
| 41.30-47.62 | pill | No gossip. We're sleeping pills. We're here to calm things down, so the owner can finally get some real rest. | Tablet explains, friendly face. | one word at a time, upper case (see caption spec) | talker's mouth on visemes; listener blinks | - | - |
| 47.84-49.81 | officer | Oh, in that case, let's go. | Officer perks up (smile). | one word at a time, upper case (see caption spec) | talker's mouth on visemes; listener blinks | - | - |
| 50.06-53.89 | officer | Okay, everyone. Quiet down. Settle down. Yep, just like that. | "QUIET" (51.15 s), "SETTLE" (52.03 s), "YEP" (52.87 s): each step shrinks the flames by 40% until they are out; the blobs' eyes go calm and half-closed. | one word at a time, upper case (see caption spec) | flames step down on each word | - | - |
| 53.89-54.40 | - | (no line) | Calm blobs, officer content. | none | held | **hard cut at 54.40 s** | soft whoosh (175) at 53.95 s, before the next first word |
| 54.80-59.86 | husband | Honey, after that sleeping pill last night, you finally slept better than you have in weeks. | Bedroom: sage wall `#cfe0c4`, window top right, bed on the left with a blue cover. The wife sits on the bed edge (left, big); the husband stands close on the right. | one word at a time, upper case (see caption spec) | husband talks; wife blinks | end at 60.46 s | no SFX; music fades out over the last 1.0 s |
## Check against the references (before delivery)
Measured with `tools/style_metrics.py` and the caption-timing script on the final file, next to the references:

| Measure | Reference creator (v1, v2, v3, v5) | Sleeping-pills reference | 023 v5 (before) | **023 v6** |
|---|---|---|---|---|
| Still frames | 57-85% | 43.6% | 8.8% | **51.9%** |
| Drawing changes a second | 5.4-13.9 | 17.5 | 28.3 | **15.6** |
| Hard cuts | 1-12 | 4 | 4 | **4** (incl. the brawl cloud on and off) |
| Caption minus word start (median) | -0.02 to +0.01 s | - | - | **+0.016 s** |
| Caption font / outline | Luckiest Guy, 2-3 px, small shadow | - | Luckiest Guy, 7-8 px | **Luckiest Guy, 2.5 px + shadow** |
| Caption height | 4-6% of the width | - | 6% | **5%** |
| Caption position | 75-80% down | 73-80% down | 80-96% down | **78% down** |
| Music + SFX under the voice | -13 to -22 dB | -18.1 dB | -5.3 dB (from stems) | **-15.2 dB** |
| Loudness | -8.5 to -10.9 LUFS | -11.1 | -14.5 | **-12.3** (no clipping) |
| Median saturation | 32-45 (pastel scenes) | 104 (organ scenes) | 83 | **83** |
| Speech recognised by whisper | - | - | 98.6% | **100%** (147 of 147) |

**Still different, honestly:**
- Our master is 1-4 dB quieter than theirs. They clip, and we don't.
- Our organ scenes keep the sleeping-pills reference's stronger colours (saturation 83), not the pastel skin-scene colours of v1-v5. This video takes place inside the stomach and brain, like the sleeping-pills reference.
- The sleeping-pills reference itself uses larger captions (about 9% of the width). v6 uses the 4-6% of the five style references, as asked.
- Our officer, blobs and bedroom people are our own code drawings, simpler than the reference's hand-drawn ones.

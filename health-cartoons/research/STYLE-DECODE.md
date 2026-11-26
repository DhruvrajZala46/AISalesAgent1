# Style guide: the reference creator's visual DNA (measured 26 Nov 2026)

The user: "I love the style of this creator: the captions, the colours, the themes, the effects. Decode their complete visual language,
then make my video in the same visual style. Recreate the techniques; don't copy their footage or content."

**References (the user's mp4 files):**
- v1 "What Really Happens After You Shave" (720p, 49 s)
- v2 "How Does Testosterone Gel Work" (720p, 62 s)
- v3 "How They Fixed His Curved Spine" (360p, 63 s)
- v4 a soda / sugar video "What Happens When..." (360p, 31 s)
- v5 "Why Your Pimple Comes Back Bigger After Popping" (240p, 63 s)

v1-v3 and v5 carry the "Dr.healthcare" watermark. v4 has a different caption font and a busier sound style, so it is treated as a variant.
The sleeping-pills video that 023 follows was measured with the same tools as a sixth reference.

## How it was measured (not guessed)
| What | How |
|---|---|
| Scenes and frames | 1 fps sheets of every video; 0.2 s and 1/30 s strips around captions and transitions |
| Fonts | full-size caption crops set beside 18 Google Fonts rendered with the same outline |
| Caption timing | caption changes detected frame by frame in the caption band, matched to whisper word timestamps |
| Colours | k-means palettes (frames every 0.5 s); median saturation and brightness |
| Motion | frame differences (still frames, drawing changes per second, hard cuts); phase correlation for camera moves |
| Ink | dark-pixel run widths at 720 px |
| Sound | EBU R128 loudness; demucs voice / non-voice split; SFX onsets labelled with an AudioSet classifier (MIT AST); music by instrument profile |

The numbers come from `tools/style_metrics.py` (motion, colour, ink, loudness, bed level, SFX rate) plus the one-off scripts described here.

## 1. Captions (the signature)
| Property | Reference value | How it is built |
|---|---|---|
| Unit | **one word at a time**, every spoken word | one text element, swapped per word |
| Font | **Luckiest Guy** (v1, v3, v5); **Anton** (v2); **Merriweather Black**, lower case (v4) | Google Fonts, all free (SIL OFL) |
| Case | UPPER CASE (lower case in the serif variant); apostrophes kept (DON'T, LET'S) | |
| Fill | pure white `#FFFFFF` | |
| Outline | thin black, about 2-3 px at 720 px width (0.3-0.4% of the width) | stroke painted under the fill |
| Shadow | small dark drop shadow, about 2 px right and 3 px down, slightly soft | |
| Background | none (no box, no pill, no highlight colour) | |
| Size | cap height 4-6% of the frame width (30-43 px at 720 px) | Luckiest Guy at about 50 px font size |
| Position | centred, one line, **75-80% down the frame**; moved high (15-33% down) when the subject fills the lower half (v2) | |
| Timing | appears on the word's first frame: caption minus word start = median 0.00 s (half of all words within ±0.06-0.11 s) | word timestamps |
| Hold | until the next word; blank during pauses (about 0.3 s or longer) | |
| Pop | 3 frames, no easing: about 90% -> one frame at 120-130% -> 100% | |
| Emphasis | none: key words (BACTERIA, INFECTION) are the same size and colour | |

## 2. Colours
- **Pastel, low saturation:** median saturation 32-45 of 255 in v1, v2, v3, v5; median brightness 210-251.
  v4 (red vein, 114) and the sleeping-pills reference (organs, 104) are the saturated exceptions, both inside the body.
- **One flat background colour per scene**, 20-48% of the screen:

| Scene | Colour |
|---|---|
| Skin | pale aqua `#daf8fa` |
| Arm | steel blue `#97c8d6` |
| Spine | grey-blue `#aecbd2` / `#b1cad0` |
| Pimple | pale sky `#cfe8fc` |
| Vein | salmon red `#b94f4c` / `#f5888b` |

- **Body colours:** skin cream `#f8e4ae` / `#f6e3cb` / `#f7e8d5`, flesh pink `#f6b1a5` / `#e49281`, fat yellow `#e4ca8f`, muscle brown `#9a6557` / `#96624d`, bone cream `#f8f4e2`.
- **People and rooms:** grey walls `#b6c1c9` / `#959594`, white coat `#f5f5f4`, the doctor's green mask and tie, the patient's blue shirt `#4383c8` / `#6c8baa`, brown floor `#a2663e`.
- **How colour changes through a video:** one palette for the inside-the-body part, then a full switch at the cut to the room or clinic (greys, white, blue, brown). There are no colour grades, fades or tints between them.
- **Soft shading on flat fills:** radial red glow on painful spots, pink glow round tired eyes, a soft vignette on the vein background, and a blurred out-of-focus window in the clinic (v5).
- **Ink:** near-black `#161413` / `#0a0909`, even line weight about 3 px at 720 px (4-5 px in the clinic).

## 3. Typography and hierarchy
1. **Caption:** Luckiest Guy, white with black outline, centre-low. The biggest text, always present while someone speaks.
2. **Location / name tags:** small white boxes with a thin dark border, comic hand lettering (Comic-Neue-like), often italic. Examples: "VEIN" at the top right, "Sugar" as a speech tag, "Amygdala (Brain's Anxiety Centre)" at the top left. On screen for the whole scene.
3. **Name labels on characters:** small white bars with dark capitals across the body (CORTISOL, INSULIN).
4. **Time card:** "FEW MOMENTS LATER" in plain white sans capitals on black, centred, about 1.1 s.
5. **Watermark:** a soft rounded font, faint (about 30-40% white), repeated 3-5 times across the frame, some tilted.

## 4. Visual themes and composition
- A medical cross-section or close-up fills the whole frame; the organ is the main character.
- Every object has the same face: big round white eyes with black pupils, small red mouths. This includes hairs, bones, gloves, razors, scanners and pills.
- The cartoon part runs 25-40 s in one locked set. Then one hard cut takes us to a room or clinic: the doctor (white hair, green mask) and the patient, shot full-body side by side.
- Compositions stay centred, with the face in the upper half and the caption in the lower middle.

## 5. Effects and motion (consistent vs scene-specific)
**Consistent in every reference:**
- static camera (0-4 camera-move frames in v1, v2, v3, v5)
- hard cuts only, 1-5 per video
- one-word popping captions
- the faint repeated watermark
- the googly-eye faces
- limited animation: 57-85% of frames show no change; drawings change about 5-14 times a second; mostly held 1-3 frames
- emotion marks drawn on the character (anger veins, sweat, tears)

**Used only in particular scenes:**

| Effect | Where | How it is built |
|---|---|---|
| Crash zoom into the body | v1 0.6-0.87 s | 5-6 cuts of 1-2 frames, each closer, then a hard cut to the cross-section |
| "FEW MOMENTS LATER" card | v1 20.3-21.4 s | black card, white sans text |
| Smoke puff cloud | v4 18 s, 26 s; v3 drill; sleeping-pills brawl | white fluffy cloud (grey shading or ink outline) that hides a fight or wipes to the next scene |
| Thought bubble | v2 clinic, sleeping-pills brain | round bubble with a dotted or pointed tail |
| Tag labels | v4, sleeping pills | see Typography |
| Shield icon | v1, v4 | a blue shield on the defending character |
| Scan beam | v3 | translucent cyan beam from a scanner |
| Dashed arrow | v3 | dark-green dashed arrow pointing at the problem |
| Green shake arcs, red glow | v2, v3 | 3 green arcs beside a shaking part; soft red radial glow on pain |
| Blurred background | v5 clinic | the window behind is out of focus |
| Camera pan | v4 17.4-18 s | slow slide following the sugar cubes |

## 6. Editing and pacing
- **Speech rate:** 1.75-2.85 words a second; words last a median 0.20-0.24 s; 2-8 pauses longer than 0.6 s per video.
- **Scene length:** the inside-body scene holds 25-40 s with no cuts; the explainer scene holds the rest.
- **Attention is kept by acting and words, not cuts:** each new word pops; mouths and eyes change on every line; one big visual beat every 5-10 s (a tool arrives, a puff, a glow, a bubble).

## 7. Sound design
| | v1 | v2 | v3 | v4 | v5 | sleeping pills |
|---|---|---|---|---|---|---|
| Loudness (LUFS) | -8.5 | -9.3 | -9.9 | -9.3 | -10.9 | -11.1 |
| Music + SFX under the voice (dB) | -22.0 | -13.0 | -17.7 | -10.1 | -13.1 | -18.1 |
| SFX hits a minute (detector) | 43 | 20 | 38 | 124 | 23 | 25 |

- **Music bed:** light comedic, plucked guitar, keyboard, marimba and glockenspiel (v1, v3, v5) or double bass, cello and piano (sleeping pills), under the whole video. v4 switches to electronic / techno.
- **SFX vocabulary (AudioSet labels at each hit):**
  - whip / whoosh on fast moves and cuts
  - plop / boing on things appearing or landing
  - ding / jingle on a realisation
  - whack, smash and bang on hits and fights (the loudest moment of a video, 4-5 dB over the median)
  - real tool sounds: drill (v3), camera shutter clicks (v3, v5), heartbeat (v1)
- **The explainer part is almost dry:** after the cut to the clinic there are few or no SFX (v3: none from 41-60 s; v5: none from 39-60 s). Music and voice only.
- **Masters are loud** (-8.5 to -11 LUFS) and their peaks clip (+1.3 to +2.4 dBFS). We match the loudness range without clipping.

## 8. What we copy and what we don't
- **Copied as techniques:** the caption system, the palette logic, the hierarchy, the effects vocabulary, the editing rhythm and the sound logic.
- **Not copied:** their drawings, characters, watermark text, voices, music files and scripts. Ours are drawn in code, voiced by us, and use Mixkit music and SFX.
- **Fonts:** Luckiest Guy, Anton and Merriweather are free fonts, so we use the same ones.

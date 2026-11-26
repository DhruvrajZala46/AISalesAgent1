# Style decode: captions, colours, themes and effects of 5 reference Shorts (26 Nov 2026)

The user: "I love the style of this creator: the captions, the colours, the themes, the effects. Decode how they've done it."
Videos studied (the user's mp4 files): What Really Happens After You Shave (v1, 720p), How Does Testosterone Gel Work (v2, 720p),
How They Fixed His Curved Spine (v3, 360p), the soda / sugar video "What Happens When..." (v4, 360p), Why Your Pimple Comes Back Bigger (v5, 240p).
v1, v2, v3 and v5 carry the "Dr.healthcare" watermark; v4 uses a different caption style.

Method: 1 fps sheets of each whole video; 30 fps strips of caption onsets; full-size caption crops rendered next to 18 Google Fonts;
k-means colour palettes (12 colours, every 0.5 s); frame-difference and phase-correlation tracking for cuts, holds and camera moves;
outline thickness measured as dark-pixel runs at 720 px width.

## 1. Captions
| | Measured |
|---|---|
| Unit | one word at a time, every spoken word, held until the next word (no gaps, no fades) |
| Font | **Luckiest Guy** (v1, v3, v5), **Anton** (v2), **Merriweather Black**, lower case (v4). All free on Google Fonts. |
| Case | UPPER CASE (Luckiest Guy, Anton); lower case for the serif style |
| Colour | white fill, thin black outline (about 2-3 px at 720 px wide, i.e. 0.3-0.4% of the width), small dark drop shadow down-right |
| Size | cap height 4-6% of the frame width (about 30-43 px at 720 px) |
| Position | centred, one line, about 75-80% down the frame; moved up (about 15-33% down) when the subject fills the lower half (v2) |
| Pop | in 3 frames (0.1 s): slightly small (about 90%) -> 1 frame big (about 120-130%) -> 100%. No easing tail, no fade. |
| Emphasis | none measured: key words (BACTERIA, INFECTION) are the same size; words that look bigger on stills are caught on the pop frame |

## 2. Colours and themes
- **Soft, low-saturation pastels:** median saturation 32-45 of 255 in four videos (v4 is the exception at 114, a red vein theme). Median brightness 210-251 of 255.
- **One flat background colour per scene, about 20-47% of the screen:** pale aqua `#daf8fa` (skin), steel blue `#97c8d6` (arm), grey-blue `#aecbd2` (spine), pale sky `#cfe8fc` (pimple), salmon red `#b94f4c` (vein).
- **Body colours:** skin cream `#f8e4ae` / `#f6e3cb` / `#f7e8d5`, flesh pink `#f6b1a5` / `#f5878a`, fat yellow `#e4ca8f`, muscle brown `#9a6557` / `#96624d`.
- **Clinic theme:** grey walls `#b6c1c9` / `#959594`, white coat `#f5f5f4`, the doctor's green mask and tie, the patient's blue shirt `#4383c8` / `#6c8baa`, brown floor `#a2663e`.
- **Ink:** near-black `#161413` / `#0a0909`, thin even outlines (about 3 px at 720 px; 5 px in the clinic), 3-8% of the screen.
- **Soft shading on top of flat fills:** radial glows (a red glow on a painful spot, pink glow round tired eyes), a vignette on the vein background, a blurred (out-of-focus) window behind the clinic.

## 3. Effects (example frames in the decode sheet)
1. **Crash zoom into the body (v1):** a wide shot of the person, then 5-6 cuts of 1-2 frames each pushing into the spot (0.6-0.85 s), then a hard cut to the cross-section.
2. **"FEW MOMENTS LATER" card:** black screen, white plain sans capitals, centred, about 1.1 s, small watermark bottom right.
3. **Smoke puff:** a fluffy white cloud with grey shading, used for a fight and as a wipe into the next scene (v4 18 s, 26 s).
4. **Thought bubbles** with a dotted tail (the doctor imagines washing hands, the brain imagines being worried).
5. **Tag labels:** small white speech-tags ("Sugar") and boxed labels ("VEIN") in a comic hand font.
6. **Emotion marks:** green shake arcs, red pain glow, anger veins, sweat drops, tears, a dashed green arrow, a cyan scan beam, a shield icon.
7. **Faces on everything:** hairs, bones, a glove, a razor, a scanner, a pimple, sugar cubes, all with the same big round white eyes and small red mouths.
8. **Watermark:** "Dr.healthcare" in a soft rounded font, low opacity, repeated 3-5 times across the frame, some tilted.

## 4. Editing rhythm
- **Static camera, very few cuts:** 1-5 hard cuts per video (1 in v3 and v5, the cut to the clinic). One slow pan (v4, following the sugar cubes). No zooms or shakes otherwise.
- **Limited animation:** 57-85% of frames show no change; drawings change about 5-14 times a second, mostly held 1-3 frames (animation on twos and threes). Only mouths, eyes and the acting part move.
- **Long held scenes:** the cartoon part runs 25-40 s in one set, then one cut to the clinic for the doctor.

## 5. Where ours differs today (GiggleMD engine)
- Our caption outline is 7-8 px at 720 px with a heavy look; theirs is 2-3 px plus a soft shadow.
- Our captions sit 80-96% down the frame; theirs 75-80% (or high when the subject is low).
- Our pop is 1.4 -> 1.0 over 0.12 s with easing; theirs is about 0.9 -> 1.25 -> 1.0 over 3 frames.
- We animate every frame (smooth idle motion); they hold drawings for 2-3 frames.
- Our watermark is one faint "@GiggleMD" at the top; theirs repeats across the frame.
- Not changed: the fonts are free (SIL Open Font License), so we can use the same three. Their drawings, characters and watermark are theirs; we copy the techniques, not the art.

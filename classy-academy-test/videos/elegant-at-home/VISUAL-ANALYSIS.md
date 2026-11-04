# How "How to Look Elegant & Expensive at Home (On Any Budget)" looks (4 Nov 2026)

This is the template for "How to Look Effortlessly Elegant at Home, Every Day".
- It is the original (`GmiAMO93vFE`, Classy Academy, 170k views, 8:19).
- The new video uses the same kinds of pictures but never the same clips:
  - none from the original;
  - none from our earlier videos (`tools/oldclash.py` against all three of them).

## What was inspected

| Evidence | What it shows |
|---|---|
| The original's YouTube storyboard: 105 frames, one every ~4.75 s, enlarged 2x and read by eye | every layout, the cards, the text, the backdrops, the kind of footage |
| Its chapters, captions and top 100 comments | the sections; the viewers' asks (a part two; darker-skinned women in the pictures, 34 likes) |
| Our own last edit (`../age-swaps/`), which the creator approved after v2 | the motion, the no-zoom full screen and the CE logo |

**Not inspected:** the original's video file (YouTube refuses it here). So its motion and music are taken from the
channel's measured files: dissolves, soft piano, no sound effects.

## Layouts (storyboard, with timestamps)

| Layout | Where it is seen | Our helper |
|---|---|---|
| Full-screen film scenes and lifestyle clips | hook 0:00-0:34 (a hat portrait, a sleep-mask film scene, Marilyn Monroe under the title), 4:56-5:01 (Audrey Hepburn, b&w), 7:39-7:44 (a film scene with a glass) | `cfull()`: vertical reels whole over their blurred copy; films full frame |
| A white flash / white card with the section in black script, **numbered** ("2. Matching Sets", "3. Choose Fabrics That Feels Luxurious", "4. Create Your Own D...", "5. Little Elegant Rituals", "6. Making Bedtime a Luxury"), although the voice never says the number | 1:23, 2:33, 3:22, 5:21, 6:40 | `card_at()` |
| **Cream (off-white) backdrop** with one clip centred, or a clip with a short line in grey script ("But here...", "Ask yourself") | 0:39-0:44, 1:04-1:14, 5:31, 6:10 | `oncream()` + `q(..., cls='dark')` |
| Text alone on cream, grey serif/script: "Nothing is wrong...", "It doesn't mean pretending things are perfect", "True elegance starts when you decide you're worthy of your own gentleness" | 5:50-5:55, 6:25 | `cream()` + `q(..., cls='dark')` |
| Rounded-corner frame centred on cream or caramel | 2:13, 3:27-3:52, 4:02, 4:36-4:41, 6:35, 7:09-7:34 | `vframe()` / `wide()` |
| Clip at the left + quote on the caramel backdrop | 0:49, 3:17, 3:57, 4:21, 6:50 | `lclip()` + `q(..., QL)` |
| Rows of 2-4 clips, edge to edge or **framed with gaps**, growing in one by one as items are named | 0:59, 1:19, 2:18-2:28, 2:47-3:12, 4:31, 5:35-5:45, 6:05, 6:45-7:04 | `lrow()` / `prow()` |
| **Circle swatches of fabrics** on caramel (pink, cream, brown, blue, sage knits and silks) | 2:38-2:43 | `circle()` (new: round photos with the fabric's name) |
| Quote on caramel, white serif, one phrase in script: "You don't need to spend a fortune, try pairing what you already own in the same color family", "When your colors and textures flow together, your outfit says intentional instead of accidental" | 1:33-1:43, 2:08 | `q(..., QC)` |
| "Check The Description For / Elegant Homewear Options" over full clips | 1:58-2:03 | `q(..., cls='over')` over `cfull()` |
| The guide: "Check The Description For / Personal Stylist Guide" (+ the website, **left out at the creator's request**) over full clips | 5:06-5:16 | same |
| Outro: "Check The Description For / Loungewear Links" over full clips, then the logo on white | 7:49-8:14 | same + the CE end card |

## Footage

- **Films:** Audrey Hepburn (b&w), Marilyn Monroe under the title, a sleep-mask scene, Margot Robbie at the guide.
- **Lifestyle reels:** women at home in cream, white, beige and blush loungewear:
  - bedrooms, kitchens, sofas, mirrors, flowers;
  - candles, perfume close-ups, a man and a woman at a Christmas tree, a mother and child.
- **Product-like pictures:** loungewear sets, fabric swatches.
- **Palette:** cream, ivory, beige, blush, soft brown; soft daylight.
- **Faces:** mostly young women. The comments ask for more darker-skinned women, so the new video adds them, and women
  of every age.

## Motion and sound (from the channel's measured files)

- **Motion:**
  - soft dissolves and fades through white;
  - panels grow in gently;
  - card text wipes in left to right;
  - **no zoom punches** (the creator asked again: do not zoom clips);
  - the full screen of a vertical reel is the whole clip over its blurred copy.
- **Sound:** one soft piano bed about 12 dB under the voice, steady; no sound effects.

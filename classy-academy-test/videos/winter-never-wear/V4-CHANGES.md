# v4: what changed after the owner's review (29 Oct 2026)

**The feedback:**
- "The visuals do not match the script."
- "Some transitions are incorrect."
- "I do NOT like the blurry background effect at the beginning."
- Use my own videos as the reference; relevance first, elegance second.

## 1. Restudied the channel's own videos first

I re-watched the openings and transitions of the two references frame by frame, at 2 fps and at 5-10 fps around each
transition (`winter/restudy/*.jpg` in the session files):
- "8 Things Elegant Ladies Never Wear" (1.2M views, the closest format);
- "7 Things Elegant Ladies Avoid in Fall".

What they really do:

- **Opening:** the reel fills the whole frame, edge to edge. There is no blurred copy behind it. Slow push-in, short
  dissolves of about 0.4 s, a new scene on the words.
- **Number cards:** fade to white, the black script wipes in, then fade out.
- **Explanations:** the caramel backdrop with one centred reel, or rows of tall reels that grow in one per spoken item.
- **Exit:** a full-screen scene, then white.

## 2. Fixed: the blurred-background layout is gone from the whole video

- v1-v3 used a blurred enlarged copy of each vertical reel behind it, for every full-screen scene: 64 scenes,
  including the opening.
- v4 has none.
- **Full-screen scenes are now full-bleed:** the clip is cut to 16:9 and fills the frame, with a slow push-in.
  - New helper `CB()` / `bleeds()` in `workflow/tools/build.py`; per-clip vertical framing `fy` was set by looking at
    each clip, so the woman and the garment stay in frame.
- **Too-close detail shots move to the caramel layout:** a full-screen enlargement made them soft, so the cobbler sole,
  the long coats and the trench swing are now shown as one centred reel, as the channel does.

## 3. Fixed: every visual chosen for the words under it

- Each of the 78 lines was re-read and its visual re-chosen for what the sentence says.
- 29 new Pinterest searches were made for the actions the script names. 134 clips were downloaded, then checked frame
  by frame and scanned for AI. One clip was flagged (cottonshirt12, 0.81) and is not used.
- The full list is in `STORYBOARD.md` (line by line, generated from this exact edit).

Examples of what now matches:

| Line | Words | v3 showed | v4 shows |
|---|---|---|---|
| 8 | "you grab your thickest knit, pull your coat over the top, and suddenly you can barely bend your arms" | an oversized cream sweater, a coat, a knit | reaching for a knit on a shelf, layering a thick coat over a knit, trying a long coat on with arms out, pulling a chunky knit over the head |
| 14 | "try it on over the thickest sweater... if you can lift your arms and button it" | a coat try-on | a coat on its hanger, then coats tried on in the mirror, arms lifted, buttoning |
| 17 | "Cotton soaks up moisture and dries slowly" | a cotton sweatshirt close-up | water drops sinking into cotton cloth |
| 19 | "Then you step back outside" | a hooded figure in a blizzard | opening the front door in a coat |
| 22 | "A thin silk layer or a good synthetic thermal" | a knit over satin trousers | a silk camisole, and a fitted thermal set |
| 23 | "not the moment you open the door" | (nothing for it) | a long coat by the front door |
| 26 | "soft on the hanger... a fraction of the price" | a sweatshirt rack | knits on hangers, then fingers reading a price tag |
| 27 | "acrylic absorbs very little moisture" | a turtleneck | water beading on fabric, not soaking in |
| 30 | "flip to the label" | a sweatshirt label | fingers turning a knit's care label, a label inside the neckline |
| 31 | "give the knit a gentle stretch... see straight through it" | combing pills | hands pressing a dense knit, then light through a sheer cloth |
| 33 | "washing your knits inside out on a gentle cycle" | a sink | hand-washing a knit, a gentle machine cycle, knits folded smooth |
| 42 | "If your foot slides around" | a shearling boot | a heeled boot stepping on wet stone |
| 44 | "tiptoeing down the pavement or worse, slipping" | a pointed boot | heels stepping carefully on ice and snow, from above |
| 54 | "you hide your hands in your sleeves" | a shivering scene | a hand pulled into a long knit sleeve, cold hands to the face |
| 59 | "You've done a beautiful blowout... hat hair" | one blowout clip | a blow-dry, the finished blowout, beanies tried on long hair |
| 61 | "Researchers writing in the British Medical Journal" | a Little Women scene | women reading the newspaper at a Paris cafe |
| 65 | "make sure your hair is completely dry before you put it on" | a red beret | blow-drying, then putting a beanie on |
| 71 | "Hold the fabric up to a window or a bright light" | ivory cloth in hand | a hand holding fabric up to the sunlight at a window, linen held to the light |

## 4. Fixed: transitions

- **Scene to scene:** the next scene is drawn on top and dissolves in over 0.35-0.45 s. The scene before stays until it
  is covered, so nothing ever dips through to the backdrop.
- **Scene to caramel:** the scene fades while the reel grows from the centre (the reference's own move).
- **Reel to reel on caramel:** the picture changes inside the same frame. The frame does not leave and come back.
- **Into a number card:** fade to white. **Out of a card:** a fade from white.
- All five kinds were checked at 4.5 fps on the rendered frames (`fine/trans.jpg` in the session files).

## 5. Also corrected

- **Episode number:** "Episode 15". The repo's edits run Episode 9-14; "Episode 32" was wrong.
- **"Yes, we have a new name":** the CE monogram on white, the same look as the end card.
- **Film scenes:** *You've Got Mail* is no longer used, because the opening is now creators' full-bleed reels. *Little
  Women* (1994) stays under "I always love hearing from you", the family reading a letter from home. It is unlicensed,
  owner's decision.
- **Clips with burned-in captions are cut:** stiffarms14 "DOS & DON'TS", mirrorcoat11 "Keep Or Return", chunky4,
  winterlook33. They are trimmed or replaced.
- **The guide plug at the end** now sits over a darker scene, so the text reads.

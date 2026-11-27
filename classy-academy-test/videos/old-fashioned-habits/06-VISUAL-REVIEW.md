# Visual review: our draft vs the Classy Academy reference footage (27 Nov 2026)

## What was inspected
- **The reference videos:** the five reference videos the user uploaded. The re-uploads are byte-identical to the
  first uploads, and all are 640x360.
  - Higher-quality versions could not be fetched: YouTube answers "Sign in to confirm you're not a bot" from this
    machine.
- **Measurement:** 18 reference frames and 16 frames of our final render, compared side by side at the same size
  (`qc/ref_vs_ours.jpg` in the session work folder).

## Why our draft looks inferior (measured and seen)

| | Reference | Our draft |
|---|---|---|
| Era of footage | Today: 2020s women, phones, sunglasses, modern interiors | 1940s-50s classroom and sponsored films |
| Colour | Full colour, warm and natural; median saturation **87** | Mostly black-and-white or faded Technicolor; median saturation **54** |
| Sharpness (Laplacian variance, both at 360p) | **246**, despite the 360p file | **188**: 640x480 sources blown up to 1080p |
| Frame shape | Vertical creator reels used *as panels*, or full-frame 16:9 | 4:3 films over a blurred copy of themselves: grey-black side bars on every full-screen shot |
| Subjects | One well-dressed modern woman per shot, outfit fully visible (camel coat, white trousers, satin, knitwear); celebrities (Kate, Jennifer Aniston); film stills of icons | Schoolgirls, men in suspenders, factory workers, title cards ("SPEECH", "HABIT PATTERNS") |
| Settings | Bright minimal apartments, Paris streets, cafés, hotel terraces, wardrobes | 1950s kitchens and bedrooms, sound stages |
| Panels | 3-4 *modern outfit* clips side by side, each a full look (head to shoe), same palette | Panels of old films with different grades, often cropped to faces or hands |
| Product shots | Cut-outs and close-ups of current pieces (satin trousers, loafers, bags), with names ("Quince Satin Pants") | None |

**Conclusion:**
- The layouts, typography, colours and timing match the reference (see the frames: the number cards, the caramel
  split with serif + script, and the panels all line up).
- **The failure is the footage itself.** It is old, colourless, 4:3 and low resolution, and it shows the wrong
  people doing the wrong things.
- No grading or upscaling fixes that. The footage has to be replaced.

## The real constraint
Modern footage of this kind (creator reels, street style, celebrity moments) is copyrighted by its makers. The
user's rules are:
1. modern, sharp, ideally 4K;
2. a verified licence or permission;
3. not Pexels, Pixabay, Unsplash, Mixkit or other free-stock sites.

| Source | Modern and sharp | Licence verifiable | Obtainable from this machine |
|---|---|---|---|
| Pinterest / Instagram / TikTok creator clips | yes | only with the creator's written permission | no: needs the user to ask the creators |
| YouTube Creative Commons (CC BY) creator videos, e.g. NYC street-style series | yes, HD | yes: the licence is on the video page; attribution required | **no**: YouTube blocks downloads here ("Sign in to confirm you're not a bot") |
| Paid stock (Storyblocks, Artgrid, Envato Elements, Shutterstock, Getty) | yes, 4K | yes: a commercial licence per clip | only once the user has an account (files or API key supplied) |
| Wikimedia Commons | very few fashion videos (2 runway hits) | yes | yes, but too little material |
| Public-domain archives (the current draft) | no | yes | yes; **rejected by the user** |

So none of the routes that meet all three rules can be completed from here without one action from the user (see
the decision in the chat).

## What is already done and kept
- **Topic, research, script (917 words), voice and word timings:** unchanged.
- **The renderer and every layout:** they can take any new footage.
- **The logo:**
  - converted to PNG pixel-for-pixel from the uploaded JPEG (1254x1254; checked identical);
  - used unchanged in the corner and on the black intro and outro;
  - the Classy Academy CA monogram is not used, and the old repo file `logo_ce.png` is not used.
- **The 30-second preview** is not made yet: the user asked for it with modern footage only, and no licensed
  modern footage is available yet.

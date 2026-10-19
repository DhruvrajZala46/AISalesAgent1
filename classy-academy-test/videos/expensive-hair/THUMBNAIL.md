# Why Her Hair Always Looks Expensive: thumbnails (v2, in the channel's own template)

v1 (same hair frizzy to glossy, cross and tick on caramel) was rejected: "it does not match my viral thumbnails, most
importantly the visual and the copy text". v2 copies the template of the user's 30 thumbnails exactly.

## What all 30 of the user's thumbnails do (each one looked at; the top 4 measured by pixel overlay)

**One template, all 30, with no exceptions.**

**Pictures.** Three real photos sit edge to edge (x 0-402 | 404-851 | 853-1280) with thin light dividers.
- **Who:** three different elegant women; at least one Black woman in most thumbnails; sometimes a known woman (Kate Middleton), never named.
- **Framing:** waist-up or closer; faces in the top third, above the words; the centre face usually looks into the camera.
- **Clothes and light:** cream, white, black and camel clothes; warm light; Instagram and Pinterest influencer photos,
  phone selfies included.
- **What it shows:** pure aspiration ("be her"), never a problem: no before/after, no cross or tick, no arrows, no labels.
- **Hair videos:** the hair is the hero (Hairstyles 951k: a blonde chignon, a brunette with bangs, a sleek bun;
  Haircuts 242k: bangs, a glossy blowout, a retro bob).

**Words.** Three centred lines, read as one phrase:
1. **Small serif setup:** "How to Look", "The Most", "Elegant Ladies". Font: Cormorant SC, cap height 54, letter-spacing 2, top at y=193.
2. **Big bold keyword:** "Expensive", "Elegant Hairstyles", "Never Wear". Font: League Spartan Bold, 166 px, smaller only to fit
   about 1,110 px; cap top at y=296.
3. **Small qualifier:** "\*Instantly\*", "All Hair Types", "\*avoid these\*". Font: Cormorant SC, cap height 30, 84 px below the big line.

- **Shadow:** soft drop shadow on all text.
- **Underline:** red underline only under "Never".
- **Logo:** top-left.
- **Wording:** the big word is the title's own keyword. The thumbnail restates the promise ("How to Instantly Look More Elegant
  & Expensive" → "How to Look / Expensive / \*Instantly\*"); it does not avoid the title's words.

**How the fonts were measured:** each font was drawn in red over the original and checked by eye.
- League Spartan Bold 166 covers "Expensive" (698k) exactly, and 146 covers "Elegant Hairstyles" (951k).
- Cormorant SC at cap 55 with letter-spacing 2 covers "Elegant Ladies" (1.25M).
- Montserrat, used by the old `thumb_make.py`, was the wrong font.

## The two (YouTube Studio -> Thumbnail -> Test & compare)

1. **A (recommended)** `thumb_A_hair_that_looks_expensive.jpg`: "HAIR THAT LOOKS / **Expensive** / \*It's Not the Cut\*".
   - **Wording:** the same shape and big word as "How to Look / Expensive / \*Instantly\*" (698k, the channel's #3). It names the subject
     (hair) and carries the title's twist.
   - **Photos:**
     - Kaia Gerber's glossy brunette blowout (Hola, press photo);
     - a blonde bouncy blowout (@salonthirtyeight, Instagram post C7xeiazsGAH);
     - a woman in white with long glossy waves (Pinterest, uploaded by AnslenRed; 1170x1636 iPhone photo).
2. **B** `thumb_B_secret_to_expensive_hair.jpg`: "THE SECRET TO / **Expensive Hair** / All Hair Types".
   - **Wording:** the shape of the two hair winners ("The Most / Elegant Hairstyles / All Hair Types" 951k, "... Haircuts" 242k).
   - **Photos:** three hair types and ages:
     - glossy brunette (Pinterest, xsalena);
     - long silver hair (Luisa Dunn, Instagram CVLv3cbhEEg);
     - sleek black silk press (@naomiknowsmore, Instagram DcRjvVBye9e).

**Feed test** (`feed_test_ce.jpg`): at 320x180, beside the channel's 1.25M, 951k, 698k and 242k thumbnails, A and B read as the same
channel's work; "Expensive" reads in one glance.

## Photos: real, checked

- **Source sizes:** all are real-camera sizes, not AI-generator sizes; found with `tools/real_search.py` (AI sizes and AI words dropped).
- **Checked by eye:** skin texture, hands, hair strands, real rooms.
- **Credit:** none of the women is named on the thumbnail, as on the channel's.
- **Permission:** not asked yet, as with the video's clips.

## Build

```
python3 -I workflow/tools/thumb_ce.py spec.json
```

- **Fonts:** League Spartan and Cormorant SC, from Google Fonts (OFL).
- **Spec and sources:** the session's `thumb/spec_ce.json` and `thumb/rs/real/keep.json`.

**Ship it, or change it?**

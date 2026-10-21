# QC report: "8 Things That Make You Look Older: What to Wear Instead" (21 Oct 2026)

Every check below was done on the **exported file** (`8_Things_That_Make_You_Look_Older.mp4`), not on the project. The picture
was checked on contact sheets taken from the export (a frame every 2 s with the words spoken at that moment, all 8:57, twice:
before and after the fixes), plus frame-by-frame sheets of every changed stretch. The sound was measured on the final mix.

## What I fixed after watching the first export

- **Empty backdrop:** three rows opened on the empty backdrop for up to 0.7 s while the voice was talking (0:12, 4:48, 7:58).
  Each row now waits until its first panel arrives, and the picture before it holds until then.
- **Half-empty row:** the deep pleats / turned-up cuff / padded shoulders row sat two-thirds empty for 5 s. Each item is a full
  sentence, so it is now one centred picture per sentence.
- **Shots that showed the wrong thing:**
  - the sneaker panel ran into the creator's denim-jacket transition (1:24);
  - the "chunkier shoe" shot started on a waist-up frame with no shoes (1:26);
  - the lips panel showed a whole face instead of the lips (5:38);
  - the closet clip at 7:44 tilted to the floor.

  Each one was re-timed or re-framed.
- **Crops:** the faces of two full-screen clips were cut off by the 16:9 crop of a vertical reel. Faces are now found
  automatically (`tools/facefocus.py`), and two more clips were changed to the centred layout so nobody's head is cut.
- **Scarf:** the first small-print scarf (R09) turned out to be a brand monogram print when checked at full size. It was replaced.
- **Frame clocks:** about half of the Pinterest downloads had a broken frame clock (a 30 fps clip reporting about 320 fps), which
  showed the wrong frames. Every clip is now converted to a clean 30 fps copy before rendering (`tools/normalize.py`).

## A. Channel style (against "8 Things Elegant Ladies Never Wear" and "Look More Elegant & Expensive")

| Check | Result |
|---|---|
| Voice from the first frame, no music intro, no hook text | **Pass.** Voice at 0.15 s; fade up from black (My7 0:00). |
| "in today's video..." white card, then the script title over a full clip | **Pass.** 0:23.6 card; 0:26.5 title "8 Things that make you look older" (My7 0:25 / 0:28). No "Episode N" (your rule). |
| Centre clip grows from a dot, then a row of 3 before point 1 | **Pass.** 0:34–0:41 (My7 0:34–0:41). |
| White number cards, black script, title read aloud, written on, about 5 s | **Pass.** 8 cards, 4.5–5.9 s (My7 4.4–8.6 s). |
| Inside points: rows built one panel per named item, a centred creator reel, quote lines on caramel, product cut-outs | **Pass.** As listed in `VISUAL-EDITING-DNA` / `VISUAL-DNA-REPORT.md`. |
| Guide call-out after the related point and again at the end | **Pass.** 5:14 after point 5 (colours), 8:40 at the end. Text: "Check the description for / Personal Stylist Guide". No website. |
| Calm clips under the thank-you, then the white end card with the logo | **Pass.** 8:28–8:50, then the CE end card. No black card. |
| Logo top-left on every picture, never on white cards | **Pass.** Your CE / The Classy Elegance logo (not the reference channel's CA). |
| No subtitles, names, brand names, ticks, crosses, statistics graphics, subscribe ask | **Pass.** The only text is the cards, 4 quote lines, 2 one-phrase cues, the title and the guide call-out. |

**Layout mix compared with the 1.2M video:**

| Layout | This video | My7 |
|---|---:|---:|
| centred clip | 39 % | 23 % |
| full screen | 27 % | 22 % |
| rows, pairs and product collages | 20 % | 35 % |
| cards | 7 % | 11 % |
| quotes and cues | 4.5 % | 8 % |

The centred share is inside the range of your top 4 (23–51 %), but rows are used less than in My7. Several items here are
whole sentences, not lists, so they work better as one picture each. **Provisional:** tell me if you want more rows.

## B. Script match

- All 124 sentences have a picture chosen for that sentence (`SCRIPT-TO-VISUAL-MAP.md`).
- Rows and collages bring in each panel on its own word:
  - "thick, clumpy sole / wide, rounded front / Velcro straps";
  - "block heel / loafer / sneaker";
  - "midi / culottes / cropped";
  - "navy / charcoal / ivory";
  - "rose / berry / warm red";
  - "tortoiseshell / thin / clear";
  - "knees / long hair / bright / sneakers / fitted";
  - "longer / looser / darker / safer";
  - "Europe / Asia / Latin America / Africa".

**Where the picture is the nearest real match, not an exact one (said plainly):**

| Time | Line | What is shown |
|---|---|---|
| 0:00 | "caught your reflection in a store window" | A woman walking past a shopfront, then a woman checking herself in a mirror. No real shop-window reflection clip of a mature woman could be found; every candidate was a young model or AI. |
| 0:31 | "start at your feet and work our way up" | A slow pan from sneakers to face over one real full-length clip. The pan is made in the edit; no real tilt-up clip was found. |
| 4:43 | the colour test | A real colour-analysis session with a black drape under the chin. The client is in her 20s–30s, not at a window, and has small speech subtitles. |
| 4:49 | navy / charcoal / ivory | Real clips. Navy and charcoal are the same model. |
| 4:09 | "ask someone to take a photo of you from a few steps away" | A phone camera screen framing a woman on a platform (a repost; original creator unknown). |
| 5:38 | "lips become a little less rosy" | The same woman as the next lipstick shot, before her colour goes on. No usable bare-lip close-up was found. |
| 6:12 | "a very pale nude that erases your lips" | A "concealer lips" makeup reel on a young woman, with its small title. |

**Script:** not changed. Nothing was rewritten to fit footage.

## C. Engagement

- **Pace:** 168 picture changes in 8:57, about 18.8 a minute (panels counted; the reels' own cuts not counted). The median gap is 2.8 s.
  My7 is 16.3 a minute counted the same way.
- **Longest hold with no new picture:** the point cards (4.5–5.9 s) and the 9 s guide clip at the end.
- **People:** women of different ages (20s to 70s+, most 40s–70s), skin tones and hair.
  Famous women appear unnamed: Audrey Hepburn (film), Helen Mirren (red carpet), Ines de la Fressange, Michelle Yeoh,
  Salma Hayek, Iman, Carine Roitfeld, Grece Ghanem.
- **Weaker moments, honestly:**
  - K03 (4:36) is a talking selfie;
  - L02 (5:30) is a woman of about 35–40 for "as we get older";
  - S06 and the end clips (8:12–8:40) show women in their 30s.

## D. Technical (measured on the export)

| Check | Result |
|---|---|
| Format | 1920×1080, 30 fps, H.264 + AAC 48 kHz stereo, 8:57.4; picture and sound the same length |
| Black frames | none |
| Frozen picture over 3 s | only the 8 point cards' held text and the end card, as intended |
| Empty backdrop while talking | none over 0.25 s. The remaining quarter-second moments are the white card and cue writing on, and a panel's first frames growing in, as in your videos. |
| Loudness | −18.0 LUFS integrated, true peak −0.9 dBTP (your top 4: −16.6 to −19.3) |
| Music | 20.0 dB under the voice, from the first word to the last, no ducking, no sound effects |
| Opening and ending | voice at 0.15 s; after "bye everyone", 0.5 s of quiet, the piano swell on the white end card for about 5.5 s, then silence (as measured in your uploads) |
| Clip sound | none; every clip is muted |
| Cards, title, guide, CTA | all present at the times above; the comment and like asks are voice only, as in your videos |

## E. Rights and attribution

- **The manifest lists only what is in the export:** `SOURCES-LOG.md` and `CREDITS.txt` are generated from the final timeline
  (`project/records.py`). 130 picture uses, 127 files. No unused candidate is listed.
- **Licences:** **none of the third-party pictures has a licence or permission.** No creator has been contacted; nothing was sent.
  Credit is not permission.
- **Footage types:**
  - 106 creator and brand reels and photos found as Pinterest pins;
  - 11 retailer product photos (cut out);
  - 6 editorial and press photos of public figures;
  - 2 scanned 1980s catalogue pages;
  - 1 Getty Images press video (A16, red carpet), found via a NewBeauty Magazine pin;
  - 1 studio film excerpt (K01, *Breakfast at Tiffany's*, Paramount, 1961).
- **Highest risk:** K01 and A16 are the most likely to get a Content ID claim or block. If you want the safest upload, swap these
  two first (I can do it).
- **Creators:**
  - 53 original Instagram posts had their author confirmed by Instagram's own embed. Those are the @handles in `CREDITS.txt`.
  - Where the embed could not confirm the author, or the clip was uploaded straight to Pinterest, the credit names the Pinterest
    uploader and says it is not confirmed as the creator.
- **Pin links:** numeric links were still being resolved when this report was written; where one is missing, the uploader's
  Pinterest profile is linked instead.
- **Real footage only:** all 105 video files passed the AI-watermark scan (highest 0.12; the AI line is 0.40). Every clip and photo
  was checked by eye at the seconds it plays. The workers rejected more than 25 candidates as AI.
- **Not stock:** no generic stock sites (Pexels, Pixabay, Mixkit, Unsplash) were used.

## What still needs you

1. **Rights:** use as is (the way your channel's footage is used), or ask me to swap K01 and A16, or to draft permission requests (nothing is sent without your OK).
2. **Voice:** the narration is the synthetic voice of your pipeline. If you record the script, I swap it in and re-time the cuts.
3. **Brand:** the logo is CE / The Classy Elegance, per your rule of 19 Oct. You now call Classy Academy "my channel". If uploads should carry the CA mark instead, say so and I swap the logo and end card.

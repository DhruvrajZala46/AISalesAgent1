# 8 Ways to Always Look Put Together: thumbnail v3 (20 Oct 2026)

**Why v2 was rejected.** v2 (`THUMBNAIL-v2.md`) was turned down: "it does not match my viral thumbnails, most importantly the visual and the copy
text… understand what gets users' attention… don't guess".

**What v3 does.** It rebuilds the thumbnail from the user's three winners:
- "Elegant Ladies / Never Wear / \*avoid these\*", 1.25M;
- "The Most / Elegant Hairstyles / All Hair Types", 951k;
- "How to Look / Expensive / \*Instantly\*", 698k.

Every one of their 9 photos was looked at, and their text positions were measured in pixels.

## How the winners think (decoded from the 9 photos and 3 texts)

### Visual selection: every photo is a "be her" image of polish

| Rule | In the winners | What v2 did wrong |
|---|---|---|
| **The grooming is the hero** | 6 of 9 women have a sleek bun or sleek ponytail; gold earrings, rings and bracelets; manicured hands raised to the face | no sleek hair; jewellery barely visible |
| **Only black, ivory and gold** | every outfit is black or ivory/white; the backgrounds are dim, blurred, golden or stone | a burgundy bag, a wooden kitchen, a striped café cushion |
| **Calm and aloof, never chatty** | eyes closed, profiles, back-of-head views, a hat, one pair of sunglasses; at most one direct gaze | the centre woman mid-sentence with pursed lips; 2 of 3 in sunglasses |
| **Luxury cues, not a busy life** | a yacht, a Paris street, candles, a car interior, a Celine pair of sunglasses | a street snapshot, a home kitchen, a café table |
| **Tight head-and-torso crops** | the woman fills her panel | full-length street shots with a lot of background |
| **Centre face high** | the centre face sits in the top quarter, with the chin at the top line | the centre face low and small |
| **Diversity** | a Black woman in 2 of the 3 | met |

### Copy: the title's own words, in one fixed shape

| Line | Font | What it carries | 1.25M | 951k | 698k |
|---|---|---|---|---|---|
| Top | small serif | who, or "how to" | Elegant Ladies | The Most | How to Look |
| Headline | huge bold | the emotional keyword | **Never Wear** | **Elegant Hairstyles** | **Expensive** |
| Small line | small serif, \*asterisks\* | a short qualifier | \*avoid these\* | All Hair Types | \*Instantly\* |

- **The words come from the title.** "How to Instantly Look More Elegant & Expensive" becomes "How to Look / Expensive / \*Instantly\*".
- **No numbers.**
- **The red underline** appears only under a negative ("Never").

### The text sits in the same place on all three

Measured as the rows of white text pixels across the centre panel:

| Thumbnail | Top line (y) | Headline (y) | Small line (y) |
|---|---|---|---|
| 1.25M | 199-248 | 296-405 | 493-522 |
| 951k | 216-271 | from 289 | 519-549 |
| 698k | 194-247 | 323-434 | 496-531 |

`thumb_ce.py` already uses these positions. **So a photo only fits the centre if the face sits above y≈195.** That ruled out several close-up
portraits (Jasmine Tookes, a sleek-bun profile by @charleighjaynehair): their faces would sit behind the headline.

## v3: the 698k "Expensive" thumbnail, rebuilt for this topic

| Panel | 698k winner | v3 | Creator, how it was checked |
|---|---|---|---|
| Left | black outfit | black blazer, sleek low bun, gold hoops, turned away to a window | **@chloehayward_** (544K followers), Instagram https://www.instagram.com/p/DWBRxH3CKu4/. Instagram's embed shows this exact photo and author. Full 3024x4032 phone photo. |
| Centre | face in the top quarter, black, polished, looking off | black off-shoulder top, black leather, belt, sleek hair with bangs, gold earrings, calm look off camera | **@yvzux** (767K), Instagram https://www.instagram.com/p/Cxz012yMTqS/ (the creator's own Bulgari "ad" post). Slide 4 of the post is this photo: every slide was clicked through in Instagram's embed. |
| Right | white, sleek hair, gold earring, profile | white blazer, sleek bun, statement gold earring, profile | **@diaristudios** (jewellery studio, New York), Instagram https://www.instagram.com/p/DE3QnVyOncz/. The embed shows this exact photo. |

**Palette:** black | black | white, plus gold, as on the 1.25M and the 698k.

### Copy: three versions for Test & compare, on the same photos

| | Top | Headline | Small | Why |
|---|---|---|---|---|
| **A (recommended)** | How to Look | **Put Together** | \*Instantly\* | The 698k text word for word, with this video's keyword. The video has instant fixes (the 30-second finish, the ten-second check). |
| B | Always Look | **Put Together** | \*Effortlessly\* | The title's own words ("Always Look Put Together"), as the winners lift theirs. |
| C | How to Always Look | **Put Together** | \*On Any Budget\* | The budget promise: the 698k's title ends "No Matter Your Budget", and budget is what our own viewers ask most (39 comments, 455 likes). |

**Optional:** make the title match A, as every winner's title matches its thumbnail: "How to Instantly Look Put Together (8 Simple Habits)".
That is the user's call: a title change on a live video resets nothing, but it changes how the video looks in search.

**Feed test** (`feed_test_v3.jpg` in the session):
- **Compared with:** the three winners, the live thumbnail and the rejected v2, all at 320x180.
- **Result:** v3 reads as the same family as the winners. "Put Together" reads in one glance, and the centre face is clear.

## Photos looked at and not used

| Photo | Reason |
|---|---|
| A jewellery-brand portrait | the Gemini ✦ AI watermark in its corner |
| A "faceless success" account | its caption advertises "Higgsfield", an AI image tool |
| Two Instagram links | the posts are deleted, so they cannot be checked |
| Jasmine Tookes's verified close-up; @charleighjaynehair's profile | real and verified, but too tight: the face would sit under the headline |
| Louise Follain for @forloveandlemons | verified and on-palette, but the hair falls across the face, which contradicts "put together" |
| @beautyiconnyc's bun | verified; kept in reserve |

## Rights

None of the creators has been asked, and nothing is sent without the user's OK. If v3 is used, add this line to the description:
"Thumbnail photos: @chloehayward_, @yvzux, @diaristudios".

## Build

```
python3 -I workflow/tools/thumb_ce.py videos/put-together/thumb-v3/spec_v3.json
```

Run it inside the session's `pt-thumb/` folder, where the photos are. Media is never committed.

**Ship it, or change it?**

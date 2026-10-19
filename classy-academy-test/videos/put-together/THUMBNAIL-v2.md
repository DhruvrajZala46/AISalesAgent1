# 8 Ways to Always Look Put Together: thumbnail v2 (19 Oct 2026)

**The video:** https://youtu.be/wz7AdkAUkRU

**The problem:** the live thumbnail's CTR is 3.0% on 475 impressions, giving 56 views (the user's analytics). The running A/B test has no
winner yet. 475 impressions at 3.0% is about 14 clicks, too few for YouTube to separate thumbnails.

**The fix:** three new thumbnails in the channel's own template (`workflow/tools/thumb_ce.py`). They share the same three new photos,
so the test measures the words. Specs: `thumb-v2/spec_final.json`.

## Why the live thumbnail loses (each point checked against data, not taste)

The live thumbnail reads "Effortlessly / **Polished** / \*at any age\*", over three women of 60-70+ in casual tees, in video frames shot at home.

1. **The two weakest long videos on the channel share this look.** From the channel's own public feed, 19 Oct:

   | Video | Views | Published |
   |---|---|---|
   | Body Shape ("Elegant Women Always / Do This / \*at any age\*", three silver-haired women in home frames) | 42 | 14 Oct |
   | Put Together (this one) | 56 | 12 Oct |
   | French Never Wear (sharp street-style photos of three striking women) | **4,739** | 11 Oct |
   | Never Wear in Winter | 263 | 10 Oct |
   | Style Rules | 122 | 13 Oct |

   French Never Wear went out a day earlier than Put Together and has 85 times its views. This is a small sample, and topic plays a
   part, but the pattern points the same way as the reference channel's.

2. **The reference template never looks like this.** All 30 Classy Academy thumbnails (`ref_sheet` in the session):
   - aspirational influencer photos ("be her"): women in their 20s-40s;
   - tailored black, cream and camel clothes, gold jewellery, sunglasses;
   - warm, slightly dark light, so the white words pop.

   None shows a plain T-shirt in a hallway. The live photos are bright and flat, so "Polished" sits on a striped T-shirt and loses contrast.

3. **"Polished" is not the keyword.** The title, the search and the niche all say **"put together"**:
   - Classy Academy's own thumbnail for this topic reads "Always Look / Put Together";
   - the channel rule (`workflow/4-THUMBNAIL.md`) is to restate the title's keyword.

4. **"\*at any age\*" tells most of the audience the video is not for them.** The channel's viewers are 20s to 70s. An older-women-only
   thumbnail fits a "women over 50" channel, not this one.

## What wins on this topic (YouTube search "how to always look put together", 19 Oct)

Each video is scored by how far it beat its own channel: views ÷ the median of that channel's last 30 uploads.

| × median | Views | Channel | Title | Thumbnail |
|---|---|---|---|---|
| **87.7×** | 2.0M | What To Wear | 7 SECRETS of Women Who ALWAYS Look Put Together \| Classy Outfits | women in camel and black tailoring, "Style Secrets of Well Dressed Women" |
| **76.0×** | 1.7M | Simone Nicole | How to look good everyday \*even on a budget\* | "Look good everyday / \*simple affordable tips\*" |
| **36.9×** | 332k | Julianna Lee | How to Always Look Put Together \| Why Some Women Look So Polished | a collage of elegant women in black and cream, "Always Look Polished" |
| **25.7×** | 238k | jess caelyn | How to Always Look Polished and Put Together | |
| **10.0×** | 280k | Jaz Turner | how to ALWAYS look put together on ANY budget | |

Data: `thumb-v2/medians.json`.

**What these winners show:**
- **Pictures:** sharp, aspirational women in classic tailoring.
- **Words:** the keyword itself, plus either *the women who do it* or *budget*.

## The three new thumbnails (YouTube Studio -> the video -> Thumbnail -> Test & compare, all three)

| | Top line (Cormorant SC) | Headline (League Spartan Bold) | Small line | The evidence |
|---|---|---|---|---|
| **A (recommended)** | Always Look | **Put Together** | \*Effortlessly\* | The title's keyword, as on Classy Academy's own thumbnail for this topic. The shortest top line, so the cleanest read at feed size. |
| B | How to Always Look | **Put Together** | \*On Any Budget\* | Budget wins in the niche (76×, 10×) and is what our viewers ask about most (39 comments, 455 likes; `videos/put-together/PACKAGE.md`). |
| C | Women Who Always Look | **Put Together** | \*8 Quiet Habits\* | "The women who do it" angle of the 87.7× and 36.9× winners. |

**Photos (left to right):** cream blazer over black, the Birkin, a black blazer with coffee. All three are real women, with faces in the top third.
Each is checked at the creator's own post.

| Panel | Creator | Source | How it was checked |
|---|---|---|---|
| Left | @anastajsha_mn (Frankfurt) | Instagram post https://www.instagram.com/p/DdqmR1Mlz3J/ (a multi-photo post; this is one of its photos, found via a Pinterest pin that links to it) | Instagram's own embed of the post names the author and shows the same outfit; full 3024x4032 phone photo; checked by eye |
| Centre | @kirasfashionfinds (1.3M) | frame at 0:22 of the Instagram reel https://www.instagram.com/reel/DdrjZyRRaYT/ | the author was verified for the hair video; the clip's AI-watermark score is 0.00; checked by eye |
| Right | @afroditikomichili (Athens) | Instagram post https://www.instagram.com/p/DeE-IxKCPqV/ | Instagram's own embed shows this exact photo and author; full 3024x4032 phone photo; checked by eye |

**Rejected, and why:**
- **Most Pinterest "outfit" photos:** AI. One uploader's own caption speaks of "my AI influencers". Many studio-perfect portraits came from "follow back" accounts, and many images share an AI-generator size (941x1672).
- **A Black woman in a cream suit (two angles of one shoot):** its copies sit on an "AI Twin" board and on a Trendyol product page, and its creator could not be traced.
- **A Black woman in a cream coat:** the uploader's connected Instagram account could not be opened.

**Feed test:** `feed_test.jpg` in the session puts the three at 320x180 next to the live thumbnail, Classy Academy's "Put Together" thumbnail and four niche winners.
- "Put Together" reads at a glance on all three.
- A is the clearest.
- The new thumbnails sit with Classy Academy's thumbnail as the same family, darker and more aspirational than the live one.

**Not done, on purpose:**
- **No new "at any age" version.** The live thumbnail already is one, and it is the version losing (see point 1).
- **The title is unchanged:** "8 Ways to Always Look Put Together" (34 characters).

## Rights

None of the three creators has been asked; nothing is sent without the user's OK. They are credited here for the description
("Thumbnail photos: @anastajsha_mn, @kirasfashionfinds, @afroditikomichili").

## Build

```
python3 -I workflow/tools/thumb_ce.py videos/put-together/thumb-v2/spec_final.json
```

Run it inside the session's `pt-thumb/` folder, where the photos are. Media is never committed.

**Ship it, or change it?**

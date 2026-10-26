# Steal like an artist: fashion winners from niches we never explored (26 Oct 2026)

The user's brief:
- fashion, clothes and outfits (with put-together and beauty), not etiquette;
- look in niches and channels we never explored, at videos with millions to tens of millions of views;
- take the psychology, not the video, and rebuild it in our DNA;
- one best next idea.

No idea is guaranteed millions. This one has the most proof of views, likes and clicks we could find.

## How it was found (all public, no login, no cookies)

- **Our lane, fashion only.** Today's `content-idea` run: 59 channels, 3,383 videos, filtered to 1,352
  fashion/outfit titles. Most top shapes are taken (see the end).
- **Wider fashion search.** 25 women's-fashion YouTube searches (627 results). Every video of 300k+ was
  scored against its own channel's median: the latest 60 long uploads of 43 channels.
- **Neighbouring niches, never explored.** 30 searches:
  - royals, style icons, old Hollywood, fashion history, flight attendants;
  - home decor "looks expensive", minimalism, decluttering, shopping psychology;
  - men's style, beauty, and Korean/Japanese/Italian style.
- **Icon deep-dive.** 16 searches on Diana, Kate, Audrey, Grace Kelly, Jackie and Carolyn Bessette-Kennedy,
  Jennifer Aniston, Amal Clooney, Sofia Richie and French actresses. Medians computed for 20 more channels.
- **Re-wear check.** 7 searches on re-wearing and making old clothes look new.
- **Love.** Views, likes and dates read live for about 50 winners (`yt-dlp --skip-download`, embedded player).
- **What they teach.** Captions read for 3 winners: Kaiti Yoo, bestdressed and Shea Whitney.

Caveats:
- Some channels' recent uploads are tiny, which inflates their multiples (TheThings, The List, Ageless
  Glamour). Those are not used as proof.
- Big media brands (Vogue, Vanity Fair, BuzzFeed, Bright Side) and DIY-craft channels are left out: their
  views say nothing about an idea's pull.

## What we found: two engines

**1. Icons bring the clicks.** Princess Diana's fashion is a hit across 6 channels:

| Views | Multiple | Channel | Title | Like rate |
|---|---|---|---|---|
| 7.07M | 146x | Real Royalty | The Hidden Meaning Behind Diana's Bold Fashion | 0.60% |
| 6.52M | 434x | Kaspar Jones | Princess Diana - Fashion Queen | 0.74% |
| 2.52M | 52x | Real Royalty | Princess Diana's Most Iconic Fashion Moments | 0.75% |
| **2.37M** | **57x** | Star News Today | **10 Fashion Tricks Princess Diana Used to Make Old Clothes Look New Again** | 0.55% |
| 1.35M | 26x | Harper's Bazaar UK | Princess Diana's best royal fashion moments | 1.17% |
| 0.42M | 28x | The Secret Garden of G. | 20 Items Princess Diana Loved You Can Still Buy Today | - |

Other icons:
- Audrey Hepburn & Givenchy: 1.78M at 69x (MsMojo, 1.45%).
- Carolyn Bessette-Kennedy: 1.53M at 56x (Cultured Elegance).
- Kate: 1.01M at 23x (The Royal Family Channel).
- Inside our own lane: "How to Dress Like Jennifer Aniston" 25.6x and "She's 68 in Paris - 5 Style Rules She
  Never Breaks" 13.6x.

Documentaries about icons get watched but not loved (0.5-1.5% like rate). The **teaching** versions get far
more love: "10 TIMELESS Style Tips from FASHION ICONS" 3.44% (Shea Whitney) and "10 OUTFITS Inspired by Audrey
Hepburn & Grace Kelly" 4.74% (Shirinatra).

**2. "Make what you already own look better or new" brings the love.**

| Views | Likes | Like rate | Multiple | Channel | Title |
|---|---|---|---|---|---|
| 7.27M | 246,768 | 3.40% | 200x | Asia Jackson | How to Make Your Outfits Better (re-styles her own old outfits) |
| 4.08M | 166,725 | 4.09% | 4.1x | Leyla Tavas | how to make ur BORING clothes CUTE |
| 3.07M | **220,703** | **7.19%** | 27.3x | Kaiti Yoo | you don't ACTUALLY have "nothing to wear." you're just shopping wrong. (outfit repeating) |
| 2.46M | 126,554 | 5.15% | 6.7x | Claire's Monologue | How To Make Your Outfits BETTER |
| 2.37M | 13,057 | 0.55% | 57x | Star News Today | 10 Fashion Tricks Princess Diana Used to Make Old Clothes Look New Again |
| 2.19M | - | - | - | Leyla Tavas | how to make ur BASIC clothes look CUTE |

- Five channels have 2M+ views; three have 120k-250k likes.
- The 85.66M / 6.37M "clothes transformation" crafts videos (scissors, DIY) are the same wish in another
  niche. They are off our DNA and not used as proof.

**Our repo has never covered re-wearing or making old clothes look new** (grep of every script and research
file: no match).

## The psychology we steal (not the videos)

1. **Permission and relief:** "you don't need new clothes; you already have enough". Kaiti Yoo built it on
   outfit repeating; Simone Nicole's 1.76M opens with "you are worth taking care of".
2. **Transformation:** the same piece, before and after, which satisfies curiosity. Asia re-creates her own
   old outfits. Our own replay study found the before/after moments are the most replayed.
3. **Icon proof:** even a princess re-wore her clothes. This gives the viewer status and permission, and it
   brings the click.
4. **Any budget, timeless, anti-trend:** already our stance, in our own words: "It's all about choosing
   quality over trends."

## ★ The idea: 8 Ways to Make Old Clothes Look New Again

- **Title scores.** `title.py` 94/100. The one note is mobile truncation, and the subject survives it ("8 Ways
  to Make Old Clothes Look New...").
- **Second title for YouTube's title test (Test & compare):** "8 Tricks Princess Diana Used to Re-Wear Her
  Clothes" (94/100). This tests whether the icon raises clicks for us.
- **The promise.** She will know 8 ways to make clothes she already owns look new, and wear them again with
  pride. Diana and Kate did it, and she can too, on any budget.
- **How it is told (our DNA):**
  - the calm voice;
  - each way is a habit she can practise, with "instead of X, try Y";
  - the demo edit: the same woman and the same piece, before and after;
  - recognisable elegant women seen re-wearing (Diana, Kate);
  - no scissors or DIY;
  - no rich-vs-poor price ladders. "$100 vs $10,000" is a red line.
- **Why now.** Late October is when wardrobes change over for the season ("what do I wear this winter?"). This
  is a reason, not a measured trend.
- **Audience fit (`fit.py`).** Our styling topic median is 0.7x across 9 videos. That is flagged, not hidden.
  - Our winners are made by the "what to wear instead" swap format (Never Wear 9.1x, Beginner's Guide 4.6x),
    which this idea reuses.
  - The stance check passes: re-wearing is the opposite of chasing trends.
- **Not repeating ourselves.** These are already taught and must not come back:
  - Put Together #1-2 (outfit formulas, a closet that goes together);
  - Dressing Rules (fit, fabric);
  - Winter #2 (pilled knitwear).
- **The 8 ways are not chosen yet.** Stage 2 builds the proof map from these winners' transcripts and top
  comments, two proofs per tip, and the user approves it before any script.
- **Rights.** Diana and Kate footage is news or archive, with no licence on record. Log every clip in
  `SOURCES-LOG.md`; the creator decides (CHANNEL-DNA section 8).

## More stolen ideas, ranked

| # | Idea (our version) | Stolen from | Proof | Flag |
|---|---|---|---|---|
| 2 | What Your Outfit Says About You | men's style | MVPerry 3.96M, 115,522 likes, 32.7x; Tim Dessaint colours 1.57M 4.6x | Both men's channels; women's version untested |
| 3 | 8 Style Rules Princess Diana Always Followed | royals / icons | Diana 6 channels 1.35-7.07M; icon teaching 3.44-4.74% likes; lane 25.6x / 13.6x | Views strong, love moderate; single-icon footage rights |
| 4 | Why Japanese/Korean Women Always Look So Polished | culture style | Wanhee 2.11M 70x 3.31% (Korean), 1.15M 38x (Japanese) | Our French video exists; culture red line ("not elegant") |
| 5 | How Women Got Dressed in the 1950s (and what to keep) | fashion history | Sage Lilleyman 3.37M 40.6x; 14th century 12.6M 25.9x | One channel in our lane; love 0.99% |
| 6 | Makeup Mistakes That Make You Look Older | beauty | Ali Andreea 2.95M 27x 3.02%; Dominique Sachse 1.70M 28.7x | Beauty, new for us; age hook must stay kind |
| 7 | Why Basics Look Cheap (and how to fix them) | basics | Petite Dressing 1.01M 28.6x; MAIAZINE 13.5x; bestdressed 6.45M, 276,995 likes | Overlaps Put Together |

## Taken in fashion (already made or on our channel)

Never Wear (and fall), styling and fit mistakes (Body Shape, Dressing Rules), put together, French, winter
trends and winter mistakes, colour combos, look expensive (and at home), quiet luxury, jewelry, jeans, casual
yet elegant, beginner's guide, old-money essentials, summer shoes, hairstyles, haircuts.

**Ship it, or change it?**

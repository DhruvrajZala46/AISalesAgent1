# Prompts for every new video

Copy a prompt, fill the `[brackets]`, send it. Each prompt points Claude to the playbook in this
folder, so nothing has to be typed or explained again. Send them in order: one stage at a time,
and approve each one ("ship it") before the next.

> Tip: open a new session for each new video, on the branch you work on.
> The first prompt of every session sets everything up.

---

## 0. Start of every session (paste first)

```
Read classy-academy-test/workflow/GOLD-STANDARD.md and README.md, and run classy-academy-test/workflow/setup.sh
for a new video folder in the scratchpad named [short-name, e.g. old-money-fall].
Read classy-academy-test/voice.md fully, especially "How I teach".
Confirm in 3 lines: the setup worked, the rules that never change, and how my channel teaches.
Make this video the way GOLD-STANDARD.md describes, or better.
```

---

## 1. Topic

```
Find my next video idea. Follow classy-academy-test/workflow/1-TOPIC.md and the content-idea
skill exactly, with today's real data.
[Optional: I am thinking about [topic] / it is for [season or month] / avoid [topic].]
Give me 3 ideas ranked by evidence: the niche multiple AND what my own viewers already reward,
plus for each one the teaching angle (what she will be able to do after watching).
Drop any idea that can only be told as news, quotes or a culture report.
```

---

## 2. Script (the most important one)

```
Write the script for: "[the approved idea / working title]".
Follow classy-academy-test/workflow/2-SCRIPT.md and the yt-script skill exactly.

The content is what matters most. Before writing:
- study the tips inside the biggest winning videos on this topic AND my own videos,
- keep only tips that are concrete, true, useful on any budget and at any age,
- rewrite every tip in MY voice. I teach; I never quote people, name people or report on a
  culture. My viewers must come away with something real they can use tomorrow.

Every point uses my 7 teaching steps: name it -> validate ("We get it") -> WHY it changes how
she looks and feels -> the principle line -> what elegant women do -> the swap or how-to with
named pieces and colours -> the inner payoff.

It must pass dna.py ("TEACHES LIKE THE CHANNEL") and fit.py ("FITS THE CHANNEL") before you
show it to me. Show me the 2 best hooks with scores, the full script with [ON SCREEN] on every
beat, the runtime, both check results, and one line per point on why it is valuable to her.
Do not build anything yet.
```

To change the script after reading it:

```
Change [point / line]: [what to change]. Keep my teaching steps, re-run dna.py and fit.py,
show me only what changed plus the check results.
```

---

## 3. Video

```
The script is approved. Build the full video.
Follow classy-academy-test/workflow/3-VIDEO.md exactly: the "stage" edit of GOLD-STANDARD.md.

Non-negotiable:
- real footage only, never AI clips: run aiscan.py on every clip and look at each one yourself;
- every clip checked frame by frame against the exact words it sits under, never guess;
- each clip used once, every creator credited;
- white number card, then one calm frame per point with the pictures changing inside it on the
  exact word, the same woman from mistake to fix, rows only for lists, full-screen only for the
  hook, title, guide and ending;
- NO sound effects; one soft solo-piano bed ~12 dB under the voice, steady, no drop-outs;
- voice: Kokoro af_heart at speed 0.80;
- full QA (qa.py, flash.py, a per-second contact sheet watched end to end) before you send it.

Take the time it needs. When it is clean, send me the full 1080p Gofile link and the credits.
```

If something in the video is wrong:

```
In the video at [mm:ss], [what is wrong]. Fix it, re-check that whole section frame by frame,
re-render, run the full QA again, and send the new 1080p link.
```

---

## 4. Thumbnails

```
Make the thumbnails for "[title]". Follow classy-academy-test/workflow/4-THUMBNAIL.md and the
yt-package skill exactly: my channel's measured layout (3 real women, Cormorant top line,
Montserrat headline, red underline under the first word, small line, CE logo), real verified
photos only (no AI, no content farms), max 3 words, not repeating the title.
Make 3 versions (my #1 format, another wording, an "at any age" version), test them at feed
size next to competitors, send me the files and tell me which one to use first.
```

---

## 5. Title, description, tags

```
Write the title, description, tags and chapters for "[working title]".
Follow classy-academy-test/workflow/5-PACKAGE.md with the yt-package, yt-seo and yt-chapters
skills exactly. Chapters from the final video's timing. Include the stylist guide link, the
part-two question, 3 hashtags, every visual credit, the thumbnail photo credits and the music
credit. Run the query test. Give me everything in copy blocks and commit PACKAGE.md.
```

---

## All-in-one (when you want Claude to run every stage, stopping for your OK)

```
New video. Run the full workflow in classy-academy-test/workflow/ (README.md), stage by stage:
1 topic -> 2 script -> 3 video -> 4 thumbnails -> 5 title/description/tags.
Stop after stages 1 and 2 and wait for my "ship it" before going on. Never build the video
before I approve the script.
The script must teach the way I teach (voice.md "How I teach", dna.py + fit.py must pass):
real, concrete, valuable tips in my own voice, nothing that is not useful to her.
Real footage only, no AI, no sound effects, af_heart 0.80, every creator credited.
[Optional: topic idea / season / anything to avoid.]
```

---

## After the video is live (optional)

```
My video "[title]" is live. Here is the retention CSV: [attach]. Use the yt-retention skill:
name the biggest leak and one change for the next video, and add what we learned to
classy-academy-test/workflow/LEARNINGS.md.
```

```
Add my new video "[title]" ([YouTube link]) to the audience baseline (transcript + views),
rebuild fit.py, and tell me if anything changes in what my viewers reward.
```

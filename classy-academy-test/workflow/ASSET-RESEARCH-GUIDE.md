# Asset Research Guide - finding, verifying and logging every visual (17 Oct 2026)

Use this for every script before any clip is downloaded. It turns a script line into a visual brief, finds
candidates, proves where each one comes from, and records the rights decision in `videos/<slug>/SOURCES-LOG.md`
(template: `SOURCES-LOG-TEMPLATE.md`). Visual DNA: `../VISUAL-EDITING-DNA.md`. What the creator's own footage is
and where it was traced: `../source-trace-2026-10-17.md`.

## 1. The visual research brief (one row per script line, before searching)

| Field | What to write | Example (reference video, 3:03) |
|---|---|---|
| Line | the exact sentence | "instead of rushing with 'Uh, I'm not sure', you can simply say 'Let me think for a second'" |
| What she must understand | the one idea the picture carries | a calm reply in a real conversation |
| What she must SEE | the concrete thing: a person, an action, an object, words | a woman in a conversation, pausing, then answering; the two phrases written |
| Layout (creator's set first) | white number card / full sentence on caramel / framed clip on cream with words beside it / full-screen clip / row of 3 / single word card / chat bubbles | framed clip on cream, phrase in script beside it |
| Subject | who (age, look; at least one woman over 45 in any group) | two women seated, interview or sofa |
| Action | what happens in the shot (speaking, listening, texting, walking, pausing) | one speaks, the other listens |
| Setting | where | living room, studio, café |
| Composition / framing | wide / medium / close-up; where the face is | medium two-shot, faces in upper third |
| Camera | static / slow push / handheld | static or slow |
| Light | soft daylight, warm interior; never harsh flash | soft daylight |
| Text on screen | only the line to remember, the exact phrase, or one word | "Uh, I'm not sure" -> "Let me think for a second" |
| Must avoid | what would contradict the line | shouting, laughing loudly, phone in hand |

Rule of thumb: if the picture would also fit three other lines in the script, it is decoration, not
demonstration. Find a better one.

## 2. Where to look, in order of how safe the rights are

1. **Free-licence libraries, per clip** - Pexels (Pexels License: free commercial use and editing, no attribution
   required; identifiable people must not be shown in a bad light or as endorsing a product; no reselling unaltered),
   Pixabay (Pixabay Content License; read the clip's page), Mixkit (**only** clips under the "Stock Video Free License";
   some older clips are "Restricted License - 720p, personal use" - test: the `-1080.mp4` file exists only for
   free-licence clips), Coverr. Save the clip page and licence page as PDF/screenshot with the date.
   *Proof this works for the creator's look:* the reference video's restaurant shot at 1:19 is a Pexels clip
   (ID 8922355), see `../source-trace-2026-10-17.md`.
2. **Paid stock, per licence** - Storyblocks / Artgrid / Envato Elements (subscription; check the licence covers
   YouTube monetisation and keep the download record), Shutterstock / Pond5 / Getty (per clip; "editorial use only"
   clips are conditional).
3. **Archive footage of public figures** - Getty Images (includes BBC Motion Gallery), AP Archive, British Pathé,
   Reuters. Licensed per clip, often "editorial". This is the lawful way to show Princess Diana or a royal speaking.
   Price and terms are per request; log the quote.
4. **Creator permission** - Instagram/TikTok/Pinterest creators (the fashion and lifestyle reels the channel uses).
   Find the **original** account (section 3), ask in writing with the template below, save the reply. A "yes" that
   names the clip and "YouTube, monetised, edited" is a licence; a like or an emoji is not.
5. **Public domain, territory-checked** - films whose US copyright lapsed (e.g. "Charade", 1963, Audrey Hepburn: no
   valid notice; its score and story may still be protected, and other countries may differ), US federal government
   footage, Internet Archive collections marked public domain, Wikimedia Commons files with a stated free licence or
   PD status (read the file page, not the category). Always "conditional" with the evidence written in.
6. **Film / TV / interview excerpts with no licence** - studio films (e.g. "Breakfast at Tiffany's", "Sabrina",
   "Scent of a Woman"), talk shows, news. These are copyrighted and Content ID usually knows them. Not "cleared" by
   credit, shortness, editing or fair-use arguments. Only used if the creator decides so, row by row, in the log.

Never: AI-generated people or AI-animated photos; a clip with someone else's watermark, logo or burnt-in text left
in; music that comes inside a clip.

## 3. Finding the original of a clip (provenance)

1. **Grab 2-3 clean frames** (no CA logo, no text overlay) from different moments of the clip, at the highest
   resolution available.
2. **Reverse image search each frame** - Yandex Images ("search by image", strongest for faces and film stills),
   Google Lens, TinEye (exact copies, oldest first), Bing Visual Search. Our tool: `tools/revsearch.py` (Yandex
   search -> candidate pages -> similarity score -> review sheet), then confirm every hit **by eye** - the automatic
   score alone produced false matches in our test (unrelated pages scoring 0.9+ on 160x90 frames).
3. **Follow the chain to the earliest upload** - a Pinterest pin is almost never the original: open its outbound
   link, look for the handle in the corner of the video, a watermark, the account named in the pin title ("via
   @..."), then search that handle on Instagram/TikTok and find the earliest post of the same clip (same framing,
   same first second). A film still: confirm the film by a second independent source (a frame on a film database, a
   review page, the dialogue).
4. **Record the chain** in the log: "found on Pinterest pin X -> outbound link Y -> original Instagram reel Z by
   @handle, posted <date>".
5. **Label the result** (used in `../source-trace-2026-10-17.md`):
   - **Confirmed** - the same footage found at its original source (studio film identified by an identical frame
     plus a second source, stock clip page, creator's own post).
   - **Likely** - the same footage found, but only on re-uploads or aggregators (Pinterest, GIF sites, fan
     channels); the original owner is inferred, not seen.
   - **Similar visual reference** - only look-alike images; useful as a style reference, says nothing about origin.
   - **Unresolved** - nothing found.

## 4. Comparing candidates (fill before choosing)

| Line | Candidate | Shows exactly the line? (yes/partly/no) | Layout fit | Quality (res, light, stable) | Age/diversity fit | Original found? | Licence | Decision |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Pick the best "yes" with a clean licence. If the only "yes" is unresolved, look again in section 2 (1-4) or change
the layout (a framed clip of a licensed woman + the exact phrase written beside it often teaches better than a
famous face).

## 5. Permission request (template)

> Hi <name>, I run the YouTube channel <channel>, which teaches everyday elegance. I would love to include your
> video <link> (about <n> seconds, from <mm:ss>) in an upcoming video about <topic>. It would be cropped/trimmed and
> shown with narration, on a monetised YouTube video and its Shorts. I would credit you as "<handle>" in the
> description. May I have your permission for this use? A simple "yes, you may use <link> on YouTube" is enough.
> Thank you so much.

Save the full reply (screenshot with date and handle) in the log's evidence column.

## 6. The two checks before delivery

1. **Copyright** - every row in SOURCES-LOG is "cleared", or "conditional" with conditions met, or "unresolved" with
   the creator's written decision next to it.
2. **YouTube monetisation (reused / inauthentic content)** - YouTube's monetisation policies exclude content reused
   without significant original commentary or modification, and mass-produced/template-like content; the test is
   whether an average viewer can tell our videos apart and sees our own teaching. Our original value is the
   script, the narration and the teaching layouts (written phrases, cards). Check: long stretches of someone else's
   footage with no teaching on screen, the same template from video to video with only words swapped, or
   compilations of film clips put a channel at risk even when each clip is licensed.

## 7. Final production audit (tick every line)

- [ ] Every script line has a brief row; every picture shows the exact thing said (not a loose theme).
- [ ] The teaching layouts carry the teaching: exact phrases written beside a real conversation; the reason or payoff
      as a full sentence on caramel; number cards.
- [ ] Named women only where the script names them, and only with footage whose rights row is decided.
- [ ] At least one woman over 45 in every group shot; different backgrounds and sizes.
- [ ] No AI people, no AI-animated photos, no watermarks/handles/burnt-in text left in.
- [ ] SOURCES-LOG complete; unresolved rows listed to the creator with the risk; credits text written.
- [ ] Music licence in the log; music ~12 dB under the voice; no sound effects unless the creator asks.
- [ ] Reused-content check (section 6) written in one paragraph in the log.

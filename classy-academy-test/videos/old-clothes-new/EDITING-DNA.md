# Reference Editing DNA Sheet

**Reference:** "The Most Elegant (Easy) Hairstyles For All Hair Types". The user's upload is a 360p copy, 8:14 (494 s).

**How it was measured:**
- One frame per second, all 494 frames, laid out as contact sheets (`ref/sheets/s00-s08.jpg`).
- ffmpeg scene detection: 90 hard cuts.
- Loudness measured with ffmpeg `ebur128` and `silencedetect`.

Everything below was seen in those frames or read from those numbers. Nothing is inferred from other videos.

## 1. Timeline (what is on screen, second by second)

| Time | Screen | Notes |
|---|---|---|
| 0:00-0:05 | Full-screen real clips: a woman in a white coat and hat leaves a door; a profile of a woman with an updo | Hook. Logo top-left from 0:01. |
| 0:06-0:09 | **White background**, two portrait photos appear one by one, side by side | "Photos on white" row. No logo. |
| 0:10-0:12 | **White card "In today's video"**, black Pinyon-style script wiping left to right | Not a number card. |
| 0:13-0:21 | Full-screen clips (a hair tutorial at shutters, a woman by the sea) | Logo on. |
| 0:22-0:25 | Full-screen clip with the title over it in white serif: "Episode 3: / The Most Elegant Hairstyles" | The title sits over a clip, not over a card. |
| 0:26-0:30 | White background, a row of three photos appearing one by one | Same photo-row grammar. |
| 0:31-0:32 | White number card "1. The French Twist", wiping in | About 2 s. |
| 0:33-0:52 | Full-screen film clips (16:9 film scenes), then a 3-panel row of photos on the caramel background, then full-screen tutorials | Mixed. |
| 0:53-1:09 | Caramel backdrop: a row of 2-3 tall panels, then 4 tall panels edge to edge | Panels enter one at a time. |
| 1:10-1:47 | **One tall vertical tutorial clip centred on the caramel backdrop**, held about 37 s | Creator credit in small script at the frame's lower right ("@... on TikTok"). A tip in small script on the left ("* We recommend using a french pin *"). |
| 1:48-1:51 | Full-screen clip | |
| 1:52-1:56 | White number card "2. Half Up Half Down" | |
| 1:57-2:08 | White-background row of three celebrity photos, then caramel rows of photos | |
| 2:09-2:48 | One tall tutorial clip centred on caramel, held about 39 s | Creator credit lower right. |
| 2:49-2:52 | White number card "3. Hollywood Waves" | |
| 2:53-2:56 | White row of three celebrity photos | |
| 2:57-4:08 | Tall clips centred on caramel (several creators, each held 10-40 s) | |
| 4:10-4:49 | One tall tutorial, held about 40 s | |
| 4:50-4:54 | Full-screen film scene | |
| 4:55-5:20 | Tall tutorial centred on caramel | |
| 5:21-5:26 | Caramel row of 2-3 photo panels | |
| 5:27-5:29 | White number card "4. The Low Bun" | |
| 5:30-5:31 | Full-screen clip | |
| 5:32-5:37 | **One photo at a time, small, centred on white** (three celebrities in turn) | |
| 5:38-5:59 | Caramel: 1-3 panels, rows building, then a tall tutorial | |
| 6:58-7:06 | White row of three photos (one of them the Princess of Wales) | A named woman shown in a photo row. |
| 7:07-7:37 | Caramel: one framed photo, then rows of 2-3 photos with gaps (floating) | |
| 7:38-7:44 | Full-screen clip (a woman in a headband with coffee on a balcony) | |
| 7:45-8:06 | Haze into a full-screen clip of a woman on a bed by a bright window | Outro. Static and calm. |
| 8:07-8:13 | White end card with the logo | |

## 2. The rules this gives (what our edit copies)

1. **Footage type.** Real vertical creator reels from social media (TikTok, Instagram and Pinterest tutorials and lifestyle clips) and celebrity or editorial photos. Film scenes are used only for named-film moments. **No stock-library look.**
2. **Layouts.** Five layouts make up the whole video:
   - full-screen clip;
   - a white background with photos appearing one by one in a row;
   - the caramel blurred backdrop with 2-4 tall panels;
   - **one tall tutorial clip centred on caramel, held a long time** (10-40 s) while the narration teaches that step;
   - the white script card.
3. **Cards.** A white card, black script wiping in from the left, about 2-3 s: "In today's video" once, then "N. Name" for each point. The numbers are on the card only.
4. **Credit.** The creator's handle in small script at the lower right of a held tutorial.
5. **Tips.** One short tip in small script beside the tall frame, between asterisks.
6. **Motion.**
   - Panels and photos grow in, one at a time, on the word.
   - Slow push-in on clips.
   - Soft fades between layouts.
   - Hard cuts are rare inside a held tutorial.
   - 90 cuts in 494 s: about one cut every 5.5 s overall, but long holds of 30-40 s on tutorials.
7. **Logo.** Small, top-left, on every non-white screen. Hidden on white screens.
8. **Title.** "Episode N:" in serif, then the title, in white, over a full-screen clip after "In today's video".
9. **Outro.** A calm full-screen bedroom or window clip under a soft haze, then the white end card.
10. **Audio.**
    - Integrated loudness -19.3 LUFS.
    - Soft piano runs continuously under the voice (only 6 dips below -35 dB in 8 minutes).
    - The last 8 s average -28.1 dB (the music fades out under the end card).
    - **No sound effects.**

## 3. Differences we keep on purpose (and why)

- **Logo.** The reference shows a "CA" (Classy Academy) logo. This repo has only The Classy Elegance "CE" logo assets, so the edit uses those. Swapping in a CA logo is one file change (`assets/logo_ce.png`), but we did not make or fake a logo.
- **Stylist-guide plug.** The approved script keeps it (line 21 and the close), so the channel's haze card for it stays. The reference video has none.
- **Voice and music.** The pipeline's own are kept: Kokoro af_heart at 0.80; Mixkit "Classical" piano about 12 dB under the voice; master at -14 LUFS for YouTube.

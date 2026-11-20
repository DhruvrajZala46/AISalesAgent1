# 001 - Why Does My Ear Feel Blocked After Cotton Buds?  (the quality bar)

- Length 57.6 s, 720×1280, 30 fps, −13.6 LUFS. Delivered 20 Nov 2026. The user's verdict: "mind blowing".
- Medical source: AAO-HNS Clinical Practice Guideline, *Cerumen Impaction* (2017 update). Ear canals are self-cleaning,
  cotton-tipped swabs push wax deeper, and impaction causes fullness and muffled hearing. This came from model knowledge and was not
  re-checked against the PDF during production.
- Post title: *Why Does My Ear Feel Blocked After Cotton Buds?*
- Caption: *Your ears clean themselves 👂 Cotton buds push earwax deeper, sometimes right against your eardrum. #earwax #health #bodyfacts #doctor #animation*

## Lines (file = `raw/NN_role.mp3` → `proc/NN_role.wav`)

| # | Role / voice | Text sent to ElevenLabs (eleven_v3) | Flow / session / generation |
|---|---|---|---|
| a01 | wax / Liam | `[surprised] Huh?! What's that fluffy thing doing in here?` | 6ngM3bL8AoY354Jm7238 / pQPQ4nxc9iJLjdNLeKwr / c6JlVsuhGLfBUiwb9ckB |
| a02 | swab / My Stephanie | `[cheerful] Cleaning crew! This ear's getting scrubbed!` | 6ngM3bL8AoY354Jm7238 / Fy1XaE1LIM7PFf6lrgYH / eQNNglOqzM91rQAa1SPy |
| a03 | wax | `[panicking] Wait, wait! I was already leaving on my own!` | 6ngM3bL8AoY354Jm7238 / QXWaVHR39urBxqR8b1BJ / ymR6DxybczuJkqdSU3ww |
| a04 | swab | `[sarcastic] Sure you were. In you go!` | 6ngM3bL8AoY354Jm7238 / Po3KujNVqE9wxtAVF6Ed / FX1SeJ5TeiwwiU2zKHX7 |
| a05 | wax | `[shouting] Ow! Not deeper! The eardrum's back there!` | 6ngM3bL8AoY354Jm7238 / PfsR9atl3ff4VVKUeUAM / WmNZJ2Q3wBJzGcVo8Xz4 |
| a06 | swab | `[proud] There! Spotless!` | 6ngM3bL8AoY354Jm7238 / fl7LOgWchHMq8Pd712N3 / N8FtWhClLzOMe7EGsLmR |
| a07 | drum / Laura | `[annoyed] Hey! Who's leaning on me?! I can't vibrate!` | 6ngM3bL8AoY354Jm7238 / 6DmRptkUi6CVb48LgBn5 / 0QxQq8ij3DFrmRMNFzAQ |
| a08 | wax | `[defensive] Don't look at me! Fluffy did this!` | 6ngM3bL8AoY354Jm7238 / 9MzrMXH6NtOoP4YoroLk / iSfDfnBwl2e3XPCP7DwE |
| a09 | swab | `[confused] Huh? Why'd it get so quiet in here?` | N05WzVPEtEcdhtCz2rTc / GbKIHxdPR55G6f9Qd0ZG / 3lAYsHA7eumk24geOZQc |
| a10 | patient / Davis | `Doc, my ear feels blocked and everything sounds muffled. But I clean it with cotton buds every single day!` | N05WzVPEtEcdhtCz2rTc / VdWQ99d5MXiR1cdY3w9F / SaRQEzsZ2M8oy62FGw1b |
| a11 | doctor / Hope | `That's the problem. Your ears clean themselves. Earwax slowly moves out on its own. Cotton buds push it back in, and it gets packed deep, right next to your eardrum. That's called earwax impaction. Only clean the outer ear, and let a doctor remove a blockage.` | 6ngM3bL8AoY354Jm7238 / LfE7Kyvu4kd16SJX0HtX / UzfVFHuYStFMHQ85jur3 |
| a12 | swab | `[sulking] Fine... I'll just stay outside.` | 6ngM3bL8AoY354Jm7238 / iwAuvyIpWmDkRh0ZSXeq / ghsgEIzpJrO6uB4khFqn |

To re-download the audio, call ElevenLabs `creative_get_flow_run_status` with the flow id and session ids. It returns fresh
`content_url`s. Save each one as `raw/<#>_<role>.mp3`, using the a01…a12 names above.
(The a09 and a10 files were originally called `l7_swab` and `l8_patient`; the processing is the same.)

## Beat sheet (seconds, from `data.js` → `ev`)

0.0 the bud whooshes toward a big realistic ear · 0.45 a01 hook line · 0.98 zoom through the dark into the diagonal canal ·
1.2 EAR CANAL label, 1.65 EARWAX label · 3.4 scrubbing (sparkles, dust) · 6.2 the wax tries to leave and bumps into the bud; yellow arrow at "leaving" ·
10.9 "go!" anticipation, then shove (punch, splat, squish, camera punch, puff, ticks) · 13.8 EARDRUM label · 15.3 "There!" final shove (boing, dizzy birds,
red glow, vibration lines stop) · 17.9 eardrum close-up · 23.3 whip-pan to the bud on "Fluffy" · 24.8 pull-out, sound waves blocked by an ❌,
music muffled, sad trombone · 28.0 clinic (push-in on the patient) · 34.9 doctor: head shake, bubble replay 1 (wax moving out), bubble replay 2 (shove),
47.4 punch-in plus EARWAX IMPACTION label · 48.7 CLEAN THE OUTER EAR ONLY label · 51.8 patient nods · 52.7 stinger outside the ear · 55.8 FOLLOW card.

## Rebuild

```
bash ../../tools/fetch_assets.sh
bash ../../tools/process_voice.sh raw proc     # after re-downloading raw/*.mp3
python3 -I ../../tools/words.py proc words.json  # words.json is already committed; only needed for new audio
python3 build_audio.py
node ../../tools/render.js && bash ../../tools/mix.sh
```

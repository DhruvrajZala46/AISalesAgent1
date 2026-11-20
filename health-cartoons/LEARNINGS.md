# Learnings: every piece of user feedback on the health-cartoon videos (newest last)

| # | What we showed | User verdict | Lesson / check now in PLAYBOOK |
|---|---|---|---|
| 1 | Hindi animated health reel sample (code-drawn, Microsoft "Madhur" TTS, marimba music) | "Animation ok, voice not attractive; make everything EXACT same" | Measure the reference before building: it had **no music and no SFX**, voice only at −14 LUFS. Never add things the reference does not have. |
| 2 | Hindi v2 with ElevenLabs "JP" voice, iris transitions, voice only | (moved on to a new reference) | Pick voices by speaker-embedding similarity (WavLM) against the reference, not by ear. |
| 3 | First English video in the dr.healthcare1 format (thick-line cartoon, clouds, cookie-like wax) | "50-60%, looks like cheap AI" | Their art is anatomy-first, objects look real, thin lines, muted colours, soft shading. |
| 4 | v2 with an anatomical cross-section, realistic bud and wax, expressive eyes, new clinic | "Far better but 65-70%; doctor part feels cheap; not as fun" | Hook in 0.5 s; the subject fills the frame; a new framing per line; mouths need real visemes; doctor ≤ 18 s with replays and a punch-in; 18+ SFX; a stinger plus CTA. |
| 5 | **v3 = video 001** | **"Mind blowing. Keep this same quality in all next videos."** | This is the bar. Copy 001 and change only the topic parts. |
| 6 | Viral study of the reference channel (406 Shorts, top 10 transcribed) | (requested) | Topic families, hook flavours, clinic at ~70%, YouTube master at about −10 LUFS. Never copy scripts or identity: format only. |
| 7 | Video 002 preview (swallowed gum, first 35 s) | **"10%. Glitchy, weird visuals, hard to understand, basic, looks AI-made. Voices, sound, pace and story all bad."** | Measured in `research/VIRAL-STUDY.md` §11: open inside the body with the characters on screen; speaking characters fill 30-60% of the width and have arms; one locked wide shot per scene (no camera move per line); clean pink anatomy with recognisable objects; plain 3-7-word bro lines. Pick topics proven on BOTH same-format channels (§10). |
| 8 | Video 003 (food out the nose when you laugh): measured script, eleven_v4 voices picked by measurement, acting timeline, 6 frame-check passes | **Script: "now okay". After the video: "Save this standard. Every new video: same effort or MORE, in editing and scripting. Never forget it."** | PLAYBOOK §0 (the effort standard) is mandatory for every video, and 003's numbers are the floor. |
| 9 | Video 003 full render | **"I don't like it at all. Basic, cheap, looks AI-made, hard to understand. Visuals are the main thing. I want 99% the same as Dr. Healthcare: scripts, voice, hook, visuals."** Sent 50 of their transcripts. | Code-drawn art has hit its ceiling for this user; the effort process (PLAYBOOK §0) stays, but the art must come from an illustration source (image model via the full ElevenLabs connector, Gemini, or an illustrator). Their scripts are a pattern bank, never copied word for word. |
| 10 | 003 v3: same audio, visuals rebuilt with Meta Muse Image art (plates + sprites, AI-drawn mouths patched in for lip-sync, closer camera, ramen-wavy noodle) | **"GREAT, I LOVED IT, WOW."** | This is the new bar. Every next video: AI art pipeline of `videos/003-food-up-nose-v2/` + the PLAYBOOK section-0 process. |
| 11 | 004 "Why you can't eat before surgery" (stomach + burger + lungs, 32M-proven topic), same pipeline as 003 v3 | (waiting for the user's verdict) | Measured: 71.7 s, 2.73 words/s, final-mix whisper 98.1%, -11.1 LUFS, true peak -1.0 dB, frozen 0.3%, longest still 0.2 s. |
| 12 | 005 "Why eating without water makes you constipated": first remake under the proven-10M rule (27M reference, studied shot by shot; same beats, the same two silent gags, our art and words) | (waiting for the user's verdict) | Measured: 76.3 s, clinic 61%, final-mix whisper 96.6% (98% ignoring spellings like "Okaaay"), -11.1 LUFS, true peak -1.2 dB, frozen 0.4%, longest still 0.2 s. |

Other user preferences:
- Talks in Hinglish; answer in simple Hinglish with plain words, clear and direct.
- Wants honesty: never claim "99% same" when it is not. Give a measured comparison.
- Visuals: AI-illustrated plates and sprites (Meta Muse Image) animated by our engine. The code-drawn look was rejected (row 9); video models are not needed.
- The user wants a separate channel in this format, with a **female doctor** and a different, trustworthy colour theme.
- "Save everything": all code and docs live here in git. Media is never committed (repo rule); re-create it from the IDs and scripts.

Checks learned while building 004 (do them before the first full render):
- **Verify every SFX id by its Mixkit title and the AST tagger.** The old map was wrong for 12+ ids: 003 and the first 004 mix played a
  cartoon LAUGH on every label pop, a creepy creature CRY on the FOLLOW card and an explosion on scene changes. 004's audio was remixed
  with verified ids (PLAYBOOK section 3 table).
- **Look at every AI mouth pair side by side at sprite level** (base, `_c`, `_o`). In 004 three of them were wrong: the stomach's open
  mouth looked like lipstick lips, its "closed" edit had no mouth at all, the lungs' open mouth sat on the lobe's bottom edge and the strain
  pose had none. Fix: make the open mouth first with an exact place ("on the right lobe, just below its eye", "no lips"), then make the
  closed one as an edit OF that open one, so both sit on the same spot.
- **Food standing inside an organ must not cover the organ's mouth.** Measure the mouth box in world pixels against the food's top. Keep the
  food low, and draw a mouth-only layer (`mouth_overlay.py`) above it.
- **A sprite that turns upside down must turn round its centre**, not its feet, or it jumps by its own height when it lands.
- **Name a body part on screen when the script names it** (the "DOOR" ring at the food-pipe valve), and show it changing when it fails.
- **Even out line loudness before the mix** (`build_audio.py` pulls each line 80% of the way to -19 dB). 004's takes spanned 14 dB; the
  sleepy stomach line and the patient sat as loud as the music, and whisper on the final mix lost a whole line and heard "gag" as "gas"
  (92%). After levelling and moving two SFX off the key words: 98.1%.
- **Cut clinic thought-bubble replays on the doctor's own words** (relaxes the muscle -> the door; cough reflex -> the lungs straining;
  came back up -> floating; slipped into your lungs -> landing), not one long replay.

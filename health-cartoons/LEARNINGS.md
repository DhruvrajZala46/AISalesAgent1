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

Other user preferences:
- Talks in Hinglish; answer in simple Hinglish with plain words, clear and direct.
- Wants honesty: never claim "99% same" when it is not. Give a measured comparison.
- No AI image or video generation for now (the user chose code). Video models are not needed at all.
- The user wants a separate channel in this format, with a **female doctor** and a different, trustworthy colour theme.
- "Save everything": all code and docs live here in git. Media is never committed (repo rule); re-create it from the IDs and scripts.

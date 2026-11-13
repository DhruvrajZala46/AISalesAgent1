# Reel 5, Gujarati version (version 2, 89.9 s)

Same scenes, music and sound effects as `../reel5/` (Hindi). The changes are the voice and the on-screen text.
- `beats.txt`: the Gujarati script (spoken Gujarati, not word-for-word Hindi). `beats_tts.txt` spells RO, WHO,
  Enagic and Kangen the way the voice should say them.
- Voice: `python3 ../reel5/tts.py gu-IN-NiranjanNeural "+40%"`, then `assemble_voice.py` (shorter gaps, 1.1 s tail,
  so the video stays under WhatsApp's 90 s status limit).
- `make_gu.py`: writes the Gujarati `build.py` from `../reel5/build.py`. It swaps every headline, label, card and
  stamp for Gujarati, and maps each Hindi word anchor to the Gujarati word it lands on. The mesh in the glass
  scene is re-timed to "ગંદકી / કેલ્શિયમ / મેગ્નેશિયમ".
- Font: Anek Gujarati (same family as the Hindi Anek Devanagari), added to `../reel5/style.css` as a Gujarati
  unicode-range face.
- Credits: `../reel5/CREDITS.txt` (voice here: Microsoft Edge neural gu-IN-NiranjanNeural).

## ElevenLabs voice (the one to use)
The owner did not like the Microsoft Gujarati voice, so the final Gujarati video uses ElevenLabs:
- Voice: "Ritesh – Gujarati E-Learning Narrator" (library voice lqUar8eoQmBGnHALVUBD: warm, clear, trustworthy,
  native Gujarati pronunciation), model eleven_v4, one take of the whole script with emotion tags:
  `elevenlabs_script_tags.txt` ([warmly], [sighs], [curious], [softly], [dramatically], [serious], [confident],
  [disappointed], [frustrated], [sad], [pause], [hopeful], [impressed], [friendly]). It cost about 1,550 credits.
- Word timings: ElevenLabs Scribe on the same flow (0 credits), saved locally as `el/scribe_words.json`.
- `elevenlabs_align.py`: caps ordinary pauses (0.13 s inside a line, 0.24 s between lines) and keeps the dramatic
  ones ("છે…", "પણ… ખાલી", "વિચારો…", the beat before "પણ જાપાનમાં"). A light 1.05x tempo brings the voice to
  89.8 s, and it writes `beats.json` with every word's time, so the edit stays in sync.
- The audio stays out of git (ElevenLabs output in the scratchpad).

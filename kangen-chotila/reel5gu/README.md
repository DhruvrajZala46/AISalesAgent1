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

# tts_sent.py: narration, one wav per sentence (Kokoro af_heart at speed 0.85, the voice and pace of the test the owner heard),
# from the approved script (classy-academy-test/videos/look-older/script.md; headings are not read).
#   python3 tools/tts_sent.py -> tts/s001.wav ... + tts/sentences.json (i, line = paragraph number, text, said, dur)
import kokoro_onnx, soundfile as sf, os, json, re
L = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = '/root/.cache/hyperframes/tts/'
m = kokoro_onnx.Kokoro(C + 'models/kokoro-v1.0.onnx', C + 'voices/voices-v1.0.bin')
src = open('/home/user/AISalesAgent1/classy-academy-test/videos/look-older/script.md').read()
paras = [l.strip() for l in src.split('\n') if l.strip() and not l.startswith('#') and not l.startswith('*Ready')]
FIX = [(r'\bcolour', 'color'), (r'\bColour', 'Color')]
out = []; i = 0
for li, para in enumerate(paras, 1):
    for sent in [x for x in re.split(r'(?<=[.?!])\s+', para) if x]:
        i += 1; say = sent
        for a, b in FIX: say = re.sub(a, b, say)
        f = f'{L}/tts/s{i:03d}.wav'
        if not (os.path.exists(f) and os.path.getsize(f) > 1000):
            y, sr = m.create(say, voice='af_heart', speed=0.85, lang='en-us'); sf.write(f, y, sr)
        y, sr = sf.read(f)
        out.append(dict(i=i, line=li, text=sent, said=say, dur=round(len(y) / sr, 3)))
json.dump(out, open(f'{L}/tts/sentences.json', 'w'), indent=1)
w = sum(len(o['text'].split()) for o in out); d = sum(o['dur'] for o in out)
print('sentences', len(out), 'words', w, 'speech s', round(d, 1), 'wpm (speech only)', round(w / d * 60, 1))

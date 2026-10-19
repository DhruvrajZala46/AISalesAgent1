# Narration: one wav per sentence (Kokoro af_heart, the channel pipeline's voice), with pronunciation fixes.
#   python3 tts_sent.py <speed>   -> tts/s001.wav ... s111.wav + tts/sentences.json
import kokoro_onnx, soundfile as sf, os, json, sys, re
C = '/root/.cache/hyperframes/tts/'
m = kokoro_onnx.Kokoro(C + 'models/kokoro-v1.0.onnx', C + 'voices/voices-v1.0.bin')
speed = float(sys.argv[1]) if len(sys.argv) > 1 else 0.8
T = json.load(open('../hair/timed.json'))
FIX = [(r'\bCannes\b', 'Kann'), (r'\bcolour', 'color'), (r'\bcentimetre', 'centimeter'), (r'\bcoily\b', 'coyly'),
       (r'\bcoils\b', 'coyls'), (r'\blowlights\b', 'low-lights')]
out = []
for i, (line, s, e, text) in enumerate(T, 1):
    say = text
    for a, b in FIX: say = re.sub(a, b, say)
    f = f'tts/s{i:03d}.wav'
    if not (os.path.exists(f) and os.path.getsize(f) > 1000):
        y, sr = m.create(say, voice='af_heart', speed=speed, lang='en-us'); sf.write(f, y, sr)
    y, sr = sf.read(f)
    out.append(dict(i=i, line=line, text=text, said=say, dur=round(len(y) / sr, 3)))
    print(i, flush=True)
json.dump(out, open('tts/sentences.json', 'w'), indent=1)
w = sum(len(o['text'].split()) for o in out); d = sum(o['dur'] for o in out)
print('words', w, 'speech s', round(d, 1), 'wpm (speech only)', round(w / d * 60, 1))

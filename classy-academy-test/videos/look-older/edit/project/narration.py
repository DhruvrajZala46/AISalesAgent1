# narration.py - builds the narration track and the sentence clock.
#   python3 project/narration.py  -> audio/voice.wav (48 kHz mono) + project/clock.json
# Pauses as in the channel's voice track (My7: median pause 0.6 s): 0.32 s between sentences of one paragraph, 0.60 s between
# paragraphs, +0.5 s before a point card (the picture fades to white). The voice starts at 0.15 s (no music intro). After the
# last word 0.5 s of quiet, then the white end card with the logo and the piano swell, 7.5 s (My7: 8:42.8-8:50).
import json, os, numpy as np, soundfile as sf, subprocess
P = os.path.dirname(os.path.abspath(__file__)); W = os.path.dirname(P)
sent = json.load(open(f'{W}/tts/sentences.json'))
scenes = json.load(open(f'{P}/scenes.json'))
cards = {sc['s0'] for sc in scenes if sc['layout'] == 'CARD'}
SR = 24000; LEAD = 0.15; END_GAP = 0.5; END_CARD = 7.5; TAIL = END_GAP + END_CARD
t = LEAD; parts = [np.zeros(int(SR * LEAD))]; clock = []
for i, s in enumerate(sent):
    if i in cards:
        parts.append(np.zeros(int(SR * 0.5))); t += 0.5
    y, sr = sf.read(f"{W}/tts/s{i + 1:03d}.wav"); assert sr == SR
    if y.ndim > 1: y = y.mean(1)
    st = t; t += len(y) / SR; parts.append(y)
    clock.append(dict(i=i, line=s['line'], text=s['text'], start=round(st, 3), end=round(t, 3)))
    if i + 1 < len(sent):
        g = 0.60 if sent[i + 1]['line'] != s['line'] else 0.32
        parts.append(np.zeros(int(SR * g))); t += g
parts.append(np.zeros(int(SR * TAIL))); t += TAIL
v = np.concatenate(parts).astype(np.float32)
os.makedirs(f'{W}/audio', exist_ok=True)
sf.write(f'{W}/audio/voice24.wav', v, SR)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{W}/audio/voice24.wav', '-ar', '48000', '-af', 'aresample=resampler=soxr', f'{W}/audio/voice.wav'], check=True)
json.dump(dict(total=round(t, 3), lead=LEAD, tail=TAIL, end_card=round(clock[-1]['end'] + END_GAP, 3), sentences=clock), open(f'{P}/clock.json', 'w'), indent=1)
w = sum(len(c['text'].split()) for c in clock)
print('total', round(t, 1), 's =', f'{int(t // 60)}:{t % 60:04.1f}', '| words', w, '| overall wpm', round(w / (clock[-1]['end'] - LEAD) * 60, 1))

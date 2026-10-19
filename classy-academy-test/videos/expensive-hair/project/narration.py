# Builds the narration track and the sentence/scene clock.
#   python3 project/narration.py  -> audio/voice.wav (48 kHz mono) + project/clock.json
# Pauses: 0.32 s between sentences of one script line, 0.60 s between lines; a card or quote scene is held
# long enough to be read (card >= 4.6 s incl. the 0.4 s fade to white, quote >= 3.0 s, payoff >= 2.8 s).
# Start and end as measured on the channel's 30 uploads: the voice starts at 0.0-0.3 s (no music intro); after the last
# word 0.5 s of silence, then the white CA end card with the logo sting, about 11 s after the last word in all.
import json, os, numpy as np, soundfile as sf
P = os.path.dirname(os.path.abspath(__file__)); W = os.path.dirname(P)
sent = json.load(open(f'{W}/tts/sentences.json'))
scenes = json.load(open(f'{P}/scenes.json'))
first = {sc['s0']: sc for sc in scenes}; last = {sc['s1']: sc for sc in scenes}
SR = 24000; LEAD = 0.15; END_GAP = 0.5; END_CARD = 10.6; TAIL = END_GAP + END_CARD
t = LEAD; parts = [np.zeros(int(SR * LEAD))]; clock = []
for i, s in enumerate(sent):
    if i in first and first[i]['layout'] == 'CARD':           # breath + fade to white before a point card
        parts.append(np.zeros(int(SR * 0.5))); t += 0.5
    y, sr = sf.read(f"{W}/tts/s{i + 1:03d}.wav"); assert sr == SR
    if y.ndim > 1: y = y.mean(1)
    st = t; t += len(y) / SR; parts.append(y)
    clock.append(dict(i=i, line=s['line'], text=s['text'], start=round(st, 3), end=round(t, 3)))
    if i + 1 < len(sent):
        g = 0.60 if sent[i + 1]['line'] != s['line'] else 0.32
        if i in last:
            sc = last[i]; s0 = clock[sc['s0']]['start'] - (0.5 if sc['layout'] == 'CARD' else 0)
            need = {'CARD': 4.6, 'QUOTE': 3.0, 'WHITE': 2.8}.get(sc['layout'], 0)
            if sc['scene'] == 9: need = (t - s0) + 0.0           # 'In today's video' card + centre clip
            g = max(g, need - (t - s0))
        parts.append(np.zeros(int(SR * g))); t += g
parts.append(np.zeros(int(SR * TAIL))); t += TAIL
v = np.concatenate(parts).astype(np.float32)
import subprocess
os.makedirs(f'{W}/audio', exist_ok=True)
sf.write(f'{W}/audio/voice24.wav', v, SR)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{W}/audio/voice24.wav', '-ar', '48000', '-af', 'aresample=resampler=soxr', f'{W}/audio/voice.wav'], check=True)
json.dump(dict(total=round(t, 3), lead=LEAD, tail=TAIL, end_card=round(clock[-1]['end'] + END_GAP, 3), sentences=clock), open(f'{P}/clock.json', 'w'), indent=1)
w = sum(len(c['text'].split()) for c in clock)
print('total', round(t, 1), 's =', f'{int(t // 60)}:{t % 60:04.1f}', '| words', w, '| overall wpm', round(w / (clock[-1]['end'] - LEAD) * 60, 1))

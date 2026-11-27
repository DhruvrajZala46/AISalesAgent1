# assemble voice track with pauses -> voice.wav + beats.json (start/end per beat, seconds)
import soundfile as sf, numpy as np, json
SR=24000
keys=[l.split('|',1)[0] for l in open('beats.txt') if l.strip()]
texts={l.split('|',1)[0]:l.strip().split('|',1)[1] for l in open('beats.txt') if l.strip()}
def gap_before(k,prev):
    if k=='H1': return 2.2
    if k[1]=='1' and k[0] in 'ABCDEFG': return 1.25   # fade to white before number card
    if k=='Z1': return 1.0
    if k in ('G6',): return 0.6
    if prev and prev[0]!=k[0]: return 0.8
    return 0.5
def gap_after(k):
    if k[1]=='1' and k[0] in 'ABCDEFG': return 0.55   # let the number card breathe
    return 0.0
out=[]; beats=[]; t=0.0; prev=None
for k in keys:
    g=gap_before(k,prev); out.append(np.zeros(int(g*SR),np.float32)); t+=g
    a,sr=sf.read(f'tts/{k}.wav',dtype='float32'); assert sr==SR
    # trim leading/trailing silence
    nz=np.where(np.abs(a)>0.003)[0]; a=a[max(0,nz[0]-240):min(len(a),nz[-1]+1200)]
    beats.append({'k':k,'s':round(t,3),'e':round(t+len(a)/SR,3),'text':texts[k]}); out.append(a); t+=len(a)/SR
    ga=gap_after(k); out.append(np.zeros(int(ga*SR),np.float32)); t+=ga; prev=k
END_CARD=12.0
out.append(np.zeros(int((END_CARD+0.5)*SR),np.float32)); t+=END_CARD+0.5
v=np.concatenate(out); sf.write('voice.wav',v,SR)
json.dump({'beats':beats,'duration':round(t,3)},open('beats.json','w'),indent=1)
print(f'total {t:.2f}s = {int(t//60)}:{t%60:05.2f}; speech ends {beats[-1]["e"]:.1f}')

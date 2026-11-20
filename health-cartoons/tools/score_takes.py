# Score every take in takes/*.mp3 against lines.txt: whisper word error rate + pitch range (semitones, 5-95 pct) -> takes/scores.json
# Usage (from a video folder): python3 -I ../../tools/score_takes.py
import glob, json, re, subprocess, numpy as np, parselmouth
from faster_whisper import WhisperModel
L=[l.split('|',1) for l in open('lines.txt').read().strip().split('\n')]
norm=lambda t:re.sub(r"[^a-z0-9' ]"," ",t.lower().replace('-',' ')).split()
def wer(r,h):
    r,h=norm(r),norm(h); d=list(range(len(h)+1))
    for i in range(1,len(r)+1):
        p=d[:]; d[0]=i
        for j in range(1,len(h)+1): d[j]=min(p[j]+1,d[j-1]+1,p[j-1]+(r[i-1]!=h[j-1]))
    return d[len(h)]/max(1,len(r))
m=WhisperModel('small',device='cpu',compute_type='int8'); out={}
for f in sorted(glob.glob('takes/*.mp3')):
    n=int(f.split('/')[-1][:2]); ref=L[n-1][1]
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-f','s16le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
    txt=' '.join(s.text.strip() for s in m.transcribe(a,language='en',beam_size=5)[0])
    p=parselmouth.Sound(a.astype(np.float64),16000).to_pitch(pitch_floor=60,pitch_ceiling=800).selected_array['frequency']; p=p[p>0]
    rng=12*np.log2(np.percentile(p,95)/np.percentile(p,5)) if len(p)>10 else 0
    out[f]={'wer':round(wer(ref,txt),2),'range':round(float(rng),1),'dur':round(len(a)/16000,2),'txt':txt}
    print(f"{f:28s} wer {out[f]['wer']:.2f} range {out[f]['range']:5.1f} st  {txt}")
json.dump(out,open('takes/scores.json','w'),indent=1)

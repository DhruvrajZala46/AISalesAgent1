# 012: pick the best take per line (lowest WER, then widest pitch range), one fixed pitch shift per character,
# trim silence, and a per-character pace (the reference's banter is quick; Marshal's grumpy voice is slow by design).
import json, subprocess, math, numpy as np, parselmouth
S=json.load(open('takes/scores.json'))
L=[l.rstrip('\n').split('\t') for l in open('lines.tsv') if l.strip()]
SHIFT={'puff':0.0,'tongue':-1.0,'puff2':3.0,'palate':0.0,'partner':0.0,'patient':0.0,'doctor':0.0}   # semitones
TEMPO={'puff':1.12,'tongue':1.22,'puff2':1.14,'palate':1.12,'partner':1.06,'patient':1.04,'doctor':1.06}
FORCE={'17_doctor':'b','07_tongue':'a','08_palate':'b','11_palate':'b'}   # 17a: whisper heard "sleep acne"; the others keep each voice's pitch consistent
LINE_SHIFT={'03_puff':4.0}                  # both takes of 03 came out 6 st lower than the puff's other lines
def f0(path):
    p=parselmouth.Sound(path).to_pitch(pitch_floor=60,pitch_ceiling=900).selected_array['frequency']; p=p[p>0]
    return float(np.median(p)) if len(p) else None
subprocess.run(['mkdir','-p','proc']); rec={}
for n,role,start,txt in L:
    k=f'{n}_{role}'; a,b=S[f'takes/{k}a.mp3'],S[f'takes/{k}b.mp3']
    t=FORCE.get(k) or ('a' if (a['wer'],-a['range'])<=(b['wer'],-b['range']) else 'b')
    src=f'takes/{k}{t}.mp3'; st=SHIFT[role]+LINE_SHIFT.get(k,0); r=2**(st/12); tp=TEMPO[role]
    af=f"asetrate=44100*{r:.4f},aresample=44100,atempo={tp/r:.4f},silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.05,areverse"
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-af',af,'-ac','1','-ar','44100',f'proc/{k}.wav'])
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'proc/{k}.wav'],capture_output=True,text=True).stdout)
    rec[k]={'take':t,'f0':round(f0(src) or 0),'shift_st':st,'tempo':tp,'dur':round(dur,2)}
    print(k,t,'f0',rec[k]['f0'],'->',round((f0(src) or 0)*r),'dur %.2f'%dur)
json.dump(rec,open('voice_proc.json','w'),indent=1)
print('total speech %.1f s'%sum(v['dur'] for v in rec.values()))

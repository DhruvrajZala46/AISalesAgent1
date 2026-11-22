# 010: pick the best take per line (lowest WER, then widest pitch range), shift its pitch to the reference
# character's measured pitch, trim silence, and fit it into the reference's slot (start .. next line's start).
import json, subprocess, math, numpy as np, parselmouth
S=json.load(open('takes/scores.json'))
L=[l.rstrip('\n').split('\t') for l in open('lines.tsv') if l.strip()]
TARGET={'guard':200,'brain':239,'stomach':250,'pill':440,'pill2':185,'prost':213,'patient':105,'doctor':120}
MAXUP={'pill':6.0,'stomach':7.0}                      # do not push the kid voice further than +7 st (clarity)
REF_END=80.4
def f0(path):
    p=parselmouth.Sound(path).to_pitch(pitch_floor=60,pitch_ceiling=900).selected_array['frequency']; p=p[p>0]
    return float(np.median(p)) if len(p) else None
subprocess.run(['mkdir','-p','proc'])
rec={}
# one fixed shift per character: median f0 over all its picked takes
pick={}
for n,role,start,txt in L:
    k=f'{n}_{role}'; a,b=S[f'takes/{k}a.mp3'],S[f'takes/{k}b.mp3']; pick[k]='a' if (a['wer'],-a['range'])<=(b['wer'],-b['range']) else 'b'
ROLE_F0={}
for role in TARGET:
    fs=[f0(f'takes/{n}_{r}{pick[n+"_"+r]}.mp3') for n,r,_,_ in L if r==role]
    fs=[x for x in fs if x]; ROLE_F0[role]=float(np.median(fs)) if fs else None
print({r:round(v) for r,v in ROLE_F0.items() if v})
for i,(n,role,start,txt) in enumerate(L):
    k=f'{n}_{role}'; a,b=S[f'takes/{k}a.mp3'],S[f'takes/{k}b.mp3']
    t=pick[k]
    src=f'takes/{k}{t}.mp3'; tmp='/tmp/claude-0/-home-user-AISalesAgent1/8b1a9160-87c6-53bb-91bc-b868cec25e40/scratchpad/_v.wav'
    m=ROLE_F0[role]; st=12*math.log2(TARGET[role]/m); st=max(-5,min(MAXUP.get(role,8),st))
    r=2**(st/12)
    nxt=float(L[i+1][2]) if i+1<len(L) else REF_END
    slot=nxt-float(start)-0.06
    af=f"asetrate=44100*{r:.4f},aresample=44100,atempo={1/r:.4f},silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-42dB:start_silence=0.05,areverse"
    if role=='brain': af+=",highpass=f=380,lowpass=f=3400,volume=1.6"
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-af',af,'-ac','1','-ar','44100',tmp])
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',tmp],capture_output=True,text=True).stdout)
    tempo=max(1.0,min(1.12 if role in('doctor','patient') else 1.38,dur/slot*1.12))   # cartoon lines run a little fast, like the reference
    subprocess.run(['ffmpeg','-v','error','-y','-i',tmp,'-af',f'atempo={tempo:.4f}',f'proc/{k}.wav'])
    rec[k]={'take':t,'f0':round(m),'shift_st':round(st,2),'tempo':round(tempo,3),'dur':round(dur/tempo,2),'slot':round(slot,2),'start':float(start)}
    print(k,t,'role f0',round(m),'->',TARGET[role],'shift %+.1f st'%st,'tempo %.2f'%tempo,'dur %.2f / slot %.2f'%(dur/tempo,slot),'OVER' if dur/tempo>slot+.02 else '')
json.dump(rec,open('voice_proc.json','w'),indent=1)

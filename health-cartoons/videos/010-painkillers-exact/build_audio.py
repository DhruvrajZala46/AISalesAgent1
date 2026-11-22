# 010: exact copy of the reference's timeline. Each line starts at the reference second (lines.tsv), or just after the
# previous line when ours runs longer. Scene cuts and SFX sit on the reference's moments (shifted only if a line overruns).
import numpy as np, subprocess, json, re, difflib
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
L=[l.rstrip('\n').split('\t') for l in open('lines.tsv') if l.strip()]
A={}; START={}; lines=[]
for n,who,ref,txt in L:
    k=f'{n}_{who}'; a=load(f'proc/{k}.wav')
    act=a[np.abs(a)>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); A[k]=a*10**(float(np.clip((-19-db)*.8,-6,10))/20)   # level each line
REF={f'{n}_{w}':float(r) for n,w,r,t in L}; KEYS=[f'{n}_{w}' for n,w,_,_ in L]
dur=lambda k: len(A[k])/SR
lend=lambda k: START[k]+dur(k)
def block(keys,first_at):
    """place a scene's lines: first at first_at, the rest keep the reference spacing (never overlapping)"""
    off=first_at-REF[keys[0]]; prev=None
    for k in keys:
        t=REF[k]+off if prev is None else max(REF[k]+off, lend(prev)+(.12 if k.split('_')[1]==prev.split('_')[1] else .06))
        START[k]=round(t,3); prev=k
EV={'slash':.4,'spark':1.0,'hop':1.6,'guardIn':3.3,'phone':6.95}
block(KEYS[0:9],3.60)                                                   # A: the guard and the brain on the phone
EV['ring']=START['08_brain']-.05
EV['stomach']=max(21.0,lend('09_brain')+.1); EV['drop']=EV['stomach']+.8; EV['wake']=EV['stomach']+1.1
block(KEYS[9:19],EV['wake']+.05)                                        # B: stomach and pills (ref: cut 21.0, "Huh?" 22.18)
EV['poke']=START['11_pill']-.5
EV['stir']=lend('19_pill2')+.12; EV['vein']=EV['stir']+1.4; EV['tunnel']=EV['vein']+1.4
block(KEYS[19:23],EV['tunnel']+.24)                                     # D: the two tunnels
EV['hopR']=lend('23_pill2')+.12; EV['hopL']=EV['hopR']+.8; EV['cut2']=EV['hopR']+1.8; EV['arrive']=EV['cut2']+.4
block(KEYS[23:27],EV['cut2']+1.8)                                       # E: the boarded cut, the prostaglandin
EV['fight']=lend('27_pill2')+.22; EV['ko']=EV['fight']+1.0; EV['clinic']=EV['fight']+1.6
block(KEYS[27:36],EV['clinic']-.3)                                      # F: clinic (the patient starts 0.3 s before the cut, as in the reference)
END=round(max(80.4,lend('36_patient')+.5),3); N=int(END*SR); voice=np.zeros(N,np.float32)
norm=lambda w: re.sub(r"[^a-z']","",w.lower())
for n,who,ref,txt in L:
    k=f'{n}_{who}'; a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a[:max(0,N-i)]
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    sw=txt.split(); ww=W[k]; sm=difflib.SequenceMatcher(a=[norm(x) for x in sw],b=[norm(x[2]) for x in ww],autojunk=False)
    times=[None]*len(sw)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag in('equal','replace'):
            for q in range(i2-i1):
                if j2>j1: j=j1+min(q*(j2-j1)//max(1,i2-i1),j2-j1-1); times[i1+q]=(ww[j][0],ww[j][1])
    for q in range(len(sw)):
        if times[q] is None:
            prev=next((times[p] for p in range(q-1,-1,-1) if times[p]),None); nxt=next((times[p] for p in range(q+1,len(sw)) if times[p]),None)
            s=prev[1] if prev else (nxt[0]-.3 if nxt else 0); e=nxt[0] if nxt else s+.3; times[q]=(s,max(e,s+.12))
    words=[[round(t0+s,3),round(t0+e,3),re.sub(r"[^A-Za-z'\-]","",w).upper()] for w,(s,e) in zip(sw,times)]
    lines.append({'id':k,'who':who,'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':[w for w in words if w[2]]})
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.2*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# SFX on the reference's moments (Mixkit ids verified in PLAYBOOK section 3)
S('1492.mp3',EV['slash'],.35); S('2364.mp3',EV['spark'],.3); S('2813.mp3',EV['hop'],.25)       # the cut slices open, spark, a cell hops
S('1464.mp3',EV['guardIn'],.3)                                                                  # the guard steps in
S('1351.mp3',EV['ring'],.12,.8)                                                                 # phone voice
S('1492.mp3',EV['stomach']-.05,.25); S('2364.mp3',EV['drop']+.55,.35); S('2364.mp3',EV['drop']+.75,.3)   # pills plop into the juice
S('2364.mp3',EV['poke'],.3); S('2364.mp3',EV['poke']+.35,.25)
S('2357.mp3',EV['stir'],.5); S('1886.mp3',EV['stir']+.2,.35); S('732.mp3',EV['stir']+.3,.3,1.0)   # big plop + stir
S('1486.mp3',EV['vein'],.3,1.4); S('1492.mp3',EV['tunnel']-.05,.25)
S('2894.mp3',EV['hopR'],.35); S('2894.mp3',EV['hopL'],.35); S('2357.mp3',EV['cut2'],.3)           # boings into the tunnels
S('2813.mp3',EV['arrive'],.25)
S('2149.mp3',EV['fight'],.45); S('2151.mp3',EV['fight']+.25,.45); S('2182.mp3',EV['fight']+.5,.4); S('2149.mp3',EV['fight']+.75,.45)  # slaps, whacks
S('2894.mp3',EV['ko'],.4); S('473.mp3',EV['ko']+.15,.2)                                         # knocked out
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END); print({k:round(v,2) for k,v in EV.items()})
print(' '.join(f"{k[:2]}:{START[k]:.2f}/{REF[k]:.2f}" for k in KEYS))

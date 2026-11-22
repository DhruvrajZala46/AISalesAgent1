# 012: the reference's beat order and spacing (lines.tsv holds its line starts). Our lines run longer, so each line starts at
# the reference second or right after the previous line. Scene cuts and SFX sit on the story moments.
import numpy as np, subprocess, json, re, difflib
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
L=[l.rstrip('\n').split('\t') for l in open('lines.tsv') if l.strip()]
clean=lambda t: re.sub(r'\[[^\]]*\]\s*','',t).replace('IS','is')
A={}; START={}; lines=[]
for n,who,ref,txt in L:
    k=f'{n}_{who}'; a=load(f'proc/{k}.wav')
    act=a[np.abs(a)>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); A[k]=a*10**(float(np.clip((-19-db)*.8,-6,10))/20)
REF={f'{n}_{w}':float(r) for n,w,r,t in L}; KEYS=[f'{n}_{w}' for n,w,_,_ in L]
dur=lambda k: len(A[k])/SR
lend=lambda k: START[k]+dur(k)
def block(keys,first_at):
    off=first_at-REF[keys[0]]; prev=None
    for k in keys:
        t=REF[k]+off if prev is None else max(REF[k]+off, lend(prev)+(.14 if k.split('_')[1]==prev.split('_')[1] else .07))
        START[k]=round(t,3); prev=k
EV={'zoomOut':1.3,'puffIn':1.7}
block(KEYS[0:4],2.45)                                     # air puff 1 vs the tongue (ref: first line 2.64)
EV['puff2In']=lend('04_tongue')+.1
block(KEYS[4:7],EV['puff2In']+.55)                        # puff 2 arrives from the nose (ref 17.9)
EV['palWake']=lend('07_tongue')+.1
block(KEYS[7:10],EV['palWake']+.35)                       # the soft palate wakes up (ref 26.5)
EV['squeeze']=lend('10_tongue')+.12; EV['vib']=EV['squeeze']+.45
block(KEYS[10:12],EV['vib']+.35)                          # the air forces through: vibration = the snore (ref 36.3-45)
EV['bed']=lend('12_tongue')+.3; EV['slap']=EV['bed']+1.75
block(KEYS[12:13],EV['slap']+.55)                         # bedroom: the snorer gets slapped (ref 45-51)
EV['clinic']=lend('13_partner')+.35
block(KEYS[13:17],EV['clinic']+.35)                       # Dr. Mira (our addition)
END=round(lend('17_doctor')+.7,3); N=int(END*SR); voice=np.zeros(N,np.float32)
norm=lambda w: re.sub(r"[^a-z']","",w.lower())
for n,who,ref,txt in L:
    k=f'{n}_{who}'; a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a[:max(0,N-i)]
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    sw=clean(txt).split(); ww=W[k]; sm=difflib.SequenceMatcher(a=[norm(x) for x in sw],b=[norm(x[2]) for x in ww],autojunk=False)
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
def S(f,t,g,dur=None,start=0.0):
    a=load(f if '/' in f else '../../assets/sfx/'+f); a=a[int(start*SR):]
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.15*SR)); a[-fl:]*=np.linspace(1,0,fl)
    pk=np.abs(a).max() or 1; a=a/pk*g
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
S('sfxgen/sfx_snoreb.mp3',.15,.28,.8); S('sfxgen/sfx_snoreb.mp3',1.05,.22,.8)     # soft snoring while the tongue sleeps (close-up)
S('1486.mp3',EV['puffIn'],.22,1.2)                                                 # the air puff drifts in
S('2364.mp3',START['01_puff']-.15,.25)                                             # it bumps the tongue
S('1486.mp3',EV['puff2In'],.22,1.2); S('2364.mp3',EV['puff2In']+.45,.22)           # puff 2 squeezes down from the nose
S('2357.mp3',EV['palWake'],.3)                                                     # the soft palate's eyes pop open
S('1492.mp3',EV['squeeze'],.35)                                                    # the puffs rush the gap
for j,t in enumerate(np.arange(EV['vib'],EV['bed']-.2,2.9)):                       # the vibration = the snore, under the lines
    S('sfxgen/sfx_snorea.mp3',t,.62 if j==0 else .34,2.75)
S('sfxgen/sfx_snorea.mp3',EV['bed']+.05,.95,2.75)                                  # bedroom: the big snore
S('1464.mp3',EV['slap']-.25,.3)                                                    # the arm swings in
S('sfxgen/sfx_slapb.mp3',EV['slap'],.95,.35); S('2920.mp3',EV['slap'],.45,.4)      # SLAP
S('2894.mp3',EV['slap']+.18,.22)                                                   # eyes snap open
S('1492.mp3',EV['clinic']-.05,.25)                                                 # to the clinic
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:round(v,2) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

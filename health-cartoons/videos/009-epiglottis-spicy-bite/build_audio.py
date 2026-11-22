# 009: voice/sfx/music + data.js. Timeline copies the reference (23.7 s) beat for beat; captions use the exact script words.
import numpy as np, subprocess, json, re, difflib
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=[l.split()[0] for l in open('takes_manifest.tsv')]
SCRIPT=[l.rstrip('\n').split('|',1)[1] for l in open('lines.txt') if l.strip()]
GAP={'01_trachea':1.0,      # food drops down past them first
     '02_epiglottis':.15,
     '03_trachea':.55,      # another piece drops
     '04_epiglottis':.12,
     '05_epiglottis':1.0,   # SILENT: the epiglottis flips shut, a spicy crumb falls, the trachea grabs it and eats it
     '06_trachea':.35,
     '07_epiglottis':.25,
     '08_man':.48}          # cut to the man at the dinner table (his cough starts at ~20.9 s, like the reference)
A={k:load(f'proc/{k}.wav') for k in ORDER}
for k in ORDER:
    act=A[k][np.abs(A[k])>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); g=float(np.clip((-19-db)*.8,-6,10)); A[k]=A[k]*10**(g/20)
t=0; START={}
for k in ORDER: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+.35,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
norm=lambda w: re.sub(r"[^a-z']","",w.lower())
for k,txt in zip(ORDER,SCRIPT):
    a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    # captions: the exact script words, timed by aligning them to whisper's words
    sw=[w for w in txt.split()]; ww=W[k]; sm=difflib.SequenceMatcher(a=[norm(x) for x in sw],b=[norm(x[2]) for x in ww],autojunk=False)
    times=[None]*len(sw)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag in('equal','replace'):
            for q in range(i2-i1):
                j=j1+min(q*(j2-j1)//max(1,i2-i1),j2-j1-1) if j2>j1 else None
                if j is not None: times[i1+q]=(ww[j][0],ww[j][1])
    for q in range(len(sw)):          # interpolate any word whisper did not hear
        if times[q] is None:
            prev=next((times[p] for p in range(q-1,-1,-1) if times[p]),None); nxt=next((times[p] for p in range(q+1,len(sw)) if times[p]),None)
            s=prev[1] if prev else (nxt[0]-.3 if nxt else 0); e=nxt[0] if nxt else s+.3; times[q]=(s,max(e,s+.12))
    words=[[round(t0+s,3),round(t0+e,3),re.sub(r"[^A-Za-z'\-]","",w).upper()] for w,(s,e) in zip(sw,times)]
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':[w for w in words if w[2]]})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
L3=lend('04_epiglottis')+.32
EV={'land1':.75,'land2':7.8,'land3':L3,'close':L3,'grab':L3+.22,'eat':14.55,
    'spicy':wt('06_trachea','SPICY'),'fire':wt('06_trachea','FIRE'),'man':START['08_man']-.02,'end':END}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.2*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
for L,g in [(EV['land1'],.3),(EV['land2'],.3),(EV['land3'],.5)]:
    S('1464.mp3',L-.95,.18); S('2357.mp3',L-.05,g)                                         # a chunk drops; plop as the flap shuts (every time)
S('2894.mp3',EV['fire']-.3,.45)                                                            # boing as the eyes turn red (reference ~16.2 s)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(.8*SR); mus[-fl:]*=np.linspace(1,0,fl)
# duck the music 6 dB under speech (009 lesson: the bed masked "chest" and "blocking")
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); act=np.clip(act*4,0,1)
mus*=10**(-6*act/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END); print({k:round(v,2) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})
for l in lines: print(l['id'],' '.join(w[2] for w in l['words']))

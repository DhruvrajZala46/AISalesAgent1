# 019: our own timeline. Lines run one after another; the story events (the cell drops in, the leg starts bouncing,
# "Going up!", the gate shuts, the shout, the leg stops) are placed around them. SFX sit on those events.
import numpy as np, subprocess, json, re, difflib
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
L=[l.rstrip('\n').split('\t') for l in open('lines.tsv') if l.strip()]
clean=lambda t: re.sub(r'\[[^\]]*\]\s*','',t)
A={}; START={}; lines=[]
for n,who,txt in L:
    k=f'{n}_{who}'; a=load(f'proc/{k}.wav')
    act=a[np.abs(a)>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); A[k]=a*10**(float(np.clip((-19-db)*.8,-6,10))/20)
K=[f'{n}_{w}' for n,w,_ in L]
dur=lambda k: len(A[k])/SR
lend=lambda k: START[k]+dur(k)
def seq(keys,t,gap=.16):
    for k in keys: START[k]=round(t,3); t=lend(k)+gap
    return t-gap
EV={}
t=seq(K[0:1],.3)                                    # 01: the adenoid lounges at the back of the nose
EV['airin']=t-.5; t=seq(K[1:5],EV['airin']+1.1,.2)  # two air bubbles come in through the nose and stop; 02-05
EV['detour']=t+.2                                   # they go back out; the mouth opens; they go in through the mouth
EV['later']=EV['detour']+2.5; EV['work']=EV['later']+1.1
t=seq(K[5:10],EV['work']+.5,.22)                    # the roof of the mouth and the tongue, worn out; 06-10
EV['make']=t+.2                                     # the "makeover": the roof is pulled up, the jaw drops
EV['mirror']=EV['make']+1.9; t=seq(K[10:11],EV['mirror']+.45)   # 11
EV['doc']=t+.3; t=seq(K[11:12],EV['doc']+.35)       # 12
END=round(t+0.6,3); N=int(END*SR); voice=np.zeros(N,np.float32)
norm=lambda w: re.sub(r"[^a-z']","",w.lower())
for n,who,txt in L:
    k=f'{n}_{who}'; a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a[:max(0,N-i)]
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    sw=clean(txt).replace('Woo-hoo','Woo-hoo').split(); ww=W[k]; sm=difflib.SequenceMatcher(a=[norm(x) for x in sw],b=[norm(x[2]) for x in ww],autojunk=False)
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
LW={l['id']:l['words'] for l in lines}
def wt(k,w,n=0): return [x[0] for x in LW[k] if x[2]==w][n]
EV['i0']=wt('12_doctor','LONG')-.25; EV['i1']=wt('12_doctor','NARROW')-.25; EV['i2']=wt('12_doctor','CROWDED')-.2; EV['i3']=wt('12_doctor','BLOCKED')-.5
EV={k:round(float(v),3) for k,v in EV.items()}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None,start=0.0):
    a=load(f if '/' in f else '../../assets/sfx/'+f); a=a[int(start*SR):]
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.15*SR)); a[-fl:]*=np.linspace(1,0,fl)
    pk=np.abs(a).max() or 1; a=a/pk*g
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
def tick(t,g,f0=900):                               # a small metal click
    n=int(.07*SR); x=np.arange(n)/SR
    a=(np.sin(2*np.pi*f0*x)*np.exp(-x*70)+.5*np.sin(2*np.pi*f0*2.4*x)*np.exp(-x*110)).astype(np.float32)*g
    i=int(t*SR); m=min(n,N-i); sfx[i:i+m]+=a[:m]
def thud(t,g):                                      # a soft thud (steps, knocks, the barbell)
    n=int(.11*SR); x=np.arange(n)/SR
    a=(np.sin(2*np.pi*(150*x-260*x*x))*np.exp(-x*38)+.25*np.random.RandomState(int(t*1000)).randn(n)*np.exp(-x*220)).astype(np.float32)*g
    i=int(t*SR); m=min(n,N-i); sfx[i:i+m]+=a[:m]
S('1492.mp3',EV['airin'],.2,.5); S('2357.mp3',EV['airin']+.9,.18)                 # whoosh in, bump
S('1492.mp3',EV['detour'],.2,.5); S('1492.mp3',EV['detour']+1.0,.22,.6); S('2828.mp3',EV['detour']+1.5,.16,.8)   # out, the mouth opens, in and down
S('sfxgen/sfx_dingb.mp3',EV['later']+.05,.3,.9)
S('1884.mp3',EV['make'],.22,.9); tick(EV['make']+.5,.4,700); tick(EV['make']+1.0,.4,600); S('473.mp3',EV['make']+.9,.14,1.2)   # ropes creak
S('1492.mp3',EV['mirror']-.05,.22); S('2357.mp3',EV['doc'],.2)
for k in ('i0','i1','i2','i3'): S('2357.mp3',EV[k],.16)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
pass
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:(round(v,2) if not isinstance(v,list) else len(v)) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

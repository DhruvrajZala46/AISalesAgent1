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
EV['drop']=.05; t=seq(K[0:2],.9,.3)                 # two pills drop into the stomach; 01, 02
EV['brain']=t+.2; t=seq(K[2:6],EV['brain']+.4,.22)  # the brain pops up in a bubble; 03-06
EV['melt']=t+.2; EV['amyg']=EV['melt']+1.6          # the pill dissolves and heads for the brain
t=seq(K[6:7],EV['amyg']+.6)                         # the worry centre: the cop and three burning worry blobs; 07
EV['flare']=t+.15; t=seq(K[7:8],EV['flare']+1.0)    # they flare up again; 08
EV['blast']=t+.2; t=seq(K[8:9],EV['blast']+1.5)     # a blast of smoke; the cop is left with a black eye; 09
EV['pillin']=t+.3; t=seq(K[9:13],EV['pillin']+.6,.22)   # the sleeping pill walks in; 10-13
EV['calm']=t+.25; t=seq(K[13:14],EV['calm'])        # 14
EV['home']=t+.5; t=seq(K[14:15],EV['home']+.4)      # the bedroom; 15
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
EV['q1']=wt('14_officer','QUIET')-.05; EV['q2']=wt('14_officer','SETTLE')-.05; EV['q3']=wt('14_officer','YEP')-.05
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
S('1492.mp3',EV['drop'],.2,.5); S('2357.mp3',EV['drop']+.55,.18); S('2357.mp3',EV['drop']+.75,.16)   # pills fall and plop
S('2357.mp3',EV['brain'],.2)                                                                       # the bubble pops in
S('2828.mp3',EV['melt'],.18,1.2); S('1492.mp3',EV['melt']+1.0,.2,.6)                               # fizz, whoosh up
S('1492.mp3',EV['amyg']-.05,.22); S('2182.mp3',EV['flare'],.22,.4); S('2182.mp3',EV['flare']+.25,.2,.4)   # flames flare
S('2182.mp3',EV['blast'],.3,.5); thud(EV['blast']+.1,.6); thud(EV['blast']+.35,.5); thud(EV['blast']+.6,.5)   # the brawl
S('2357.mp3',EV['pillin'],.2)
for k in ('q1','q2','q3'): S('2364.mp3',EV[k],.16)                                                   # flames go out
S('sfxgen/sfx_dingb.mp3',EV['q3']+.3,.24,.9); S('1492.mp3',EV['home']-.05,.22)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
pass
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:(round(v,2) if not isinstance(v,list) else len(v)) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

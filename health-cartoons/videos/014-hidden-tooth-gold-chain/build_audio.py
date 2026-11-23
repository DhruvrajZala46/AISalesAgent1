# 014: our own timeline. Lines run one after another; the story events (the cell drops in, the leg starts bouncing,
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
t=seq(K[0:1],0.0)                                   # 01: on the first frame, while the scalpel is cutting
EV['open']=t+.05; t=seq(K[1:2],t+.3)                # the flap opens; 02
EV['canCam']=t+.05; t=seq(K[2:3],t+.25)             # 03: the sleepy canine
t=seq(K[3:4],t+.2)                                  # 04
EV['chain']=t+.75; t=seq(K[4:5],EV['chain']+.15)    # the button and chain go on; 05
EV['tug']=t+.15; t=seq(K[5:6],EV['tug']+.3)         # the first pulls; 06
t=seq(K[6:7],t+.18); t=seq(K[7:8],t+.18)            # 07, 08
EV['seat']=t+.1; t=seq(K[8:9],t+.18)                # 09: the saved seat
EV['doc']=t+.15; t=seq(K[9:13],t+.3,.2)             # 10-13: the doctor, in a bubble
EV['tl0']=START['13_doctor']-.1; EV['tl1']=t+.3     # twelve months go by
t=seq(K[13:14],EV['tl1']+.15)                       # 14: Made it!
END=round(t+0.8,3); N=int(END*SR); voice=np.zeros(N,np.float32)
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
EV['lbCan']=wt('10_doctor','IMPACTED')-.05; EV['lbBtn']=wt('11_doctor','BUTTON')-.05; EV['lbChain']=wt('11_doctor','CHAIN')-.05; EV['lbBr']=wt('12_doctor','BRACES')-.05
EV={k:round(float(v),3) for k,v in EV.items()}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None,start=0.0):
    a=load(f if '/' in f else '../../assets/sfx/'+f); a=a[int(start*SR):]
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.15*SR)); a[-fl:]*=np.linspace(1,0,fl)
    pk=np.abs(a).max() or 1; a=a/pk*g
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
def tick(t,g,f0=900):                               # a small metal click (chain links, month ticks)
    n=int(.07*SR); x=np.arange(n)/SR
    a=(np.sin(2*np.pi*f0*x)*np.exp(-x*70)+.5*np.sin(2*np.pi*f0*2.4*x)*np.exp(-x*110)).astype(np.float32)*g
    i=int(t*SR); m=min(n,N-i); sfx[i:i+m]+=a[:m]
S('1492.mp3',0.05,.2,.6); S('1492.mp3',0.9,.16,.6)                           # the scalpel
S('2364.mp3',EV['open'],.3); S('2357.mp3',EV['open']+.12,.2)                 # the gum flap opens
S('2182.mp3',EV['chain']-.05,.26,.35)                                        # the button goes on
for j in range(6): tick(EV['chain']+.08+j*.07,.2,1100+j*60)                  # the chain drops
for j in range(9):
    tt=EV['tug']+j*.55
    if tt<EV['seat']-.2: S('2358.mp3',tt,.14,.3); tick(tt+.05,.12,700)        # tug, tug
S('2357.mp3',EV['seat']+.5,.2)                                               # the RESERVED sign
S('2357.mp3',EV['doc'],.22)
for k in ('lbCan','lbBtn','lbChain','lbBr'): S('2357.mp3',EV[k],.15)
for m_ in range(12): tick(EV['tl0']+.25+(EV['tl1']-EV['tl0']-.3)*m_/11,.2,900+m_*45)   # the months tick by
S('sfxgen/sfx_dingb.mp3',EV['tl1']-.05,.4,.9); S('2256.mp3',EV['tl1']+.05,.28,1.2)   # it clicks into its seat
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
pass
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:(round(v,2) if not isinstance(v,list) else len(v)) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

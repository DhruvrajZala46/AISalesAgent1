# 024: our own timeline. Lines run one after another; the story events (the cell drops in, the leg starts bouncing,
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
EV['drop']=.05; t=seq(K[0:3],.55,.2)                 # the pill shoots down and sticks to the dry wall; 01-03
t=seq(K[3:4],t+.2)                                    # 04: the pipe shouts up to the brain
EV['bub']=t+.1; t=seq(K[4:5],EV['bub']+.45)          # the brain pops up in a thought bubble, in bed; 05
EV['lie']=t+.15; t=seq(K[5:6],EV['lie']+.35)         # the brain lies down; 06
EV['fizz']=t+.2; t=seq(K[6:7],EV['fizz']+.5)         # the pill starts to melt; 07
EV['burn']=t+.15; t=seq(K[7:9],EV['burn']+.55,.22)   # the wall burns red; 08, 09
EV['card']=t+.45; EV['clinic']=EV['card']+1.1        # "NEXT MORNING" card, then the clinic
t=seq(K[9:12],EV['clinic']+.45,.22)                  # 10-12
EV['bub2']=t+.2; t=seq(K[12:13],EV['bub2']+.3)       # the doctor's thought bubble: the stuck pill and the sore; 13
t=seq(K[13:15],t+.25,.3)                              # 14 (the water slide), 15
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
EV['water']=wt('14_doctor','WATER')-.05; EV['thirty']=wt('14_doctor','THIRTY')-.05; EV['slide']=wt('15_patient','SLIDE')
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
# the decoded sound vocabulary (research/STYLE-DECODE.md 7): a swoosh and a boing as the pill lands, a pop for each thought bubble,
# fizz while it melts, a sizzle while it burns, a whoosh into the time card; the clinic is almost dry (one pour, one ding).
S('1464.mp3',EV['drop'],.3,.3)                                                     # swoosh: the pill shoots down
S('2894.mp3',EV['drop']+.3,.55,.5)                                                 # boing: it sticks to the wall
S('2358.mp3',EV['bub'],.35)                                                        # pop: the brain's bubble
S('1486.mp3',EV['lie'],.22,.6)                                                     # soft whoosh: the brain lies down
S('732.mp3',EV['fizz'],.28,2.2)                                                    # fizz: the pill melts
S('123.mp3',EV['burn'],.3,2.6,start=.3)                                            # sizzle: the wall burns
S('1492.mp3',EV['card']-.1,.3,.8)                                                  # whoosh into "NEXT MORNING"
S('2358.mp3',EV['bub2'],.28)                                                       # pop: the doctor's bubble
S('2833.mp3',EV['water'],.18,1.2)                                                  # pour: the glass of water
S('2256.mp3',EV['slide'],.28)                                                      # ding: "the pill's slide"
brawl=np.zeros(N,np.float32)
# music bed: mixkit-9 is 3.8 dB quieter than 508, so -4 dB here lands it ~17 dB under the voice (references 10-22 dB)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; mus*=10**(-4/20); fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl); fi=int(1.6*SR); mus[:fi]*=np.linspace(0,1,fi)**2   # soft start, as in the top videos
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus),]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
pass
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:(round(v,2) if not isinstance(v,list) else len(v)) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

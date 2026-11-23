# 013: our own timeline. Lines run one after another; the story events (the cell drops in, the leg starts bouncing,
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
EV={'drop':.2,'land':.48,'zoomOut':2.55}
t=seq(K[0:3],.6)                                   # 01-03: the cells, stuck at the ankle
EV['calfCam']=t-.15; t=seq(K[3:4],t+.22)            # 04: the calf
EV['gateCam']=t+.02; t=seq(K[4:5],t+.22)            # 05: the gate
EV['bounce']=t+.3                                   # the leg starts to bounce
t=seq(K[5:8],EV['bounce']+.75,.14)                  # 06-08
EV['up']=START['08_calf']+ (W['08_calf'][1][0] if len(W['08_calf'])>1 else .6)   # "Going up!"
t=seq(K[8:9],lend('08_calf')+.05)                   # 09: Woo-hoo!
EV['shut']=t+.18; t=seq(K[9:10],EV['shut']+.12)     # 10: the gate snaps shut
EV['flex']=t+.2; t=seq(K[10:11],t+.3)               # 11: second heart
EV['shout']=t+.35; t=seq(K[11:12],EV['shout'])      # 12: the partner
EV['stop']=t+.12                                    # the leg stops
t=seq(K[12:13],EV['stop']+.45)                      # 13
EV['clinic']=t+.4
t=seq(K[13:18],EV['clinic']+.35,.2)
END=round(t+.7,3); N=int(END*SR); voice=np.zeros(N,np.float32)
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
EV['two']=wt('02_cell2','FOR')-.1; EV['second']=wt('11_calf','SECOND')-.05
EV['rp0']=wt('15_doctor','EACH')-.06; EV['rpHeart']=wt('15_doctor','BACK')-.05; EV['rpCut']=START['16_doctor']-.08   # the doctor's words over the leg
EV['rpStop']=wt('16_doctor','KEEP')-.2; EV['rp1']=START['17_doctor']-.08
EV['card0']=wt('17_doctor','PEOPLE')-.1; EV['arrDown']=wt('17_doctor','DROPPED'); EV['arrUp']=wt('17_doctor','ROSE'); EV['card1']=START['18_doctor']-.1
EV['getUp']=wt('18_doctor','GET'); EV['walk']=wt('18_doctor','WALK')
EV={k:round(float(v),3) for k,v in EV.items()}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None,start=0.0):
    a=load(f if '/' in f else '../../assets/sfx/'+f); a=a[int(start*SR):]
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.15*SR)); a[-fl:]*=np.linspace(1,0,fl)
    pk=np.abs(a).max() or 1; a=a/pk*g
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
def tap(t,g):                                       # a soft heel tap on the floor (synthesised: a low thud + a tiny click)
    n=int(.11*SR); x=np.arange(n)/SR
    a=(np.sin(2*np.pi*(150*x-260*x*x))*np.exp(-x*38)+.25*np.random.RandomState(int(t*1000)).randn(n)*np.exp(-x*220)).astype(np.float32)*g
    i=int(t*SR); m=min(n,N-i); sfx[i:i+m]+=a[:m]
S('2364.mp3',EV['land'],.32)                                              # the second cell plops onto the pile
S('2364.mp3',START['01_cell']+.55,.16); S('2364.mp3',START['01_cell']+.85,.16)   # jabbing the call button
S('1486.mp3',EV['zoomOut'],.14,1.0)
S('2357.mp3',EV['calfCam']+.25,.2); S('2357.mp3',EV['gateCam']+.3,.2)      # labels pop
TAPS=[round(float(x),3) for x in np.arange(EV['bounce'],EV['stop']-.05,.25)]
for j,tt in enumerate(TAPS): tap(tt,.34 if j<6 else .22)                    # the bouncing leg: 4 taps a second
S('sfxgen/sfx_dingb.mp3',EV['up']-.02,.5,.9); S('1492.mp3',EV['up']+.05,.3)  # elevator ding, cells shoot up
S('2357.mp3',EV['up']+.45,.2); S('2357.mp3',EV['up']+.75,.18)
S('2182.mp3',EV['shut'],.3,.35)                                             # the gate claps shut
S('2256.mp3',START['11_calf']+ .9,.26,1.2)                                  # sparkle on "second heart"
S('sfxgen/down_fast.wav',EV['stop'],.34)                                    # the elevator powers down
S('sfxgen/whistle_down.wav',EV['stop']+.35,.2,1.1); S('2364.mp3',EV['stop']+1.3,.25)   # the cell slides back down
S('1492.mp3',EV['clinic']-.05,.25)
S('1492.mp3',EV['rp0']-.05,.15)                                             # back inside the leg while the doctor explains
for tt in TAPS:
    tq=EV['rpStop']+(tt-EV['stop'])
    if tq>=EV['rp0']: tap(tq,.11)
S('2182.mp3',EV['rpStop']+.02,.15,.35); S('2364.mp3',EV['rpStop']+1.3,.13)   # the valves catch the blood
S('1492.mp3',EV['rp1']-.05,.13)
S('2357.mp3',EV['card0'],.2)                                                # the study card pops up
for tt in np.arange(EV['card0']+.25,EV['card1']-.1,.25): tap(float(tt),.085)  # the fidgeting leg on the card
S('sfxgen/down_fast.wav',EV['arrDown'],.2,.6); S('sfxgen/sfx_dingb.mp3',EV['arrUp'],.3,.9)
S('2357.mp3',EV['getUp'],.16)
for j in range(4): tap(EV['walk']+.1+j*.28,.26)                             # he gets up and walks out
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.0*SR); mus[-fl:]*=np.linspace(1,0,fl)
act=np.convolve((np.abs(voice)>0.02).astype(np.float32),np.ones(int(.25*SR),np.float32)/int(.25*SR),'same'); mus*=10**(-5*np.clip(act*4,0,1)/20)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
EV['taps']=TAPS
data={'end':END,'lines':lines,'ev':EV,'start':START}
open('data.js','w').write('window.DATA='+json.dumps(data)+';'); json.dump(data,open('data.json','w'))
print('END',END); print({k:(round(v,2) if not isinstance(v,list) else len(v)) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

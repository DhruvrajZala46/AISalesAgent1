# 003: builds voice.wav, sfx.wav, music.wav and data.js (line timings, mouth envelopes, words, events) from proc/*.wav + words.json.
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=['01_noodle','02_palate','03_noodle','04_palate','05_noodle','06_palate','07_noodle','08_brain','09_palate','10_brain','11_laugh',
       '12_palate','13_noodle','14_noodle','15_palate','16_brain','17_patient','18_doctor','19_noodle']
# gap BEFORE each line (s). Tight like the reference (median 0.3 s); longer only where an action plays.
GAP={'01_noodle':.55,'02_palate':.16,'03_noodle':.14,'04_palate':.14,'05_noodle':.22,'06_palate':.14,'07_noodle':.45,'08_brain':1.05,
     '09_palate':.14,'10_brain':.12,'11_laugh':.05,'12_palate':0,'13_noodle':.05,'14_noodle':.75,'15_palate':.25,'16_brain':.12,
     '17_patient':.95,'18_doctor':.3,'19_noodle':1.0}
FIX={'DUCK':'DOC','PALLET':'PALATE','WHEE':'WHEEE','HAHAHAHA':'HA-HA-HA!'}
A={k:load(f'proc/{k}.wav') for k in ORDER}
# the laugh: keep only the "ha ha" part (cut before "Stop it, man") and let the palate shout over its tail
lw=W['11_laugh']; stop=[w for w in lw if w[2].lower().startswith('stop')][0][0]
A['11_laugh']=A['11_laugh'][:int((stop+.25)*SR)]; fade=int(.25*SR); A['11_laugh'][-fade:]*=np.linspace(1,0,fade)
W['11_laugh']=[w for w in lw if w[0]<stop]
t=0; START={}
for k in ORDER:
    t+=GAP[k]
    if k=='12_palate': t=START['11_laugh']+len(A['11_laugh'])/SR-.55   # shouts over the end of the laugh
    START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+2.2,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
for k in ORDER:
    a=A[k].copy(); t0=START[k]
    if k=='11_laugh': a=a*.85
    i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    words=[]
    for s,e,w in W[k]:
        u=re.sub(r"[^A-Za-z'\-]","",w).upper(); u=FIX.get(u,u)
        if k=='11_laugh': u='HA-HA-HA!'
        words.append([round(t0+s,3),round(t0+e,3),u])
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
EV={'slurp':0.0,'enter':0.25,
    'door':wt('01_noodle','DOOR'),'nose':wt('02_palate','NOSE'),'down':wt('02_palate','DOWN'),'peek':wt('03_noodle','PEEK'),
    'noway':START['04_palate'],'shut':wt('04_palate','SHUT'),'up':wt('05_noodle','UP'),
    'public':wt('06_palate','PUBLIC'),'bubble':wt('06_palate','COME')-.1,'bubbleEnd':lend('06_palate')+.25,
    'boring':wt('07_noodle','BORING'),'ring':lend('07_noodle')+.1,'brain':START['08_brain'],'joke':wt('08_brain','JOKE'),
    'notnow':wt('09_palate','NOT'),'noodles':wt('09_palate','NOODLES'),'toolate':START['10_brain'],
    'laugh':START['11_laugh'],'laughEnd':lend('11_laugh'),'whoa':START['12_palate'],'breathing':wt('12_palate','BREATHING'),
    'drop':wt('12_palate','DROP'),'cant':wt('12_palate','CAN\'T'),'launch':lend('12_palate')-.35,'goingup':wt('13_noodle','UP'),
    'innose':START['14_noodle']-.35,'hairy':wt('14_noodle','HAIRY'),'wait':wt('14_noodle','WAIT'),'daylight':wt('14_noodle','DAYLIGHT'),
    'popout':lend('14_noodle')+.05,'blame':START['15_palate'],'goodjoke':wt('16_brain','JOKE'),
    'clinic':START['17_patient']-.6,'regurg':wt('18_doctor','REGURGITATION'),'swallow':wt('18_doctor','SWALLOW'),
    'seals':wt('18_doctor','SEALS'),'laughing':wt('18_doctor','LAUGHING'),'drops':wt('18_doctor','DROPS'),'shoot':wt('18_doctor','SHOOT'),
    'harmless':wt('18_doctor','HARMLESS'),'lot':wt('18_doctor','LOT'),'checked':wt('18_doctor','CHECKED'),
    'stinger':START['19_noodle']-.75,'chew':wt('19_noodle','CHEW'),'then':wt('19_noodle','THEN'),'cta':lend('19_noodle')+.1}
sfx=np.zeros(N,np.float32)
def S(f,t,g,rate=1.0):
    a=load('../../assets/sfx/'+f)*g
    if rate!=1.0: a=np.interp(np.arange(0,len(a),rate),np.arange(len(a)),a).astype(np.float32)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
def slurp(t,dur=.7,g=.5):   # wet slurp: noise through a sweeping resonant band with a fast wobble
    n=int(dur*SR); x=np.random.default_rng(3).standard_normal(n).astype(np.float32); tt=np.arange(n)/SR
    f=500+1500*(tt/dur)**.7; ph=2*np.pi*np.cumsum(f)/SR; y=np.zeros(n,np.float32); r=.985; a1=a2=0.0
    c=np.cos(2*np.pi*f/SR)
    for j in range(n):   # 2-pole resonator
        v=x[j]*.04+2*r*c[j]*a1-r*r*a2; a2=a1; a1=v; y[j]=v
    env=np.minimum(1,tt/.05)*np.minimum(1,(dur-tt)/.15)*(.55+.45*np.sin(2*np.pi*22*tt)**2)
    y=y/np.abs(y).max()*env*g; i=int(t*SR); sfx[i:i+n]+=y[:N-i]
slurp(0.0,.75,.55); S('1492.mp3',EV['enter'],.3)
S('2882.mp3',EV['nose']-.05,.3)                 # NOSE / SOFT PALATE labels pop
S('2209.mp3',EV['noway'],.5); S('473.mp3',EV['noway']+.18,.35)     # shove + boing
S('2151.mp3',EV['shut'],.4)
S('1486.mp3',EV['bubble'],.3); S('343.mp3',EV['public']+.1,.35)    # bubble: people laughing at him
S('1351.mp3',EV['ring'],.55)
S('2882.mp3',EV['brain'],.3)
S('2999.mp3',EV['notnow'],.35)
S('2936.mp3',EV['drop'],.45); S('2209.mp3',EV['drop']+.05,.4)     # the palate drops: clang + thump
S('1714.mp3',EV['launch'],.55); S('616.mp3',EV['launch']+.1,.45)  # rocket up the nose
S('2886.mp3',EV['hairy']-.2,.3); S('2364.mp3',EV['popout'],.55); S('473.mp3',EV['popout']+.1,.3)
S('1714.mp3',EV['clinic']-.15,.4)
S('2882.mp3',EV['regurg']-.05,.45); S('1486.mp3',EV['seals']-.3,.3); S('2151.mp3',EV['drops'],.4); S('2882.mp3',EV['lot'],.35)
S('1492.mp3',EV['stinger']-.1,.4); S('2894.mp3',EV['then']+.35,.35); S('2873.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END,' clinic at %.0f%%'%(100*EV['clinic']/END)); print({k:round(v,2) for k,v in EV.items()})

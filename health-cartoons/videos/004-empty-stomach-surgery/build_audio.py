# 004: voice/sfx/music + data.js (line timings, mouth envelopes, words, events) from proc/*.wav + words.json.
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=['01_stomach','02_burger','03_stomach','04_burger','05_stomach','06_burger','07_brain','08_stomach','09_burger','10_lungs','11_burger',
       '12_lungs','13_burger','14_lungs','15_patient','16_doctor','17_burger']
GAP={'01_stomach':.55,'02_burger':.16,'03_stomach':.16,'04_burger':.16,'05_stomach':.16,'06_burger':.18,'07_brain':1.05,'08_stomach':.25,
     '09_burger':1.0,'10_lungs':.9,'11_burger':.18,'12_lungs':.16,'13_burger':.25,'14_lungs':.2,'15_patient':.95,'16_doctor':.3,'17_burger':1.0}
FIX={'UGH':None}
A={k:load(f'proc/{k}.wav') for k in ORDER}
# even out line loudness (takes ranged over 14 dB, the quiet ones sank under the music): pull each line 80% of the way to -19 dB
for k in ORDER:
    act=A[k][np.abs(A[k])>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); g=float(np.clip((-19-db)*.8,-6,10))
    A[k]=A[k]*10**(g/20); print(k,'gain %+.1f dB'%g)
t=0; START={}
for k in ORDER: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+2.2,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
for k in ORDER:
    a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    words=[]
    for s,e,w in W[k]:
        u=re.sub(r"[^A-Za-z'\-]","",w).upper(); u=FIX.get(u,u)
        if u: words.append([round(t0+s,3),round(t0+e,3),u])
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
EV={'drop':0.25,'surgery':wt('03_stomach','SURGERY'),'sleep':wt('05_stomach','SLEEP'),'door':wt('05_stomach','DOOR'),'up':wt('05_stomach','UP'),
    'down':wt('06_burger','DOWN'),'ring':lend('06_burger')+.1,'brain':START['07_brain'],'lights':wt('07_brain','LIGHTS'),
    'drowsy':START['08_stomach'],'limp':wt('08_stomach','LIMP'),'asleep':lend('08_stomach')-.9,'float':lend('08_stomach')-.2,
    'throat':START['09_burger']+.55,'wrongpipe':lend('09_burger')+.05,'lungs':START['10_lungs']-.55,'land':START['10_lungs']-.3,
    'pipe':wt('10_lungs','PIPE'),'cough1':wt('12_lungs','COUGH'),'cough2':wt('12_lungs','COUGH',1),'cant':wt('12_lungs','CAN\'T'),
    'asleepB':wt('13_burger','ASLEEP'),'nocough':wt('13_burger','COUGH'),'nogag':wt('13_burger','GAG'),'burn':START['14_lungs'],
    'clinic':START['15_patient']-.6,'aspiration':wt('16_doctor','ASPIRATION'),'relaxes':wt('16_doctor','RELAXES'),'reflex':wt('16_doctor','REFLEX'),'shuts':wt('16_doctor','SHUTS'),'came':wt('16_doctor','CAME'),
    'slipped':wt('16_doctor','SLIPPED'),'six':wt('16_doctor','SIX'),'hours':wt('16_doctor','HOURS'),'stinger':START['17_burger']-.75,
    'after':wt('17_burger','AFTER'),'cta':lend('17_burger')+.1}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):   # dur: keep only the first `dur` seconds, with a short fade-out
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.25*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# Mixkit ids checked by title AND by the AST tagger (PLAYBOOK "Sound effects map"; the old map had wrong names)
S('1492.mp3',0.0,.3); S('1464.mp3',EV['drop'],.45); S('2890.mp3',.6,.4); S('2894.mp3',.66,.35)   # whoosh in, swoosh down, splat + boing on landing
S('2357.mp3',EV['surgery']-.05,.45); S('1464.mp3',EV['up'],.4); S('1464.mp3',EV['down'],.35)       # label pop, arrows
S('1351.mp3',EV['ring'],.55); S('2358.mp3',EV['brain'],.35)                                          # phone ring, inset pops in
S('473.mp3',EV['limp']+.55,.3); S('1486.mp3',EV['float']-.1,.35)                                     # sad "fail" jingle as the door goes limp, float whoosh
S('1492.mp3',EV['throat'],.4); S('616.mp3',EV['throat']+.3,.35); S('3024.mp3',EV['wrongpipe']-.4,.4)
S('2364.mp3',EV['land'],.55); S('2894.mp3',EV['land']+.08,.4); S('2357.mp3',EV['pipe'],.35)
S('473.mp3',EV['cant']+.1,.35); S('123.mp3',EV['burn'],.35,2.2)                                      # can't cough: fail jingle; burning: sizzle
S('1492.mp3',EV['clinic']-.15,.4); S('2357.mp3',EV['aspiration']-.05,.45); S('2358.mp3',EV['relaxes']-.3,.35); S('2364.mp3',EV['slipped'],.4); S('2256.mp3',EV['six'],.4)
S('1492.mp3',EV['stinger']-.1,.4); S('473.mp3',EV['after']+.3,.3); S('2359.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END,' clinic at %.0f%%'%(100*EV['clinic']/END)); print({k:round(v,2) for k,v in EV.items()})

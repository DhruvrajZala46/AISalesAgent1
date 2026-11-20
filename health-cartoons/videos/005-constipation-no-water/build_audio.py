# 005: voice/sfx/music + data.js (line timings, mouth envelopes, words, events) from proc/*.wav + words.json.
# The timeline follows the 27M reference shot list (script.md): the same beats, the same two silent gags, the clinic at ~57%.
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=['01_stomach','02_stomach','03_stomach','04_stomach','05_brain','06_stomach','07_brain','08_stomach','09_stomach','10_stomach',
       '11_softpoop','12_rockpoop','13_boy','14_boy','15_mom','16_doctor','17_rockpoop']
GAP={'01_stomach':.85,'02_stomach':.25,'03_stomach':.85,'04_stomach':.8,'05_brain':.25,'06_stomach':.2,'07_brain':.2,
     '08_stomach':5.3,                     # SILENT GAG 1 (ref 6.3 s): Timmy gulps soda, a soda wave floods the food and drains away
     '09_stomach':1.0,'10_stomach':.2,
     '11_softpoop':3.5,                    # SILENT GAG 2 (ref 4.7 s): the food is shoved on, cut to the rectum, the rock poop drops in
     '12_rockpoop':.25,'13_boy':.75,'14_boy':.2,'15_mom':.85,'16_doctor':.3,'17_rockpoop':1.5}
FIX={'MOOM':'MOM'}
A={k:load(f'proc/{k}.wav') for k in ORDER}
# even out line loudness (004 lesson): pull each line 80% of the way to -19 dB
for k in ORDER:
    act=A[k][np.abs(A[k])>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); g=float(np.clip((-19-db)*.8,-6,10))
    A[k]=A[k]*10**(g/20); print(k,'gain %+.1f dB'%g)
t=0; START={}
for k in ORDER: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+2.4,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
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
g1=lend('07_brain')
EV={'food':0.08,'land':0.62,'stir':START['02_stomach']+.6,'stuck':START['03_stomach']-.3,'ring':lend('03_stomach')+.15,
    'bubble':lend('04_stomach')+.05,'gulp':g1+.25,'pour':g1+1.9,'flood':g1+2.7,'drain':g1+4.2,'dry':g1+5.2,
    'stir2':START['09_stomach']-.95,'snap':START['09_stomach']-.4,'shove':wt('10_stomach','YOUR'),
    'squeeze':lend('10_stomach')+.05,'rectum':lend('10_stomach')+1.0,'rockdrop':lend('10_stomach')+1.45,'rockland':lend('10_stomach')+1.85,
    'softin':START['11_softpoop']-1.1,'bath':START['13_boy']-.55,'clinic':START['15_mom']-.6,
    'constipation':wt('16_doctor','CONSTIPATION'),'soda':wt('16_doctor','SODA'),'pulls':wt('16_doctor','PULLS'),
    'hard':wt('16_doctor','HARD'),'push':wt('16_doctor','PUSH'),'drink':wt('16_doctor','DRINK'),
    'stinger':START['17_rockpoop']-1.2,'splash':START['17_rockpoop']-.55,'slide':lend('17_rockpoop')+.05,'cta':lend('17_rockpoop')+.75}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):   # dur: keep only the first `dur` seconds, with a short fade-out
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.25*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# SFX at the reference's moments (boing on the food drop, cracks on the stick, plops for the soda and the poop), Mixkit ids checked (PLAYBOOK 3)
S('1492.mp3',0.0,.35); S('2894.mp3',EV['land'],.45); S('2890.mp3',EV['land']+.06,.35); S('2364.mp3',EV['land']+.18,.35); S('2364.mp3',EV['land']+.34,.3)
S('1884.mp3',EV['stir'],.35); S('1884.mp3',EV['stir']+.55,.3); S('2182.mp3',EV['stuck'],.45)                  # squishy stirring, the stick jams
S('1351.mp3',EV['ring'],.5); S('2358.mp3',EV['bubble'],.4)                                                     # phone ring, Timmy's bubble pops in
S('2828.mp3',EV['gulp'],.5); S('2828.mp3',EV['gulp']+.55,.45); S('2828.mp3',EV['gulp']+1.1,.45)              # glug glug glug
S('3181.mp3',EV['pour'],.45,1.4); S('2890.mp3',EV['flood'],.4); S('732.mp3',EV['flood']+.2,.4); S('1321.mp3',EV['flood']+.3,.3,1.4)
S('3207.mp3',EV['drain'],.45); S('473.mp3',EV['dry'],.25)                                                      # the soda drains away, fail jingle
S('1884.mp3',EV['stir2'],.3); S('2945.mp3',EV['snap'],.6); S('2182.mp3',EV['snap']+.05,.35)                    # the stick SNAPS
S('2149.mp3',EV['shove'],.45); S('1886.mp3',EV['squeeze'],.4); S('1492.mp3',EV['rectum']-.15,.4)
S('2920.mp3',EV['rockland'],.6); S('2894.mp3',EV['rockland']+.05,.35); S('2813.mp3',EV['softin']+.6,.4)       # thud of the rock, squeaky soft poop
S('2357.mp3',EV['rectum']+.4,.35)
S('1492.mp3',EV['bath']-.1,.35)
S('1492.mp3',EV['clinic']-.15,.4); S('2357.mp3',EV['constipation']-.05,.45); S('2358.mp3',EV['soda']-.3,.35)
S('2358.mp3',EV['pulls']-.3,.3); S('2358.mp3',EV['hard']-.3,.3); S('2256.mp3',EV['drink'],.4)
S('1492.mp3',EV['stinger']-.1,.4); S('1311.mp3',EV['splash'],.5,1.2); S('2364.mp3',EV['slide']+.3,.4); S('1889.mp3',EV['slide']+.7,.35,2.2); S('2359.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END,' clinic at %.0f%%'%(100*EV['clinic']/END)); print({k:round(v,2) for k,v in EV.items()})

# 008: voice/sfx/music + data.js. The timeline follows the 21M reference shot list (script.md).
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p,af=None):
    cmd=['ffmpeg','-v','error','-i',p]+(['-af',af] if af else [])+['-f','s16le','-ac','1','-ar',str(SR),'-']
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=[l.split()[0] for l in open('takes_manifest.tsv')]
GAP={'01_guard':2.0,                # silent intro: blood cells roll past the cut, the officer walks in
     '02_guard':.2,'03_guard':.35,'04_guard':.15,'05_brain':.3,
     '06_stomach':2.6,              # cut to the sleeping stomach: two capsules drop in, splash, it wakes up
     '07_pill':.25,'08_stomach':.15,'09_pill2':.15,'10_stomach':.2,'11_pill':.2,'12_pill2':.15,
     '13_pill2':3.1,                # SILENT: the stomach stirs them in, they dissolve, ride a vein, reach a fork
     '14_pill':.2,'15_pill':.1,
     '16_pill':2.6,                 # SILENT: they split into two tunnels; cut back to the boarded-up cut and a prostaglandin
     '17_prost':.15,'18_pill2':.15,
     '19_patient':2.1,              # SILENT: dust-cloud fight, the prostaglandin is knocked out; cut to the clinic
     '20_doctor':.3,'21_patient':.35}
A={k:load(f'proc/{k}.wav','highpass=f=420,lowpass=f=3200,volume=1.8' if k=='05_brain' else None) for k in ORDER}   # the brain is on the phone
for k in ORDER:   # even out line loudness (004 lesson)
    act=A[k][np.abs(A[k])>0.01]; db=20*np.log10(np.sqrt((act**2).mean())+1e-9); g=float(np.clip((-19-db)*.8,-6,10)); A[k]=A[k]*10**(g/20)
t=0; START={}
for k in ORDER: t+=GAP[k]; START[k]=round(t,3); t+=len(A[k])/SR
END=round(t+2.6,3); N=int(END*SR); voice=np.zeros(N,np.float32); lines=[]
for k in ORDER:
    a=A[k]; t0=START[k]; i=int(t0*SR); voice[i:i+len(a)]+=a
    hop=SR//FPS; env=[float(np.sqrt((a[j:j+hop]**2).mean())) for j in range(0,len(a),hop)]
    mx=max(env) or 1; env=[round(min(1,e/mx*1.35),3) for e in env]
    words=[]
    for s,e,w in W[k]:
        u=re.sub(r"[^A-Za-z'\-]","",w).upper()
        if u.startswith('-') and words: words[-1][1]=round(t0+e,3); words[-1][2]+=u; continue
        if u=='KILLERS' and words and words[-1][2]=='PAIN': words[-1][1]=round(t0+e,3); words[-1][2]='PAINKILLERS'; continue
        if u: words.append([round(t0+s,3),round(t0+e,3),u])
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
EV={'walk':.5,'whoa':START['01_guard'],'phone':START['03_guard']-.3,'brainUp':START['05_brain']-.25,
    'stom':lend('05_brain')+.25,'drop':lend('05_brain')+.7,'wake':START['06_stomach']-.45,
    'stir':lend('12_pill2')+.15,'vein':lend('12_pill2')+1.45,'fork':START['13_pill2']-.75,
    'split':lend('15_pill')+.1,'cut2':lend('15_pill')+1.2,'arrive':lend('15_pill')+1.6,
    'fight':lend('18_pill2')+.1,'ko':lend('18_pill2')+1.35,'clinic':START['19_patient']-.45,
    'heal':wt('20_doctor','HEAL'),'prost':wt('20_doctor','PROSTAGLANDINS'),'brainW':wt('20_doctor','BRAIN'),
    'looking':wt('20_doctor','LOOKING'),'down':wt('20_doctor','DOWN'),'cta':lend('21_patient')+.2}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.25*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# SFX: Mixkit ids checked by title + AST tagger (PLAYBOOK section 3)
S('1486.mp3',.05,.3,1.6); S('2364.mp3',.7,.25); S('2364.mp3',1.1,.25); S('2364.mp3',1.5,.22)                 # cells roll, the officer's steps
S('772.mp3',EV['whoa']-.05,.35); S('1351.mp3',EV['phone'],.4,1.0); S('2358.mp3',EV['brainUp'],.4)            # the cut, phone, brain inset
S('1492.mp3',EV['stom']-.1,.4); S('1464.mp3',EV['drop'],.4); S('2890.mp3',EV['drop']+.75,.45); S('2890.mp3',EV['drop']+.95,.4)   # capsules splash in
S('2894.mp3',EV['wake'],.4); S('2357.mp3',START['07_pill']+.2,.35)                                            # wakes up, label
S('1886.mp3',EV['stir'],.4); S('1884.mp3',EV['stir']+.4,.4); S('732.mp3',EV['stir']+.6,.35,1.0)                # stir + fizz
S('1486.mp3',EV['vein'],.35,1.4); S('1492.mp3',EV['fork']-.1,.35)                                             # ride the vein, the fork
S('1464.mp3',EV['split'],.4); S('1464.mp3',EV['split']+.25,.35)                                              # split up
S('1492.mp3',EV['cut2']-.1,.35); S('2182.mp3',EV['cut2']+.1,.3); S('2182.mp3',EV['cut2']+.3,.3); S('2182.mp3',EV['cut2']+.5,.3)   # boarded-up cut
S('2813.mp3',EV['arrive'],.3); S('2357.mp3',START['17_prost']-.2,.35)
S('2149.mp3',EV['fight'],.45); S('2151.mp3',EV['fight']+.3,.45); S('2149.mp3',EV['fight']+.65,.45); S('2151.mp3',EV['fight']+.95,.45)
S('2894.mp3',EV['ko'],.45); S('473.mp3',EV['ko']+.25,.25)                                                     # knocked out
S('1492.mp3',EV['clinic']-.15,.4); S('2357.mp3',EV['prost']-.05,.45); S('2358.mp3',EV['heal']-.3,.35); S('2358.mp3',EV['looking']-.3,.35)
S('2256.mp3',EV['down'],.4); S('2359.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END,' clinic at %.0f%%'%(100*EV['clinic']/END)); print({k:round(v,2) for k,v in EV.items()}); print({k:round(v,2) for k,v in START.items()})

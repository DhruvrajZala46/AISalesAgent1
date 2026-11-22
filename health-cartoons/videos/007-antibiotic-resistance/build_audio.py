# 007: voice/sfx/music + data.js. The timeline follows the 17M reference shot list (script.md).
import numpy as np, subprocess, json, re
SR=44100; FPS=30
def load(p): return np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-f','s16le','-ac','1','-ar',str(SR),'-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768
W=json.load(open('words.json'))
ORDER=['01_stomach','02_stomach','03_stomach','04_buddy','05_stomach','06_buddy','07_stomach','08_guard','09_guard','10_bacteria','11_bacteria',
       '12_bacteria','13_guard','14_guard','15_wbc','16_bacteria','17_wbc','18_guard','19_guard','20_stomach','21_antibiotic','22_bacteria',
       '23_bacteria','24_patient','25_doctor','26_bacteria']
GAP={'01_stomach':1.0,             # capsules drop in first
     '02_stomach':.2,'03_stomach':.15,'04_buddy':.25,'05_stomach':.15,'06_buddy':.15,'07_stomach':.2,
     '08_guard':2.2,               # cut to the skin: the bacterium slips in through the cut (silent)
     '09_guard':.15,'10_bacteria':.2,'11_bacteria':.15,'12_bacteria':.2,
     '13_guard':1.1,               # the shove: the guard falls, gets up, grabs his radio
     '14_guard':.15,'15_wbc':1.0,  # the white blood cell rolls in
     '16_bacteria':.2,'17_wbc':.15,
     '18_guard':2.3,               # SILENT: the fight in a dust cloud, the white blood cell is beaten, the bacteria multiply
     '19_guard':.15,
     '20_stomach':1.4,             # cut to the stomach: another capsule drops
     '21_antibiotic':1.3,          # cut back: the antibiotic soldier marches in
     '22_bacteria':1.0,            # the spear bounces off a shield
     '23_bacteria':.2,
     '24_patient':1.1,             # cut to the hospital
     '25_doctor':.3,
     '26_bacteria':1.3}            # stinger: a stronger antibiotic arrives
FIX={}
A={k:load(f'proc/{k}.wav') for k in ORDER}
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
        u=re.sub(r"[^A-Za-z'\-]","",w).upper(); u=FIX.get(u,u)
        if u.startswith('-') and words: words[-1][1]=round(t0+e,3); words[-1][2]+=u; continue   # "Uh" + "-oh" -> one caption "UH-OH"
        if u: words.append([round(t0+s,3),round(t0+e,3),u])
    lines.append({'id':k,'who':k.split('_')[1],'t0':t0,'dur':round(len(a)/SR,3),'env':env,'words':words})
def wt(k,word,n=0):
    L=[l for l in lines if l['id']==k][0]; m=[w for w in L['words'] if w[2]==word]; return m[n][0] if m else L['t0']
def lend(k): return START[k]+len(A[k])/SR
EV={'drop':.15,'burn':wt('07_stomach','BURNS'),'skin':lend('07_stomach')+.25,'sneak':lend('07_stomach')+.5,'stop':START['08_guard'],
    'shove':wt('12_bacteria','WAY'),'radio':START['13_guard']-.35,'wbc':lend('14_guard')+.1,'fight':lend('17_wbc')+.1,'clones':lend('17_wbc')+1.5,
    'wbcGone':lend('17_wbc')+1.9,'stom2':lend('19_guard')+.2,'drop2':lend('19_guard')+.35,'skin2':lend('20_stomach')+.25,'ab':lend('20_stomach')+.35,
    'poke':lend('21_antibiotic')+.15,'bounce':lend('21_antibiotic')+.45,'clinic':lend('23_bacteria')+.25,
    'resist':wt('25_doctor','RESISTANCE'),'misused':wt('25_doctor','MISUSED'),'headache':wt('25_doctor','HEADACHE'),'adapt':wt('25_doctor','ADAPT'),
    'stronger':wt('25_doctor','STRONGER'),'sting':lend('25_doctor')+.15,'big':START['26_bacteria']-.9,'cta':lend('26_bacteria')+.2}
sfx=np.zeros(N,np.float32)
def S(f,t,g,dur=None):
    a=load('../../assets/sfx/'+f)*g
    if dur: a=a[:int(dur*SR)].copy(); fl=min(len(a),int(.25*SR)); a[-fl:]*=np.linspace(1,0,fl)
    i=max(0,int(t*SR)); n=min(len(a),N-i); sfx[i:i+n]+=a[:n]
# SFX: Mixkit ids checked by title + AST tagger (PLAYBOOK section 3)
S('1464.mp3',EV['drop'],.4); S('2364.mp3',EV['drop']+.55,.4); S('2364.mp3',EV['drop']+.7,.35)              # capsules drop and plop
S('123.mp3',EV['burn']-.1,.3,1.6)                                                                              # sizzle on "burns"
S('1492.mp3',EV['skin']-.1,.4); S('2357.mp3',EV['skin']+.4,.3); S('2813.mp3',EV['sneak']+.6,.35)              # cut to the skin, label, sneaky squeak
S('1838.mp3',EV['stop']-.05,.25); S('2149.mp3',EV['shove'],.5); S('2894.mp3',EV['shove']+.35,.4); S('2182.mp3',EV['shove']+.5,.35)   # whistle-ish beep, shove, fall
S('1351.mp3',EV['radio'],.4,1.0); S('1464.mp3',EV['wbc'],.45); S('2895.mp3',EV['wbc']+.6,.35)                 # radio, the white blood cell rolls in
S('2149.mp3',EV['fight'],.45); S('2151.mp3',EV['fight']+.35,.45); S('2149.mp3',EV['fight']+.7,.45); S('2151.mp3',EV['fight']+1.05,.45); S('2894.mp3',EV['fight']+1.45,.4)
S('2359.mp3',EV['clones'],.4); S('473.mp3',EV['wbcGone'],.3)                                                   # bacteria pop out, fail jingle
S('1492.mp3',EV['stom2']-.1,.35); S('1464.mp3',EV['drop2'],.4); S('2364.mp3',EV['drop2']+.5,.35)
S('1492.mp3',EV['skin2']-.1,.35); S('2182.mp3',EV['ab']+.3,.3); S('2182.mp3',EV['ab']+.75,.3)                 # marching steps
S('2149.mp3',EV['poke'],.45); S('2895.mp3',EV['bounce'],.5)                                                    # poke, metallic boing off the shield
S('1492.mp3',EV['clinic']-.15,.4); S('2357.mp3',EV['resist']-.05,.45); S('2358.mp3',EV['misused']-.3,.35); S('2358.mp3',EV['adapt']-.3,.35); S('2256.mp3',EV['stronger'],.4)
S('1492.mp3',EV['sting']-.1,.4); S('3024.mp3',EV['big'],.35,1.4); S('2359.mp3',EV['cta'],.45)
mus=np.tile(load('../../assets/music/mixkit-9.mp3'),3)[:N]; fl=int(1.4*SR); mus[-fl:]*=np.linspace(1,0,fl)
for name,b in [('voice',voice),('sfx',sfx),('music',mus)]:
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',f'{name}.wav'],input=np.clip(b,-1,1).tobytes())
data={'end':END,'lines':lines,'ev':EV,'start':START}
json.dump(data,open('data.json','w')); open('data.js','w').write('window.DATA='+json.dumps(data)+';')
print('END',END,' clinic at %.0f%%'%(100*EV['clinic']/END)); print({k:round(v,2) for k,v in EV.items()})

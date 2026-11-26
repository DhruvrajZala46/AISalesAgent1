// =============== 024: "Why you should never take a pill without water." The food pipe, the time card, the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${esoScene()}</g>`, S2=`<g id="s2">${cardScene()}</g>`, S3=`<g id="s3">${clinicRoom()}</g>`;
svg.innerHTML=`<defs><filter id="capsh" x="-20%" y="-40%" width="140%" height="180%"><feDropShadow dx="2" dy="3" stdDeviation="1" flood-color="#000" flood-opacity=".5"/></filter>${DEFS}</defs>`
 +`<g id="cam">`+S1+S2+S3+`</g>`+`<g id="wm" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:23px" fill="#fff" stroke="#000" stroke-opacity=".25" stroke-width=".8" opacity=".42" text-anchor="middle">${[[360,46,0],[560,330,-28],[150,620,-28],[575,860,-28],[170,1180,-28]].map(([x,y,r])=>`<text x="${x}" y="${y}" transform="rotate(${r},${x},${y})">@GiggleMD</text>`).join('')}</g>`
 +`<g id="capg" filter="url(#capsh)"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:5px;font-size:50px;letter-spacing:.5px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);if($(id+'_m'))setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1,sy=null)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s.toFixed(3)},${(sy===null?s:sy).toFixed(3)})`);
const rn=k=>{const x=Math.sin(k*12.9898)*43758.5453;return x-Math.floor(x);};
const PX=345, PY=455;                                  // where the pill sticks
// ---------- scene 1: the food pipe ----------
function renderEso(T){
  // the pill shoots down and sticks across the dry pipe
  const t=T-E.drop,k=clamp(P(t,0,.3)),land=t>=.3,sq=land?Math.max(0,1-(t-.3)/.25):0,plT=speak('pill',T);
  const melt=clamp(P(T,E.fizz,E.fizz+3))*.18+clamp(P(T,E.burn,E.burn+5))*.17;
  let x=lerp(380,PX,k),y=lerp(-170,PY,k*k),r=lerp(-75,-24,k);
  if(land){r=-24+(inL('02_pill',T)?Math.sin(T*16)*3:0);x=PX+(inL('02_pill',T)?Math.sin(T*23)*3:0);}
  const s=(.92-melt*.92)*(1+sq*.12);mv('pillW',x,y,r,s,(.92-melt*.92)*(1-sq*.12));
  let pf={dx:0,dy:-4,lid:.1,bA:0,arch:4,mood:-.3};
  if(inL('02_pill',T))pf={dx:4,dy:-2,lid:.05,bA:-14,arch:2,mood:-.7};
  if(T>=E.fizz-.2)pf={dx:-6,dy:8,lid:.1,bA:-16,arch:7,mood:-.8};
  if(inL('09_pill',T))pf={dx:4,dy:10,lid:.25,bA:-14,arch:7,mood:-.5};
  face('pl',17,{...pf,blink:blinkK(T,2.3),small:T>=E.burn,bx:24,by:-30,bw:18,talk:plT,mw:9,T,seed:2});
  // the brain, in bed, in a thought bubble
  const bOn=T>=E.bub&&T<E.card;show('bub',bOn?1:0);
  if(bOn){$('bub').setAttribute('transform',`translate(540,215) scale(${eob(P(T,E.bub,E.bub+.3)).toFixed(3)}) translate(-540,-215)`);
    const lk=eio(P(T,E.lie,E.lie+.35)),brT=speak('brain',T);
    $('brW').setAttribute('transform',`translate(${lerp(560,548,lk).toFixed(1)},${(lerp(176,226,lk)+(lk<1?Math.sin(T*1.6)*2:Math.sin(T*1.2)*1.5)).toFixed(1)}) rotate(${lerp(brT>.3?Math.sin(T*6)*2:0,-12,lk).toFixed(1)})`);
    face('br',28,{dx:-12,dy:14,lid:lk>.5?.2:.5,blink:lk>.9?1:blinkK(T,.9)*.6,bx:34,by:-40,bw:28,bA:-6,arch:6,talk:brT,mw:10,mood:-.1,T,seed:3});
    const z=T>=E.lie+.5;show('zz',z?1:0);if(z){$('z1').setAttribute('y',(150+Math.sin(T*2)*6).toFixed(1));$('z2').setAttribute('y',(120+Math.sin(T*2+1)*6).toFixed(1));}}
  // the pill melts: fizz
  let fz='';if(T>=E.fizz&&T<E.card){for(let j=0;j<12;j++){const q=((T*.9+j/12)%1),a=rn(j)*Math.PI*2;
    fz+=`<circle cx="${(PX+Math.cos(a)*110*(1-melt)+Math.sin(T*3+j)*6).toFixed(0)}" cy="${(PY+Math.sin(a)*40-q*120).toFixed(0)}" r="${(5+j%3*3)}" fill="#fff" stroke="${INK}" stroke-width="2" opacity="${(1-q).toFixed(2)}"/>`;}}
  $('fz').innerHTML=fz;
  // it burns the wall: red glow, a sore, smoke
  const kb=clamp(P(T,E.burn,E.burn+1.2));
  $('burn').innerHTML=kb>0?`<circle cx="${PX}" cy="${PY+10}" r="${(70+120*kb+Math.sin(T*5)*6).toFixed(0)}" fill="url(#burnG)" opacity="${kb.toFixed(2)}"/>`:'';
  $('sore').innerHTML=kb>0?`<ellipse cx="${PX}" cy="${PY+10}" rx="${(40+110*kb).toFixed(0)}" ry="${(18+30*kb).toFixed(0)}" transform="rotate(-24,${PX},${PY+10})" fill="#b8282d" opacity="${(kb*.9).toFixed(2)}" ${OLW2}/><ellipse cx="${PX+20}" cy="${PY+2}" rx="${(20+50*kb).toFixed(0)}" ry="${(8+12*kb).toFixed(0)}" transform="rotate(-24,${PX},${PY+10})" fill="#7e1b20" opacity="${(kb*.8).toFixed(2)}"/>`:'';
  let sm='';if(kb>0){for(let j=0;j<3;j++){const q=((T*.7+j/3)%1),x0=PX-70+j*70;sm+=`<path d="M${x0},${PY-30-q*150} q-16,-22 0,-44 q16,-22 0,-44" fill="none" stroke="#f3eded" stroke-width="7" stroke-linecap="round" opacity="${((1-q)*kb*.9).toFixed(2)}"/>`;}}
  $('smk').innerHTML=sm;
  // the food pipe's face
  const eT=speak('pipe',T);let f={dx:0,dy:-24,lid:.1,bA:10,arch:3,mood:-.4,small:false};
  if(T<E.drop+.35)f={dx:0,dy:lerp(-40,-24,k),lid:0,bA:-6,arch:7,mood:-.2,small:true};
  if(inL('01_pipe',T))f={dx:-2,dy:-30,lid:.05,bA:18,arch:2,mood:-.8,small:false};
  if(inL('03_pipe',T))f={dx:-2,dy:-26,lid:0,bA:-10,arch:8,mood:-.3,small:true};
  if(inL('04_pipe',T)||(T>=E.bub&&T<E.lie))f={dx:28,dy:-38,lid:0,bA:-4,arch:7,mood:-.2,small:false};
  if(inL('06_pipe',T,0.2))f={dx:26,dy:-36,lid:0,bA:-16,arch:8,mood:-.7,small:true};
  if(T>=E.fizz)f={dx:-4,dy:-30,lid:0,bA:-14,arch:8,mood:-.8,small:true};
  if(T>=E.burn)f={dx:-4,dy:-26,lid:.55,bA:22,arch:2,mood:-1,small:false};
  face('es',52,{...f,blink:T<1.2?0:blinkK(T,1.4),bx:64,by:-70,bw:52,talk:eT,mw:eT>.05?13:18,T,seed:1});['es_bL','es_bR'].forEach(b=>$(b).setAttribute('stroke-width','9'));
  const shake=(T>=E.burn||inL('06_pipe',T,0.2))?Math.sin(T*41)*3:0;
  $('eface').setAttribute('transform',`translate(${(360+shake).toFixed(1)},${(770+Math.sin(T*2.1)*3).toFixed(1)})`);
  show('esSweat',(inL('06_pipe',T,0.2)||(T>=E.fizz&&T<E.burn))?1:0);show('esPain',T>=E.burn?1:0);
  const tear=T>=E.burn+.3;show('esTears',tear?1:0);
  if(tear)$('esTears').innerHTML=[-64,64].map((ex,i)=>{const q=((T*1.4+i*.5)%1);return `<path d="M${ex+(i?26:-26)},${18+q*90} c6,10 8,16 4,21 c-4,5 -12,4 -13,-2 c-1,-6 4,-12 9,-19 Z" fill="#8fd0f4" ${OLW2} opacity="${(1-q*.6).toFixed(2)}"/>`;}).join('');}
// ---------- scene 2: the clinic ----------
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.3,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  // the patient: hand on his chest (it burns), then guilty, then he gets it
  const guilty=T>=ST['12_patient']-.1&&T<ST['13_doctor'],happy=T>=ST['15_patient']-.1,chest=T<ST['12_patient']-.1;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2+(guilty?4:0),1,1,-4+(pT>.2?Math.sin(T*7)*1.5:0)+(guilty?-3:0));
  $('pBrows').setAttribute('d',happy?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':'M-36,70 Q-24,62 -10,57 M8,57 Q22,62 34,70');
  setMouthV('pat_m',pT,10,happy?.85:(guilty?-.3:-.6),T,6);
  setHEye('pEyeL',-4,Math.max(guilty?.45:0,blinkK(T,2.1)));setHEye('pEyeR',-4,Math.max(guilty?.45:0,blinkK(T,2.1)));show('patBlush',guilty?1:0);show('pSweat',0);
  const P3=chest?[[-84,234],[-58,338],[-4,296]]:[[-84,234],[-100,370],[-92,468]],dd=limbD(P3,[44,38,32]);
  $('patArmLD').setAttribute('d',dd);$('patArmLO').setAttribute('d',dd);$('patHandL').innerHTML=chest?hand(2,292,-110,1.2,PSK):hand(-92,480,-8,1.2,PSK);
  const rg=T>=ST['10_patient']+1.2&&T<ST['11_doctor'];show('chartRing',rg?1:0);if(rg)$('chartRing').setAttribute('r',(24+Math.sin(T*8)*3).toFixed(1));
  // the doctor's thought bubble: first the stuck pill and the sore, then the right way (water carries the pill down)
  const on=T>=E.bub2;show('dbub',on?1:0);if(!on)return;
  $('dbub').setAttribute('transform',`translate(380,232) scale(${eob(P(T,E.bub2,E.bub2+.3)).toFixed(3)}) translate(-380,-232)`);
  const right=T>=ST['14_doctor'];show('mSore',right?0:1);show('glass',right?1:0);
  if(!right){$('mSore').setAttribute('opacity',(.85+Math.sin(T*5)*.15).toFixed(2));mv('mPill',380+Math.sin(T*20)*1.5,236,-24,1);
    face('mp',17,{dx:0,dy:8,lid:.3,bA:20,arch:2,mood:-.9,small:true,bx:24,by:-30,bw:18,T,seed:7});$('mWater').innerHTML='';show('clock',0);return;}
  const g0=E.water,gk=eio(P(T,g0-.4,g0));mv('glass',238+gk*20,118,gk*62,1);
  const pourOn=T>=g0&&T<g0+1.6;
  const s0=T>=E.slide-.35?E.slide-.35:g0+.25,fk=clamp(P(T,s0,s0+1.25)),fy=fk*480;
  let w=pourOn?`<path d="M300,96 C340,84 360,70 376,40" fill="none" stroke="#7cc6f2" stroke-width="14" stroke-linecap="round"/>`:'';
  if(fk>0)w+=`<path d="M318,0 H442 V${(fy-8).toFixed(0)} q-31,${(14+Math.sin(T*9)*5).toFixed(0)} -62,0 q-31,-14 -62,0 Z" fill="#7cc6f2" opacity=".85"/>`;
  $('mWater').innerHTML=w;
  const py=fk<=0?70:Math.min(520,fy-34);mv('mPill',380+Math.sin(T*8)*4,py,-8+Math.sin(T*10)*6,1);
  face('mp',17,{dx:0,dy:4,lid:0,bA:-8,arch:7,mood:.9,small:false,bx:24,by:-30,bw:18,T,seed:7});
  const ck=T>=E.thirty;show('clock',ck?1:0);if(ck)$('clock').setAttribute('transform',`translate(575,236) scale(${eob(P(T,E.thirty,E.thirty+.3)).toFixed(3)})`);}
// reference caption system: one word, on the word's start frame; held to the next word unless the pause is over 0.3 s;
// pop = 90% on the first frame, 125% on the second, 100% from the third (no easing)
const WL=D.lines.flatMap(L=>L.words);
function caption(T){let w='',ws=0;
  for(let i=0;i<WL.length;i++){const x=WL[i],nx=WL[i+1],end=nx&&nx[0]-x[1]<0.3?nx[0]:Math.max(x[1],x[0]+.15)+.1;if(T>=x[0]&&T<end){w=x[2];ws=x[0];}}
  const c=$('cap');c.textContent=w;const y0=1000;c.setAttribute('y',y0+18);const f=Math.floor((T-ws)*30+1e-6),k=f<=0?.9:(f===1?1.25:1);
  c.setAttribute('transform',`translate(360,${y0}) scale(${k}) translate(-360,${-y0})`);}
window.render=function(Tf){const T=Math.floor(Tf*15+1e-6)/15;
  const sc=Tf<E.card?1:(Tf<E.clinic?2:3);[1,2,3].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));
  if(sc===1)renderEso(T);if(sc===3)renderClinic(T);show('wm',sc===2?0:1);
  caption(Tf);};
window.render(0);

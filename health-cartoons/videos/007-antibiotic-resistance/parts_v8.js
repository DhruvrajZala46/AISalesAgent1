// =============== 007 v2: antibiotic resistance, ALL code in the 001 / 003-v1 style (the user's references, 22 Nov 2026). No image model, no AI art. ===============
const E=D.ev, ST=D.start, END=D.end;
const KEY=/^(ANTIBIOTICS|ANTIBIOTIC|HEADACHE|BURNS|STOP|CUT|WAY|SKIN|BACTERIA|WHITE|BLOOD|CELLS|CELL|MESS|BACKUP|FAST|ANOTHER|INTRUDER|MATCH|RESIST|WEAPONS|INFECTION|RESISTANCE|MISUSED|ADAPT|STRONGER|UH-OH)$/;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
// capsule (red + white), drawn like the antibiotic soldier but tiny and faceless
function capsule(id){return `<g id="${id}"><rect x="-16" y="-34" width="32" height="68" rx="16" fill="#fff" ${STK2}/><path d="M-16,0 L-16,-18 A16,16 0 0 1 16,-18 L16,0Z" fill="#e0392f" ${STK2}/><path d="M-9,-22 L-9,-6" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".7"/></g>`;}
// ---------- SCENE 1: the stomach ----------
let S1=`<g id="s1"><g id="cam1">${stomachWorld()}</g>
 ${labelBox('lbSto','STOMACH',560,300,24)}${labelBox('lbAb','ANTIBIOTIC',590,680,22)}
</g>`;
// ---------- SCENE 2: the skin (all code) ----------
let S2=`<g id="s2"><g id="cam2"><g id="wSkin">${skinWorld()}
  ${bactSVG('cl1','#b7ee84','#6fb846')}${bactSVG('cl2','#b7ee84','#6fb846')}
  ${guardSVG('gd')}${wbcSVG('wb')}${bactSVG('bc')}<g id="shield" opacity="0"><ellipse rx="150" ry="112" fill="#a9dc7c" opacity=".25" stroke="#6d9f45" stroke-width="4"/><path d="M-90,-60 C-50,-96 40,-98 80,-70" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/></g>
  ${abSVG('ab')}${abSVG('ab2')}<g id="drops"></g><g id="dust"></g><g id="stars"></g></g></g>
 ${labelBox('lbSkin','SKIN',120,90,26)}${labelBox('lbCut','CUT',470,330,24)}${labelBox('lbBac','BACTERIA',560,600,24)}${labelBox('lbWbc','WHITE BLOOD CELL',520,560,22)}${labelBox('lbAb2','ANTIBIOTIC',540,520,22)}
</g>`;
let CTA=`<g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>`;
// =============== assemble ===============
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +S1+S2+S3+CTA+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
// gold helmet for the stronger antibiotic (stinger)
document.querySelectorAll('#ab2 path').forEach(p=>{const f=p.getAttribute('fill')||'';if(f.includes('ab2g3'))p.setAttribute('fill','#f2c233');});
// =============== timing ===============
const T_SKIN=E.skin, T_ST2=E.stom2, T_SKIN2=E.skin2, T_CLIN=E.clinic, T_STING=E.sting;
function renderSkin(T){
  skinAnim(T);
  const stinger=T>=T_STING, sk2=T>=T_SKIN2;
  // the bacterium: slips down through the cut, argues, shoves, fights, multiplies; shield later
  const bTalk=speak('bacteria',T);
  let bx=510,by=760,bs=1.05,brot=0,barms='hips',bsmug=.6,bmood=.5;
  const sn=P(T,E.sneak,E.stop-.1); if(T<E.stop){const p=along([[355,200],[360,380],[420,560],[510,760]],eio(sn));bx=p[0];by=p[1];brot=lerp(-30,0,sn);bs=lerp(.5,1.05,sn);}
  if(T>=E.shove-.3&&T<E.radio){const k=eob(P(T,E.shove-.3,E.shove+.1));bx=lerp(510,360,k);barms='push';}
  if(T>=E.radio){bx=370;by=765;bs=1.0;}
  if(T>=E.fight-.1&&T<E.clones){bx=440+Math.sin(T*30)*12;}
  if(sk2){bx=330;by=770;bs=1.0;}
  if(stinger){bx=280;by=780;bs=1.0;bsmug=0;bmood=-1;barms='up';brot=Math.sin(T*30)*2;}
  const inFight=T>=E.fight&&T<E.clones-.1;
  show('bc',inFight?0:1);
  setBact('bc',bx,by+Math.sin(T*2.2)*6,bs,{talk:bTalk,T,smug:bsmug,mood:bmood,rot:brot,arms:barms,look:stinger?1:(T<E.radio?-1:1),seed:0});
  // clones appear after the fight
  const ck=eob(P(T,E.clones,E.clones+.35)); show('cl1',T>=E.clones?1:0); show('cl2',T>=E.clones+.15?1:0);
  if(T>=E.clones){setBact('cl1',sk2?170:230,(sk2?630:660)+Math.sin(T*2.6)*8,.64*ck,{T,smug:stinger?0:.7,mood:stinger?-1:.6,seed:2,look:stinger?1:-1,arms:stinger?'up':'hips'});
    setBact('cl2',sk2?490:560,(sk2?600:620)+Math.sin(T*2.3+1)*8,.58*eob(P(T,E.clones+.15,E.clones+.5)),{T,smug:stinger?0:.7,mood:stinger?-1:.6,seed:4,look:stinger?1:-1,arms:stinger?'up':'hips'});}
  // the guard
  const gTalk=speak('guard',T), gOn=!sk2; show('gd',gOn?1:0);
  if(gOn){let gx=200,gy=710,gs=1.08,pose='stop',grot=0,gmood=-.6,brows=1;
    if(T>=E.shove){const k=eio(P(T,E.shove,E.shove+.35)),up=eio(P(T,E.radio-.3,E.radio+.2));gx=lerp(200,150,k)-up*15;gy=lerp(710,830,k)-up*50;grot=lerp(0,-78,k)*(1-up);pose=up>.5?'phone':'fallen';gs=lerp(1.08,.85,up);}
    if(T>=E.radio){pose='phone';gx=135;gy=780;gs=.85;gmood=-1;brows=-1;}
    setGuard('gd',gx,gy+(pose==='stop'?Math.sin(T*2)*3:0),gs,{talk:gTalk,T,pose,rot:grot,look:1,mood:gmood,brows});}
  // the white blood cell rolls in, fights, gets knocked away
  const wOn=T>=E.wbc&&T<E.wbcGone+.6; show('wb',wOn?1:0);
  if(wOn){const rin=eio(P(T,E.wbc,E.wbc+.7)); let wx=lerp(860,575,rin),wy=755,wr=(1-rin)*-360,ws=.98;
    if(T>=E.wbcGone){const k=P(T,E.wbcGone,E.wbcGone+.6);wx=575+k*280;wy=755-k*500;wr=k*720;ws=.98*(1-k*.5);}
    setWbc('wb',wx,wy+Math.sin(T*3)*5,ws,{talk:speak('wbc',T),T,rot:wr,look:-1,angry:1,punch:T>=ST['17_wbc']?Math.abs(Math.sin(T*10)):0});}
  // the fight dust cloud
  const fk=P(T,E.fight,E.clones); if(fk>0&&fk<1){let h='';for(let i=0;i<12;i++){const a=i/12*6.283+T*3,r=90+Math.sin(T*9+i)*20;
      h+=`<circle cx="${(500+Math.cos(a)*r).toFixed(1)}" cy="${(730+Math.sin(a)*r*.7).toFixed(1)}" r="${(60+rnd(i)*30+Math.sin(T*12+i)*8).toFixed(1)}" fill="#fff" stroke="${OL}" stroke-width="2.6"/>`;}
    h+=`<circle cx="500" cy="730" r="110" fill="#fff"/>`; $('dust').innerHTML=h;
    let s='';for(let i=0;i<5;i++){const k=((T*2.2)+i/5)%1;s+=`<path transform="translate(${(500+Math.cos(i*1.3)*k*200).toFixed(1)},${(700+Math.sin(i*1.9)*k*160).toFixed(1)}) scale(${(.6+k).toFixed(2)})" d="M0,-16 L5,-5 L16,-5 L7,2 L10,14 L0,7 L-10,14 L-7,2 L-16,-5 L-5,-5Z" fill="#ffd21f" stroke="${OL}" stroke-width="2" opacity="${(1-k).toFixed(2)}"/>`;}
    $('stars').innerHTML=s;} else {$('dust').innerHTML='';$('stars').innerHTML='';}
  // the antibiotic soldier: marches in, pokes, the spear bounces off a shield
  const aOn=sk2&&!stinger; show('ab',aOn?1:0);
  if(aOn){const k=eio(P(T,E.ab,E.ab+1.0)); let ax=lerp(860,590,k),ay=735+Math.abs(Math.sin(T*8))*(k<1?10:0),poke=0,shock=0,arot=0;
    if(T>=E.poke-.1){poke=Math.sin(clamp(P(T,E.poke-.1,E.poke+.25))*Math.PI);}
    if(T>=E.bounce){const b=P(T,E.bounce,E.bounce+.5);ax+=Math.sin(b*Math.PI)*60;arot=Math.sin(b*Math.PI)*12;shock=1;}
    setAb('ab',ax,ay,.98,{talk:speak('antibiotic',T),T,poke,shock,rot:arot,look:-1});}
  const shK=T>=E.bounce-.15&&T<T_CLIN?eob(P(T,E.bounce-.15,E.bounce+.15)):0; show('shield',shK>0?Math.min(1,shK)*(.75+.25*Math.sin(T*6)):0);
  if(shK>0) $('shield').setAttribute('transform',`translate(330,770) scale(${(1.0*shK).toFixed(3)})`);
  // stinger: a bigger antibiotic with a gold helmet slides in
  const a2=stinger; show('ab2',a2?1:0); if(a2){const k=eob(P(T,E.big,E.big+.8));setAb('ab2',lerp(900,535,k),690,1.3,{T,look:-1,mood:.6,poke:0});}
  let dr='';for(let i=0;i<3;i++){const u=((T*.4)+i/3)%1, x=lerp(i===1?404:304,352,u), y=lerp(SURF2(350)+10,470,u);dr+=`<path d="M${x.toFixed(1)},${y.toFixed(1)} c7,9 9,17 0,21 c-9,-4 -7,-12 0,-21z" fill="#d6404a" stroke="${OL}" stroke-width="2" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}$('drops').innerHTML=dr;
  // labels
  popLabel('lbSkin',T,T_SKIN+.2,T_SKIN+2.4,120,90); popLabel('lbCut',T,T_SKIN+.4,T_SKIN+2.4,470,330);
  popLabel('lbBac',T,ST['10_bacteria']-.1,ST['10_bacteria']+2.2,560,600); popLabel('lbWbc',T,E.wbc+.5,E.wbc+2.8,520,560);
  popLabel('lbAb2',T,E.ab+.6,E.ab+2.8,630,554);
}
function renderClinic(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['25_doctor'], pa=ST['24_patient'];
  let dr=2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,dr);
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8)*1; if(T>=d0&&dT<.05) pr+=Math.sin(T*9)*1.5*(speak('doctor',T-.25)>.1?1:0);
  if(T<d0&&pT>.2) pr+=Math.sin(T*7)*2;
  if(T>=E.stronger-.1&&T<E.stronger+.9) pr+=Math.sin(P(T,E.stronger-.1,E.stronger+.9)*Math.PI*2)*4;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  const worried=T<E.resist, shocked=T>=E.resist&&T<E.misused+.4;
  $('pBrows').setAttribute('d',shocked?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':(worried?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70'));
  setMouthV('doc_m',dT,10,.7,T,5); setMouthV('pat_m',pT,10,worried?-.6:.2,T,6);
  setHEye('dEyeL',3,blinkK(T,.7)); setHEye('dEyeR',3,blinkK(T,.7));
  setHEye('pEyeL',T<d0?-1:-3,blinkK(T,2.1)); setHEye('pEyeR',T<d0?-1:-3,blinkK(T,2.1));
  show('patBlush',.7); show('pSweat',T<E.misused?1:0); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  // left hand: he holds up the bandaged hand while he asks, then rests it on his lap
  const down=eio(P(T,d0+.2,d0+1.0)), up=eio(P(T,pa-.4,pa+.3));
  const sh=[-84,234], el=[lerp(lerp(-102,-124,up),-102,down),lerp(lerp(370,344,up),370,down)], wr=[lerp(lerp(-90,-44,up),-90,down),lerp(lerp(470,286,up),470,down)];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  const ha=lerp(lerp(-8,150,up),-8,down);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+(down>.5?12:0),ha,1.2,PSK)+bandageAt(wr[0]+Math.cos((ha-90)*Math.PI/180)*2,wr[1]+(down>.5?12:0),ha+90,.62);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.75&&Math.floor(T*2)%3===0)?-7:0},86,226)`);
  $('clkM').setAttribute('transform',`rotate(${T*6})`);
  // camera: push in on the patient's question, punch in on the doctor at "antibiotic resistance"
  const pq=eio(P(T,pa,pa+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,T_STING)+.07*pq, cx=lerp(360,430,pq), cy=lerp(640,600,pq);
  const pk=eio(P(T,E.resist-.15,E.resist+.15))*(1-eio(P(T,E.misused-.45,E.misused-.1)));
  z=lerp(z,1.42,pk); cx=lerp(cx,232,pk); cy=lerp(cy,430,pk);
  const ty=lerp(640,560,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // thought bubbles cut on the doctor's words: misused -> capsules for a headache; adapt -> the shield
  const sA=E.misused-.15, sB=E.adapt-.15, sE=E.stronger-.25, bOn=T>=sA&&T<sE;
  $('bub').setAttribute('opacity',bOn?1:0);
  if(bOn){const seg=T<sB?0:1, t0=[sA,sB][seg], t1=[sB,sE][seg], u=P(T,t0,t1);
    const pop=seg===0?eob(P(T,sA,sA+.3)):1+.06*Math.sin(clamp(P(T,t0,t0+.25))*Math.PI);
    $('bub').setAttribute('transform',`translate(300,178) scale(${(1.38*pop).toFixed(3)}) translate(-265,-150)`);
    show('bubA',seg===0?1:0); show('bubB',seg===1?1:0);
    if(seg===0) renderStomach(lerp(E.drop,ST['03_stomach']+1.5,u)); else renderSkin(lerp(E.poke-.3,ST['23_bacteria'],u));}
  popLabel('lbRes',T,E.resist-.05,E.misused-.2,360,64);
  popLabel('lbTip',T,E.stronger-.1,T_STING,360,84);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z'\-]/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_SKIN?1:T<T_ST2?2:T<T_SKIN2?1:T<T_CLIN?2:T<T_STING?3:2;
  ['s1','s2','s3'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  let dark=0;
  const bounds=[[0,T_SKIN],[T_SKIN,T_ST2],[T_ST2,T_SKIN2],[T_SKIN2,T_CLIN],[T_CLIN,T_STING],[T_STING,END]];
  const seg=bounds.find(([a,b])=>T>=a&&T<b)||bounds[5];
  dark=Math.max(seg[0]>0?1-P(T,seg[0],seg[0]+.16):0, seg[1]<END?P(T,seg[1]-.16,seg[1]):0);
  if(sc===1){renderStomach(T); const c=1.0+.012*Math.sin(T*.3); $('cam1').setAttribute('transform',`translate(360,640) scale(${c}) translate(-360,-640)`);
    popLabel('lbSto',T,1.6,3.4,560,300); popLabel('lbAb',T,E.drop+1.0,E.drop+3.0,590,680);}
  if(sc===2){renderSkin(T); const shake=(Math.sin(clamp(P(T,E.shove,E.shove+.3))*Math.PI)+Math.sin(clamp(P(T,E.bounce,E.bounce+.3))*Math.PI)+(T>=E.fight&&T<E.clones?.5:0))*Math.sin(T*70)*7;
    const z=1.1+.02*P(T,T_SKIN,T_ST2)*(T<T_ST2?1:0)+.02*P(T,T_SKIN2,T_CLIN)*(T>=T_SKIN2?1:0)+.008*Math.sin(T*.3);
    $('cam2').setAttribute('transform',`translate(${(360+shake).toFixed(1)},640) scale(${z.toFixed(4)}) translate(-360,-662)`);}
  if(sc===3) renderClinic(T);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0); $('cta').setAttribute('transform',`translate(360,${250+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
  show('indark',dark*.9);
  caption(T);
};
window.render(0);

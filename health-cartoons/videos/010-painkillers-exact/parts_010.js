// =============== 010: the 21M "how do painkillers find the pain" Short, copied shot for shot (same script, same sets, same staging,
// same sound moments), drawn in code with our own characters. Every position below was measured on the reference's frames. ===============
const E=D.ev, ST=D.start, END=D.end;
const KEY=/^(WHOA|HUGE|HELP|SERIOUS|CUT|OUT|ASAP|ALREADY|PAIN|HILARIOUS|STIR|AHA|JOB|OURS|FOOT|HEAL|WOUND|BRAIN|GONE|DOWN|SENSE)$/;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inLine=(id,T,pre=.1,post=.15)=>T>=ST[id]-pre&&T<lend(id)+post;
const T_STOM=E.stomach, T_VEIN=E.vein, T_TUN=E.tunnel, T_CUT2=E.cut2, T_CLIN=E.clinic;

// ---------- the six sets ----------
let S1=`<g id="s1">${wallWorld()}${topBand()}${labelTop('lbIVS','INTRAVASCULAR SPACE',360,80,562,52,530)}</g>`;
let S2=`<g id="s2">${stomachWorld10()}</g>`;
let S3=`<g id="s3">${veinWorld10()}${labelTop('lbVein','VEIN',586,52,213,50)}</g>`;
let S4=`<g id="s4">${tunnelWorld10()}</g>`;
let S5=`<g id="s5">${clinicRoom10()}<g transform="translate(190,580) scale(1.5)">${doctorSVG()}</g><g transform="translate(565,720) scale(1.6)">${patientSVG()}</g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +S1+S2+S3+S4+S5+`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

// setPill flip (a pill that walks left faces left)
const _setPill=setPill; setPill=function(id,x,y,s,o={}){_setPill(id,x,y,s,o); if(o.flip===-1){const t0=$(id).getAttribute('transform');$(id).setAttribute('transform',t0.replace(/scale\(([^)]+)\)/,(m,v)=>`scale(${-parseFloat(v)},${parseFloat(v)})`));}};

// ================= SET A / E: the cut in the vessel wall =================
// red cells roll in along the floor and hop up into the cut (the first one at 1.6 s with the squeak), one after another
const RBC_TRIPS=[[0,[[0,441],[1.6,384]],'R']];
RBC_TRIPS.push([1,[[0,170],[2.4,318]],'L']);
{for(let k=1;k<9;k++){const h=2.4+k*2.3;RBC_TRIPS.push([1+(k%3),[[h-3.8,-110],[h,318]],'L']);}}
function rbcAt(i,T){ // -> null or {x,y,s,op,dir,hop}
  for(const [cell,[[t0,x0],[t1,x1]],side] of RBC_TRIPS){ if(cell!==i) continue; if(T<t0||T>t1+.55) continue;
    if(T<=t1){const u=P(T,t0,t1);return {x:lerp(x0,x1,u),y:1080-Math.abs(Math.sin(T*7+i))*10,s:1.78,op:1,dir:side==='L'?1:-1,hop:0};}
    const h=P(T,t1,t1+.55), x=lerp(x1,392,eo(h)), y=lerp(1080,912,eo(h))-Math.sin(h*Math.PI)*50;
    return {x,y,s:lerp(1.78,1.15,P(h,.4,1)),op:1-P(h,.6,1),dir:side==='L'?1:-1,hop:h};}
  return null;}
function renderWall(T){
  const boarded=T>=T_CUT2;
  // the cut slices open from the top at 0.4-0.9 s
  $('cutReveal').setAttribute('height',(boarded?900:900*eio(P(T,E.slash,E.slash+.5))).toFixed(1));
  show('planks',boarded?1:0);
  const sk=P(T,E.spark,E.spark+.35); show('spark',sk>0&&sk<1?1:0);
  $('spark').setAttribute('transform',`translate(460,975) scale(${(eob(P(T,E.spark,E.spark+.12))*(1-P(T,E.spark+.2,E.spark+.35)*.4)).toFixed(3)}) rotate(${(sk*40).toFixed(1)})`);
  for(let i=0;i<4;i++){const r=boarded?null:rbcAt(i,T); show('rb'+i,r?r.op:0); if(!r) continue;
    $('rb'+i).setAttribute('transform',`translate(${r.x.toFixed(1)},${r.y.toFixed(1)}) rotate(${(r.hop?-r.dir*r.hop*30:Math.sin(T*7+i)*5).toFixed(1)}) scale(${r.s.toFixed(3)})`);
    const lk={dx:r.dir*24,dy:r.hop?-20:-4,lid:.1,blink:blinkK(T,i*.9)}; setOEye('rb'+i+'_eL',13,lk); setOEye('rb'+i+'_eR',13,lk);}
  // the officer: walks in from the right at 3.3, phones the brain from 6.95
  const gOn=!boarded&&T>=E.guardIn; show('gd',gOn?1:0);
  if(gOn){const wk=eo(P(T,E.guardIn,E.guardIn+.7)), gx=lerp(830,527,wk), walking=wk<1;
    const gt=speak('guard',T), phone=T>=E.phone, look=phone?-.35:-1;
    setGuard('gd',gx,951+(walking?-Math.abs(Math.sin(T*16))*12:Math.sin(T*2)*2),1.32,{talk:gt,T,pose:phone?'phone':'stop',look,mood:T<lend('01_guard')?-.4:-.2,brows:T<lend('02_guard')?1:-.3});
    show('gd_sign',0);
    if(!phone){const sw=walking?Math.sin(T*16)*16:Math.sin(T*3)*3; setArm('gd_aL',-90,0,-116,72+sw,-12,20); setArm('gd_aR',90,0,116,72-sw,12,-20);}
    // the phone: yellow sound lines at his ear while it rings and while the brain answers
    const ring=T>=E.ring&&T<T_STOM&&(T<E.ring+.6||speak('brain',T)>.05||(T>=ST['08_brain']&&T<lend('09_brain')));
    let rl='';if(ring){for(let i=0;i<3;i++){const a=-.9+i*.55, k=((T*3)+i*.3)%1;
      rl+=`<path d="M${(gx+150+Math.cos(a)*(20+k*10)).toFixed(1)},${(830+Math.sin(a)*(20+k*10)).toFixed(1)} l${(Math.cos(a)*26).toFixed(1)},${(Math.sin(a)*26).toFixed(1)}" stroke="#ffd21f" stroke-width="7" stroke-linecap="round"/>`;}}
    $('ringLines').innerHTML=rl;} else $('ringLines').innerHTML='';
  // scene E: the prostaglandin at the boarded cut, the two painkillers arrive, the fight, the knock-out
  const eOn=boarded; ['pg','pA','pB'].forEach(id=>show(id,eOn?1:0));
  if(!eOn){$('dust').innerHTML='';return;}
  const inFight=T>=E.fight&&T<E.ko, ko=T>=E.ko;
  const pgT=speak('prost',T);
  if(!ko) setProst('pg',433,903+Math.sin(T*2)*3,.85,{talk:pgT,T,look:T>=E.arrive?-1:0,rot:pgT>.1?Math.sin(T*9)*3:0,angry:T>=ST['26_prost']?.5:.2,mood:.1});
  else {const kk=eob(P(T,E.ko,E.ko+.3)); setProst('pg',lerp(433,560,kk),lerp(903,960,kk),.85,{T,rot:-70*kk,ko:1});}
  show('pg',inFight?0:1);
  const arr=eio(P(T,E.arrive,E.arrive+.8)), run=arr<1&&T>=E.arrive;
  const aT=speak('pill',T), bT=speak('pill2',T);
  setPill('pA',ko?lerp(130,286,eo(P(T,E.ko,E.ko+.2))):lerp(-60,130,arr),1004,.7,{talk:aT,T,look:1,mood:ko?1:.3,arms:ko?'fist':(aT>.05?'point':(run?'run':'down')),seed:1,run,angry:ko?0:.6});
  setPill('pB',ko?lerp(205,362,eo(P(T,E.ko,E.ko+.2))):lerp(-140,205,arr),1004,.7,{talk:bT,T,look:1,mood:ko?1:.1,arms:ko?'fist':(bT>.05?'point':(run?'run':'down')),seed:3,run,angry:ko?0:.8});
  if(ko){$('pA').setAttribute('transform',$('pA').getAttribute('transform').replace(/translate\(([^,]+),([^)]+)\)/,(m,x,y)=>`translate(${x},${(parseFloat(y)-Math.abs(Math.sin(T*8))*10).toFixed(1)})`));}
  show('pA',inFight?0:1); show('pB',inFight?0:1);
  if(inFight){let h='';const u=T-E.fight, gk=eob(P(u,0,.18))*.9, cx=376, cy=900;
    const blob=(i,sc,fill,str)=>{const a=i/16*6.283+Math.sin(u*3+i)*.08, r=(205+rnd(i)*60)*sc*gk, rr=(70+rnd(i+30)*45+Math.sin(u*14+i*1.7)*9)*sc*gk;
      return `<circle cx="${(cx+Math.cos(a)*r*1.15).toFixed(1)}" cy="${(cy+Math.sin(a)*r*.95).toFixed(1)}" r="${rr.toFixed(1)}" fill="${fill}" ${str}/>`;};
    for(let i=0;i<16;i++) h+=blob(i,1,'#d9d9d7','stroke="#a9a9a7" stroke-width="3"');
    for(let i=0;i<16;i++) h+=blob(i,.82,'#f6f6f4','');
    h+=`<ellipse cx="${cx}" cy="${cy}" rx="${(250*gk).toFixed(1)}" ry="${(210*gk).toFixed(1)}" fill="#f6f6f4"/>`;
    for(let i=0;i<5;i++){const a=i*1.3+u*4;h+=`<path d="M${(cx+Math.cos(a)*120).toFixed(1)},${(cy+Math.sin(a)*90).toFixed(1)} c16,-12 34,-6 40,8" fill="none" stroke="#c4c4c2" stroke-width="6" stroke-linecap="round"/>`;}
    for(let i=0;i<7;i++){const k=((u*2.2)+i/7)%1, a=-2.6+i*.55;h+=`<circle cx="${(cx+Math.cos(a)*(250+k*140)).toFixed(1)}" cy="${(cy+Math.sin(a)*(220+k*120)).toFixed(1)}" r="${(30*(1-k)+8).toFixed(1)}" fill="#f2f2f0" stroke="#a9a9a7" stroke-width="2.5" opacity="${(1-k*k).toFixed(2)}"/>`;}
    $('dust').innerHTML=h;} else $('dust').innerHTML='';
}

// ================= SET B: the stomach =================
function stomArm(id,sh,mid,end,rot){setHose(id,[sh,mid,end],rot,.66);}
['sArmL10','sArmR10'].forEach(id=>{$(id+'_i').setAttribute('stroke','#f38c8f');$(id+'_o').setAttribute('stroke-width','10');$(id+'_i').setAttribute('stroke-width','5.5');});
function renderStomach(T){
  const asleep=T<E.wake, se=speak('stomach',T), stirring=T>=E.stir;
  const mk=eio(P(T,E.wake,E.wake+.3));
  $('mask10').setAttribute('transform',`translate(${(mk*40).toFixed(1)},${(-mk*170).toFixed(1)}) rotate(${(mk*18).toFixed(1)},452,276)`); show('mask10',1-P(T,E.wake+.15,E.wake+.3));
  const grumpy=T>=ST['14_stomach']-.15&&!stirring, shocked=(T>=E.wake&&T<E.wake+.5)||(stirring);
  const lookP=!asleep&&!stirring, bl=blinkK(T,.3);
  const dx=lookP?-14:0, dy=lookP?30:(stirring?6:0);
  const lid=asleep?1:(grumpy?.48:(shocked?0:.06));
  setOEye('sEyeL',38,{dx,dy,lid,tilt:grumpy?14:0,blink:bl,small:shocked&&!stirring}); setOEye('sEyeR',38,{dx,dy,lid,tilt:grumpy?-14:0,blink:bl,small:shocked&&!stirring});
  setMouthV('sto_m',se,15,grumpy?-.6:(shocked?-.2:.1),T,3);
  // breathing
  const br=1+Math.sin(T*(asleep?1.5:2.4))*(asleep?.006:.003)+se*.006;
  $('stoFace10').setAttribute('transform',`translate(0,${(Math.sin(T*(asleep?1.5:2.4))*(asleep?3:1.5)-se*2).toFixed(2)})`);
  // the little arms: resting "( )" by the face, the right one pokes the pills twice, both hold the stirring stick
  const pk=Math.max(Math.sin(clamp(P(T,E.poke,E.poke+.3))*Math.PI),Math.sin(clamp(P(T,E.poke+.35,E.poke+.65))*Math.PI));
  const reach=eio(P(T,E.poke-.25,E.poke))*(1-eio(P(T,E.poke+.65,E.poke+.95)));
  const sk=stirring?[Math.cos((T-E.stir)*8)*22,Math.sin((T-E.stir)*8)*8]:[0,0];
  const w=Math.sin(T*2.2)*3;
  if(stirring){stomArm('sArmL10',[392,394],[410,420],[466+sk[0],436+sk[1]],-60); stomArm('sArmR10',[556,394],[540,420],[496+sk[0],436+sk[1]],60);}
  else {stomArm('sArmL10',[392,394],[364,432+w],[380,474],20);
    const ex=lerp(570,382,reach)+pk*-10, ey=lerp(474,600,reach)+pk*16;
    stomArm('sArmR10',[556,394],[lerp(584,520,reach),lerp(432,470,reach)-w],[ex,ey],lerp(-20,40,reach));}
  show('stick10',stirring?1:0); $('stick10').setAttribute('transform',`translate(${(480+sk[0]).toFixed(1)},${(566+sk[1]).toFixed(1)}) rotate(${(sk[0]*.25).toFixed(1)})`);
  // the juice: a gentle swell, churning while it is stirred
  const jy=x=>540+Math.sin(x/46+T*2)*5+(stirring?Math.sin(x/22-T*12)*9*Math.exp(-Math.abs(x-480)/260):0);
  let jd='M-20,'+jy(-20).toFixed(1);for(let x=0;x<=780;x+=20)jd+=` L${x},${jy(x).toFixed(1)}`;jd+=' L780,1000 L-20,1000Z';$('juice10').setAttribute('d',jd);
  let jt='';for(let x=-20;x<=780;x+=20)jt+=(jt?' L':'M')+`${x},${(jy(x)+3).toFixed(1)}`;$('juiceTop10').setAttribute('d',jt);
  // the two painkillers: out of the food pipe, plop into the juice, float there; the stir throws them up and they dissolve
  const AL=[[118,-40],[124,120],[170,250],[260,380],[330,520],[350,640]], BL=[[118,-40],[126,120],[176,252],[272,384],[350,526],[384,650]];
  [['sA',E.drop,'pill',0,AL],['sB',E.drop+.2,'pill2',1,BL]].forEach(([id,t0,who,i,path])=>{const q=(T-t0)/.55; if(q<0){show(id,0);return;}
    const talk=speak(who,T);
    let p,rot,sc=.42;
    if(q<1){p=along(path,q*q*.5+q*.5);rot=lerp(-12,i?-30:30,q)+Math.sin(q*12)*12;}
    else {const land=P(T,t0+.55,t0+.85);p=[path[5][0]+Math.sin(T*1.3+i)*3,path[5][1]+Math.sin(T*2+i*2)*4-Math.sin(land*Math.PI)*10];rot=(i?-30:30)+Math.sin(T*1.6+i)*6;
      if(reach>0&&pk>0){p=[p[0]+pk*(i?6:-6),p[1]+pk*8];rot+=pk*(i?20:-20);}}
    if(stirring){const s=T-E.stir, jump=Math.abs(Math.sin(s*7+i*1.6));p=[lerp(p[0],(i?520:432)+sk[0],P(s,0,.25)),lerp(p[1],(i?476:520)-jump*46+sk[1],P(s,0,.25))];rot=s*(i?-520:480);sc=.5;}
    const dis=stirring?P(T,E.vein-.35,E.vein-.05):0;
    setPill(id,p[0],p[1],sc,{talk,T,look:i?-.5:.5,lookY:stirring?0:-.7,mood:stirring?-.6:.5,arms:stirring?'fist':(talk>.05?'wave':'down'),seed:i*2,rot,angry:stirring?.6:0});
    show(id,1-dis);});
  // the plop: a splash ring where each pill lands
  let sp='';[[E.drop+.55,350,560],[E.drop+.75,384,566]].forEach(([t0,x,y])=>{const k=P(T,t0,t0+.45);if(k>0&&k<1){sp+=`<ellipse cx="${x}" cy="${y+4}" rx="${(14+k*46).toFixed(1)}" ry="${(4+k*10).toFixed(1)}" fill="none" stroke="#fff3e6" stroke-width="4" opacity="${(1-k).toFixed(2)}"/>`;
    for(let j=0;j<4;j++){const a=-Math.PI*(.2+j*.2), d=k*50;sp+=`<circle cx="${(x+Math.cos(a)*d).toFixed(1)}" cy="${(y+Math.sin(a)*d+k*k*60).toFixed(1)}" r="${(6*(1-k)+2).toFixed(1)}" fill="#f7c6a8" ${OLW} opacity="${(1-k).toFixed(2)}"/>`;}}});
  $('dropPills').innerHTML=sp;
}

// ================= SET C: the vein =================
function renderVein(T){
  const u=P(T,T_VEIN,T_TUN), k=P(u,.18,1);
  setPill('vA',lerp(-140,560,k),667+Math.sin(T*9)*8,.82,{T,look:1,lookY:0,mood:.7,arms:'run',seed:1,run:1});
  setPill('vB',lerp(-20,680,k),603+Math.sin(T*9+1.5)*8,.82,{T,look:1,lookY:0,mood:.4,arms:'run',seed:3,run:1});
}

// ================= SET D: the two tunnels =================
function renderTunnels(T){
  const aT=speak('pill',T), bT=speak('pill2',T);
  const hr=P(T,E.hopR,E.hopR+.7), hl=P(T,E.hopL,E.hopL+.9);
  // the bow pill (asks the question) jumps into the right tunnel ("east"), the plain one into the left
  let ax=257,ay=882,as=1.45,arot=0; if(hr>0){ax=lerp(257,628,eio(hr));ay=lerp(882,520,eio(hr))-Math.sin(hr*Math.PI)*170;as=lerp(1.45,.5,hr);arot=hr*30;}
  let bx=493,by=842,bs=1.45,brot=0; if(hl>0){bx=lerp(493,120,eio(hl));by=lerp(842,480,eio(hl))-Math.sin(hl*Math.PI)*170;bs=lerp(1.45,.5,hl);brot=-hl*30;}
  const pointing=inLine('23_pill2',T,0,0);
  setPill('tA',ax,ay+(hr>0?0:Math.sin(T*2.4)*4),as,{talk:aT,T,look:hr>0?1:.8,lookY:0,mood:.4,arms:hr>0?'run':(aT>.05?'wave':'down'),seed:1,rot:arot,run:hr>0&&hr<1?1:0});
  setPill('tB',bx,by+(hl>0?0:Math.sin(T*2.1+1)*4),bs,{talk:bT,T,look:hl>0?-1:-.8,lookY:0,mood:.2,arms:hl>0?'run':(pointing?'point':(bT>.05?'wave':'down')),seed:3,rot:brot,run:hl>0&&hl<1?1:0});
  show('tA',hr>=1?0:1-P(hr,.8,1)); show('tB',hl>=1?0:1-P(hl,.8,1));
}

// ================= SET F: the clinic (001's code doctor and patient, the reference's framing) =================
function renderClinic(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['30_doctor'], p2=ST['36_patient'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8)*1; if(pT>.2) pr+=Math.sin(T*7)*2; if(T>=p2-.1&&T<p2+.9) pr+=Math.sin(P(T,p2-.1,p2+.9)*Math.PI*2)*4;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  const hurt=T<d0, aha=T>=p2-.2;
  $('pBrows').setAttribute('d',aha?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':(hurt?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70'));
  setMouthV('doc_m',dT,10,.5,T,5); setMouthV('pat_m',pT,10,aha?.8:(hurt?-.6:-.1),T,6);
  setHEye('dEyeL',3,blinkK(T,.7)); setHEye('dEyeR',3,blinkK(T,.7));
  setHEye('pEyeL',-3,blinkK(T,2.1)); setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',hurt?.6:.3); show('pSweat',hurt?1:0); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  // he holds a glass of water in front of his chest the whole time
  const sh=[-84,234], el=[-110,352], wr=[-30,300+Math.sin(T*1.4)*2];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=glassAt(wr[0]+4,wr[1]-24,1.15)+hand(wr[0],wr[1],120,1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
}

function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap'); c.textContent=w;   // the reference: every word the same size, each one pops in
  const k=eo(P(T,ws,ws+.12)); c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){
  const sc=T<T_STOM?1:T<T_VEIN?2:T<T_TUN?3:T<T_CUT2?4:T<T_CLIN?1:5;
  ['s1','s2','s3','s4','s5'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  if(sc===1){renderWall(T); const shake=(T>=E.fight&&T<E.ko?Math.sin(T*70)*5:0)+(T>=E.ko&&T<E.ko+.25?Math.sin(T*90)*7:0);
    $('wWall').setAttribute('transform',`translate(${shake.toFixed(1)},0)`);}
  if(sc===2) renderStomach(T);
  if(sc===3) renderVein(T);
  if(sc===4) renderTunnels(T);
  if(sc===5) renderClinic(T);
  caption(T);
};
window.render(0);

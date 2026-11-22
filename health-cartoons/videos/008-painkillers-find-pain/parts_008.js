// =============== 008: how painkillers "find" the pain - remake of the 21M reference. ALL code, 001 / 003-v1 style. No image model. ===============
const E=D.ev, ST=D.start, END=D.end;
const KEY=/^(HUGE|CUT|BRAIN|BLOOD|PLATELETS|PAINKILLERS|PAINKILLER|MEDICINE|TALK|PAIN|STIR|SPLIT|EAST|NORTH|JOB|OURS|FOOT|HEAL|WOUND|IBUPROFEN|PROSTAGLANDINS|NERVES|SIGNALS|SIGNAL|INJURY|DOWN|NERVE)$/;
//__VISEME__
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const T_STOM=E.stom, T_VEIN=E.vein, T_FORK=E.fork, T_CUT2=E.cut2, T_CLIN=E.clinic;
// ---------- scenes ----------
let S1=`<g id="s1"><g id="cam1">${cutWorld()}</g>${brainInset()}
 ${labelBox('lbFoot','INSIDE THE FOOT',360,80,24)}${labelBox('lbCut','CUT',420,250,24)}${labelBox('lbBrain','BRAIN',500,140,22)}${labelBox('lbPg','PROSTAGLANDIN',360,700,22)}</g>`;
let S2=`<g id="s2"><g id="cam2">${stomachWorld()}</g>${labelBox('lbSto','STOMACH',560,300,24)}${labelBox('lbPk','PAINKILLERS',560,640,22)}</g>`;
let S3=`<g id="s3"><g id="cam3">${veinWorld()}</g>${labelBox('lbVein','VEIN',560,120,26)}</g>`;
let S4=`<g id="s4"><g id="cam4">${forkWorld()}</g></g>`;
let CTA=`<g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}${GDEF}</defs>`
 +S1+S2+S3+S4+S5+CTA+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;

// ---------- SCENE A / E: the cut ----------
function renderCut(T){
  const boarded=T>=T_CUT2;
  show('planks',boarded?1:0);
  // red blood cells roll along the floor (fewer once the cut is boarded up)
  [0,1,2].forEach(i=>{const per=boarded?7:4.6, ph=i*per/3, u=((T+ph)%per)/per, on=!boarded||i===0;
    show('rb'+i,on?1:0); if(!on)return; const x=lerp(-90,820,u), y=912+Math.abs(Math.sin(u*per*5))*-8;
    $('rb'+i).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${(Math.sin(T*6+i)*6).toFixed(1)}) scale(.9)`);
    setOEye('rb'+i+'_eL',13,{dx:20,dy:-6,lid:.1,blink:blinkK(T,i)}); setOEye('rb'+i+'_eR',13,{dx:20,dy:-6,lid:.1,blink:blinkK(T,i)});});
  // blood drips out of the cut and pools (before the platelets board it up)
  let dr='';if(!boarded){for(let i=0;i<4;i++){const u=((T*.8)+i/4)%1;dr+=`<path d="M${(286+i*6).toFixed(0)},${(870+u*90).toFixed(1)} c6,8 8,15 0,19 c-8,-4 -6,-11 0,-19z" fill="#d8303a" ${LN2} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}}
  const pool=boarded?1:clamp(T/6); dr+=`<ellipse cx="300" cy="986" rx="${(30+70*pool).toFixed(1)}" ry="${(8+10*pool).toFixed(1)}" fill="#c9303a" ${LN2} opacity="${boarded?.55:.9}"/>`;
  $('drips').innerHTML=dr;
  // the officer cell: walks in, sees the cut, phones the brain
  const gOn=!boarded; show('gd',gOn?1:0);
  if(gOn){const wk=eio(P(T,E.walk,E.walk+1.4)); let gx=lerp(860,520,wk), pose=T>=E.phone?'phone':'up';
    const gt=speak('guard',T), pk=popK(T,E.whoa);
    setGuard('gd',gx,804+(wk<1?Math.abs(Math.sin(T*12))*-10:Math.sin(T*2)*3)-pk*10,1.0,{talk:gt,T,pose,look:-1,mood:-.6,brows:T<E.phone?-1:1}); show('gd_sign',0);}
  // prostaglandin + the painkillers (scene E)
  const eOn=boarded; ['pg','pA','pB'].forEach(id=>show(id,eOn?1:0));
  if(eOn){
    const arr=eio(P(T,E.arrive,E.arrive+.9)), run=arr<1&&T>=E.arrive;
    const ko=T>=E.ko, inFight=T>=E.fight&&T<E.ko;
    const pgT=speak('prost',T);
    if(!inFight) setProst('pg',ko?330:360,ko?930:862+Math.sin(T*2)*4,ko?.9:.95,{talk:pgT,T,look:ko?0:1,rot:ko?-96:(pgT>.1?Math.sin(T*9)*3:0),ko,angry:T<ST['17_prost']?0:.6,mood:.2});
    show('pg',inFight?0:1);
    const aT=speak('pill',T), bT=speak('pill2',T);
    const ax=lerp(860,560,arr), bx=lerp(960,660,arr);
    const armsA=T>=E.ko?'fist':(aT>.05?'point':(run?'run':'down')), armsB=T>=E.ko?'fist':(bT>.05?'fist':(run?'run':'down'));
    if(!inFight){setPill('pA',ax,840+(run?0:Math.sin(T*3)*7),.85,{talk:aT,T,look:-1,mood:T>=E.ko?1:.6,arms:armsA,seed:1,run,angry:.5,flip:-1});
      setPill('pB',bx,846+(run?0:Math.sin(T*2.6+1)*7),.8,{talk:bT,T,look:-1,mood:T>=E.ko?1:-.2,arms:armsB,seed:3,run,angry:.8,flip:-1});}
    show('pA',inFight?0:1); show('pB',inFight?0:1);
    const fk=P(T,E.fight,E.ko); if(fk>0&&fk<1){let h='';for(let i=0;i<12;i++){const a=i/12*6.283+T*3,r=96+Math.sin(T*9+i)*20;
        h+=`<circle cx="${(470+Math.cos(a)*r).toFixed(1)}" cy="${(830+Math.sin(a)*r*.7).toFixed(1)}" r="${(62+rnd(i)*30+Math.sin(T*12+i)*8).toFixed(1)}" fill="#fff" stroke="${INK}" stroke-width="2.6"/>`;}
      h+=`<circle cx="470" cy="830" r="112" fill="#fff"/>`; $('dust').innerHTML=h;
      let s='';for(let i=0;i<5;i++){const k=((T*2.2)+i/5)%1;s+=`<path transform="translate(${(470+Math.cos(i*1.3)*k*200).toFixed(1)},${(800+Math.sin(i*1.9)*k*160).toFixed(1)}) scale(${(.6+k).toFixed(2)})" d="M0,-16 L5,-5 L16,-5 L7,2 L10,14 L0,7 L-10,14 L-7,2 L-16,-5 L-5,-5Z" fill="#ffd21f" stroke="${INK}" stroke-width="2" opacity="${(1-k).toFixed(2)}"/>`;}
      $('stars').innerHTML=s;} else {$('dust').innerHTML='';$('stars').innerHTML='';}
  } else {$('dust').innerHTML='';$('stars').innerHTML='';}
}
// setPill flip support (characters on the right face left)
const _setPill=setPill; setPill=function(id,x,y,s,o={}){_setPill(id,x,y,s,o); if(o.flip===-1){const tr0=$(id).getAttribute('transform');$(id).setAttribute('transform',tr0.replace(/scale\(([^)]+)\)/,(m,v)=>`scale(${-parseFloat(v)},${parseFloat(v)})`));}};

// ---------- SCENE B: the stomach ----------
const S_POSE={base:{L:[[176,540],[130,580],[116,646]],R:[[330,372],[380,342],[408,362]],rl:-10,rr:30},
  shrug:{L:[[176,540],[112,500],[96,450]],R:[[330,372],[400,330],[440,300]],rl:-70,rr:60},
  point:{L:[[176,540],[130,580],[116,646]],R:[[330,372],[400,420],[430,520]],rl:-10,rr:150},
  stir:{L:[[176,540],[130,580],[116,646]],R:[[330,372],[400,420],[430,470]],rl:-10,rr:100}};
function poseLerp(a,b,k){return a.map((p,i)=>[lerp(p[0],b[i][0],k),lerp(p[1],b[i][1],k)]);}
function renderStomach(T){
  const [pz,p0]=poseAt(T,[[ST['08_stomach']-.1,ST['09_pill2'],'point'],[ST['10_stomach']-.1,ST['11_pill'],'shrug'],[E.stir-.3,1e9,'stir']],'base');
  const se=speak('stomach',T), pk=popK(T,p0), P0=S_POSE[pz], k=eo(P(T,p0,p0+.22)), PB=S_POSE.base, w=Math.sin(T*3.2)*5;
  const stirring=T>=E.stir;
  const sw=stirring?[Math.cos((T-E.stir)*9)*40,Math.sin((T-E.stir)*9)*14]:[0,0];
  let R=poseLerp(PB.R,P0.R,k); if(stirring){R=[R[0],R[1],[440+sw[0],460+sw[1]]];}
  setHose('sArmL',poseLerp(PB.L,P0.L,k).map((p,i)=>i?[p[0],p[1]+w*i*.4]:p),P0.rl,1.05);
  setHose('sArmR',R.map((p,i)=>i&&!stirring?[p[0]+w*i*.3,p[1]]:p),P0.rr,1.05);
  show('stick',stirring?1:0); if(stirring) $('stick').setAttribute('transform',`translate(${(440+sw[0]).toFixed(1)},${(440+sw[1]).toFixed(1)}) rotate(${(sw[0]*.3).toFixed(1)})`);
  const asleep=T<E.wake, maskK=eio(P(T,E.wake,E.wake+.35));
  const rot=asleep?Math.sin(T*1.3)*1.2:(stirring?Math.sin(T*9)*1.2:Math.sin(T*1.1)*.6), sy=1+Math.sin(T*(asleep?1.4:2.6))*(asleep?.02:.008)+se*.018-pk*.03;
  $('stoBody').setAttribute('transform',`translate(430,850) rotate(${rot.toFixed(2)}) scale(${(1+pk*.03).toFixed(4)},${sy.toFixed(4)}) translate(-430,-850)`);
  $('sMask').setAttribute('transform',`translate(0,${(-maskK*140).toFixed(1)}) rotate(${(-maskK*12).toFixed(1)},266,440)`); show('sMask',1-P(T,E.wake+.2,E.wake+.45));
  let zz='';if(asleep){for(let i=0;i<3;i++){const u=((T*.5)+i/3)%1;zz+=`<text x="${(370+u*60).toFixed(0)}" y="${(400-u*120).toFixed(0)}" style="font-family:LG,sans-serif;font-size:${(26+u*20).toFixed(0)}px" fill="#7aa6d6" stroke="${INK}" stroke-width="2" opacity="${Math.sin(u*Math.PI).toFixed(2)}">Z</text>`;}}
  $('zzz').innerHTML=zz;
  const lookPills=T>=E.drop+.6, groggy=T<ST['07_pill'], shocked=T>=ST['08_stomach']-.1&&T<ST['09_pill2']+.5, grumpy=T>=ST['10_stomach']-.1&&T<E.stir;
  const bl=blinkK(T,.3), lid=asleep?1:(groggy?.45:(grumpy?.3:.08));
  const dx=lookPills?24:4, dy=lookPills?34:2;
  setOEye('sEyeL',36,{dx,dy,lid,blink:bl,small:shocked}); setOEye('sEyeR',36,{dx,dy,lid,blink:bl,small:shocked});
  const ang=grumpy?[16,-16,2]:(shocked?[-14,14,10]:[6,-6,6]);
  setBrow('sBrowL',224,404-(shocked?8:0),44,ang[0],ang[2]); setBrow('sBrowR',308,396-(shocked?8:0),44,ang[1],ang[2]);
  setMouthV('sto_m',se,20,asleep?.2:(grumpy?-.7:(shocked?-.3:.1)),T,3);
  // juice surface, bubbles
  let jd='M180,736';for(let x=180;x<=720;x+=20){jd+=` L${x},${(736+Math.sin(x/34+T*2.2)*5+(stirring?Math.sin(x/20+T*14)*6:0)).toFixed(1)}`;}jd+=' L720,900 L180,900Z';
  $('juiceD').setAttribute('d',jd); let jh='';for(let x=200;x<=700;x+=20){jh+=(jh?' L':'M')+`${x},${(732+Math.sin(x/34+T*2.2)*5+(stirring?Math.sin(x/20+T*14)*6:0)).toFixed(1)}`;} $('juiceH').setAttribute('d',jh);
  let bb='';const nb=stirring?16:6;for(let i=0;i<nb;i++){const u=((T*(stirring?1.4:.5))+i/nb)%1;bb+=`<circle cx="${(300+(i*37)%320+Math.sin(T*3+i)*6).toFixed(1)}" cy="${(800-u*70).toFixed(1)}" r="${(4+i%3*2)}" fill="none" ${TH(JUICE_S)} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;} $('bubbles').innerHTML=bb;
  let sw2='';if(stirring){for(let i=0;i<3;i++){const a=(T-E.stir)*8+i*2.1;sw2+=`<path d="M${(440+Math.cos(a)*70).toFixed(1)},${(770+Math.sin(a)*18).toFixed(1)} A70,18 0 0 1 ${(440+Math.cos(a+1.4)*70).toFixed(1)},${(770+Math.sin(a+1.4)*18).toFixed(1)}" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".8"/>`;}}
  $('swirl').innerHTML=sw2; show('swirl',stirring?1:0);
  // the two painkillers: drop down the food pipe, splash, talk, then dissolve as they are stirred
  [['sA',E.drop,'pill',0,412],['sB',E.drop+.22,'pill2',1,478]].forEach(([id,t0,who,i,lx])=>{const q=(T-t0)/.85; if(q<0){show(id,0);return;} show(id,1);
    const dis=stirring?P(T,E.stir+.3,E.vein-.15):0;
    let p=q<1?along(CAP_PATH,eio(q)):[lx,708+Math.sin(T*2+i)*4];
    if(stirring){const a=(T-E.stir)*7+i*3.1;p=[lerp(p[0],440+Math.cos(a)*60,P(T,E.stir,E.stir+.3)),lerp(p[1],750+Math.sin(a)*14,P(T,E.stir,E.stir+.3))];}
    setPill(id,p[0],p[1],.4*(1-dis*.85),{talk:speak(who,T),T,look:i?-.6:.6,lookY:-.8,mood:.6,arms:speak(who,T)>.05?'wave':'down',seed:i*2,rot:q<1?Math.sin(q*9)*30:(stirring?(T-E.stir)*300:0)});
    $(id).setAttribute('opacity',(1-dis).toFixed(2));});
}
// ---------- SCENE C: the vein ----------
function renderVein(T){
  const u=P(T,T_VEIN-.1,T_FORK+.1);
  const path=[[-160,1000],[120,900],[300,760],[420,640],[560,520],[720,430],[900,350]];
  [['vA',0,'pill'],['vB',.12,'pill2']].forEach(([id,o,who],i)=>{const p=along(path,clamp(u*1.05-o+.05));setPill(id,p[0],p[1]+Math.sin(T*10+i)*6,.62,{T,look:1,lookY:-.4,mood:1,arms:'fist',seed:i,rot:-30});});
  [0,1].forEach(i=>{const p=along(path,clamp(u*1.2-.2-i*.35));$('vr'+i).setAttribute('transform',`translate(${p[0].toFixed(1)},${(p[1]+40).toFixed(1)}) rotate(${(T*200+i*90)%360}) scale(.7)`);});
  let sl='';for(let i=0;i<8;i++){const k=((T*3)+i/8)%1;const p=along(path,clamp(u-.1-k*.15));sl+=`<path d="M${(p[0]-60).toFixed(0)},${(p[1]+30+(i%3-1)*34).toFixed(0)} l-70,36" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity="${(1-k).toFixed(2)}"/>`;}
  $('speed').innerHTML=sl;
}
// ---------- SCENE D: the fork ----------
function renderFork(T){
  $('holes').setAttribute('transform',`translate(360,520) scale(${(1+.025*Math.sin(T*2.2)).toFixed(4)},${(1+.02*Math.sin(T*2.2+1)).toFixed(4)}) translate(-360,-520)`);
  let spk='';for(let i=0;i<10;i++){const u=((T*.12)+i/10)%1;spk+=`<circle cx="${(60+(i*71)%600+Math.sin(T*1.3+i)*20).toFixed(1)}" cy="${(880-u*700).toFixed(1)}" r="${(3+i%3*2)}" fill="#fff" opacity="${(.6*Math.sin(u*Math.PI)).toFixed(2)}"/>`;} $('specks').innerHTML=spk;
  const aT=speak('pill',T), bT=speak('pill2',T), sp=eio(P(T,E.split,E.split+1.0)), run=T>=E.split;
  const ax=lerp(428,620,sp), bx=lerp(286,100,sp), sc=1-.45*sp, y=lerp(900,760,sp);
  const looking=T>=ST['13_pill2']-.1&&T<ST['14_pill'];
  const bobA=run?0:Math.sin(T*3.1)*8, bobB=run?0:Math.sin(T*2.7+1)*8;
  setPill('fA',ax,y+bobA,1.05*sc,{talk:aT,T,look:run?1:(looking?Math.sin(T*2):-.8),mood:.6,arms:run?'run':(aT>.05?(T>=ST['15_pill']?'point':'wave'):'down'),seed:1,run,flip:run?1:1});
  setPill('fB',bx,y+6+bobB,1.0*sc,{talk:bT,T,look:run?-1:(looking?Math.sin(T*2.4+1):.8),mood:-.2,arms:run?'run':(bT>.05?'wave':'down'),seed:3,run,flip:run?-1:1});
  if(run){$('fB').setAttribute('opacity',(1-P(T,E.split+.7,E.split+1.0)).toFixed(2));$('fA').setAttribute('opacity',(1-P(T,E.split+.7,E.split+1.0)).toFixed(2));}
  else {$('fB').setAttribute('opacity',1);$('fA').setAttribute('opacity',1);}
}
// ---------- the clinic (001's code doctor + patient) ----------
function renderClinic(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['20_doctor'], pa=ST['19_patient'], p2=ST['21_patient'];
  let dr=2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,dr);
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8)*1; if(T>=d0&&T<p2&&dT<.05) pr+=Math.sin(T*9)*1.5*(speak('doctor',T-.25)>.1?1:0);
  if((T<d0||T>=p2)&&pT>.2) pr+=Math.sin(T*7)*2;
  if(T>=p2-.1&&T<p2+.9) pr+=Math.sin(P(T,p2-.1,p2+.9)*Math.PI*2)*4;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  const hurt=T<E.prost, aha=T>=p2-.2;
  $('pBrows').setAttribute('d',aha?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':(hurt?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70'));
  setMouthV('doc_m',dT,10,.7,T,5); setMouthV('pat_m',pT,10,aha?.8:(hurt?-.6:.1),T,6);
  setHEye('dEyeL',3,blinkK(T,.7)); setHEye('dEyeR',3,blinkK(T,.7));
  setHEye('pEyeL',-3,blinkK(T,2.1)); setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',hurt?.6:.3); show('pSweat',hurt?1:0); $('pSweat').setAttribute('transform',`translate(46,${(70+((T*14)%24)).toFixed(1)})`);
  // left hand holds the glass of water: up while he asks, then down
  const up=eio(P(T,pa-.4,pa+.3)), down=eio(P(T,d0+.2,d0+1.0));
  const sh=[-84,234], el=[lerp(lerp(-102,-124,up),-102,down),lerp(lerp(370,344,up),370,down)], wr=[lerp(lerp(-90,-44,up),-90,down),lerp(lerp(470,286,up),470,down)];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  const ha=lerp(lerp(-8,150,up),-8,down), gy=wr[1]+(down>.5?12:0);
  $('patHandL').innerHTML=glassAt(wr[0]+2,gy-22,1.15)+hand(wr[0],gy,ha,1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  $('clkM').setAttribute('transform',`rotate(${T*6})`);
  // camera: push in on his question, punch in on the doctor at "prostaglandins"
  const pq=eio(P(T,pa,pa+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,END)+.07*pq, cx=lerp(360,430,pq), cy=lerp(640,600,pq);
  const pk=eio(P(T,E.prost-.15,E.prost+.15))*(1-eio(P(T,E.brainW-.6,E.brainW-.25)));
  z=lerp(z,1.42,pk); cx=lerp(cx,232,pk); cy=lerp(cy,430,pk);
  const ty=lerp(640,560,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // thought bubbles cut on his words: "...to your brain" -> the painkillers knock out the prostaglandin; "never went looking" -> the fork
  const sA=E.brainW-.3, sB=E.looking-.15, sE=E.down-.3, bOn=T>=sA&&T<sE;
  $('bub').setAttribute('opacity',bOn?1:0);
  if(bOn){const seg=T<sB?0:1, t0=[sA,sB][seg], t1=[sB,sE][seg], u=P(T,t0,t1);
    const pop=seg===0?eob(P(T,sA,sA+.3)):1+.06*Math.sin(clamp(P(T,t0,t0+.25))*Math.PI);
    $('bub').setAttribute('transform',`translate(300,178) scale(${(1.38*pop).toFixed(3)}) translate(-265,-150)`);
    show('bubA',seg===0?1:0); show('bubB',seg===1?1:0);
    if(seg===0) renderCut(lerp(E.fight-.4,E.ko+.25,u)); else renderFork(lerp(ST['13_pill2'],E.split+.9,u));}
  popLabel('lbPro',T,E.prost-.05,E.brainW-.35,360,64);
  popLabel('lbTip',T,E.down-.15,END,360,84);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z'\-]/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_STOM?1:T<T_VEIN?2:T<T_FORK?3:T<T_CUT2?4:T<T_CLIN?1:5;
  ['s1','s2','s3','s4','s5'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  const bounds=[[0,T_STOM],[T_STOM,T_VEIN],[T_VEIN,T_FORK],[T_FORK,T_CUT2],[T_CUT2,T_CLIN],[T_CLIN,END]];
  const seg=bounds.find(([a,b])=>T>=a&&T<b)||bounds[5];
  const dark=Math.max(seg[0]>0?1-P(T,seg[0],seg[0]+.14):0, seg[1]<END?P(T,seg[1]-.14,seg[1]):0);
  if(sc===1){renderCut(T);
    const pz=eob(P(T,E.whoa,E.whoa+.25))*(1-P(T,E.whoa+1.2,E.whoa+1.8)), fight=T>=E.fight&&T<E.ko;
    const shake=(fight?.6:0)*Math.sin(T*70)*7+(T>=E.ko&&T<E.ko+.3?Math.sin(T*90)*8:0);
    const pe=T>=T_CUT2?eio(P(T,T_CUT2,E.fight)):0, z=1+.08*pz+.14*pe+.01*Math.sin(T*.3), cx=lerp(lerp(360,300,pz),470,pe), cy=lerp(lerp(640,600,pz),760,pe); $('cam1').setAttribute('transform',`translate(${(360+shake).toFixed(1)},640) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)},${(-cy).toFixed(1)})`);
    // brain on the phone
    const bOn=T>=E.brainUp&&T<T_STOM, bk=eob(P(T,E.brainUp,E.brainUp+.3)); show('bInset',bOn?1:0);
    if(bOn){$('bInset').setAttribute('transform',`translate(500,330) scale(${bk.toFixed(3)})`); const bt=speak('brain',T);
      setOEye('brEyeL',20,{dx:-14,dy:4,lid:.35,blink:blinkK(T,.5)}); setOEye('brEyeR',20,{dx:-14,dy:4,lid:.35,blink:blinkK(T,.5)}); setMouthV('brain_m',bt,12,.3,T,8);
      let wv='';if(bt>.1||speak('guard',T)>.1){for(let i=0;i<3;i++){const k=((T*2)+i/3)%1;wv+=`<path d="M${(-150-k*40).toFixed(0)},${(-20-k*30).toFixed(0)} q-14,20 0,40" fill="none" stroke="#ffd21f" stroke-width="5" stroke-linecap="round" opacity="${(1-k).toFixed(2)}"/>`;}} $('waves').innerHTML=wv;}
    popLabel('lbFoot',T,.3,2.8,360,80); popLabel('lbCut',T,E.whoa+.1,E.whoa+2.2,420,250); popLabel('lbBrain',T,E.brainUp+.2,T_STOM-.2,500,140);
    popLabel('lbPg',T,ST['17_prost']-.25,ST['18_pill2'],360,700);}
  if(sc===2){renderStomach(T); let zz=0,n=0;for(let i=0;i<=14;i++){const t=T-.7+i*.05;zz+=(speak('pill',t)>.02||speak('pill2',t)>.02||D.lines.some(l=>(l.who==='pill'||l.who==='pill2')&&t>=l.t0-.1&&t<l.t0+l.dur+.2&&l.t0<E.stir))?1:0;n++;}
    const k=eio(zz/n), z=1+.32*k+.01*Math.sin(T*.3), cx=lerp(360,440,k), cy=lerp(640,690,k);
    $('cam2').setAttribute('transform',`translate(360,640) scale(${z.toFixed(4)}) translate(${(-cx).toFixed(1)},${(-cy).toFixed(1)})`);
    popLabel('lbSto',T,ST['06_stomach']+.1,ST['06_stomach']+2.2,560,300); popLabel('lbPk',T,ST['07_pill']-.05,ST['07_pill']+2.2,600,620);}
  if(sc===3){renderVein(T); popLabel('lbVein',T,T_VEIN+.1,T_FORK,560,120);}
  if(sc===4){renderFork(T); const z=1+.12*eio(P(T,T_FORK,E.split))+.01*Math.sin(T*1.7); $('cam4').setAttribute('transform',`translate(360,640) scale(${z.toFixed(4)}) translate(-360,-700)`);}
  if(sc===5) renderClinic(T);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0); $('cta').setAttribute('transform',`translate(360,${250+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
  show('indark',dark*.9);
  caption(T);
};
window.render(0);

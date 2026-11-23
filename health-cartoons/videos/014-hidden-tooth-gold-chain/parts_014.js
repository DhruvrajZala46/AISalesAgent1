// =============== 014 v2: the hidden tooth and the gold chain. The reference's scenes and order; our characters and words. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
let S1=`<g id="s1"><g id="cam" transform="translate(360,640) scale(1.1) translate(-360,-545)">${mouthWorld()}</g></g>`;
let SL=`<g id="sL"><rect x="-10" y="-10" width="740" height="1300" fill="#0b0b0d"/><text id="later" x="360" y="660" text-anchor="middle" style="font-family:LG,sans-serif;font-size:76px;letter-spacing:2px" fill="#ffd23a">LATER...</text></g>`;
let S3=`<g id="s3">${clinic14()}</g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S3+SL+`<text id="wm" x="360" y="64" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".55">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

function canPos(T){const tug=T>=E.tug?Math.pow(Math.abs(Math.sin((T-E.tug)*Math.PI/.7)),3)*(T<E.hook+1.2?1:.45):0,pre=T>=E.tug?Math.min(1,(T-E.tug)/9)*30:0;
  return {x:GAP+6,y:250+pre+tug*9,rot:24-pre*.25,tug};}
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}

function renderMouth(T){
  const opened=T>=E.open,k0=P(T,E.open,E.open+.35),c=canPos(T),chained=T>=E.chain,pulling=T>=E.tug,hooked=T>=E.hook;
  // the cut: a red glow on the gum, the scalpel working round it, then the gum opens
  const gl=opened?0:.55+.45*Math.sin(T*9);
  $('glow').innerHTML=opened?'':`<ellipse cx="${GAP}" cy="250" rx="${(118+gl*8).toFixed(1)}" ry="${(136+gl*8).toFixed(1)}" fill="none" stroke="#ff3b4e" stroke-width="9" opacity="${(.35+.4*gl).toFixed(2)}"/><ellipse cx="${GAP}" cy="250" rx="104" ry="122" fill="none" stroke="${INK}" stroke-width="3" stroke-dasharray="12 9"/>`;
  $('flap').setAttribute('transform',`translate(${GAP},132) rotate(${(-k0*14).toFixed(1)}) scale(${(1-.25*eo(k0)).toFixed(3)},${lerp(1,-.32,eo(k0)).toFixed(3)}) translate(${-GAP},-132)`);
  show('pocket',opened?1:0);show('can',opened?1:0);
  const a=lerp(-1.3,1.5,P(T,-.9,E.open-.05)),sx=GAP+Math.cos(a)*104,sy=250+Math.sin(a)*122,out=eio(P(T,E.open-.05,E.open+.5));
  $('scalpel').setAttribute('transform',`translate(${(sx+out*330).toFixed(1)},${(sy-out*420+Math.sin(T*30)*2).toFixed(1)}) rotate(${(8+Math.sin(T*7)*5).toFixed(1)})`);show('scalpel',out<1?1:0);
  let fx=!opened?[0,1,2].map(j=>{const f=((T*3+j/3)%1);return `<path d="M${(sx-8-f*26*(j-1)).toFixed(1)},${(sy+4+f*22).toFixed(1)} l-6,10" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="${(1-f).toFixed(2)}"/>`;}).join(''):'';
  // the canine
  $('can').setAttribute('transform',`translate(${c.x.toFixed(1)},${c.y.toFixed(1)}) rotate(${c.rot.toFixed(1)})`);
  const cT=speak('can',T);
  let cf={dx:0,dy:10,lid:.8,bA:0,arch:2,mood:-.1,small:false,blink:T<E.chain-.3?1:blinkK(T,1.1)};            // found: eyes still shut
  if(chained)cf={dx:0,dy:34,lid:.05,bA:-10,arch:8,mood:-.3,small:false,blink:blinkK(T,1.1)};
  if(pulling)cf={dx:Math.sin(T*9)*8,dy:22,lid:0,bA:-18,arch:7,mood:-.9,small:true,blink:0};
  if(T>=ST['04_tl']-.1)cf={dx:-20,dy:26,lid:.05,bA:-12,arch:6,mood:-.6,small:false,blink:blinkK(T,1.1)};
  if(T>=ST['05_can']-.1)cf={dx:Math.sin((T-ST['05_can'])*4)*26,dy:16,lid:0,bA:-14,arch:8,mood:-.6,small:true,blink:0};
  if(T>=ST['06_tr']-.1)cf={dx:22,dy:28,lid:.08,bA:-8,arch:6,mood:-.3,small:false,blink:blinkK(T,1.1)};
  face('c',19,{...cf,bx:22,by:-70,bw:24,talk:cT,mw:12,T,seed:7});
  // the button, the chain and the tweezers that pull it down to the wire
  const kb=P(T,E.chain-.6,E.chain-.05),bOn=T>=E.chain-.05;show('btn',bOn?1:0);show('cBrk',0);
  const r=c.rot*Math.PI/180,bxw=c.x-Math.sin(r)*60,byw=c.y+Math.cos(r)*60;
  const kc=eio(P(T,E.tug,E.hook)),sw=Math.sin(T*5)*10*(1-kc);
  const ex=lerp(bxw+sw,GAP,kc),ey=lerp(byw+86,WIRE,kc);
  let tw=null;
  if(kb>0&&T<E.chain+.45){const kk=eo(kb),away=eio(P(T,E.chain+.05,E.chain+.45));tw=[bxw+(1-kk)*260+away*300,byw-(1-kk)*330-away*380];
    if(!bOn)fx+=`<circle cx="${tw[0].toFixed(1)}" cy="${tw[1].toFixed(1)}" r="14" fill="${C_GOLD}" ${OLW2}/>`;}
  if(T>=E.tug-.5&&T<E.hook+.5){const inK=eo(P(T,E.tug-.5,E.tug-.05)),away=eio(P(T,E.hook+.08,E.hook+.5));tw=[ex+(1-inK)*300+away*320,ey-(1-inK)*200-away*300];}
  show('tweez',tw?1:0);if(tw)$('tweez').setAttribute('transform',`translate(${tw[0].toFixed(1)},${tw[1].toFixed(1)})`);
  if(chained){const drop=eo(P(T,E.chain,E.chain+.35)),x2=lerp(bxw,ex,drop),y2=lerp(byw,ey,drop),taut=hooked?c.tug*-3:0;
    const d=`M${bxw.toFixed(1)},${byw.toFixed(1)} Q${((bxw+x2)/2+(hooked?taut:10*(1-kc))).toFixed(1)},${((byw+y2)/2).toFixed(1)} ${x2.toFixed(1)},${y2.toFixed(1)}`;['chO','chG','chH'].forEach(id=>{$(id).setAttribute('d',d);show(id,1);});}
  else ['chO','chG','chH'].forEach(id=>show(id,0));
  if(pulling&&c.tug>.5)fx+=`<path d="M${c.x-78},${c.y-30} l-16,-8 M${c.x-80},${c.y} l-18,0 M${c.x+78},${c.y-30} l16,-8 M${c.x+80},${c.y} l18,0" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>`;
  $('fx').innerHTML=fx;$('zz').innerHTML='';show('sign',0);
  // the neighbours
  const lT=speak('tl',T),rT=speak('tr',T),jig=hooked?c.tug*2:0;
  const look=(x)=>{const dx=c.x-x,dy=c.y-80-(UTOP+80),m=Math.hypot(dx,dy)||1;return [dx/m*30,dy/m*30];};
  const [lx,ly]=look(205),[rx,ry]=look(515);
  $('t205').setAttribute('transform',`translate(205,${(UTOP+jig).toFixed(1)}) rotate(${(lT>.3?Math.sin(T*8)*1.5:0).toFixed(2)})`);
  $('t515').setAttribute('transform',`translate(515,${(UTOP-jig).toFixed(1)}) rotate(${(rT>.3?Math.sin(T*8+1)*1.5:0).toFixed(2)})`);
  const early=T<ST['02_tr'];
  face('t205',22,{dx:lx,dy:ly,lid:early?0:.08,blink:blinkK(T,.4),small:T<E.open+.5,bx:27,by:48-(early?6:0),bw:28,bA:early?-10:(inL('04_tl',T)?-4:0),arch:6,talk:lT,mw:13,mood:early?-.3:(inL('04_tl',T)?.4:.1),T,seed:1});
  const calm=T>=ST['06_tr']-.1;
  face('t515',22,{dx:rx,dy:ly,lid:calm?.3:.05,blink:blinkK(T,2.3),small:T<E.open+.4,bx:27,by:48-(inL('02_tr',T)?7:0),bw:28,bA:calm?-3:-8,arch:calm?7:6,talk:rT,mw:13,mood:calm?.8:-.1,T,seed:2});
  [55,665].forEach(x=>{const [px,py]=look(x);['L','R'].forEach((sd,i)=>{const e=$('t'+x+'_p'+sd);e.setAttribute('cx',((i?24:-24)+px*.22).toFixed(1));e.setAttribute('cy',(84+py*.22).toFixed(1));});});
}
// ---------- the clinic: our doctor, our patient in the dental chair ----------
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['08_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,4+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.5,T,5);setHEye('dEyeL',4,blinkK(T,.7));setHEye('dEyeR',4,blinkK(T,.7));
  const ar=-58+(dT>.2?Math.sin(T*4.2)*5*dT:Math.sin(T*1.6)*1.5);
  $('docArmR').setAttribute('transform',`rotate(${ar.toFixed(2)},86,226)`);
  const q=ar*Math.PI/180,hx=86+(98-86)*Math.cos(q)-(350-226)*Math.sin(q),hy=226+(98-86)*Math.sin(q)+(350-226)*Math.cos(q);
  $('mirror').setAttribute('transform',`translate(${(150+hx).toFixed(1)},${(338+hy).toFixed(1)}) rotate(${(ar+50).toFixed(1)})`);
  let pr=-4+Math.sin(T*.8)*1;if(pT>.2)pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  $('pBrows').setAttribute('d',T<d0?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  setMouthV('pat_m',pT,10,T<d0?-.5:-.1,T,6);setHEye('pEyeL',-4,blinkK(T,2.1));setHEye('pEyeR',-4,blinkK(T,2.1));
  show('patBlush',.5);show('pSweat',0);
  const sh=[-84,234],el=[-112,330],wr=[-86,420];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+8,10,1.2,PSK);
  $('patWrap').setAttribute('transform',`translate(0,${(Math.sin(T*1.2)*1.2).toFixed(2)})`);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){
  const sc=T<E.later?1:(T<E.clinic?2:3);
  $('s1').setAttribute('display',sc===1?'inline':'none');$('sL').setAttribute('display',sc===2?'inline':'none');$('s3').setAttribute('display',sc===3?'inline':'none');
  show('wm',sc===2?0:.55);
  if(sc===1)renderMouth(T);if(sc===3)renderClinic(T);
  if(sc===2){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  caption(T);};
window.render(0);

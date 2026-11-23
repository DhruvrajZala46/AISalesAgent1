// =============== 014: "Why did the dentist put a gold chain on this tooth?" One set: the mouth. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
let S1=`<g id="s1"><g id="cam">${mouthWorld()}</g>
 ${labelBox('lbCan','IMPACTED CANINE',470,150,25)}${labelBox('lbBtn','BUTTON',190,560,25)}${labelBox('lbChain','GOLD CHAIN',540,760,25)}${labelBox('lbBr','BRACES',150,560,25)}
 <text id="month" opacity="0" x="430" y="170" text-anchor="middle" style="font-family:LG,sans-serif;font-size:66px;letter-spacing:1px;paint-order:stroke" fill="#ffd23a" stroke="${INK}" stroke-width="9" stroke-linejoin="round"></text>
 ${docBubble()}</g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+`<text id="wm" x="360" y="64" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".55">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

const MAIN=[1.3,360,430], CAN=[1.9,360,290], TL=[1.15,360,470];
const CAM=[[0,...MAIN,0],[E.canCam,...CAN,.4],[ST['04_tl']-.1,...MAIN,.35],[E.chain-.55,...CAN,.4],[ST['07_tr']-.1,...MAIN,.35],[ST['08_can']-.1,...CAN,.3],[E.seat,1.55,330,520,.4],
  [E.doc,...CAN,.4],[ST['12_doctor']-.1,...MAIN,.4],[E.tl0,...TL,.5]];
function camAt(T){let s=CAM[0][1],x=CAM[0][2],y=CAM[0][3];for(let i=1;i<CAM.length;i++){const [t,ks,kx,ky,d]=CAM[i];if(T<t)break;const k=eio(P(T,t,t+d));s=lerp(s,ks,k);x=lerp(x,kx,k);y=lerp(y,ky,k);}return [s,x,y];}

// where the canine is: asleep in its pocket, tugged a little, then pulled down over twelve months
function canPos(T){const k=eio(P(T,E.tl0+.2,E.tl1)),tug=T>=E.tug&&T<E.tl0?Math.pow(Math.abs(Math.sin((T-E.tug)*Math.PI/.55)),3):0;
  const pre=T>=E.tug?Math.min(1,(T-E.tug)/6)*26:0;
  let y=lerp(250+pre+tug*9,575,k),rot=lerp(24-pre*.2,0,k),x=lerp(GAP+6,GAP,k);
  const land=T>=E.tl1?Math.exp(-(T-E.tl1)*9)*Math.cos((T-E.tl1)*24):0;
  return {x,y:y+(k>=1?0:0),rot,k,tug,sy:1-.1*land,sx:1+.07*land};}
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}

function renderMouth(T){
  const opened=T>=E.open,k0=P(T,E.open,E.open+.35),c=canPos(T),chained=T>=E.chain,pulling=T>=E.tug,seated=T>=E.tl1;
  // the cut: a red glow on the gum, the scalpel working round it, then the flap lifts
  const gl=opened?0:.55+.45*Math.sin(T*9);
  $('glow').innerHTML=opened?'':`<ellipse cx="${GAP}" cy="250" rx="${(118+gl*8).toFixed(1)}" ry="${(136+gl*8).toFixed(1)}" fill="none" stroke="#ff3b4e" stroke-width="9" opacity="${(.35+.4*gl).toFixed(2)}"/><ellipse cx="${GAP}" cy="250" rx="104" ry="122" fill="none" stroke="${INK}" stroke-width="3" stroke-dasharray="12 9"/>`;
  $('flap').setAttribute('transform',`translate(${GAP},132) rotate(${(-k0*14).toFixed(1)}) scale(${(1-.25*eo(k0)).toFixed(3)},${lerp(1,-.32,eo(k0)).toFixed(3)}) translate(${-GAP},-132)`);
  show('pocket',opened?1:0);show('can',opened?1:0);
  const a=lerp(-1.2,1.5,P(T,-.5,E.open-.1)),sx=GAP+Math.cos(a)*104,sy=250+Math.sin(a)*122,out=eio(P(T,E.open-.1,E.open+.45));
  $('scalpel').setAttribute('transform',`translate(${(sx+out*330).toFixed(1)},${(sy-out*420+Math.sin(T*30)*2).toFixed(1)}) rotate(${(8+Math.sin(T*7)*5).toFixed(1)})`);show('scalpel',out<1?1:0);
  $('fx').innerHTML=!opened?[0,1,2].map(j=>{const f=((T*3+j/3)%1);return `<path d="M${(sx-8-f*26*(j-1)).toFixed(1)},${(sy+4+f*22).toFixed(1)} l-6,10" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="${(1-f).toFixed(2)}"/>`;}).join(''):'';
  // the canine
  $('can').setAttribute('transform',`translate(${c.x.toFixed(1)},${c.y.toFixed(1)}) rotate(${c.rot.toFixed(1)}) scale(${c.sx.toFixed(3)},${c.sy.toFixed(3)})`);
  const cT=speak('can',T),asleep=T<ST['03_can']-.1,dozy=T<ST['04_tl']+.6;
  let cf={dx:0,dy:20,lid:.15,bA:0,arch:3,mood:0,small:false};
  if(dozy)cf={dx:0,dy:14,lid:.72,bA:0,arch:2,mood:-.1,small:false};
  if(T>=ST['04_tl']+.6)cf={dx:-18,dy:22,lid:.1,bA:-6,arch:6,mood:-.2,small:false};
  if(chained)cf={dx:0,dy:34,lid:0,bA:-10,arch:8,mood:-.3,small:false};
  if(pulling)cf={dx:Math.sin(T*9)*8,dy:20,lid:0,bA:-16,arch:7,mood:-.8,small:true};
  if(T>=ST['07_tr']-.1)cf={dx:22,dy:24,lid:.1,bA:-10,arch:5,mood:-.4,small:false};
  if(T>=E.seat)cf={dx:-16,dy:30,lid:.1,bA:-4,arch:6,mood:.1,small:false};
  if(T>=E.doc)cf={dx:0,dy:8,lid:.12,bA:0,arch:4,mood:.1,small:false};
  if(T>=E.tl0)cf={dx:0,dy:30,lid:.05,bA:8,arch:6,mood:.6,small:false};
  if(seated)cf={dx:0,dy:0,lid:0,bA:-6,arch:10,mood:1,small:false};
  face('c',19,{...cf,blink:asleep?1:blinkK(T,1.1),bx:22,by:-70,bw:24,talk:cT,mw:11,T,seed:7});
  $('zz').innerHTML=(opened&&asleep)?[0,1,2].map(j=>{const f=((T*.8+j/3)%1);return `<text x="${(GAP+70+f*46).toFixed(0)}" y="${(190-f*70).toFixed(0)}" style="font-family:LG,sans-serif;font-size:${(22+f*20).toFixed(0)}px" fill="#fff" stroke="${INK}" stroke-width="1.6" opacity="${(1-f).toFixed(2)}">Z</text>`;}).join(''):'';
  // button, chain, tweezers
  const kb=P(T,E.chain-.6,E.chain-.05),bOn=T>=E.chain-.05;show('btn',bOn&&!seated?1:0);show('cBrk',seated?1:0);
  if(seated)$('cBrk').setAttribute('transform',`translate(0,58) scale(${eob(P(T,E.tl1,E.tl1+.25)).toFixed(3)}) translate(0,-58)`);
  const r=c.rot*Math.PI/180,bxw=c.x-Math.sin(r)*60,byw=c.y+Math.cos(r)*60;
  show('tweez',kb>0&&T<E.chain+.5?1:0);
  if(kb>0){const kk=eo(kb),away=eio(P(T,E.chain+.05,E.chain+.5));$('tweez').setAttribute('transform',`translate(${(bxw+(1-kk)*260+away*300).toFixed(1)},${(byw-(1-kk)*330-away*380).toFixed(1)})`);}
  if(kb>0&&!bOn)$('fx').innerHTML=`<circle cx="${(bxw+(1-eo(kb))*260).toFixed(1)}" cy="${(byw-(1-eo(kb))*330).toFixed(1)}" r="14" fill="${C_GOLD}" ${OLW2}/>`;
  const kc=eo(P(T,E.chain,E.chain+.4)),chOn=chained&&!seated;
  if(chOn){const ex=lerp(bxw,GAP,kc),ey=lerp(byw,WIRE,kc),sag=pulling?c.tug*-4:(1-P(T,E.chain+.4,E.tug))*0+18;
    const d=`M${bxw.toFixed(1)},${byw.toFixed(1)} Q${((bxw+ex)/2+(pulling?0:sag)).toFixed(1)},${((byw+ey)/2).toFixed(1)} ${ex.toFixed(1)},${ey.toFixed(1)}`;['chO','chG','chH'].forEach(id=>{$(id).setAttribute('d',d);show(id,1);});}
  else ['chO','chG','chH'].forEach(id=>show(id,0));
  // the neighbours
  const lT=speak('tl',T),rT=speak('tr',T),jig=pulling&&T<E.tl0?c.tug*2:0,cheer=seated?Math.abs(Math.sin((T-E.tl1)*9))*10:0;
  const look=(x)=>{const dx=c.x-x,dy=c.y-80-(UTOP+80),m=Math.hypot(dx,dy)||1;return [dx/m*30,dy/m*30];};
  const [lx,ly]=look(205),[rx,ry]=look(515);
  $('t205').setAttribute('transform',`translate(205,${(UTOP-cheer+jig).toFixed(1)}) rotate(${(lT>.3?Math.sin(T*8)*1.5:0).toFixed(2)})`);
  $('t515').setAttribute('transform',`translate(515,${(UTOP-cheer*.8-jig).toFixed(1)}) rotate(${(rT>.3?Math.sin(T*8+1)*1.5:0).toFixed(2)})`);
  const lAnn=inL('04_tl',T),lHappy=T>=E.seat&&T<E.doc||seated;
  face('t205',22,{dx:lx,dy:ly,lid:lAnn?.3:(T<E.open+1?0:.08),blink:blinkK(T,.4),small:T<E.open+.4,bx:27,by:48-(T<E.open+1?6:0),bw:28,bA:lAnn?12:(T<E.open+1?-10:(lHappy?-4:0)),arch:lAnn?2:6,talk:lT,mw:13,mood:lAnn?-.5:(lHappy?.9:(T<E.open+1?-.5:.2)),T,seed:1});
  const rAm=T>=ST['07_tr']-.1&&T<E.seat;
  face('t515',22,{dx:rx,dy:ry,lid:rAm?.32:(T<E.open?0:.08),blink:blinkK(T,2.3),small:T<E.open+.2||inL('02_tr',T,0,-1.6),bx:27,by:48-(inL('02_tr',T)?7:0),bw:28,bA:rAm?-3:(T<ST['03_can']?-10:0),arch:rAm?7:6,talk:rT,mw:13,mood:rAm?.8:(seated?.95:(T<ST['03_can']?-.3:.2)),T,seed:2});
  [55,665].forEach(x=>{const [px,py]=look(x);['L','R'].forEach((sd,i)=>{const e=$('t'+x+'_p'+sd);e.setAttribute('cx',((i?24:-24)+px*.22).toFixed(1));e.setAttribute('cy',(84+py*.22).toFixed(1));});
    $('t'+x).setAttribute('transform',`translate(${x},${(UTOP-cheer*.6).toFixed(1)})`);});
  // the RESERVED sign on the empty seat
  const sOn=T>=E.seat+.5&&c.k<.55;show('sign',sOn?1:0);if(sOn)$('sign').setAttribute('transform',`translate(${GAP},${540+Math.sin(T*3)*3}) rotate(${Math.sin(T*2.2)*4}) scale(${eob(P(T,E.seat+.5,E.seat+.8)).toFixed(3)})`);
  // sparkles when it lands
  if(seated){$('fx').innerHTML=[[270,470,0],[452,500,1],[300,690,2],[430,700,3],[360,430,4]].map(([x,y,j])=>{const kk=.5+.5*Math.sin(T*8+j*1.9),rr=9+11*kk;
    return `<path d="M${x},${y-rr} Q${x+2},${y-2} ${x+rr},${y} Q${x+2},${y+2} ${x},${y+rr} Q${x-2},${y+2} ${x-rr},${y} Q${x-2},${y-2} ${x},${y-rr}Z" fill="#fff8c9" stroke="${INK}" stroke-width="2" opacity="${(.5+.5*kk).toFixed(2)}"/>`;}).join('');}
  else if(opened&&!(kb>0&&!bOn))$('fx').innerHTML=pulling&&T<E.tl0&&c.tug>.5?`<path d="M${c.x-78},${c.y-30} l-16,-8 M${c.x-80},${c.y} l-18,0 M${c.x+78},${c.y-30} l16,-8 M${c.x+80},${c.y} l18,0" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".9"/>`:'';
  const [s,ccx,ccy]=camAt(T);$('cam').setAttribute('transform',`translate(360,640) scale(${s.toFixed(4)}) translate(${(-ccx).toFixed(2)},${(-ccy).toFixed(2)})`);
  popLabel('lbCan',T,E.lbCan,ST['11_doctor']-.1,470,160);popLabel('lbBtn',T,E.lbBtn,ST['12_doctor']-.1,182,618);popLabel('lbChain',T,E.lbChain,ST['12_doctor']-.1,548,820);popLabel('lbBr',T,E.lbBr,E.tl0-.1,566,842);
  const mOn=T>=E.tl0+.2;show('month',mOn?1:0);
  if(mOn){const m=seated?12:1+Math.min(11,Math.floor(P(T,E.tl0+.2,E.tl1)*12)),t0=E.tl0+.2+(m-1)*(E.tl1-E.tl0-.2)/12,kk=seated?1+.05*Math.sin(T*10):lerp(1.35,1,eo(P(T,t0,t0+.14)));
    $('month').textContent='MONTH '+m;$('month').setAttribute('transform',`translate(430,150) scale(${kk.toFixed(3)}) translate(-430,-150)`);}
}
function renderDoc(T){
  const on=T>=E.doc;show('docB',on?1:0);if(!on)return;
  const k=eob(P(T,E.doc,E.doc+.3));$('docB').setAttribute('transform',`translate(122,196) scale(${k.toFixed(3)})`);
  const dT=speak('doctor',T);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.5,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
window.render=function(T){renderMouth(T);renderDoc(T);caption(T);};
window.render(0);

// =============== 019: "How picking your nose makes it bleed". Inside the nose, the nose from the front, the pinch, the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${insideNose()}${labelBox('lbM','DRY MUCUS',150,640,24)}${labelBox('lbV','TINY BLOOD VESSELS',560,214,22)}${labelBox('lbS','SCRATCH!',600,380,30)}${labelBox('lbB','IT BLEEDS',596,380,28)}</g>`,
 S2=`<g id="s2">${frontNose()}${labelBox('lbW','STILL BLEEDING!',360,300,30)}${labelBox('lbT','TISSUE',190,1010,26)}</g>`,
 S3=`<g id="s3">${profile()}${labelBox('lbL','1. LEAN FORWARD',205,880,30)}${labelBox('lbP','2. PINCH THE SOFT PART',205,956,23)}${labelBox('lbH','3. HOLD 10-15 MIN',205,1032,28)}</g>`,
 S4=`<g id="s4"><rect x="-10" y="-10" width="740" height="1300" fill="#0b0b0d"/><text id="later" x="360" y="640" text-anchor="middle" style="font-family:LG,sans-serif;font-size:58px;letter-spacing:2px" fill="#ffd23a">15 MINUTES LATER</text></g>`, S5=`<g id="s5">${clinic19()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S2+S3+S5+S4+`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
const dropD='M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z';
const lab=(id,T,a,b,x,y)=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);};
// ---------- scene 1 ----------
function renderInside(T){
  const picked=T>=E.pick,pull=eio(P(T,E.pick,E.pick+.5)),bleed=T>=E.bleed,lt=speak('lining',T);
  // the finger: already inside on the first frame, wiggles, hooks the dry mucus and drags it out
  const wig=picked?0:Math.sin(T*26)*10,fx=414+wig,fy=lerp(760,1330,pull)+(picked?0:Math.sin(T*13)*8);
  mv('finger',fx,fy);mv('booger',lerp(410,fx-4,clamp(pull*6)),lerp(706,fy-30,clamp(pull*6)),pull*60);show('booger',pull<.95?1:0);
  show('scratch',picked?1:0);if(picked)$('scratch').setAttribute('transform',`translate(405,690) scale(${eob(P(T,E.pick,E.pick+.25)).toFixed(3)}) translate(-405,-690)`);
  // blood wells up in the scratch and runs out of the nostril
  let b='',d='';if(picked){const k=eio(P(T,E.pick+.5,E.bleed+1.2)),r=10+k*34;b+=`<circle cx="406" cy="700" r="${r.toFixed(1)}" fill="${C_BLOOD}" stroke="${INK}" stroke-width="2.6"/><circle cx="${(396-r*.3).toFixed(1)}" cy="${(692-r*.3).toFixed(1)}" r="${(r*.22).toFixed(1)}" fill="#ff8d94"/>`;
    if(bleed){const L=eo(P(T,E.bleed,E.bleed+1.3))*270;b+=`<path d="M392,${700} C388,${700+L*.5} 404,${700+L*.7} 410,${700+L} L432,${700+L} C436,${700+L*.6} 420,${700+L*.4} 424,700 Z" fill="${C_BLOOD}"/>`;
      for(let j=0;j<3;j++){const p=((T-E.bleed)*1.1+j/3)%1,y=960+p*p*330;if(T>E.bleed+.9)d+=`<path transform="translate(${414+j*4},${y.toFixed(1)}) scale(2.3)" d="${dropD}" fill="${C_BLOOD}" stroke="${INK}" stroke-width="1.3"/>`;}}}
  $('blood1').innerHTML=b;$('drip1').innerHTML=d;
  let f={dx:-4,dy:30,lid:.05,bA:-12,arch:7,mood:-.5,small:false};
  if(picked)f={dx:Math.sin(T*30)*6,dy:24,lid:0,bA:-20,arch:6,mood:-1,small:true};
  if(bleed)f={dx:-6,dy:30,lid:0,bA:-16,arch:8,mood:-.9,small:true};
  face('ln',33,{...f,blink:picked?0:blinkK(T,.4),bx:36,by:-50,bw:34,talk:lt,mw:17,T,seed:2});
  $('lface').setAttribute('transform',`translate(${(420+(picked&&T<E.pick+.6?Math.sin(T*50)*5:0)).toFixed(1)},${(440+Math.sin(T*2.4)*4).toFixed(1)}) scale(1.35)`);
  $('ring').setAttribute('r',(18+Math.abs(Math.sin(T*3.2))*9).toFixed(1));
  lab('lbM',T,0,E.pick,150,640);lab('lbV',T,0,E.pick+.05,566,214);lab('lbS',T,E.pick,E.bleed,600,380);lab('lbB',T,E.bleed,99,596,380);}
// ---------- scene 2 ----------
const dripStarts=[[E.front+.1,E.wipe1+.25],[E.wipe1+.75,E.wipe2+.25],[E.wipe2+.7,E.plug+.1]];
function renderFront(T){
  let L=0;for(const [a,b] of dripStarts)if(T>=a&&T<b)L=eo(P(T,a,a+1.6))*190;
  const plugOn=T>=E.plug,pk=eo(P(T,E.plug,E.plug+.45)),tT=speak('tissue',T);
  let d='';if(L>4){d+=`<path d="M440,756 L440,${756+L} C440,${786+L} 478,${786+L} 478,${756+L} L478,756 Z" fill="${C_BLOOD}" ${OLW2}/><path d="M450,772 V${740+L}" stroke="#ff8d94" stroke-width="6" stroke-linecap="round"/>`;
    const p=((T*1.2)%1);if(L>120)d+=`<path transform="translate(459,${(790+L+p*p*240).toFixed(1)}) scale(2.6)" d="${dropD}" fill="${C_BLOOD}" stroke="${INK}" stroke-width="1.2"/>`;}
  if(plugOn&&T>=E.plug+2.0){const k=eo(P(T,E.plug+2.0,E.plug+3.6))*150;d+=`<path d="M500,760 C504,${760+k*.6} 498,${760+k*.8} 506,${760+k} L524,${760+k} C528,${760+k*.6} 518,${760+k*.4} 522,760 Z" fill="${C_BLOOD}" ${OLW2}/>`;}
  $('drip2').innerHTML=d;
  // wiping with a tissue: it comes in from the right, wipes and leaves with a red stain
  let wOn=false;[E.wipe1,E.wipe2].forEach((t0,i)=>{if(T>=t0-.3&&T<t0+.75){wOn=true;const a=eo(P(T,t0-.3,t0)),o=eio(P(T,t0+.35,t0+.75)),sw=Math.sin(clamp(P(T,t0,t0+.35))*Math.PI*2)*46;
    mv('wipe',lerp(900,470,a)+sw+o*500,lerp(1200,850,a)+o*380,-8,1.15);
    $('wipeRed').innerHTML=T>=t0+.12?`<path d="M-40,-70 C-10,-96 40,-80 34,-44 C50,-20 16,0 -6,-12 C-36,-6 -58,-40 -40,-70 Z" fill="${C_BLOOD}"/>`:'';}});
  show('wipe',wOn?1:0);
  let sn='';if(T>=E.wipe2-.6&&T<E.wipe2-.15){const k=P(T,E.wipe2-.6,E.wipe2-.15);[0,1,2].forEach(j=>{sn+=`<path d="M${390+j*10},${900-j*26-k*30} q70,-34 140,0" fill="none" stroke="#f2c21d" stroke-width="12" stroke-linecap="round" opacity="${(1-k).toFixed(2)}"/>`;});}
  $('sniff').innerHTML=sn;
  // the tissue plug: pushed into the nostril, soaks through from the top
  show('plug',plugOn?1:0);if(plugOn){mv('plug',459,lerp(1500,742,pk)+Math.sin(T*2.4)*4-tT*4,Math.sin(T*1.8)*2,1.1);
    const s=eio(P(T,E.plug+.5,E.plug+3.2)),h=30+s*150;$('plugRed').innerHTML=`<path d="M-46,${h} L-46,10 C-46,-34 46,-34 46,10 L46,${h} q-15,16 -30,0 t-31,0 t-31,0 Z" fill="${C_BLOOD}" stroke="${INK}" stroke-width="2.6"/>`;
    face('tp',18,{dx:0,dy:-24,lid:0,blink:blinkK(T,1.3),small:s>.4,bx:19,by:-28,bw:20,bA:-14,arch:7,talk:tT,mw:10,mood:-.7,T,seed:4});}
  lab('lbT',T,E.plug+.5,E.plug+2.4,170,1080);lab('lbW',T,E.plug+2.4,99,360,250);}
// ---------- scene 3 ----------
function renderProfile(T){const t=T-E.pinch,lean=eio(P(t,.15,.9)),pin=eo(P(t,1.0,1.4));
  $('head').setAttribute('transform',`rotate(${(-13*lean).toFixed(2)},640,1000) translate(0,${(Math.sin(T*2)*3).toFixed(1)})`);
  mv('phand',lerp(-340,256,pin),lerp(300,498,pin)+Math.sin(T*3)*2,0);
  show('pblood',1-P(t,1.5,2.6));
  lab('lbL',T,E.pinch+.2,99,205,880);lab('lbP',T,E.pinch+1.25,99,205,956);lab('lbH',T,E.pinch+1.9,99,205,1032);
  const cOn=t>=1.9;show('clock',cOn?1:0);if(cOn){mv('clock',205,1160,0,eob(P(t,1.9,2.2))*.95);$('clockH').setAttribute('transform',`rotate(${((t-1.9)*200).toFixed(1)})`);}}
// ---------- scene 5 ----------
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['06_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.5,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  let pr=-3+Math.sin(T*.8)*1;if(pT>.2)pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr-(T>=d0?4:0));
  $('pBrows').setAttribute('d','M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66');
  setMouthV('pat_m',pT,10,T>=E.i3?.3:-.4,T,6);setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',.3);show('pSweat',0);
  const sh=[-84,234],el=[-134,300],wr=[-98,196];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]-6,-170,1.2,PSK);
  $('patWrap').setAttribute('transform',`translate(${(Math.sin(T*1.1)*2).toFixed(1)},${(Math.sin(T*2.2)*3).toFixed(1)})`);
  $('brd').setAttribute('transform',`translate(360,280) scale(${(1+Math.sin(T*2.4)*.006).toFixed(4)}) translate(-360,-280)`);
  [['b0',E.i0],['b1',E.i1],['b2',E.i2],['b3',E.i3]].forEach(([id,t0],i)=>{const on=T>=t0;show(id,on?1:0);if(on){const k=eob(P(T,t0,t0+.3)),y=175+i*94;$(id).setAttribute('transform',`translate(360,${y}) scale(${k.toFixed(3)}) translate(-360,${-y})`);}});}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1150,2:1160,3:1130,4:1130,5:1200}[sc];c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,${-y0})`);}
window.render=function(T){
  const sc=T<E.front?1:(T<E.pinch?2:(T<E.later?3:(T<E.clinic?4:5)));
  [1,2,3,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));show('wm',sc===4?0:.7);
  if(sc===1)renderInside(T);if(sc===2)renderFront(T);if(sc===3)renderProfile(T);if(sc===5)renderClinic(T);
  if(sc===4){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  caption(T,sc);};
window.render(0);

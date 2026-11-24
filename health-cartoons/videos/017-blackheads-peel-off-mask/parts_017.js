// =============== 017: "Why do blackheads come back after a peel-off mask?" One locked skin scene, then the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${skinWorld()}${labelBox('lbMask','PEEL-OFF MASK',470,318,28)}<path id="lbLine" d="M440,340 L420,398" stroke="#111" stroke-width="3.4" stroke-linecap="round" opacity="0"/>${labelBox('lbBH','BLACKHEAD',360,596,26)}${labelBox('lbOil','OIL',360,846,26)}${labelBox('lbPore','PORE',624,720,22)}</g>`, S3=`<g id="s3">${clinic17()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S3+`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".6">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1125" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
// how full each pore is (0 = full to the surface, 1 = empty) and how dark its top is
function state(id,T){const p=PORES[id];let empty=0,dark=1;
  if(id!=='big'){const rip=eo(P(T,E.peel+.05,E.peel+.3)),re=eio(P(T,E.refill,E.back));empty=.6*rip*(1-re);dark=1-rip*(1-re*re);
    const m=eio(P(T,E.melt+1.3,E.gone));empty=lerp(empty,1,m);dark*=1-P(T,E.melt+1.0,E.melt+1.6);}
  else{const m=eio(P(T,E.melt+.5,E.gone-.1));empty=m;dark=1-P(T,E.melt+.2,E.melt+1.3);}
  return {level:lerp(SURF-8,p.bot+6,empty),empty,dark};}
function renderSkin(T){
  const peelK=eio(P(T,E.peel,E.peel+.5)),dryK=P(T,E.dry,E.dry+2.2),melting=T>=E.melt,gone=T>=E.gone;
  // ---- the mask: brushed on from the first frame, dries, then is ripped away with the small plugs' tops ----
  const mx=lerp(150,880,eio(P(T,-.2,1.7)));
  let d='M-140,480 L-140,386';for(let x=-140;x<=mx;x+=40)d+=` Q${x+20},${372+((Math.round(x/40))%2?10:-2)} ${Math.min(x+40,mx)},${384}`;d+=` L${mx},480 Z`;
  $('maskP').setAttribute('d',d);$('maskP').setAttribute('fill',dryK>0?`rgb(${23+dryK*34},${23+dryK*34},${26+dryK*36})`:'#17171a');
  $('maskHi').setAttribute('d',`M0,410 q60,-10 120,0 M${Math.min(mx-150,260)},416 q70,-10 140,0 M${Math.min(mx-150,470)},408 q60,-10 120,0`);show('maskHi',1-dryK);show('maskDry',dryK);
  show('tops',T>=E.peel?1:0);show('mask',peelK<1?1:0);
  $('mask').setAttribute('transform',`translate(${(-peelK*160).toFixed(1)},${(-peelK*peelK*760).toFixed(1)}) rotate(${(-peelK*16).toFixed(1)},0,470)`);
  const bOn=T<2.3;show('brush',bOn?1:0);if(bOn){const out=eio(P(T,1.7,2.3));$('brush').setAttribute('transform',`translate(${(mx+out*300).toFixed(1)},${(420-out*500+Math.sin(T*20)*3).toFixed(1)}) rotate(${(Math.sin(T*9)*5).toFixed(1)})`);}
  const mlOn=T>=1.7&&T<E.peel;show('lbLine',mlOn?1:0);popLabel('lbMask',T,1.7,E.peel,470,318);
  ['lbBH','lbOil','lbPore'].forEach((id,i)=>{const on=T<3.5;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${[360,360,596][i]},${[640,940,800][i]}) scale(1)`);});
  // ---- the pores ----
  const bT=speak('big',T),sT=speak('sm',T),st={};
  ['sL','sR','big'].forEach(id=>{const p=PORES[id],s=state(id,T);st[id]=s;
    $(id+'_lr').setAttribute('y',s.level.toFixed(1));$(id+'_dark').setAttribute('transform',`translate(${p.cx},${s.level.toFixed(1)})`);show(id+'_dark',clamp(s.dark));
    const wob=Math.sin(T*3+p.cx)*3;$(id+'_surf').setAttribute('d',`M${p.cx-p.r},${(s.level+4).toFixed(1)} q${p.r/2},${(-6+wob).toFixed(1)} ${p.r},0 t${p.r},0`);show(id+'_surf',s.dark<.5&&s.empty<.98?.5:0);
    const fy=Math.min(p.bot-p.r*.42,Math.max(p.cy,s.level+p.r*.5)),sq=s.empty>.5?lerp(1,.25,(s.empty-.5)*2):1;
    $(id+'_face').setAttribute('transform',`translate(${(p.cx+Math.sin(T*1.3+p.cx)*3).toFixed(1)},${(fy+Math.sin(T*2.6+p.cx)*5).toFixed(1)}) scale(${(1+Math.sin(T*2.6+p.cx)*.02).toFixed(3)},${(sq*(1-Math.sin(T*2.6+p.cx)*.02)).toFixed(3)})`);show(id+'_face',s.empty<.97?1:0);});
  // faces
  let bf={dx:0,dy:-6,lid:.46,bA:2,arch:3,mood:.3,small:false};                                          // smug
  if(inL('04_big',T))bf={dx:0,dy:-24,lid:0,bA:-8,arch:8,mood:.2,small:false};
  if(T>=E.peel&&T<E.refill)bf={dx:-20,dy:-4,lid:.42,bA:0,arch:3,mood:.4,small:false};
  if(T>=E.acid+.5)bf={dx:0,dy:-30,lid:.3,bA:6,arch:2,mood:-.1,small:false};
  if(inL('12_big',T))bf={dx:0,dy:-28,lid:.5,bA:4,arch:3,mood:.6,small:false};
  if(melting)bf={dx:Math.sin(T*12)*10,dy:-20,lid:0,bA:-18,arch:8,mood:-.9,small:true};
  face('big',40,{...bf,blink:melting?0:blinkK(T,1.1),bx:46,by:-62,bw:42,talk:bT,mw:22,T,seed:3});
  const leftTalk=inL('01_sm',T)||inL('05_sm',T)||inL('07_sm',T)||inL('09_sm',T),rightTalk=inL('03_sm',T)||inL('09_sm',T);
  const scared=(T>=E.dry-.2&&T<E.refill)||melting,happy=T>=E.back&&T<E.acid+.6;
  ['sL','sR'].forEach((id,i)=>{const tk=(i?rightTalk:leftTalk)?sT:0;
    face(id,19,{dx:scared?(i?-8:8):(i?-18:18),dy:T<E.peel?-22:(T>=E.acid?-26:-8),lid:scared?0:.1,blink:blinkK(T,i?2.4:.4),small:scared&&!happy,bx:22,by:-30,bw:20,bA:scared?-16:(happy?-4:-8),arch:scared?5:7,talk:tk,mw:9,mood:happy?.9:(scared?-.8:-.3),T,seed:i+5});});
  // ---- the salicylic acid bottle and its drops ----
  const aIn=eo(P(T,E.acid,E.acid+.8)),aT=speak('acid',T);show('bottle',T>=E.acid?1:0);
  const bx=lerp(560,372,aIn),by=lerp(-80,412,aIn)+Math.sin(T*2.4)*5-aT*5;$('bottle').setAttribute('transform',`translate(${bx.toFixed(1)},${by.toFixed(1)}) rotate(${(lerp(14,4,aIn)+Math.sin(T*1.7)*2).toFixed(1)})`);
  face('ac',19,{dx:-4,dy:26,lid:inL('13_acid',T)?.35:.08,blink:blinkK(T,3.1),bx:24,by:-30,bw:22,bA:inL('13_acid',T)?6:-4,arch:6,talk:aT,mw:10,mood:.7,T,seed:9});
  let dr='',fx='';
  if(melting&&T<E.gone-.3){for(let j=0;j<3;j++){const p=((T-E.melt)/.32+j/3)%1,y=lerp(by+6,SURF+20,p*p);dr+=`<path transform="translate(${bx.toFixed(1)},${y.toFixed(1)}) scale(${(1.7).toFixed(2)})" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="#7ec8f7" stroke="${INK}" stroke-width="1.6"/>`;}}
  if(melting&&!gone){const p=PORES.big;for(let j=0;j<7;j++){const q=((T*.9+j/7)%1),x=p.cx+Math.sin(j*2.3)*p.r*.7,y=lerp(p.cy+p.r*.6,st.big.level,q);if(y>st.big.level+8)fx+=`<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${(6+j%3*4)}" fill="#bfe6ff" stroke="#5aa9dd" stroke-width="2.4" opacity="${(1-q).toFixed(2)}"/>`;}}
  if(gone){[[250,660,0],[470,640,1],[360,560,2],[96,560,3],[624,560,4]].forEach(([x,y,j])=>{const k=.5+.5*Math.sin(T*7+j*1.9),r=9+11*k;fx+=`<path d="M${x},${y-r} Q${x+2},${y-2} ${x+r},${y} Q${x+2},${y+2} ${x},${y+r} Q${x-2},${y+2} ${x-r},${y} Q${x-2},${y-2} ${x},${y-r}Z" fill="#fff" stroke="${INK}" stroke-width="2" opacity="${(.5+.5*k).toFixed(2)}"/>`;});}
  $('drops').innerHTML=dr;$('fx').innerHTML=fx;
}
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['16_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.5,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  let pr=-3+Math.sin(T*.8)*1;if(pT>.2)pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr-(T>=d0?4:0));
  $('pBrows').setAttribute('d',T<d0?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  setMouthV('pat_m',pT,10,T>=E.c2?.5:-.2,T,6);setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',.3);show('pSweat',0);
  const sh=[-84,234],el=[-108,356],wr=[-100,470];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+8,10,1.2,PSK);
  [['cd1',E.c1,197,340],['cd2',E.c2,523,340],['cd3',E.c3,360,588]].forEach(([id,t0,x,y])=>{const on=T>=t0;show(id,on?1:0);if(on){const k=eob(P(T,t0,t0+.3));$(id).setAttribute('transform',`translate(${x},${y}) scale(${k.toFixed(3)}) translate(${-x},${-y})`);}});
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,1108) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-1108)`);}
window.render=function(T){
  const sc=T<E.clinic?1:3;$('s1').setAttribute('display',sc===1?'inline':'none');$('s3').setAttribute('display',sc===3?'inline':'none');
  if(sc===1)renderSkin(T);else renderClinic(T);caption(T);};
window.render(0);

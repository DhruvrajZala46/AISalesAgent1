// =============== 019: "How picking your nose makes it bleed". Inside the nose, the nose from the front, the pinch, the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${insideNose()}</g>`, S2=`<g id="s2">${frontNose()}</g>`, S3=`<g id="s3">${profile()}</g>`,
 S4=`<g id="s4"><rect x="-10" y="-10" width="740" height="1300" fill="#000"/><text id="later" x="360" y="660" text-anchor="middle" style="font-family:LG,sans-serif;font-size:58px;letter-spacing:2px" fill="#ffe81a">15 MINUTES LATER</text></g>`, S5=`<g id="s5">${clinic19()}</g>`;
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
const WX=404,WY=694;
function renderInside(T){
  const pk=E.pick,picked=T>=pk,pull=eio(P(T,pk+.05,pk+.55)),bleed=T>=E.bleed,lt=speak('lining',T);
  // the finger is deep in the nose on frame 0, comes out, goes back in, scrapes the dry mucus off and pulls it out
  let tip; if(T<.3)tip=470+Math.sin(T*40)*14; else if(T<.5)tip=lerp(470,1080,eio(P(T,.3,.5))); else if(T<.7)tip=1080; else if(T<.92)tip=lerp(1080,WY-10,eo(P(T,.7,.92))); else if(!picked)tip=WY-10+Math.sin(T*46)*16; else tip=lerp(WY-10,1500,pull);
  const fx=lerp(388,WX,clamp((1000-tip)/300))+(T>.92&&!picked?Math.sin(T*33)*7:0);
  $('finger').setAttribute('transform',`translate(${fx.toFixed(1)},${tip.toFixed(1)}) rotate(-5)`);
  mv('booger',picked?fx+10:WX,picked?tip-26:WY,pull*40,1.3);show('booger',pull<.97?1:0);
  show('scratch',picked?1:0);if(picked)$('scratch').setAttribute('transform',`translate(${WX},${WY}) scale(${(eob(P(T,pk,pk+.25))*1.55).toFixed(3)}) translate(-405,-690)`);
  let b='',b2='',d='';if(picked){const o=eo(P(T,pk+.3,E.bleed));b+=`<circle cx="${WX}" cy="${WY}" r="${(6+o*20).toFixed(1)}" fill="#e0303a" opacity=".9"/>`;}
  if(bleed){const k=eo(P(T,E.bleed,E.bleed+1.5)),L=k*300,wd=40+k*26;
    b+=`<ellipse cx="${WX}" cy="${WY}" rx="${(30+k*26).toFixed(1)}" ry="${(30+k*20).toFixed(1)}" fill="#e0303a" opacity=".92"/><path d="${streamD(WX,WY,L,wd,T)}" fill="#e0303a" opacity=".92"/><ellipse cx="${WX-12}" cy="${WY-10}" rx="${(8+k*6).toFixed(1)}" ry="${(5+k*4).toFixed(1)}" fill="#ff9aa0" opacity=".8"/>`;
    if(k>.6){const m=eo(P(k,.6,1))*120;b2+=`<path d="${streamD(WX-14,905,20+m,58,T)}" fill="#e0303a" opacity=".92"/>`;
      for(let j=0;j<3;j++){const q=((T-E.bleed)*1.1+j/3)%1,y=1040+m+q*q*260;d+=`<path transform="translate(${WX-24+j*14},${y.toFixed(1)}) scale(2.8)" d="${dropD}" fill="#e0303a"/>`;}}}
  $('blood1').innerHTML=b;$('blood1b').innerHTML=b2;$('drip1').innerHTML=d;
  const scream=picked&&T<pk+.75;show('lnShut',scream?1:0);show('lnOpen',scream?0:1);
  let f={dx:-16,dy:30,lid:.02,bA:-8,arch:8,mood:-.3,small:false},talk=lt;
  if(T>.9&&!picked)f={dx:-10,dy:30,lid:0,bA:-18,arch:6,mood:-.8,small:true};
  if(scream){f={dx:0,dy:0,lid:0,bA:-26,arch:4,mood:-1,small:true};talk=Math.max(lt,.95);}
  else if(picked&&!bleed)f={dx:-8,dy:26,lid:.3,bA:-24,arch:9,mood:-1,small:false};
  else if(bleed)f={dx:-14,dy:34,lid:0,bA:-20,arch:9,mood:-.9,small:true};
  face('ln',33,{...f,blink:picked?0:blinkK(T,2.4),bx:34,by:-52,bw:34,talk,mw:13,T,seed:2});
  const sh=scream?Math.sin(T*55)*7:0;
  $('lface').setAttribute('transform',`translate(${(552+sh).toFixed(1)},${(420+Math.sin(T*2.4)*4).toFixed(1)}) scale(1.42)`);}
// ---------- scene 2 ----------
const NX=500,NY=764,dripStarts=[[E.front+.05,E.wipe1+.15],[E.wipe1+1.0,E.wipe2+.15],[E.wipe2+1.0,E.wipe3+.15],[E.rebleed,E.pinch+1]];
function renderFront(T){
  let L=0;for(const [a,b] of dripStarts)if(T>=a&&T<b)L=eo(P(T,a,a+2.0))*230+Math.sin(T*3)*5;
  [E.wipe2,E.wipe3].forEach(t0=>{if(T>=t0-.65&&T<t0-.1)L*=1-.55*Math.sin(P(T,t0-.65,t0-.1)*Math.PI);});
  const tT=speak('tissue',T),pt=T-E.plug;
  let d='';if(L>4){d+=`<path d="M432,770 C462,752 540,752 568,766 C536,786 462,788 432,770 Z" fill="#b3202b"/><path d="${streamD(NX,NY,L,72,T)}" fill="#e5484d"/><path d="M${NX-28},${NY} q28,22 56,0 l-4,26 q-24,10 -48,0 Z" fill="#c52a35"/>`;}
  $('drip2').innerHTML=d;
  // both hands bring a tissue up from below, wipe, and take it away with a red stain
  let wOn=false;[E.wipe1,E.wipe2,E.wipe3].forEach((t0)=>{if(T>=t0-.4&&T<t0+1.0){wOn=true;const a=eo(P(T,t0-.4,t0)),o=eio(P(T,t0+.5,t0+1.0)),sw=Math.sin(clamp(P(T,t0,t0+.5))*Math.PI*3)*24;
    mv('wipe',400+sw,lerp(1500,820,a)+o*760,sw*.1,1);
    $('wipeRed').innerHTML=T>=t0+.15?`<path d="M70,-50 C104,-70 140,-40 130,-4 C146,26 110,50 84,34 C54,42 40,-10 70,-50 Z" fill="#e5484d"/>`:'';}});
  show('wipe',wOn?1:0);
  let sn='';[E.wipe2,E.wipe3].forEach(t0=>{if(T>=t0-.65&&T<t0-.1){const k=P(T,t0-.65,t0-.1);[0,1,2].forEach(j=>{const y=1090-j*34-k*50,dd=`M${NX-80},${y} q80,-40 160,0`;sn+=`<path d="${dd}" fill="none" stroke="${INK}" stroke-width="24" stroke-linecap="round" opacity="${(1-k*k).toFixed(2)}"/><path d="${dd}" fill="none" stroke="#fff01f" stroke-width="16" stroke-linecap="round" opacity="${(1-k*k).toFixed(2)}"/>`;});}});
  $('sniff').innerHTML=sn;
  // a hand rolls a small ball of tissue, pushes it into the nostril, and it comes back out soaked and worried
  const on=pt>=0;show('plug',on?1:0);if(on){const up=eo(P(pt,0,.4)),inn=eio(P(pt,.5,.9)),out=eio(P(pt,1.9,2.3));
    const hx=lerp(lerp(420,NX-4,inn),390,out),hy=lerp(lerp(lerp(1500,1050,up),NY+22,inn),1040,out)+(pt>.9&&pt<1.9?Math.sin(pt*30)*5:0)+(pt>2.3?Math.sin(T*2.4)*5-tT*5:0);
    mv('plug',hx,hy,pt>2.3?Math.sin(T*1.8)*2:0,1.15);
    const s=clamp(P(pt,.9,1.9));$('plugRed').innerHTML=`<circle cx="6" cy="-10" r="${(8+s*40).toFixed(1)}" fill="#ef7f8a" opacity="${(s*.9).toFixed(2)}" filter="url(#soft)"/><circle cx="4" cy="-8" r="${(s*20).toFixed(1)}" fill="#e5484d" opacity=".75"/>`;
    const fo=clamp(P(pt,2.25,2.4));show('tface',fo);$('tface').setAttribute('transform',`scale(${eob(P(pt,2.2,2.5)).toFixed(3)})`);
    const scared=T>=E.rebleed;
    face('tp',18,{dx:scared?10:-4,dy:scared?-30:8,lid:0,blink:blinkK(T,1.3),small:scared,bx:30,by:-58,bw:22,bA:scared?-24:-12,arch:7,talk:tT,mw:11,mood:-.9,T,seed:4});}}
// ---------- scene 3 ----------
function renderProfile(T){const t=T-E.pinch,lean=eio(P(t,.1,.8)),pin=eo(P(t,.75,1.15));
  $('head').setAttribute('transform',`rotate(${(-10*lean).toFixed(2)},700,1100) translate(0,${(Math.sin(T*2)*3).toFixed(1)})`);
  mv('phand',lerp(-120,300,pin),lerp(200,478,pin)+Math.sin(T*3)*2,0);
  show('pmouth',clamp(P(t,1.15,1.4)));
  $('head').setAttribute('transform',`translate(${(150*lean).toFixed(1)},0) rotate(${(-10*lean).toFixed(2)},700,1100) translate(0,${(Math.sin(T*2)*3).toFixed(1)})`);
  $('pblood').setAttribute('opacity',(1-.2*P(t,1.6,2.6)).toFixed(2));}
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
  setMouthV('pat_m',pT,10,-.4,T,6);setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',.3);show('pSweat',0);
  const lift=pT>.2?Math.sin(T*8)*4:0,sh=[-84,234],el=[-128,300],wr=[-170,236+Math.sin(T*2.2)*3+lift];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]-6,-170,1.2,PSK);
  $('ptis').setAttribute('transform',`translate(${(540+wr[0]*1.08-4).toFixed(1)},${(330+wr[1]*1.08+6).toFixed(1)}) rotate(${(Math.sin(T*2.2)*4+lift).toFixed(1)})`);
  $('patWrap').setAttribute('transform',`translate(${(Math.sin(T*1.1)*2).toFixed(1)},0)`);}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1150,2:940,3:1130,4:1130,5:1130}[sc];c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));const x0=sc===2?250:360;c.setAttribute('x',x0);c.setAttribute('transform',`translate(${x0},${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(${-x0},${-y0})`);}
window.render=function(T){
  const sc=T<E.front?1:(T<E.pinch?2:(T<E.later?3:(T<E.clinic?4:5)));
  [1,2,3,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));show('wm',sc===4?0:.7);
  if(sc===1)renderInside(T);if(sc===2)renderFront(T);if(sc===3)renderProfile(T);if(sc===5)renderClinic(T);
  if(sc===4){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  caption(T,sc);};
window.render(0);

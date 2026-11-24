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
  const picked=T>=E.pick,pull=eio(P(T,E.pick+.05,E.pick+.6)),bleed=T>=E.bleed,lt=speak('lining',T);
  // the finger comes up through the nostril, scrapes the dry mucus off and pulls it out
  const up=eo(P(T,0,.28)),wig=picked?0:Math.sin(T*30)*8;
  const fy=picked?lerp(WY+20,1500,pull):lerp(930,WY+20,up),fx=lerp(350,WX,picked?1-pull:up)+wig;
  $('finger').setAttribute('transform',`translate(${fx.toFixed(1)},${fy.toFixed(1)}) rotate(${(-7+pull*4).toFixed(1)})`);
  mv('booger',lerp(WX,fx,clamp(pull*5)),lerp(WY,fy-40,clamp(pull*5)),pull*50,1.25);show('booger',pull<.97?1:0);
  show('scratch',picked?1:0);if(picked)$('scratch').setAttribute('transform',`translate(${WX},${WY}) scale(${(eob(P(T,E.pick,E.pick+.25))*1.5).toFixed(3)}) translate(-405,-690)`);
  let b='',b2='',d='';if(bleed){const k=eo(P(T,E.bleed,E.bleed+1.4)),L=k*330,w=22+k*14;
    b+=`<path d="M${WX-w},${WY-30} q${w},-30 ${2*w},0 C${WX+w+10},${WY+L*.3} ${WX+w-12},${WY+L*.6} ${WX+w},${WY+L} L${WX-w},${WY+L} C${WX-w-10},${WY+L*.6} ${WX-w+12},${WY+L*.3} ${WX-w},${WY-30} Z" fill="${C_BLOOD}" opacity=".93"/>`;
    if(k>.55){const m=eo(P(k,.55,1))*90;b2+=`<path d="M${WX-34},900 L${WX-36},${930+m} q6,26 16,4 q8,30 22,6 q10,22 20,-10 L${WX+30},900 Z" fill="${C_BLOOD}"/>`;
      for(let j=0;j<3;j++){const p=((T-E.bleed)*1.1+j/3)%1,y=1040+p*p*300;d+=`<path transform="translate(${WX-14+j*10},${y.toFixed(1)}) scale(2.6)" d="${dropD}" fill="${C_BLOOD}"/>`;}}}
  $('blood1').innerHTML=b;$('blood1b').innerHTML=b2;$('drip1').innerHTML=d;
  let f={dx:-10,dy:26,lid:.05,bA:-10,arch:7,mood:-.4,small:false};
  if(picked)f={dx:Math.sin(T*30)*6,dy:22,lid:0,bA:-22,arch:6,mood:-1,small:true};
  if(bleed)f={dx:-10,dy:28,lid:0,bA:-18,arch:8,mood:-.9,small:false};
  face('ln',33,{...f,blink:picked?0:blinkK(T,.4),bx:36,by:-50,bw:34,talk:lt,mw:15,T,seed:2});
  $('lface').setAttribute('transform',`translate(${(548+(picked&&T<E.pick+.6?Math.sin(T*50)*5:0)).toFixed(1)},${(420+Math.sin(T*2.4)*4).toFixed(1)}) scale(1.35)`);}
// ---------- scene 2 ----------
const dripStarts=[[E.front+.1,E.wipe1+.2],[E.wipe1+.9,E.wipe2+.2],[E.wipe2+.9,E.pinch]];
function renderFront(T){
  let L=0;for(const [a,b] of dripStarts)if(T>=a&&T<b)L=eo(P(T,a,a+1.8))*210+Math.sin(T*3)*4;
  if(T>=E.wipe2-.6&&T<E.wipe2-.1)L*=1-.5*Math.sin(P(T,E.wipe2-.6,E.wipe2-.1)*Math.PI);
  const plugOn=T>=E.plug,pk=eo(P(T,E.plug,E.plug+.5)),tT=speak('tissue',T);
  let d='';if(L>4){const y=756+L,s=Math.sin(T*5)*3;d+=`<path d="M418,752 C414,${756+L*.5} ${424+s},${756+L*.7} 420,${y-10} q6,30 18,6 q8,32 22,8 q10,20 18,-12 C${486-s},${756+L*.7} 494,${756+L*.5} 492,752 Z" fill="#e5484d"/><path d="M420,752 q36,26 72,0 Z" fill="#b3202b"/>`;}
  $('drip2').innerHTML=d;
  // both hands wipe with a tissue from below; it leaves with a red stain
  let wOn=false;[E.wipe1,E.wipe2].forEach((t0)=>{if(T>=t0-.35&&T<t0+.9){wOn=true;const a=eo(P(T,t0-.35,t0)),o=eio(P(T,t0+.45,t0+.9)),sw=Math.sin(clamp(P(T,t0,t0+.45))*Math.PI*3)*26;
    mv('wipe',400+sw,lerp(1500,850,a)+o*700,sw*.1,1);
    $('wipeRed').innerHTML=T>=t0+.15?`<path d="M0,-70 C34,-90 70,-60 60,-24 C76,6 40,30 14,14 C-16,22 -30,-30 0,-70 Z" fill="#e5484d"/>`:'';}});
  show('wipe',wOn?1:0);
  let sn='';if(T>=E.wipe2-.6&&T<E.wipe2-.1){const k=P(T,E.wipe2-.6,E.wipe2-.1);[0,1,2].forEach(j=>{sn+=`<path d="M${385},${1060-j*30-k*40} q70,-34 140,0" fill="none" stroke="${INK}" stroke-width="20" stroke-linecap="round" opacity="${(1-k).toFixed(2)}"/><path d="M${385},${1060-j*30-k*40} q70,-34 140,0" fill="none" stroke="#fff01f" stroke-width="13" stroke-linecap="round" opacity="${(1-k).toFixed(2)}"/>`;});}
  $('sniff').innerHTML=sn;
  // a hand holds up a small ball of tissue; it soaks pink and gets worried
  show('plug',plugOn?1:0);if(plugOn){mv('plug',300+Math.sin(T*1.3)*8,lerp(1500,1010,pk)+Math.sin(T*2.4)*5-tT*5,Math.sin(T*1.8)*3,1.3);
    const s=eio(P(T,E.plug+.4,E.plug+2.4));$('plugRed').innerHTML=`<circle cx="-8" cy="8" r="${(8+s*26).toFixed(1)}" fill="#ef7f8a" opacity="${(.5+s*.4).toFixed(2)}" filter="url(#soft)"/><circle cx="-8" cy="10" r="${(4+s*12).toFixed(1)}" fill="#e5484d" opacity=".8"/>`;
    face('tp',18,{dx:-6,dy:-10,lid:0,blink:blinkK(T,1.3),small:s>.6,bx:18,by:-27,bw:18,bA:-16,arch:6,talk:tT,mw:9,mood:-.8,T,seed:4});}}
// ---------- scene 3 ----------
function renderProfile(T){const t=T-E.pinch,lean=eio(P(t,.1,.8)),pin=eo(P(t,.9,1.35));
  $('head').setAttribute('transform',`rotate(${(-9*lean).toFixed(2)},700,1100) translate(0,${(Math.sin(T*2)*3).toFixed(1)})`);
  mv('phand',lerp(-80,292,pin),lerp(250,470,pin)+Math.sin(T*3)*2,0);
  $('pblood').setAttribute('opacity',(1-.25*P(t,1.6,2.8)).toFixed(2));}
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
  const sh=[-84,234],el=[-120,290],wr=[-140,176+Math.sin(T*2.2)*3];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]-6,-170,1.2,PSK);
  $('ptis').setAttribute('transform',`translate(${548+wr[0]*1.25},${500+wr[1]*1.25+4}) rotate(${(Math.sin(T*2.2)*4+(pT>.2?Math.sin(T*9)*3:0)).toFixed(1)})`);
  $('patWrap').setAttribute('transform',`translate(${(Math.sin(T*1.1)*2).toFixed(1)},0)`);}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1120,2:880,3:1130,4:1130,5:1100}[sc];c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,${-y0})`);}
window.render=function(T){
  const sc=T<E.front?1:(T<E.pinch?2:(T<E.later?3:(T<E.clinic?4:5)));
  [1,2,3,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));show('wm',sc===4?0:.7);
  if(sc===1)renderInside(T);if(sc===2)renderFront(T);if(sc===3)renderProfile(T);if(sc===5)renderClinic(T);
  if(sc===4){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  caption(T,sc);};
window.render(0);

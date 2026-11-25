// =============== 021: "How cutting your toenails can cause an ingrown toenail". Two toes and a clipper, "LATER...", the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${toesScene()}</g>`, S4=`<g id="s4"><rect x="-10" y="-10" width="740" height="1300" fill="#0b0b0d"/><rect x="-10" y="450" width="740" height="380" fill="#3a2a8a"/><text id="later" x="360" y="668" text-anchor="middle" style="font-family:LG,sans-serif;font-size:96px;letter-spacing:4px" fill="#5fe3e8" stroke="#141418" stroke-width="5" paint-order="stroke">LATER...</text></g>`, S5=`<g id="s5">${clinic21()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +`<g id="cam">`+S1+S5+S4+`</g>`+labelBox('lbR','CORNERS CUT ROUND',0,0,28)+labelBox('lbS','EVEN SHORTER!',0,0,30)+labelBox('lbG','GROWS INTO THE SKIN',0,0,28)+labelBox('lbI','INGROWN TOENAIL',0,0,32)
 +`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);if($(id+'_m'))setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
const lab=(id,T,a,b,x,y)=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);};
// the nail's state over time: [top, corner radius, extra half-width]
const LONG=[430,40,0],SHORT1=[512,112,0],SHORT2=[548,118,0],IN=[470,60,16];
function nailState(T){const mix=(a,b,k)=>a.map((v,i)=>lerp(v,b[i],k));
  if(T<E.cut1+.38)return LONG; if(T<E.grow1+.55)return SHORT1; if(T<E.cut2+.38)return mix(SHORT1,LONG,eob(P(T,E.grow1+.55,E.grow1+.85)));
  if(T<E.grow2+.55)return SHORT2; return mix(SHORT2,IN,eo(P(T,E.grow2+.55,E.grow2+1.1)));}
function renderToes(T){
  const bad=T>=E.later,[top,r,w]=nailState(T),d=nailD(top,r,w);
  ['nail','nailO','nailCP'].forEach(id=>$(id).setAttribute('d',d));
  const isLong=top<500;$('free').setAttribute('y',top-6);$('free').setAttribute('height',isLong?76:0);$('freeL').setAttribute('d',isLong?`M0,${top+70} H460`:'');
  // the clipper: home at the top left; swoops to the nail's corner and snips; leaves and returns
  const cT=speak('clipper',T);let cx=118,cy=236,cr=-14,cs=.92;
  const sw=t0=>{const a=eio(P(T,t0,t0+.34)),b=eio(P(T,t0+.46,t0+.8)),k=a-b;cx=lerp(118,318,k);cy=lerp(236,360,k);cr=lerp(-14,38,k)+(T>t0+.34&&T<t0+.46?Math.sin(T*90)*4:0);};
  if(T>=E.cut1&&T<E.cut1+.8)sw(E.cut1);if(T>=E.cut2&&T<E.cut2+.8)sw(E.cut2);
  let off=0;if(T>=E.exit1&&T<E.back1)off=T<E.back1-.01?eio(P(T,E.exit1,E.exit1+.35)):0;if(T>=E.back1)off=1-eo(P(T,E.back1,E.back1+.35));if(T>=E.exit2&&!bad)off=eio(P(T,E.exit2,E.exit2+.35));
  cx-=off*330;cy-=off*260;
  if(bad){const k=eo(P(T,E.bad+.15,E.bad+.6)),rec=eo(P(T,E.bad+.6,E.bad+.9));cx=lerp(900,500,k)+rec*40;cy=lerp(60,330,k)-rec*40;cr=24+rec*10+Math.sin(T*3)*3;cs=.9;}
  mv('clipW',cx,cy+Math.sin(T*2.2)*5,cr,cs);
  $('cmouth').setAttribute('height',(46+cT*56).toFixed(1));show('ctong',cT>.3?1:0);
  show('carms',bad&&T>=E.bad+.6?1:0);
  const lookB=bad?{dx:-20,dy:26}:{dx:14,dy:30};
  face('cl',34,{dx:lookB.dx,dy:lookB.dy,lid:bad?0:.22,blink:blinkK(T,.4),small:bad,bx:36,by:-46,bw:30,bA:bad?-22:10,arch:5,T});
  // the clipping flies off
  let ch=0;[E.cut1,E.cut2].forEach(t0=>{const t=T-t0-.38;if(t>=0&&t<.7){ch=1;mv('chip',330+t*420,430-t*260+t*t*900,t*500,1);}});show('chip',ch);
  // the dashed line on the rounded edge
  const dOn=T>=E.dash&&T<lend('02_bigtoe')+.2;show('dash',dOn?(.7+.3*Math.sin(T*10)):0);if(dOn)$('dash').setAttribute('d',`M36,${top+r+40} Q36,${top-14} ${48+r},${top-14} L${402-r},${top-14} Q414,${top-14} 414,${top+r+40}`);
  // growing: strain, sparkles
  const g1=T>=E.grow1&&T<E.grow1+.6,g2=T>=E.grow2&&T<E.grow2+1.1,strain=g1||g2;
  let sp='';if(strain||(T>=E.grow1+.55&&T<E.grow1+1.1)){for(let j=0;j<7;j++){const a=j*.9+T*2,x=225+Math.cos(a)*(230+j%2*30),y=600+Math.sin(a)*(250+j%3*20)*.8;sp+=`<path transform="translate(${x.toFixed(0)},${y.toFixed(0)}) scale(${(1.2+Math.sin(T*9+j)*.5).toFixed(2)})" d="M0,-14 L4,-4 L14,0 L4,4 L0,14 L-4,4 L-14,0 L-4,-4 Z" fill="#fff" stroke="${INK}" stroke-width="1.6"/>`;}}
  $('spark').innerHTML=sp;
  // swelling and smell
  const sK=bad?1:eo(P(T,E.grow2+.5,E.grow2+1.2));let swl='';if(sK>0){const pu=1+Math.sin(T*5)*.06;swl=`<ellipse cx="34" cy="640" rx="${62*sK*pu}" ry="${170*sK}" fill="${C_RED}" opacity="${(.85*sK).toFixed(2)}" filter="url(#soft2)"/><ellipse cx="420" cy="650" rx="${62*sK*pu}" ry="${170*sK}" fill="${C_RED}" opacity="${(.85*sK).toFixed(2)}" filter="url(#soft2)"/><ellipse cx="225" cy="${top-10}" rx="${200*sK}" ry="${34*sK}" fill="#e98b6a" opacity="${(.5*sK).toFixed(2)}" filter="url(#soft2)"/>`;}
  $('swell').innerHTML=swl;
  $('swell2').innerHTML=sK>0?[[40,1],[410,-1]].map(([x,s])=>{const pu=1+Math.sin(T*5+x)*.05;return `<path d="M${x-s*34*sK},${top+40} C${x+s*50*sK*pu},${top+90} ${x+s*56*sK*pu},${top+300} ${x-s*30*sK},${top+350} C${x-s*60*sK},${top+260} ${x-s*60*sK},${top+120} ${x-s*34*sK},${top+40} Z" fill="#e2504a" stroke="${INK}" stroke-width="3" opacity="${Math.min(1,sK*1.2).toFixed(2)}"/><path d="M${x+s*10*sK},${top+110} q${s*14},70 0,150" fill="none" stroke="#f59a8e" stroke-width="8" stroke-linecap="round" opacity="${sK.toFixed(2)}"/>`;}).join(''):'';
  let stk='';if(bad){const o=clamp(P(T,E.bad,E.bad+.5));for(let j=0;j<6;j++){const x=40+j*76,ph=T*2+j;let dd=`M${x},470`;for(let k=1;k<=5;k++)dd+=` q${(k%2?26:-26)+Math.sin(ph+k)*8},-34 0,-68`;stk+=`<path d="${dd}" fill="none" stroke="#8fc46a" stroke-width="14" stroke-linecap="round" opacity="${(o*.6).toFixed(2)}"/>`;}}
  $('stink').innerHTML=stk;
  // faces
  const bT=speak('bigtoe',T),tT=speak('toe',T);
  let f={dx:-16,dy:-30,lid:.05,bA:0,arch:5,mood:.1,small:false};                         // watching the clipper
  if(T>=E.cut1+.38)f={dx:-10,dy:-26,lid:0,bA:-16,arch:8,mood:-.8,small:true};
  if(T>=ST['03_clipper'])f={dx:-16,dy:-28,lid:.2,bA:14,arch:3,mood:-.8,small:false};
  if(T>=E.exit1)f={dx:22,dy:0,lid:.1,bA:6,arch:4,mood:-.5,small:false};                  // listens to the second toe
  if(T>=E.grow1+.55)f={dx:0,dy:-20,lid:0,bA:0,arch:8,mood:1,small:false};
  if(T>=E.back1)f={dx:-16,dy:-30,lid:.05,bA:-4,arch:6,mood:.1,small:false};
  if(T>=E.cut2+.38)f={dx:-12,dy:-26,lid:.1,bA:20,arch:2,mood:-1,small:false};            // angry
  if(T>=E.exit2)f={dx:22,dy:2,lid:.15,bA:16,arch:2,mood:-.8,small:false};
  if(T>=ST['09_bigtoe'])f={dx:8,dy:-6,lid:.12,bA:22,arch:2,mood:-.6,small:false};
  if(bad)f={dx:16,dy:-22,lid:.2,bA:-4,arch:5,mood:.8,small:false};                       // smug
  show('bShut',strain?1:0);show('bOpen',strain?0:1);
  face('bt',40,{...f,blink:blinkK(T,1.3),bx:68,by:-66,bw:50,talk:strain?.8:bT,mw:13,T,seed:1});
  $('bface').setAttribute('transform',`translate(${(225+(strain?Math.sin(T*50)*6:0)).toFixed(1)},${(lerp(650,676,clamp((top-430)/118))+Math.sin(T*2.1)*3).toFixed(1)}) scale(${bad?1.3:1.42})`);
  let g={dx:-22,dy:-16,lid:.1,bA:0,arch:4,mood:0,small:false};
  if(inL('04_toe',T))g={dx:-24,dy:4,lid:.2,bA:6,arch:3,mood:.4,small:false};
  if(T>=E.cut2+.38)g={dx:-24,dy:-8,lid:.1,bA:-8,arch:6,mood:-.4,small:false};
  if(inL('08_toe',T))g={dx:-24,dy:4,lid:.3,bA:14,arch:2,mood:-.4,small:false};
  if(T>=E.grow2+.5)g={dx:-26,dy:6,lid:0,bA:-18,arch:8,mood:-.9,small:true};
  face('t2',36,{...g,blink:blinkK(T,2.6),bx:42,by:-52,bw:34,talk:tT,mw:11,T,seed:2});
  $('tface').setAttribute('transform',`translate(576,${(662+Math.sin(T*2.4+1)*3).toFixed(1)}) scale(1.18)`);
  show('inset',bad?0:1);$('ring').setAttribute('r',(28+Math.abs(Math.sin(T*3.2))*8).toFixed(1));}
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['12_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.4,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,-4+(pT>.2?Math.sin(T*7)*2:0));
  $('pBrows').setAttribute('d','M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66');
  setMouthV('pat_m',pT,10,-.5,T,6);setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));show('patBlush',0);show('pSweat',0);
  const P3=[[-84,234],[-116,340],[-96,440]],d=limbD(P3,[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);$('patHandL').innerHTML=hand(-94,452,-10,1.2,PSK);
  let pn='';for(let j=0;j<4;j++){const q=((T*1.4+j/4)%1),a=-2.4+j*.55;pn+=`<path d="M${(Math.cos(a)*(84+q*20)).toFixed(0)},${(Math.sin(a)*(84+q*20)-10).toFixed(0)} l${(Math.cos(a)*18).toFixed(0)},${(Math.sin(a)*18).toFixed(0)}" stroke="#e02626" stroke-width="7" stroke-linecap="round" opacity="${(1-q).toFixed(2)}"/>`;}$('pain').innerHTML=pn;
  $('pfoot').setAttribute('transform',`translate(400,1110) scale(${(1+Math.sin(T*5)*.02).toFixed(3)})`);
  const on=T>=d0;show('brd',on?1:0);if(on)$('brd').setAttribute('transform',`translate(360,270) scale(${(eob(P(T,d0,d0+.35))*(1+Math.sin(T*2.4)*.005)).toFixed(4)}) translate(-360,-270)`);
  [['m0',E.i0,196,200],['m1',E.i1,524,200],['m2',E.i3,360,476]].forEach(([id,t0,x,y])=>{const o=T>=t0;show(id,o?1:0);if(o){const k=eob(P(T,t0,t0+.3));$(id).setAttribute('transform',`translate(${x},${y}) scale(${k.toFixed(3)}) translate(${-x},${-y})`);}});}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1010,4:1130,5:1235}[sc];c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,${-y0})`);}
window.render=function(T){
  const sc=T>=E.clinic?5:(T>=E.later&&T<E.bad?4:1);
  [1,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));show('wm',sc===4?0:.7);
  if(sc===1)renderToes(T);if(sc===5)renderClinic(T);
  if(sc===4){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  $('cam').setAttribute('transform',`translate(360,640) scale(${(1.012+Math.sin(T*1.4)*.012).toFixed(4)}) translate(-360,-640)`);
  const s1=sc===1;lab('lbR',T,s1?E.cut1+.5:99,E.exit1,230,404);lab('lbS',T,s1?E.cut2+.5:99,E.exit2,230,430);lab('lbG',T,s1?E.grow2+.6:99,E.later,230,404);lab('lbI',T,s1?E.bad+.2:99,E.clinic,230,404);
  caption(T,sc);};
window.render(0);

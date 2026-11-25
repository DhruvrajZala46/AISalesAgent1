// =============== 022: "Why mouth breathing changes your face". The head from the side, "LATER...", the mirror and the doctor. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${headScene().replace('<g id="airB"></g>',`<g id="airB">${bubbleSVG('a2')}${bubbleSVG('a1')}</g>`)}</g>`,
 S4=`<g id="s4"><rect x="-10" y="-10" width="740" height="1300" fill="#0b0b0d"/><rect x="-10" y="450" width="740" height="380" fill="#3a2a8a"/><text id="later" x="360" y="668" text-anchor="middle" style="font-family:LG,sans-serif;font-size:96px;letter-spacing:4px" fill="#5fe3e8" stroke="#141418" stroke-width="5" paint-order="stroke">LATER...</text></g>`, S5=`<g id="s5">${mirrorScene()}</g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +`<g id="cam">`+S1+S5+S4+`</g>`+labelBox('lbA','ADENOIDS',0,0,28)+labelBox('lbN','NOSE BLOCKED!',0,0,32)+labelBox('lbM','BREATHING THROUGH THE MOUTH',0,0,24)+labelBox('lbP','ROOF OF THE MOUTH',0,0,24)+labelBox('lbT','TONGUE',0,0,28)+labelBox('lbH','ROOF PULLED HIGH',0,0,28)+labelBox('lbJ','JAW HANGS OPEN',0,0,28)
 +`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
const lab=(id,T,a,b,x,y)=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);};
// a point along a polyline, k in 0..1 (by segment count)
const along=(pts,k)=>{k=clamp(k)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(k)),f=k-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];};
const HX=x=>Math.round(64+1.02*x),HY=y=>Math.round(-52+1.02*y);
const NOSEIN=[[-220,540],[60,590],[150,500],[286,452]],MOUTH=[[-220,720],[110,694],[300,684],[450,700],[560,880],[600,1560]];
function renderHead(T){
  const worked=T>=E.work,mk=eio(P(T,E.make+.2,E.make+1.4));
  const op=eio(P(T,E.detour+.75,E.detour+1.2))*(1+mk*.7);
  $('jaw').setAttribute('transform',`rotate(${(-op*7.5).toFixed(2)},600,760) translate(0,${(Math.sin(T*2)*(worked?2:0)).toFixed(1)})`);
  $('pal').setAttribute('d',palD(mk));
  // the adenoid
  const aT=speak('adenoid',T),shades=T<ST['02_air']-.2;show('shades',shades?1:0);
  let af={dx:-20,dy:6,lid:.5,bA:8,arch:2,mood:-.2};if(inL('03_adenoid',T))af={dx:-22,dy:4,lid:.6,bA:10,arch:2,mood:-.5};if(T>=E.detour)af={dx:0,dy:10,lid:1,bA:0,arch:2,mood:.4};
  face('ad',24,{...af,blink:0,bx:26,by:-34,bw:24,talk:aT,mw:10,T,seed:1});
  $('adeW').setAttribute('transform',`translate(556,${(476+Math.sin(T*1.6)*4).toFixed(1)}) scale(${(1+Math.sin(T*1.6)*.03).toFixed(3)})`);
  show('xmark',T>=ST['02_air']&&T<E.later?(.85+.15*Math.sin(T*8)):0);
  // the two air bubbles
  const t1=T-E.airin,td=T-E.detour;let p1,p2,vis=T>=E.airin&&T<E.later;
  if(td<0){p1=along(NOSEIN.concat([[396,458]]),eo(P(t1,0,1.0))*(4/4));p2=along(NOSEIN,eo(P(t1,.25,1.2)));}
  else{const seg=(d)=>{const t=td-d;if(t<.8)return along([[d?300:404,d?446:452],[150,500],[60,590],[-150,600]],eio(P(t,0,.8)));if(t<1.0)return along([[-150,600],[-220,720]],P(t,.8,1.0));return along(MOUTH,P(t,1.0,2.3));};p1=seg(.15);p2=seg(0);}
  show('airB',vis?1:0);if(vis){const b=i=>Math.sin(T*5+i)*5;mv('a1',p1[0],p1[1]+b(0),Math.sin(T*3)*4,1.08);mv('a2',p2[0],p2[1]+b(2),Math.sin(T*3+1)*4,1.0);
    const s1=speak('air',T),s2=speak('airb',T),mad=T>=ST['02_air'];
    face('a1',17,{dx:20,dy:2,lid:mad?.15:0,blink:blinkK(T,.5),bx:17,by:-26,bw:16,bA:mad?18:0,arch:3,talk:s1,mw:8,mood:-.6,T,seed:3});
    face('a2',17,{dx:20,dy:0,lid:.1,blink:blinkK(T,1.7),bx:17,by:-26,bw:16,bA:inL('04_airb',T)?16:4,arch:3,talk:s2,mw:8,mood:-.3,T,seed:4});}
  // after "LATER": a steady stream of air through the mouth
  let st='';if(worked){for(let j=0;j<5;j++){const k=((T*.42+j/5)%1),[x,y]=along(MOUTH,k);st+=`<circle cx="${x.toFixed(0)}" cy="${(y+Math.sin(T*6+j)*4).toFixed(0)}" r="${24+j%2*6}" fill="#fff" opacity=".5" stroke="${INK}" stroke-width="2.4"/><path d="M${(x-12).toFixed(0)},${(y-10).toFixed(0)} q6,-8 14,-8" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>`;}}
  $('airF').innerHTML=st;
  // the roof of the mouth and the tongue
  show('pFace',worked?1:0);show('tFace',worked?1:0);
  if(worked){const pT=speak('palate',T),gT=speak('tongue',T),ang=inL('06_palate',T)||inL('08_palate',T),sly=T>=ST['10_palate'];
    face('pl',30,{dx:sly?10:0,dy:ang?-4:16,lid:mk>.3?.9:(sly?.3:.42),blink:blinkK(T,.9),bx:38,by:-66,bw:34,bA:ang?20:(sly?-10:8),arch:3,talk:pT,mw:12,mood:sly?.7:-.8,T,seed:5});
    $('pFace').setAttribute('transform',`translate(${(300+(ang?Math.sin(T*24)*2:0)).toFixed(1)},${(596-mk*82+Math.sin(T*2.3)*2).toFixed(1)})`);
    face('tg',30,{dx:0,dy:-22,lid:mk>.3?.9:.4,blink:blinkK(T,2.2),bx:38,by:-44,bw:32,bA:6,arch:3,talk:gT,mw:12,mood:-.6,T,seed:6});}
  // the "makeover": ropes pull the roof up and the tongue down
  const rk=clamp(P(T,E.make,E.make+.25));
  $('ropeP').innerHTML=rk>0?[[236,392],[372,374]].map(([x,y])=>`<path d="M${x},${y} L${x+6},${598-mk*84}" stroke="${INK}" stroke-width="9" stroke-linecap="round" opacity="${rk}"/><path d="M${x},${y} L${x+6},${598-mk*84}" stroke="#e9dcc0" stroke-width="5" stroke-linecap="round" stroke-dasharray="10 6" opacity="${rk}"/>`).join(''):'';
  $('ropeT').innerHTML=rk>0?[[250,800],[330,812]].map(([x,y])=>`<path d="M${x},${y} L${x+250},${y+110}" stroke="${INK}" stroke-width="9" stroke-linecap="round" opacity="${rk}"/><path d="M${x},${y} L${x+250},${y+110}" stroke="#e9dcc0" stroke-width="5" stroke-linecap="round" stroke-dasharray="10 6" opacity="${rk}"/>`).join(''):'';}
function renderMirror(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=E.doc,dk=eo(P(T,d0,d0+.4));
  $('docW').setAttribute('transform',`translate(${(-420*(1-dk)).toFixed(1)},0)`);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,.3,T,5);setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  // the long face in the mirror
  tr('patHead',0,-18+Math.sin(T*1.5+1)*1.2,.94,1.2,-5+(pT>.2?Math.sin(T*7)*1.5:0));
  $('pBrows').setAttribute('d','M-36,62 Q-24,60 -10,52 M8,52 Q22,60 34,62');
  setMouthV('pat_m',Math.max(pT,.55),11,-.6,T,6);setHEye('pEyeL',-4,Math.max(.35,blinkK(T,2.1)));setHEye('pEyeR',-4,Math.max(.35,blinkK(T,2.1)));show('patBlush',0);show('pSweat',0);
  const wr=[-150,306+Math.sin(T*2)*3],P3=[[-84,234],[-130,350],wr],d=limbD(P3,[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);$('patHandL').innerHTML=hand(wr[0],wr[1],-160,1.2,PSK);
  const hx=560+wr[0]*.9,hy=470+wr[1]*.9;$('mirror').setAttribute('transform',`translate(${(hx-14).toFixed(1)},${(hy-186).toFixed(1)}) rotate(${(-8+Math.sin(T*2)*2).toFixed(1)},24,300) scale(.62)`);
  {const z=lerp(1.75,1,eio(P(T,d0-.15,d0+.45)));$('s5').setAttribute('transform',`translate(${lerp(600,440,(z-1)/.75).toFixed(0)},610) scale(${z.toFixed(3)}) translate(-600,-610)`);}
  const on=T>=d0;show('brd',on?1:0);if(on)$('brd').setAttribute('transform',`translate(360,250) scale(${(eob(P(T,d0,d0+.35))*(1+Math.sin(T*2.4)*.005)).toFixed(4)}) translate(-360,-250)`);
  [['b0',E.i0],['b1',E.i1],['b2',E.i2],['b3',E.i3]].forEach(([id,t0],i)=>{const o=T>=t0;show(id,o?1:0);if(o){const k=eob(P(T,t0,t0+.3)),y=161+i*78;$(id).setAttribute('transform',`translate(360,${y}) scale(${k.toFixed(3)}) translate(-360,${-y})`);}});}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1150,4:1130,5:(T<E.doc?1060:1235)}[sc],x0=sc===1?300:360;c.setAttribute('x',x0);c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(${x0},${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(${-x0},${-y0})`);}
window.render=function(T){
  const sc=T>=E.mirror?5:(T>=E.later&&T<E.work?4:1);
  [1,4,5].forEach(i=>$('s'+i).setAttribute('display',sc===i?'inline':'none'));show('wm',sc===4?0:.7);
  if(sc===1)renderHead(T);if(sc===5)renderMirror(T);
  if(sc===4){const k=eob(P(T,E.later,E.later+.25));$('later').setAttribute('transform',`translate(360,640) scale(${k.toFixed(3)}) translate(-360,-640)`);}
  $('cam').setAttribute('transform',`translate(360,640) scale(${(1.012+Math.sin(T*1.4)*.012).toFixed(4)}) translate(-360,-640)`);
  const s1=sc===1;lab('lbA',T,s1?.2:99,ST['02_air'],HX(540),HY(330));lab('lbN',T,s1?ST['02_air']+.3:99,E.detour,HX(430),HY(300));lab('lbM',T,s1?E.detour+1.3:99,E.later,360,HY(1040));
  lab('lbP',T,s1?E.work+.2:99,E.work+3.4,HX(440),HY(520));lab('lbT',T,s1?E.work+.4:99,E.work+3.4,HX(300),HY(920));lab('lbH',T,s1?E.make+.6:99,E.mirror,HX(430),HY(300));lab('lbJ',T,s1?E.make+.9:99,E.mirror,HX(280),HY(1060));
  caption(T,sc);};
window.render(0);

// =============== 020: "Why babies under 6 months shouldn't drink water". The stomach, the intestine, the living room, the clinic. ===============
const E=D.ev, ST=D.start, END=D.end;
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const svg=$('S');
const S1=`<g id="s1">${stomachScene()}</g>`, S2=`<g id="s2">${gutScene()}</g>`, S3=`<g id="s3">${homeBG()}</g>`, S4B=`<g id="s4b">${clinicBG()}</g>`,
 DAD=`<g id="dadL">${dadSVG()}</g>`, S4F=`<g id="s4f"><g transform="translate(170,985) scale(1.1)">${momSVG()}</g><g transform="translate(575,404) scale(.95)">${doctorSVG()}</g></g>`;
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +`<g id="cam">`+S1+S2+S3+S4B+DAD+S4F+`</g>`+labelBox('lbA',"BABY'S TUMMY",0,0,30)+labelBox('lbM','MILK',0,0,34)+labelBox('lbW','WATER',0,0,34)+labelBox('lbD','TOO WATERY!',0,0,30)+labelBox('lbI','INTESTINE',0,0,30)+`<text id="wm" x="360" y="58" text-anchor="middle" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".7">@GiggleMD</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;
function face(id,r,{dx=0,dy=0,lid=.1,blink=0,small=false,bx=27,by=48,bw=26,bA=0,arch=3,talk=0,mw=12,mood=0,T=0,seed=0}){
  setOEye(id+'_eL',r,{dx,dy,lid,blink,small});setOEye(id+'_eR',r,{dx,dy,lid,blink,small});
  setBrow(id+'_bL',-bx,by,bw,bA,arch);setBrow(id+'_bR',bx,by,bw,-bA,arch);setMouthV(id+'_m',talk,mw,mood,T,seed);}
const mv=(id,x,y,r=0,s=1)=>$(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${r.toFixed(1)}) scale(${s})`);
const lab=(id,T,a,b,x,y)=>{const on=T>=a&&T<b;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${(T<.02?1:Math.max(.01,eob(P(T,a-.01,a+.28)))).toFixed(3)})`);};
const pulse=(T,on)=>on?(.75+.25*Math.sin(T*18)):0;
// ---------- scene 1: the stomach ----------
function renderStomach(T){
  const sT=speak('stomach',T),dadOn=inL('01_dad',T,0,0),tossed=T>=E.toss,tk=eo(P(T,E.toss,E.toss+.45));
  const milkT=T-E.milk,watT=T-E.water,spoonOn=T>=E.spoon&&T<E.water+.2,phoneOn=T>=E.phone,pk=eob(P(T,E.phone,E.phone+.3));
  // newspaper and pacifier
  show('paper',tk<1?1:0);mv('paper',lerp(545,960,tk),lerp(486,60,tk)+Math.sin(T*2)*3,tk*200,.86-tk*.3);
  show('paci',tossed?1-P(T,E.toss,E.toss+.5):1);$('paci').setAttribute('transform',`translate(${(tk*-60).toFixed(1)},${(84+tk*tk*420).toFixed(1)}) rotate(${(tk*-120).toFixed(0)})`);
  show('vArcs',pulse(T,dadOn));
  // arms
  let aL,aR;if(!tossed){aL='M446,440 C420,452 410,470 414,490';aR='M640,440 C668,452 680,470 676,488';}
  else{const w=Math.sin(T*3)*6;aL=`M440,430 q-14,${36+w} 4,${64+w}`;aR=`M642,430 q14,${36-w} -4,${64-w}`;}
  if(spoonOn)aL='M440,430 C410,440 400,460 414,482';
  if(phoneOn)aR=`M646,410 C${696},${lerp(430,372,pk)} ${lerp(660,700,pk)},${lerp(470,318,pk)} ${lerp(644,676,pk)},${lerp(494,290,pk)}`;
  $('armL').innerHTML=lim(aL,20,C_ST)+`<circle cx="${aL.split(' ').pop().split(',')[0]}" cy="${aL.split(',').pop()}" r="3" fill="none"/>`;$('armR').innerHTML=lim(aR,20,C_ST);
  // the stream down the food pipe: milk, then water
  let sOn=0;[[milkT,'#f6fbff',.97],[watT,'#aee0f6',.8]].forEach(([t,col,op])=>{if(t>=0&&t<1.2){sOn=1;const a=eo(P(t,0,.5))*980,b=eio(P(t,.7,1.2))*980;const e=$('stream');e.setAttribute('stroke',col);e.setAttribute('stroke-width',48);e.setAttribute('opacity',op);e.setAttribute('stroke-dasharray',`${Math.max(1,a-b).toFixed(0)} 3000`);e.setAttribute('stroke-dashoffset',(-b).toFixed(0));}});
  if(!sOn)show('stream',0);
  // the pool: white milk, then thin and watery
  let pool='';if(milkT>.35){const lv=lerp(lerp(660,486,eo(P(milkT,.35,1.2))),436,watT>0?eo(P(watT,.4,1.4)):0),k=watT>0?eo(P(watT,.4,1.6)):0;
    let d=`M100,${lv}`;for(let x=100;x<=780;x+=40)d+=` L${x},${(lv+Math.sin(x*.03+T*2.6)*(5+(watT>0&&watT<1.6?8:0))).toFixed(1)}`;d+=' L780,720 L100,720 Z';
    pool=`<path d="${d}" fill="#fff" opacity="${(1-k).toFixed(2)}"/><path d="${d}" fill="#e9d6ea" opacity="${(k*.86).toFixed(2)}"/><path d="${d}" fill="none" stroke="${k>.5?'#cdb5d6':'#d9e6ee'}" stroke-width="4"/>`;
    if(watT>.3&&watT<2.2)for(let j=0;j<6;j++){const q=((watT*1.3+j/6)%1);pool+=`<circle cx="${300+j*70}" cy="${(lv+30+q*90).toFixed(0)}" r="${10+j%3*5}" fill="#fff" opacity="${(.6*(1-q)).toFixed(2)}"/>`;}}
  $('pool').innerHTML=pool;
  let stm='';if(milkT>.9&&watT<0){const o=clamp(P(milkT,.9,1.3))*.75;for(let j=0;j<3;j++){const q=((T*.45+j/3)%1),x=360+j*120,y=470-q*150;stm+=`<path d="M${x},${y} q16,-22 0,-44 q-16,-22 0,-44" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" opacity="${(o*(1-q)).toFixed(2)}"/>`;}}
  $('steam').innerHTML=stm;
  // spoon and lick
  show('spoon',spoonOn?1:0);if(spoonOn)mv('spoon',414,484,-14+Math.sin(T*8)*5,eob(P(T,E.spoon,E.spoon+.25)));
  const lick=T>=E.spoon+.25&&T<E.spoon+.95;show('tongue',lick?1:0);if(lick)$('tongue').setAttribute('transform',`rotate(${(Math.sin((T-E.spoon)*14)*24).toFixed(1)},0,84)`);
  // phone
  show('phone',phoneOn?1:0);if(phoneOn)mv('phone',lerp(700,690,pk),lerp(520,262,pk),0,pk);show('pArcs',pulse(T,inL('07_intestine',T,0,0)));
  // the face
  const yum=milkT>.6&&watT<0;show('sSpark',yum?1:0);show('sEyes',yum?0:1);
  let f={dx:0,dy:34,lid:.12,bA:0,arch:4,mood:.2,small:false};                           // reading
  if(!tossed){f.dx=Math.sin(T*2.2)*14;if(dadOn)f={dx:-26,dy:-30,lid:0,bA:6,arch:8,mood:.3,small:false};}
  else if(milkT<0)f={dx:-20,dy:-26,lid:0,bA:8,arch:9,mood:1,small:false};                // chow time: looks up
  else if(watT<0)f={dx:-8,dy:30,lid:0,bA:6,arch:9,mood:1,small:false};
  else if(T<ST['05_stomach']-.2)f={dx:watT<1.2?-24:-4,dy:watT<1.2?-10:6,lid:0,bA:-18,arch:9,mood:-1,small:true};   // whoa, water
  else if(T<E.phone)f={dx:0,dy:36,lid:.28,bA:16,arch:2,mood:-.9,small:false};             // look at my food
  else if(inL('07_intestine',T))f={dx:26,dy:2,lid:.05,bA:-14,arch:8,mood:-.6,small:false};
  else f={dx:8,dy:4,lid:0,bA:-20,arch:8,mood:-.9,small:T>=ST['08_stomach']};
  face('st',36,{...f,blink:yum?0:blinkK(T,1.1),bx:44,by:-56,bw:36,talk:lick?0:sT,mw:13,T,seed:1});
  const hop=tossed&&T<E.toss+.5?-Math.sin(P(T,E.toss,E.toss+.5)*Math.PI)*16:0,shk=watT>0&&watT<.8?Math.sin(T*50)*5:0;
  $('sface').setAttribute('transform',`translate(${(540+shk).toFixed(1)},${(250+hop+Math.sin(T*2.2)*4).toFixed(1)}) scale(1.28)`);}
// ---------- scene 2: the intestine ----------
function renderGut(T){const t=T-E.gut,fx=-60+eo(P(t,.15,1.0))*900,sink=eio(P(t,1.5,2.6)),yt=lerp(450,940,sink),yb=1000;
  let d=`M-60,${yt}`;for(let x=-60;x<=fx;x+=40)d+=` L${x},${(yt+Math.sin(x*.025+T*5)*10).toFixed(1)}`;d+=` L${fx},${yt} C${fx+70},${(yt+yb)/2-60} ${fx+70},${(yt+yb)/2+60} ${fx},${yb} L-60,${yb} Z`;
  let s=`<path d="${d}" fill="#f7e6ea" opacity="${(1-sink*.35).toFixed(2)}"/>`;
  for(let j=0;j<7;j++){const x=((j*137+T*260)%900)-80,y=yt+40+((j*71)%Math.max(60,yb-yt-80));if(x<fx-40)s+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} q40,-18 80,0 q40,18 80,0" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" opacity="${(.9-sink*.5).toFixed(2)}"/>`;}
  if(t>1.4)for(let j=0;j<9;j++){const q=((t*1.2+j/9)%1);s+=`<path transform="translate(${40+j*80},${(yt-10-q*90).toFixed(0)}) scale(2.4)" d="M0,-9 C5,-2 7,3 5,7 C3,11 -4,11 -5,7 C-7,3 -4,-2 0,-9Z" fill="#cfeaf7" stroke="${INK}" stroke-width="1" opacity="${(1-q).toFixed(2)}"/>`;}
  $('flood').innerHTML=s;
  let f={dx:-30,dy:20,lid:0,bA:-14,arch:9,mood:-.6,small:true};
  if(t>1.0)f={dx:0,dy:34,lid:.34,bA:20,arch:2,mood:-1,small:false};
  const strain=t>1.6;
  face('gt',38,{...f,blink:strain?1:0,bx:46,by:-58,bw:38,talk:0,mw:14,T,seed:3});
  $('gface').setAttribute('transform',`translate(${(360+(strain?Math.sin(T*46)*5:0)).toFixed(1)},${(214+Math.sin(T*3)*3).toFixed(1)})`);}
// ---------- the people ----------
function babyAnim(id,T){const tw=Math.sin(T*1.7)>.2?Math.sin(T*26)*4:0;
  $(id+'_head').setAttribute('transform',`translate(-34,-22) rotate(${tw.toFixed(1)})`);$(id+'_arm').setAttribute('transform',`rotate(${(tw*3).toFixed(1)},14,2)`);
  $(id+'_pL').setAttribute('cx',(-5+Math.sin(T*9)*1.5).toFixed(1));$(id+'_pL').setAttribute('cy',-5);$(id+'_pR').setAttribute('cx',(5+Math.cos(T*11)*1.5).toFixed(1));$(id+'_pR').setAttribute('cy',5);}
function dadPose(T,home){const dT=speak('dad',T);
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,(home?-5:2)+(dT>.2?Math.sin(T*7)*2:0));
  $('pBrows').setAttribute('d','M-36,64 Q-24,62 -10,56 M8,56 Q22,62 34,64');
  setMouthV('pat_m',dT,10,-.5,T,6);const look=home?(speak('mom',T)>0||inL('10_mom',T)||inL('12_mom',T)?5:-4):4;setHEye('pEyeL',look,blinkK(T,2.1));setHEye('pEyeR',look,blinkK(T,2.1));
  show('patBlush',0);show('pSweat',home?0:1);if(!home)$('pSweat').setAttribute('transform',`translate(46,${(60+((T*30)%30)).toFixed(0)}) scale(1.3)`);
  const P3=home?[[-84,234],[-136,336],[-34,412+Math.sin(T*2.2)*2]]:[[-84,234],[-100,370],[-92,468]];const d=limbD(P3,[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(P3[2][0],P3[2][1]+(home?0:12),home?-100:-8,1.2,PSK);
  show('dadBaby',home?1:0);show('glass',home?1:0);if(home)babyAnim('bb1',T);
  $('dadArmR').setAttribute('transform',home?`rotate(${(Math.sin(T*1.7)*2+(dT>.3?Math.sin(T*6)*2:0)).toFixed(1)},84,234)`:'rotate(40,84,234)');}
function renderHome(T){$('dadL').setAttribute('transform',`translate(${(260+Math.sin(T*1.1)*2).toFixed(1)},262) scale(1.18)`);dadPose(T,true);
  show('spArcs',pulse(T,inL('10_mom',T,0,0)||inL('12_mom',T,0,0)));
  $('spk').setAttribute('transform',`translate(0,${(inL('10_mom',T,0,0)||inL('12_mom',T,0,0)?Math.sin(T*30)*2:0).toFixed(1)})`);}
function renderClinic(T){$('dadL').setAttribute('transform',`translate(${(330+Math.sin(T*1.1)*2).toFixed(1)},400) scale(.95)`);dadPose(T,false);
  const dT=speak('doctor',T);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,-2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  setMouthV('doc_m',dT,10,-.1,T,5);setHEye('dEyeL',-3,blinkK(T,.7));setHEye('dEyeR',-3,blinkK(T,.7));
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
  setHEye('mEyeL',dT>0?4:1,blinkK(T,1.6));setHEye('mEyeR',dT>0?4:1,blinkK(T,1.6));
  $('momHead').setAttribute('transform',`rotate(${(Math.sin(T*1.2)*1.5).toFixed(2)},-8,-230) translate(0,${(Math.sin(T*2.4)*1.5).toFixed(1)})`);
  $('momMouth').setAttribute('ry',(5+Math.abs(Math.sin(T*1.3))*2).toFixed(1));babyAnim('bb2',T);}
function caption(T,sc){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const y0={1:1010,2:1010,3:1150,4:1200}[sc];c.setAttribute('y',y0+17);const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,${y0}) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,${-y0})`);}
window.render=function(T){
  const sc=T<E.gut?1:(T<E.home?2:(T<E.clinic?3:4));
  const vis={s1:sc===1,s2:sc===2,s3:sc===3,s4b:sc===4,s4f:sc===4,dadL:sc>=3};for(const k in vis)$(k).setAttribute('display',vis[k]?'inline':'none');
  if(sc===1)renderStomach(T);if(sc===2)renderGut(T);if(sc===3)renderHome(T);if(sc===4)renderClinic(T);
  $('cam').setAttribute('transform',`translate(360,640) scale(${(1.012+Math.sin(T*1.4)*.012).toFixed(4)}) translate(-360,-640)`);
  lab('lbA',T,0,E.toss,250,640);lab('lbM',T,E.milk+.2,E.spoon,170,440);lab('lbW',T,E.water+.2,ST['05_stomach'],170,440);lab('lbD',T,ST['05_stomach'],E.phone,420,700);lab('lbI',T,E.gut+.1,E.home,360,380);
  caption(T,sc);};
window.render(0);

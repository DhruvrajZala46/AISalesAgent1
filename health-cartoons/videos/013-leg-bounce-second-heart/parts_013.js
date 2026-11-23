// =============== 013: "Why is bouncing your leg good for you?" Our own story (the elevator in the leg), 012 style. ===============
const E=D.ev, ST=D.start, END=D.end, TAPS=E.taps;
let RP=false;                                     // true while the doctor's words replay the leg (no mouths move, no story acting)
const spk=(who,T)=>RP?0:speak(who,T);
//__VISEME__
const lend=id=>{const L=D.lines.find(l=>l.id===id);return L.t0+L.dur;};
const inL=(id,T,pre=.05,post=.1)=>T>=ST[id]-pre&&T<lend(id)+post;
const ss=(a,b,x)=>{const k=clamp((x-a)/(b-a));return k*k*(3-2*k);};
const win=(y,a,b)=>ss(a-70,a,y)*(1-ss(b,b+70,y));

// ---------- scenes ----------
let S1=`<g id="s1"><g id="cam">${legWorld()}</g>
 ${labelBox('lbVein','VEIN',560,470,26)}${labelBox('lbHeart','TO THE HEART',420,72,22)}${labelBox('lbCalf','CALF MUSCLE',480,404,24)}${labelBox('lbValve','VALVE',196,560,26)}${labelBox('lb2nd','SECOND HEART',452,372,25)}${labelBox('lbOne','ONE-WAY VALVE',132,797,24)}${heartIcon('hrt')}
 <g id="shout" opacity="0"><path d="${Array.from({length:24},(_,i)=>{const a=i/24*Math.PI*2,r=i%2?62:96;return (i?'L':'M')+(Math.cos(a)*r*1.25).toFixed(1)+','+(Math.sin(a)*r).toFixed(1);}).join(' ')}Z" fill="#fff" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/>
  <text text-anchor="middle" y="24" style="font-family:LG,sans-serif;font-size:74px" fill="#ff7a66" stroke="${INK}" stroke-width="3">!!</text></g></g>`;
let S3=`<g id="s3">${clinicRoom13()}<g transform="translate(190,580) scale(1.5)">${doctorSVG()}</g><g id="patWrap"><g transform="translate(565,720) scale(1.6)">${patientSVG()}</g></g>${studyCard()}</g>`;
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S3+`<text id="wm" x="60" y="168" style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:24px" fill="#fff" stroke="#0b6e6b" stroke-width=".6" opacity=".5">@DrMiraExplains</text>`
 +`<g id="capg"><text id="cap" class="cap" x="360" y="1015" text-anchor="middle" style="stroke-width:7px;font-size:48px"></text></g>`;

// ---------- the bounce: the heel taps the floor 4 times a second ----------
function bounceB(T){ if(T<E.bounce||T>=E.stop) return 0; const ph=((T-E.bounce)%.25)/.25, amp=lerp(.55,1,P(T,E.bounce,E.bounce+1.2));
  return Math.pow(Math.sin(Math.PI*ph),.8)*amp; }
const UP_TAPS=TAPS.filter(t=>t>=E.up-.01);
function U(T){let u=0;for(const t of UP_TAPS){if(T<=t)break;u+=62*eo(P(T,t,t+.17));}return u;}   // how far the column has been pumped up

// ---------- the small blood cells ----------
const CELLS=[];
for(let r=0;r<6;r++){const y=826-r*28;(r%2?[-15,15]:[-30,0,30]).forEach((x,j)=>CELLS.push({x,y,rot:(rnd(r*7+j)-.5)*50}));}
CELLS.sort((a,b)=>a.y-b.y||a.x-b.x);                                   // the top of the pile leaves first, one cell per tap
CELLS.forEach((c,i)=>{c.dep=UP_TAPS[Math.min(i,UP_TAPS.length-1)];c.u0=U(c.dep);});
const LAST=CELLS.length-2;                                              // the cell that squeezes in from below at the start
function flowPos(i,T){const c=CELLS[i];const u=Math.max(0,U(T)-c.u0);let y=c.y-u;y=((y+256)%1116+1116)%1116-256;
  const k=clamp(u/80);return {x:lerp(VX(c.y)+c.x,VX(y)+(i%2?18:-18),k),y,rot:c.rot+u*.6};}
const REST=(()=>{const arr=CELLS.map((c,i)=>({i,p:flowPos(i,E.stop)}));const by=(a,b)=>b.p.y-a.p.y;
  const A=arr.filter(a=>a.p.y<150).sort(by),B=arr.filter(a=>a.p.y>=150&&a.p.y<470).sort(by),C=arr.filter(a=>a.p.y>=470).sort(by);
  const SL=CELLS.slice().sort((a,b)=>b.y-a.y),out=[];
  A.forEach((a,k)=>out[a.i]={x:VX(100)+(k%2?21:-21),y:102-Math.floor(k/2)*35});
  B.forEach((a,k)=>out[a.i]={x:VX(380)+(k%2?21:-21)+(Math.floor(k/2)%2?6:-4),y:388-Math.floor(k/2)*33});out.nB=B.length;
  C.forEach((a,k)=>out[a.i]={x:VX(SL[k].y)+SL[k].x,y:SL[k].y});return out;})();
const A_LAND=REST.nB?388-Math.ceil(REST.nB/2)*33-12:366, A_HANG=212, T_LAND=E.stop+1.3;   // cell A lands on the cells the gate has caught
function cellPos(i,T){const c=CELLS[i];
  if(T<c.dep){const b=bounceB(T),bump=Math.sin(clamp(P(T,E.drop,E.land+.25))*Math.PI);
    let y=c.y-b*6*(1+(i%3)*.3)-bump*8*(c.y<800?1:.5),x=VX(c.y)+c.x;
    if(i===LAST){const k=eo(P(T,E.drop,E.land));y=lerp(900,y,k);}
    return {x,y,rot:c.rot+b*8};}
  if(T<E.stop) return flowPos(i,T);
  const p=flowPos(i,E.stop),q=REST[i],dist=Math.abs(q.y-p.y),f=P(T,E.stop+.1,E.stop+.4+dist/800);
  return {x:lerp(p.x,q.x,f),y:lerp(p.y,q.y,f*f),rot:p.rot+f*40};}

// ---------- the two cells with faces ----------
function heroA(T){let x=398,y=654,sx=1,sy=1,rot=0;const b=bounceB(T);
  [ST['01_cell']+.55,ST['01_cell']+.85,ST['03_cell']+.15].forEach(t0=>{const k=Math.sin(clamp(P(T,t0-.09,t0+.15))*Math.PI);x-=k*10;y-=k*20;rot-=k*12;});
  y-=Math.sin(clamp(P(T,E.drop,E.land+.25))*Math.PI)*8;
  if(T<E.shut-.95){y-=b*7;}
  else if(T<E.stop){const r1=eio(P(T,E.shut-.95,E.shut-.4)),r2=eio(P(T,E.shut-.4,E.shut-.02)),r3=P(T,E.shut,E.stop);
    const r4=eio(P(T,E.shut,E.shut+1.4));y=lerp(654,548,r1);y=lerp(y,360,r2);y=lerp(y,A_HANG+10,r4)-(r3>0?b*10:0);x=lerp(398,VX(y),r1);if(r2>0&&r2<1){sx=.8;sy=1.16;}}
  else {const f=P(T,E.stop+.3,T_LAND),g=Math.pow(f,2.4);y=lerp(A_HANG+10,A_LAND,g);x=VX(y)+(f<1?Math.sin(T*46)*4.5*(1-g):0);rot=f<1?Math.sin(T*23)*9*(1-g):0;
    if(f>0&&f<1){sy=1+.1*f;sx=1-.07*f;}
    const t=T-T_LAND,w=f>=1?Math.exp(-t*8)*Math.cos(t*20):0;if(f>=1){sy=1-.24*w;sx=1+.16*w;}
    if(!RP&&T>=ST['13_cell']+1.2&&inL('13_cell',T,0,0)) y-=Math.abs(Math.sin((T-ST['13_cell'])*10))*10*speak('cell',T);}
  return {x,y,sx,sy,rot};}
function heroB(T){let x=424,y=606,sx=1,sy=1;const b=bounceB(T),bump=Math.sin(clamp(P(T,E.drop,E.land+.25))*Math.PI);
  y-=bump*11;sy=1-.1*bump;sx=1+.08*bump;
  if(T<E.up) y-=b*8; else {const r=P(T,E.up,E.up+2.1);y=lerp(606,-120,eio(r)*.5+r*.5);x=lerp(424,VX(y),clamp(r*4));}
  return {x,y,sx,sy,rot:0};}
function setHero(id,p,{talk=0,T=0,dx=0,dy=0,mood=.2,worry=0,happy=0,seed=0,lid=.08,small=false}={}){
  $(id).setAttribute('transform',`translate(${p.x.toFixed(1)},${p.y.toFixed(1)}) rotate(${(p.rot||0).toFixed(1)}) scale(${(p.sx||1).toFixed(3)},${(p.sy||1).toFixed(3)})`);
  const bl=blinkK(T,seed*1.3+.2);setOEye(id+'_eL',9,{dx,dy,lid,blink:bl,small});setOEye(id+'_eR',9,{dx,dy,lid,blink:bl,small});
  setBrow(id+'_bL',-10.8,-18-worry*2,11,-worry*18+happy*6,2+happy*3);setBrow(id+'_bR',10.8,-18-worry*2,11,worry*18-happy*6,2+happy*3);
  setMouthV(id+'_m',talk,8,mood,T,seed);}

// ---------- vein, valves ----------
function leafD(hx,hy,tipx,tipy,side){const mx=(hx+tipx)/2;
  return `M${hx.toFixed(1)},${hy} Q${mx.toFixed(1)},${(hy-4).toFixed(1)} ${tipx.toFixed(1)},${tipy.toFixed(1)} Q${(mx-side*5).toFixed(1)},${((hy-26+tipy)/2-9).toFixed(1)} ${hx.toFixed(1)},${hy-28} Z`;}
function drawValve(idL,idR,hy,o,wHalf){const c=VX(hy),lx=c-wHalf,rx=c+wHalf;
  const tl=[lerp(c-1,lx+11,o),lerp(hy-46,hy-54,o)],tr2=[lerp(c+1,rx-11,o),lerp(hy-46,hy-54,o)];
  $(idL).setAttribute('d',leafD(lx,hy,tl[0],tl[1],1));$(idR).setAttribute('d',leafD(rx,hy,tr2[0],tr2[1],-1));}
function drawVein(sq,pk){const L=[],R=[];for(let y=-440;y<=880;y+=40){const w=46+9*pk*win(y,640,860)-9*sq*win(y,170,700),c=VX(y);L.push([c-w,y]);R.push([c+w,y]);}
  const d=smooth(L)+' L'+smooth(R.slice().reverse()).slice(1)+'Z';['veinO','veinW','veinL','lumClipP'].forEach(id=>$(id).setAttribute('d',d));
  $('veinShine').setAttribute('d',smooth(L.map(([x,y])=>[x+13,y])));
  return y=>46+9*pk*win(y,640,860)-9*sq*win(y,170,700);}

// ---------- the camera: close on the stuck cells, then our own shots ----------
const CAM=[[0,2.0,398,650,0],[E.zoomOut,1,360,640,.8],[E.two,1.6,420,600,.5],[E.calfCam,1.5,480,300,.6],[E.gateCam,1.9,404,470,.5],[E.bounce,1,360,640,.5],
  [ST['07_calf']-.1,1.35,470,400,.45],[E.up-.05,1.2,400,640,.25],[E.up+.3,1.2,400,380,1.3],[E.shut-.25,1.9,404,470,.3],[E.flex-.05,1.6,500,310,.4],
  [E.shout-.1,1,360,640,.45],[E.stop+.3,1.6,405,440,.4]];
function camAt(T){let s=CAM[0][1],x=CAM[0][2],y=CAM[0][3];for(let i=1;i<CAM.length;i++){const [t,ks,kx,ky,d]=CAM[i];if(T<t)break;const k=eio(P(T,t,t+d));s=lerp(s,ks,k);x=lerp(x,kx,k);y=lerp(y,ky,k);}return [s,x,y];}

function renderLeg(T,camOv){
  const b=bounceB(T),lifting=T>=E.up&&T<E.stop,stopped=T>=E.stop;
  const sq=(T>=ST['08_calf']&&!stopped)?b:0;
  const pk=T<E.up?1:(stopped?.55*P(T,E.stop+.4,E.stop+1.2):1-P(T,E.up,E.up+2.5));
  // the outside: the leg rides up as the heel lifts, the sneaker turns about its toes, the couch shakes
  $('legG').setAttribute('transform',`translate(0,${(-21*b).toFixed(2)})`);
  $('shoeG').setAttribute('transform',`rotate(${(-4.2*b).toFixed(3)},110,1112)`);
  $('couch').setAttribute('transform',`translate(${(b*2.2).toFixed(2)},${(-b*1.5).toFixed(2)})`);
  $('shadow').setAttribute('opacity',(.14-.05*b).toFixed(3));
  let im='';if(T>=E.bounce&&!stopped){const ph=(T-E.bounce)%.25;if(ph<.11){const o=(1-ph/.11).toFixed(2);im=`<path d="M552,1126 q12,9 26,2 M566,1140 q9,6 20,1" fill="none" stroke="${INK}" stroke-width="3.2" stroke-linecap="round" opacity="${o}"/>`;}}
  $('impact').innerHTML=im;
  // the vein and the calf's squeeze
  const wAt=drawVein(sq,pk);
  $('calfG').setAttribute('transform',`translate(604,300) scale(${(1+.055*sq).toFixed(4)},${(1-.012*sq).toFixed(4)}) translate(-604,-300)`);
  // valves: closed while he sits still; they open on every squeeze and snap shut in between
  let oL=0,oU=0;if(lifting){const p=clamp((b-.2)/.4);oL=Math.max(p,T<E.up+.9?1:0);oU=T>E.up+.5?Math.max(p,T<E.up+2?1:0):0;
    if(T>=E.shut-.4&&T<E.shut-.02)oL=1;if(T>=E.shut&&T<E.shut+.32)oL=0;}
  drawValve('gvL','gvR',530,oL,wAt(530));drawValve('uvL','uvR',172,oU,wAt(172));
  // small cells
  let h='';for(let i=0;i<CELLS.length;i++){const p=cellPos(i,T);h+=smallCell(p.x,p.y,18,p.rot);}
  $('cellsG').innerHTML=h;
  // the call button: amber (and it flashes when jabbed), green while the lift runs, red when it stops
  const jab=[ST['01_cell']+.55,ST['01_cell']+.85,ST['03_cell']+.15].some(t0=>T>=t0&&T<t0+.16);
  $('btn').setAttribute('fill',stopped?'#e0454f':(lifting?'#3ecf6e':(jab?'#fff3c4':'#f2b340')));
  // heroes
  const aT=spk('cell',T),bT=spk('cell2',T),pa=heroA(T),pb=heroB(T);
  const aUp=T>=ST['03_cell']-.1&&T<E.bounce, aPanic=T<ST['03_cell']||stopped;
  setHero('hA',pa,{talk:aT,T,seed:1,dx:T<ST['02_cell2']?-22:(aUp?22:(stopped?0:10)),dy:T<ST['02_cell2']?4:(stopped?(T<T_LAND?24:-26):(aUp?-26:(lifting?-22:6))),
    mood:stopped?-.7:(lifting?.8:-.3),worry:aPanic?1:(lifting?0:.4),happy:lifting?1:0,small:stopped&&T<T_LAND+.25});
  const bConf=T>=E.bounce&&T<ST['07_calf'];
  setHero('hB',pb,{talk:bT,T,seed:2,dx:T<E.bounce?-10:0,dy:bConf?28:(T>=E.up?-28:(T<ST['03_cell']?-8:-20)),mood:T>=E.up?1:-.5,worry:T>=E.up?0:.8,happy:T>=E.up?1:0,lid:inL('02_cell2',T)?.3:.08});
  show('hB',T<E.up+2.15?1:0);
  // the gate (valve)
  const gT=spk('gate',T),T_CAP=REST.nB?E.stop+.5:T_LAND,landed=T>=T_CAP;
  setOEye('gEyeL',13,{dx:landed?0:(T>=ST['03_cell']&&T<ST['05_gate']?24:0),dy:landed?-34:(lifting?14:6),lid:.44,blink:blinkK(T,2.2)});
  setOEye('gEyeR',13,{dx:landed?0:(T>=ST['03_cell']&&T<ST['05_gate']?24:0),dy:landed?-34:(lifting?14:6),lid:.44,blink:blinkK(T,2.2)});
  setBrow('gBrL',392,424,16,landed?16:6,1);setBrow('gBrR',428,424,16,landed?-16:-6,1);
  setMouthV('gate_m',gT,7,-.35,T,3);
  const capK=landed?.42+.2*Math.exp(-(T-T_CAP)*7):1;
  $('gateCap').setAttribute('transform',`translate(410,410) scale(${landed?1.12:1},${capK.toFixed(3)}) translate(-410,-410)`);
  // the calf
  const cT=spk('calf',T),smug=!RP&&T>=E.flex-.1&&T<E.shout,excited=RP?!stopped:(T>=ST['07_calf']-.1&&T<E.shut),startled=!RP&&T>=E.shout&&!stopped,sad=!RP&&stopped;
  const lazy=T<E.bounce;
  let cdx=-24,cdy=18,clid=.42;
  if(inL('05_gate',T)){cdx=-34;cdy=26;}
  if(T>=E.bounce&&T<ST['07_calf']-.1){cdx=Math.sin(T*5)*26;cdy=30;clid=.12;}
  if(excited){cdx=-14;cdy=inL('08_calf',T)?10:22;clid=0;}
  if(T>=E.shut&&T<E.flex-.1){cdx=-30;cdy=14;clid=.15;}
  if(smug){cdx=-4;cdy=2;clid=.4;}
  if(startled){cdx=-10;cdy=-34;clid=0;}
  if(sad){cdx=-20;cdy=-20;clid=.3;}
  const cbl=blinkK(T,.6);
  setOEye('cEyeL',25,{dx:cdx,dy:cdy,lid:clid,blink:cbl,small:startled});setOEye('cEyeR',25,{dx:cdx,dy:cdy,lid:clid,blink:cbl,small:startled});
  setBrow('cBrL',508,240-(excited||startled?8:0),30,sad?-14:(smug?-4:(excited&&inL('08_calf',T)?14:(lazy?4:0))),smug?7:(excited?8:3));
  setBrow('cBrR',562,240-(excited||startled?8:0)-(smug?9:0),30,sad?14:(smug?-10:(excited&&inL('08_calf',T)?-14:(lazy?-4:0))),smug?9:(excited?8:3));
  setMouthV('calf_m',cT,16,smug?.95:(excited?.8:(sad?-.7:(lazy?-.25:.1))),T,4);
  $('calfFace').setAttribute('transform',`translate(0,${(Math.sin(T*1.4)*1.5-cT*2).toFixed(2)})`);
  let sp='';if(smug){[[474,238,0],[606,262,1],[598,344,2],[478,352,3],[540,176,4]].forEach(([x,y,j])=>{const k=.5+.5*Math.sin(T*7+j*1.9),r=7+9*k;
      sp+=`<path d="M${x},${y-r} Q${x+2},${y-2} ${x+r},${y} Q${x+2},${y+2} ${x},${y+r} Q${x-2},${y+2} ${x-r},${y} Q${x-2},${y-2} ${x},${y-r}Z" fill="#fff" stroke="${INK}" stroke-width="2" opacity="${(.5+.5*k).toFixed(2)}"/>`;});}
  $('sparks').innerHTML=sp;
  // camera
  const [s,cx,cy]=camOv||camAt(T);$('cam').setAttribute('transform',`translate(360,640) scale(${s.toFixed(4)}) translate(${(-cx).toFixed(2)},${(-cy).toFixed(2)})`);
  // labels (each pops while its shot is held) and the off-screen shout
  popLabel('lbVein',T,.95,E.zoomOut-.1,566,470);popLabel('lbHeart',T,ST['03_cell']+.9,E.calfCam-.05,352,112);
  popLabel('lb2nd',RP?-1:T,E.second,E.shout-.15,452,372);
  popLabel('lbCalf',T,E.calfCam+.65,ST['05_gate']-.35,476,404);popLabel('lbValve',T,E.gateCam+.6,E.bounce-.1,180,566);
  const shOn=!RP&&T>=E.shout&&T<E.stop+.15;show('shout',shOn?1:0);
  if(shOn){const k=eob(P(T,E.shout,E.shout+.22));$('shout').setAttribute('transform',`translate(${190+Math.sin(T*38)*3},${318+Math.cos(T*31)*3}) rotate(${-8+Math.sin(T*9)*3}) scale(${k.toFixed(3)})`);}
}
// ---------- Dr. Mira's clinic ----------
function renderClinic(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['15_doctor'];
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0));
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  const nod=T>=lend('18_doctor')-.9?Math.sin(clamp(P(T,lend('18_doctor')-.9,lend('18_doctor')+.3))*Math.PI*2)*4:0;
  let pr=-3+Math.sin(T*.8)*1+nod;if(pT>.2)pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  $('pBrows').setAttribute('d',T<d0?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70');
  setMouthV('doc_m',dT,10,.5,T,5);setMouthV('pat_m',pT,10,T>=ST['18_doctor']?.5:-.2,T,6);
  const dLook=T>=E.walk+.25?3+Math.min(3,(T-E.walk)*4):3;setHEye('dEyeL',dLook,blinkK(T,.7));setHEye('dEyeR',dLook,blinkK(T,.7));setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',.3);show('pSweat',0);
  // he is still bouncing his leg while he asks (his whole body jiggles), and stops to listen
  const jig=(1-P(T,d0+.2,d0+.8))*Math.pow(Math.abs(Math.sin((T-E.clinic)*Math.PI*4)),.8)*5;
  const up=eob(P(T,E.getUp,E.getUp+.4))*46, wk=Math.max(0,T-E.walk), wx=wk*wk*230+wk*150, wb=wk>0?Math.abs(Math.sin(wk*Math.PI/.28))*16:0;   // "Get up and walk": he does
  $('patWrap').setAttribute('transform',`translate(${wx.toFixed(1)},${(-jig-up-wb).toFixed(2)})`);
  // the study card: two legs after three hours of sitting
  const cOn=T>=E.card0&&T<E.card1+.16;show('card',cOn?1:0);show('wm',cOn?0:.5);
  if(cOn){const k=eob(P(T,E.card0,E.card0+.3))*(1-P(T,E.card1,E.card1+.16));$('card').setAttribute('transform',`translate(360,300) scale(${Math.max(.001,k).toFixed(3)}) translate(-360,-300)`);
    const ph=((T-E.card0)%.25)/.25,fb=Math.pow(Math.sin(Math.PI*ph),.8);
    $('mlF_leg').setAttribute('transform',`translate(0,${(-24*fb).toFixed(2)})`);$('mlF_shoe').setAttribute('transform',`rotate(${(-4.8*fb).toFixed(3)},110,1112)`);
    $('mlF_imp').innerHTML=ph<.45?`<path d="M560,1124 q14,10 32,2 M578,1146 q11,8 26,1 M556,1090 q16,-4 30,-16" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round" opacity="${(1-ph/.45).toFixed(2)}"/>`:'';
    const a1=T>=E.arrDown,a2=T>=E.arrUp;show('arrD',a1?1:0);show('arrU',a2?1:0);show('tD',a1?1:0);show('tU',a2?1:0);
    if(a1){const k1=eob(P(T,E.arrDown,E.arrDown+.28));$('arrD').setAttribute('transform',`translate(296,${(272+Math.abs(Math.sin((T-E.arrDown)*3.2))*12).toFixed(1)}) scale(${k1.toFixed(3)})`);}
    if(a2){const k2=eob(P(T,E.arrUp,E.arrUp+.28));$('arrU').setAttribute('transform',`translate(584,${(284-Math.abs(Math.sin((T-E.arrUp)*3.2))*12).toFixed(1)}) scale(${k2.toFixed(3)})`);}}
  const sh=[-84,234],el=[-108,356],wr=[-100,470];const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+8,10,1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.2?-6+Math.sin(T*4.2)*7*dT:0).toFixed(2)},86,226)`);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.1){w=x[2];ws=x[0];}}}
  const c=$('cap');c.textContent=w;const k=eo(P(T,ws,ws+.12));c.setAttribute('transform',`translate(360,998) scale(${lerp(1.4,1,k).toFixed(3)}) translate(-360,-998)`);}
// while the doctor explains, we go back inside the leg: the squeeze, then the valves catching the blood
function renderReplay(T){RP=true;const tR=E.stop+(T-E.rpStop),k=P(T,E.rp0,E.rpCut),k2=P(T,E.rpCut,E.rp1);
  renderLeg(tR,T<E.rpCut?[lerp(1.28,1.36,k),430,lerp(410,395,k)]:[1.6,420,lerp(338,352,k2)]);RP=false;
  const hOn=T>=E.rpHeart&&T<E.rpCut;show('hrt',hOn?1:0);
  if(hOn){const kk=eob(P(T,E.rpHeart,E.rpHeart+.25)),beat=1+.13*Math.pow(Math.abs(Math.sin((T-E.rpHeart)*Math.PI/.5)),6);$('hrt').setAttribute('transform',`translate(350,150) scale(${(kk*beat).toFixed(3)})`);}
  popLabel('lbOne',T,E.rpCut+.3,E.rp1,132,797);}
window.render=function(T){
  const rp=T>=E.rp0&&T<E.rp1, sc=(T<E.clinic||rp)?1:3;
  $('s1').setAttribute('display',sc===1?'inline':'none');$('s3').setAttribute('display',sc===3?'inline':'none');
  if(sc===1){if(rp)renderReplay(T);else{show('hrt',0);show('lbOne',0);renderLeg(T);}}else renderClinic(T);
  caption(T);
};
window.render(0);

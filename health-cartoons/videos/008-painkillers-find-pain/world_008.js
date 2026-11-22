// =============== 008 worlds: ALL code, in the 001 / 003-v1 style (thin INK lines, shaded(), muted colours, objects with faces) ===============
const STW='#ee9ea3', STW_S='#d47c86', LUM='#f9c8c2', LUM_S='#eaa39f', JUICE='#e9c97c', JUICE_S='#c9a654';
const FLESH='#ec9a90', FLESH_S='#d07a72', FLOOR='#f2a6a3', FLOOR_S='#d98785';
function closedD(pts){return smooth(pts.concat([pts[0],pts[1]]))+'Z';}
function tubeL(d,w,fill,shade,id=''){return `<path ${id?`id="${id}"`:''} d="${d}" fill="none" stroke="${INK}" stroke-width="${w+5.2}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${fill}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${shade}" stroke-width="${(w*.22).toFixed(1)}" stroke-linecap="round" stroke-linejoin="round" opacity=".55" transform="translate(0,${(w*.28).toFixed(1)})"/>`;}
function hose(id){return `<g id="${id}"><path id="${id}_o" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="${id}_i" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"/><g id="${id}_h"></g></g>`;}
function setHose(id,pts,rot,s=1){const d=smooth(pts);$(id+'_o').setAttribute('d',d);$(id+'_i').setAttribute('d',d);const e=pts[pts.length-1];$(id+'_h').innerHTML=glove(e[0],e[1],rot,s);}
function wrinkles(n,x0,x1,y0,y1,col,seed){let s='';for(let i=0;i<n;i++){const x=x0+rnd(seed+i)*(x1-x0),y=y0+rnd(seed+i+50)*(y1-y0),h=60+rnd(seed+i+90)*140;
  s+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} c${(rnd(i+7)*16-8).toFixed(0)},${(h*.3).toFixed(0)} ${(rnd(i+9)*20-10).toFixed(0)},${(h*.6).toFixed(0)} ${(rnd(i+11)*12-6).toFixed(0)},${h.toFixed(0)}" ${TH(col)} stroke-width="2.4"/>`;}return s;}

// ---------- characters ----------
// painkiller capsule with a face (pill2 wears a pink bow)
function pillSVG(id,bow=false){return `<g id="${id}"><g id="${id}_b">${leg(-16,84,34,4)}${leg(16,84,34,-4)}
  <path d="M-36,0 L-36,-48 A36,36 0 0 1 36,-48 L36,0Z" fill="#e2474b" ${STK}/><path d="M-36,0 L-36,48 A36,36 0 0 0 36,48 L36,0Z" fill="#f8f6f2" ${STK}/>
  <path d="M-22,-62 C-14,-74 6,-78 18,-72" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".55"/><path d="M22,10 L22,52" stroke="#e3ded6" stroke-width="5" stroke-linecap="round"/>
  <g transform="translate(-14,-44)">${oEye(id+'_eL',13,'#e2474b')}</g><g transform="translate(14,-44)">${oEye(id+'_eR',13,'#e2474b')}</g>${brow(id+'_bL')}${brow(id+'_bR')}
  ${mouthEl(id+'_m',0,-16)}
  ${bow?`<g transform="translate(-20,-80) rotate(-18)"><path d="M0,0 L-22,-14 L-22,14Z M0,0 L22,-14 L22,14Z" fill="#f06aa6" ${LN2}/><circle r="6" fill="#d94b8c" ${LN2}/></g>`:''}
  </g>${hose(id+'_aL')}${hose(id+'_aR')}</g>`;}
function setPill(id,x,y,s,{talk=0,T=0,look=0,lookY=0,mood=.4,rot=0,arms='down',seed=0,angry=0,run=0}={}){
  const hop=run?Math.abs(Math.sin(T*16+seed))*14:0;
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${(y-hop).toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${s})`);
  const bl=blinkK(T,seed*.7+.2); setOEye(id+'_eL',13,{dx:look*40,dy:lookY*40,lid:.1,blink:bl}); setOEye(id+'_eR',13,{dx:look*40,dy:lookY*40,lid:.1,blink:bl});
  setBrow(id+'_bL',-14,-62+angry*3,16,angry*18,2); setBrow(id+'_bR',14,-62+angry*3,16,-angry*18,2);
  setMouthV(id+'_m',talk,9,mood,T,seed);
  const w=Math.sin(T*4+seed)*5, sw=run?Math.sin(T*16+seed)*16:0;
  const A={down:[[[-36,4],[-54,30],[-58,58+w]],[[36,4],[54,30],[58,58-w]],40,-40],
           wave:[[[-36,4],[-56,24],[-60,56]],[[36,4],[62,-20],[70,-62+w]],40,-150],
           point:[[[-36,4],[-54,30],[-58,58]],[[36,4],[72,-2],[104,-10]],40,-90],
           fist:[[[-36,4],[-66,-10],[-80,-40+w]],[[36,4],[66,-10],[80,-40-w]],150,-150],
           run:[[[-36,4],[-56,20+sw],[-62,40+sw]],[[36,4],[56,20-sw],[62,40-sw]],40,-40]}[arms];
  setHose(id+'_aL',A[0],A[2],.62); setHose(id+'_aR',A[1],A[3],.62);}
// red blood cell with eyes
function rbcSVG(id){return `<g id="${id}">${shaded('M-52,0 C-52,-30 -28,-46 0,-46 C28,-46 52,-30 52,0 C52,30 28,46 0,46 C-28,46 -52,30 -52,0Z','#e2474b','#c3363c',12)}
  <ellipse rx="28" ry="22" fill="#cc3a41" opacity=".55"/><path d="M-30,-28 C-18,-38 4,-40 16,-36" fill="none" stroke="#ff9a9d" stroke-width="5" stroke-linecap="round"/>
  <g transform="translate(-14,-8)">${oEye(id+'_eL',13,'#e2474b')}</g><g transform="translate(14,-8)">${oEye(id+'_eR',13,'#e2474b')}</g></g>`;}
// prostaglandin: a spiky magenta ball (the pain messenger)
function prostSVG(id){let sp='';for(let i=0;i<10;i++){const a=i/10*Math.PI*2-.2,x=Math.cos(a)*84,y=Math.sin(a)*80,x2=Math.cos(a)*112,y2=Math.sin(a)*108;
   sp+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} L${x2.toFixed(0)},${y2.toFixed(0)}" stroke="${INK}" stroke-width="11" stroke-linecap="round"/><path d="M${x.toFixed(0)},${y.toFixed(0)} L${x2.toFixed(0)},${y2.toFixed(0)}" stroke="#d63c95" stroke-width="6.5" stroke-linecap="round"/><circle cx="${x2.toFixed(0)}" cy="${y2.toFixed(0)}" r="13" fill="#e46aae" ${LN2}/>`;}
  return `<g id="${id}"><g id="${id}_sp">${sp}</g>${shaded('M-90,0 C-90,-52 -50,-88 0,-88 C50,-88 90,-52 90,0 C90,52 50,88 0,88 C-50,88 -90,52 -90,0Z','#dc4a9c','#b52d7c',18)}
  <path d="M-54,-52 C-34,-70 0,-74 22,-68" fill="none" stroke="#f7a3cf" stroke-width="6" stroke-linecap="round"/>
  <g id="${id}_face"><g transform="translate(-26,-16)">${oEye(id+'_eL',22,'#dc4a9c')}</g><g transform="translate(26,-16)">${oEye(id+'_eR',22,'#dc4a9c')}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,30)}</g>
  <g id="${id}_ko" opacity="0"><path d="M-40,-30 l26,26 M-14,-30 l-26,26 M14,-30 l26,26 M40,-30 l-26,26" stroke="${INK}" stroke-width="5" stroke-linecap="round"/><path d="M-16,30 Q0,40 16,30" fill="none" ${LN}/><path d="M4,34 q8,18 18,6" fill="#e88a8f" ${LN2}/></g>
  ${hose(id+'_aL')}${hose(id+'_aR')}</g>`;}
function setProst(id,x,y,s,{talk=0,T=0,look=0,mood=.2,rot=0,ko=0,angry=0}={}){
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${s})`);
  $(id+'_sp').setAttribute('transform',`rotate(${(Math.sin(T*3)*4).toFixed(1)})`);
  show(id+'_face',ko?0:1); show(id+'_ko',ko?1:0);
  const bl=blinkK(T,1.7); setOEye(id+'_eL',22,{dx:look*40,dy:2,lid:.15,blink:bl}); setOEye(id+'_eR',22,{dx:look*40,dy:2,lid:.15,blink:bl});
  setBrow(id+'_bL',-26,-46,26,angry*20,3); setBrow(id+'_bR',26,-46,26,-angry*20,3);
  setMouthV(id+'_m',talk,16,mood,T,4);
  const w=Math.sin(T*4)*6;
  if(ko){setHose(id+'_aL',[[-84,10],[-120,30],[-140,60]],20,.8);setHose(id+'_aR',[[84,10],[120,30],[140,60]],-20,.8);}
  else if(talk>.05){setHose(id+'_aL',[[-84,10],[-122,-10],[-136,-50+w]],60,.8);setHose(id+'_aR',[[84,10],[122,-10],[136,-50-w]],-60,.8);}
  else {setHose(id+'_aL',[[-84,10],[-114,40],[-104,74+w]],0,.8);setHose(id+'_aR',[[84,10],[114,40],[104,74-w]],0,.8);}}

// ---------------- SCENE A / E: inside the foot, the cut (later boarded up by the platelets) ----------------
const GASH='M258,-60 L346,-60 C338,300 322,640 306,968 L270,968 C266,640 260,300 258,-60Z';
function cutWorld(){
  let s=`<g id="wCut"><rect x="-200" y="-200" width="1120" height="1680" fill="${FLESH}"/>
   <path d="M-200,-200 H920 V1480 H-200Z M-60,-60 C200,-90 520,-90 780,-60 L780,1340 L-60,1340Z" fill="${FLESH_S}" opacity=".45" filter="url(#soft)"/>
   ${wrinkles(26,-40,760,-40,860,'#c76c66',3)}
   <g id="bloodTrail"></g>
   ${shaded(GASH,'#fbe5d0','#e6c0a2',18)}
   <path d="M290,40 C292,300 286,600 280,900" fill="none" stroke="#fff6ea" stroke-width="8" stroke-linecap="round" opacity=".8"/>
   ${shaded('M-200,968 C40,948 200,986 360,966 C520,948 640,980 920,962 L920,1480 L-200,1480Z',FLOOR,FLOOR_S,20)}
   ${Array.from({length:14},(_,i)=>`<path d="M${(i*58-20+rnd(i+300)*20).toFixed(0)},${(1010+rnd(i+310)*240).toFixed(0)} q22,-10 44,0" ${TH('#e08f8c')} stroke-width="3"/>`).join('')}
   <g id="drips"></g>
   <g id="planks" opacity="0">${[[300,-10,320],[296,8,500],[292,-6,680]].map(([x,r,y],i)=>`<g transform="translate(${x},${y}) rotate(${r})">${shaded('M-112,-26 L112,-26 C118,-26 120,-20 120,-14 L120,14 C120,22 116,26 110,26 L-112,26 C-118,26 -120,20 -120,14 L-120,-14 C-120,-22 -116,-26 -112,-26Z','#deb985','#c29c63',10)}
     <path d="M-96,-8 C-50,-14 10,-2 90,-10 M-90,10 C-30,4 40,14 96,6" ${TH('#b98d55')} stroke-width="2.4"/><circle cx="-98" cy="0" r="5" fill="#9aa3ad" ${LN2}/><circle cx="98" cy="0" r="5" fill="#9aa3ad" ${LN2}/></g>`).join('')}</g>
   ${rbcSVG('rb0')}${rbcSVG('rb1')}${rbcSVG('rb2')}
   ${prostSVG('pg')}${guardSVG('gd')}${pillSVG('pA')}${pillSVG('pB',true)}
   <g id="dust"></g><g id="stars"></g></g>`;
  return s;}

// ---------------- SCENE B: the stomach (asleep under an eye mask; the painkillers drop in) ----------------
const STOM_OUT=[[384,318],[420,402],[452,494],[502,574],[562,606],[614,598],[648,572],[678,558],[702,568],[702,608],[670,654],[618,726],[548,802],[448,854],[338,848],[246,798],[184,706],[162,594],[172,472],[210,372],[264,310],[314,292],[344,298]];
const STOM_LUM=[[358,330],[392,410],[422,500],[472,590],[548,634],[620,628],[668,594],[688,596],[676,624],[630,688],[562,762],[454,814],[352,810],[278,768],[250,714],[292,666],[352,624],[384,544],[376,446],[356,370]];
const CAP_PATH=[[356,-60],[356,80],[357,200],[360,320],[384,400],[410,480],[432,570],[444,660],[440,700]];
function stomachWorld(){
  DEFS+=`<clipPath id="lumClip"><path d="${closedD(STOM_LUM)}"/></clipPath>`;
  let s=`<g id="wStomach"><rect x="-200" y="-200" width="1120" height="1680" fill="#f6d6cb"/>
  <path d="M-200,-200 H920 V1480 H-200Z M-40,60 C80,20 640,20 760,60 L760,1340 L-40,1340Z" fill="#e9b8ab" opacity=".5" filter="url(#soft)"/>
  <path d="M-60,-60 H780 V150 C620,96 480,86 360,86 C240,86 100,96 -60,150Z" fill="#f5c0c6"/>
  ${shaded('M-60,150 C100,96 240,86 360,86 C480,86 620,96 780,150 L780,196 C620,142 480,132 360,132 C240,132 100,142 -60,196Z','#dc7c82','#c2616a',10)}
  ${shaded('M-60,170 C80,150 250,160 330,206 C300,262 240,300 190,334 C120,382 40,420 -60,452Z','#c8716a','#a8564f',16)}`;
  {const pts=[];[904,986,1068,1150,1232,1314].forEach((y,r)=>{const xs=r%2?[690,560,420,280,140,44]:[44,140,280,420,560,690];xs.forEach((x,k)=>pts.push([x,y+Math.sin(k*1.3+r)*14]));});
   s+=tubeL(smooth(pts),70,'#f1aca2','#d68d86');}
  s+=tubeL('M698,588 C744,640 748,760 700,860',46,'#f3aea6','#da8e88');
  s+=tubeL('M356,-80 C356,60 356,200 362,326',62,STW,STW_S)+`<path d="M356,-80 C356,60 356,200 362,326" fill="none" stroke="${LUM}" stroke-width="24" stroke-linecap="round"/>`;
  s+=`<g id="stoBody">${shaded(closedD(STOM_OUT),STW,STW_S,26)}
   <path d="M200,420 C190,500 200,600 236,680" fill="none" stroke="#f8c0c3" stroke-width="10" stroke-linecap="round" opacity=".7"/>
   ${shaded(closedD(STOM_LUM),LUM,LUM_S,30)}
   <g clip-path="url(#lumClip)">
    ${[[300,690,120],[330,740,170],[420,780,190],[520,700,150],[560,660,110],[420,520,90]].map(([x,y,w],i)=>`<path d="M${x-w/2},${y} q${w/4},-14 ${w/2},0 t${w/2},0" ${TH(i%2?'#e3999a':'#df9294')} stroke-width="2.6"/>`).join('')}
    <g id="juice"><path id="juiceD" fill="${JUICE}"/><path id="juiceH" fill="none" stroke="#fbf0c8" stroke-width="4" stroke-linecap="round"/><g id="bubbles"></g></g>
    <g id="swirl" opacity="0"></g>
    ${pillSVG('sA')}${pillSVG('sB',true)}
   </g>
   <path d="${closedD(STOM_LUM)}" fill="none" ${LN}/>
   <g id="stoFace"><g transform="translate(226,454)">${oEye('sEyeL',36,STW)}</g><g transform="translate(306,446)">${oEye('sEyeR',36,STW)}</g>${brow('sBrowL')}${brow('sBrowR')}
    <ellipse cx="206" cy="520" rx="16" ry="9" fill="#e9838f" opacity=".45"/><ellipse cx="330" cy="512" rx="14" ry="8" fill="#e9838f" opacity=".45"/>
    ${mouthEl('sto_m',266,532)}
    <g id="sMask"><path d="M178,420 C200,404 330,398 356,414 C364,440 356,476 340,482 C300,470 230,476 196,486 C180,472 174,440 178,420Z" fill="#7aa6d6" ${LN}/><path d="M188,430 C230,416 320,412 348,424" ${TH('#a9c8ea')} stroke-width="4"/>
     <path d="M178,426 C150,420 140,440 150,452 M356,418 C380,410 392,426 384,440" fill="none" stroke="#5f86b8" stroke-width="6" stroke-linecap="round"/></g>
    <g id="zzz"></g></g>
   <g id="stick" opacity="0"><path d="M0,0 L0,330" stroke="${INK}" stroke-width="13" stroke-linecap="round"/><path d="M0,0 L0,330" stroke="#f4efe6" stroke-width="8" stroke-linecap="round"/><path d="M-3,10 L-3,320" stroke="#e45b62" stroke-width="2.5" stroke-dasharray="14 14"/></g>
   ${hose('sArmL')}${hose('sArmR')}</g>`;
  s+=`</g>`;return s;}

// ---------------- SCENE C: riding a vein ----------------
function veinWorld(){
  let s=`<g id="wVein"><rect x="-200" y="-200" width="1120" height="1680" fill="#ef9f96"/>
   ${Array.from({length:10},(_,i)=>{const x=-40+i*90,y=rnd(i+500)*1280;return `<path d="M${x},${y.toFixed(0)} c40,${(rnd(i+510)*80-40).toFixed(0)} 80,${(rnd(i+520)*80).toFixed(0)} 140,${(rnd(i+530)*60-30).toFixed(0)} m-60,10 c10,30 30,50 20,90" ${TH('#d45f5b')} stroke-width="5"/>`;}).join('')}
   ${tubeL('M-120,980 C160,900 300,740 420,620 C540,500 660,420 860,360',330,'#f3aab2','#d98692')}
   <path d="M-120,930 C160,850 300,690 420,570 C540,450 660,370 860,310" fill="none" stroke="#fbd0d4" stroke-width="16" stroke-linecap="round" opacity=".8"/>
   ${Array.from({length:7},(_,i)=>`<path d="M${(-40+i*130).toFixed(0)},${(960-i*95).toFixed(0)} q30,-22 60,-30" ${TH('#e597a2')} stroke-width="3"/>`).join('')}
   <g id="vRbc">${rbcSVG('vr0')}${rbcSVG('vr1')}</g>${pillSVG('vA')}${pillSVG('vB',true)}<g id="speed"></g></g>`;
  return s;}

// ---------------- SCENE D: a fork in the tunnel ----------------
function forkWorld(){
  DEFS+=`<radialGradient id="holeG" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#3e0d16"/><stop offset=".7" stop-color="#6e1a28"/><stop offset="1" stop-color="#a43344"/></radialGradient>`;
  let s=`<g id="wFork"><rect x="-200" y="-200" width="1120" height="1680" fill="#f4a8aa"/>
   ${wrinkles(18,-40,760,-40,700,'#d77c80',40)}
   <g id="holes"><path d="M-40,140 C20,80 230,60 300,180 C340,260 330,700 300,880 L-40,900Z" fill="url(#holeG)" ${LN}/>
   <path d="M760,120 C700,70 480,60 420,180 C384,260 392,700 420,880 L760,900Z" fill="url(#holeG)" ${LN}/>
   <path d="M300,180 C340,260 330,700 300,880 M420,180 C384,260 392,700 420,880" fill="none" stroke="#f9c3c4" stroke-width="10" stroke-linecap="round" opacity=".7"/></g><g id="specks"></g>
   ${shaded('M-200,900 C60,870 220,930 360,904 C520,878 640,920 920,890 L920,1480 L-200,1480Z','#f6b5b6','#dd9395',20)}
   ${Array.from({length:12},(_,i)=>`<path d="M${(i*64-10+rnd(i+600)*20).toFixed(0)},${(960+rnd(i+610)*260).toFixed(0)} q24,-12 48,0" ${TH('#e69a9c')} stroke-width="3"/>`).join('')}
   ${pillSVG('fA')}${pillSVG('fB',true)}</g>`;
  return s;}

// ---------------- the brain on the phone (inset) ----------------
function brainInset(){return `<g id="bInset" opacity="0"><g id="bInset_i"><circle r="150" fill="#e6f1f6" ${LN}/><clipPath id="binClip"><circle r="146"/></clipPath>
  <g clip-path="url(#binClip)"><path d="M-150,90 L150,90 L150,160 L-150,160Z" fill="#cfe2ea"/>
   ${shaded('M-110,20 C-120,-40 -80,-86 -20,-90 C30,-96 90,-80 110,-30 C126,10 110,56 70,66 C20,76 -40,74 -80,62 C-104,54 -108,40 -110,20Z','#f4a8b6','#da8396',14)}
   ${[-60,-28,6,40].map((x,i)=>`<path d="M${x},-80 c${i%2?14:-10},20 ${i%2?-6:12},40 ${i%2?8:-4},62" ${TH('#c96f84')} stroke-width="3.2"/>`).join('')}
   <path d="M-96,0 C-60,-12 -30,6 0,-6 C30,-16 60,0 96,-10" ${TH('#c96f84')} stroke-width="3.2"/>
   <g transform="translate(-30,8)">${oEye('brEyeL',20,'#f4a8b6')}</g><g transform="translate(18,6)">${oEye('brEyeR',20,'#f4a8b6')}</g>${mouthEl('brain_m',-6,44)}
   <path d="M76,30 C110,20 118,-20 96,-40" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M76,30 C110,20 118,-20 96,-40" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round"/>
   <g transform="translate(92,-44) rotate(-30) scale(1.1)"><path d="M-30,-34 C-40,-30 -42,-14 -34,-8 L-24,-2 C-18,4 -12,0 -10,-6 L-6,-14 C-2,-22 -8,-28 -14,-30 Z" fill="#e2474b" ${LN2}/><path d="M14,24 C24,30 40,26 44,16 L46,4 C46,-4 38,-6 32,-2 L22,4 C16,8 14,16 14,24 Z" fill="#e2474b" ${LN2}/><path d="M-30,-14 C-14,8 8,20 30,6" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M-30,-14 C-14,8 8,20 30,6" fill="none" stroke="#e2474b" stroke-width="8" stroke-linecap="round"/></g>
  </g><circle r="150" fill="none" ${LN}/><g id="waves"></g></g></g>`;}

// ---------------- clinic extras ----------------
function painPoster(){return `<g transform="translate(560,250)"><rect x="-92" y="-118" width="184" height="236" fill="#fbfaf7" ${LN}/><rect x="-80" y="-106" width="160" height="182" fill="#eaf3f6"/>
  <path d="M-40,-80 C-30,-60 -34,-10 -30,40 C-28,58 -8,64 10,60 C40,54 58,44 60,30 C62,16 40,14 20,16 C6,18 -6,10 -8,-10 L-12,-80Z" fill="#f2cbb2" ${LN2}/>
  <path d="M26,22 l10,-16 l6,14 l12,-18" fill="none" stroke="#e0454f" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="-62" y="86" width="124" height="10" rx="3" fill="#8fb2bf"/><rect x="-44" y="100" width="88" height="8" rx="3" fill="#bcd2da"/></g>`;}
function glassAt(x,y,s=1){return `<g transform="translate(${x},${y}) scale(${s})"><path d="M-16,-26 L16,-26 L12,24 C12,28 -12,28 -12,24Z" fill="#e6f4fa" ${LN2} opacity=".95"/><path d="M-14,-6 L14,-6 L12,22 C12,25 -12,25 -12,22Z" fill="#a9d6ea"/><path d="M-9,-20 L-8,16" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>`;}

// =============== 007 v2 worlds, drawn in the 001 / 003-v1 code style ===============
// The user's references for this version: 001 (ear, cotton bud) and 003 v1 (food out the nose), both fully code-drawn:
// clean anatomy, thin INK lines, airbrushed inner shading (shaded()), muted colours, cream background, objects with faces.
const CAV='#f6d6cb', CAV_S='#e9b8ab';
const STW='#ee9ea3', STW_S='#d47c86', LUM='#f9c8c2', LUM_S='#eaa39f';
const JUICE='#dcd56f', JUICE_S='#bfb64f', LIV='#c8716a', LIV_S='#a8564f', SI='#f3aea6', SI_S='#da8e88';
function closedD(pts){return smooth(pts.concat([pts[0],pts[1]]))+'Z';}
function tubeL(d,w,fill,shade,id=''){return `<path ${id?`id="${id}"`:''} d="${d}" fill="none" stroke="${INK}" stroke-width="${w+5.2}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${fill}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${shade}" stroke-width="${(w*.22).toFixed(1)}" stroke-linecap="round" stroke-linejoin="round" opacity=".55" transform="translate(0,${(w*.28).toFixed(1)})"/>`;}
// white rubber-hose arm (like the brain's arm in 003 v1) + mitten glove
function hose(id){return `<g id="${id}"><path id="${id}_o" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="${id}_i" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"/><g id="${id}_h"></g></g>`;}
function setHose(id,pts,rot,s=1){const d=smooth(pts);$(id+'_o').setAttribute('d',d);$(id+'_i').setAttribute('d',d);const e=pts[pts.length-1];$(id+'_h').innerHTML=glove(e[0],e[1],rot,s);}

// ---------------- SCENE 1: the stomach (front view, cut open on the right to show the juice) ----------------
const STOM_OUT=[[384,318],[420,402],[452,494],[502,574],[562,606],[614,598],[648,572],[678,558],[702,568],[702,608],[670,654],[618,726],[548,802],[448,854],[338,848],[246,798],[184,706],[162,594],[172,472],[210,372],[264,310],[314,292],[344,298]];
const STOM_LUM=[[358,330],[392,410],[422,500],[472,590],[548,634],[620,628],[668,594],[688,596],[676,624],[630,688],[562,762],[454,814],[352,810],[278,768],[250,714],[292,666],[352,624],[384,544],[376,446],[356,370]];
const CAP_PATH=[[356,-60],[356,80],[357,200],[360,320],[384,400],[410,480],[432,570],[444,660],[440,730]];
const BUDC=[150,1000];
function stomachWorld(){
  DEFS+=`<clipPath id="lumClip"><path d="${closedD(STOM_LUM)}"/></clipPath>`;
  let s=`<g id="wStomach"><rect x="-200" y="-200" width="1120" height="1680" fill="${CAV}"/>
  <path d="M-200,-200 H920 V1480 H-200Z M-40,60 C80,20 640,20 760,60 L760,1340 L-40,1340Z" fill="${CAV_S}" opacity=".5" filter="url(#soft)"/>`;
  // lungs above the diaphragm, then the diaphragm dome
  s+=`<path d="M-60,-60 H780 V150 C620,96 480,86 360,86 C240,86 100,96 -60,150Z" fill="#f5c0c6"/>
   ${[[60,30],[150,60],[240,24],[480,30],[570,64],[660,28],[110,100],[620,104]].map(([x,y])=>`<path d="M${x-14},${y} a14,12 0 0 1 28,0" ${TH('#dc9aa3')}/>`).join('')}
   ${shaded('M-60,150 C100,96 240,86 360,86 C480,86 620,96 780,150 L780,196 C620,142 480,132 360,132 C240,132 100,142 -60,196Z','#dc7c82','#c2616a',10)}
   ${[0,1,2,3,4,5,6,7,8].map(i=>{const x=-20+i*90;return `<path d="M${x},${150-Math.sin((x+60)/840*Math.PI)*58} l14,40" ${TH('#c2616a')}/>`;}).join('')}`;
  // liver (top left, behind the stomach) and the background gut coils (bottom)
  s+=shaded('M-60,170 C80,150 250,160 330,206 C300,262 240,300 190,334 C120,382 40,420 -60,452Z',LIV,LIV_S,16);
  s+=`<path d="M40,250 C90,236 160,236 210,250" ${TH('#e3948c')} stroke-width="3"/>`;
  // small intestine: one long tube winding left-right with U-turns (reads as coiled gut, not stripes)
  {const pts=[];[904,986,1068,1150,1232,1314].forEach((y,r)=>{const xs=r%2?[690,560,420,280,140,44]:[44,140,280,420,560,690];
     xs.forEach((x,k)=>pts.push([x,y+Math.sin(k*1.3+r)*14]));});
   s+=tubeL(smooth(pts),70,'#f1aca2','#d68d86');
   pts.forEach((p,k)=>{if(k%3===1)s+=`<path d="M${p[0]-20},${p[1]-10} q20,-10 40,0" ${TH('#fbd0c8')} stroke-width="3"/>`;});}
  // duodenum: from the pylorus down the right edge into the coils
  s+=tubeL('M698,588 C744,640 748,760 700,860',46,SI,SI_S);
  // food pipe (cut open: we see the inside strip where the capsules slide)
  s+=tubeL('M356,-80 C356,60 356,200 362,326',62,STW,STW_S)+`<path d="M356,-80 C356,60 356,200 362,326" fill="none" stroke="${LUM}" stroke-width="24" stroke-linecap="round"/><path d="M356,-80 C356,60 356,200 362,326" fill="none" ${TH(LUM_S)} stroke-width="2"/>`;
  // the stomach: body with a face (left), cut open on the right
  s+=`<g id="stoBody">${shaded(closedD(STOM_OUT),STW,STW_S,26)}
   <path d="M200,420 C190,500 200,600 236,680" fill="none" stroke="#f8c0c3" stroke-width="10" stroke-linecap="round" opacity=".7"/>
   ${shaded(closedD(STOM_LUM),LUM,LUM_S,30)}
   <g clip-path="url(#lumClip)">
    ${[[300,690,120],[330,740,170],[420,780,190],[520,700,150],[560,660,110],[420,520,90]].map(([x,y,w],i)=>`<path d="M${x-w/2},${y} q${w/4},-14 ${w/2},0 t${w/2},0" ${TH(i%2?'#e3999a':'#df9294')} stroke-width="2.6"/>`).join('')}
    <g id="juice"><path id="juiceD" fill="${JUICE}"/><path id="juiceH" fill="none" stroke="#f4efb0" stroke-width="4" stroke-linecap="round"/><g id="bubbles"></g></g>
    <g id="burnGlow" opacity="0"><ellipse cx="460" cy="800" rx="200" ry="70" fill="#ff5a2a" filter="url(#soft)"/></g>
    <g id="caps">${capsule('cp0')}${capsule('cp1')}${capsule('cp2')}</g>
   </g>
   <path d="${closedD(STOM_LUM)}" fill="none" ${LN}/>
   <g id="stoFace"><g transform="translate(226,454)">${oEye('sEyeL',36,STW)}</g><g transform="translate(306,446)">${oEye('sEyeR',36,STW)}</g>${brow('sBrowL')}${brow('sBrowR')}
    <ellipse cx="206" cy="520" rx="16" ry="9" fill="#e9838f" opacity=".45"/><ellipse cx="330" cy="512" rx="14" ry="8" fill="#e9838f" opacity=".45"/>
    ${mouthEl('sto_m',266,532)}<path id="sweat" d="M0,-12 C6,-3 9,4 7,9 C5,14 -5,14 -7,9 C-9,4 -6,-3 0,-12Z" fill="#9fd8f5" ${LN2} opacity="0"/></g>
   ${hose('sArmL')}${hose('sArmR')}</g>
   <g id="steam1"></g>`;
  // the small-intestine buddy (bottom left): a coiled tube with a face
  s+=`<g id="bud"><g id="budBody">${shaded('M40,1000 C40,930 100,900 156,902 C220,904 268,940 268,1004 C268,1066 220,1104 156,1104 C90,1104 40,1066 40,1000Z',SI,SI_S,18)}
    <path d="${smooth([[156,1004],[176,1000],[184,1020],[160,1040],[124,1028],[118,992],[150,960],[200,966],[226,1010],[210,1060],[150,1076],[90,1050],[72,1000],[92,948]])}" ${TH('#c97770')} stroke-width="3.6"/>
    <g transform="translate(128,958)">${oEye('uEyeL',24,SI)}</g><g transform="translate(184,954)">${oEye('uEyeR',24,SI)}</g>${brow('uBrowL')}${brow('uBrowR')}
    ${mouthEl('bud_m',156,1000)}</g>${hose('uArmL')}${hose('uArmR')}</g>`;
  s+=`</g>`;
  return s;}
const S1_POSE={base:{L:[[176,540],[130,580],[116,646]],R:[[330,372],[380,342],[408,362]],rl:-10,rr:30},
  point:{L:[[176,540],[134,540],[150,600]],R:[[330,372],[348,300],[344,226]],rl:-40,rr:-20},
  shout:{L:[[176,540],[112,470],[90,394]],R:[[330,372],[392,312],[444,262]],rl:-60,rr:40},
  smug:{L:[[176,540],[130,580],[116,646]],R:[[330,372],[398,400],[426,456]],rl:-10,rr:110},
  panic:{L:[[176,540],[142,508],[178,470]],R:[[330,372],[372,420],[348,470]],rl:30,rr:-30}};
function poseLerp(a,b,k){return a.map((p,i)=>[lerp(p[0],b[i][0],k),lerp(p[1],b[i][1],k)]);}
function renderStomach(T){
  const [pz,p0]=poseAt(T,[[ST['02_stomach']-.1,ST['03_stomach']-.1,'point'],[ST['03_stomach']-.1,ST['04_buddy'],'shout'],[ST['05_stomach']-.1,ST['06_buddy'],'point'],
     [ST['07_stomach']-.1,T_SKIN,'smug'],[ST['20_stomach']-.3,1e9,'panic']],'base');
  const se=speak('stomach',T), pk=popK(T,p0), P0=S1_POSE[pz], k=eo(P(T,p0,p0+.22)), PB=S1_POSE.base;
  const w=Math.sin(T*3.2)*5;
  setHose('sArmL',poseLerp(PB.L,P0.L,k).map((p,i)=>i?[p[0],p[1]+w*i*.4]:p),P0.rl,1.05);
  setHose('sArmR',poseLerp(PB.R,P0.R,k).map((p,i)=>i?[p[0]+w*i*.3,p[1]]:p),P0.rr,1.05);
  const sy=1+Math.sin(T*2.6)*.008+se*.018-pk*.03, rot=pz==='shout'?Math.sin(T*22)*.7:Math.sin(T*1.1)*.6;
  tr('stoBody',0,0,1,1,0); $('stoBody').setAttribute('transform',`translate(430,850) rotate(${rot.toFixed(2)}) scale(${(1+pk*.03).toFixed(4)},${sy.toFixed(4)}) translate(-430,-850)`);
  // face: eyes look at what matters (the capsule, the buddy), brows/lids/mouth by mood
  const lookBud=(T>=ST['04_buddy']-.2&&T<ST['07_stomach'])&&!(T>=ST['05_stomach']-.1&&T<ST['06_buddy']-.2);
  const capT=(T>=E.drop-.2&&T<E.drop+1.2)||(T>=E.drop2-.2&&T<E.drop2+1.2);
  let dx=lookBud?-18:(capT?20:6), dy=lookBud?30:(capT?-26:2); if(pz==='shout') {dx=0;dy=-4;}
  const bl=blinkK(T,.3), lid=pz==='smug'?.42:(pz==='panic'?0:.1);
  setOEye('sEyeL',36,{dx,dy,lid,blink:bl,small:pz==='panic'}); setOEye('sEyeR',36,{dx,dy,lid,blink:bl,small:pz==='panic'});
  const ang={base:[6,-6,6],point:[16,-16,2],shout:[22,-22,0],smug:[-6,10,2],panic:[-18,18,10]}[pz];
  setBrow('sBrowL',224,404-(pz==='panic'?8:0),44,ang[0],ang[2]); setBrow('sBrowR',308,396-(pz==='panic'?8:0),44,ang[1],ang[2]);
  setMouthV('sto_m',se,pz==='shout'?26:20,{base:.2,point:-.6,shout:-1,smug:.9,panic:-1}[pz],T,3);
  const sw=pz==='panic'; show('sweat',sw?1:0); if(sw) $('sweat').setAttribute('transform',`translate(352,${(400+((T*30)%40)).toFixed(1)})`);
  // buddy: bobs, talks, looks up at the stomach
  const be=speak('buddy',T), bpk=popK(T,ST['04_buddy']-.1)+popK(T,ST['06_buddy']-.1);
  $('budBody').setAttribute('transform',`translate(156,1104) scale(${(1+bpk*.04).toFixed(3)},${(1+Math.sin(T*2.4)*.02+be*.03).toFixed(3)}) translate(-156,-1104)`);
  const bbl=blinkK(T,2.2), bud6=T>=ST['06_buddy']-.1&&T<ST['07_stomach'];
  setOEye('uEyeL',24,{dx:14,dy:-20,lid:bud6?.4:.12,blink:bbl}); setOEye('uEyeR',24,{dx:14,dy:-20,lid:bud6?.4:.12,blink:bbl});
  setBrow('uBrowL',126,926,30,bud6?-8:8,3); setBrow('uBrowR',186,922,30,bud6?8:-8,3);
  setMouthV('bud_m',be,13,bud6?-.3:.7,T,7);
  const bw=Math.sin(T*3)*4, talkB=be>.1;
  setHose('uArmL',[[52,1010],[16,1000],[talkB?6:14,talkB?950:1050]],talkB?-30:20,.85);
  setHose('uArmR',[[262,1010],[300,990+bw],[talkB?318:296,talkB?946:1046]],talkB?30:-20,.85);
  // juice surface, bubbles
  let jd='M180,'+(746).toFixed(0);for(let x=180;x<=720;x+=20){jd+=` L${x},${(746+Math.sin(x/34+T*2.2)*5).toFixed(1)}`;}jd+=' L720,900 L180,900Z';
  $('juiceD').setAttribute('d',jd); let jh='';for(let x=200;x<=700;x+=20){jh+=(jh?' L':'M')+`${x},${(742+Math.sin(x/34+T*2.2)*5).toFixed(1)}`;} $('juiceH').setAttribute('d',jh);
  let bb='';for(let i=0;i<7;i++){const u=((T*.5)+i/7)%1;bb+=`<circle cx="${(300+i*52+Math.sin(T*3+i)*6).toFixed(1)}" cy="${(800-u*50).toFixed(1)}" r="${(4+i%3*2)}" fill="none" ${TH(JUICE_S)} opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;} $('bubbles').innerHTML=bb;
  // capsules: 2 at the start, 1 more at drop2; down the food pipe into the juice, then they bob
  [[E.drop,0],[E.drop+.18,1],[E.drop2,2]].forEach(([t0,i])=>{const el=$('cp'+i),q=(T-t0)/.9; if(q<0||(i===2&&T<E.stom2-.1)){el.setAttribute('opacity',0);return;}
    el.setAttribute('opacity',1); const p=q<1?along(CAP_PATH,eio(q)):[410+(i-1)*52,756+Math.sin(T*2+i)*4];
    el.setAttribute('transform',`translate(${p[0].toFixed(1)},${p[1].toFixed(1)}) rotate(${(q<1?q*300:70+i*30+Math.sin(T*2+i)*6).toFixed(1)}) scale(.9)`);});
  const bk=clamp(P(T,E.burn-.2,E.burn+.4))*(1-P(T,T_SKIN-.4,T_SKIN)); show('burnGlow',bk*(.45+.15*Math.sin(T*8)));
  let st='';if(bk>0||(T>E.drop+1&&T<T_SKIN))for(let i=0;i<4;i++){const u=((T*.7)+i/4)%1;st+=`<path d="M${(360+i*48).toFixed(0)},${(760-u*110).toFixed(1)} q10,-14 0,-28 q-10,-14 0,-28" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="${((.25+bk*.6)*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
  $('steam1').innerHTML=st;
}

// ---------------- SCENE 2: the skin (clean cross-section, like 001's ear canal) ----------------
const SURF2=x=>150+8*Math.sin(x/70)+3*Math.sin(x/23), JUNC2=x=>252+9*Math.sin(x/45+1), FAT2=x=>866+10*Math.sin(x/66+.7), VES2=x=>560+12*Math.sin(x/95+.4);
function band(f1,f2){let d='';for(let x=-80;x<=800;x+=16)d+=(d?'L':'M')+x+','+f1(x).toFixed(1)+' ';for(let x=800;x>=-80;x-=16)d+='L'+x+','+f2(x).toFixed(1)+' ';return d+'Z';}
function lineF(f,a=-80,b=800){let d='';for(let x=a;x<=b;x+=16)d+=(d?'L':'M')+x+','+f(x).toFixed(1)+' ';return d;}
function skinWorld(){
  let s=`<g id="tissue"><rect x="-200" y="-200" width="1120" height="1680" fill="#fbf0e2"/>`;
  s+=shaded(band(FAT2,()=>1460),'#f5e3a3','#e3c47c',22);
  for(let r=0;r<6;r++)for(let c=0;c<9;c++){const x=-40+c*100+(r%2)*50+(rnd(r*9+c)-.5)*16, y=930+r*86+(rnd(r*9+c+40)-.5)*12;
    s+=`<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="${(42+rnd(r*9+c+80)*8).toFixed(1)}" ry="${(34+rnd(r*9+c+120)*6).toFixed(1)}" fill="#f8eab8" ${TH('#d9bb72')} stroke-width="2.2"/>`;}
  s+=`<path d="${lineF(FAT2)}" fill="none" ${LN}/>`;
  s+=shaded(band(JUNC2,FAT2),'#efa49c','#d98580',26);
  for(let i=0;i<9;i++){const y0=320+i*60;s+=`<path d="${lineF(x=>y0+10*Math.sin(x/(50+i*7)+i)+4*Math.sin(x/17+i))}" ${TH('#e3928d')} stroke-width="2.2"/>`;}
  // hair follicles (left, right) with their hairs
  [[112,430,-6],[650,400,8]].forEach(([x,b,t],i)=>{const top=SURF2(x);
    s+=`<path d="M${x-16},${top} C${x-16+t},${(top+b)/2} ${x-20+t},${b-20} ${x-24+t},${b} C${x-24+t},${b+30} ${x+24+t},${b+30} ${x+24+t},${b} C${x+20+t},${b-20} ${x+16+t},${(top+b)/2} ${x+16},${top}Z" fill="#f4cdb1" ${LN2}/>
     <ellipse cx="${x+t}" cy="${b+6}" rx="12" ry="9" fill="#e08b86" ${LN2}/><path d="M${x+t},${b} C${x+t*.7},${(top+b)/2} ${x+t*.3},${top+40} ${x+t*.6},${top+60}" fill="none" stroke="${INK}" stroke-width="3.4" stroke-linecap="round"/>
     <path id="hairS${i}" fill="none" stroke="${INK}" stroke-width="3.4" stroke-linecap="round"/>`;});
  // one blood vessel with cells flowing inside
  s+=tubeL(lineF(VES2),40,'#dc5a60','#b83f48')+`<path d="${lineF(x=>VES2(x)-9)}" fill="none" stroke="#f39a9d" stroke-width="5" stroke-linecap="round" opacity=".8"/><g id="rbc2"></g>`;
  s+=shaded(band(SURF2,JUNC2),'#f2c6a8','#dca282',16);
  s+=`<path d="${lineF(x=>SURF2(x)+30)}" ${TH('#e2ad8f')} stroke-width="2.2"/><path d="${lineF(x=>SURF2(x)+62)}" ${TH('#e2ad8f')} stroke-width="2.2"/>`;
  // the cut: a clean V wound, a little swelling, beads of blood
  s+=`<ellipse cx="354" cy="${SURF2(354)+6}" rx="120" ry="34" fill="#ef7f7c" opacity=".35" filter="url(#soft)"/>
  <g id="cut">${shaded(`M294,${SURF2(294)} C304,${SURF2(294)+70} 330,330 352,472 C374,330 400,${SURF2(414)+70} 414,${SURF2(414)}Z`,'#b8434b','#8a2a33',16)}
   <path d="M330,200 C338,260 344,330 350,410" fill="none" stroke="#e47378" stroke-width="5" stroke-linecap="round" opacity=".8"/>
   <circle cx="290" cy="${SURF2(290)-7}" r="8" fill="#d6404a" ${LN2}/><circle cx="418" cy="${SURF2(418)-6}" r="6.5" fill="#d6404a" ${LN2}/></g>`;
  s+=`</g>`;return s;}
function skinAnim(T){
  let a='';for(let i=0;i<8;i++){const x=((T*50+i*108)%864)-72, y=VES2(x)+Math.sin(T*2+i)*3;
    a+=`<ellipse cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" rx="12" ry="8" fill="#e8474f" ${LN2} transform="rotate(${(Math.sin(T*1.7+i)*14).toFixed(1)},${x.toFixed(1)},${y.toFixed(1)})"/>`;}
  $('rbc2').innerHTML=a;
  [[112,-6],[650,8]].forEach(([x,t],i)=>{const sw=Math.sin(T*1.2+i*2)*7, top=SURF2(x);
    $('hairS'+i).setAttribute('d',`M${x+t*.6},${top+60} C${x},${top} ${x+(i?18:-18)+sw},${top-50} ${x+(i?40:-40)+sw},${top-96}`);});
}

// ---------------- clinic extras ----------------
function germPoster(){return `<g transform="translate(560,250)"><rect x="-92" y="-118" width="184" height="236" fill="#fbfaf7" ${LN}/><rect x="-80" y="-106" width="160" height="182" fill="#eaf3f6"/>
  <circle cx="-6" cy="-24" r="58" fill="#fff" ${LN2}/><circle cx="-6" cy="-24" r="50" fill="#e7f4dc"/>
  ${[[-26,-40,0],[14,-14,40],[-14,4,-30],[16,-52,20]].map(([x,y,r])=>`<rect x="${x-14}" y="${y-7}" width="28" height="14" rx="7" fill="#9ccf6a" ${LN2} transform="rotate(${r},${x},${y})"/>`).join('')}
  <path d="M36,18 L70,52" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M36,18 L70,52" stroke="#8a6a4a" stroke-width="7" stroke-linecap="round"/>
  <rect x="-62" y="86" width="124" height="10" rx="3" fill="#8fb2bf"/><rect x="-44" y="100" width="88" height="8" rx="3" fill="#bcd2da"/></g>`;}
function bandageAt(x,y,rot,s=1){return `<g transform="translate(${x},${y}) rotate(${rot}) scale(${s})"><rect x="-20" y="-8" width="40" height="16" rx="5" fill="#fbf6ee" ${LN2}/><path d="M-10,-8 v16 M10,-8 v16" ${TH('#d9cfc4')}/><circle r="3.6" fill="#d6404a" opacity=".55"/></g>`;}

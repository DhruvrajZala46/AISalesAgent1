// =============== 009 v2 worlds: the reference's layout and staging, redrawn in code (our characters) ===============
// v1 was rejected ("5%"): the throat could not be read. v2 copies the reference's anatomy layout 1:1 (measured on its 720x1280 frame):
// open salmon throat, tongue base top-left, the epiglottis as a curved flap rising from the front wall with its face at the base,
// the TRACHEA = the open space behind the front wall (face inside it), the ESOPHAGUS = a narrow tube with an opening at the top,
// a thick back wall and big vertebrae on the right. Thick outlines, high contrast, big eyes.
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const SAL='#f07e7c', WALL='#b9474f', WALL_L='#d4626a', CART='#f3c4c4', MUC='#cf5f60', BONE='#f7e48e', BONE_D='#eebb5e', DISC='#efe2d4';
function hose(id){return `<g id="${id}"><path id="${id}_o" fill="none" stroke="${INK}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/><path id="${id}_i" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><g id="${id}_h"></g></g>`;}
function setHose(id,pts,rot,s=1){const d=smooth(pts);$(id+'_o').setAttribute('d',d);$(id+'_i').setAttribute('d',d);const e=pts[pts.length-1];$(id+'_h').innerHTML=glove(e[0],e[1],rot,s);}
function dots(list){return list.map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${BONE_D}"/>`).join('');}
// a big meat chunk with a spicy red coat (the reference's food chunk, same size)
function chunkSVG(id){return `<g id="${id}"><path d="M-30,-92 C-8,-102 18,-88 24,-62 C42,-50 46,-20 36,0 C48,20 48,54 30,72 C16,94 -12,96 -28,78 C-44,62 -46,30 -38,10 C-50,-10 -48,-40 -40,-56 C-44,-74 -40,-88 -30,-92Z" fill="#d79b72" ${OLW}/>
  <path d="M-38,10 C-30,30 -10,40 10,34 C26,30 36,14 36,0 C48,20 48,54 30,72 C16,94 -12,96 -28,78 C-44,62 -46,30 -38,10Z" fill="#8c4a2b" ${OLW}/>
  <path d="M-20,-70 C-8,-78 8,-74 14,-62" fill="none" stroke="#f3cfae" stroke-width="6" stroke-linecap="round"/>
  ${[[-18,-40],[6,-20],[-24,-6],[18,-48],[-4,56],[20,40]].map(([x,y])=>`<path d="M${x},${y} l9,-4" stroke="#e3262c" stroke-width="5" stroke-linecap="round"/>`).join('')}</g>`;}
function vbody(y0,y1,xl,dl){return `<path d="M${xl+18},${y0} C${xl-6},${y0+10} ${xl-10},${(y0+y1)/2} ${xl},${y1-14} C${xl+6},${y1} ${xl+20},${y1+2} ${xl+40},${y1} L780,${y1} L780,${y0}Z" fill="${BONE}" ${OLW}/>${dots(dl)}`;}
function throatWorld(){
  let s=`<g id="wThroat"><rect x="-200" y="-200" width="1120" height="1680" fill="${SAL}"/>`;
  // spine (right): big vertebral bodies with discs, following the curve of the neck
  s+=vbody(-60,222,600,[[650,40,9],[700,90,7],[660,150,8],[722,180,6],[690,10,6]]);
  s+=`<path d="M582,226 C640,214 720,218 780,226 L780,300 C720,306 640,304 576,300 C566,280 570,240 582,226Z" fill="${DISC}" ${OLW}/>`;
  s+=vbody(302,454,574,[[620,350,8],[672,400,7],[700,340,6],[640,420,6]]);
  s+=`<path d="M584,458 C640,452 720,454 780,458 L780,486 C720,490 640,490 586,486Z" fill="${DISC}" ${OLW}/>`;
  s+=vbody(488,614,586,[[630,530,7],[690,575,8],[660,600,5]]);
  s+=`<path d="M596,618 C650,612 720,614 780,618 L780,646 C720,650 650,650 600,646Z" fill="${DISC}" ${OLW}/>`;
  s+=vbody(648,834,610,[[656,700,8],[712,760,7],[676,800,6],[730,690,5]]);
  s+=`<path d="M624,838 C680,832 730,834 780,838 L780,872 C730,876 680,876 630,872Z" fill="${DISC}" ${OLW}/>`;
  s+=vbody(874,1096,640,[[690,930,8],[740,1000,7],[700,1060,6]]);
  s+=`<path d="M652,1100 C700,1094 740,1096 780,1100 L780,1132 C740,1136 700,1136 656,1132Z" fill="${DISC}" ${OLW}/>`;
  s+=vbody(1134,1340,664,[[710,1190,7],[750,1260,6]]);
  // back wall of the throat
  s+=`<path d="M506,-40 C498,200 510,500 538,800 C558,1000 570,1150 578,1340 L626,1340 C614,1120 602,920 590,720 C578,460 566,220 570,-40Z" fill="${MUC}" ${OLW}/>
   <path d="M514,-30 C506,210 518,505 546,800 C564,1000 576,1150 584,1330" fill="none" stroke="#e98482" stroke-width="10" stroke-linecap="round"/>`;
  // food pipe (esophagus): a narrow tube with its opening at the top
  s+=`<g id="eso"><path d="M372,706 C366,684 384,668 410,668 C438,668 454,686 452,710 C456,840 474,1000 500,1120 C512,1180 528,1240 542,1340 L470,1340 C452,1230 430,1120 412,1000 C396,900 378,800 372,706Z" fill="${WALL}" ${OLW}/>
   <path d="M392,718 C392,698 430,696 434,718 C440,800 442,860 438,914 C432,934 404,934 398,914 C392,860 390,790 392,718Z" fill="#c76b6e" ${OLW}/>
   <path d="M424,960 C440,958 454,1000 462,1060 C468,1110 466,1140 454,1144 C440,1148 432,1110 426,1060 C420,1010 414,962 424,960Z" fill="${CART}" ${OLW}/>
   <ellipse cx="412" cy="684" rx="28" ry="10" fill="#7e2630" ${OLW}/></g>`;
  // front wall of the windpipe with its cartilage rings, and the neck skin in front of it
  s+=`<path d="M-30,632 C40,690 72,800 112,920 C150,1040 176,1160 200,1340 L-30,1340Z" fill="#f4e3d1" ${OLW}/>
   <path d="M-30,632 C40,690 72,800 112,920 C150,1040 176,1160 200,1340 L338,1340 C306,1170 264,1030 234,910 C214,830 216,760 250,704 L240,650 C160,640 60,620 -30,600Z" fill="${WALL}" ${OLW}/>
   <path d="M246,712 C214,766 214,834 236,912 C266,1032 306,1170 334,1330" fill="none" stroke="${WALL_L}" stroke-width="12" stroke-linecap="round"/>
   <g transform="translate(126,872) rotate(-20)"><rect x="-46" y="-130" width="92" height="260" rx="44" fill="${CART}" ${OLW}/></g>
   <g transform="translate(226,1152) rotate(-18)"><rect x="-38" y="-86" width="76" height="172" rx="36" fill="${CART}" ${OLW}/></g>`;
  // tongue base (top left)
  s+=`<path d="M-30,-40 L212,-40 C208,80 192,190 174,262 C162,314 172,340 204,348 L230,354 C196,390 140,420 40,436 L-30,444Z" fill="${WALL}" ${OLW}/>
   <path d="M200,-30 C196,90 182,196 166,262 C156,308 168,334 196,344" fill="none" stroke="${WALL_L}" stroke-width="10" stroke-linecap="round"/>
   <path d="M0,130 l58,-24 M0,282 l52,18 M0,342 l62,30" stroke="${INK}" stroke-width="3.6" stroke-linecap="round"/>`;
  // the epiglottis: the flap (animated) + its root with the hyoid bone and the face
  s+=`<g id="epiG"><path id="flapO" fill="${WALL}" ${OLW}/><path id="flapS1" fill="none" stroke="${INK}" stroke-width="26" stroke-linecap="round"/><path id="flapS2" fill="none" stroke="#f7cdcb" stroke-width="18" stroke-linecap="round"/>
   <path d="M30,700 C14,650 24,592 70,556 C110,526 168,520 214,548 C246,570 252,640 246,700 C230,720 60,724 30,700Z" fill="${WALL}" ${OLW}/>
   <path d="M14,506 C10,462 50,428 110,428 C150,428 166,452 158,480 C150,522 110,552 60,558 C30,562 16,540 14,506Z" fill="${BONE}" ${OLW}/>${dots([[50,470,7],[92,450,6],[118,486,7],[70,520,6],[34,500,5]])}
   <g id="epiFace"><g transform="translate(105,592)">${oEye('eEyeL',40,WALL)}</g><g transform="translate(192,586)">${oEye('eEyeR',40,WALL)}</g>
    <path id="eBrowL" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/><path id="eBrowR" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>
    ${mouthEl('epi_m',150,648)}<g id="grit" opacity="0"><rect x="124" y="638" width="52" height="20" rx="6" fill="#fff" ${OLW}/><path d="M137,638 v20 M150,638 v20 M163,638 v20 M124,648 h52" stroke="${INK}" stroke-width="2.4"/></g></g></g>`;
  // the windpipe's face (inside the open airway) + its arms
  s+=`<g id="traFace"><g transform="translate(246,946)">${oEye('tEyeL',42,SAL)}</g><g transform="translate(332,946)">${oEye('tEyeR',42,SAL)}</g>
   <g id="redEyes" opacity="0">${[246,332].map(x=>`<circle cx="${x}" cy="946" r="40" fill="#e3242c" ${OLW}/><path d="M${x-26},${930} q10,8 4,22 M${x+22},${926} q-12,10 -6,24 M${x-10},${970} q8,-10 18,-4" fill="none" stroke="#9e141c" stroke-width="3" stroke-linecap="round"/><circle cx="${x-4}" cy="${938}" r="11" fill="#1b1717"/><ellipse cx="${x-16}" cy="${926}" rx="10" ry="6" fill="#ff9ea2" opacity=".9"/>
     <path d="M${x-30},${972} C${x-34},${992} ${x-20},${1004} ${x-12},${990} C${x-4},${1006} ${x+12},${1002} ${x+10},${984} C${x+22},${996} ${x+34},${986} ${x+28},${970}" fill="#7fc8ef" ${OLW}/>`).join('')}</g>
   <path id="tBrowL" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/><path id="tBrowR" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/>
   ${mouthEl('tra_m',290,1008)}<g id="tTears"></g></g>
   ${hose('tArmL')}${hose('tArmR')}`;
  s+=`${chunkSVG('food1')}${chunkSVG('food2')}${chunkSVG('food3')}`;
  s+=`</g>`;return s;}
function throatLabels(){const box=(id,t,x,y,r,w,fs)=>`<g id="${id}" transform="translate(${x},${y}) rotate(${r})"><rect x="${-w/2}" y="-24" width="${w}" height="48" fill="#fff" ${OLW}/><text x="0" y="10" text-anchor="middle" style="font-family:'DejaVu Sans',sans-serif;font-weight:700;font-size:${fs}px;letter-spacing:1px" fill="#111">${t}</text></g>`;
  return box('lbEpi','EPIGLOTTIS',52,676,-90,150,18)+box('lbTra','TRACHEA',256,850,-4,166,28)+box('lbEso','ESOPHAGUS',536,824,-4,152,20);}

// ---------------- SCENE B: the man at the dinner table (medium close-up, like the reference) ----------------
function dinnerWorld(){
  return `<g id="wDinner"><rect x="-200" y="-200" width="1120" height="1680" fill="#eceeef"/>
   <g transform="translate(-30,-60)"><rect x="0" y="0" width="330" height="380" fill="#f8fafb" ${OLW}/><rect x="18" y="18" width="294" height="344" fill="#d9e9f1"/><path d="M165,18 V362 M18,190 H312" stroke="#8d989f" stroke-width="12"/><rect x="0" y="0" width="330" height="380" fill="none" ${OLW}/></g>
   <rect x="600" y="-200" width="46" height="740" fill="#7f878d" ${OLW}/>
   <path d="M150,700 L150,520 C150,500 640,500 640,520 L640,700Z" fill="#6b4a33" ${OLW}/>
   <g transform="translate(390,206) scale(1.9)">${patientSVG()}</g>
   <g id="manFx"></g>
   <path d="M-200,880 C120,866 600,866 920,880 L920,1480 L-200,1480Z" fill="#7a5235" ${OLW}/><path d="M-200,896 C120,882 600,882 920,896" fill="none" stroke="#956744" stroke-width="5"/>
   ${plateBig(200,1000)}${saladBowl(560,1060)}${plateBig(300,1210,.85)}
   </g>`;}
function plateBig(x,y,s=1){return `<g transform="translate(${x},${y}) scale(${s})"><ellipse rx="210" ry="74" fill="#f8f7f3" ${OLW}/><ellipse rx="168" ry="54" fill="none" stroke="#d8d3c9" stroke-width="4"/>
  ${[[-110,-30,0],[-50,-44,40],[10,-36,80],[70,-30,120],[-80,6,160],[-14,0,200],[54,8,240],[110,-6,280]].map(([a,b,r],i)=>`<g transform="translate(${a},${b}) rotate(${r}) scale(.62)"><path d="M-30,-40 C-6,-52 24,-44 34,-20 C44,6 36,34 14,44 C-8,54 -34,42 -40,18 C-46,-6 -46,-30 -30,-40Z" fill="${i%2?'#c63a2a':'#da4f2c'}" ${OLW}/><path d="M-12,-18 l9,-4 M10,8 l9,-4" stroke="#8f1219" stroke-width="5" stroke-linecap="round"/></g>`).join('')}
  ${[[-150,-40],[140,-34],[-20,24]].map(([a,b])=>`<path d="M${a},${b} c12,-18 32,-18 38,0 c-4,10 -30,12 -38,0z" fill="#e3262c" ${OLW}/><path d="M${a+36},${b-2} l10,-8" stroke="#3f8a3a" stroke-width="5" stroke-linecap="round"/>`).join('')}</g>`;}
function saladBowl(x,y){return `<g transform="translate(${x},${y})"><path d="M-150,-10 C-140,70 140,70 150,-10Z" fill="#f2efe7" ${OLW}/><ellipse cx="0" cy="-10" rx="150" ry="34" fill="#f8f7f3" ${OLW}/>
  ${[[-90,-22],[-40,-34],[10,-28],[60,-30],[100,-16],[-60,-4],[30,-6]].map(([a,b],i)=>`<path d="M${a},${b} c-12,-26 24,-34 30,-8 c12,-18 32,-6 22,12 c-10,14 -42,16 -52,-4z" fill="${i%2?'#5fa64a':'#86cc5a'}" ${OLW}/>`).join('')}
  <circle cx="-110" cy="-16" r="15" fill="#e3474b" ${OLW}/><circle cx="84" cy="-40" r="13" fill="#e3474b" ${OLW}/></g>`;}

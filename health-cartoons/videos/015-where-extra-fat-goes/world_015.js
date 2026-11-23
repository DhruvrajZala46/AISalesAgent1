// =============== 015: "where the extra fat goes". The reference's five scenes, our characters, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_LIV='#cf5740', C_LIV_S='#a23c2b', C_FAT='#ffc62e', C_FAT_S='#e59d12', C_INS='#cfe8ff', C_INS_S='#9cc4ea', C_TEAL='#14a3a0', C_STEEL='#b9c3cf';
const XA=1000, XB=1900, XC=2800, XD=3900, FLOOR=930;
const fatLump=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${C_FAT}" ${OLW2}/><path d="M${x-r*.5},${y-r*.35} q${r*.3},-${r*.4} ${r*.7},-${r*.15}" fill="none" stroke="#fff3b0" stroke-width="3.5" stroke-linecap="round"/>`;
// ---- scene 1: the liver works out ----
function liverScene(){
  const tube=(d)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="66" stroke-linecap="round"/><path d="${d}" fill="none" stroke="#ffb7a3" stroke-width="59" stroke-linecap="round"/><path d="${d}" fill="none" stroke="#ffd2c4" stroke-width="10" stroke-linecap="round" transform="translate(0,-14)" opacity=".8"/>`;
  return `<rect x="-20" y="-20" width="760" height="1320" fill="#f39c93"/><path d="M-20,120 C200,60 520,60 740,120 M-20,760 C200,700 520,700 740,760" fill="none" stroke="#e58379" stroke-width="26" opacity=".6"/>
   <path d="M450,600 C560,548 730,610 716,790 C706,912 570,972 448,912 C384,872 420,772 474,732 C524,692 508,634 450,600Z" fill="#ff8ea0" ${OLW}/><path d="M500,650 C560,640 640,680 650,760" fill="none" stroke="#ffc0cb" stroke-width="9" stroke-linecap="round"/>
   ${tube('M-40,1010 C120,960 220,1060 380,1010 C520,966 620,1050 780,1010')}${tube('M-40,1110 C100,1160 240,1060 400,1112 C540,1158 640,1076 780,1120')}${tube('M-40,1216 C120,1170 240,1262 400,1214 C540,1172 660,1250 780,1214')}
   <g id="liv"><g id="livB">${shaded('M30,330 C80,190 330,150 560,200 C690,230 720,330 660,420 C560,540 330,600 170,570 C50,548 0,430 30,330Z',C_LIV,C_LIV_S,22)}
    <path d="M40,300 C100,190 330,150 560,200 C640,216 690,260 690,300 C660,290 650,330 620,318 C596,308 590,280 560,276 C530,272 528,330 498,326 C470,322 474,268 440,262 C404,256 404,300 372,298 C340,296 344,250 304,252 C268,254 272,310 238,312 C206,314 208,270 176,278 C140,288 144,340 112,344 C80,348 76,310 40,300Z" fill="${C_FAT}" ${OLW}/>
    <path d="M110,262 C180,214 300,192 400,196" fill="none" stroke="#fff3b0" stroke-width="8" stroke-linecap="round"/>
    <g transform="translate(350,372)"><g transform="translate(-52,0)">${oEye('lv_eL',34,C_LIV)}</g><g transform="translate(52,0)">${oEye('lv_eR',34,C_LIV)}</g>${brow('lv_bL')}${brow('lv_bR')}${mouthEl('lv_m',0,92)}</g></g>
    <g id="drips"></g><g id="lsweat"></g>
    <path id="armLo" fill="none" stroke="${INK}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><path id="armL" fill="none" stroke="${C_LIV}" stroke-width="27" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="armRo" fill="none" stroke="${INK}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><path id="armR" fill="none" stroke="${C_LIV}" stroke-width="27" stroke-linecap="round" stroke-linejoin="round"/>
    <g id="bar"><path d="M80,0 H620" stroke="${INK}" stroke-width="16" stroke-linecap="round"/><path d="M80,0 H620" stroke="${C_STEEL}" stroke-width="9" stroke-linecap="round"/>
     ${[[112,54],[150,40],[588,54],[550,40]].map(([x,h])=>`<rect x="${x-15}" y="${-h}" width="30" height="${h*2}" rx="9" fill="#2b2f3a" ${OLW}/><path d="M${x-6},${-h+10} v${h*2-20}" stroke="#565d6e" stroke-width="5" stroke-linecap="round"/>`).join('')}
     <circle cx="230" cy="0" r="21" fill="${C_LIV}" ${OLW}/><circle cx="470" cy="0" r="21" fill="${C_LIV}" ${OLW}/></g></g>`;}
// ---- scene 2: the corridor of fat storage rooms ----
function door(x,label,id,body){const col=body?'#a53030':'#cc8349',fr=body?'#f1f1ee':'#4a2a16';
  return `<text x="${x}" y="446" text-anchor="middle" style="font-family:LG,sans-serif;font-size:${body?34:36}px;letter-spacing:1px" fill="#2a2018">${label}</text>
   <rect x="${x-128}" y="470" width="256" height="${FLOOR-470}" fill="${fr}" ${OLW}/><rect x="${x-108}" y="490" width="216" height="${FLOOR-490}" fill="${col}" ${OLW}/>
   ${body?`<path d="M${x-70},560 h140 M${x-70},592 h140 M${x-70},624 h140" stroke="#5b3d86" stroke-width="12" stroke-linecap="round"/><rect id="${id}_open" x="${x-108}" y="490" width="216" height="${FLOOR-490}" fill="#17110f" opacity="0"/>`
     :`<rect x="${x-74}" y="522" width="148" height="46" rx="5" fill="#fff" ${OLW2}/><g id="${id}_full" opacity="0"><rect x="${x-74}" y="522" width="148" height="46" rx="5" fill="#ffe9e6" ${OLW2}/><text x="${x}" y="553" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#d82f2f">STORAGE FULL</text></g>`}
   <rect x="${x+62}" y="690" width="26" height="62" rx="6" fill="#3a3a3a" ${OLW2}/><path d="M${x+52},722 h-34" stroke="${INK}" stroke-width="9" stroke-linecap="round"/>`;}
function insulinSVG(id,flip){
  return `<g id="${id}"><g id="${id}_s"><path d="M-64,0 C-88,-52 -72,-152 -8,-162 C54,-170 82,-112 76,-50 C72,-14 52,0 24,0 Z" fill="${C_INS}" ${OLW}/><path d="M-50,-30 C-62,-70 -52,-118 -26,-138" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" opacity=".7"/>
    <path d="M-60,-126 C-56,-186 54,-192 70,-130 Z" fill="#232b3d" ${OLW2}/><path d="M36,-140 L104,-128 L98,-110 L34,-118 Z" fill="#232b3d" ${OLW2}/>
    <text x="2" y="-140" text-anchor="middle" transform="${flip?'translate(4,0) scale(-1,1)':''}" style="font-family:Inter,sans-serif;font-weight:900;font-size:17px;letter-spacing:.5px" fill="#fff">INSULIN</text>
    <g transform="translate(34,-88)"><g transform="translate(-19,0)">${oEye(id+'_eL',15,C_INS)}</g><g transform="translate(19,0)">${oEye(id+'_eR',15,C_INS)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',2,42)}</g>
    <g id="${id}_arm"><path d="M44,-40 q30,-4 46,-26" fill="none" stroke="${INK}" stroke-width="24" stroke-linecap="round"/><path d="M44,-40 q30,-4 46,-26" fill="none" stroke="${C_INS}" stroke-width="17" stroke-linecap="round"/></g></g></g>`;}
function corridor(){
  return `<g id="corW"><rect x="-600" y="-20" width="6400" height="${FLOOR+10}" fill="#fbf1d9"/><rect x="-600" y="${FLOOR-26}" width="6400" height="26" fill="#a9a39a" ${OLW2}/>
   <rect x="-600" y="${FLOOR}" width="6400" height="400" fill="#f7b7ae"/><path d="M-600,${FLOOR} H5800" ${OLW}/><path d="M-600,1210 H5800" stroke="#e99b92" stroke-width="16"/>
   ${door(XA,'FAT STORAGE A','dA')}${door(XB,'FAT STORAGE B','dB')}${door(XC,'FAT STORAGE C','dC')}${door(XD,'BODY FAT STORAGE','dD',true)}
   <g id="fxk"></g>
   <g id="i2w"><g transform="scale(-1.45,1.45)">${insulinSVG('i2',true)}</g></g>
   <g id="i1w"><g transform="scale(1.45)">${insulinSVG('i1')}</g></g>
   <g id="barrow"><g id="fatPile">${[[-52,-78,26],[-8,-92,30],[40,-80,27],[-30,-116,24],[18,-124,26],[64,-104,20],[-70,-100,18]].map(([x,y,r])=>fatLump(x,y,r)).join('')}</g>
     <path d="M-96,-74 L104,-74 L74,-10 L-66,-10 Z" fill="#aab3c0" ${OLW}/><path d="M-84,-60 L92,-60" stroke="#d5dbe3" stroke-width="6" stroke-linecap="round"/>
     <path d="M-96,-70 L-170,-96" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M-96,-70 L-170,-96" stroke="#7d8697" stroke-width="6" stroke-linecap="round"/>
     <path d="M-50,-10 L-64,22" stroke="${INK}" stroke-width="9" stroke-linecap="round"/><circle id="wheel" cx="62" cy="2" r="24" fill="#2b2f3a" ${OLW}/><circle cx="62" cy="2" r="8" fill="#aab3c0"/></g></g>`;}
// ---- scene 4: the body, where the fat ends up ----
function bodyScene(){
  const blob=(id,x,y,rx,ry,rot)=>`<g id="${id}" transform="translate(${x},${y})"><g transform="rotate(${rot})"><ellipse rx="${rx}" ry="${ry}" fill="#ffd95a" ${OLW}/>${Array.from({length:7},(_,i)=>`<circle cx="${((rnd2(i+rx)-.5)*rx*1.2).toFixed(0)}" cy="${((rnd2(i*3+ry)-.5)*ry*1.3).toFixed(0)}" r="${(8+rnd2(i+7)*9).toFixed(0)}" fill="#fff0a8" stroke="${C_FAT_S}" stroke-width="2"/>`).join('')}</g></g>`;
  return `<rect x="-20" y="-20" width="760" height="1320" fill="#fbf1d9"/>
   <g id="belly"><path d="M210,-40 C180,220 120,420 150,640 C170,790 250,900 262,1040 L250,1300 L560,1300 C560,1180 640,1060 650,900 C664,700 560,560 520,380 C500,260 520,100 520,-40 Z" fill="#f6c9a2" ${OLW}/>
    <path d="M40,-40 C30,200 60,430 110,560 C140,640 200,640 210,560 C230,400 190,200 200,-40 Z" fill="#f2bd93" ${OLW}/>
    <path d="M430,640 q22,14 6,34" fill="none" ${OLW2}/><path d="M246,1040 L250,1300 L560,1300 L566,1030 C470,1070 340,1070 246,1040 Z" fill="#2c3252" ${OLW}/></g>
   ${blob('f1',120,330,44,120,8)}${blob('f2',330,300,60,90,-14)}${blob('f3',300,620,70,150,10)}${blob('f4',520,720,90,170,-6)}${blob('f5',400,930,120,70,4)}`;}
function rnd2(i){const x=Math.sin(i*91.7+13.1)*43758.5453;return x-Math.floor(x);}
// ---- scene 5: the clinic. Our patient on the scale, our doctor with her clipboard ----
function clinic15(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#e8f7f5"/>
   <rect x="640" y="-60" width="140" height="1230" fill="#f7fdfc" ${OLW}/>
   <g transform="translate(262,52)"><rect x="0" y="0" width="304" height="192" fill="#2b3b3b" ${OLW}/>${[0,1,2,3].map(i=>`<rect x="10" y="${10+i*45}" width="284" height="36" fill="#c6d4d2"/><rect x="10" y="${36+i*45}" width="284" height="8" fill="#8b9b99"/>`).join('')}</g>
   <rect x="-10" y="300" width="60" height="880" fill="${C_TEAL}" ${OLW}/>
   <rect x="-60" y="1150" width="840" height="200" fill="#cfe3e1"/><path d="M-60,1150 H780" ${OLW}/>
   <g transform="translate(360,1150) scale(1.12) translate(-392,-1150)">
    <g transform="translate(170,350)">${doctorSVG()}</g>
    <ellipse cx="520" cy="1146" rx="150" ry="14" fill="#000" opacity=".12"/>
    <path d="M636,1120 V760" stroke="${INK}" stroke-width="22" stroke-linecap="round"/><path d="M636,1120 V760" stroke="${C_STEEL}" stroke-width="15" stroke-linecap="round"/>
    <rect x="586" y="712" width="100" height="62" rx="10" fill="#2b2f3a" ${OLW}/><rect x="596" y="722" width="80" height="42" rx="5" fill="#bfe9d2"/><text id="scaleTxt" x="636" y="753" text-anchor="middle" style="font-family:LG,sans-serif;font-size:26px" fill="#1d3b2a">0</text>
    <g id="patWrap"><g transform="translate(500,332)">${patientSVG()}</g></g>
    <rect x="400" y="1098" width="270" height="40" rx="12" fill="#5d7bd0" ${OLW}/><rect x="414" y="1090" width="200" height="14" rx="6" fill="#2b2f3a" ${OLW2}/></g>`;}

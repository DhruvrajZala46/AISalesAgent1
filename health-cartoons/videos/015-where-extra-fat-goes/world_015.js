// =============== 015: "where the extra fat goes". The reference's five scenes, our characters, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_LIV='#cf5740', C_LIV_S='#a23c2b', C_FAT='#ffc62e', C_FAT_S='#e59d12', C_INS='#cfe8ff', C_INS_S='#9cc4ea', C_TEAL='#14a3a0', C_STEEL='#b9c3cf';
const XA=1100, XB=2300, XC=3500, XD=4800, FLOOR=900;
// fat looks the same everywhere (on the liver, in the wheelbarrow, on the body): yellow, lumpy, dripping
const bumps=(pts)=>pts.map(([x,y,r])=>`<path d="M${x-r},${y} q${r},${-r*1.1} ${r*2},0" fill="none" stroke="${C_FAT_S}" stroke-width="4" stroke-linecap="round"/>`).join('');
// ---- scene 1: the liver works out (liver, stomach and intestines drawn where they sit in the body) ----
const LIV_D='M-40,250 C120,140 420,140 620,186 C704,204 736,262 700,306 C640,384 520,430 400,524 C300,604 140,700 -40,712 Z';
function liverScene(){
  const gut=(d)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="92" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="#f7a79b" stroke-width="85" stroke-linecap="round" stroke-linejoin="round"/>`;
  const folds=(pts)=>pts.map(([x,y,r])=>`<path d="M${x},${y-34} q${r},34 0,68" fill="none" stroke="#e58379" stroke-width="5" stroke-linecap="round"/>`).join('');
  DEFS+=`<clipPath id="livC"><path d="${LIV_D}"/></clipPath>`;
  return `<g id="s1cam"><rect x="-400" y="-400" width="1520" height="2100" fill="#b3736c"/>
   <path d="M610,-60 C600,80 640,200 600,330" fill="none" stroke="${INK}" stroke-width="62" stroke-linecap="round"/><path d="M610,-60 C600,80 640,200 600,330" fill="none" stroke="#f08f8f" stroke-width="55" stroke-linecap="round"/>
   <path d="M560,300 C660,300 740,420 736,580 C730,780 600,910 430,910 C290,910 220,830 244,740 C258,690 322,684 352,730 C384,786 474,796 546,734 C608,680 606,560 540,468 Z" fill="#ff9d9d" ${OLW}/>
   <path d="M566,360 C640,380 690,470 686,580 C680,740 580,850 436,856 C340,860 296,810 300,770 C360,850 500,860 590,770 C656,700 660,560 600,460 Z" fill="#f47f88" ${OLW2}/>
   <path d="M610,470 q26,60 14,130 M560,790 q-50,34 -110,30" fill="none" stroke="#ffc4c4" stroke-width="8" stroke-linecap="round"/>
   ${gut('M-60,1010 C60,960 150,1040 250,1000 C360,956 440,1040 560,1000 C640,974 700,1000 790,990')}${gut('M790,1110 C680,1150 600,1070 480,1112 C380,1148 300,1070 190,1108 C100,1140 40,1090 -60,1116')}${gut('M-60,1224 C60,1180 150,1262 260,1222 C370,1180 450,1262 570,1222 C650,1196 710,1226 790,1214')}
   ${folds([[90,1002,14],[250,1000,-14],[410,1004,14],[560,1000,-14],[690,996,14],[120,1112,-14],[300,1090,14],[480,1112,-14],[640,1110,14],[90,1216,14],[260,1222,-14],[420,1228,14],[570,1222,-14]])}
   <g id="liv"><g id="livB">${shaded(LIV_D,'#dc6048','#a53d2c',26)}
    <g clip-path="url(#livC)"><path d="M470,150 C440,280 470,380 420,520" fill="none" stroke="#a53d2c" stroke-width="7" stroke-linecap="round" opacity=".8"/><path d="M-10,640 C80,640 200,580 300,500" fill="none" stroke="#f08a70" stroke-width="12" stroke-linecap="round" opacity=".7"/></g>
    <path d="M-40,262 C120,150 420,150 620,190 C690,203 722,240 716,276 C700,270 696,300 676,296 C660,292 664,262 640,258 C612,254 618,330 590,330 C564,330 572,270 546,262 C520,256 520,300 496,300 C470,300 478,250 450,246 C420,242 424,340 394,342 C366,344 372,268 344,262 C316,256 318,304 290,306 C262,308 268,262 240,262 C210,262 214,360 184,362 C156,364 162,290 134,290 C106,290 110,330 82,334 C54,338 56,300 28,300 C0,300 -4,340 -40,330 Z" fill="${C_FAT}" ${OLW}/>
    ${bumps([[60,236,16],[150,208,18],[250,190,16],[350,184,18],[450,186,16],[550,200,16],[640,226,12],[200,236,12],[400,222,12],[590,290,9],[184,318,9],[394,300,9]])}
    <g transform="translate(205,440)"><g transform="translate(-58,0)">${oEye('lv_eL',44,'#dc6048')}</g><g transform="translate(58,0)">${oEye('lv_eR',44,'#dc6048')}</g>${brow('lv_bL')}${brow('lv_bR')}${mouthEl('lv_m',0,104)}</g>
    <path id="vein" d="M330,356 l22,-14 M336,372 l26,2 M322,344 l8,-24" stroke="#8f2e20" stroke-width="6" stroke-linecap="round"/></g>
    <g id="drips"></g><g id="lsweat"></g>
    <path id="armLo" fill="none" stroke="${INK}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/><path id="armL" fill="none" stroke="#dc6048" stroke-width="23" stroke-linecap="round" stroke-linejoin="round"/>
    <path id="armRo" fill="none" stroke="${INK}" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/><path id="armR" fill="none" stroke="#dc6048" stroke-width="23" stroke-linecap="round" stroke-linejoin="round"/>
    <g id="bar"><path d="M-10,0 H420" stroke="${INK}" stroke-width="20" stroke-linecap="round"/><path d="M-10,0 H420" stroke="${C_STEEL}" stroke-width="12" stroke-linecap="round"/>
     ${[[10,66],[52,50],[400,66],[358,50]].map(([x,h])=>`<rect x="${x-19}" y="${-h}" width="38" height="${h*2}" rx="11" fill="#2b2f3a" ${OLW}/><path d="M${x-7},${-h+12} v${h*2-24}" stroke="#5b6274" stroke-width="6" stroke-linecap="round"/>`).join('')}
     <circle cx="120" cy="0" r="25" fill="#fff" ${OLW}/><circle cx="290" cy="0" r="25" fill="#fff" ${OLW}/></g></g></g>`;}
// ---- scene 2: the corridor of fat storage rooms, inside the liver ----
function door(x,label,id,body){const col=body?'#a53030':'#cc8349',fr=body?'#f1f1ee':'#4a2a16';
  return `<text x="${x}" y="226" text-anchor="middle" style="font-family:LG,sans-serif;font-size:${body?46:54}px;letter-spacing:1.5px" fill="#1d1712">${label}</text>
   <rect x="${x-196}" y="254" width="392" height="${FLOOR-254}" fill="${fr}" ${OLW}/><rect x="${x-176}" y="274" width="352" height="${FLOOR-274}" fill="${col}" ${OLW}/>
   ${body?`<path d="M${x-110},350 h220 M${x-110},392 h220 M${x-110},434 h220" stroke="#5b3d86" stroke-width="16" stroke-linecap="round"/><rect id="${id}_open" x="${x-176}" y="274" width="352" height="${FLOOR-274}" fill="#17110f" opacity="0"/>`
     :`<rect x="${x-132}" y="326" width="264" height="70" rx="6" fill="#fff" ${OLW}/><g id="${id}_full" opacity="0"><rect x="${x-132}" y="326" width="264" height="70" rx="6" fill="#fff" ${OLW}/><text x="${x}" y="375" text-anchor="middle" style="font-family:LG,sans-serif;font-size:34px;letter-spacing:.5px" fill="#e02626">STORAGE FULL</text></g>`}
   <rect x="${x+104}" y="560" width="40" height="92" rx="7" fill="#3a3a3a" ${OLW}/><rect x="${x+112}" y="570" width="24" height="26" rx="3" fill="#cfd5dc"/><path d="M${x+96},622 h-50" stroke="${INK}" stroke-width="13" stroke-linecap="round"/>`;}
function insulinSVG(id){
  return `<g id="${id}"><g id="${id}_s"><path d="M-72,0 C-116,-44 -104,-156 -72,-236 C-50,-296 44,-304 72,-244 C102,-172 112,-62 82,-12 C62,12 -40,16 -72,0 Z" fill="${C_INS}" ${OLW}/><path d="M-80,-60 C-84,-110 -72,-170 -52,-214" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round" opacity=".75"/>
    <g transform="rotate(-10,-6,-262)"><path d="M-92,-224 C-92,-312 60,-322 82,-240 C40,-256 -40,-250 -92,-224 Z" fill="#1e2536" ${OLW}/><circle cx="-96" cy="-226" r="12" fill="#1e2536" ${OLW2}/>
     <text x="-6" y="-258" text-anchor="middle" style="font-family:LG,sans-serif;font-size:27px;letter-spacing:1px" fill="#fff">INSULIN</text></g>
    <g transform="translate(40,-176)"><g transform="translate(-26,0)">${oEye(id+'_eL',28,C_INS)}</g><g transform="translate(26,0)">${oEye(id+'_eR',28,C_INS)}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',10,58)}</g>
    <g id="${id}_arm"><path d="M74,-104 q34,-2 52,-34" fill="none" stroke="${INK}" stroke-width="28" stroke-linecap="round"/><path d="M74,-104 q34,-2 52,-34" fill="none" stroke="${C_INS}" stroke-width="21" stroke-linecap="round"/><circle cx="128" cy="-142" r="17" fill="${C_INS}" ${OLW2}/></g></g></g>`;}
function corridor(){
  return `<g id="corW"><rect x="-800" y="-20" width="7200" height="${FLOOR+10}" fill="#fbf1d9"/><rect x="-800" y="${FLOOR-24}" width="7200" height="24" fill="#a9a39a" ${OLW2}/>
   <rect x="-800" y="${FLOOR}" width="7200" height="420" fill="#f9b9b0"/><path d="M-800,${FLOOR} H6400" ${OLW}/><rect x="-800" y="1200" width="7200" height="100" fill="#e8948b"/>
   ${door(XA,'FAT STORAGE A','dA')}${door(XB,'FAT STORAGE B','dB')}${door(XC,'FAT STORAGE C','dC')}${door(XD,'BODY FAT STORAGE','dD',true)}
   <g id="fxk"></g>
   <g id="i2w"><g transform="scale(1.12)">${insulinSVG('i2')}</g></g>
   <g id="i1w"><g transform="scale(1.18)">${insulinSVG('i1')}</g></g>
   <g id="barrow"><path d="M-108,-70 L-196,-112" stroke="${INK}" stroke-width="15" stroke-linecap="round"/><path d="M-108,-70 L-196,-112" stroke="#7d8697" stroke-width="8" stroke-linecap="round"/>
     <g id="fatPile"><path d="M-108,-66 C-140,-110 -96,-156 -58,-142 C-52,-190 14,-200 34,-162 C66,-188 122,-154 106,-112 C132,-98 126,-66 106,-66 Z" fill="${C_FAT}" ${OLW}/>${bumps([[-70,-104,15],[-20,-150,16],[40,-126,16],[78,-96,13],[-34,-100,12],[10,-98,12]])}</g>
     <path d="M-112,-72 L112,-72 L82,-6 L-74,-6 Z" fill="#aab3c0" ${OLW}/><path d="M-98,-56 L98,-56" stroke="#d5dbe3" stroke-width="7" stroke-linecap="round"/>
     <g id="fatDrip"><path d="M-84,-74 C-84,-50 -74,-36 -66,-50 C-62,-60 -60,-70 -58,-74 Z M-10,-74 C-12,-40 0,-24 8,-44 C12,-56 12,-66 14,-74 Z M56,-74 C54,-52 64,-40 70,-54 C74,-62 74,-70 76,-74 Z" fill="${C_FAT}" ${OLW2}/></g>
     <path d="M-56,-6 L-72,30" stroke="${INK}" stroke-width="11" stroke-linecap="round"/><circle cx="70" cy="8" r="28" fill="#23262f" ${OLW}/><circle cx="70" cy="8" r="9" fill="#aab3c0"/></g></g>`;}
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
    <g id="patWrap"><g transform="translate(500,332)">${patientSVG()}<g id="pBelly">${shaded('M-112,300 C-150,360 -150,470 -104,520 C-50,560 60,560 110,518 C152,470 150,360 112,300 C60,280 -60,280 -112,300 Z','#c7884a','#a86c34',18)}<path d="M-64,428 C-24,444 24,444 64,428 L60,482 C22,494 -22,494 -60,482 Z" fill="#b47a40" ${OLW2}/><path d="M-10,300 v40 M10,300 v40" stroke="#f3eadf" stroke-width="3.5" stroke-linecap="round"/></g></g></g>
    <rect x="400" y="1098" width="270" height="40" rx="12" fill="#5d7bd0" ${OLW}/><rect x="414" y="1090" width="200" height="14" rx="6" fill="#2b2f3a" ${OLW2}/></g>`;}

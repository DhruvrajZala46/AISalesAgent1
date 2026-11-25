// =============== 023: how sleeping pills work. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_ST='#f7a29c', C_ST_L='#fbc9c3', C_ST_D='#e27c78', C_LIV='#d9533f', C_ACID='#efa874';
const lim=(d,wd,col)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
const ST_D='M226,-80 C228,120 236,260 230,330 C222,410 160,460 60,480 L-80,494 L-80,880 C120,940 360,950 520,900 C640,860 690,770 700,640 C708,520 690,400 640,320 C590,250 500,232 420,250 C370,262 344,220 340,160 L336,-80 Z';
const PILL=(id,s=1)=>`<g id="${id}" transform="scale(${s})"><ellipse rx="26" ry="20" fill="#fff" ${OLW2}/><path d="M-20,0 h40" stroke="${INK}" stroke-width="3"/><path d="M-14,-10 q8,-6 18,-4" fill="none" stroke="#dfe6ee" stroke-width="5" stroke-linecap="round"/></g>`;
function bodyCard(x,y,ringY,txt,organ){return `<g id="inset_${txt[11]}"><rect x="${x}" y="${y}" width="190" height="270" rx="18" fill="#fff" ${OLW}/>
   <circle cx="${x+95}" cy="${y+62}" r="38" fill="${PSK}" ${OLW2}/><path d="M${x+60},${y+52} C${x+60},${y+14} ${x+130},${y+14} ${x+130},${y+52} C${x+116},${y+38} ${x+76},${y+38} ${x+60},${y+52} Z" fill="#1f1d24" ${OLW2}/><circle cx="${x+82}" cy="${y+64}" r="4.5" fill="${INK}"/><circle cx="${x+108}" cy="${y+64}" r="4.5" fill="${INK}"/>
   <path d="M${x+48},${y+130} C${x+48},${y+108} ${x+142},${y+108} ${x+142},${y+130} L${x+146},${y+222} L${x+44},${y+222} Z" fill="#c7884a" ${OLW2}/>
   ${organ==='st'?`<path d="M${x+84},${y+140} L${x+86},${y+156} C${x+70},${y+164} ${x+66},${y+190} ${x+84},${y+198} C${x+104},${y+206} ${x+126},${y+192} ${x+124},${y+168} C${x+122},${y+150} ${x+104},${y+148} ${x+96},${y+156} L${x+94},${y+140} Z" fill="${C_ST}" ${OLW2}/>`:`<circle cx="${x+95}" cy="${y+62}" r="38" fill="${PSK}" ${OLW2}/><path d="M${x+64},${y+54} C${x+62},${y+26} ${x+126},${y+22} ${x+128},${y+54} C${x+130},${y+70} ${x+66},${y+72} ${x+64},${y+54} Z" fill="#c46a5f" ${OLW2}/><path d="M${x+76},${y+44} q8,-8 16,0 M${x+98},${y+38} q8,8 18,2 M${x+84},${y+58} q10,-6 22,2" fill="none" stroke="#7a3a33" stroke-width="2.6" stroke-linecap="round"/><circle cx="${x+84}" cy="${y+80}" r="4" fill="${INK}"/><circle cx="${x+106}" cy="${y+80}" r="4" fill="${INK}"/>`}
   <circle class="ring" cx="${x+95}" cy="${ringY}" r="22" fill="none" stroke="#e02626" stroke-width="6"/>
   <text x="${x+95}" y="${y+252}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#1d2a44">${txt}</text></g>`;}
// ---- scene 1: the stomach, cut open, with the food pipe coming down ----
function stomachScene(){
  DEFS+=`<clipPath id="stC"><path d="${ST_D}"/></clipPath>`;
  const coil=(x,y,wd,h)=>`<rect x="${x}" y="${y}" width="${wd}" height="${h}" rx="${h/2}" fill="#f6a8a4" ${OLW}/><path d="M${x+h*.4},${y+h*.3} h${wd-h*.8}" stroke="#fbd0cc" stroke-width="8" stroke-linecap="round"/>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#f6d6d1"/>
   <path d="M336,-40 H760 V110 C640,130 500,160 420,200 C380,150 350,60 336,-40 Z" fill="#c79a92"/><path d="M420,200 C500,160 640,130 760,110" fill="none" ${OLW2}/>
   <path d="M-60,90 C100,70 250,110 330,190 L330,390 C200,372 60,382 -60,404 Z" fill="#e2533a" ${OLW}/><path d="M-60,404 C60,378 200,372 330,388 L330,620 C200,640 60,650 -60,660 Z" fill="#b9463f" ${OLW}/>
   <path d="M90,140 C112,260 96,420 116,548" fill="none" stroke="${INK}" stroke-width="26" stroke-linecap="round"/><path d="M90,140 C112,260 96,420 116,548" fill="none" stroke="#e8b23a" stroke-width="18" stroke-linecap="round"/><path d="M116,548 q-12,20 0,30 q12,-10 0,-30 Z" fill="#e8b23a" ${OLW2}/>
   <path d="M-60,900 C120,950 380,950 560,900 C660,870 720,840 780,820 L780,1080 L-60,1080 Z" fill="#ea8e8c" ${OLW}/>
   ${Array.from({length:11},(_,i)=>`<path d="M${-40+i*76},${940+Math.sin(i)*14} q38,-34 76,0" fill="none" stroke="${INK}" stroke-width="3"/>`).join('')}
   ${(()=>{const d='M-80,1090 H600 C680,1090 680,1180 600,1180 H120 C40,1180 40,1270 120,1270 H800';return `<path d="${d}" fill="none" stroke="${INK}" stroke-width="96" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="#f6a8a4" stroke-width="88" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="#fbd0cc" stroke-width="12" stroke-dasharray="60 40" transform="translate(0,-22)"/>`;})()}
   <path d="${ST_D}" fill="none" stroke="${INK}" stroke-width="84"/><path d="${ST_D}" fill="none" stroke="#f1c3b8" stroke-width="76"/><path d="${ST_D}" fill="none" stroke="${INK}" stroke-width="54"/><path d="${ST_D}" fill="none" stroke="#d24d50" stroke-width="46"/>
   <path d="${ST_D}" fill="${C_ST}" ${OLW}/>
   <g clip-path="url(#stC)"><path d="${ST_D}" fill="none" stroke="#fbd5cf" stroke-width="22" stroke-dasharray="2 22" stroke-linecap="round"/><path d="${ST_D}" fill="none" stroke="#f4b9b2" stroke-width="10"/>
    <path d="M272,-60 L276,560" stroke="${C_ST_L}" stroke-width="16" stroke-linecap="round" opacity=".8"/>
    ${[[380,380],[460,370],[700,380],[430,600],[650,610],[560,640]].map(([x,y])=>`<path d="M${x},${y} q-18,50 4,100 q18,50 -6,100" fill="none" stroke="${C_ST_D}" stroke-width="5" stroke-linecap="round" opacity=".55"/>`).join('')}
    <g id="acid"></g><g id="pills">${PILL('p1')}${PILL('p2')}</g><g id="fizz"></g></g>
   <path d="${ST_D}" fill="none" ${OLW}/>
   <g id="sface" transform="translate(540,390)"><g transform="translate(-68,0)">${oEye('st_eL',60,C_ST)}</g><g transform="translate(68,0)">${oEye('st_eR',60,C_ST)}</g>${brow('st_bL')}${brow('st_bR')}<g transform="translate(0,96) scale(2.4)">${mouthEl('st_m',0,0)}</g></g>
   <g id="bub" opacity="0"><path d="M300,460 L330,350 L246,372 Z" fill="#fff" ${OLW}/><circle cx="190" cy="220" r="170" fill="#fff" ${OLW}/><path d="M246,384 L316,362" stroke="#fff" stroke-width="14"/>
    <g id="brainW" transform="translate(190,224)"><path d="M-130,24 C-142,-46 -92,-104 -20,-106 C44,-124 116,-98 132,-36 C150,14 128,64 80,72 C60,96 8,94 -12,82 C-62,96 -112,80 -130,24 Z" fill="#c46a5f" ${OLW}/>
     <path d="M-104,-20 q14,-26 40,-14 q10,-30 40,-20 M-30,-80 q20,10 14,36 q20,6 22,30 M30,-92 q-4,30 22,36 M70,-70 q-10,26 16,40 q24,0 26,26 M-112,30 q24,-20 50,0 q20,-20 46,0 M-40,10 q10,24 40,18 M20,-10 q30,-6 40,20 M-60,60 q20,-14 40,4 M30,50 q20,-18 46,-6" fill="none" stroke="#7a3a33" stroke-width="5.5" stroke-linecap="round"/>
     <g transform="translate(40,4)"><g transform="translate(-30,0)">${oEye('br_eL',26,'#c46a5f')}</g><g transform="translate(30,0)">${oEye('br_eR',26,'#c46a5f')}</g>${brow('br_bL')}${brow('br_bR')}<g transform="translate(0,44) scale(1.3)">${mouthEl('br_m',0,0)}</g></g></g></g>
   <g id="upArrow" opacity="0"><path d="M480,760 C640,700 712,560 706,300 L700,40" fill="none" stroke="#fff" stroke-width="16" stroke-dasharray="26 18" stroke-linecap="round"/><path d="M672,70 L702,8 L730,74 Z" fill="#fff" ${OLW2}/></g>
   ${bodyCard(16,990,'1154','INSIDE THE STOMACH','st')}<g transform="translate(560,120)"><rect x="-130" y="-34" width="260" height="68" rx="14" fill="#fff" ${OLW}/><text x="0" y="14" text-anchor="middle" style="font-family:LG,sans-serif;font-size:40px;letter-spacing:2px" fill="#1d2a44">STOMACH</text></g>`;}
// ---- scene 2: the worry centre of the brain ----
function blob(id,col,label,w){return `<g id="${id}"><g class="fl"></g><ellipse rx="${w}" ry="${w*.9}" fill="${col}" ${OLW}/><path d="M${-w*.55},${-w*.45} q${w*.3},-${w*.3} ${w*.6},-${w*.2}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".5"/>
   <rect x="${-w*.95}" y="${w*.12}" width="${w*1.9}" height="36" rx="6" fill="#fff" ${OLW2}/><text x="0" y="${w*.12+27}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:${label.length>8?21:24}px" fill="#1d2a44">${label}</text>
   <g class="mark" transform="translate(${w*.55},${-w*.62})"><path d="M-14,-4 q10,-2 10,-12 M4,-16 q2,10 12,10 M14,4 q-10,2 -10,12 M-4,16 q-2,-10 -12,-10" fill="none" stroke="#e02626" stroke-width="6" stroke-linecap="round"/></g><g transform="translate(0,${-w*.3})"><g transform="translate(-${w*.34},0)">${oEye(id+'_eL',w*.24,col)}</g><g transform="translate(${w*.34},0)">${oEye(id+'_eR',w*.24,col)}</g>${brow(id+'_bL')}${brow(id+'_bR')}</g><g transform="translate(0,${-w*.02}) scale(1.2)">${mouthEl(id+'_m',0,0)}</g></g>`;}
function copSVG(){return `<g id="cop"><path d="M-46,330 L-50,460 M46,330 L50,460" stroke="${INK}" stroke-width="44" stroke-linecap="round"/><path d="M-46,330 L-50,460 M46,330 L50,460" stroke="#2c3346" stroke-width="36" stroke-linecap="round"/>
   <path d="M-84,470 q30,-26 64,0 v12 h-64 Z M20,470 q30,-26 64,0 v12 h-64 Z" fill="#17171a" ${OLW2}/>
   <path d="M-80,170 C-80,140 80,140 80,170 L88,340 L-88,340 Z" fill="#9ec3e6" ${OLW}/><path d="M-88,318 H88 V340 H-88 Z" fill="#2c3346" ${OLW2}/><path d="M0,160 L-12,220 L0,290 L12,220 Z" fill="#2c3346" ${OLW2}/>
   <g transform="translate(-46,212)"><path d="M-22,-24 L22,-24 L22,8 L0,26 L-22,8 Z" fill="#f0c94a" ${OLW2}/><text x="0" y="2" text-anchor="middle" style="font-family:LG,sans-serif;font-size:16px" fill="#1d2a44">GABA</text></g>
   <g id="copArmL">${lim('M-78,180 C-104,240 -100,290 -84,320',30,'#9ec3e6')}</g><g id="copArmR">${lim('M78,180 C104,240 100,290 84,320',30,'#9ec3e6')}</g>
   <g id="copHead"><circle cx="0" cy="96" r="62" fill="${DSK}" ${OLW}/><path d="M-66,96 C-78,88 -80,112 -62,118 M66,96 C78,88 80,112 62,118" fill="${DSK}" ${OLW2}/>
    <path d="M-74,50 C-70,10 70,10 74,50 L84,64 L-84,64 Z" fill="#2c3346" ${OLW}/><path d="M-90,60 H90 Q90,78 70,78 H-70 Q-90,78 -90,60 Z" fill="#1b1f2c" ${OLW2}/><circle cx="0" cy="36" r="10" fill="#f0c94a" ${OLW2}/>
    <g transform="translate(-22,96)">${oEye('cp_eL',14,DSK)}</g><g transform="translate(22,96)">${oEye('cp_eR',14,DSK)}</g><g transform="translate(0,4)">${brow('cp_bL')}${brow('cp_bR')}</g>
    <path d="M-40,124 C-24,112 -8,118 0,124 C8,118 24,112 40,124 C30,138 10,134 0,128 C-10,134 -30,138 -40,124 Z" fill="#4a2a1c" ${OLW2}/><g transform="translate(0,146)">${mouthEl('cp_m',0,0)}</g>
    <g id="bruise" opacity="0"><ellipse cx="22" cy="96" rx="22" ry="20" fill="#5b3a7a" opacity=".75"/><path d="M-50,70 l24,24 M-44,88 l18,-14" stroke="#f3f0e6" stroke-width="10" stroke-linecap="round"/><path d="M-50,70 l24,24 M-44,88 l18,-14" stroke="${INK}" stroke-width="2"/></g></g></g>`;}
function sleepPill(){return `<g id="sp"><ellipse cx="0" cy="8" rx="82" ry="14" fill="#000" opacity=".15"/><ellipse rx="80" ry="58" fill="#fff" ${OLW}/><path d="M-80,0 C-60,8 60,8 80,0" fill="none" stroke="#c9d2dc" stroke-width="5"/><path d="M-52,-34 q20,-14 44,-12" fill="none" stroke="#e6ecf2" stroke-width="8" stroke-linecap="round"/>
   <g transform="translate(0,-22)"><g transform="translate(-22,0)">${oEye('sp_eL',18,'#fff')}</g><g transform="translate(22,0)">${oEye('sp_eR',18,'#fff')}</g>${brow('sp_bL')}${brow('sp_bR')}</g><g transform="translate(0,24) scale(1.2)">${mouthEl('sp_m',0,0)}</g></g>`;}
function amygScene(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#c4847a"/><ellipse cx="360" cy="420" rx="520" ry="420" fill="#d9a095" opacity=".7"/>
   <path d="M-40,760 C60,730 140,780 240,750 C340,720 420,770 520,740 C620,710 700,750 760,730 L760,1330 L-40,1330 Z" fill="#e2724e" ${OLW}/>
   ${[[60,880],[300,940],[520,860],[160,1060],[440,1090],[620,1010],[80,1200],[380,1220]].map(([x,y])=>`<path d="M${x},${y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#a84a30" stroke-width="5" stroke-linecap="round"/>`).join('')}
   <g transform="translate(360,92)"><rect x="-300" y="-36" width="600" height="72" rx="14" fill="#fff" ${OLW}/><text x="0" y="12" text-anchor="middle" style="font-family:LG,sans-serif;font-size:30px" fill="#1d2a44">AMYGDALA: THE WORRY CENTRE</text></g>
   ${bodyCard(16,150,'200','INSIDE THE BRAIN','br')}
   <g id="firePool"></g><g id="bG" transform="translate(470,860)">${blob('bg','#9bc25a','CORTISOL',96)}</g><g id="bB" transform="translate(615,920)">${blob('bb','#2f7fd0','GLUTAMATE',92)}</g><g id="bY" transform="translate(530,1050)">${blob('by','#f6d78a','ADRENALINE',104)}</g>
   <g id="copW">${copSVG()}</g>
   <g id="spW">${sleepPill()}</g>
   <g id="smoke" opacity="0"></g>`;}
// ---- scene 3: the bedroom ----
function wifeSVG(){return `<g id="wife">
   ${lim('M-20,-8 C30,-16 70,-12 96,0 C104,50 100,100 98,146',50,'#24242a')}${lim('M-34,-2 C20,-14 60,-10 76,2 C84,50 82,100 80,150',50,'#2c2c33')}
   <path d="M64,150 C100,140 132,152 134,168 L62,170 Z" fill="#f4a4be" ${OLW2}/><path d="M82,146 C118,136 150,148 152,164 L80,166 Z" fill="#f4a4be" ${OLW2}/>
   <path d="M-70,-196 C-40,-214 20,-214 44,-196 C60,-150 56,-60 44,0 L-66,0 C-80,-60 -84,-150 -70,-196 Z" fill="#f6adc4" ${OLW}/>
   <path d="M-22,-250 L-20,-200 L12,-200 L12,-250 Z" fill="${DSK}" ${OLW2}/>
   <path d="M-76,-286 C-96,-380 60,-390 58,-290 C76,-250 70,-200 40,-190 C52,-230 30,-250 -40,-250 C-70,-240 -84,-210 -76,-180 C-104,-210 -100,-260 -76,-286 Z" fill="#4a1f2a" ${OLW}/>
   <g id="wifeHead"><path d="M-54,-296 C-56,-340 36,-346 40,-296 C42,-262 28,-238 6,-226 C-6,-222 -22,-222 -32,-228 C-48,-240 -54,-266 -54,-296 Z" fill="${DSK}" ${OLW}/>
    <path d="M-60,-290 C-70,-360 30,-374 48,-306 C20,-330 -20,-334 -44,-318 C-52,-310 -58,-300 -60,-290 Z" fill="#4a1f2a" ${OLW2}/>
    ${humanEye('wEyeL',-22,-286,12,8)}${humanEye('wEyeR',18,-286,12,8)}
    <path d="M-36,-306 Q-22,-314 -10,-304 M6,-304 Q20,-314 32,-306" fill="none" stroke="#3a1820" stroke-width="4" stroke-linecap="round"/>
    <path d="M0,-280 C6,-268 6,-262 0,-258" fill="none" ${TH('#b98468')}/><ellipse id="wifeMouth" cx="-2" cy="-242" rx="9" ry="6" fill="#8c2f3a" ${OLW2}/><ellipse cx="-34" cy="-262" rx="9" ry="5" fill="#ef8f86" opacity=".6"/><ellipse cx="26" cy="-262" rx="9" ry="5" fill="#ef8f86" opacity=".6"/></g>
   ${lim('M-50,-170 C-60,-110 -40,-60 20,-40',34,'#f6adc4')}<circle cx="26" cy="-40" r="16" fill="${DSK}" ${OLW2}/></g>`;}
function bedroomScene(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#cfe0c4"/><path d="M-40,1040 H760 V1330 H-40 Z" fill="#9b7b5c"/><path d="M-40,1040 H760" ${OLW}/>
   <g transform="translate(420,110)"><rect x="0" y="0" width="300" height="420" fill="#fff" ${OLW}/><rect x="18" y="18" width="264" height="384" fill="#cfe8f6" ${OLW2}/><path d="M150,18 V402 M18,210 H282" stroke="${INK}" stroke-width="10"/><path d="M150,18 V402 M18,210 H282" stroke="#fff" stroke-width="6"/></g>
   <path d="M-40,560 H40 V1060 H-40 Z" fill="#8a6a4c" ${OLW}/>
   <path d="M-40,840 H400 Q420,840 420,860 V1000 H-40 Z" fill="#fff" ${OLW}/><path d="M-20,770 C30,740 130,744 150,780 C160,810 120,840 60,840 C0,842 -30,820 -20,770 Z" fill="#fff" ${OLW}/>
   <path d="M-40,880 H300 C330,880 330,1000 300,1000 H-40 Z" fill="#9fc3e6" ${OLW}/><path d="M20,900 q60,30 120,0 M160,920 q50,24 110,0" fill="none" stroke="#7fa6cc" stroke-width="5" stroke-linecap="round"/>
   <path d="M-40,1000 H420 V1040 H-40 Z" fill="#8a6a4c" ${OLW}/><path d="M396,1040 V1100" stroke="${INK}" stroke-width="22"/>
   <g id="wifeW"></g><g id="husW"></g>`;}

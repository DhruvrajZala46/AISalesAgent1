// =============== 023: how sleeping pills work. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_ST='#f7a29c', C_ST_L='#fbc9c3', C_ST_D='#e27c78', C_LIV='#d9533f', C_ACID='#efa874';
const lim=(d,wd,col)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
const ST_D='M262,-60 L262,230 C262,300 220,340 150,360 C80,380 0,400 -60,420 L-60,860 C80,900 300,905 480,862 C640,822 760,720 790,560 L790,300 C740,240 640,200 540,200 C460,200 400,222 380,200 L380,-60 Z';
const PILL=(id,s=1)=>`<g id="${id}" transform="scale(${s})"><ellipse rx="26" ry="20" fill="#fff" ${OLW2}/><path d="M-20,0 h40" stroke="${INK}" stroke-width="3"/><path d="M-14,-10 q8,-6 18,-4" fill="none" stroke="#dfe6ee" stroke-width="5" stroke-linecap="round"/></g>`;
function bodyCard(y,ringY,txt){return `<g id="inset_${txt[0]}"><rect x="16" y="${y}" width="190" height="270" rx="18" fill="#fff" ${OLW}/>
   <circle cx="111" cy="${y+62}" r="38" fill="${PSK}" ${OLW2}/><path d="M76,${y+52} C76,${y+14} 146,${y+14} 146,${y+52} C132,${y+38} 92,${y+38} 76,${y+52} Z" fill="#1f1d24" ${OLW2}/><circle cx="98" cy="${y+64}" r="4.5" fill="${INK}"/><circle cx="124" cy="${y+64}" r="4.5" fill="${INK}"/>
   <path d="M64,${y+130} C64,${y+108} 158,${y+108} 158,${y+130} L162,${y+222} L60,${y+222} Z" fill="#c7884a" ${OLW2}/><circle class="ring" cx="111" cy="${ringY}" r="22" fill="#e02626" fill-opacity=".15" stroke="#e02626" stroke-width="6"/>
   <text x="111" y="${y+252}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#1d2a44">${txt}</text></g>`;}
// ---- scene 1: the stomach, cut open, with the food pipe coming down ----
function stomachScene(){
  DEFS+=`<clipPath id="stC"><path d="${ST_D}"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#f6d6d1"/>
   <path d="M-40,40 C120,0 250,60 250,200 L250,520 C170,560 60,560 -40,540 Z" fill="${C_LIV}" ${OLW}/><path d="M-40,300 C60,280 160,300 240,340" fill="none" stroke="#b8402f" stroke-width="10" stroke-linecap="round"/>
   <path d="M196,170 C200,300 196,420 210,520" fill="none" stroke="${INK}" stroke-width="20" stroke-linecap="round"/><path d="M196,170 C200,300 196,420 210,520" fill="none" stroke="#e8b23a" stroke-width="13" stroke-linecap="round"/>
   ${[0,1,2,3,4].map(i=>{const y=980+i*76;return `<path d="M-40,${y} ${Array.from({length:9},(_,k)=>`q45,${k%2?-40:40} 90,0`).join(' ')}" fill="none" stroke="${INK}" stroke-width="42" stroke-linecap="round"/><path d="M-40,${y} ${Array.from({length:9},(_,k)=>`q45,${k%2?-40:40} 90,0`).join(' ')}" fill="none" stroke="#f3a3a0" stroke-width="35" stroke-linecap="round"/>`;}).join('')}
   <path d="${ST_D}" fill="none" stroke="${INK}" stroke-width="66"/><path d="${ST_D}" fill="none" stroke="#d6585c" stroke-width="58"/><path d="${ST_D}" fill="none" stroke="#e98a86" stroke-width="22"/><path d="${ST_D}" fill="${C_ST}" ${OLW}/>
   <g clip-path="url(#stC)"><path d="${ST_D}" fill="none" stroke="${C_ST_D}" stroke-width="44" opacity=".55"/><path d="${ST_D}" fill="none" stroke="#fde3df" stroke-width="10" opacity=".8"/>
    <path d="M292,-60 L300,300" stroke="${C_ST_L}" stroke-width="20" stroke-linecap="round" opacity=".7"/>
    ${[[380,560],[470,520],[560,540],[650,580],[300,620]].map(([x,y])=>`<path d="M${x},${y} q-20,60 4,120 q20,60 -6,120" fill="none" stroke="${C_ST_D}" stroke-width="6" stroke-linecap="round" opacity=".6"/>`).join('')}
    <g id="acid"></g><g id="pills">${PILL('p1')}${PILL('p2')}</g><g id="fizz"></g></g>
   <path d="${ST_D}" fill="none" ${OLW}/>
   <g id="sface" transform="translate(560,420)"><g transform="translate(-48,0)">${oEye('st_eL',42,C_ST)}</g><g transform="translate(48,0)">${oEye('st_eR',42,C_ST)}</g>${brow('st_bL')}${brow('st_bR')}<g transform="translate(0,80) scale(2)">${mouthEl('st_m',0,0)}</g></g>
   <g id="bub" opacity="0"><path d="M300,470 L330,360 L250,380 Z" fill="#fff" ${OLW}/><circle cx="200" cy="230" r="170" fill="#fff" ${OLW}/><path d="M248,392 L318,368" stroke="#fff" stroke-width="14"/>
    <g id="brainW" transform="translate(200,232)"><path d="M-120,10 C-130,-60 -70,-110 -10,-100 C40,-120 110,-90 120,-30 C140,20 110,80 50,84 C20,100 -40,100 -70,80 C-110,74 -126,46 -120,10 Z" fill="#f2a1a6" ${OLW}/>
     <path d="M-90,-30 q20,-20 40,0 q20,20 40,0 M-20,-80 q10,30 -10,50 M40,-70 q-6,30 20,40 M-100,30 q30,-10 50,10 M10,20 q30,-20 60,0 M70,-20 q20,20 40,10" fill="none" stroke="#a84a58" stroke-width="7" stroke-linecap="round"/>
     <path d="M-10,84 q6,30 -4,56" fill="none" stroke="${INK}" stroke-width="22" stroke-linecap="round"/><path d="M-10,84 q6,30 -4,56" fill="none" stroke="#e8939a" stroke-width="15" stroke-linecap="round"/>
     <g transform="translate(-6,-6)"><g transform="translate(-30,0)">${oEye('br_eL',26,'#f2a1a6')}</g><g transform="translate(30,0)">${oEye('br_eR',26,'#f2a1a6')}</g>${brow('br_bL')}${brow('br_bR')}<g transform="translate(0,46) scale(1.4)">${mouthEl('br_m',0,0)}</g></g></g></g>
   <g id="upArrow" opacity="0"><path d="M520,700 C560,560 620,420 640,140" fill="none" stroke="#fff" stroke-width="16" stroke-dasharray="26 18" stroke-linecap="round"/><path d="M612,170 L644,110 L672,176 Z" fill="#fff" ${OLW2}/></g>
   ${bodyCard(896,'1076','INSIDE THE STOMACH')}`;}
// ---- scene 2: the worry centre of the brain ----
function blob(id,col,label,w){return `<g id="${id}"><g class="fl"></g><ellipse rx="${w}" ry="${w*.9}" fill="${col}" ${OLW}/><path d="M${-w*.55},${-w*.45} q${w*.3},-${w*.3} ${w*.6},-${w*.2}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" opacity=".5"/>
   <rect x="${-w*.95}" y="${w*.12}" width="${w*1.9}" height="36" rx="6" fill="#fff" ${OLW2}/><text x="0" y="${w*.12+27}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:${label.length>8?21:24}px" fill="#1d2a44">${label}</text>
   <g transform="translate(0,${-w*.3})"><g transform="translate(-${w*.34},0)">${oEye(id+'_eL',w*.24,col)}</g><g transform="translate(${w*.34},0)">${oEye(id+'_eR',w*.24,col)}</g>${brow(id+'_bL')}${brow(id+'_bR')}</g><g transform="translate(0,${-w*.02}) scale(1.2)">${mouthEl(id+'_m',0,0)}</g></g>`;}
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
function sleepPill(){return `<g id="sp"><path d="M-70,0 C-70,-48 -40,-60 0,-60 C40,-60 70,-48 70,0 C70,48 40,60 0,60 C-40,60 -70,48 -70,0 Z" fill="#fff" ${OLW}/><path d="M0,-60 V60" stroke="#d6dde6" stroke-width="4"/><path d="M-46,-34 q16,-12 34,-10" fill="none" stroke="#e6ecf2" stroke-width="7" stroke-linecap="round"/>
   <g transform="translate(-20,-6)">${oEye('sp_eL',17,'#fff')}</g><g transform="translate(20,-6)">${oEye('sp_eR',17,'#fff')}</g>${brow('sp_bL')}${brow('sp_bR')}<g transform="translate(0,26) scale(1.2)">${mouthEl('sp_m',0,0)}</g>
   <path d="M-30,56 L-34,92 M30,56 L34,92" stroke="${INK}" stroke-width="7" stroke-linecap="round"/><path d="M-46,92 h24 M22,92 h24" stroke="${INK}" stroke-width="9" stroke-linecap="round"/></g>`;}
function amygScene(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#c4847a"/><ellipse cx="360" cy="420" rx="520" ry="420" fill="#d9a095" opacity=".7"/>
   <path d="M-40,760 C60,730 140,780 240,750 C340,720 420,770 520,740 C620,710 700,750 760,730 L760,1330 L-40,1330 Z" fill="#e2724e" ${OLW}/>
   ${[[60,880],[300,940],[520,860],[160,1060],[440,1090],[620,1010],[80,1200],[380,1220]].map(([x,y])=>`<path d="M${x},${y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#a84a30" stroke-width="5" stroke-linecap="round"/>`).join('')}
   <g transform="translate(360,92)"><rect x="-300" y="-36" width="600" height="72" rx="14" fill="#fff" ${OLW}/><text x="0" y="12" text-anchor="middle" style="font-family:LG,sans-serif;font-size:30px" fill="#1d2a44">AMYGDALA: THE WORRY CENTRE</text></g>
   ${bodyCard(150,'190','INSIDE THE BRAIN')}
   <g id="bG" transform="translate(440,770)">${blob('bg','#9bc25a','CORTISOL',96)}</g><g id="bB" transform="translate(640,800)">${blob('bb','#2f7fd0','GLUTAMATE',92)}</g><g id="bY" transform="translate(540,930)">${blob('by','#f6d78a','ADRENALINE',104)}</g>
   <g id="copW">${copSVG()}</g>
   <g id="spW">${sleepPill()}</g>
   <g id="smoke" opacity="0"></g>`;}
// ---- scene 3: the bedroom ----
function wifeSVG(){return `<g id="wife"><path d="M-78,-176 V160 M-78,20 H84 M84,20 V160 M-30,24 V150" fill="none" stroke="#141418" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/><path d="M-84,6 H92 V28 H-84 Z" fill="#26262c" ${OLW2}/>
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
   <path d="M-40,820 H380 V1060 H-40 Z" fill="#fff" ${OLW}/><path d="M-40,780 H380 Q400,780 400,820 V860 H-40 Z" fill="#f2f2f2" ${OLW}/><path d="M-40,1060 H380 V1110 H-40 Z" fill="#8a6a4c" ${OLW}/><path d="M360,1110 V1170" stroke="${INK}" stroke-width="22"/>
   <g id="wifeW"></g><g id="husW"></g>`;}

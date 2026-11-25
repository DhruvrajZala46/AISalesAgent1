// =============== 020: why babies under 6 months shouldn't drink water. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_ST='#f28e92', C_ST_L='#f9cfcb', C_ST_D='#d9686f', C_BG1='#a8736c', C_LIV='#c94f53', C_GUT='#f2a3a7', C_BSK='#f8dcc8';
const lim=(d,wd,col)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
const arcsD=(n=3)=>Array.from({length:n},(_,j)=>`<path d="M${-34-j*4},${-j*24} q${34+j*4},-26 ${68+j*8},0" fill="none" stroke="${INK}" stroke-width="19" stroke-linecap="round"/><path d="M${-34-j*4},${-j*24} q${34+j*4},-26 ${68+j*8},0" fill="none" stroke="#ffe81a" stroke-width="12" stroke-linecap="round"/>`).join('');
const BODY_D='M40,-40 C50,120 100,250 180,330 C160,470 200,600 330,640 C470,680 660,660 770,560 L770,250 C700,170 600,145 520,158 C430,170 360,215 300,246 C210,190 165,90 150,-40 Z';
const STREAM_D='M96,-60 C108,90 150,220 236,296 C262,330 270,420 276,640';
// ---- scene 1: the baby's stomach ----
function stomachScene(){
  DEFS+=`<clipPath id="stC"><path d="${BODY_D}"/></clipPath>`;
  const scal=(y0,slope,r,col)=>Array.from({length:10},(_,i)=>{const x=-20+i*84;return `<circle cx="${x}" cy="${(y0+slope*x).toFixed(0)}" r="${r}" fill="${col}" ${OLW2}/>`;}).join('');
  return `<rect x="-40" y="-40" width="800" height="1360" fill="${C_BG1}"/>
   <path d="M-40,1040 C220,1000 520,930 770,800 L770,1330 L-40,1330 Z" fill="#b85a62" ${OLW}/>
   ${[[60,1210],[230,1190],[420,1150],[610,1100]].map(([x,y])=>`<path d="M${x},${y} q60,-40 120,0 q-20,60 -10,130 h-100 q10,-70 -10,-130 Z" fill="#c9656d" ${OLW2}/>`).join('')}
   ${scal(1068,-.3,50,'#e88f96')}<path d="M-40,1068 C220,1020 520,950 770,826 L770,960 C520,1070 220,1130 -40,1160 Z" fill="#e88f96"/>
   ${scal(968,-.3,52,C_GUT)}<path d="M-40,960 C220,930 520,860 770,740 L770,860 C520,980 220,1040 -40,1070 Z" fill="${C_GUT}"/>
   <path d="M-40,1000 C220,968 520,900 770,780" fill="none" stroke="${INK}" stroke-width="3"/><path d="M-40,1024 C220,992 520,924 770,804" fill="none" stroke="#fbd3d3" stroke-width="10"/>
   <path d="M-40,540 L170,470 C190,620 330,700 520,700 C640,700 720,660 770,610 L770,790 C560,900 260,960 -40,990 Z" fill="${C_LIV}" ${OLW}/>
   <path d="M300,900 C460,880 620,830 740,760" fill="none" stroke="#ee8a8a" stroke-width="12" stroke-linecap="round"/>
   <path d="${BODY_D}" fill="${C_ST}" ${OLW}/>
   <g clip-path="url(#stC)"><path d="${BODY_D}" fill="none" stroke="${C_ST_L}" stroke-width="30"/><path d="M96,-40 C108,90 150,210 230,290" fill="none" stroke="#e77a82" stroke-width="40" opacity=".5"/>
    <path d="M330,300 q-16,120 10,240 M420,280 q-10,140 16,300 M700,300 q20,120 -4,230" fill="none" stroke="${C_ST_D}" stroke-width="5" stroke-linecap="round" opacity=".45"/>
    <g id="pool"></g><path id="stream" d="${STREAM_D}" fill="none" stroke-linecap="round" opacity="0"/><g id="steam"></g></g>
   <path d="${BODY_D}" fill="none" ${OLW}/>
   <g id="vArcs" transform="translate(100,60) rotate(-20)" opacity="0">${arcsD()}</g>
   <g id="armL"></g><g id="armR"></g>
   <g id="paper"><g transform="rotate(-6)"><path d="M-150,-70 L0,-52 L150,-76 L158,74 L0,96 L-156,70 Z" fill="#e9e9e4" ${OLW}/><path d="M0,-52 V96" ${OLW2}/>
     <text x="78" y="-30" text-anchor="middle" style="font-family:LG,sans-serif;font-size:30px" fill="#3a3a3a" transform="rotate(-8,78,-30)">NEWS</text>
     ${[-34,-10,14,38,62].map(y=>`<path d="M-136,${y+4} L-18,${y+14} M20,${y+10} L140,${y}" stroke="#9a9a96" stroke-width="6" stroke-linecap="round"/>`).join('')}</g></g>
   <g id="sface" transform="translate(540,236)"><g id="sEyes"><g transform="translate(-44,0)">${oEye('st_eL',36,C_ST)}</g><g transform="translate(44,0)">${oEye('st_eR',36,C_ST)}</g></g>
     <g id="sSpark" opacity="0">${[-44,44].map(x=>`<g transform="translate(${x},0)"><ellipse rx="33" ry="36" fill="#fff" ${OLW2}/><circle cx="0" cy="6" r="25" fill="#171313"/><circle cx="-9" cy="-4" r="9" fill="#fff"/><circle cx="10" cy="12" r="5" fill="#fff"/><path d="M8,-10 l3,7 l7,3 l-7,3 l-3,7 l-3,-7 l-7,-3 l7,-3 Z" fill="#fff"/></g>`).join('')}</g>
     ${brow('st_bL')}${brow('st_bR')}<g transform="translate(0,74) scale(2)">${mouthEl('st_m',0,0)}</g>
     <path id="tongue" d="M0,78 C30,70 56,84 60,104 C62,118 44,122 34,110 C22,98 10,92 0,92 Z" fill="#ef6f86" ${OLW2} opacity="0"/>
     <g id="paci" transform="translate(0,84)"><ellipse rx="34" ry="22" fill="#9fd4ee" ${OLW2}/><circle r="12" fill="#e6f5fc" ${OLW2}/><circle cx="0" cy="26" r="13" fill="none" stroke="${INK}" stroke-width="6.5"/><circle cx="0" cy="26" r="13" fill="none" stroke="#6fb6d8" stroke-width="3"/></g></g>
   ${bodyCard()}<g id="spoon" opacity="0"><path d="M0,0 L60,150" stroke="${INK}" stroke-width="13" stroke-linecap="round"/><path d="M0,0 L60,150" stroke="#b9bec4" stroke-width="7" stroke-linecap="round"/><path d="M44,146 C40,186 96,190 96,150 Z" fill="#b9bec4" ${OLW2}/></g>
   <g id="phone" opacity="0"><g transform="rotate(18)"><rect x="-26" y="-56" width="52" height="112" rx="10" fill="#17171a" ${OLW2}/><rect x="-19" y="-44" width="38" height="78" rx="4" fill="#2c3440"/></g><g id="pArcs" transform="translate(36,-74) rotate(30) scale(.7)" opacity="0">${arcsD()}</g></g>`;}
function bodyCard(){return `<g id="inset"><rect x="14" y="640" width="200" height="330" rx="18" fill="#fff" ${OLW}/>
   <circle cx="114" cy="712" r="44" fill="${C_BSK}" ${OLW2}/><path d="M104,668 C108,654 124,654 122,668" fill="none" ${OLW2}/><circle cx="100" cy="708" r="5" fill="${INK}"/><circle cx="128" cy="708" r="5" fill="${INK}"/><path d="M104,726 q10,8 20,0" fill="none" ${OLW2}/>
   <path d="M70,772 C70,750 158,750 158,772 L164,868 C164,900 64,900 64,868 Z" fill="${C_BSK}" ${OLW2}/><path d="M64,852 C90,838 138,838 164,852 L164,868 C164,900 64,900 64,868 Z" fill="#fff" ${OLW2}/>
   <path d="M70,780 L40,826 M158,780 L188,826" stroke="${INK}" stroke-width="19" stroke-linecap="round"/><path d="M70,780 L40,826 M158,780 L188,826" stroke="${C_BSK}" stroke-width="13" stroke-linecap="round"/>
   <path d="M104,790 C120,780 140,792 136,812 C132,828 110,830 102,816 C98,806 98,796 104,790 Z" fill="${C_ST}" ${OLW2}/><circle id="ring" cx="118" cy="806" r="26" fill="none" stroke="#e02626" stroke-width="6"/>
   <text x="114" y="930" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#1d2a44">INSIDE THE</text><text x="114" y="954" text-anchor="middle" style="font-family:LG,sans-serif;font-size:19px" fill="#1d2a44">BABY'S TUMMY</text></g>`;}
// ---- scene 2: inside the small intestine ----
function gutScene(){
  const villi=(y,dir,seed)=>Array.from({length:17},(_,i)=>{const x=-10+i*46,L=58+((i*37+seed*13)%5)*13,w=17;
    return `<path d="M${x-w},${y} L${x-w},${y+dir*L} C${x-w},${y+dir*(L+26)} ${x+w},${y+dir*(L+26)} ${x+w},${y+dir*L} L${x+w},${y} Z" fill="#ee6d7b" ${OLW2}/><path d="M${x},${y+dir*14} V${y+dir*(L-4)}" stroke="#b9485a" stroke-width="9" stroke-linecap="round"/>`;}).join('');
  const lumps=(y)=>Array.from({length:7},(_,i)=>`<ellipse cx="${-20+i*130}" cy="${y+((i*53)%3)*22}" rx="92" ry="66" fill="#8a4a47" ${OLW2}/>`).join('');
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#6e3a38"/>${lumps(10)}${lumps(1250)}
   <rect x="-40" y="330" width="800" height="760" fill="#a8736c"/>
   <g id="flood"></g>
   ${villi(326,1,1)}${villi(1094,-1,2)}
   <path d="M-40,120 H760 V330 H-40 Z" fill="#f78a8d" ${OLW}/><path d="M-40,300 H760" stroke="#e0606c" stroke-width="18"/>
   <path d="M-40,1090 H760 V1180 H-40 Z" fill="#ef6471" ${OLW}/><path d="M-40,1110 H760" stroke="#f9a1a6" stroke-width="10"/>
   <g id="gface" transform="translate(360,214)"><g transform="translate(-46,0)">${oEye('gt_eL',38,'#f78a8d')}</g><g transform="translate(46,0)">${oEye('gt_eR',38,'#f78a8d')}</g>${brow('gt_bL')}${brow('gt_bR')}<g transform="translate(0,62) scale(1.8)">${mouthEl('gt_m',0,0)}</g></g>`;}
// ---- the baby ----
function babySVG(id){return `<g id="${id}"><g transform="rotate(-14)">
   <path d="M-30,-34 C20,-62 120,-34 136,26 C144,62 110,84 66,72 C8,58 -40,26 -30,-34 Z" fill="#bfe3f5" ${OLW}/>
   <path d="M-12,-30 C36,-6 84,14 128,56 M40,-44 C30,-10 24,20 30,58" fill="none" stroke="#8fc4de" stroke-width="5" stroke-linecap="round"/>
   <g id="${id}_arm"><circle cx="34" cy="-8" r="13" fill="${C_BSK}" ${OLW2}/></g>
   <g id="${id}_head" transform="translate(-52,-40)"><circle r="50" fill="${C_BSK}" ${OLW}/><path d="M-46,8 C-58,4 -60,24 -46,26" fill="${C_BSK}" ${OLW2}/>
    <path d="M-10,-50 C-4,-70 14,-70 12,-52 M4,-50 C14,-64 28,-58 22,-46" fill="none" ${OLW2}/>
    <g transform="translate(-10,-4)"><circle r="14" fill="#fff" ${OLW2}/><circle id="${id}_pL" r="6.5" fill="#171313"/></g><g transform="translate(26,-2)"><circle r="14" fill="#fff" ${OLW2}/><circle id="${id}_pR" r="6.5" fill="#171313"/></g>
    <path d="M-24,-26 q12,-8 24,0 M16,-24 q12,-8 22,2" fill="none" ${OLW2}/><ellipse id="${id}_m" cx="10" cy="26" rx="8" ry="6" fill="#8c3a3a" ${OLW2}/>
    <ellipse cx="-24" cy="20" rx="9" ry="6" fill="#f3a9a0" opacity=".75"/><ellipse cx="38" cy="20" rx="8" ry="6" fill="#f3a9a0" opacity=".75"/></g>
   <path d="M-34,-6 C-10,14 10,6 22,-30" fill="none" stroke="#bfe3f5" stroke-width="16" stroke-linecap="round"/><path d="M-36,2 C-10,24 18,12 30,-28" fill="none" ${OLW2}/></g></g>`;}
// ---- dad: the channel's patient, with one arm bent to hold a glass and the baby in the other ----
function dadSVG(){let s=patientSVG();const a=s.indexOf('<!-- right arm (hangs) -->'),b=s.indexOf('<g id="patHead">');
  const armR=`<g id="dadArmR">${shaded(limbD([[84,234],[124,336],[164,296]],[44,38,32]),'#c7884a','#a86c34',10)}<g id="glass" transform="translate(112,-116)"><path d="M26,318 L36,412 L84,412 L94,318 Z" fill="#eaf8fd" ${OLW2}/><path d="M30,352 L36,410 L84,410 L90,352 Z" fill="#7cc8ea"/><path d="M26,318 L36,412 L84,412 L94,318 Z" fill="none" ${OLW}/></g>${hand(170,292,-150,1.2,PSK)}</g>`;
  s=s.slice(0,a)+armR+s.slice(b);
  return s.replace('<!-- left arm: hand to ear -->',`<g id="dadBaby" transform="translate(-36,356) scale(1.12)">${babySVG('bb1')}</g>`);}
// ---- mom, seated, holding the baby ----
function momSVG(){return `<g id="mom"><path d="M-78,-176 V160 M-78,20 H84 M84,20 V160 M-30,24 V150" fill="none" stroke="#141418" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/><path d="M-84,6 H92 V28 H-84 Z" fill="#26262c" ${OLW2}/>
   ${lim('M-20,-8 C30,-16 70,-12 96,0 C104,50 100,100 98,146',50,'#24242a')}${lim('M-34,-2 C20,-14 60,-10 76,2 C84,50 82,100 80,150',50,'#2c2c33')}
   <path d="M64,150 C100,140 132,152 134,168 L62,170 Z" fill="#f4a4be" ${OLW2}/><path d="M82,146 C118,136 150,148 152,164 L80,166 Z" fill="#f4a4be" ${OLW2}/>
   <path d="M-70,-196 C-40,-214 20,-214 44,-196 C60,-150 56,-60 44,0 L-66,0 C-80,-60 -84,-150 -70,-196 Z" fill="#f6adc4" ${OLW}/>
   <path d="M-22,-250 L-20,-200 L12,-200 L12,-250 Z" fill="${DSK}" ${OLW2}/>
   <path d="M-76,-286 C-96,-380 60,-390 58,-290 C76,-250 70,-200 40,-190 C52,-230 30,-250 -40,-250 C-70,-240 -84,-210 -76,-180 C-104,-210 -100,-260 -76,-286 Z" fill="#4a1f2a" ${OLW}/>
   <g id="momHead"><path d="M-54,-296 C-56,-340 36,-346 40,-296 C42,-262 28,-238 6,-226 C-6,-222 -22,-222 -32,-228 C-48,-240 -54,-266 -54,-296 Z" fill="${DSK}" ${OLW}/>
    <path d="M-60,-290 C-70,-360 30,-374 48,-306 C20,-330 -20,-334 -44,-318 C-52,-310 -58,-300 -60,-290 Z" fill="#4a1f2a" ${OLW2}/>
    ${humanEye('mEyeL',-22,-286,12,8)}${humanEye('mEyeR',18,-286,12,8)}
    <path d="M-36,-306 Q-22,-314 -10,-304 M6,-304 Q20,-314 32,-306" fill="none" stroke="#3a1820" stroke-width="4" stroke-linecap="round"/>
    <path d="M0,-280 C6,-268 6,-262 0,-258" fill="none" ${TH('#b98468')}/><ellipse id="momMouth" cx="-2" cy="-242" rx="9" ry="6" fill="#8c2f3a" ${OLW2}/><ellipse cx="-34" cy="-262" rx="9" ry="5" fill="#ef8f86" opacity=".6"/><ellipse cx="26" cy="-262" rx="9" ry="5" fill="#ef8f86" opacity=".6"/></g>
   <g transform="translate(24,-84) scale(1.05)">${babySVG('bb2')}</g>
   ${lim('M-50,-170 C-70,-110 -60,-60 -20,-40 C20,-28 60,-30 96,-44',34,'#f6adc4')}<circle cx="100" cy="-46" r="16" fill="${DSK}" ${OLW2}/></g>`;}
// ---- scene 3: the living room (background only; dad is a shared layer) ----
function homeBG(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#efc2a8"/><rect x="-40" y="-40" width="800" height="70" fill="#8a5a3c"/><rect x="-40" y="30" width="800" height="14" fill="#f7dcc8" ${OLW2}/>
   <path d="M-40,1010 H760 V1330 H-40 Z" fill="#6d5a5e"/><path d="M-40,1010 H760" ${OLW}/><path d="M60,1090 L620,1090 L720,1250 L-20,1250 Z" fill="#7e6a70" ${OLW2}/>
   <path d="M-40,640 C40,620 110,660 120,760 L120,1040 L-40,1040 Z" fill="#5fd2c2" ${OLW}/><path d="M-40,900 H150 V1060 H-40 Z" fill="#4fc0b0" ${OLW}/>
   <path d="M150,880 H330 V1040 H150 Z" fill="#f2cf86" ${OLW}/><path d="M166,900 H314 V950 H166 Z M166,966 H314 V1020 H166 Z" fill="#e8bd6c" ${OLW2}/><path d="M228,926 h24 M228,994 h24" ${OLW}/>
   <path d="M450,470 H760 V494 H450 Z" fill="#e0b070" ${OLW}/><path d="M486,494 H760 V640 H486 Z" fill="#a8763c" ${OLW}/><path d="M506,512 H760 V624 H506 Z" fill="#7a5226"/>
   ${[['#2f6fb8',530],['#2f9e5a',562],['#e0a020',594],['#b83a3a',626],['#3a4ab8',658]].map(([c,x])=>`<rect x="${x}" y="532" width="26" height="92" fill="${c}" ${OLW2}/>`).join('')}
   <g id="spk"><path d="M520,300 H650 V470 H520 Z" fill="#48b7c4" ${OLW}/><path d="M520,300 L544,284 H674 L650,300 Z M650,300 L674,284 V452 L650,470 Z" fill="#3597a4" ${OLW2}/><circle cx="585" cy="372" r="42" fill="#2d7f8b" ${OLW2}/><circle cx="585" cy="372" r="20" fill="#16434a" ${OLW2}/><rect x="560" y="434" width="50" height="14" rx="6" fill="#d6f3f6" ${OLW2}/></g>
   <path d="M690,400 L698,470 H744 L752,400 Z" fill="#f4f4f0" ${OLW2}/>
   <g id="spArcs" transform="translate(700,330) rotate(60)" opacity="0">${arcsD()}</g>`;}
// ---- scene 4: the clinic ----
function clinicBG(){const row=(id,y,col,txt)=>`<g id="${id}" opacity="0"><rect x="60" y="${y}" width="600" height="66" rx="14" fill="${col}" stroke="#1d2a44" stroke-width="4"/><text x="360" y="${y+46}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:31px;letter-spacing:.5px" fill="#fff">${txt}</text></g>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#dcdcf0"/>
   <rect x="-40" y="760" width="800" height="290" fill="#c8d27c"/><rect x="-40" y="740" width="800" height="26" fill="#7a5a3c" ${OLW2}/>
   <path d="M-40,1050 H760 V1330 H-40 Z" fill="#6b5f58"/><path d="M-40,1050 H760" ${OLW}/>
   <g id="brd"><rect x="36" y="46" width="660" height="424" rx="24" fill="#000" opacity=".12"/><rect x="28" y="36" width="660" height="424" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="104" text-anchor="middle" style="font-family:LG,sans-serif;font-size:46px;letter-spacing:1px" fill="#1d2a44">WATER INTOXICATION</text>
   ${row('b0',128,'#2f8fe0','1. TINY KIDNEYS CAN\'T COPE')}${row('b1',206,'#8a5bd1','2. BLOOD GETS TOO WATERY')}${row('b2',284,'#e8473f','3. THE BRAIN SWELLS')}${row('b3',362,'#2fae62','UNDER 6 MONTHS: MILK ONLY')}</g>`;}

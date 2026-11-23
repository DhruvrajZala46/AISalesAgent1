// =============== 016: "this habit left him with one lung". The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_PINK='#f29aa8', C_PINK_S='#cf7086', C_DARK='#5d3d38', C_DARK_S='#392320', C_STEEL='#c3cad3', C_TEAL='#14a3a0';
const PINK_D='M250,250 C300,250 326,330 326,430 C326,520 318,610 320,700 C322,790 250,880 150,890 C60,896 14,820 20,700 C26,560 90,400 150,310 C180,266 215,250 250,250 Z';
const DARK_D='M470,250 C420,250 396,330 396,430 C396,520 402,610 400,690 C398,760 450,820 540,826 C630,830 690,760 686,660 C680,540 620,400 570,310 C544,266 505,250 470,250 Z';
const darkArt=()=>`<path d="${DARK_D}" fill="${C_DARK}"/><path d="${DARK_D}" fill="none" stroke="${C_DARK_S}" stroke-width="20" opacity=".55"/>
  <path d="M400,600 C470,560 560,580 680,640 M410,440 C470,480 540,470 610,420" fill="none" stroke="${C_DARK_S}" stroke-width="6" stroke-linecap="round"/>
  ${[[450,330,9],[520,360,7],[560,520,10],[470,560,8],[610,600,9],[500,700,11],[590,730,8],[440,690,7],[640,680,6],[540,300,6]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="#2a1917" opacity=".8"/>`).join('')}
  <path d="M430,380 q14,10 6,26 M600,470 q-12,14 0,28 M480,640 q16,6 12,24" fill="none" stroke="#2a1917" stroke-width="4" stroke-linecap="round"/><path d="${DARK_D}" fill="none" ${OLW}/>`;
const packSVG=()=>`<rect x="-26" y="-34" width="52" height="68" rx="5" fill="#f7ead0" ${OLW2}/><rect x="-26" y="-34" width="52" height="20" rx="5" fill="#d8443a" ${OLW2}/>${[-14,0,14].map(x=>`<rect x="${x-5}" y="-48" width="10" height="18" rx="2" fill="#fff" ${OLW2}/><rect x="${x-5}" y="-48" width="10" height="6" fill="#e9a23b"/>`).join('')}`;
const cigSVG=()=>`<rect x="-24" y="-5" width="48" height="10" rx="3" fill="#fff" ${OLW2}/><rect x="-24" y="-5" width="14" height="10" rx="3" fill="#e9a23b" ${OLW2}/><circle cx="26" cy="0" r="4.5" fill="#ff6a2b"/>`;
function chestWorld(){
  DEFS+=`<clipPath id="pc1"><path d="M380,200 H720 V452 L380,488 Z"/></clipPath><clipPath id="pc2"><path d="M380,488 L720,452 V628 L380,652 Z"/></clipPath><clipPath id="pc3"><path d="M380,652 L720,628 V900 H380 Z"/></clipPath>`;
  let s=`<g id="chest"><rect x="-40" y="-40" width="800" height="1360" fill="#ad6a63"/>
   <path d="M-40,-40 H250 C250,60 210,150 130,170 C70,184 20,170 -40,190 Z" fill="#7b4a46" stroke="#c98a80" stroke-width="8"/><path d="M760,-40 H470 C470,60 510,150 590,170 C650,184 700,170 760,190 Z" fill="#7b4a46" stroke="#c98a80" stroke-width="8"/>
   <path d="M60,1000 q40,80 30,180 M660,1000 q-40,80 -30,180" fill="none" stroke="#96564f" stroke-width="7" stroke-linecap="round"/>
   <path d="M-40,1010 C120,900 600,900 760,1010 L760,1320 L-40,1320 Z" fill="#a1605a"/><path d="M-40,1010 C120,900 600,900 760,1010" fill="none" stroke="#8a4d48" stroke-width="6"/>
   <g id="ccam" transform="translate(360,600) scale(1.04) translate(-358,-590)"><path d="M336,-130 V400 C336,440 300,450 286,470 M384,-130 V400 C384,440 420,450 434,470" fill="none" stroke="${INK}" stroke-width="5"/>
   <path d="M336,-130 H384 V404 C384,436 414,448 432,470 L410,490 C392,468 372,452 360,452 C348,452 328,468 310,490 L288,470 C306,448 336,436 336,404 Z" fill="#c4c7ce" ${OLW}/>
   ${Array.from({length:20},(_,i)=>`<path d="M338,${-114+i*26} q22,9 44,0" fill="none" stroke="#8d919b" stroke-width="5" stroke-linecap="round"/>`).join('')}
   <path id="cavity" d="${DARK_D}" fill="#cf7a6e" stroke="#9a4f48" stroke-width="5" transform="translate(540,540) scale(1.04) translate(-540,-540)"/>
   <g id="tray"><rect x="-215" y="-62" width="430" height="124" rx="16" fill="#8f98a5" ${OLW}/><rect x="-196" y="-46" width="392" height="92" rx="10" fill="#c9d0d9" ${OLW2}/><path d="M-180,-34 h200" stroke="#eef1f5" stroke-width="7" stroke-linecap="round"/></g>
   <g id="pinkG"><g id="pinkB">${shaded(PINK_D,C_PINK,C_PINK_S,22)}<path d="M40,640 C130,600 230,640 320,700 M120,420 C200,470 270,470 326,440" fill="none" stroke="${C_PINK_S}" stroke-width="6" stroke-linecap="round"/><path d="M70,560 C80,460 130,370 190,310" fill="none" stroke="#ffc6cf" stroke-width="10" stroke-linecap="round" opacity=".8"/>
     <g transform="translate(228,452)"><g transform="translate(-42,0)">${oEye('pk_eL',40,C_PINK)}</g><g transform="translate(42,0)">${oEye('pk_eR',40,C_PINK)}</g>${brow('pk_bL')}${brow('pk_bR')}${mouthEl('pk_m',2,86)}</g></g>
     <g id="pkHand"><path id="pkArm" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/><g id="pkPack">${packSVG()}</g><g id="pkCig">${cigSVG()}</g></g><g id="pkSweat"></g></g>
   <g id="darkG"><g id="dp3" clip-path="url(#pc3)"><g id="dp3m">${darkArt()}</g></g><g id="dp2" clip-path="url(#pc2)"><g id="dp2m">${darkArt()}</g></g><g id="dp1" clip-path="url(#pc1)"><g id="dp1m">${darkArt()}<path id="dSleep" d="M446,440 q22,14 44,0 M524,440 q22,14 44,0" fill="none" stroke="#f4e9e6" stroke-width="6" stroke-linecap="round" opacity="0"/></g></g>
     <g id="darkFace" transform="translate(508,440)"><g transform="translate(-40,0)">${oEye('dk_eL',38,C_DARK)}</g><g transform="translate(40,0)">${oEye('dk_eR',38,C_DARK)}</g>${brow('dk_bL')}${brow('dk_bR')}${mouthEl('dk_m',0,80)}</g>
     <g id="dkHand"><path id="dkArm" fill="none" stroke="${INK}" stroke-width="6" stroke-linecap="round"/><g id="dkCig">${cigSVG()}</g></g><g id="cuts"></g></g>
   <g id="smoke"></g><g id="dkPack">${packSVG()}</g>
   
   <g id="cone" opacity="0"><path d="M0,0 L-190,-250 L40,-330 Z" fill="#8fe3ff" opacity=".42" stroke="#49b8e0" stroke-width="3"/>${[[-70,-170,16],[-30,-230,13],[-100,-220,11],[-50,-120,10],[-10,-280,9]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="#2f4a52" opacity=".7"/>`).join('')}</g>
   <g id="scope"><path d="M60,70 C160,200 260,330 420,460" fill="none" stroke="${INK}" stroke-width="16" stroke-linecap="round"/><path d="M60,70 C160,200 260,330 420,460" fill="none" stroke="#2d313c" stroke-width="10" stroke-linecap="round"/>
     <g transform="rotate(38)"><rect x="-34" y="-10" width="68" height="230" rx="30" fill="#f4f6f8" ${OLW}/><rect x="-20" y="96" width="40" height="96" rx="12" fill="#dfe5ec" ${OLW2}/>${[112,130,148,166].map(y=>`<path d="M-12,${y} h24" stroke="#9aa3b0" stroke-width="5" stroke-linecap="round"/>`).join('')}
      <rect x="-22" y="30" width="44" height="50" rx="9" fill="#6fb6f2" ${OLW2}/><path d="M0,42 v26 M-13,55 h26" stroke="#fff" stroke-width="7" stroke-linecap="round"/></g>
     <circle r="40" fill="#1d2a44" ${OLW}/><circle r="27" fill="#5ed0ff" ${OLW2}/><circle cx="-8" cy="-9" r="8" fill="#fff" opacity=".8"/>
     <g id="scFace" opacity="0" transform="translate(-58,84) scale(1.25)"><g transform="translate(-17,0)">${oEye('sc_eL',16,'#f4f6f8')}</g><g transform="translate(17,0)">${oEye('sc_eR',16,'#f4f6f8')}</g>${mouthEl('sc_m',0,30)}</g></g>
   <g id="scalpel"><path d="M0,0 L20,-70 L48,-54 Z" fill="#eef2f6" ${OLW}/><path d="M30,-60 L150,-270" stroke="${INK}" stroke-width="28" stroke-linecap="round"/><path d="M30,-60 L150,-270" stroke="${C_STEEL}" stroke-width="21" stroke-linecap="round"/><path d="M60,-112 L120,-216" stroke="#8f98a5" stroke-width="5" stroke-linecap="round"/>
     <g transform="translate(34,-96)"><g transform="translate(-13,6)">${oEye('sl_eL',14,C_STEEL)}</g><g transform="translate(15,-8)">${oEye('sl_eR',14,C_STEEL)}</g></g></g>
   <g id="syringe"><path d="M0,0 L40,-66" stroke="${INK}" stroke-width="5" stroke-linecap="round"/><g transform="translate(40,-66) rotate(31)"><rect x="-24" y="-170" width="48" height="170" rx="6" fill="#f5f8fb" ${OLW}/><rect x="-18" y="-90" width="36" height="84" rx="3" fill="#ffd93b"/>${[-150,-125,-100].map(y=>`<path d="M-24,${y} h16" stroke="${INK}" stroke-width="3"/>`).join('')}<rect x="-34" y="-180" width="68" height="14" rx="5" fill="#dfe5ec" ${OLW2}/><rect id="plunger" x="-9" y="-250" width="18" height="74" fill="#dfe5ec" ${OLW2}/><rect x="-28" y="-262" width="56" height="16" rx="6" fill="#f5f8fb" ${OLW2}/></g></g>
   <g id="forceps"><path d="M0,0 L130,-190 L144,-180 L12,8 Z" fill="${C_STEEL}" ${OLW2}/><path d="M8,10 L152,-170 L164,-158 L16,18 Z" fill="#e3e8ee" ${OLW2}/></g></g></g>`;
  return s;}
// ---- the hospital room: our patient in bed, our doctor beside him ----
function ward(){
  DEFS+=`<clipPath id="bedC"><rect x="-300" y="-100" width="600" height="700"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#cfe0e6"/><rect x="430" y="-40" width="26" height="700" fill="#eef7fa"/><rect x="456" y="-40" width="8" height="700" fill="#b9cdd4"/>
   <rect x="-40" y="560" width="800" height="14" fill="#b9cdd4"/>
   <g transform="translate(360,640) scale(1.3) translate(-372,-560)"><g transform="translate(176,330) scale(1.22)">${doctorSVG()}</g>
   <path d="M440,560 C440,500 700,500 700,560 L720,900 L420,900 Z" fill="#fff" ${OLW}/><path d="M470,590 q90,-40 200,0" fill="none" stroke="#d5dde2" stroke-width="6" stroke-linecap="round"/>
   <g id="patWrap"><g transform="translate(545,470) scale(1.3)"><g clip-path="url(#bedC)">${patientSVG()}</g></g></g></g><g transform="translate(0,84)">
   <path d="M-40,1000 C60,930 180,880 300,930 C380,880 520,850 640,880 C700,892 740,900 760,910 L760,1320 L-40,1320 Z" fill="#fff" ${OLW}/>
   <path d="M60,1010 C160,960 240,950 300,1000 C330,1040 330,1120 300,1200 M360,960 C460,910 580,910 700,950 M420,1040 C500,1010 600,1010 700,1060 M120,1120 C180,1100 230,1110 260,1150" fill="none" stroke="#cfd6db" stroke-width="7" stroke-linecap="round"/></g>`;}

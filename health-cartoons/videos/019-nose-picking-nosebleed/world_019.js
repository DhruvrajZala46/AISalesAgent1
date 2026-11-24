// =============== 019: how picking your nose makes it bleed. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f6cfa8', C_SK_S='#e4b184', C_CAV='#a8323c', C_CAV_S='#7c1f2a', C_BLOOD='#e02634', C_TEAL='#14a3a0';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const CAV_D='M300,250 C400,250 540,520 610,720 C640,810 600,860 540,860 C500,862 486,900 482,964 L348,964 C344,900 330,862 290,860 C220,858 190,720 210,520 C222,380 250,270 300,250 Z';
const fingerSVG=(w,len)=>`<path d="M${-w/2},${len} L${-w/2},${w*.5} C${-w/2},${-w*.2} ${w/2},${-w*.2} ${w/2},${w*.5} L${w/2},${len} Z" fill="${C_SK}" ${OLW}/><path d="M${-w*.3},${w*.5} C${-w*.3},${w*.1} ${w*.3},${w*.1} ${w*.3},${w*.5} L${w*.3},${w*.95} L${-w*.3},${w*.95} Z" fill="#fde9da" ${OLW2}/><path d="M${-w*.3},${w*1.9} h${w*.6} M${-w*.26},${w*2.1} h${w*.52}" stroke="${C_SK_S}" stroke-width="4" stroke-linecap="round"/>`;
const card=(inner,txt)=>`<g id="inset"><rect x="16" y="130" width="196" height="330" rx="18" fill="#fff" ${OLW}/>${inner}<text x="114" y="440" text-anchor="middle" style="font-family:LG,sans-serif;font-size:20px" fill="#1d2a44">${txt}</text></g>`;
// ---- scene 1: inside the nose (cut from the side) ----
function insideNose(){
  DEFS+=`<clipPath id="cavC"><path d="${CAV_D}"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#d9f0fa"/>
   <path d="M-40,-40 L230,-40 C380,180 640,560 700,740 C740,860 680,950 560,950 L500,950 C470,950 460,990 480,1040 C500,1100 470,1180 420,1240 L400,1320 L-40,1320 Z" fill="${C_SK}" ${OLW}/>
   <path d="M360,-10 C470,200 600,470 660,640" fill="none" stroke="#fde3c9" stroke-width="22" stroke-linecap="round" opacity=".8"/>
   <path d="M560,560 C640,600 690,700 660,800 C640,860 580,900 520,900" fill="none" stroke="${C_SK_S}" stroke-width="10" stroke-linecap="round"/><ellipse cx="415" cy="966" rx="96" ry="26" fill="#fde3c9" ${OLW2}/><path d="${CAV_D}" fill="${C_CAV}" ${OLW}/>
   <g clip-path="url(#cavC)"><path d="${CAV_D}" fill="none" stroke="${C_CAV_S}" stroke-width="40" opacity=".5"/>
    <g id="vessels"><path d="M250,560 C330,540 380,600 440,640 C480,668 520,700 560,760 M380,600 C400,540 440,500 470,440 M440,640 C420,700 400,740 396,800 M300,548 C290,480 300,420 320,370" fill="none" stroke="#e4636c" stroke-width="6" stroke-linecap="round"/></g>
    ${[[250,440,34,16,-60],[520,600,30,13,62],[290,800,30,13,10],[540,810,26,11,-20]].map(([x,y,a,b,r])=>`<ellipse cx="${x}" cy="${y}" rx="${a}" ry="${b}" fill="#a39a4c" opacity=".85" transform="rotate(${r},${x},${y})"/>`).join('')}
    <g id="scratch" opacity="0"><path d="M372,664 l22,-18 l14,16 l24,-14 l16,22 l-10,26 l14,24 l-22,18 l-20,-10 l-24,16 l-14,-24 l-18,-8 l10,-26 Z" fill="#f29aa0" stroke="#fbe0e2" stroke-width="5" stroke-linejoin="round"/><path d="M392,690 l14,10 M420,676 l-6,16 M410,716 l16,-6" stroke="${C_BLOOD}" stroke-width="4" stroke-linecap="round"/></g>
    <g id="blood1"></g></g>
   <g id="lface" transform="translate(420,440)"><g transform="translate(-36,0)">${oEye('ln_eL',33,C_CAV)}</g><g transform="translate(36,0)">${oEye('ln_eR',33,C_CAV)}</g>${brow('ln_bL')}${brow('ln_bR')}${mouthEl('ln_m',0,76)}</g>
   <g id="booger"><path d="M-40,-10 C-46,-40 -10,-52 12,-40 C40,-48 58,-18 44,6 C52,32 20,48 -4,36 C-32,46 -54,18 -40,-10 Z" fill="#b8ad52" ${OLW}/><path d="M-18,-18 q14,-8 26,2 M-8,14 q14,8 28,-2" fill="none" stroke="#8d8433" stroke-width="4" stroke-linecap="round"/></g>
   <g id="finger">${fingerSVG(104,900)}</g><g id="drip1"></g>
   ${card(`<circle cx="114" cy="250" r="62" fill="${C_SK}" ${OLW2}/><path d="M60,224 C60,170 168,170 168,224 C150,204 80,204 60,224 Z" fill="#3a2a22" ${OLW2}/><circle cx="92" cy="244" r="6" fill="${INK}"/><circle cx="136" cy="244" r="6" fill="${INK}"/><path d="M114,250 l-12,30 h24 Z" fill="${C_SK_S}" ${OLW2}/><path d="M96,294 q18,10 36,0" fill="none" ${OLW2}/><rect x="96" y="312" width="36" height="34" fill="${C_SK}" ${OLW2}/><path d="M50,400 C50,350 178,350 178,400 Z" fill="#7fb6e8" ${OLW2}/><circle id="ring" cx="114" cy="268" r="20" fill="none" stroke="#e02626" stroke-width="6"/><path d="M132,278 L232,400" stroke="#e02626" stroke-width="5" stroke-dasharray="10 9" stroke-linecap="round"/>`,'INSIDE THE NOSE')}`;}
// ---- scene 2: the nose from the front ----
function frontNose(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#f9e2cc"/>
   <g transform="translate(360,760) scale(1.32) translate(-360,-740)"><path d="M250,-340 C268,260 250,440 214,560 M470,-340 C452,260 470,440 506,560" fill="none" stroke="#e8c4a0" stroke-width="16" stroke-linecap="round"/>
   <path d="M214,548 C110,540 60,650 110,740 C140,800 220,810 280,780 C330,810 390,810 440,780 C500,810 580,800 610,740 C660,650 610,540 506,548 C470,470 250,470 214,548 Z" fill="#fbe8d6" ${OLW}/>
   <path d="M150,640 C130,690 150,730 190,750 M570,640 C590,690 570,730 530,750" fill="none" stroke="#e8c4a0" stroke-width="9" stroke-linecap="round"/>
   <ellipse cx="262" cy="754" rx="58" ry="17" fill="#3a1f1c" transform="rotate(8,262,754)"/><ellipse cx="458" cy="754" rx="58" ry="17" fill="#3a1f1c" transform="rotate(-8,458,754)"/>
   <path d="M330,880 C345,900 375,900 390,880" fill="none" stroke="#e8c4a0" stroke-width="8" stroke-linecap="round"/>
   <g id="drip2"></g><g id="sniff"></g>
   <g id="plug"><g id="plugB"><path d="M-46,300 L-46,10 C-46,-34 46,-34 46,10 L46,300 Z" fill="#fff" ${OLW}/><path d="M-20,20 v250 M12,10 v270" stroke="#d9dde2" stroke-width="5" stroke-linecap="round"/></g>
     <g id="plugRed"></g><g transform="translate(0,150)"><g transform="translate(-19,0)">${oEye('tp_eL',18,'#fff')}</g><g transform="translate(19,0)">${oEye('tp_eR',18,'#fff')}</g>${brow('tp_bL')}${brow('tp_bR')}${mouthEl('tp_m',0,38)}</g>
     <g transform="translate(0,270)"><g transform="translate(-58,60) rotate(-16)">${fingerSVG(60,400)}</g><g transform="translate(58,60) rotate(16)">${fingerSVG(60,400)}</g></g></g>
   <g id="wipe"><path d="M-150,40 C-160,-60 -70,-130 10,-120 C90,-150 170,-80 160,10 C190,80 120,150 40,130 C-30,170 -130,130 -150,40 Z" fill="#fff" ${OLW}/><path d="M-80,-40 q40,30 20,90 M20,-70 q30,50 0,120 M90,-30 q-10,50 -40,90" fill="none" stroke="#d9dde2" stroke-width="6" stroke-linecap="round"/><g id="wipeRed"></g>
     <g transform="translate(120,90) rotate(-30)">${fingerSVG(74,700)}</g><g transform="translate(40,130) rotate(-18)">${fingerSVG(74,700)}</g></g></g>`;}
// ---- scene 3: lean forward and pinch ----
function profile(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#d9f0fa"/>
   <g id="head"><path d="M800,-80 L430,-80 C330,40 296,200 310,340 L226,520 C214,548 236,566 268,566 L290,566 C284,600 290,624 302,644 C282,664 286,686 306,694 C296,748 314,806 384,832 L480,862 L520,1400 L800,1400 Z" fill="${C_SK}" ${OLW}/>
    <path d="M800,-80 L430,-80 C380,-20 350,60 336,140 C420,60 560,40 660,120 C700,240 700,380 800,470 Z" fill="#2c211c" ${OLW}/>
    <path d="M356,352 q34,22 70,2" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/><path d="M340,292 q44,-30 100,-8" fill="none" stroke="#2c211c" stroke-width="13" stroke-linecap="round"/>
    <path d="M610,420 C650,400 680,440 660,490 C650,520 620,530 604,510" fill="${C_SK}" ${OLW}/><path d="M306,694 q26,-6 50,2" fill="none" ${OLW2}/>
    <path id="pblood" d="M276,566 C262,600 262,640 280,648 C298,640 298,600 284,566 Z" fill="${C_BLOOD}" ${OLW2}/>
    <g id="phand"><path d="M-760,-40 C-560,-120 -330,-60 -250,60 C-210,150 -260,260 -380,300 C-520,340 -700,300 -760,260 Z" fill="${C_SK}" ${OLW}/><path d="M-330,60 q30,60 -10,120 M-420,40 q24,70 -16,140" fill="none" stroke="${C_SK_S}" stroke-width="7" stroke-linecap="round"/><g transform="rotate(72)">${fingerSVG(66,700)}</g><g transform="translate(14,84) rotate(108)">${fingerSVG(70,700)}</g></g></g>
   <g id="clock" opacity="0"><circle r="74" fill="#fff" ${OLW}/><circle r="60" fill="#fff8e0" ${OLW2}/><path id="clockH" d="M0,0 V-46" stroke="${INK}" stroke-width="8" stroke-linecap="round"/><path d="M0,0 L24,14" stroke="${INK}" stroke-width="8" stroke-linecap="round"/><circle r="7" fill="${INK}"/></g>`;}
// ---- scene 5: the clinic ----
function clinic19(){const row=(id,y,col,txt)=>`<g id="${id}" opacity="0"><rect x="64" y="${y}" width="592" height="78" rx="16" fill="${col}" stroke="#1d2a44" stroke-width="4"/><text x="360" y="${y+52}" text-anchor="middle" style="font-family:LG,sans-serif;font-size:33px;letter-spacing:.5px" fill="#fff">${txt}</text></g>`;
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#dcefe9"/>
   <g id="brd"><rect x="38" y="42" width="660" height="494" rx="24" fill="#000" opacity=".12"/><rect x="30" y="32" width="660" height="494" rx="24" fill="#fff" stroke="#1d2a44" stroke-width="5"/>
   <text x="360" y="108" text-anchor="middle" style="font-family:LG,sans-serif;font-size:58px;letter-spacing:2px" fill="#1d2a44">NOSEBLEED?</text>
   ${row('b0',136,'#e8473f','PICKING SCRATCHES THE INSIDE')}${row('b1',230,'#2f8fe0','1. LEAN FORWARD')}${row('b2',324,'#14a3a0','2. PINCH THE SOFT PART')}${row('b3',418,'#2fae62','3. HOLD FOR 10-15 MINUTES')}</g>
   <g transform="translate(190,660) scale(1.5)">${doctorSVG()}</g><g id="patWrap"><g transform="translate(565,790) scale(1.6)">${patientSVG()}</g>
    <g id="ptis" transform="translate(408,1040)"><path d="M-50,10 C-60,-30 -20,-56 10,-46 C44,-58 70,-20 56,12 C66,44 30,62 0,50 C-30,64 -58,40 -50,10 Z" fill="#fff" ${OLW}/><path d="M-20,-20 C0,-34 26,-20 20,4 C30,22 6,34 -8,22 C-26,24 -32,-2 -20,-20 Z" fill="${C_BLOOD}"/><circle cx="30" cy="28" r="9" fill="${C_BLOOD}"/><circle cx="-34" cy="24" r="6" fill="${C_BLOOD}"/></g></g>`;}

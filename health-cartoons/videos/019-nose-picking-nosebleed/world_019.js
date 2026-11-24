// =============== 019: how picking your nose makes it bleed. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f9e6cf', C_SK_S='#e6c9a6', C_CAV='#a8323c', C_CAV_S='#7c1f2a', C_BLOOD='#e02634', C_TEAL='#14a3a0';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const CAV_D='M566,236 C622,236 650,320 654,430 L660,716 C660,790 606,812 520,804 L176,792 C96,786 84,716 150,646 C284,494 440,324 506,262 C524,244 544,236 566,236 Z';
const fingerSVG=(w,len)=>`<path d="M${-w/2},${len} L${-w/2},${w*.5} C${-w/2},${-w*.2} ${w/2},${-w*.2} ${w/2},${w*.5} L${w/2},${len} Z" fill="${C_SK}" ${OLW}/><path d="M${-w*.3},${w*.5} C${-w*.3},${w*.1} ${w*.3},${w*.1} ${w*.3},${w*.5} L${w*.3},${w*.95} L${-w*.3},${w*.95} Z" fill="#fde9da" ${OLW2}/><path d="M${-w*.3},${w*1.9} h${w*.6} M${-w*.26},${w*2.1} h${w*.52}" stroke="${C_SK_S}" stroke-width="4" stroke-linecap="round"/>`;
const card=(inner,txt)=>`<g id="inset"><rect x="16" y="130" width="196" height="330" rx="18" fill="#fff" ${OLW}/>${inner}<text x="114" y="440" text-anchor="middle" style="font-family:LG,sans-serif;font-size:20px" fill="#1d2a44">${txt}</text></g>`;
// ---- scene 1: inside the nose, seen from the side (the reference's staging) ----
function insideNose(){
  DEFS+=`<clipPath id="cavC"><path d="${CAV_D}"/></clipPath>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#ddf3fb"/>
   <path d="M520,-40 C440,200 240,520 56,700 C-20,776 -6,890 110,940 C230,990 400,1010 470,1000 C430,1060 400,1160 440,1330 L770,1330 L770,-40 Z" fill="${C_SK}" ${OLW}/>
   <path d="M664,600 C724,700 716,880 600,960 C560,988 520,1000 470,1000" fill="none" ${OLW}/>
   <path d="M150,930 C260,975 380,985 470,975" fill="none" stroke="#fff" stroke-width="14" stroke-linecap="round" opacity=".7"/>
   <path d="${CAV_D}" fill="${C_CAV}" ${OLW}/>
   <g clip-path="url(#cavC)"><path d="M130,690 C270,520 430,350 520,262" fill="none" stroke="#f0cdb0" stroke-width="30" stroke-linecap="round"/><path d="M176,700 C300,550 450,390 536,300" fill="none" stroke="${C_CAV_S}" stroke-width="16" stroke-linecap="round" opacity=".55"/>
    <path d="M230,640 q40,-30 60,-70 q30,10 20,40 q-30,40 -80,60 Z" fill="#b59a5a" opacity=".9"/>
    <path d="M440,560 l16,-14 l12,12 l-8,18 l-16,2 Z" fill="#a9ad5c"/>
    <g id="scratch" opacity="0"><path d="M372,664 l22,-18 l14,16 l24,-14 l16,22 l-10,26 l14,24 l-22,18 l-20,-10 l-24,16 l-14,-24 l-18,-8 l10,-26 Z" fill="#8e1420"/><path d="M392,690 l14,10 M420,676 l-6,16 M410,716 l16,-6" stroke="#5f0c16" stroke-width="5" stroke-linecap="round"/></g>
    <g id="blood1"></g></g>
   <g transform="rotate(12,372,924)"><ellipse cx="372" cy="924" rx="176" ry="58" fill="${C_CAV_S}" ${OLW}/><ellipse cx="372" cy="930" rx="150" ry="42" fill="${C_CAV}"/></g>
   <g id="blood1b"></g>
   <g id="lface" transform="translate(548,420)"><g transform="translate(-36,0)">${oEye('ln_eL',33,C_CAV)}</g><g transform="translate(36,0)">${oEye('ln_eR',33,C_CAV)}</g>${brow('ln_bL')}${brow('ln_bR')}${mouthEl('ln_m',0,70)}</g>
   <g id="booger"><path d="M-46,-6 l14,-34 l30,-12 l34,10 l22,30 l-8,36 l-30,22 l-36,-2 l-24,-22 Z" fill="#a9ad5c" ${OLW2}/><path d="M-18,-18 l20,-8 l18,12 M-12,14 l22,6 l16,-14" fill="none" stroke="#868a3c" stroke-width="4" stroke-linecap="round"/></g>
   <g id="finger">${fingerSVG(128,1100)}</g><g id="drip1"></g>`;}
// ---- scene 2: the nose from the front ----
function frontNose(){
  const handL=`<path d="M-360,640 C-350,360 -280,80 -196,-30 C-170,-64 -122,-44 -132,0 C-156,100 -176,240 -160,640 Z" fill="${C_SK}" ${OLW}/><path d="M-178,-14 C-166,-34 -142,-26 -146,-4 L-156,40 L-190,30 Z" fill="#fdf1e2" ${OLW2}/><path d="M-250,140 q40,10 70,-6 M-262,200 q40,10 74,-4" fill="none" stroke="${C_SK_S}" stroke-width="5" stroke-linecap="round"/>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#f9e6cf"/>
   <g transform="translate(360,650) scale(1.1) translate(-360,-660)"><path d="M262,-340 C286,200 262,420 214,560 M458,-340 C434,200 458,420 506,560" fill="none" stroke="#ecd3b2" stroke-width="20" stroke-linecap="round"/>
   <path d="M214,548 C110,540 60,650 110,740 C140,800 220,810 280,780 C330,810 390,810 440,780 C500,810 580,800 610,740 C660,650 610,540 506,548 C470,470 250,470 214,548 Z" fill="#fbecd9" ${OLW}/>
   <path d="M150,640 C130,690 150,730 190,750 M570,640 C590,690 570,730 530,750" fill="none" stroke="#ecd3b2" stroke-width="9" stroke-linecap="round"/>
   <path d="M204,752 C230,728 300,736 322,760 C290,776 232,772 204,752 Z" fill="#2a1a16"/><path d="M516,752 C490,728 420,736 398,760 C430,776 488,772 516,752 Z" fill="#2a1a16"/>
   <g id="drip2"></g><g id="sniff"></g>
   <g id="plug"><path d="M-150,470 C-170,300 -120,150 -50,70 C-26,40 14,50 16,90 L20,170 C60,90 96,50 130,60 C166,74 164,116 144,160 C120,240 150,330 150,470 Z" fill="${C_SK}" ${OLW}/><path d="M20,170 C10,230 -10,270 -40,300 M-60,90 q20,-10 40,0" fill="none" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>
     <path d="M-44,20 C-56,-14 -30,-44 0,-40 C22,-58 56,-40 54,-12 C74,6 62,40 36,44 C22,62 -10,62 -22,44 C-44,48 -56,34 -44,20 Z" fill="#fff" ${OLW2}/><g id="plugRed"></g>
     <g transform="translate(40,-40) scale(1.6)"><g transform="translate(-17,0)">${oEye('tp_eL',18,'#fff')}</g><g transform="translate(17,0)">${oEye('tp_eR',18,'#fff')}</g>${brow('tp_bL')}${brow('tp_bR')}${mouthEl('tp_m',-2,30)}</g></g>
   <g id="wipe"><path d="M-190,-40 C-150,-120 -60,-80 0,-120 C60,-80 150,-120 190,-40 L250,640 L-250,640 Z" fill="#fff" ${OLW}/><path d="M-90,-40 q30,200 -20,660 M10,-80 q30,300 10,700 M100,-40 q-10,240 40,660" fill="none" stroke="#dfe3e8" stroke-width="7" stroke-linecap="round"/><g id="wipeRed"></g>
     ${handL}<g transform="scale(-1,1)">${handL}</g></g></g>`;}
// ---- scene 3: lean forward and pinch (close on the nose and mouth) ----
function profile(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#ddf3fb"/>
   <g id="head"><path d="M1300,-300 L560,-300 L540,-80 C520,60 486,200 446,300 L282,452 C250,482 262,520 308,524 L352,528 C340,580 330,604 352,630 C328,656 336,682 362,690 C350,740 362,800 424,850 C510,920 566,1020 586,1700 L1300,1700 Z" fill="${C_SK}" ${OLW}/>
    <path d="M430,178 q80,-56 170,-8" fill="none" stroke="#1c1512" stroke-width="26" stroke-linecap="round"/><path d="M456,262 q46,30 100,2" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>
    <path d="M372,452 q44,-34 66,22" fill="none" ${OLW}/><path d="M362,690 q34,-10 70,8" fill="none" ${OLW2}/>
    <path id="pblood" d="M300,522 C296,560 306,590 322,612 C330,630 350,628 352,606 C360,580 356,550 350,526 Z" fill="#e5484d"/>
    <g id="phand"><g transform="translate(150,-30)"><path d="M-640,-430 C-430,-480 -230,-390 -196,-250 C-176,-130 -200,60 -264,200 C-330,330 -520,360 -680,300 Z" fill="${C_SK}" ${OLW}/><path d="M-330,-200 q40,60 20,130 M-360,-60 q44,50 30,120 M-400,70 q40,40 30,100" fill="none" stroke="${INK}" stroke-width="3" stroke-linecap="round"/></g><g transform="translate(6,-44) rotate(118)">${fingerSVG(74,300)}</g><g transform="translate(10,50) rotate(64)">${fingerSVG(82,300)}</g></g></g>`;}
// ---- scene 5: the clinic (the reference's two-shot: desk, doctor, patient holding the stained tissue) ----
function clinic19(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#b9c58c"/><rect x="-60" y="180" width="840" height="56" fill="#a4996c"/>
   <path d="M-60,900 H780 V1400 H-60 Z" fill="#9a8f80"/><path d="M-60,900 H780 M-60,1030 H780 M-60,1190 H780 M120,900 L40,1340 M330,900 L300,1340 M520,900 L560,1340 M690,900 L780,1300" stroke="#6f665b" stroke-width="3" fill="none"/>
   <g transform="translate(170,430) scale(1.25)">${doctorSVG()}</g>
   <path d="M-60,760 H350 V800 H-60 Z" fill="#b89a86" ${OLW}/><path d="M160,800 H330 V1180 H160 Z" fill="#b39581" ${OLW}/><path d="M-60,800 H160" ${OLW}/>
   <g id="patWrap"><path d="M470,900 L462,1180 L530,1180 L548,960 L566,1180 L636,1180 L630,900 Z" fill="#2b2b30" ${OLW}/><path d="M446,1180 q40,-26 90,0 v22 h-90 Z M560,1180 q44,-26 90,0 v22 h-90 Z" fill="#17171a" ${OLW2}/>
    <g transform="translate(548,500) scale(1.25)">${patientSVG()}</g>
    <g id="ptis" transform="translate(372,700)"><path d="M0,0 C-34,30 -56,100 -44,170 l20,-24 l12,36 l22,-30 l14,30 l16,-34 l18,20 C70,110 40,36 0,0 Z" fill="#fff" ${OLW}/><path d="M-10,60 C6,50 22,70 14,96 C24,120 0,140 -12,120 C-28,104 -24,74 -10,60 Z" fill="#e5484d"/><ellipse cx="24" cy="130" rx="9" ry="16" fill="#e5484d"/><ellipse cx="-26" cy="140" rx="6" ry="12" fill="#ef8a8d"/></g></g>`;}

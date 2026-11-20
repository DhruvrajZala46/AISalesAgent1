// =============== SCENE 1 : head cross-section (one locked wide shot) ===============
// Face looks LEFT. Brain on top, nose passage, hard palate, mouth + tongue, soft palate (hero), throat, spine on the right.
const FLESH='#e3807f', FLESH_S='#c9615f', LUMEN='#f7b5ae', LUMEN_S='#ea9590', SKIN2='#f2c6a8', BONEY='#f5e3a3', BONEY_D='#e9b85e';
const PAL='#ef9097', PAL_S='#d36e78', NOOD='#f6d27a', NOOD_S='#d9a948';
function boneDots(pts){return pts.map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${BONEY_D}" opacity=".8"/>`).join('');}
function vertebra(y){return `<g transform="translate(0,${y})"><path d="M614,0 C640,-6 700,-6 740,0 L740,70 C700,76 640,76 614,70 C606,48 606,22 614,0 Z" fill="${BONEY}" ${LN}/>
 ${boneDots([[640,18,4],[668,40,3],[700,22,4],[652,52,3],[716,50,3],[690,10,2.5]])}
 <path d="M612,74 C640,82 700,82 740,76 L740,88 C700,92 640,92 612,86 Z" fill="#f8efe1" ${LN2}/></g>`;}
const LUMEN_D='M52,488 C70,444 96,400 130,372 C200,330 330,322 450,326 C520,330 572,350 588,400 L590,960 C588,1000 586,1100 586,1290 L500,1290 C500,1100 498,1010 492,980 C484,962 472,956 462,962 L462,1290 L394,1290 L394,962 C394,936 404,910 418,894 C436,868 450,820 458,780 C466,736 472,712 470,690 C452,620 380,582 290,580 C210,580 140,594 94,602 L80,606 L80,596 L98,566 C140,522 200,508 260,506 C320,505 370,506 400,508 L402,472 C330,466 220,466 140,472 C100,476 72,484 52,488 Z';
const PROFILE='M150,-20 C128,110 116,220 104,296 C100,320 88,342 78,362 C62,394 36,428 24,454 C18,470 30,482 52,486 C64,488 72,494 76,504 C80,524 72,546 68,560 C62,576 68,590 80,598 C68,606 60,620 64,636 C68,660 84,672 86,690 C92,722 78,760 82,790 C90,822 142,842 222,852 C292,860 342,882 354,942 L362,1300 L740,1300 L740,-20 Z';
function brainD(sc,off){const cx=420,cy=150,pts=[];for(let i=0;i<72;i++){const a=i/72*Math.PI*2;let r=1+.035*Math.sin(a*11)+.02*Math.sin(a*5+1);
  let x=cx+Math.cos(a)*(222*sc+off)*r, y=cy+Math.sin(a)*(128*sc+off)*r; if(y>cy+100*sc+off) y=cy+100*sc+off+(y-cy-100*sc-off)*.25; pts.push([x,y]);}return smooth(pts,true);}
function gyri(){let h='';const R=(i)=>{const v=Math.sin(i*12.9898)*43758.5453;return v-Math.floor(v);};
  [44,92,140,188,232].forEach((y0,r)=>{const pts=[];for(let x=196;x<=650;x+=18){pts.push([x,y0+Math.sin(x/26+r*1.7)*13+Math.sin(x/9+r)*3]);}
   h+=`<path d="${smooth(pts)}" fill="none" stroke="#c96f84" stroke-width="3.4" stroke-linecap="round" ${VE}/>`;
   for(let k=0;k<4;k++){const x=230+R(r*9+k)*380,y=y0+8;h+=`<path d="M${x.toFixed(0)},${y} c${(R(k+r)*16-8).toFixed(0)},14 ${(R(k*2+r)*20-10).toFixed(0)},26 ${(R(k*3+r)*16-8).toFixed(0)},38" fill="none" stroke="#c96f84" stroke-width="3" stroke-linecap="round" ${VE}/>`;}});
  return h;}
let W=`<g id="world">
 <rect x="-200" y="-200" width="1120" height="1680" fill="#fbf0e2"/>
 <!-- body: skin band + cut flesh -->
 <path d="${PROFILE}" fill="${FLESH}" stroke="${SKIN2}" stroke-width="22" stroke-linejoin="round"/>
 <path d="${PROFILE}" fill="none" ${LN}/>
 <path d="M150,-20 C128,110 116,220 104,296" fill="none" stroke="#e3b28f" stroke-width="3" ${VE}/>
 <!-- skull + brain -->
 <path d="${brainD(1.13,14)}" fill="${BONEY}" ${LN}/>${boneDots([[236,70,4],[300,26,3],[420,8,4],[560,30,3],[640,96,4],[230,200,3],[660,200,3]])}
 <path d="M150,250 C210,300 300,306 420,308 C520,310 600,300 664,262 L670,320 C600,330 520,330 420,330 C300,330 220,322 150,300 Z" fill="${BONEY}" ${LN}/>
 <g id="brainG"><clipPath id="brainClip"><path d="${brainD(1,0)}"/></clipPath>
  <path d="${brainD(1,0)}" fill="#f4a8b6" ${LN}/>
  <g clip-path="url(#brainClip)"><path d="${brainD(1,0)}" fill="none" stroke="#da8396" stroke-width="22" opacity=".55" filter="url(#soft3)"/>${gyri()}
   <path d="M560,236 C600,228 640,240 652,262 C640,286 590,292 560,282 Z" fill="#e991a3" ${LN2}/><path d="M568,252 h76 M566,266 h80" ${TH('#c96f84')} stroke-width="2.5"/></g>
  <g id="brainFace">
   <g transform="translate(386,176)">${oEye('bEyeL',36,'#f4a8b6')}</g><g transform="translate(462,170)">${oEye('bEyeR',36,'#f4a8b6')}</g>
   ${brow('bBrowL')}${brow('bBrowR')}
   ${mouthEl('brain_m',424,236)}
  </g>
  <g id="brainArm"><path id="bArmO" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="bArmI" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
   <g id="phone"><g transform="scale(1.45)"><path d="M-30,-34 C-40,-30 -42,-14 -34,-8 L-24,-2 C-18,4 -12,0 -10,-6 L-6,-14 C-2,-22 -8,-28 -14,-30 Z" fill="#e2474b" ${LN2}/>
     <path d="M14,24 C24,30 40,26 44,16 L46,4 C46,-4 38,-6 32,-2 L22,4 C16,8 14,16 14,24 Z" fill="#e2474b" ${LN2}/><path d="M-30,-14 C-14,8 8,20 30,6" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round"/><path d="M-30,-14 C-14,8 8,20 30,6" fill="none" stroke="#e2474b" stroke-width="8" stroke-linecap="round"/></g></g>
   <g id="ring" opacity="0">${[0,1,2].map(i=>`<path d="M${640+i*16},${130-i*12} q${18+i*6},${24+i*6} 0,${52+i*16} M${560-i*16},${130-i*12} q${-18-i*6},${24+i*6} 0,${52+i*16}" fill="none" stroke="#ffd21f" stroke-width="6" stroke-linecap="round"/>`).join('')}</g>
   <g id="bHand"></g></g>
 </g>
 <!-- air spaces (nose, mouth, throat) -->
 ${shaded(LUMEN_D,LUMEN,LUMEN_S,22)}
 <!-- turbinates (soft shelves in the nose) -->
 ${[[200,350,250,16],[230,392,230,15],[260,432,180,13]].map(([x,y,w,h])=>`<path d="M${x},${y} C${x+w*.3},${y-h} ${x+w*.75},${y-h*.6} ${x+w},${y-h*.2} C${x+w*.8},${y+h*.6} ${x+w*.3},${y+h*.7} ${x},${y} Z" fill="#f1a7a3" stroke="#e08f8c" stroke-width="2" ${VE}/>`).join('')}
 <!-- nostril glow (daylight) -->
 <ellipse id="glow" cx="40" cy="494" rx="70" ry="60" fill="#fffbe0" opacity="0" filter="url(#soft2)"/>
 <!-- hard palate (bone between nose and mouth) -->
 <path d="M112,474 C200,466 320,466 402,470 L400,508 C330,505 220,506 140,520 C122,524 110,510 112,474 Z" fill="${BONEY}" ${LN}/>${boneDots([[170,484,3.5],[240,490,3],[310,486,3.5],[370,490,3]])}
 <!-- teeth -->
 <path d="M96,514 C112,512 120,520 118,540 L112,572 C108,580 98,580 96,572 C92,552 90,530 96,514 Z" fill="#fbfaf4" ${LN2}/>
 <path d="M98,612 C110,606 120,612 120,628 L118,660 C110,668 100,666 96,656 C92,640 92,622 98,612 Z" fill="#fbfaf4" ${LN2}/>
 <!-- chin bone + hyoid -->
 <path d="M104,672 C130,660 160,668 168,700 C176,740 166,790 140,808 C118,820 100,806 98,780 C94,740 92,700 104,672 Z" fill="${BONEY}" ${LN}/>${boneDots([[124,700,3],[140,750,3.5],[124,786,3]])}
 <ellipse cx="392" cy="868" rx="22" ry="12" fill="${BONEY}" ${LN2}/>
 <!-- tongue -->
 ${shaded('M100,606 C140,592 220,578 300,580 C380,584 452,620 470,690 C474,740 466,800 446,860 C400,840 330,800 260,780 C200,764 160,740 132,700 C118,676 104,640 100,606 Z','#e45f6d','#c94656',14)}
 <path d="M150,600 C230,592 330,596 420,640" fill="none" stroke="#f08893" stroke-width="5" stroke-linecap="round" opacity=".8"/>
 <!-- epiglottis, windpipe, food pipe -->
 <path d="M420,894 C430,866 444,836 452,800 C458,784 470,786 468,804 C462,840 448,872 432,900 Z" fill="#ef9a9c" ${LN2}/>
 ${[1000,1046,1092,1138,1184,1230].map(y=>`<path d="M396,${y} C416,${y+8} 442,${y+8} 460,${y}" fill="none" stroke="#f9ddd6" stroke-width="9" stroke-linecap="round"/>`).join('')}
 <!-- spine -->
 ${[300,392,484,576,668,760,852,944,1036,1128,1220].map(vertebra).join('')}
 <!-- nose hairs at the nostril -->
 <g id="hairs">${[[60,470,-40],[70,452,-30],[84,436,-20],[98,420,-10],[112,404,0],[74,486,20],[90,478,30],[106,470,35],[120,462,40],[136,456,45]].map(([x,y,a],i)=>`<path id="hair${i}" d="M${x},${y} q${Math.cos((a-90)*Math.PI/180)*14},${Math.sin((a-90)*Math.PI/180)*14} ${Math.cos((a-60)*Math.PI/180)*26},${Math.sin((a-60)*Math.PI/180)*26}" fill="none" stroke="#3b2522" stroke-width="2.6" stroke-linecap="round"/>`).join('')}</g>
 <!-- teaching arrows -->
 <g id="arDown" opacity="0"><path d="M548,600 L548,700 L530,700 L560,746 L590,700 L572,700 L572,600 Z" fill="#ffd21f" ${LN}/></g>
 <g id="arUpX" opacity="0"><path d="M520,320 L520,250 L504,250 L530,214 L556,250 L540,250 L540,320 Z" fill="#ffd21f" ${LN2} transform="translate(0,40)"/><circle cx="530" cy="296" r="24" fill="#e0454f" ${LN2}/><path d="M520,286 L540,306 M540,286 L520,306" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>
 <!-- noodle -->
 <g id="noodleG"><path id="ndO" fill="none" stroke="${INK}" stroke-width="33" stroke-linecap="round" stroke-linejoin="round"/>
  <path id="ndF" fill="none" stroke="${NOOD}" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
  <path id="ndS" fill="none" stroke="${NOOD_S}" stroke-width="5" stroke-linecap="round" opacity=".7"/>
  <path id="ndH" fill="none" stroke="#fff4c6" stroke-width="4" stroke-linecap="round" opacity=".9"/>
  <g id="ndFace"><g id="ndEyes"><g transform="translate(-17,-14)">${oEye('nEyeL',19,NOOD)}</g><g transform="translate(17,-14)">${oEye('nEyeR',19,NOOD)}</g>${brow('nBrowL')}${brow('nBrowR')}</g>
   ${mouthEl('noodle_m',0,12)}</g>
  <g id="speed" opacity="0"></g></g>
 <!-- air from the lungs -->
 <g id="air"></g>
 <g id="has"></g>
 <!-- soft palate (hero) -->
 <g id="palG"><g id="palBody">${shaded('M0,-36 C60,-46 130,-40 172,-20 C188,-12 196,6 190,18 C202,36 198,62 182,64 C166,66 158,48 166,32 C130,38 60,44 0,36 Z',PAL,PAL_S,14)}
   <path d="M30,-10 C70,-16 120,-14 150,-4" fill="none" stroke="#f7b3b8" stroke-width="4" stroke-linecap="round"/></g>
 <g id="palArms"><path id="paAO" fill="none" stroke="${INK}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/><path id="paAI" fill="none" stroke="#fff" stroke-width="6.5" stroke-linecap="round" stroke-linejoin="round"/><g id="paHands"></g></g>
  <g id="palFace"><g transform="translate(-28,0)">${oEye('pEyeL2',32,PAL)}</g><g transform="translate(30,-3)">${oEye('pEyeR2',32,PAL)}</g>${brow('paBrowL')}${brow('paBrowR')}${mouthEl('palate_m',2,42)}</g>
 </g>
 <g id="ticks" opacity="0">${[0,1,2,3].map(i=>`<path d="M${600+i*0},${380+i*24} l26,${-6+i*4}" stroke="#ffd21f" stroke-width="5" stroke-linecap="round"/>`).join('')}</g>
 <g id="sweat" opacity="0"><path d="M0,-14 C6,-4 10,4 8,10 C6,16 -6,16 -8,10 C-10,4 -6,-4 0,-14 Z" fill="#8fd3f4" ${LN2} transform="translate(-48,-30)"/><path d="M0,-14 C6,-4 10,4 8,10 C6,16 -6,16 -8,10 C-10,4 -6,-4 0,-14 Z" fill="#8fd3f4" ${LN2} transform="translate(52,-40) scale(.8)"/></g>
 <!-- thought bubble: what happens "in public" -->
 <g id="pubBub" opacity="0"><g transform="translate(300,190)">
  <ellipse rx="210" ry="140" fill="#fff" ${LN}/><circle cx="150" cy="168" r="20" fill="#fff" ${LN2}/><circle cx="178" cy="206" r="12" fill="#fff" ${LN2}/>
  <clipPath id="pubClip"><ellipse rx="200" ry="130"/></clipPath>
  <g clip-path="url(#pubClip)"><rect x="-210" y="-140" width="420" height="280" fill="#fdf1d6"/><rect x="-210" y="40" width="420" height="120" fill="#c98a55"/><path d="M-210,40 h420" ${LN2}/>
   <g transform="translate(-30,-10)"><path d="M-40,60 C-60,20 -56,-40 -20,-62 C10,-80 52,-70 66,-40 C74,-24 72,-8 66,4 C76,12 84,22 80,30 C74,36 66,36 62,40 C60,52 54,64 40,70 C10,84 -26,80 -40,60 Z" fill="${SKIN2}" ${LN}/>
     <path d="M-24,-60 C-10,-90 40,-92 62,-58 C40,-66 10,-64 -6,-50 C-14,-40 -22,-44 -24,-60 Z" fill="#2b2430" ${LN2}/><path d="M-30,-56 C-48,-40 -54,-10 -48,18 C-40,0 -30,-20 -28,-40 Z" fill="#2b2430" ${LN2}/>
     <ellipse cx="34" cy="-22" rx="6" ry="8" fill="#1b1717"/><path d="M24,-36 l18,-4" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>
     <path d="M44,48 q8,6 18,0" fill="none" ${LN2}/><circle cx="20" cy="18" r="10" fill="#f3a3a0" opacity=".7"/>
     <path id="pubNoodle" d="M72,30 C80,44 70,58 78,72 C84,84 76,96 82,110" fill="none" stroke="${INK}" stroke-width="11" stroke-linecap="round"/><path d="M72,30 C80,44 70,58 78,72 C84,84 76,96 82,110" fill="none" stroke="${NOOD}" stroke-width="7" stroke-linecap="round"/></g>
   <path d="M60,70 C60,110 150,110 150,70 Z" fill="#fff" ${LN2}/><path d="M64,70 h82" ${LN2}/>
   <text id="ha1" class="cap" x="-150" y="-70" style="font-size:40px" opacity="0" transform="rotate(-12,-150,-70)">HA HA!</text>
   <text id="ha2" class="cap" x="96" y="-60" style="font-size:40px" opacity="0" transform="rotate(10,96,-60)">LOL!</text></g>
  <ellipse rx="210" ry="140" fill="none" ${LN}/></g></g>
</g>`;
let S1=`<g id="s1"><g id="cam">${W}</g>
 ${labelBox('lbPal','SOFT PALATE',500,560,22)}${labelBox('lbNose','NOSE',300,402,24)}${labelBox('lbBrain','BRAIN',300,40,24)}</g>`;

// =============== 009 worlds: ALL code, our 001 / 003-v1 style (thin INK lines, shaded(), the 003 v1 throat colours) ===============
const FLESH='#e3807f', FLESH_S='#c9615f', LUMEN='#f39c97', LUMEN_S='#e07f7c', BONEY='#f5e3a3', BONEY_D='#e9b85e';
const EPI='#f2a3a8', EPI_S='#d8808a', TRA='#f6b8b6', TRA_S='#e3938f', ESO='#d86a70', ESO_S='#b9505a', TONGUE='#c9545d', TONGUE_S='#a8404b';
function hose(id){return `<g id="${id}"><path id="${id}_o" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="${id}_i" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"/><g id="${id}_h"></g></g>`;}
function setHose(id,pts,rot,s=1){const d=smooth(pts);$(id+'_o').setAttribute('d',d);$(id+'_i').setAttribute('d',d);const e=pts[pts.length-1];$(id+'_h').innerHTML=glove(e[0],e[1],rot,s);}
function boneDots(pts){return pts.map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${BONEY_D}" opacity=".8"/>`).join('');}
function vertebra(y){return `<g transform="translate(0,${y})"><path d="M590,0 C620,-6 700,-6 760,0 L760,96 C700,102 620,102 590,96 C580,66 580,30 590,0 Z" fill="${BONEY}" ${LN}/>
 ${boneDots([[620,24,5],[652,58,4],[690,28,5],[636,80,4],[712,70,4],[676,14,3]])}
 <path d="M588,100 C620,110 700,110 760,104 L760,122 C700,128 620,128 588,120 Z" fill="#f8efe1" ${LN2}/></g>`;}
// spicy chicken chunk (red-orange, chili flakes)
function foodSVG(id,s=1){return `<g id="${id}"><g transform="scale(${s})"><path d="M-30,-40 C-6,-52 24,-44 34,-20 C44,6 36,34 14,44 C-8,54 -34,42 -40,18 C-46,-6 -46,-30 -30,-40Z" fill="#c9622f" ${LN}/>
  <path d="M-30,-40 C-6,-52 24,-44 34,-20 C26,-30 4,-36 -12,-32 C-26,-28 -34,-18 -36,-6 C-42,-18 -40,-32 -30,-40Z" fill="#9c3f1c" opacity=".8"/>
  ${[[-14,-10],[10,4],[-20,18],[18,-22],[4,26]].map(([x,y])=>`<path d="M${x},${y} l7,-3" stroke="#e0262c" stroke-width="4" stroke-linecap="round"/>`).join('')}
  <path d="M-22,-30 C-12,-36 4,-36 12,-32" fill="none" stroke="#f3a26e" stroke-width="4" stroke-linecap="round"/></g></g>`;}

// ---------------- SCENE A: close-up of the throat (face to the left, spine to the right) ----------------
function throatWorld(){
  DEFS+=`<clipPath id="traClip"><path d="M150,760 C190,744 300,744 336,760 L336,1400 L150,1400Z"/></clipPath><clipPath id="esoClip"><path d="M372,700 L470,700 L470,1400 L372,1400Z"/></clipPath>`;
  let s=`<g id="wThroat"><rect x="-200" y="-200" width="1120" height="1680" fill="${LUMEN}"/>
   <path d="M-200,-200 H920 V1480 H-200Z M40,-40 C200,-80 520,-80 680,-40 L680,1320 L40,1320Z" fill="${LUMEN_S}" opacity=".5" filter="url(#soft)"/>`;
  // spine + the back wall of the throat
  s+=[-60,62,184,306,428,550,672,794,916,1038,1160,1282].map(vertebra).join('');
  s+=shaded('M500,-200 C520,200 520,700 500,1480 L590,1480 L590,-200Z',FLESH,FLESH_S,14);
  s+=`<path d="M512,-100 C530,300 530,800 512,1400" fill="none" stroke="#f3a09d" stroke-width="6" stroke-linecap="round" opacity=".7"/>`;
  // food pipe (behind the windpipe)
  s+=shaded('M360,700 C360,690 482,690 484,700 L484,1480 L360,1480Z',ESO,ESO_S,16);
  s+=`<path d="M422,712 C418,900 426,1100 420,1480" fill="none" stroke="#f6a7ab" stroke-width="18" stroke-linecap="round"/><path d="M422,712 C418,900 426,1100 420,1480" fill="none" ${TH('#c4586a')} stroke-width="2.4"/>`;
  // tongue base / front tissue (top left) and the front of the neck (left edge)
  s+=shaded('M-200,-200 L300,-200 C310,40 300,240 250,380 C220,460 170,520 100,560 L-200,620Z',TONGUE,TONGUE_S,18);
  s+=`<path d="M60,-40 C140,60 200,200 210,330" fill="none" stroke="#e07b84" stroke-width="7" stroke-linecap="round" opacity=".7"/>`;
  s+=shaded('M-200,560 C40,560 120,600 150,700 L150,1480 L-200,1480Z','#f1c9b0','#dca98c',16);
  s+=`<path d="M-40,760 C40,780 100,820 140,880" ${TH('#d6a587')} stroke-width="3"/><path d="M-60,1040 C20,1060 90,1100 140,1150" ${TH('#d6a587')} stroke-width="3"/>`;
  // windpipe (front), cartilage rings, the trachea's face
  s+=`<g id="tra">${shaded('M150,760 C190,744 300,744 336,760 L336,1480 L150,1480Z',TRA,TRA_S,18)}
   <g clip-path="url(#traClip)">${[800,880,1060,1140,1220,1300].map(y=>`<path d="M150,${y} C200,${y+16} 290,${y+16} 336,${y}" fill="none" stroke="#fbe0da" stroke-width="12" stroke-linecap="round"/><path d="M150,${y+7} C200,${y+23} 290,${y+23} 336,${y+7}" ${TH('#e2a19b')} stroke-width="2"/>`).join('')}
    <ellipse cx="243" cy="762" rx="88" ry="16" fill="#8e2a35" opacity=".85"/></g>
   <g id="traFace"><g transform="translate(212,960)">${oEye('tEyeL',30,TRA)}</g><g transform="translate(276,960)">${oEye('tEyeR',30,TRA)}</g>
    <g id="redEyes" opacity="0"><circle cx="212" cy="960" r="27" fill="#e2323c"/><circle cx="276" cy="960" r="27" fill="#e2323c"/>
     <path d="M196,948 l12,8 M222,946 l-8,12 M262,948 l10,8 M290,950 l-10,8" stroke="#a51d27" stroke-width="2.5" stroke-linecap="round"/>
     <circle cx="212" cy="962" r="11" fill="#1b1717"/><circle cx="276" cy="962" r="11" fill="#1b1717"/><circle cx="208" cy="957" r="4" fill="#fff"/><circle cx="272" cy="957" r="4" fill="#fff"/>
     <circle cx="212" cy="960" r="27" fill="none" ${LN2}/><circle cx="276" cy="960" r="27" fill="none" ${LN2}/></g>
    ${brow('tBrowL')}${brow('tBrowR')}<g id="traBlush" opacity="0"><ellipse cx="190" cy="1004" rx="16" ry="9" fill="#ef5e66"/><ellipse cx="300" cy="1004" rx="16" ry="9" fill="#ef5e66"/></g>
    ${mouthEl('tra_m',244,1016)}<g id="tears"></g></g>
   ${hose('tArmL')}${hose('tArmR')}</g>`;
  s+=`<path d="M336,740 L336,1480" ${LN}/>`;
  // the epiglottis: a flap that hinges at its base (pivot 186,742) and folds back over the windpipe
  s+=`<g id="epi"><g id="epiFlap">${shaded('M128,742 C112,640 128,520 170,430 C204,360 250,310 300,300 C318,298 322,316 310,330 C276,372 262,430 258,520 C256,600 250,680 246,742Z',EPI,EPI_S,16)}
    <path d="M168,700 C160,600 176,500 214,430 C238,388 268,350 298,320" fill="none" stroke="#fbd0d3" stroke-width="8" stroke-linecap="round" opacity=".8"/>
    ${shaded('M70,520 C60,470 110,440 150,456 C180,470 182,520 160,560 C140,592 90,590 76,560Z',BONEY,BONEY_D,10)}${boneDots([[100,500,4],[132,488,3],[118,540,4],[148,524,3]])}
    <g id="epiFace"><g transform="translate(168,600)">${oEye('eEyeL',28,EPI)}</g><g transform="translate(228,592)">${oEye('eEyeR',28,EPI)}</g>${brow('eBrowL')}${brow('eBrowR')}${mouthEl('epi_m',198,650)}</g></g>
    ${hose('eArm')}</g>`;
  s+=`${foodSVG('food1')}${foodSVG('food2')}${foodSVG('crumb',.5)}<g id="steam"></g><g id="flames"></g>`;
  s+=`</g>`;return s;}
function throatLabels(){const v=`<g id="lbEpi" transform="translate(52,690) rotate(-90)"><rect x="-74" y="-17" width="148" height="34" fill="#fff" ${LN}/><text class="lbl" style="font-size:19px" text-anchor="middle" y="7">EPIGLOTTIS</text></g>`;
  return v+labelBox('lbTra','TRACHEA',246,852,22)+labelBox('lbEso','ESOPHAGUS',560,800,20);}

// ---------------- SCENE B: the man at the dinner table, eating spicy food ----------------
function dinnerWorld(){
  let s=`<g id="wDinner"><rect x="-200" y="-200" width="1120" height="1680" fill="#eef0f1"/>
   <rect x="-200" y="-200" width="1120" height="260" fill="#e3e6e8"/>
   <g transform="translate(70,-40)"><rect x="0" y="0" width="300" height="420" fill="#f9fbfc" ${LN}/><rect x="16" y="16" width="268" height="388" fill="#dcebf2"/><path d="M150,16 V404 M16,210 H284" stroke="#9aa5ac" stroke-width="10"/><rect x="0" y="0" width="300" height="420" fill="none" ${LN}/></g>
   <rect x="580" y="-200" width="40" height="760" fill="#8a9298" ${LN2}/>
   <g transform="translate(360,430) scale(1.32)">${patientSVG()}</g>
   <g id="spicyFace" opacity="0"></g>
   <path d="M-200,930 C100,910 620,910 920,930 L920,1480 L-200,1480Z" fill="#7a5235" ${LN}/><path d="M-200,944 C100,926 620,926 920,944" ${TH('#9c6d49')} stroke-width="4"/>
   ${plate(170,1010,1.25,true)}${plate(540,1060,1.05,false)}${plate(330,1190,.9,true)}
   </g>`;
  return s;}
function plate(x,y,s,chicken){return `<g transform="translate(${x},${y}) scale(${s})"><ellipse rx="150" ry="52" fill="#f7f6f2" ${LN}/><ellipse rx="118" ry="38" fill="none" ${TH('#d4d0c8')} stroke-width="3"/>
  ${chicken?[[-60,-14],[-10,-24],[40,-12],[-34,10],[18,8],[66,4]].map(([a,b],i)=>`<g transform="translate(${a},${b}) rotate(${i*40}) scale(.55)"><path d="M-30,-40 C-6,-52 24,-44 34,-20 C44,6 36,34 14,44 C-8,54 -34,42 -40,18 C-46,-6 -46,-30 -30,-40Z" fill="${i%2?'#c9422c':'#d65a2e'}" ${LN}/><path d="M-12,-18 l8,-3 M8,6 l8,-3" stroke="#a31b22" stroke-width="5" stroke-linecap="round"/></g>`).join('')+
   [[-80,-30],[70,-26],[0,16]].map(([a,b])=>`<path d="M${a},${b} c10,-14 26,-14 30,0" fill="#e0262c" ${LN2}/>`).join(''):
   [[-50,-10],[-10,-18],[30,-8],[60,6],[-30,10]].map(([a,b],i)=>`<path d="M${a},${b} c-10,-22 20,-30 26,-8 c10,-16 28,-6 18,10 c-8,12 -36,14 -44,-2z" fill="${i%2?'#6fb04f':'#8ccf5e'}" ${LN2}/>`).join('')+`<circle cx="-60" cy="4" r="12" fill="#e2474b" ${LN2}/><circle cx="52" cy="-18" r="10" fill="#e2474b" ${LN2}/>`}</g>`;}

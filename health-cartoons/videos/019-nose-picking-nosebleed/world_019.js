// =============== 019: how picking your nose makes it bleed. The reference's scenes; our drawings, all code ===============
const OLW=`stroke="${INK}" stroke-width="3.4" stroke-linejoin="round" stroke-linecap="round"`;
const OLW2=`stroke="${INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"`;
const C_SK='#f9e6cf', C_SK_S='#e6c9a6', C_CAV='#a8323c', C_CAV_S='#7c1f2a', C_BLOOD='#e02634', C_TEAL='#14a3a0';
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const CAV_D='M566,236 C622,236 650,320 654,430 L660,716 C660,790 606,812 520,804 L176,792 C96,786 84,716 150,646 C284,494 440,324 506,262 C524,244 544,236 566,236 Z';
const fingerSVG=(w,len)=>`<path d="M${-w/2},${len} L${-w/2},${w*.5} C${-w/2},${-w*.2} ${w/2},${-w*.2} ${w/2},${w*.5} L${w/2},${len} Z" fill="${C_SK}" ${OLW}/><path d="M${-w*.3},${w*.5} C${-w*.3},${w*.1} ${w*.3},${w*.1} ${w*.3},${w*.5} L${w*.3},${w*.95} L${-w*.3},${w*.95} Z" fill="#fde9da" ${OLW2}/><path d="M${-w*.3},${w*1.9} h${w*.6} M${-w*.26},${w*2.1} h${w*.52}" stroke="${C_SK_S}" stroke-width="4" stroke-linecap="round"/>`;
const card=(inner,txt)=>`<g id="inset"><rect x="16" y="130" width="196" height="330" rx="18" fill="#fff" ${OLW}/>${inner}<text x="114" y="440" text-anchor="middle" style="font-family:LG,sans-serif;font-size:20px" fill="#1d2a44">${txt}</text></g>`;
const lim=(d,wd,col=C_SK)=>`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${wd+7}" stroke-linecap="round" stroke-linejoin="round"/><path d="${d}" fill="none" stroke="${col}" stroke-width="${wd}" stroke-linecap="round" stroke-linejoin="round"/>`;
const nail=(x,y,rot,s=1)=>`<g transform="translate(${x},${y}) rotate(${rot}) scale(${s})"><path d="M-22,-4 C-22,-34 22,-34 22,-4 L22,26 C22,34 -22,34 -22,26 Z" fill="#fdf3e6" ${OLW2}/></g>`;
// a wobbly stream of blood: top at (x,y0), length L, width wd, ending in lobes
function streamD(x,y0,L,wd,T){const n=7,l=[],rr=[];for(let i=0;i<=n;i++){const y=y0+L*i/n,ww=wd*(1+.16*Math.sin(i*1.9+T*2.2)),o=Math.sin(i*1.2+T*1.6)*wd*.13*(i/n);l.push([x-ww/2+o,y]);rr.push([x+ww/2+o,y]);}
  let d=`M${l[0][0].toFixed(1)},${y0}`;for(let i=1;i<=n;i++)d+=` L${l[i][0].toFixed(1)},${l[i][1].toFixed(1)}`;
  const a=l[n],b=rr[n],u=(b[0]-a[0])/3,k=Math.min(wd*.55,L*.3);d+=` q${(u*.5).toFixed(1)},${k.toFixed(1)} ${u.toFixed(1)},${(k*.1).toFixed(1)} q${(u*.5).toFixed(1)},${(k*1.5).toFixed(1)} ${u.toFixed(1)},${(k*.2).toFixed(1)} q${(u*.5).toFixed(1)},${(k*.8).toFixed(1)} ${u.toFixed(1)},${(-k*.3).toFixed(1)}`;
  for(let i=n-1;i>=0;i--)d+=` L${rr[i][0].toFixed(1)},${rr[i][1].toFixed(1)}`;return d+' Z';}
// ---- scene 1: inside the nose, seen from the side (the reference's staging) ----
function insideNose(){
  DEFS+=`<clipPath id="cavC"><path d="${CAV_D}"/></clipPath><radialGradient id="cavG" cx=".35" cy=".7" r=".8"><stop offset="0" stop-color="#b8404a"/><stop offset="1" stop-color="#8f2630"/></radialGradient>`;
  const eyeShut=x=>`<g transform="translate(${x},0)"><ellipse rx="31" ry="33" fill="#fff" ${OLW2}/><path d="M${x<0?-14:14},-14 L${x<0?10:-10},0 L${x<0?-14:14},14" fill="none" stroke="${INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></g>`;
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#ddf3fb"/>
   <path d="M540,-40 C450,200 240,520 56,700 C-20,776 -6,890 110,940 C230,990 400,1010 470,1000 C430,1060 400,1160 440,1330 L770,1330 L770,-40 Z" fill="${C_SK}" ${OLW}/>
   <path d="M664,600 C724,700 716,880 600,960 C560,988 520,1000 470,1000" fill="none" ${OLW}/>
   <path d="M60,790 C40,850 80,900 150,925" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" opacity=".6"/>
   <path d="${CAV_D}" fill="url(#cavG)" ${OLW}/>
   <g clip-path="url(#cavC)"><path d="M120,700 C270,520 430,350 524,256" fill="none" stroke="#efcfb4" stroke-width="34" stroke-linecap="round"/><path d="M168,712 C300,556 450,392 540,300" fill="none" stroke="#7a1c26" stroke-width="16" stroke-linecap="round" opacity=".6"/>
    <path d="M200,690 q30,-50 80,-90 q40,0 30,34 q-40,50 -90,70 Z" fill="#b59a5a" opacity=".9"/><path d="M230,676 q30,-30 60,-52" stroke="#9a8046" stroke-width="5" fill="none" stroke-linecap="round"/>
    <path d="M452,566 l16,-14 l12,12 l-8,18 l-16,2 Z M486,520 l8,-8 l8,6 l-6,10 Z" fill="#a9ad5c"/>
    <g id="scratch" opacity="0"><path d="M372,664 l22,-18 l14,16 l24,-14 l16,22 l-10,26 l14,24 l-22,18 l-20,-10 l-24,16 l-14,-24 l-18,-8 l10,-26 Z" fill="#7d101b"/><path d="M392,690 l14,10 M420,676 l-6,16 M410,716 l16,-6" stroke="#4f0810" stroke-width="5" stroke-linecap="round"/></g>
    <g id="blood1"></g></g>
   <g transform="rotate(12,372,924)"><ellipse cx="372" cy="924" rx="176" ry="58" fill="#7a1c26" ${OLW}/><ellipse cx="372" cy="932" rx="150" ry="40" fill="${C_CAV}"/></g>
   <g id="blood1b"></g>
   <g id="booger"><path d="M-46,-6 l14,-34 l30,-12 l34,10 l22,30 l-8,36 l-30,22 l-36,-2 l-24,-22 Z" fill="#a9ad5c" ${OLW2}/><path d="M-18,-18 l20,-8 l18,12 M-12,14 l22,6 l16,-14 M-30,2 l14,10" fill="none" stroke="#868a3c" stroke-width="4" stroke-linecap="round"/></g>
   <g id="finger"><path d="M-78,1300 L-78,70 C-78,-30 78,-30 78,70 L78,1300 Z" fill="${C_SK}" ${OLW}/><path d="M-50,60 C-50,-6 50,-6 50,60 L50,150 C50,168 -50,168 -50,150 Z" fill="#fdf3e6" ${OLW2}/><path d="M-44,330 q44,14 88,0 M-40,366 q40,12 80,0" fill="none" stroke="${C_SK_S}" stroke-width="5" stroke-linecap="round"/></g>
   <g id="rim" transform="rotate(12,372,924)"><path d="M200,936 C250,990 494,990 544,936" fill="none" stroke="${INK}" stroke-width="27" stroke-linecap="round"/><path d="M200,936 C250,990 494,990 544,936" fill="none" stroke="${C_SK}" stroke-width="20" stroke-linecap="round"/></g>
   <g id="drip1"></g>
   <g id="lface" transform="translate(552,420)"><g id="lnOpen"><g transform="translate(-34,0)">${oEye('ln_eL',33,'#a3323c')}</g><g transform="translate(34,0)">${oEye('ln_eR',33,'#a3323c')}</g></g><g id="lnShut" opacity="0">${eyeShut(-34)}${eyeShut(34)}</g>${brow('ln_bL')}${brow('ln_bR')}<g transform="translate(0,64) scale(2.1)">${mouthEl('ln_m',0,0)}</g></g>`;}
// ---- scene 2: the nose from the front ----
function frontNose(){
  const handL=`<path d="M-420,760 C-400,420 -300,120 -200,-20 C-176,-56 -128,-40 -136,4 C-160,110 -190,300 -180,760 Z" fill="${C_SK}" ${OLW}/><path d="M-186,-6 C-174,-30 -148,-22 -152,2 L-164,50 L-200,38 Z" fill="#fdf3e6" ${OLW2}/><path d="M-262,150 q40,12 72,-4 M-276,214 q42,12 78,-2" fill="none" stroke="${INK}" stroke-width="2.6" stroke-linecap="round"/>`;
  const OUT='M188,557 C120,540 44,590 44,680 C44,745 80,790 130,806 C200,832 290,796 360,822 C430,796 520,832 590,806 C640,790 676,745 676,680 C676,590 600,540 532,557';
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#f9e6cf"/>
   <path d="M262,-40 C276,200 250,420 176,560 C250,440 318,200 302,-40 Z M458,-40 C444,200 470,420 544,560 C470,440 402,200 418,-40 Z" fill="#ecd7b8"/>
   <path d="${OUT} C470,470 250,470 188,557 Z" fill="#fbeedc"/><path d="M92,640 C80,700 100,760 150,786 M628,640 C640,700 620,760 570,786" fill="none" stroke="#f0dcc0" stroke-width="16" stroke-linecap="round"/>
   <path d="${OUT}" fill="none" ${OLW}/>
   <path d="M150,762 C182,726 262,730 292,770 C262,786 190,788 150,762 Z" fill="#241512"/><path d="M570,762 C538,726 458,730 428,770 C458,786 530,788 570,762 Z" fill="#241512"/>
   <g id="drip2"></g><g id="sniff"></g>
   <g id="wipe"><path d="M-200,-30 C-150,-120 -60,-80 0,-124 C60,-80 150,-120 200,-30 L270,760 L-270,760 Z" fill="#fff" ${OLW}/><path d="M-90,-40 q30,240 -30,780 M10,-80 q30,340 10,820 M100,-40 q-10,280 50,780" fill="none" stroke="#dfe3e8" stroke-width="7" stroke-linecap="round"/><g id="wipeRed"></g>
     ${handL}<g transform="scale(-1,1)">${handL}</g></g>
   <g id="plug"><path d="M-140,470 C-176,330 -156,170 -92,112 L80,100 C184,140 224,330 204,470 Z" fill="${C_SK}" ${OLW}/>
     <path d="M-26,156 L-8,60 L26,62 L40,166 Z" fill="#e3cba8"/>
     ${lim('M160,230 C212,244 226,286 206,318',58)}${lim('M162,318 C214,332 222,372 200,402',58)}
     ${lim('M-76,196 C-84,112 -62,50 -28,8',74)}${lim('M82,206 C94,132 82,70 40,16',84)}
     <path d="M-70,270 C-20,244 70,244 120,272" fill="none" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>${nail(-38,28,26,.75)}
     <g id="ball"><path d="M-34,-10 C-44,-40 -18,-62 6,-54 C28,-68 56,-46 50,-22 C66,-2 52,28 28,28 C14,44 -18,42 -24,22 C-44,22 -48,2 -34,-10 Z" fill="#fff" ${OLW2}/><g id="plugRed"></g><path d="M-10,-30 q14,-8 24,2 M0,6 q14,6 24,-6" fill="none" stroke="#d8dce2" stroke-width="4" stroke-linecap="round"/></g>
     <g id="tface" opacity="0"><g transform="translate(84,-66) scale(2.4)">${oEye('tp_eL',18,'#fff')}</g><g transform="translate(156,-22) scale(2.4)">${oEye('tp_eR',18,'#fff')}</g><g transform="translate(120,-44) scale(1.3)">${brow('tp_bL')}${brow('tp_bR')}</g><g transform="translate(70,40) scale(2.3)">${mouthEl('tp_m',0,0)}</g></g></g>`;}
// ---- scene 3: lean forward and pinch (close on the nose and mouth) ----
function profile(){
  return `<rect x="-40" y="-40" width="800" height="1360" fill="#ddf3fb"/>
   <g id="head"><path d="M1300,-300 L560,-300 L540,-80 C520,60 486,200 446,300 L282,452 C250,482 262,520 308,524 L352,528 C340,580 330,604 352,630 C328,656 336,682 362,690 C350,740 362,800 424,850 C510,920 566,1020 586,1700 L1300,1700 Z" fill="${C_SK}" ${OLW}/>
    <path d="M430,178 q80,-56 170,-8" fill="none" stroke="#1c1512" stroke-width="30" stroke-linecap="round"/><path d="M456,262 q46,30 100,2" fill="none" stroke="${INK}" stroke-width="7" stroke-linecap="round"/>
    <path d="M372,452 q44,-34 66,22" fill="none" ${OLW}/><path d="M362,690 q34,-10 70,8" fill="none" ${OLW2}/>
    <path id="pmouth" d="M350,628 L430,640 L360,676 C340,664 340,640 350,628 Z" fill="#5a2a2a" ${OLW2} opacity="0"/>
    <path id="pblood" d="M300,522 C292,560 300,596 318,622 C328,640 350,634 352,608 C360,580 356,550 350,526 Z" fill="#e5484d"/>
    <g id="phand"><path d="M-520,-200 C-430,-276 -280,-256 -220,-170 C-180,-110 -180,40 -230,112 C-300,184 -470,174 -540,100 C-600,30 -590,-140 -520,-200 Z" fill="${C_SK}" ${OLW}/>
     ${lim('M-300,92 C-220,112 -110,102 -6,52',78)}${lim('M-300,-150 C-220,-236 -60,-204 0,-46',74)}
     <ellipse cx="-350" cy="-30" rx="120" ry="160" fill="${C_SK}"/><path d="M-262,-110 q-52,10 -62,52 M-250,-30 q-52,6 -66,46 M-262,50 q-46,4 -62,38" fill="none" stroke="${INK}" stroke-width="3.4" stroke-linecap="round"/>
     ${nail(-20,54,-104,.7)}${nail(-2,-64,170,.7)}</g></g>`;}
// ---- scene 5: the clinic (the reference's two-shot: desk, doctor, patient holding the stained tissue) ----
function clinic19(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#b9c58c"/><rect x="-60" y="150" width="840" height="60" fill="#a4996c"/>
   <path d="M-60,930 H780 V1400 H-60 Z" fill="#9a8f80"/><path d="M-60,930 H780 M-60,1050 H780 M-60,1200 H780 M120,930 L40,1340 M330,930 L300,1340 M520,930 L560,1340 M690,930 L780,1300" stroke="#6f665b" stroke-width="3" fill="none"/>
   <g transform="translate(150,300) scale(1.08)">${doctorSVG()}</g>
   <path d="M-60,800 H330 V842 H-60 Z" fill="#b89a86" ${OLW}/><path d="M150,842 H312 V1190 H150 Z" fill="#b39581" ${OLW}/>
   <g id="patWrap"><g transform="translate(540,330) scale(1.08)">${patientSVG()}</g>
    <g id="ptis"><path d="M0,0 C-34,30 -60,110 -48,190 l22,-26 l12,38 l24,-32 l14,32 l18,-36 l18,22 C76,120 40,36 0,0 Z" fill="#fff" ${OLW}/><path d="M-12,64 C6,52 24,74 16,102 C26,128 0,150 -14,128 C-30,110 -26,80 -12,64 Z" fill="#e5484d"/><ellipse cx="26" cy="140" rx="9" ry="18" fill="#e5484d"/><ellipse cx="-28" cy="150" rx="7" ry="13" fill="#ef8a8d"/></g></g>`;}

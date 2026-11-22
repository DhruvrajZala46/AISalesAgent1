// =============== 010: the reference's six sets, at the positions and sizes measured on its 720x1280 frames. All code, our characters. ===============
const OLW=`stroke="${INK}" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round"`;
const WALL='#e98d81', WALL_D='#c96d62', FLR='#fa9394', FLR_D='#d66e6f', DEEP='#7e2b2e';
function wavyLine(x0,x1,y,amp,wl,ph){let d='';for(let x=x0;x<=x1;x+=12)d+=(d?'L':'M')+x+','+(y+amp*Math.sin(x/wl+ph)).toFixed(1)+' ';return d;}
function labelTop(id,text,cx,cy,w,fs=46,tl=0){return `<g id="${id}"><rect x="${cx-w/2}" y="${cy-33}" width="${w}" height="66" fill="#fff" stroke="${INK}" stroke-width="4" stroke-linejoin="round"/><text x="${cx}" y="${cy+fs*.36}" text-anchor="middle" ${tl?`textLength="${tl}" lengthAdjust="spacingAndGlyphs"`:''} style="font-family:ComicNeue,sans-serif;font-weight:700;font-size:${fs}px" fill="#111">${text}</text></g>`;}

// ---------------- SET A / E: the blood-vessel wall with the cut (INTRAVASCULAR SPACE) ----------------
// measured on the reference: wall #e98d81 with dark vertical cracks, a wide cream cut (left edge 251,250 -> 344,950; right edge
// bulging to 418 at y 800), floor #fa9394 from y 985 with #d66e6f blotches, top band #903b3e, label box 79-641 x 47-113.
const CUT_L=[[248,205],[251,250],[258,400],[272,500],[286,600],[299,700],[321,800],[338,900],[350,986]];
const CUT_R=[[436,986],[425,900],[418,800],[407,700],[388,600],[363,500],[339,400],[307,350],[272,300],[250,214]];
const CUT_D=smooth(CUT_L)+' L'+smooth(CUT_R).slice(1)+'Z';
function crack(x,y,h,seed){let d=`M${x},${y}`,cx=x;for(let k=1;k<=6;k++){cx+=(rnd(seed+k)-.5)*16;d+=` L${cx.toFixed(0)},${(y+h*k/6).toFixed(0)}`;}return d;}
function wallWorld(){
  let s=`<g id="wWall"><rect x="-60" y="-60" width="840" height="1400" fill="${WALL}"/>
   <rect x="680" y="-60" width="100" height="1100" fill="#d9786d" opacity=".5"/><rect x="-60" y="-60" width="80" height="1100" fill="#d9786d" opacity=".35"/>`;
  [[30,150,240],[96,420,300],[150,120,160],[392,120,180],[452,430,270],[560,150,250],[610,520,300],[680,200,200],[50,690,230],[520,740,210],[190,640,200],[640,820,150],[470,150,120],[120,880,90]].forEach(([x,y,h],i)=>{
    s+=`<path d="${crack(x,y,h,i*7)}" fill="none" stroke="${WALL_D}" stroke-width="9" stroke-linecap="round" opacity=".45"/><path d="${crack(x,y,h,i*7)}" fill="none" stroke="#3a1f1c" stroke-width="2.6" stroke-linecap="round"/>`;});
  // the cut (revealed top-to-bottom by #cutReveal), cream with a dark lip on its left edge
  s+=`<clipPath id="cutClip"><rect id="cutReveal" x="200" y="190" width="280" height="0"/></clipPath>
   <g clip-path="url(#cutClip)"><path d="${CUT_D}" fill="#fbe5cc" ${OLW}/><path d="${smooth(CUT_L)}" fill="none" stroke="#8c523f" stroke-width="9" stroke-linecap="round"/>
   <path d="${smooth(CUT_L.map(([x,y])=>[x+16,y]))}" fill="none" stroke="#f3d2b4" stroke-width="6" stroke-linecap="round" opacity=".8"/></g>`;
  // the planks the platelets nailed over the cut (set E): two crossed at the top, two below
  s+=`<g id="planks" opacity="0">${[[287,340,10,290],[290,346,-12,280],[300,520,-3,280],[322,622,-16,280]].map(([x,y,r,w])=>`<g transform="translate(${x},${y}) rotate(${r})"><path d="M${-w/2},-30 L${w/2-8},-36 L${w/2+6},-12 L${w/2-4},28 L${-w/2+6},34 L${-w/2-8},4Z" fill="#d6b788" ${OLW}/>
     <path d="M${-w/2+18},-10 C${-w/6},-18 ${w/6},-2 ${w/2-22},-14 M${-w/2+28},12 C${-w/6},6 ${w/5},18 ${w/2-26},8" fill="none" stroke="#a5845a" stroke-width="3" stroke-linecap="round"/><circle cx="${-w/2+18}" cy="0" r="4" fill="#7a6a5a"/><circle cx="${w/2-20}" cy="-6" r="4" fill="#7a6a5a"/></g>`).join('')}</g>`;
  // floor
  s+=`<path d="M-60,986 ${wavyLine(-60,780,986,4,40,1).replace('M','L')} L780,1340 L-60,1340Z" fill="${FLR}"/>
   ${[[40,1040,90],[250,1030,70],[470,1050,80],[650,1035,60],[120,1110,120],[380,1120,100],[600,1100,110],[60,1180,150],[280,1190,170],[520,1185,150],[700,1175,90],[160,1250,200],[420,1255,200],[660,1255,160]].map(([x,y,w],i)=>`<path d="M${x-w/2},${y} C${x-w/4},${y-18-i%3*4} ${x+w/4},${y+12} ${x+w/2},${y-2} C${x+w/4},${y+20} ${x-w/4},${y+22} ${x-w/2},${y}Z" fill="${FLR_D}"/>`).join('')}
   <path d="${wavyLine(-60,780,986,4,40,1)}" fill="none" ${OLW}/>`;
  s+=`<g id="spark" opacity="0"><path d="M0,-40 L10,-12 L38,-16 L16,6 L28,34 L0,16 L-28,34 L-16,6 L-38,-16 L-10,-12Z" fill="#ffd21f" ${OLW}/></g>`;
  s+=`${rbcSVG('rb0')}${rbcSVG('rb1')}${rbcSVG('rb2')}${rbcSVG('rb3')}${prostSVG('pg')}${guardSVG('gd')}${pillSVG('pA',true)}${pillSVG('pB')}
   <g id="ringLines"></g><g id="dust"></g></g>`;
  return s;}
function topBand(){return `<path d="M-20,-20 L740,-20 L740,24 ${wavyLine(740,-20,30,6,26,0).replace('M','L')} Z" fill="#903b3e" ${OLW}/>`;}

// ---------------- SET B: the stomach close-up (one shape: food pipe + stomach, lining band inside, juice in the bottom) ----------------
const STO_PTS=[[52,-70],[174,-70],[179,100],[192,180],[209,240],[236,300],[268,326],[330,326],[400,316],[500,304],[600,292],[650,288],[690,300],[712,350],[720,450],[715,560],[695,670],[655,755],[590,820],[500,862],[400,920],[300,968],[180,992],[100,1000],[-70,1004],
  [-70,800],[-20,788],[70,700],[170,600],[191,500],[150,400],[96,300],[76,240],[67,180],[60,100]];
function stomachWorld10(){
  const SD=closedD(STO_PTS);
  DEFS+=`<clipPath id="lumClip10"><path d="${SD}"/></clipPath><clipPath id="lowClip10"><rect x="-60" y="560" width="840" height="800"/></clipPath>`;
  let s=`<g id="wStom"><rect x="-60" y="-60" width="840" height="1400" fill="#c25253"/>
   <path d="M290,-70 L790,-70 L790,250 C660,262 540,236 440,206 C360,180 306,120 290,-70Z" fill="#af4945" ${OLW}/>
   <path d="M330,-70 C340,70 400,150 520,190" fill="none" stroke="#c45c58" stroke-width="10" stroke-linecap="round" opacity=".7"/>
   <path d="M-60,-60 L40,-60 C30,120 20,260 -60,330Z" fill="#b24a4c" ${OLW}/>`;
  // the yellow duct behind the food pipe
  s+=`<path d="M246,-70 C258,60 270,180 266,330" fill="none" stroke="${INK}" stroke-width="47" stroke-linecap="round"/><path d="M246,-70 C258,60 270,180 266,330" fill="none" stroke="#eccb7a" stroke-width="41" stroke-linecap="round"/>
   <path d="M240,-60 C250,60 258,170 256,300" fill="none" stroke="#f7e3a8" stroke-width="8" stroke-linecap="round" opacity=".8"/>`;
  // gallbladder peeking out on the left
  s+=`<path d="M-50,520 C30,500 140,520 160,580 C176,640 130,690 50,690 C0,690 -40,670 -50,650Z" fill="#2e7a30" ${OLW}/><path d="M-30,545 C40,530 110,545 135,580" fill="none" stroke="#5fae55" stroke-width="10" stroke-linecap="round" opacity=".8"/>
   <path d="M10,620 C40,590 90,590 110,620 C100,650 40,655 10,620Z" fill="#1d5520" ${OLW}/>`;
  // the muscular wall under the stomach, then the intestines
  s+=`<g clip-path="url(#lowClip10)"><path d="${SD}" fill="none" stroke="${INK}" stroke-width="86"/><path d="${SD}" fill="none" stroke="#c64650" stroke-width="80"/>
    <path d="${SD}" fill="none" stroke="#d9606a" stroke-width="10" opacity=".7" transform="translate(0,14)"/></g>`;
  const lobes=(y,h,n,ph)=>{let d=`M-80,${y}`;const w=920/n;for(let i=0;i<n;i++){const x=-80+i*w;d+=` C${(x+w*.2).toFixed(0)},${y+h} ${(x+w*.8).toFixed(0)},${y+h} ${(x+w).toFixed(0)},${y}`;}return d;};
  s+=`<path d="M-80,1040 C120,1010 300,1060 500,1040 C620,1028 700,1000 800,960 L800,1340 L-80,1340Z" fill="#eca1a5" ${OLW}/>
   <path d="${lobes(1110,60,6,0)}" fill="none" ${OLW}/><path d="${lobes(1190,-50,5,0)}" fill="none" ${OLW}/><path d="${lobes(1230,50,7,0)}" fill="none" ${OLW}/>
   <path d="M-60,1100 C100,1080 300,1110 520,1090" fill="none" stroke="#f6c3c6" stroke-width="10" stroke-linecap="round" opacity=".8"/>`;
  // the stomach itself
  s+=`<g id="stoB"><path d="${SD}" fill="#f38c8f"/>
   <g clip-path="url(#lumClip10)">
    ${[[300,420,120],[540,400,110],[640,470,80],[230,470,70],[600,520,70]].map(([x,y,w])=>`<path d="M${x-w/2},${y} c${w/4},-18 ${w/2},16 ${w},0" fill="none" stroke="#dd6f77" stroke-width="3" stroke-linecap="round"/>`).join('')}
    ${[[120,60],[110,180],[150,260]].map(([x,y])=>`<path d="M${x-14},${y} c6,10 18,12 28,4" fill="none" stroke="#dd6f77" stroke-width="3" stroke-linecap="round"/>`).join('')}
    <path id="juice10" fill="#eda285"/><path id="juiceTop10" fill="none" stroke="#f6c0a4" stroke-width="5"/>
    <g opacity=".55">${Array.from({length:46},(_,i)=>{const x=-20+rnd(i+300)*740,y=575+rnd(i+400)*420,w=40+rnd(i+500)*70;return `<path d="M${x.toFixed(0)},${y.toFixed(0)} q${(w/4).toFixed(0)},-7 ${(w/2).toFixed(0)},0 t${(w/2).toFixed(0)},0" fill="none" stroke="#fbd5c0" stroke-width="2.6" stroke-linecap="round"/>`;}).join('')}</g>
    <path d="${SD}" fill="none" stroke="${INK}" stroke-width="56"/><path d="${SD}" fill="none" stroke="#f9c3c3" stroke-width="51"/>
    ${Array.from({length:22},(_,i)=>{const p=along(STO_PTS.slice(1,25),i/21);return `<circle cx="${p[0].toFixed(0)}" cy="${p[1].toFixed(0)}" r="${3+i%3}" fill="#ea8d95" opacity=".8"/>`;}).join('')}
   </g><path d="${SD}" fill="none" ${OLW}/>
   <g id="stoFace10"><g transform="translate(412,270)">${oEye('sEyeL',37,'#f38c8f')}</g><g transform="translate(500,270)">${oEye('sEyeR',37,'#f38c8f')}</g>
    ${mouthEl('sto_m',450,352)}
    <g id="mask10"><path d="M352,232 C376,212 540,208 562,232 C574,258 566,300 548,312 C500,300 420,302 372,314 C352,302 344,260 352,232Z" fill="#a9c9e6" ${OLW}/>
     <path d="M372,246 C410,232 520,230 548,244" fill="none" stroke="#d7e8f5" stroke-width="6" stroke-linecap="round"/><path d="M394,276 q20,10 40,0" fill="none" stroke="${INK}" stroke-width="3"/><path d="M474,276 q20,10 40,0" fill="none" stroke="${INK}" stroke-width="3"/>
     <path d="M352,262 C320,262 300,276 286,296" fill="none" stroke="#7fa3c4" stroke-width="7" stroke-linecap="round"/></g></g>
   <g id="stick10" opacity="0"><rect x="-6" y="-166" width="12" height="330" rx="5" fill="#e9dfc8" ${OLW}/><path d="M-1,-156 L-1,154" stroke="#fffaf0" stroke-width="3"/></g>
   ${pillSVG('sA',true)}${pillSVG('sB')}
   ${hose('sArmL10')}${hose('sArmR10')}<g id="dropPills"></g></g></g>`;
  return s;}
// ---------------- SET C: the vein ----------------
function veinWorld10(){
  let s=`<g id="wVein"><rect x="-60" y="-60" width="840" height="1400" fill="#e9786f"/>`;
  [[-40,60,780,140],[-40,190,780,120],[100,-40,180,250],[480,-40,560,230],[-40,1120,780,1200],[60,1060,260,1300],[420,1080,520,1300],[600,1050,700,1300]].forEach(([x1,y1,x2,y2],i)=>{
    const d=`M${x1},${y1} C${(x1*2+x2)/3+40},${(y1*2+y2)/3-40} ${(x1+x2*2)/3-40},${(y1+y2*2)/3+40} ${x2},${y2}`;
    s+=`<path d="${d}" fill="none" stroke="${INK}" stroke-width="${i%2?26:20}" stroke-linecap="round"/><path d="${d}" fill="none" stroke="#f3a09d" stroke-width="${i%2?19:13}" stroke-linecap="round"/>`;});
  s+=`<path d="M-60,322 C200,300 500,220 780,130" fill="none" stroke="${INK}" stroke-width="20"/><path d="M-60,322 C200,300 500,220 780,130" fill="none" stroke="#d8505a" stroke-width="14"/>
   <path d="M-60,336 C200,314 500,234 780,148 L780,1030 C500,1050 200,1080 -60,1110Z" fill="#f3c38d" ${OLW}/>
   <path d="M-60,362 C200,340 500,260 780,174 L780,1004 C500,1024 200,1054 -60,1084Z" fill="#e99aa4" ${OLW}/>
   <path d="M-60,1100 C200,1070 500,1042 780,1022" fill="none" stroke="#d8505a" stroke-width="12" opacity=".0"/>
   ${[[60,420,200],[380,360,240],[150,560,260],[500,520,200],[60,720,220],[360,760,280],[560,880,180],[180,920,240]].map(([x,y,w])=>`<path d="M${x},${y} C${x+w/3},${y-10} ${x+w*2/3},${y+10} ${x+w},${y}" fill="none" stroke="#d47d8b" stroke-width="4" stroke-linecap="round"/>`).join('')}
   ${pillSVG('vA',true)}${pillSVG('vB')}</g>`;
  return s;}

// ---------------- SET D: the two tunnels (reference: pink tissue full of creases, a dark cave on each side, a crease-covered trunk between) ----------------
function creaseSet(n,x0,x1,y0,y1,seed,len=90){let s='';for(let i=0;i<n;i++){const x=x0+rnd(seed+i)*(x1-x0),y=y0+rnd(seed+i+70)*(y1-y0),a=(rnd(seed+i+140)-.5)*1.6-Math.PI/2,L=len*(.5+rnd(seed+i+210));
  const x2=x+Math.cos(a)*L,y2=y+Math.sin(a)*L,cx=(x+x2)/2+(rnd(seed+i+280)-.5)*40,cy=(y+y2)/2+(rnd(seed+i+350)-.5)*40;
  s+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} Q${cx.toFixed(0)},${cy.toFixed(0)} ${x2.toFixed(0)},${y2.toFixed(0)}" fill="none" stroke="${INK}" stroke-width="${(2.2+rnd(seed+i+420)*1.6).toFixed(1)}" stroke-linecap="round"/>`;}return s;}
function cave(pts,vp,cols){let s='';cols.forEach((c,k)=>{const f=1-k*(k<2?.1:.2);const p=pts.map(([x,y])=>[vp[0]+(x-vp[0])*f+(k?Math.sin(k*2.1+y/90)*8:0),vp[1]+(y-vp[1])*f]);
  s+=`<path d="${closedD(p)}" fill="${c}" ${k?'stroke="#3a0a10" stroke-width="2.4"':OLW}/>`;});
  for(let i=0;i<5;i++){const x=vp[0]+(i-2)*34,y0=vp[1]-200+i*14;s+=`<path d="M${x},${y0} C${x+20},${y0+120} ${x-16},${y0+260} ${x+10},${y0+400}" fill="none" stroke="#3a0a10" stroke-width="3" opacity=".5"/>`;}return s;}
function tunnelWorld10(){
  let s=`<g id="wTun"><rect x="-60" y="-60" width="840" height="1400" fill="#fb989f"/>
   <path d="M-60,-60 L780,-60 L780,140 C640,110 560,40 480,-10 C420,40 330,60 240,10 C150,60 60,90 -60,70Z" fill="#d46c76" ${OLW}/>
   ${creaseSet(26,230,470,40,820,11,120)}${creaseSet(10,40,700,20,140,31,70)}
   ${cave([[-80,60],[110,40],[220,140],[262,320],[258,520],[222,700],[150,830],[-80,860]],[40,470],['#9a2f3a','#7d2430','#6a1d27','#531219','#3f0c12'])}
   ${cave([[800,120],[610,128],[496,236],[456,430],[474,630],[540,770],[640,800],[800,800]],[690,470],['#9a2f3a','#8f2f35','#6a1d27','#531219','#3f0c12'])}
   <path d="M-60,820 C80,850 160,800 300,830 C420,856 520,800 640,812 C700,818 740,830 780,826 L780,1340 L-60,1340Z" fill="#fc989f" ${OLW}/>
   ${Array.from({length:30},(_,i)=>{const x=-40+rnd(i+600)*780,y=860+rnd(i+650)*400,w=60+rnd(i+700)*110;return `<path d="M${(x-w/2).toFixed(0)},${y.toFixed(0)} C${(x-w/4).toFixed(0)},${(y-14-rnd(i)*10).toFixed(0)} ${(x+w/4).toFixed(0)},${(y+12).toFixed(0)} ${(x+w/2).toFixed(0)},${(y-4).toFixed(0)}" fill="none" stroke="${INK}" stroke-width="${(2.2+rnd(i+750)*1.5).toFixed(1)}" stroke-linecap="round"/>`;}).join('')}
   ${pillSVG('tA',true)}${pillSVG('tB')}</g>`;
  return s;}

// ---------------- SET F: the clinic (the reference's plain room: light wall, ceiling vent, door frame on the left) ----------------
function clinicRoom10(){
  return `<rect x="-60" y="-60" width="840" height="1400" fill="#e8f3f9"/>
   <rect x="640" y="-60" width="140" height="1400" fill="#f7fbfd" ${OLW}/>
   <g transform="translate(262,52)"><rect x="0" y="0" width="304" height="192" fill="#2b2b2b" ${OLW}/>${[0,1,2,3].map(i=>`<rect x="10" y="${10+i*45}" width="284" height="36" fill="#c6c9cc"/><rect x="10" y="${36+i*45}" width="284" height="8" fill="#8b9095"/>`).join('')}</g>
   <rect x="-10" y="432" width="82" height="900" fill="#a3683f" ${OLW}/><rect x="16" y="462" width="56" height="880" fill="#cfd8dd" ${OLW}/>
   <path d="M600,1110 L780,1110 L780,1340 L600,1340Z" fill="#dfe9ee" ${OLW}/>`;}

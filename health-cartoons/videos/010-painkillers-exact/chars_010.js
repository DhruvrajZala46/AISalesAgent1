// =============== 008 worlds: ALL code, in the 001 / 003-v1 style (thin INK lines, shaded(), muted colours, objects with faces) ===============
const STW='#ee9ea3', STW_S='#d47c86', LUM='#f9c8c2', LUM_S='#eaa39f', JUICE='#e9c97c', JUICE_S='#c9a654';
const FLESH='#ec9a90', FLESH_S='#d07a72', FLOOR='#f2a6a3', FLOOR_S='#d98785';
function closedD(pts){return smooth(pts.concat([pts[0],pts[1]]))+'Z';}
function tubeL(d,w,fill,shade,id=''){return `<path ${id?`id="${id}"`:''} d="${d}" fill="none" stroke="${INK}" stroke-width="${w+5.2}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${fill}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="${d}" fill="none" stroke="${shade}" stroke-width="${(w*.22).toFixed(1)}" stroke-linecap="round" stroke-linejoin="round" opacity=".55" transform="translate(0,${(w*.28).toFixed(1)})"/>`;}
function hose(id){return `<g id="${id}"><path id="${id}_o" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><path id="${id}_i" fill="none" stroke="#fff" stroke-width="7.5" stroke-linecap="round" stroke-linejoin="round"/><g id="${id}_h"></g></g>`;}
function setHose(id,pts,rot,s=1){const d=smooth(pts);$(id+'_o').setAttribute('d',d);$(id+'_i').setAttribute('d',d);const e=pts[pts.length-1];$(id+'_h').innerHTML=glove(e[0],e[1],rot,s);}
function wrinkles(n,x0,x1,y0,y1,col,seed){let s='';for(let i=0;i<n;i++){const x=x0+rnd(seed+i)*(x1-x0),y=y0+rnd(seed+i+50)*(y1-y0),h=60+rnd(seed+i+90)*140;
  s+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} c${(rnd(i+7)*16-8).toFixed(0)},${(h*.3).toFixed(0)} ${(rnd(i+9)*20-10).toFixed(0)},${(h*.6).toFixed(0)} ${(rnd(i+11)*12-6).toFixed(0)},${h.toFixed(0)}" ${TH(col)} stroke-width="2.4"/>`;}return s;}

// ---------- characters ----------
// painkiller capsule with a face (pill2 wears a pink bow)
function pillSVG(id,bow=false){return `<g id="${id}"><g id="${id}_b">${leg(-16,84,34,4)}${leg(16,84,34,-4)}
  <path d="M-36,0 L-36,-48 A36,36 0 0 1 36,-48 L36,0Z" fill="#e2474b" ${STK}/><path d="M-36,0 L-36,48 A36,36 0 0 0 36,48 L36,0Z" fill="#f8f6f2" ${STK}/>
  <path d="M-22,-62 C-14,-74 6,-78 18,-72" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".55"/><path d="M22,10 L22,52" stroke="#e3ded6" stroke-width="5" stroke-linecap="round"/>
  <g transform="translate(-14,-44)">${oEye(id+'_eL',13,'#e2474b')}</g><g transform="translate(14,-44)">${oEye(id+'_eR',13,'#e2474b')}</g>${brow(id+'_bL')}${brow(id+'_bR')}
  ${mouthEl(id+'_m',0,-16)}
  ${bow?`<g transform="translate(-20,-80) rotate(-18)"><path d="M0,0 L-22,-14 L-22,14Z M0,0 L22,-14 L22,14Z" fill="#f06aa6" ${LN2}/><circle r="6" fill="#d94b8c" ${LN2}/></g>`:''}
  </g>${hose(id+'_aL')}${hose(id+'_aR')}</g>`;}
function setPill(id,x,y,s,{talk=0,T=0,look=0,lookY=0,mood=.4,rot=0,arms='down',seed=0,angry=0,run=0}={}){
  const hop=run?Math.abs(Math.sin(T*16+seed))*14:0;
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${(y-hop).toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${s})`);
  const bl=blinkK(T,seed*.7+.2); setOEye(id+'_eL',13,{dx:look*40,dy:lookY*40,lid:.1,blink:bl}); setOEye(id+'_eR',13,{dx:look*40,dy:lookY*40,lid:.1,blink:bl});
  setBrow(id+'_bL',-14,-62+angry*3,16,angry*18,2); setBrow(id+'_bR',14,-62+angry*3,16,-angry*18,2);
  setMouthV(id+'_m',talk,9,mood,T,seed);
  const w=Math.sin(T*4+seed)*5, sw=run?Math.sin(T*16+seed)*16:0;
  const A={down:[[[-36,4],[-54,30],[-58,58+w]],[[36,4],[54,30],[58,58-w]],40,-40],
           wave:[[[-36,4],[-56,24],[-60,56]],[[36,4],[62,-20],[70,-62+w]],40,-150],
           point:[[[-36,4],[-54,30],[-58,58]],[[36,4],[72,-2],[104,-10]],40,-90],
           fist:[[[-36,4],[-66,-10],[-80,-40+w]],[[36,4],[66,-10],[80,-40-w]],150,-150],
           run:[[[-36,4],[-56,20+sw],[-62,40+sw]],[[36,4],[56,20-sw],[62,40-sw]],40,-40]}[arms];
  setHose(id+'_aL',A[0],A[2],.62); setHose(id+'_aR',A[1],A[3],.62);}
// red blood cell with eyes
function rbcSVG(id){return `<g id="${id}">${shaded('M-52,0 C-52,-30 -28,-46 0,-46 C28,-46 52,-30 52,0 C52,30 28,46 0,46 C-28,46 -52,30 -52,0Z','#e2474b','#c3363c',12)}
  <ellipse rx="28" ry="22" fill="#cc3a41" opacity=".55"/><path d="M-30,-28 C-18,-38 4,-40 16,-36" fill="none" stroke="#ff9a9d" stroke-width="5" stroke-linecap="round"/>
  <g transform="translate(-14,-8)">${oEye(id+'_eL',13,'#e2474b')}</g><g transform="translate(14,-8)">${oEye(id+'_eR',13,'#e2474b')}</g></g>`;}
// prostaglandin: a spiky magenta ball (the pain messenger)
function prostSVG(id){let sp='';for(let i=0;i<10;i++){const a=i/10*Math.PI*2-.2,x=Math.cos(a)*84,y=Math.sin(a)*80,x2=Math.cos(a)*112,y2=Math.sin(a)*108;
   sp+=`<path d="M${x.toFixed(0)},${y.toFixed(0)} L${x2.toFixed(0)},${y2.toFixed(0)}" stroke="${INK}" stroke-width="11" stroke-linecap="round"/><path d="M${x.toFixed(0)},${y.toFixed(0)} L${x2.toFixed(0)},${y2.toFixed(0)}" stroke="#d63c95" stroke-width="6.5" stroke-linecap="round"/><circle cx="${x2.toFixed(0)}" cy="${y2.toFixed(0)}" r="13" fill="#e46aae" ${LN2}/>`;}
  return `<g id="${id}"><g id="${id}_sp">${sp}</g>${shaded('M-90,0 C-90,-52 -50,-88 0,-88 C50,-88 90,-52 90,0 C90,52 50,88 0,88 C-50,88 -90,52 -90,0Z','#dc4a9c','#b52d7c',18)}
  <path d="M-54,-52 C-34,-70 0,-74 22,-68" fill="none" stroke="#f7a3cf" stroke-width="6" stroke-linecap="round"/>
  ${(()=>{DEFS+=`<clipPath id="${id}_bc"><path d="M-90,0 C-90,-52 -50,-88 0,-88 C50,-88 90,-52 90,0 C90,52 50,88 0,88 C-50,88 -90,52 -90,0Z"/></clipPath>`;return `<g clip-path="url(#${id}_bc)"><path d="M-100,40 L100,30 L100,64 L-100,74Z" fill="#2a2322"/><text x="0" y="61" text-anchor="middle" transform="rotate(-3)" style="font-family:LG,sans-serif;font-size:17px;letter-spacing:.5px" fill="#fff">PROSTAGLANDIN</text></g>`;})()}
  <g id="${id}_face"><g transform="translate(-26,-30)">${oEye(id+'_eL',22,'#dc4a9c')}</g><g transform="translate(26,-30)">${oEye(id+'_eR',22,'#dc4a9c')}</g>${brow(id+'_bL')}${brow(id+'_bR')}${mouthEl(id+'_m',0,12)}</g>
  <g id="${id}_ko" opacity="0"><path d="M-40,-44 l26,26 M-14,-44 l-26,26 M14,-44 l26,26 M40,-44 l-26,26" stroke="${INK}" stroke-width="5" stroke-linecap="round"/><path d="M-16,14 Q0,24 16,14" fill="none" ${LN}/><path d="M4,18 q8,18 18,6" fill="#e88a8f" ${LN2}/></g>
  ${hose(id+'_aL')}${hose(id+'_aR')}</g>`;}
function setProst(id,x,y,s,{talk=0,T=0,look=0,mood=.2,rot=0,ko=0,angry=0}={}){
  $(id).setAttribute('transform',`translate(${x.toFixed(1)},${y.toFixed(1)}) rotate(${rot.toFixed(1)}) scale(${s})`);
  $(id+'_sp').setAttribute('transform',`rotate(${(Math.sin(T*3)*4).toFixed(1)})`);
  show(id+'_face',ko?0:1); show(id+'_ko',ko?1:0);
  const bl=blinkK(T,1.7); setOEye(id+'_eL',22,{dx:look*40,dy:2,lid:.15,blink:bl}); setOEye(id+'_eR',22,{dx:look*40,dy:2,lid:.15,blink:bl});
  setBrow(id+'_bL',-26,-60,26,angry*20,3); setBrow(id+'_bR',26,-60,26,-angry*20,3);
  setMouthV(id+'_m',talk,14,mood,T,4);
  const w=Math.sin(T*4)*6;
  if(ko){setHose(id+'_aL',[[-84,10],[-120,30],[-140,60]],20,.8);setHose(id+'_aR',[[84,10],[120,30],[140,60]],-20,.8);}
  else if(talk>.05){setHose(id+'_aL',[[-84,10],[-122,-10],[-136,-50+w]],60,.8);setHose(id+'_aR',[[84,10],[122,-10],[136,-50-w]],-60,.8);}
  else {setHose(id+'_aL',[[-84,10],[-114,40],[-104,74+w]],0,.8);setHose(id+'_aR',[[84,10],[114,40],[104,74-w]],0,.8);}}

// ---------------- SCENE A / E: inside the foot, the cut (later boarded up by the platelets) ----------------
function glassAt(x,y,s=1){return `<g transform="translate(${x},${y}) scale(${s})"><path d="M-16,-26 L16,-26 L12,24 C12,28 -12,28 -12,24Z" fill="#e6f4fa" ${LN2} opacity=".95"/><path d="M-14,-6 L14,-6 L12,22 C12,25 -12,25 -12,22Z" fill="#a9d6ea"/><path d="M-9,-20 L-8,16" stroke="#fff" stroke-width="3" stroke-linecap="round"/></g>`;}

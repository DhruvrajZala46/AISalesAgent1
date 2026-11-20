// =============== SCENE 1 : stomach cross-section (world coords) ===============
function crSample(C,n){const out=[],m=C.length;for(let i=0;i<n;i++){const u=i/(n-1)*(m-1),k=Math.min(m-2,Math.floor(u)),t=u-k;
  const p0=C[Math.max(0,k-1)],p1=C[k],p2=C[k+1],p3=C[Math.min(m-1,k+2)];
  const f=(a,b,c,d)=>0.5*((2*b)+(-a+c)*t+(2*a-5*b+4*c-d)*t*t+(-a+3*b-3*c+d)*t*t*t);out.push([f(p0[0],p1[0],p2[0],p3[0]),f(p0[1],p1[1],p2[1],p3[1])]);}return out;}
function lerpArr(ws,n){const out=[];for(let i=0;i<n;i++){const u=i/(n-1)*(ws.length-1),k=Math.min(ws.length-2,Math.floor(u));out.push(lerp(ws[k],ws[k+1],u-k));}return out;}
function along(pts,u){u=clamp(u);const L=[0];for(let i=1;i<pts.length;i++)L.push(L[i-1]+Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]));
  const d=u*L[L.length-1];let i=1;while(i<L.length-1&&L[i]<d)i++;const k=(d-L[i-1])/((L[i]-L[i-1])||1);
  return [lerp(pts[i-1][0],pts[i][0],k),lerp(pts[i-1][1],pts[i][1],k),Math.atan2(pts[i][1]-pts[i-1][1],pts[i][0]-pts[i-1][0])*180/Math.PI];}
const STO_C=[[318,372],[470,470],[522,640],[440,830],[262,880]], STO_W=[110,330,340,240,74];
const NS=15, STO_PTS=crSample(STO_C,NS), STO_WS=lerpArr(STO_W,NS);
function stoPaths(sq){const wo=STO_WS.map((w,i)=>w*(1-sq(i))), wi=wo.map(w=>Math.max(12,w-46));return [limbD(STO_PTS,wo),limbD(STO_PTS,wi)];}
const ESO_C=[[262,-90],[285,120],[305,290],[326,380]];
const DUO_C=[[262,880],[190,905],[150,990],[165,1120],[230,1330]];
const GUMD='M-30,10 C-36,-4 -30,-18 -16,-20 C-10,-27 4,-27 10,-21 C24,-23 34,-12 32,2 C38,10 32,20 20,20 C10,25 -6,24 -14,21 C-26,23 -34,18 -30,10 Z';
function gumBody(id,face,sc=1){return `<g id="${id}"><g id="${id}_i" transform="scale(${sc})"><path d="${GUMD}" fill="url(#gGum)"/><path d="${GUMD}" fill="none" ${LN}/>
  <path d="M-20,-12 C-14,-17 -6,-17 -2,-15" fill="none" stroke="#ffe3ef" stroke-width="3" stroke-linecap="round" ${VE}/>
  <path d="M-24,12 q4,-4 8,0 M-4,16 q4,-4 8,0 M14,13 q4,-4 8,0" ${TH('#c4467a')}/>
  ${face?`<g id="${id}F"><g transform="translate(-10,-6)">${oEye(id+'E1',9,'#f58fb9')}</g><g transform="translate(11,-6)">${oEye(id+'E2',9,'#f58fb9')}</g>${brow(id+'B1')}${brow(id+'B2')}${mouthEl(id+'_m',0,9)}</g>`:''}
  </g></g>`;}
const TIS='#a95a5d';
let W=`<g id="world">
 <rect x="-700" y="-700" width="2120" height="2680" fill="${TIS}"/>
 <g fill="none" stroke="#934a4e" stroke-width="5" stroke-linecap="round" opacity=".8">${[[60,220,240,170],[560,60,700,180],[40,700,170,820],[620,980,700,1100],[80,1180,300,1240]].map(([a,b,c,d])=>`<path d="M${a},${b} Q${(a+c)/2},${b-40} ${c},${d}"/>`).join('')}</g>
 ${shaded('M520,-60 C640,-40 760,40 760,160 C700,260 600,260 520,220 C470,180 470,60 520,-60 Z','#8c3a36','#6a2724',22)}
 <g>${[[110,1080],[300,1150],[520,1110],[640,980],[420,1250],[180,1250]].map(([x,y])=>shaded(`M${x-90},${y} C${x-90},${y-60} ${x+90},${y-60} ${x+90},${y} C${x+90},${y+60} ${x-90},${y+60} ${x-90},${y} Z`,'#e39ea2','#c27479',16)).join('')}</g>
 ${shaded(limbD(DUO_C,[78,78,78,78,78]),'#e47d85','#b9545e',14)}<path d="${limbD(DUO_C,[50,50,50,50,50])}" fill="#f5c2c1"/>
 <clipPath id="stoClip"><path id="stoClipP"/></clipPath><clipPath id="lumClip"><path id="lumClipP"/></clipPath>
 <path id="stoO" fill="#e47d85"/><g clip-path="url(#stoClip)"><path id="stoOs" fill="none" stroke="#b9545e" stroke-width="26" filter="url(#soft)"/></g>
 <path id="stoI" fill="url(#gSto)"/>
 <g clip-path="url(#lumClip)">
   <g fill="none" stroke="#e48e96" stroke-width="5" stroke-linecap="round" opacity=".8">${[0,1,2,3,4,5,6].map(i=>`<path d="M${330+i*40},${420+i*18} q30,40 0,80 q-30,40 0,80 q30,40 0,80"/>`).join('')}</g>
   <circle id="antGlow" cx="300" cy="860" r="90" fill="#e0473f" filter="url(#soft2)" opacity="0"/>
   <g id="acidG"><path id="acidP" fill="#d6d36a" opacity=".88"/><path id="acidHi" fill="none" stroke="#f3f0a8" stroke-width="5" stroke-linecap="round"/>
     ${[0,1,2,3,4,5].map(i=>`<circle id="ab${i}" r="${5+i%3*2}" fill="none" stroke="#f6f3b5" stroke-width="2.5"/>`).join('')}</g>
   ${[0,1,2,3].map(i=>`<g id="fd${i}" opacity="0">${[`<path d="M-18,-10 L18,-12 L20,10 L-16,12 Z" fill="#e2b062" ${LN2}/>`,`<circle r="11" fill="#86b64e" ${LN2}/>`,`<path d="M-20,0 C-10,-12 10,12 20,0" fill="none" stroke="#f1d27c" stroke-width="7" stroke-linecap="round"/>`,`<path d="M-14,-12 L16,-8 L12,12 L-16,8 Z" fill="#c9673f" ${LN2}/>`][i]}</g>`).join('')}
 </g>
 <path id="stoOl" fill="none" ${LN}/><path id="stoIl" fill="none" stroke="#c45f69" stroke-width="2.2" ${VE}/>
 ${shaded(limbD(ESO_C,[92,90,92,104]),'#e47d85','#b9545e',12)}<path d="${limbD(ESO_C,[60,58,60,66])}" fill="#f5c2c1"/>
 <g id="stoFace"><g transform="translate(428,318)">${oEye('sfE1',25,'#e47d85')}</g><g transform="translate(500,324)">${oEye('sfE2',25,'#e47d85')}</g>${brow('sfB1')}${brow('sfB2')}${mouthEl('sf_m',466,372)}
   <g id="sfSweat" opacity="0"><path d="M560,300 C566,312 568,320 560,326 C552,320 554,312 560,300Z" fill="#8fd3f4" ${LN2}/></g></g>
 ${[0,1,2,3,4].map(i=>`<g id="adrop${i}" opacity="0"><path d="M0,-8 C5,-2 6,4 0,8 C-6,4 -5,-2 0,-8Z" fill="#d6d36a" ${LN2}/></g>`).join('')}
 ${[0,1,2].map(i=>`<g id="stm${i}" opacity="0"><path d="M0,0 c-10,-10 10,-20 0,-30 c-10,-10 10,-20 0,-30" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".85"/></g>`).join('')}
 ${[0,1,2,3,4].map(i=>gumBody('gp'+i,false,.62)).join('')}
 ${gumBody('blob',true,1)}
 ${gumBody('gum',true,1)}
 <g id="shades" opacity="0"><path d="M-22,-12 h17 v9 q-8,7 -17,0 Z M4,-12 h17 v9 q-8,7 -17,0 Z" fill="#1d1b20" ${LN2}/><path d="M-5,-10 h9" stroke="${INK}" stroke-width="2.5"/></g>
 <g id="gSpark" opacity="0">${[[34,-26],[-36,-22],[40,14]].map(([x,y],i)=>`<path id="gs${i}" transform="translate(${x},${y})" d="M0,-9 L2.5,-2.5 9,0 2.5,2.5 0,9 -2.5,2.5 -9,0 -2.5,-2.5Z" fill="#fff6b0" ${LN2}/>`).join('')}</g>
</g>`;
let S1=`<g id="s1"><g id="cam">${W}</g>${labelBox('lbSto','STOMACH',560,110)}${labelBox('lbAcid','STOMACH ACID',360,1000,20)}</g>`;

// =============== SCENE 3 : intestines ===============
const IC=crSample([[-90,130],[560,150],[630,300],[120,380],[80,540],[600,600],[640,760],[110,830],[90,990],[560,1050],[640,1200],[650,1420]],70);
let S3=`<g id="s3"><g id="icam"><rect x="-700" y="-700" width="2120" height="2680" fill="${TIS}"/>
 ${shaded(limbD(IC,IC.map(()=>134)),'#e7979c','#bf6a71',18)}<path d="${limbD(IC,IC.map(()=>94))}" fill="#f7cdcc"/>
 <path d="${limbD(IC,IC.map(()=>94))}" fill="none" stroke="#c45f69" stroke-width="2" ${VE}/>
 <g transform="translate(332,498)">${oEye('inE1',21,'#e7979c')}</g><g transform="translate(392,504)">${oEye('inE2',21,'#e7979c')}</g>${brow('inB1')}${brow('inB2')}${mouthEl('in_m',362,532)}
 ${gumBody('igum',true,1)}
 <g id="swirl" opacity="0" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round">${[0,1,2].map(i=>`<path d="M${-40-i*20},0 A${40+i*20},${40+i*20} 0 0 1 0,${-40-i*20}"/>`).join('')}</g>
 </g>${labelBox('lbInt','INTESTINES',190,110)}</g>`;
// =============== LATER card ===============
let SL=`<g id="sL"><rect width="720" height="1280" fill="#0b0b0d"/><text id="laterT" x="360" y="660" text-anchor="middle" class="cta" style="font-size:64px;stroke-width:8px" fill="#ffd21f">2 DAYS LATER...</text></g>`;

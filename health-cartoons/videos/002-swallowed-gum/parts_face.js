// =============== SCENE X : patient's face (hook)  +  SCENE G : gum on its wrapper (stinger) ===============
function faceSVG(){return `<g id="face" transform="translate(360,300) scale(3.4)">
  <path d="M-17,150 L-16,212 L16,212 L17,150 Z" fill="${PSK}" ${LN2}/><path d="M-16,178 C-6,188 6,188 16,178 L16,212 L-16,212Z" fill="${PSK_S}" opacity=".7"/>
  <path d="M-110,300 C-100,230 -60,212 -40,206 C-30,232 30,232 40,206 C60,212 100,230 110,300 Z" fill="#c7884a" ${LN}/><path d="M-40,206 C-30,232 30,232 40,206" fill="#b47a40" ${LN2}/>
  <ellipse id="lump" cx="0" cy="170" rx="9" ry="7" fill="${PSK_S}" opacity="0"/>
  ${shaded('M-52,70 C-54,28 -30,6 0,6 C32,6 56,28 54,72 C53,108 42,138 24,154 C12,162 -12,162 -24,154 C-42,138 -53,108 -52,70 Z',PSK,PSK_S,10)}
  <path d="M-54,88 C-62,84 -64,104 -54,108" fill="${PSK}" ${LN2}/><path d="M54,88 C62,84 64,104 54,108" fill="${PSK}" ${LN2}/>
  <path d="M-56,74 C-64,20 -30,-12 6,-8 C40,-6 64,16 58,72 C52,44 40,30 20,28 C4,34 -14,30 -24,24 C-34,40 -46,52 -56,74 Z" fill="#1f1d24" ${LN}/>
  <path id="fBrows" d="M-36,68 Q-24,62 -10,64 M8,64 Q22,62 34,68" fill="none" stroke="#1f1d24" stroke-width="4.2" stroke-linecap="round"/>
  ${humanEye('fEyeL',-22,88,12,7)}${humanEye('fEyeR',18,88,12,7)}
  <path d="M-4,96 C-10,110 -10,118 -2,121 C2,122 5,120 7,118" fill="none" ${TH('#9c6b4e')}/>
  <g transform="translate(-2,138)"><path id="fMouth" fill="#5e1a20" ${LN2}/><path id="fGumIn" fill="#f58fb9" opacity="0"/></g>
  <g id="bubG" opacity="0"><circle id="bubC" cx="-2" cy="140" r="1" fill="url(#gBub)" ${LN2}/><path id="bubHi" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/></g>
  <g id="popG" opacity="0" fill="#f58fb9">${[[-40,120,9],[34,118,8],[-18,160,7],[22,158,10],[-50,146,6],[46,142,7]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" ${LN2}/>`).join('')}</g>
 </g>`;}
let SX=`<g id="sx"><g id="fcam"><rect x="-400" y="-400" width="1520" height="2080" fill="#e8e3d8"/><rect x="-400" y="900" width="1520" height="900" fill="#b9c8cd"/>${faceSVG()}</g>
 <rect id="fdark" x="-10" y="-10" width="740" height="1300" fill="#3a0f14" opacity="0"/></g>`;
let SG=`<g id="sg"><g id="gcam"><rect x="-400" y="-400" width="1520" height="2080" fill="#e8e3d8"/><rect x="-400" y="760" width="1520" height="1000" fill="#c08d63"/><rect x="-400" y="752" width="1520" height="14" fill="#a87650"/>
  <g transform="translate(360,880) rotate(-6)"><path d="M-170,-40 L-120,-62 L-40,-46 L40,-66 L130,-48 L176,-20 L160,30 L90,52 L0,40 L-90,60 L-160,36 Z" fill="#d9dee4" ${LN}/>
   <path d="M-120,-62 L-100,40 M-40,-46 L-20,44 M40,-66 L52,46 M130,-48 L110,50" fill="none" ${TH('#a9b1bb')}/><path d="M-150,-20 L150,-30" stroke="#f7f9fb" stroke-width="6" opacity=".8"/></g>
  <g transform="translate(360,822)">${gumBody('sgum',true,2.1)}</g></g>
 <g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g></g>`;

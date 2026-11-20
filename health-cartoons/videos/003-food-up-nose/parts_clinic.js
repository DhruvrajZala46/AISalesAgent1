//__MARKUP__
function nosePoster(){return `<g transform="translate(560,250)"><rect x="-92" y="-118" width="184" height="236" fill="#fbfaf7" ${LN}/><rect x="-80" y="-106" width="160" height="182" fill="#eaf3f6"/>
  <path d="M-62,-96 C-30,-104 20,-100 34,-66 C40,-50 38,-34 36,-22 C52,-8 62,8 56,16 C50,22 42,20 38,22 C38,38 32,56 18,66 C4,74 -40,74 -62,74 Z" fill="#f2cbb2" ${LN2}/>
  <path d="M-62,-96 C-40,-110 0,-112 22,-90 C0,-92 -30,-86 -50,-70 C-58,-62 -62,-80 -62,-96 Z" fill="#3a2a2a" ${LN2}/><circle cx="14" cy="-34" r="4" fill="${INK}"/>
  <path d="M42,22 C50,36 40,46 48,58 C54,66 46,74 50,82" fill="none" stroke="${INK}" stroke-width="8" stroke-linecap="round"/><path d="M42,22 C50,36 40,46 48,58 C54,66 46,74 50,82" fill="none" stroke="#f6d27a" stroke-width="5" stroke-linecap="round"/>
  <rect x="-62" y="86" width="124" height="10" rx="3" fill="#8fb2bf"/><rect x="-44" y="100" width="88" height="8" rx="3" fill="#bcd2da"/></g>`;}
// =============== SCENE G : stinger (the noodle sulks on a tissue) + FOLLOW ===============
const SG_PTS=[[262,636],[300,700],[372,712],[452,704],[492,752],[462,812],[386,836],[300,826],[244,786],[262,740],[330,756],[402,770],[452,760]];
let SG=`<g id="sg"><g id="gcam"><rect width="720" height="1280" fill="#f4e4d3"/>
 <rect x="0" y="900" width="720" height="380" fill="#c99b72"/><path d="M0,900 h720" ${LN}/>
 ${[960,1040,1140].map(y=>`<path d="M0,${y} h720" stroke="#b5875f" stroke-width="3"/>`).join('')}
 <ellipse cx="370" cy="912" rx="250" ry="26" fill="#000" opacity=".12"/>
 <path d="M140,880 C120,840 150,800 130,760 C120,720 170,690 210,700 C240,650 300,660 330,640 C370,620 420,650 450,640 C500,630 540,670 560,700 C600,710 620,760 600,800 C620,840 600,880 560,896 C480,920 240,920 140,880 Z" fill="#ffffff" ${LN}/>
 <path d="M200,720 C240,760 230,820 270,860 M330,660 C350,720 340,800 380,880 M470,660 C470,720 500,780 480,860 M560,720 C540,780 570,830 540,880" fill="none" ${TH('#c9cfd6')} stroke-width="3"/>
 <path id="sgO" fill="none" stroke="${INK}" stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/><path id="sgF" fill="none" stroke="${NOOD}" stroke-width="31" stroke-linecap="round" stroke-linejoin="round"/>
 <path id="sgH" fill="none" stroke="#fff4c6" stroke-width="6" stroke-linecap="round" opacity=".9"/>
 <g id="sgFace"><g transform="translate(-26,-24)">${oEye('sEyeL',26,NOOD)}</g><g transform="translate(26,-24)">${oEye('sEyeR',26,NOOD)}</g>${brow('sBrowL')}${brow('sBrowR')}${mouthEl('sting_m',0,18)}
  <path id="tear" d="M0,-10 C5,-2 8,4 6,9 C4,14 -5,14 -7,9 C-9,4 -5,-2 0,-10 Z" fill="#8fd3f4" ${LN2} opacity="0"/></g></g>
 <g id="cta" opacity="0"><g id="cta_i">
  <rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>
</g>`;
//__CODE__
function renderS2(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['18_doctor'], pa=ST['17_patient'];
  let dr=2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0);
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,dr);
  $('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8)*1; if(T>=d0&&dT<.05) pr+=Math.sin(T*9)*1.5*(speak('doctor',T-.25)>.1?1:0);
  if(T>=E.checked-.1) pr+=Math.sin(P(T,E.checked-.1,E.checked+.9)*Math.PI*2)*4;
  if(T<d0&&pT>.2) pr+=Math.sin(T*7)*2;
  tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  const worried=T<E.regurg, surprised=T>=E.regurg&&T<E.swallow+.4;
  $('pBrows').setAttribute('d',surprised?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':(worried?'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66':'M-36,70 Q-24,64 -10,66 M8,66 Q22,64 34,70'));
  setMouthV('doc_m',dT,10,.7,T,5); setMouthV('pat_m',pT,10,worried?-.5:1,T,6);
  setHEye('dEyeL',3,blinkK(T,.7)); setHEye('dEyeR',3,blinkK(T,.7));
  setHEye('pEyeL',-3,blinkK(T,2.1)); setHEye('pEyeR',-3,blinkK(T,2.1));
  show('patBlush',T<d0+2?.75:.35);
  // the noodle still hanging out of his nose, swaying
  const sw=Math.sin(T*2.4)*5, pn=`M-6,121 C${-18+sw*.3},132 ${-24+sw*.6},146 ${-18+sw},160 C${-12+sw},174 ${-26+sw*1.2},184 ${-22+sw*1.4},198`;
  $('pnO').setAttribute('d',pn); $('pnF').setAttribute('d',pn);
  // left arm: points at the noodle while asking, then rests on his lap
  const down=eio(P(T,d0+.2,d0+1.0));
  const sh=[-84,234], el=[lerp(-132,-102,down),lerp(176,370,down)], wr=[lerp(-46,-90,down),lerp(140,470,down)];
  const d=limbD([sh,el,wr],[44,38,32]); $('patArmLD').setAttribute('d',d); $('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+(down>.5?12:0),lerp(130,-8,down),1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.75&&Math.floor(T*2)%3===0)?-7:0},86,226)`);
  $('clkM').setAttribute('transform',`rotate(${T*6})`);
  // camera: push in on the patient's question, punch in on the doctor at the condition name
  const pq=eio(P(T,pa,pa+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,END)+.07*pq, cx=lerp(360,430,pq), cy=lerp(640,600,pq);
  const pk=eio(P(T,E.regurg-.15,E.regurg+.15))*(1-eio(P(T,E.swallow-.35,E.swallow)));
  z=lerp(z,1.42,pk); cx=lerp(cx,232,pk); cy=lerp(cy,430,pk);
  const ty=lerp(640,560,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // thought bubbles: 1) the door sealed while he swallows, 2) the laugh drops it and the noodle shoots up
  const b1=T>=E.swallow-.15&&T<E.laughing-.15, b2=T>=E.laughing-.15&&T<E.harmless-.3;
  $('bub').setAttribute('opacity',(b1||b2)?1:0);
  if(b1||b2){const k=P(T,E.swallow-.15,E.swallow+.15);$('bub').setAttribute('transform',`translate(300,178) scale(${1.38*eob(k)}) translate(-265,-150)`);
    const rt=b1?lerp(E.peek-.6,E.shut+.6,P(T,E.swallow,E.laughing-.3)):lerp(E.drop-.3,E.innose+.3,P(T,E.laughing,E.harmless-.6));
    renderWorld(rt);}
  popLabel('lbReg',T,E.regurg-.05,E.swallow-.2,360,64);
  popLabel('lbTip',T,E.lot-.1,END,360,64);
  show('indark',Math.max(P(T,T_STING-.22,T_STING),1-P(T,T_CLINIC,T_CLINIC+.22))*.9);
}
function renderSting(T){
  const t=T-T_STING, talk=speak('noodle',T);
  const pts=SG_PTS.map((p,i)=>[p[0]+Math.sin(T*2+i)*2,p[1]+Math.cos(T*1.7+i*.7)*2+(i===0?Math.sin(T*1.4)*4:0)]);
  const d=smooth(pts); $('sgO').setAttribute('d',d); $('sgF').setAttribute('d',d); $('sgH').setAttribute('d',smooth(pts.slice(0,6).map(p=>[p[0]-3,p[1]-7])));
  const hx=pts[0][0], hy=pts[0][1];
  tr('sgFace',hx,hy-8,1,1,talk>.3?Math.sin(T*8)*3:-4);
  const bl=blinkK(T,.9), sad=T<E.then+.2;
  setOEye('sEyeL',26,{dx:-6,dy:14,lid:sad?.5:.2,blink:bl});setOEye('sEyeR',26,{dx:-6,dy:14,lid:sad?.5:.2,blink:bl});
  setBrow('sBrowL',-26,-60,32,sad?-16:4,3);setBrow('sBrowR',26,-60,32,sad?16:-4,3);
  setMouthV('sting_m',talk,14,sad?-1:.6,T,2);
  show('tear',sad&&t>.6?1:0); if(sad) $('tear').setAttribute('transform',`translate(-44,${(-6+((t*40)%34)).toFixed(1)})`);
  const zin=1.55+.1*eio(P(t,0,2)); $('gcam').setAttribute('transform',`translate(360,700) scale(${zin}) translate(-372,-748)`);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0);
  $('cta').setAttribute('transform',`translate(360,${220+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
  show('indark',(1-P(t,0,.22))*.9);
}

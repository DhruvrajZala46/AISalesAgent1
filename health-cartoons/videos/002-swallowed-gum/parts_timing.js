// =============== timing / animation (002) ===============
const E=D.ev, ST=D.start, END=D.end;
const GS=1.6, IN0=1.05, T_CLINIC=E.clinic, T_STING=E.stinger;
const KEY=/^(GUM|SEVEN|YEARS|YEAR|ACID|DIGEST|LEASE|TOILET|PACK|BLOB|MYTH|BEZOAR|KIDS|GUT|SPIT|STOMACH|MOVING|CLASSIC|MELT|BLOCK|SWALLOWED|FOLLOW)$/;
function lineDur(k){const L=D.lines.find(l=>l.id===k);return L?L.dur:0;}
//__VISEME__
// ---------------- stomach world ----------------
function stomachSq(T){let pos=-10,amp=0;
  if(T>=E.kick&&T<E.later){const k=((T-E.kick)/1.5)%1;pos=lerp(3,NS+2,k);amp=.30;}
  if(T>=E.blob-.4&&T<E.clinic+30){const k=((T-E.blob+.4)/1.1)%1;pos=lerp(5,NS-2,k);amp=.16;}
  return i=>amp*Math.exp(-Math.pow((i-pos)/1.7,2));}
function acidLevel(T){let y=640+Math.sin(T*1.7)*6;if(T>=E.acid-.2&&T<E.acid+1.1)y-=46*Math.sin(P(T,E.acid-.2,E.acid+1.1)*Math.PI);return y;}
const ESO_PTS=crSample(ESO_C,24);
const GUM_PATH=crSample([[410,610],[470,720],[440,812],[330,866],[262,880],[190,905],[150,990],[165,1140]],48);
function gumState(T){let x=410,y=600,r=0,sx=1,sy=1;const vis=T<E.later+.15;
  if(T<IN0+.45){const p=along(ESO_PTS,eo(P(T,IN0,IN0+.45)));x=p[0];y=p[1];r=Math.sin(T*20)*15;}
  else if(T<E.splash){const k=P(T,IN0+.45,E.splash);x=lerp(326,410,k);y=lerp(380,acidLevel(T)-16,eio(k));r=k*220;}
  else{x=410+Math.sin(T*1.3)*8;y=acidLevel(T)-16+Math.sin(T*2.1)*3;r=Math.sin(T*1.1)*8;}
  const k0=E.kick+.15,k1=ST['09_gum']+2.25,k2=E.later+.1;
  if(T>=k0){const u=T<k1?0.6*eio(P(T,k0,k1)):lerp(0.6,1,eio(P(T,k1,k2)));const p=along(GUM_PATH,u),m=P(T,k0,k0+.35);
    x=lerp(x,p[0],m);y=lerp(y,p[1],m);r=lerp(r,0,m);const pyl=P(T,k1-.7,k1)*(1-P(T,k1,k1+.2));sx=1+.9*pyl;sy=1-.5*pyl;}
  return {x,y,r,sx,sy,vis};}
const GP_T=[[302,842],[334,866],[286,878],[322,834],[306,860]];
function renderWorld(T){
  const [o,i]=stoPaths(stomachSq(T));
  ['stoO','stoOs','stoOl','stoClipP'].forEach(id=>$(id).setAttribute('d',o));['stoI','stoIl','lumClipP'].forEach(id=>$(id).setAttribute('d',i));
  const ay=acidLevel(T);let d=`M140,${ay}`;for(let x=140;x<=720;x+=24)d+=` L${x},${(ay+Math.sin(x*.04+T*3)*5).toFixed(1)}`;d+=' L720,1120 L140,1120 Z';$('acidP').setAttribute('d',d);
  let h=`M170,${ay+3}`;for(let x=170;x<=660;x+=24)h+=` L${x},${(ay+3+Math.sin(x*.04+T*3)*5).toFixed(1)}`;$('acidHi').setAttribute('d',h);
  [0,1,2,3,4,5].forEach(k=>{const ph=(T*.6+k*.17)%1,e=$('ab'+k);e.setAttribute('cx',250+k*70+Math.sin(T+k)*8);e.setAttribute('cy',lerp(910,ay+8,ph));e.setAttribute('opacity',(1-ph).toFixed(2));});
  // --- the gum
  const g=gumState(T);show('gum',g.vis?1:0);tr('gum',g.x,g.y);tr('gum_i',0,0,g.sx*GS,g.sy*GS,g.r);$('gumF').setAttribute('transform',`rotate(${-g.r})`);
  const sh=T>=ST['03_gum']+.35&&T<E.acid;show('shades',sh?1:0);tr('shades',g.x,g.y,GS*eob(P(T,ST['03_gum']+.35,ST['03_gum']+.6)));
  const tG=speak('gum',T),tS=speak('stomach',T);
  let ge={lid:.12,mood:1,brow:0,small:false,dx:40,dy:-30};
  if(T<E.splash+.6) ge={lid:0,mood:0,brow:-12,small:true,dx:0,dy:-40};
  if(T>=ST['03_gum']&&T<ST['06_stomach']) ge={lid:.42,mood:1,brow:-8,small:false,dx:40,dy:-40};
  if(T>=ST['06_stomach']&&T<ST['07_gum']) ge={lid:0,mood:-1,brow:-14,small:true,dx:0,dy:30};
  if(T>=ST['07_gum']&&T<ST['08_stomach']) ge={lid:.62,mood:1,brow:-6,small:false,dx:30,dy:-30};
  if(T>=ST['08_stomach']) ge={lid:.1,mood:-1,brow:-14,small:T>=ST['09_gum'],dx:-20,dy:-30};
  ['gumE1','gumE2'].forEach((e,k)=>setOEye(e,9,{dx:ge.dx,dy:ge.dy,lid:ge.lid,tilt:(k?-1:1)*(ge.brow<-10?-10:0),blink:blinkK(T,.5),small:ge.small}));
  setBrow('gumB1',-10,-19,10,ge.brow,2);setBrow('gumB2',11,-19,10,-ge.brow,2);setMouthV('gum_m',tG,6.5,ge.mood,T,1);
  // acid drops + steam + sparkle
  [0,1,2,3,4].forEach(k=>{const t0=E.acid+.05+k*.08,q=P(T,t0,t0+.55);show('adrop'+k,q>0&&q<1?1:0);
    tr('adrop'+k,lerp(330+k*35,g.x-18+k*9,q),lerp(ay,g.y-40,q)-Math.sin(q*Math.PI)*90,1.4);});
  [0,1,2].forEach(k=>{const q=((T-E.melt)*.9+k*.33)%1,on=T>=E.melt&&T<ST['07_gum']+.6;show('stm'+k,on?(1-q)*.9:0);tr('stm'+k,g.x-24+k*24,g.y-30-q*44);});
  const sp=T>=ST['07_gum']&&T<ST['08_stomach'];show('gSpark',sp?1:0);tr('gSpark',g.x,g.y,GS);
  [0,1,2].forEach(k=>{const q=(T*2.4+k*.3)%1;$('gs'+k).setAttribute('opacity',Math.sin(q*Math.PI).toFixed(2));});
  // --- twist: the whole pack, merging into one blob
  const twist=T>=E.packStart;
  [0,1,2,3,4].forEach(k=>{const t0=E.packStart+.15+k*.32;let x,y,s=1;
    if(T<t0){show('gp'+k,0);return;}
    if(T<t0+.45){const p=along(ESO_PTS,eo(P(T,t0,t0+.45)));x=p[0];y=p[1];}
    else{const q=eio(P(T,t0+.45,t0+1.0));x=lerp(326,GP_T[k][0],q);y=lerp(380,GP_T[k][1],q)-Math.sin(q*Math.PI)*60;}
    const mg=eio(P(T,E.blob-.45,E.blob-.1));x=lerp(x,305,mg);y=lerp(y,852,mg);s=1-mg;
    show('gp'+k,s>.02?1:0);tr('gp'+k,x,y,1,1,k*40);tr('gp'+k+'_i',0,0,.62*s,.62*s,0);});
  const bs=T>=E.blob-.35?eob(P(T,E.blob-.35,E.blob+.1))*1.4:0;show('blob',twist&&bs>0?1:0);
  const bb=T>=E.blob+.2?1+.08*Math.exp(-(T-E.blob-.2)*4)*Math.sin((T-E.blob-.2)*25):1;tr('blob',305,850,1,1,0);tr('blob_i',0,0,bs*bb,bs/bb,0);
  ['blobE1','blobE2'].forEach((e,k)=>setOEye(e,9,{dx:40,dy:-30,lid:.35,tilt:(k?1:-1)*-14,blink:blinkK(T,1.1)}));
  setBrow('blobB1',-10,-19,10,16,1);setBrow('blobB2',11,-19,10,-16,1);setMouthV('blob_m',T>=ST['13_gum']?speak('gum',T):0,6.5,1,T,7);
  show('antGlow',twist&&T>=E.blob?Math.min(.55,(T-E.blob)*1.5):0);
  [[402,800],[446,822],[380,768],[432,760]].forEach((p,k)=>{const t0=E.blob+.5+k*.22,q=P(T,t0,t0+.6);show('fd'+k,twist&&T>=t0?1:0);tr('fd'+k,lerp(330,p[0],q),lerp(380,p[1],eio(q))-Math.sin(q*Math.PI)*60,1,1,k*30);});
  // --- stomach face
  let se={lid:.12,mood:0,brow:0,small:false};const lookX=g.vis?g.x-464:(twist?305-464:0),lookY=g.vis?g.y-321:(twist?400:0);
  if(T>=ST['02_stomach']&&T<ST['04_stomach']) se={lid:.45,mood:-1,brow:12,small:false};
  if(T>=ST['04_stomach']&&T<ST['06_stomach']) se={lid:.1,mood:0,brow:-10,small:false};
  if(T>=ST['06_stomach']&&T<ST['08_stomach']) se={lid:.5,mood:1,brow:8,small:false};
  if(T>=ST['08_stomach']&&T<E.later) se={lid:.3,mood:-1,brow:16,small:false};
  if(twist&&T<E.blob) se={lid:0,mood:-1,brow:-16,small:true};
  if(twist&&T>=E.blob) se={lid:.62,mood:-1,brow:-16,small:false};
  ['sfE1','sfE2'].forEach((e,k)=>setOEye(e,25,{dx:lookX,dy:lookY,lid:se.lid,tilt:(k?1:-1)*(se.brow>10?12:se.brow<-10?-12:0),blink:blinkK(T,2.2),small:se.small}));
  setBrow('sfB1',428,284,26,se.brow,4);setBrow('sfB2',500,290,26,-se.brow,4);setMouthV('sf_m',tS,15,se.mood,T,2);
  show('sfSweat',twist?1:0);$('sfSweat').setAttribute('transform',`translate(0,${((T*1.4)%1)*30})`);
  return g;}
function avgTarget(fn,T){let a=[0,0,0],w=0;for(let k=0;k<6;k++){const t=fn(T-k*.07),ww=1-k*.12;a=a.map((v,i)=>v+t[i]*ww);w+=ww;}return a.map(v=>v/w);}
function stoTarget(T){const g=gumState(T);
  if(T<E.splash) return [360,520,1.0];
  if(T>=E.packStart) return T<E.blob-.3?[400,640,1.0]:(T>=ST['13_gum']-.1?[318,820,1.55]:[440,560,1.18]);
  if(T>=E.kick+.15) return [Math.max(260,Math.min(470,g.x)),g.y-60,1.32];
  for(const k of ['02_stomach','04_stomach','06_stomach','08_stomach']) if(T>=ST[k]-.15&&T<ST[k]+lineDur(k)) return [468,420,1.45];
  for(const k of ['03_gum','05_gum','07_gum']) if(T>=ST[k]-.15&&T<ST[k]+lineDur(k)) return [g.x+10,g.y-40,1.6];
  return [420,560,1.1];}
function renderStomach(T){const g=renderWorld(T);const [cx,cy,Z]=avgTarget(stoTarget,T);
  let sx=0,sy=0;[[E.splash,8],[E.kick,6],[E.blob+.2,10]].forEach(([t0,a])=>{const k=P(T,t0,t0+.4);if(k>0&&k<1){sx+=Math.sin(k*45)*a*(1-k);sy+=Math.cos(k*38)*a*.6*(1-k);}});
  $('cam').setAttribute('transform',`translate(${360+sx},${640+sy}) scale(${Z}) translate(${-cx},${-cy})`);
  const lb=(id,t0,t1,x,y)=>{const on=T>=t0&&T<t1;show(id,on?1:0);if(on)$(id).setAttribute('transform',`translate(${x},${y}) scale(${eob(P(T,t0,t0+.28))})`);};
  lb('lbSto',ST['02_stomach'],E.later,560,110); lb('lbAcid',E.acid,ST['08_stomach'],520,168);
  show('indark',1-P(T,IN0,IN0+.25));}
// ---------------- intestines ----------------
function renderGut(T){const u=lerp(.04,1,eio(P(T,E.intestine,E.flush+.5)));const p=along(IC,u);
  tr('igum',p[0],p[1]);tr('igum_i',0,0,1.5,1.5,Math.sin(T*3)*10);
  const sad=T>=ST['11_gum'];['igumE1','igumE2'].forEach((e,k)=>setOEye(e,9,{dx:sad?0:40,dy:sad?30:-20,lid:sad?.5:.15,tilt:(k?-1:1)*(sad?-12:0),blink:blinkK(T,.8)}));
  setBrow('igumB1',-10,-19,10,sad?-14:0,2);setBrow('igumB2',11,-19,10,sad?14:0,2);setMouthV('igum_m',speak('gum',T),6.5,sad?-1:0,T,3);
  ['inE1','inE2'].forEach((e,k)=>setOEye(e,21,{dx:p[0]-362,dy:p[1]-500,lid:.15,blink:blinkK(T,1.6)}));
  setBrow('inB1',332,474,20,0,4);setBrow('inB2',392,480,20,0,4);setMouthV('in_m',speak('intestine',T),12,1,T,4);
  let Z=1.25,cx=clamp(p[0],250,470),cy=p[1]+40;
  if(T<ST['10_intestine']+lineDur('10_intestine')+.1&&T>=ST['10_intestine']-.1){cx=lerp(cx,362,.5);cy=lerp(cy,520,.5);}
  const fl=P(T,E.flush,E.flush+.9);show('swirl',fl>0&&fl<1?1:0);tr('swirl',p[0],p[1],1+fl,1+fl,fl*720);
  $('icam').setAttribute('transform',`translate(360,640) rotate(${fl*200}) scale(${Z*(1+fl*.6)}) translate(${-cx},${-cy})`);
  const on=T>=E.intestine+.1;show('lbInt',on?1:0);if(on)$('lbInt').setAttribute('transform',`translate(190,110) scale(${eob(P(T,E.intestine+.1,E.intestine+.4))})`);}
// ---------------- hook: the patient's face ----------------
function renderFace(T){
  const chew=T<.12||(T>.62&&T<.7)?Math.abs(Math.sin(T*22)):0, bub=P(T,.12,.5), popped=T>=.5;
  let m='M-12,0 Q0,3 12,0';let fill='none';
  if(chew>.3){m='M-12,0 Q0,-5 12,0 Q0,12 -12,0Z';fill='#5e1a20';}
  if(T>=.12&&T<.5){m='M-5,1 a5,5 0 1,0 10,0 a5,5 0 1,0 -10,0';fill='#5e1a20';}
  if(T>=.5&&T<.62){m='M-14,-1 Q0,-6 14,-1 Q0,16 -14,-1Z';fill='#5e1a20';}
  const fm=$('fMouth');fm.setAttribute('d',m);fm.setAttribute('fill',fill);
  show('fGumIn',chew>.3?1:0);$('fGumIn').setAttribute('d','M-8,3 Q0,0 8,3 Q0,9 -8,3Z');
  show('bubG',T>=.12&&T<.5?1:0);$('bubC').setAttribute('r',1+eo(bub)*58);$('bubC').setAttribute('cy',140+eo(bub)*10);
  const r=1+eo(bub)*58;$('bubHi').setAttribute('d',`M${-2-r*.55},${150-r*.35} A${r*.7},${r*.7} 0 0 1 ${-2-r*.1},${150-r*.7}`);
  show('popG',popped&&T<.8?1:0);$('popG').setAttribute('transform',`translate(0,${(T-.5)*20})`);
  const gulp=P(T,.68,.95);show('lump',gulp>0&&gulp<1?1:0);$('lump').setAttribute('cy',165+gulp*40);
  const wide=T>=.68;setHEye('fEyeL',0,T>=.5&&T<.6?.85:0);setHEye('fEyeR',0,T>=.5&&T<.6?.85:0);
  ['fEyeL','fEyeR'].forEach(e=>{$(e).setAttribute('transform',`scale(${wide?1.25:1},${wide?1.35:1})`);});
  $('fBrows').setAttribute('transform',`translate(0,${wide?-6:0})`);
  const z=1+Math.pow(P(T,.82,IN0),2)*5.5;$('fcam').setAttribute('transform',`translate(353,776) scale(${z}) translate(-353,-776)`);
  show('fdark',P(T,.88,IN0));}
// ---------------- ending: the gum on its wrapper ----------------
function renderSting(T){const up=T>=E.cta+.15;
  $('gcam').setAttribute('transform',`translate(360,760) scale(${1.85+.08*P(T,T_STING,END)}) translate(-360,-815)`);
  tr('sgum',0,Math.sin(T*2)*3);
  ['sgumE1','sgumE2'].forEach((e,k)=>setOEye(e,9,{dx:up?0:-10,dy:up?-40:30,lid:up?.1:.48,tilt:(k?-1:1)*(up?0:-12),blink:blinkK(T,1.2)}));
  setBrow('sgumB1',-10,-19,10,up?0:-14,2);setBrow('sgumB2',11,-19,10,up?0:14,2);setMouthV('sgum_m',speak('gum',T),6.5,up?1:-1,T,4);
  const ck=P(T,E.cta,E.cta+.35);show('cta',T>=E.cta?1:0);
  $('cta').setAttribute('transform',`translate(360,${200+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`);$('cta_i').setAttribute('transform',`scale(${eob(ck)})`);}
// ---------------- clinic ----------------
function renderS2(T){
  const dT=speak('doctor',T),pT=speak('patient',T),d0=ST['15_doctor'];
  let dr=2+(dT>.15?Math.sin(T*6.5)*1.8*dT:0);const shk=P(T,d0,d0+.9);if(shk>0&&shk<1)dr+=Math.sin(shk*Math.PI*4)*3.5;
  tr('docHead',0,Math.sin(T*1.3)*1.2-(dT>.7?1.5:0),1,1,dr);$('dBrows').setAttribute('transform',`translate(0,${dT>.72?-3.5:0})`);
  let pr=-3+Math.sin(T*.8);if(T>=E.gut)pr+=Math.sin(P(T,E.gut,E.gut+1)*Math.PI*2)*4;tr('patHead',0,Math.sin(T*1.5+1)*1.2,1,1,pr);
  const surprised=T>=E.bezoar&&T<E.gut+.3;
  $('pBrows').setAttribute('d',surprised?'M-36,64 Q-24,56 -10,60 M8,60 Q22,56 34,64':'M-36,66 Q-24,64 -10,60 M8,60 Q22,64 34,66');
  setMouthV('doc_m',dT,10,.7,T,5);setMouthV('pat_m',pT,10,-.5,T,6);
  setHEye('dEyeL',3,blinkK(T,.7));setHEye('dEyeR',3,blinkK(T,.7));setHEye('pEyeL',-3,blinkK(T,2.1));setHEye('pEyeR',-3,blinkK(T,2.1));
  const down=eio(P(T,d0+1.2,d0+2.0));const sh=[-84,234],el=[lerp(-124,-102,down),lerp(338,370,down)],wr=[lerp(-30,-90,down),lerp(408,470,down)];
  const d=limbD([sh,el,wr],[44,38,32]);$('patArmLD').setAttribute('d',d);$('patArmLO').setAttribute('d',d);
  $('patHandL').innerHTML=hand(wr[0],wr[1]+(down>.5?12:0),lerp(-25,-8,down),1.2,PSK);
  $('docArmR').setAttribute('transform',`rotate(${(dT>.75&&Math.floor(T*2)%3===0)?-7:0},86,226)`);$('clkM').setAttribute('transform',`rotate(${T*6})`);
  const pa=ST['14_patient'],pq=eio(P(T,pa,pa+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,E.bezoar)+.07*pq,cx=lerp(360,430,pq),cy=lerp(640,600,pq);
  const pk=eio(P(T,E.bezoar-.15,E.bezoar+.15))*(1-eio(P(T,E.gut+.5,E.gut+.85)));z=lerp(z,1.42,pk);cx=lerp(cx,232,pk);cy=lerp(cy,430,pk);
  $('ccam').setAttribute('transform',`translate(360,${lerp(640,560,pk)}) scale(${z}) translate(${-cx},${-cy})`);
  const b1=T>=E.passes-.3&&T<E.danger-.3,b2=T>=E.clump-.4&&T<E.bezoar-.15;$('bub').setAttribute('opacity',(b1||b2)?1:0);
  if(b1||b2){const k=b1?P(T,E.passes-.3,E.passes):P(T,E.clump-.4,E.clump-.1);$('bub').setAttribute('transform',`translate(265,150) scale(${1.12*eob(k)}) translate(-265,-150)`);
    const rt=b1?lerp(E.kick,E.later,P(T,E.passes,E.danger-.4)):lerp(E.packStart+.1,E.blob+1.6,P(T,E.clump,E.bezoar-.3));renderWorld(rt);}
  popLabel('lbMyth',T,E.myth-.05,E.passes-.4,360,64);popLabel('lbBez',T,E.bezoar-.05,E.gut+.8,360,64);}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  if(T>=E.later&&T<E.intestine)w='';
  const c=$('cap'),big=KEY.test(w);c.textContent=w;c.style.fontSize=big?'56px':'44px';c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09));c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const face=T<IN0,sto=(T>=IN0&&T<E.later)||(T>=E.packStart&&T<T_CLINIC),later=T>=E.later&&T<E.intestine,gut=T>=E.intestine&&T<E.packStart,cli=T>=T_CLINIC&&T<T_STING,sting=T>=T_STING;
  [['sx',face],['s1',sto],['sL',later],['s3',gut],['s2',cli],['sg',sting]].forEach(([id,v])=>$(id).setAttribute('display',v?'inline':'none'));
  show('indark',0);
  if(face)renderFace(T);
  if(sto)renderStomach(T);
  if(later){const k=eob(P(T,E.later,E.later+.3));$('laterT').setAttribute('transform',`translate(360,640) scale(${k}) translate(-360,-640)`);}
  if(gut)renderGut(T);
  if(cli){renderWorld(E.blob+1.6);renderS2(T);}
  if(sting)renderSting(T);
  if(sto&&T>=E.packStart&&T<E.packStart+.25)show('indark',1-P(T,E.packStart,E.packStart+.25));
  caption(T);};
window.render(0);

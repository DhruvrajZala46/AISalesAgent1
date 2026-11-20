// =============== 005: constipation from eating without water - remake of the 27M reference, our AI art + our engine ===============
const A=window.ART, E=D.ev, ST=D.start, END=D.end;
const KEY=/^(FOOD|STICK|STUCK|WATER|SODA|SODA'S|NOT|AGAIN|LAST|INTESTINES|YOUR|ROCK|POOPED|WEEK|CONSTIPATION|FIBER|HARD|DRY|PUSH|DRINK|VEGGIES|LEAVING)$/;
//__VISEME__
function actorSVG(id){return `<g id="${id}"><image id="${id}_img" preserveAspectRatio="none"/><g id="${id}_mg">${mouthEl(id+'_m',0,0)}</g></g>`;}
const lastPose={};
function placeActor(id,pose,fx,fy,H,o={}){
  const m=A[pose], w=H*m.w/m.h, x0=-w/2, y0=-H; let file=pose; const V=m.variants||[];
  if(V.length){const env=o.env||0, f=Math.floor((o.T||0)*15)+(o.seed||0); let open=env>0.12; if(open&&env<0.45&&f%3===0) open=false; file=pose+'_'+(open&&V.includes('o')?'o':'c');}
  const im=$(id+'_img'); if(lastPose[id]!==file){im.setAttribute('href','art/'+file+'.png');lastPose[id]=file;}
  im.setAttribute('x',x0.toFixed(1)); im.setAttribute('y',y0.toFixed(1)); im.setAttribute('width',w.toFixed(1)); im.setAttribute('height',H.toFixed(1));
  $(id).setAttribute('transform',`translate(${fx.toFixed(1)},${fy.toFixed(1)}) rotate(${(o.rot||0).toFixed(2)}) scale(${(o.sx||1).toFixed(4)},${(o.sy||1).toFixed(4)})`);
  $(id+'_mg').setAttribute('opacity',0);
}
function key(T,ks){if(T<=ks[0][0])return ks[0][1];for(let i=1;i<ks.length;i++){if(T<ks[i][0]){const k=eio(P(T,ks[i-1][0],ks[i][0]));const a=ks[i-1][1],b=ks[i][1];return Array.isArray(a)?a.map((v,j)=>lerp(v,b[j],k)):lerp(a,b,k);}}return ks[ks.length-1][1];}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
function along(pts,s){s=clamp(s)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;return [lerp(pts[i][0],pts[i+1][0],f),lerp(pts[i][1],pts[i+1][1],f)];}
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x);}
const IMG=(f)=>`<image href="art/${f}" x="-5.5" y="0" width="731" height="1280" preserveAspectRatio="none"/>`;
const SPR=(id)=>`<image id="${id}" preserveAspectRatio="none"/>`;
function placeImg(id,f,cx,by,H,o={}){const m=A[f],w=H*m.w/m.h,el=$(id);if(el.dataset.f!==f){el.setAttribute('href','art/'+f+'.png');el.dataset.f=f;}
  el.setAttribute('x',(-w/2).toFixed(1));el.setAttribute('y',(-H).toFixed(1));el.setAttribute('width',w.toFixed(1));el.setAttribute('height',H.toFixed(1));
  el.setAttribute('transform',`translate(${cx.toFixed(1)},${by.toFixed(1)}) rotate(${(o.rot||0).toFixed(1)}) scale(${(o.s||1).toFixed(3)})`);el.setAttribute('opacity',o.op===undefined?1:o.op);}
// ---------- geometry (world = 720x1280 frame) ----------
const STO=[382,1052,690];                 // stomach mom feet x, y, height
const PIPE=[[180,350],[184,385],[218,436],[251,498],[262,600],[262,741],[280,793],[313,850],[352,900]];   // food pipe top -> (behind the head) -> down the cavity wall -> the food
const SODA1=[[180,370],[218,436],[251,498]], SODA2=[[261,741],[280,793],[313,850],[352,888]];
const HEAP=[355,948,140];                 // food heap feet x, y, height
const GRIP=[376,742];                     // where the gripping hands hold the stick
const ROCK=[360,1090,390], SOFT=[372,744,250];
// ---------- SCENE 1: the stomach (Mom) ----------
const FOODS=['food_burger','food_drum','food_egg','food_fries'];
let S1=`<g id="s1"><g id="cam1"><g id="wStomach">${IMG('plate_abdomen.jpg')}
  ${actorSVG('sto')}
  <path id="sodaPipe" fill="none" stroke="#4a2414" stroke-width="24" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>
  <path id="sodaPipeHi" fill="none" stroke="#4a2414" stroke-width="26" stroke-linecap="round" stroke-linejoin="round" opacity="0"/>
  ${SPR('heap')}
  <g id="flood" opacity="0"><ellipse id="floodE" cx="355" cy="905" rx="150" ry="52" fill="#5a2c16" stroke="#2c140a" stroke-width="4"/><ellipse id="floodHi" cx="335" cy="888" rx="80" ry="12" fill="#a0603a" opacity=".6"/><g id="fizz"></g></g>
  <g id="items">${Array.from({length:12},(_,i)=>SPR('it'+i)).join('')}</g>
  <g id="stick" opacity="0"><g id="stickA"><rect x="-10" y="-46" width="20" height="270" rx="10" fill="#b8814a" stroke="#4a2a18" stroke-width="5"/><path d="M-3,-36 v250" stroke="#e0b07a" stroke-width="4" opacity=".7"/></g></g>
  <g id="snapTop" opacity="0"><rect x="-10" y="-46" width="20" height="140" rx="10" fill="#b8814a" stroke="#4a2a18" stroke-width="5"/><path d="M-10,94 l6,-10 l6,8 l8,-9" fill="none" stroke="#4a2a18" stroke-width="4"/></g>
  <g id="snapBot" opacity="0"><rect x="-10" y="0" width="20" height="130" rx="10" fill="#b8814a" stroke="#4a2a18" stroke-width="5"/><path d="M-10,4 l6,8 l6,-8 l8,9" fill="none" stroke="#4a2a18" stroke-width="4"/></g>
  <g id="splinters"></g>
  <g id="ring" opacity="0">${[0,1,2].map(i=>`<path d="M${-30-i*16},${-34-i*10} q${-14-i*6},${22+i*6} 0,${48+i*14}" fill="none" stroke="#ffd21f" stroke-width="7" stroke-linecap="round"/>`).join('')}</g>
 </g></g>
 ${labelBox('lbSto','STOMACH',560,300,24)}
</g>`;
// ---------- Timmy's brain on the phone (inset bubble, top-left like the reference) ----------
let INSET=`<g id="bInset" opacity="0"><circle r="134" fill="none" ${LN}/><circle r="129" fill="#fff"/><clipPath id="bClip"><circle r="122"/></clipPath>
  <g clip-path="url(#bClip)"><circle r="122" fill="#fdeee8"/>${actorSVG('brn')}</g><circle r="122" fill="none" ${LN2}/></g>`;
// ---------- SCENE 2: the rectum ----------
let S2=`<g id="s2"><g id="cam2"><g id="wRectum">${IMG('plate_rectum.jpg')}
  <g id="dust"></g>${actorSVG('rock')}${actorSVG('poo2')}<g id="drops"></g><g id="water" opacity="0"></g></g></g>
 ${labelBox('lbRect','LARGE INTESTINE',360,140,26)}
 <g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g>
</g>`;
// ---------- SCENE 3: the bathroom ----------
let S3=`<g id="s3"><g id="cam3"><g id="wBath">${IMG('plate_bathroom.jpg')}${actorSVG('boy')}<g id="sweat"></g><g id="strainLines"></g></g></g></g>`;
// ---------- SCENE 4: the clinic ----------
let S4=`<g id="s4"><g id="ccam">${IMG('clinic_bg.jpg')}${actorSVG('doc')}${actorSVG('mom')}
 <g id="bub" opacity="0"><g transform="translate(360,250)"><ellipse rx="300" ry="196" fill="#fff" ${LN}/><clipPath id="bubClip"><ellipse rx="290" ry="186"/></clipPath>
   <g clip-path="url(#bubClip)"><use id="bubA" href="#wStomach" transform="scale(.62) translate(-345,-790)"/><use id="bubB" href="#wRectum" transform="scale(.62) translate(-360,-860)"/><use id="bubC" href="#wBath" transform="scale(.66) translate(-372,-760)"/></g>
   <ellipse rx="300" ry="196" fill="none" ${LN}/></g></g></g>
 ${labelBox('lbCon','CONSTIPATION',360,74,32)}
 <g id="lbTip" opacity="0" transform="translate(360,120)"><rect x="-290" y="-62" width="580" height="124" rx="14" fill="#fff" ${LN}/>
  <circle cx="-256" cy="-22" r="22" fill="#2fa36b" ${LN2}/><path d="M-267,-22 l8,8 l15,-16" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
  <text class="lbl" style="font-size:36px" x="26" y="-8" text-anchor="middle">DRINK WATER EVERY DAY</text><text class="lbl" style="font-size:28px" x="0" y="40" text-anchor="middle">EAT FIBER  •  LESS SODA</text></g>
</g>`;
// =============== assemble ===============
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter>${DEFS}</defs>`
 +S1+S2+S3+S4+INSET+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
// =============== timing ===============
const T_RECT=E.rectum, T_BATH=E.bath, T_CLINIC=E.clinic, T_STING=E.stinger;
const NIT=12, ITEM=[...Array(NIT)].map((_,i)=>({f:FOODS[i%4],t0:E.food+i*.05,dur:.5+rnd(i)*.12,x:300+rnd(i+20)*110,y:905+rnd(i+40)*24,h:62+rnd(i+60)*22,r:rnd(i+80)*360}));
function renderStomach(T){
  const s02=ST['02_stomach'],s03=ST['03_stomach'],s06=ST['06_stomach'],s09=ST['09_stomach'],s10=ST['10_stomach'];
  const [sp,s0]=poseAt(T,[[s02-.1,E.stuck,'mom_grip'],[E.stuck,E.ring,'mom_strain'],[E.ring,s06-.1,'mom_phone'],[s06-.1,ST['07_brain']+.1,'mom_yell'],
     [ST['07_brain']+.1,E.flood+.2,'mom_phone'],[E.flood+.2,E.stir2-.1,'mom_groan'],[E.stir2-.1,E.snap+.15,'mom_grip'],[E.snap+.15,s10-.1,'mom_despair'],[s10-.1,1e9,'mom_shove']],'stomach_mom');
  const se=speak('stomach',T), pk=popK(T,s0), land=Math.sin(clamp(P(T,E.land-.1,E.land+.3))*Math.PI);
  const strain=sp==='mom_strain'?Math.sin(T*34)*1.4:0, shove=sp==='mom_shove'?Math.sin(clamp(P(T,E.shove-.1,E.shove+.35))*Math.PI):0;
  placeActor('sto',sp,STO[0],STO[1],STO[2],{sy:1+Math.sin(T*3)*.01+se*.02-land*.05-pk*.04-shove*.05,sx:1+land*.03+pk*.05+shove*.03,rot:strain+(sp==='mom_strain'?-2:0),env:se,T,seed:3});
  // the food avalanche: 12 items fall down the food pipe, the heap grows as they land
  let landed=0;
  ITEM.forEach((it,i)=>{const k=(T-it.t0)/it.dur;
    if(k<=0||k>=1.25){$('it'+i).setAttribute('opacity',0); if(k>=1) landed++; return;}
    if(k>=1) landed++;
    const end=[it.x,it.y], p=k<1?(k<.75?along(PIPE.slice(0,6),k/.75):[lerp(PIPE[5][0],end[0],(k-.75)/.25),lerp(PIPE[5][1],end[1],(k-.75)/.25)]):end;
    placeImg('it'+i,it.f,p[0],p[1]+it.h*.5,it.h,{rot:it.r+k*300,op:k<1?1:1-(k-1)/.25});});
  const hk=clamp(landed/NIT), squeeze=eio(P(T,E.shove,E.squeeze+.4)), gone=T>=E.squeeze+.45;
  const hx=lerp(HEAP[0],205,squeeze), hy=lerp(HEAP[1],1030,squeeze), hs=Math.max(.001,(.35+.65*eob(hk))*(1-.75*squeeze));
  if(hk<=0||gone) $('heap').setAttribute('opacity',0); else placeImg('heap','food_heap',hx,hy,HEAP[2],{s:hs*(1+.03*Math.sin(T*2)),rot:squeeze*-25});
  // the stick: stirring, stuck, stirring again, SNAP
  const stirA=T>=s02+.3&&T<E.stuck, stuckA=T>=E.stuck&&T<E.ring-.2, stir2=T>=E.stir2&&T<E.snap;
  const stickOn=stirA||stuckA||stir2;
  show('stick',stickOn?1:0);
  if(stickOn){const ang=stirA?Math.sin((T-s02)*7.5)*16*(1-.7*P(T,E.stuck-.8,E.stuck)):(stuckA?Math.sin(T*40)*1.5:Math.sin((T-E.stir2)*9)*14);
    const pull=stuckA?-14*Math.abs(Math.sin(T*6)):0;
    $('stick').setAttribute('transform',`translate(${GRIP[0]},${GRIP[1]+pull}) rotate(${ang.toFixed(2)})`);}
  const sk=P(T,E.snap,E.snap+1.1), snapOn=T>=E.snap&&sk<1;
  show('snapTop',snapOn?1:0); show('snapBot',snapOn||(T>=E.snap&&T<s10+.2)?1:0);
  if(T>=E.snap&&T<s10+.2){const a=eo(clamp(sk));
    $('snapTop').setAttribute('transform',`translate(${GRIP[0]-a*230},${GRIP[1]-a*260+a*a*520}) rotate(${-a*540})`);
    $('snapBot').setAttribute('transform',`translate(${GRIP[0]+8},${GRIP[1]+96+a*30}) rotate(${a*28})`);
    let h='';for(let i=0;i<6;i++){const k=P(T,E.snap,E.snap+.5);if(k>0&&k<1){const an=-Math.PI*(.1+.8*i/5);h+=`<rect x="${(GRIP[0]+Math.cos(an)*k*90).toFixed(1)}" y="${(GRIP[1]+150+Math.sin(an)*k*70+k*k*40).toFixed(1)}" width="10" height="4" fill="#b8814a" stroke="#4a2a18" stroke-width="1.5" opacity="${(1-k).toFixed(2)}" transform="rotate(${i*40},${GRIP[0]},${GRIP[1]+150})"/>`;}}
    $('splinters').innerHTML=h;} else $('splinters').innerHTML='';
  // phone ring lines by the mom's phone
  const ringOn=T>=E.ring&&T<ST['04_stomach']-.05; show('ring',ringOn&&Math.floor(T*8)%2===0?1:0);
  if(ringOn) $('ring').setAttribute('transform',`translate(${168+Math.sin(T*60)*3},560)`);
  // SILENT GAG: soda pours down the food pipe, floods the food (fizz), drains away
  const pk2=P(T,E.pour,E.flood), dk=P(T,E.drain,E.dry), pipeOn=T>=E.pour&&T<E.drain+.3;
  ['sodaPipe','sodaPipeHi'].forEach(id=>show(id,pipeOn?(1-P(T,E.flood+.4,E.drain+.3)):0));
  if(pipeOn){const L=900;[['sodaPipe',SODA1,P(T,E.pour,E.pour+.45)],['sodaPipeHi',SODA2,P(T,E.pour+.35,E.flood)]].forEach(([id,pts,k])=>{
      const d='M'+pts.map((q,i)=>(q[0]+Math.sin(T*9+i)*2).toFixed(1)+','+q[1].toFixed(1)).join(' L');$(id).setAttribute('d',d);$(id).setAttribute('stroke-dasharray',`${(eo(k)*L).toFixed(0)} ${L}`);});}
  const fl=T>=E.flood-.05&&T<E.dry+.2; show('flood',fl?1:0);
  if(fl){const up=eob(P(T,E.flood-.05,E.flood+.4)), down=eio(dk);
    $('floodE').setAttribute('rx',(150*up*(1-.55*down)).toFixed(1)); $('floodE').setAttribute('ry',(54*up*(1-.85*down)).toFixed(1)); $('floodE').setAttribute('cy',(905+35*down).toFixed(1));
    $('floodHi').setAttribute('opacity',(.6*up*(1-down)).toFixed(2));
    let h='';for(let i=0;i<14;i++){const u=((T*1.4)+rnd(i))%1,x=250+rnd(i+5)*210,y=905-u*120;h+=`<circle cx="${(x+Math.sin(T*5+i)*6).toFixed(1)}" cy="${y.toFixed(1)}" r="${(4+rnd(i+9)*7).toFixed(1)}" fill="none" stroke="#f4d9b0" stroke-width="2.5" opacity="${((1-u)*(1-down)*up).toFixed(2)}"/>`;}
    $('fizz').innerHTML=h;}
}
function renderInset(T){
  const on=T>=E.bubble&&T<E.pour+.6; show('bInset',on?1:0); if(!on) return;
  const k=eob(P(T,E.bubble,E.bubble+.3))*(1-eio(P(T,E.pour+.3,E.pour+.6)));
  $('bInset').setAttribute('transform',`translate(170,212) scale(${k.toFixed(3)})`);
  const be=speak('brain',T), pose=T>=E.gulp-.1?'brain_soda':(T>=ST['07_brain']-.1?'brain_eyeroll':'brain_timmy');
  const gl=pose==='brain_soda'?Math.sin(T*16)*.03:0;
  placeActor('brn',pose,6,150,262,{sy:1+be*.03+Math.sin(T*2.6)*.012+gl,rot:pose==='brain_soda'?-6+Math.sin(T*8)*2:0,env:be,T,seed:7});
}
function renderRectum(T,o={}){
  const st=T>=T_STING;
  // the rock drops in (thud, dust), sits stuck at the exit; in the stinger water splashes on it and it slides out soggy
  const dk=P(T,E.rockdrop,E.rockland), ry=T<E.rockland?lerp(-120,ROCK[1],dk*dk):ROCK[1];
  const thud=Math.sin(clamp(P(T,E.rockland,E.rockland+.3))*Math.PI);
  let rp='rock_base',rx=ROCK[0],ryy=ry,rs=1;
  if(st){rp=T>=E.slide?'rock_soggy':'rock_panic'; if(T>=E.slide){const k=eio(P(T,E.slide,E.slide+1.2)); ryy=ROCK[1]+k*520; rs=1-.25*k;}}
  const re=speak('rockpoop',T);
  placeActor('rock',rp,rx+(rp==='rock_panic'?Math.sin(T*30)*3:0),ryy,ROCK[2]*rs,{sy:1-thud*.12+re*.02+Math.sin(T*2)*.008,sx:1+thud*.1,env:re,T,seed:4});
  // the soft poop slides down from the top and pushes
  const sk=P(T,E.softin,E.softin+.9), sy=lerp(-160,SOFT[1],eob(sk)), push=Math.max(0,Math.sin(T*7))*.04;
  const se=speak('softpoop',T); const sfollow=st&&T>=E.slide?eio(P(T,E.slide+.4,E.slide+1.6))*560:0;
  const aside=st?eio(P(T,T_STING,T_STING+.6)):0;
  placeActor('poo2','soft_base',SOFT[0]+aside*150-(st&&T>=E.slide?eio(P(T,E.slide+.4,E.slide+1.6))*150:0),sy+sfollow+aside*120,SOFT[2],{sy:1-push+se*.03,sx:1+push*.6,rot:-4+Math.sin(T*7)*2,env:se,T,seed:2});
  show('poo2',T>=E.softin?1:0);
  // dust when the rock lands
  const dd=P(T,E.rockland,E.rockland+.8); if(dd>0&&dd<1){let h='';for(let i=0;i<8;i++){const a=Math.PI*(1+i/7),r=60+dd*120;h+=`<circle cx="${(ROCK[0]+Math.cos(a)*r*1.4).toFixed(1)}" cy="${(ROCK[1]-20+Math.sin(a)*r*.35).toFixed(1)}" r="${(16+dd*20).toFixed(1)}" fill="#c9a07a" opacity="${(.6*(1-dd)).toFixed(2)}"/>`;}$('dust').innerHTML=h;} else $('dust').innerHTML='';
  // doctor replay: water pulled OUT of the stool into the walls (blue drops flying outward)
  const pull=o.pull||0; if(pull>0){let h='';for(let i=0;i<14;i++){const u=((pull*1.6)+rnd(i))%1,side=i%2?1:-1,x=ROCK[0]+side*(40+u*230),y=ROCK[1]-120-rnd(i+3)*180-u*30;
      h+=`<path d="M${x.toFixed(1)},${(y-24).toFixed(1)} c14,17 17,31 0,38 c-17,-7 -14,-21 0,-38z" fill="#5ab4f0" stroke="#1d5f8f" stroke-width="2" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}$('drops').innerHTML=h;} else $('drops').innerHTML='';
  // stinger: a stream of water splashes down on the rock
  const wo=st&&T>=E.splash-.1&&T<E.slide+.6; show('water',wo?1:0);
  if(wo){const k=eo(P(T,E.splash-.1,E.splash+.3));let h=`<path d="M${ROCK[0]-22},-10 L${ROCK[0]+22},-10 L${ROCK[0]+16},${(k*(ROCK[1]-ROCK[2]+30)).toFixed(1)} L${ROCK[0]-16},${(k*(ROCK[1]-ROCK[2]+30)).toFixed(1)} Z" fill="#7cc8f4" stroke="#1d5f8f" stroke-width="3" opacity=".85"/>`;
    for(let i=0;i<12;i++){const u=((T*1.8)+rnd(i))%1,a=-Math.PI*(.1+.8*rnd(i+7));h+=`<circle cx="${(ROCK[0]+Math.cos(a)*u*170).toFixed(1)}" cy="${(ROCK[1]-ROCK[2]+40+Math.sin(a)*u*90+u*u*120).toFixed(1)}" r="${(5+rnd(i)*6).toFixed(1)}" fill="#7cc8f4" stroke="#1d5f8f" stroke-width="1.5" opacity="${(1-u).toFixed(2)}"/>`;}
    $('water').innerHTML=h;}
  return thud;
}
function renderBath(T){
  const be=speak('boy',T), k=P(T,T_BATH,T_CLINIC);
  placeActor('boy','boy_toilet',BOY[0]+Math.sin(T*38)*1.6,BOY[1],BOY[2],{sy:1+Math.sin(T*5)*.01-Math.abs(Math.sin(T*3))*.015+be*.01,env:be,T,seed:5});
  let h='';for(let i=0;i<4;i++){const u=((T*.9)+i/4)%1;const side=i%2?1:-1;h+=`<path d="M${(BOY[0]+side*(70+i*8)).toFixed(1)},${(BOY[1]-BOY[2]*.86+u*80).toFixed(1)} c5,8 7,14 0,18 c-7,-4 -5,-10 0,-18z" fill="#9fd8f7" stroke="#2a6f9a" stroke-width="2" opacity="${Math.sin(u*Math.PI).toFixed(2)}"/>`;}
  $('sweat').innerHTML=h;
  let s='';if(Math.floor(T*6)%2===0)for(let i=0;i<3;i++){const a=-.9+i*.45;s+=`<path d="M${(BOY[0]+150*Math.cos(a-1.57)).toFixed(1)},${(BOY[1]-BOY[2]*.8+150*Math.sin(a-1.57)).toFixed(1)} l${(14*Math.cos(a-1.57)).toFixed(1)},${(14*Math.sin(a-1.57)).toFixed(1)}" stroke="#e0454f" stroke-width="6" stroke-linecap="round"/>`;}
  $('strainLines').innerHTML=s;
}
const BOY=[372,1190,820];
function renderClinic(T){
  const dT=speak('doctor',T), mT=speak('mom',T), d0=ST['16_doctor'], m0=ST['15_mom'];
  const dpose=T>=E.drink-.2?'doc_point':(T>=E.pulls-.15?'doc_explain':'doc_base');
  placeActor('doc',dpose,DOC[0],DOC[1],DOC[2],{rot:dT>.15?Math.sin(T*6.5)*.6*dT:0,sy:1+Math.sin(T*1.3)*.006+dT*.012,env:dT,T,seed:5});
  placeActor('mom','mom_boy',MOMB[0],MOMB[1],MOMB[2],{sy:1+Math.sin(T*1.4+1)*.006+mT*.01,rot:T<d0&&mT>.2?Math.sin(T*7)*.4:0,env:mT,T,seed:6});
  const pq=eio(P(T,m0,m0+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,T_STING)+.08*pq, cx=lerp(360,500,pq), cy=lerp(640,620,pq);
  const pk=eio(P(T,E.constipation-.15,E.constipation+.15))*(1-eio(P(T,E.soda-.45,E.soda-.1)));
  z=lerp(z,1.45,pk); cx=lerp(cx,DOC[0]+40,pk); cy=lerp(cy,640,pk);
  const ty=lerp(640,600,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // thought-bubble replays cut on the doctor's words: soda floods the food / water pulled out of the stool / it hurts to push
  const sA=E.soda-.15, sB=E.pulls-.15, sC=E.hard-.3, sE=E.drink-.25, bOn=T>=sA&&T<sE;
  $('bub').setAttribute('opacity',bOn?1:0);
  if(bOn){const seg=T<sB?0:T<sC?1:2, t0=[sA,sB,sC][seg], t1=[sB,sC,sE][seg], u=P(T,t0,t1);
    const pop=seg===0?eob(P(T,sA,sA+.3)):1+.06*Math.sin(clamp(P(T,t0,t0+.25))*Math.PI);
    $('bub').setAttribute('transform',`translate(360,250) scale(${pop.toFixed(3)}) translate(-360,-250)`);
    show('bubA',seg===0?1:0); show('bubB',seg===1?1:0); show('bubC',seg===2?1:0);
    if(seg===0) renderStomach(lerp(E.pour-.2,E.dry+.3,u));
    else if(seg===1) renderRectum(lerp(ST['12_rockpoop'],ST['12_rockpoop']+2,u),{pull:u*3});
    else renderBath(lerp(ST['13_boy'],ST['14_boy']+1,u));}
  popLabel('lbCon',T,E.constipation-.05,E.soda-.2,360,74);
  popLabel('lbTip',T,E.drink-.1,T_STING,360,120);
}
const DOC=[168,1238,730], MOMB=[548,1252,770];
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z']/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_RECT?1:T<T_BATH?2:T<T_CLINIC?3:T<T_STING?4:5;
  ['s1','s2','s3','s4'].forEach((id,i)=>$(id).setAttribute('display',(sc===i+1||(sc===5&&id==='s2'))?'inline':'none'));
  let dark=0;
  if(sc===1){renderStomach(T);const c=1.05+.02*Math.sin(T*.3);$('cam1').setAttribute('transform',`translate(360,640) scale(${c}) translate(-366,-660)`);
    popLabel('lbSto',T,1.2,4.0,560,300); dark=Math.max(P(T,T_RECT-.18,T_RECT));}
  if(sc===2||sc===5){const thud=renderRectum(T); const z=sc===5?1.3+.05*eio(P(T,T_STING,T_STING+2)):1.3+.06*eio(P(T,ST['11_softpoop'],ST['12_rockpoop']+1.5));
    const sh=Math.sin(T*70)*8*thud; $('cam2').setAttribute('transform',`translate(${360+sh},640) scale(${z.toFixed(4)}) translate(-360,${-Math.min(800,1280-640/z).toFixed(1)})`);
    if(sc===2){popLabel('lbRect',T,T_RECT+.4,T_RECT+2.6,360,140); dark=Math.max(1-P(T,T_RECT,T_RECT+.18),P(T,T_BATH-.15,T_BATH));}
    else {show('lbRect',0); dark=1-P(T,T_STING,T_STING+.2);}
    const ck=P(T,E.cta,E.cta+.35); show('cta',sc===5&&T>=E.cta?1:0);
    $('cta').setAttribute('transform',`translate(360,${230+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);}
  if(sc===3){renderBath(T); const z=1.0+.1*eio(P(T,T_BATH,T_CLINIC)); $('cam3').setAttribute('transform',`translate(360,640) scale(${z}) translate(-360,${-Math.min(700,1280-640/z).toFixed(1)})`);
    dark=Math.max(1-P(T,T_BATH,T_BATH+.15),P(T,T_CLINIC-.2,T_CLINIC));}
  if(sc===4){renderClinic(T); dark=Math.max(1-P(T,T_CLINIC,T_CLINIC+.2),P(T,T_STING-.22,T_STING));}
  show('indark',dark*.9);
  if(sc===1) renderInset(T); else show('bInset',0);
  caption(T);
};
window.render(0);

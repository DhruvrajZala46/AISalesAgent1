// =============== 004: empty stomach before surgery - AI plates + sprites animated by our engine ===============
const A=window.ART, E=D.ev, ST=D.start, END=D.end;
const KEY=/^(BURGER|SURGERY|SLEEP|DOOR|UP|DOWN|ANESTHESIA'S|LIMP|PIPE|COUGH|ASLEEP|GAG|BURNING|ASPIRATION|PNEUMONIA|RELAXES|REFLEX|LUNGS|SIX|EIGHT|HOURS|AFTER|FOLLOW)$/;
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
  const mo=document.getElementById(id+'_mo');   // mouth-only layer drawn above things standing in front of the actor
  if(mo){const on=file!==pose; mo.setAttribute('display',on?'inline':'none');
    if(on){if(mo.dataset.f!==file){mo.setAttribute('href','art/'+file+'_m.png');mo.dataset.f=file;}
      ['x','y','width','height'].forEach(a=>mo.setAttribute(a,im.getAttribute(a))); $(id+'_mog').setAttribute('transform',$(id).getAttribute('transform'));}}
}
function key(T,ks){if(T<=ks[0][0])return ks[0][1];for(let i=1;i<ks.length;i++){if(T<ks[i][0]){const k=eio(P(T,ks[i-1][0],ks[i][0]));const a=ks[i-1][1],b=ks[i][1];return Array.isArray(a)?a.map((v,j)=>lerp(v,b[j],k)):lerp(a,b,k);}}return ks[ks.length-1][1];}
function poseAt(T,segs,def){let p=def,t0=0;for(const [a,b,q] of segs) if(T>=a&&T<b){p=q;t0=a;} return [p,t0];}
function popK(T,t0){const k=P(T,t0,t0+.18);return k<1?Math.sin(k*Math.PI):0;}
const IMG=(f)=>`<image href="art/${f}" x="-5.5" y="0" width="731" height="1280" preserveAspectRatio="none"/>`;
const ARROW_UP=`<path d="M-14,60 L-14,-10 L-32,-10 L0,-58 L32,-10 L14,-10 L14,60 Z" fill="#ffd21f" ${LN}/>`;
// ---------- SCENE 1: the stomach ----------
let S1=`<g id="s1"><g id="cam1"><g id="wStomach">${IMG('plate_abdomen.jpg')}
  ${actorSVG('sto')}
  <g id="doorRing" opacity="0"><g id="doorRing_i"><ellipse rx="46" ry="16" fill="none" stroke="#4a2a24" stroke-width="13"/><ellipse id="doorRingC" rx="46" ry="16" fill="none" stroke="#ffd21f" stroke-width="7"/></g></g>
  ${labelBox('lbDoor','DOOR',100,545,24)}
  <g id="splash" opacity="0"></g>
  ${actorSVG('bur')}<g id="sto_mog"><image id="sto_mo" preserveAspectRatio="none"/></g>
  <g id="arUp" opacity="0">${ARROW_UP}</g><g id="arDn" opacity="0"><g transform="rotate(180)">${ARROW_UP}</g></g>
 </g></g>
 <rect id="dim1" width="720" height="1280" fill="#141a3a" opacity="0"/>
 ${labelBox('lbSto','STOMACH',560,330,24)}
 <g id="lbSurg" opacity="0" transform="translate(360,150)"><rect x="-205" y="-30" width="410" height="60" rx="8" fill="#fff" ${LN}/><circle cx="-172" cy="0" r="19" fill="#fff" stroke="#e0454f" stroke-width="4"/><path d="M-172,-11 v11 l8,5" fill="none" stroke="#e0454f" stroke-width="3.5" stroke-linecap="round"/><text class="lbl" style="font-size:26px" x="18" y="9" text-anchor="middle">SURGERY IN 1 HOUR</text></g>
</g>`;
// ---------- SCENE 1b: the throat (003 plate) ----------
let S1b=`<g id="s1b"><g id="cam2"><g id="wThroat">${IMG('bg_throat.jpg')}${actorSVG('bur2')}</g></g>
 ${labelBox('lbFood','FOOD PIPE',560,640,22)}${labelBox('lbWind','WINDPIPE',230,640,22)}</g>`;
// ---------- SCENE 1c: the lungs ----------
let S1c=`<g id="s1c"><g id="cam3"><g id="wLungs">${IMG('plate_chest.jpg')}
  <ellipse id="burnGlow" cx="360" cy="780" rx="370" ry="270" fill="#ff5a2a" opacity="0" filter="url(#soft2)"/>
  ${actorSVG('lng')}<g id="puffs"></g><g id="steam"></g>${actorSVG('bur3')}</g></g>
 ${labelBox('lbLungs','LUNGS',590,440,24)}</g>`;
// ---------- brain inset (phone) ----------
let INSET=`<g id="bInset" opacity="0"><circle r="128" fill="none" ${LN}/><circle r="123" fill="#fff"/><clipPath id="bClip"><circle r="115"/></clipPath>
  <g clip-path="url(#bClip)"><circle r="115" fill="#ffe8de"/><circle r="115" fill="none" stroke="#f4c3b6" stroke-width="28" opacity=".6"/>${actorSVG('brn')}</g><circle r="115" fill="none" ${LN2}/>
  <g id="ring" opacity="0">${[0,1,2].map(i=>`<path d="M${136+i*14},${-40-i*10} q${16+i*6},${24+i*6} 0,${52+i*14} M${-136-i*14},${-40-i*10} q${-16-i*6},${24+i*6} 0,${52+i*14}" fill="none" stroke="#ffd21f" stroke-width="7" stroke-linecap="round"/>`).join('')}</g>
  <text id="zzz" class="cap" x="70" y="-70" style="font-size:40px" opacity="0">Zzz</text></g>`;
// ---------- SCENE 2: hospital ----------
let S2=`<g id="s2"><g id="ccam">${IMG('plate_hospital.jpg')}${actorSVG('pat')}${actorSVG('doc')}
 <g id="bub" opacity="0"><g transform="translate(360,250)"><ellipse rx="300" ry="196" fill="#fff" ${LN}/><clipPath id="bubClip"><ellipse rx="290" ry="186"/></clipPath>
   <g clip-path="url(#bubClip)"><use id="bubA" href="#wStomach" transform="scale(.66) translate(-340,-700)"/><use id="bubB" href="#wLungs" transform="scale(.66) translate(-360,-720)"/></g>
   <ellipse rx="300" ry="196" fill="none" ${LN}/></g></g></g>
 ${labelBox('lbAsp','ASPIRATION PNEUMONIA',360,64,26)}
 <g id="lbTip" opacity="0" transform="translate(360,80)"><rect x="-274" y="-27" width="548" height="54" fill="#fff" ${LN}/><circle cx="-244" cy="0" r="17" fill="#2fa36b" ${LN2}/><path d="M-252,0 l6,6 l11,-12" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><text class="lbl" style="font-size:22px" x="20" y="8" text-anchor="middle">NO FOOD 6-8 HOURS BEFORE SURGERY</text></g>
</g>`;
// ---------- SCENE G: stinger ----------
let SG=`<g id="sg"><g id="gcam">${IMG('plate_tray.jpg')}${actorSVG('bur4')}</g>
 <g id="cta" opacity="0"><g id="cta_i"><rect x="-250" y="-62" width="500" height="132" rx="26" fill="#fff" ${LN}/>
  <text class="cta" text-anchor="middle" y="6" style="font-size:66px;stroke-width:9px" fill="#ffd21f">FOLLOW</text>
  <text class="cta" text-anchor="middle" y="52" style="font-size:30px;stroke-width:6px" fill="#fff">FOR MORE BODY SECRETS</text></g></g></g>`;
// =============== assemble ===============
const svg=$('S');
svg.innerHTML=`<defs><filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="7"/></filter><filter id="soft2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>${DEFS}</defs>`
 +S1+S1b+S1c+S2+SG+INSET+`<rect id="indark" width="720" height="1280" fill="#1e1012" opacity="0"/><g id="capg"><text id="cap" class="cap" x="360" y="1110" text-anchor="middle"></text></g>`;
// =============== timing ===============
const LNG=[360,1000,530], BL=[368,590];
const T_THROAT=E.throat, T_LUNGS=E.lungs, T_CLINIC=E.clinic, T_STING=E.stinger;
const POOL=[414,962], BH=200, DOORS={stomach_base:[233,512,15],stomach_point:[233,512,15],stomach_panic:[233,512,15],stomach_drowsy:[262,505,25],stomach_asleep:[244,510,25]};
function renderStomach(T){
  // stomach
  const [sp,s0]=poseAt(T,[[ST['03_stomach']-.1,ST['04_burger']+1.2,'stomach_panic'],[ST['05_stomach']-.1,ST['06_burger']-.1,'stomach_point'],[E.drowsy-.1,E.asleep,'stomach_drowsy'],[E.asleep,1e9,'stomach_asleep']],'stomach_base');
  const se=speak('stomach',T), pk=popK(T,s0), land=Math.sin(clamp(P(T,.55,.85))*Math.PI);
  const breathe=sp==='stomach_asleep'?Math.sin(T*2.2)*.025:Math.sin(T*3)*.01;
  placeActor('sto',sp,382,1052,690,{sy:1+breathe+se*.02-land*.04-pk*.04,sx:1-breathe*.5+land*.03+pk*.05,rot:sp==='stomach_drowsy'?Math.sin(T*1.6)*2.5:(sp==='stomach_panic'?Math.sin(T*28)*.8:0),env:se,T,seed:3});
  // burger: falls down the food pipe into the juice, bobs, then floats back up when the door goes limp
  let bx,by,brot=0,bp='burger_base';
  if(T<.62){const k=P(T,0,.62);const pts=[[206,380],[214,470],[262,580],[340,700],[402,850],[414,962]];const s=k*k*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;
    bx=lerp(pts[i][0],pts[i+1][0],f);by=lerp(pts[i][1],pts[i+1][1],f);brot=lerp(-25,0,k);}
  else if(T<E.float){bx=POOL[0]+Math.sin(T*1.3)*8;by=POOL[1]+Math.sin(T*2.1)*5;brot=Math.sin(T*1.7)*4;}
  else {const k=P(T,E.float,T_THROAT+.05);const pts=[[414,962],[380,800],[300,640],[232,500],[208,380],[205,220]];const s=eio(k)*(pts.length-1);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;
    bx=lerp(pts[i][0],pts[i+1][0],f);by=lerp(pts[i][1],pts[i+1][1],f);brot=Math.sin(T*12)*10;bp='burger_scared';}
  const be=speak('burger',T); const bpk=popK(T,E.float);
  placeActor('bur',bp,bx,by,BH,{rot:brot,sy:1+be*.04+Math.sin(T*5)*.01-bpk*.05,sx:1+bpk*.05,env:be,T,seed:1});
  // splash when it lands
  const sk=P(T,.58,1.2); if(sk>0&&sk<1){let h='';for(let i=0;i<7;i++){const a=-Math.PI*(.15+.7*i/6),r=40+sk*110;h+=`<ellipse cx="${(POOL[0]+Math.cos(a)*r).toFixed(1)}" cy="${(POOL[1]-20+Math.sin(a)*r*.8+sk*sk*90).toFixed(1)}" rx="9" ry="12" fill="#cde34a" stroke="#4a2a24" stroke-width="2" opacity="${(1-sk).toFixed(2)}"/>`;}$('splash').innerHTML=h;show('splash',1);} else show('splash',0);
  // the door (the ring muscle where the food pipe meets the stomach): shown when it is named, then again when it goes limp
  const d1=T>=E.door-.05&&T<E.up+1.3, d2=T>=E.limp-.1&&T<E.float+.8;
  show('doorRing',d1||d2?1:0);
  if(d1||d2){const DOOR=DOORS[sp], t0=d1?E.door-.05:E.limp-.1, pop=eob(P(T,t0,t0+.25)), op=d2?eio(P(T,E.limp,E.limp+1.2)):0;
    $('doorRing').setAttribute('transform',`translate(${DOOR[0]},${DOOR[1]}) rotate(${DOOR[2]})`);
    $('doorRing_i').setAttribute('transform',`scale(${(pop*(1+op*.35+(d1?.06*Math.sin(T*9):.05*Math.sin(T*4)))).toFixed(3)},${(pop*(1+op*.6)).toFixed(3)})`);
    $('doorRingC').setAttribute('stroke',d2?'#ff4d4d':'#ffd21f'); $('doorRingC').setAttribute('stroke-dasharray',d2&&op>.3?'14 9':'none');}
  popLabel('lbDoor',T,E.door-.05,E.up+1.3,100,545); if(!d1) popLabel('lbDoor',T,E.limp-.1,E.float+.8,100,545);
  // arrows: UP along the food pipe, DOWN into the stomach
  const u=T>=E.up-.05&&T<E.up+1.3, d=T>=E.down-.05&&T<E.down+1.3;
  show('arUp',u?1:0); if(u) $('arUp').setAttribute('transform',`translate(250,${560-P(T,E.up,E.up+1.2)*60}) rotate(-20) scale(${eob(P(T,E.up-.05,E.up+.2))})`);
  show('arDn',d?1:0); if(d) $('arDn').setAttribute('transform',`translate(${POOL[0]+120},${700+P(T,E.down,E.down+1.2)*60}) scale(${eob(P(T,E.down-.05,E.down+.2))})`);
}
function renderThroat(T){
  const k=P(T,T_THROAT,T_LUNGS+.1);
  const pts=[[515,1380],[512,1080],[506,820],[488,720],[452,712],[425,790],[416,950],[414,1150],[414,1420]];
  const s=key(T,[[T_THROAT,0],[E.wrongpipe-.9,3.2],[E.wrongpipe-.2,5],[T_LUNGS+.1,8]]);const i=Math.min(pts.length-2,Math.floor(s)),f=s-i;
  const bx=lerp(pts[i][0],pts[i+1][0],f), by=lerp(pts[i][1],pts[i+1][1],f);
  const rot=s<3?Math.sin(T*12)*8:(s<5?lerp(0,170,(s-3)/2):170+Math.sin(T*10)*6);
  placeActor('bur2','burger_scared',bx,by+95,190,{rot,env:speak('burger',T),T,seed:1});
  const z=1.22, cx=430, cy=Math.min(1280-640/z,760);
  $('cam2').setAttribute('transform',`translate(360,640) scale(${z}) translate(${-cx},${-cy})`);
  popLabel('lbFood',T,T_THROAT+.2,T_LUNGS,560,640); popLabel('lbWind',T,E.wrongpipe-.5,T_LUNGS,230,640);
}
function renderLungs(T){
  const [lp,l0]=poseAt(T,[[E.cough1-.25,E.cant-.1,'lungs_strain'],[E.burn-.1,1e9,'lungs_burn']],'lungs_base');
  const le=speak('lungs',T), pk=popK(T,l0), hit=Math.sin(clamp(P(T,E.land,E.land+.35))*Math.PI);
  const strain=lp==='lungs_strain'?Math.sin(T*30)*1.2:0;
  placeActor('lng',lp,LNG[0],LNG[1],LNG[2],{sy:1+Math.sin(T*2.6)*.02+le*.02-hit*.06-pk*.04,sx:1-Math.sin(T*2.6)*.01+hit*.04+pk*.05,rot:strain,env:le,T,seed:4});
  // burger falls in from the windpipe and gets stuck at the split
  let bx=BL[0],by=key(T,[[T_LUNGS,-260],[E.land,BL[1]]]),brot=170+Math.sin(T*10)*6,bp='burger_scared';
  if(T>=E.land){bx=BL[0]+Math.sin(T*2)*3;by=BL[1]+Math.sin(T*3)*3;brot=lerp(170,0,eob(P(T,E.land,E.land+.5)));bp=T>=ST['11_burger']-.1?(T>=ST['13_burger']-.1?'burger_base':'burger_nervous'):'burger_scared';}
  if(T>=E.cough1&&T<E.cant){const c=Math.max(Math.sin(clamp(P(T,E.cough1,E.cough1+.4))*Math.PI),Math.sin(clamp(P(T,E.cough2,E.cough2+.4))*Math.PI));by-=c*12;}
  const rr=brot*Math.PI/180, bcy=by-85; placeActor('bur3',bp,bx-85*Math.sin(rr),bcy+85*Math.cos(rr),170,{rot:brot,env:speak('burger',T),T,seed:2});
  // weak cough puffs that fizzle
  let h='';[E.cough1,E.cough2].forEach((t0,j)=>{const k=P(T,t0,t0+.8);if(k>0&&k<1)for(let i=0;i<4;i++){const x=BL[0]+(i-1.5)*46,y=BL[1]-150-k*120-i*8;h+=`<circle cx="${x}" cy="${y.toFixed(1)}" r="${(14+k*22).toFixed(1)}" fill="#fff" opacity="${(.8*(1-k)).toFixed(2)}" stroke="#c9b9b4" stroke-width="2"/>`;}});
  $('puffs').innerHTML=h;
  const burn=clamp(P(T,E.burn-.1,E.burn+.6)); show('burnGlow',burn*(.45+.15*Math.sin(T*6)));
  let st='';if(burn>0)for(let i=0;i<5;i++){const u=((T*.6)+i/5)%1;const x=240+i*95+Math.sin(T*2+i)*10,y=760-u*260;st+=`<path d="M${x},${y.toFixed(1)} q14,-18 0,-36 q-14,-18 0,-36" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity="${(burn*.75*Math.sin(u*Math.PI)).toFixed(2)}"/>`;}
  $('steam').innerHTML=st;
  const sh=T>=E.land&&T<E.land+.3?Math.sin(T*80)*6*(1-P(T,E.land,E.land+.3)):0;
  const z3=1.04+.07*eio(P(T,T_LUNGS,E.burn))+.05*eob(P(T,E.burn-.05,E.burn+.3)), cy3=clamp(lerp(640,700,P(T,T_LUNGS,E.burn)),640/z3,1280-640/z3);
  $('cam3').setAttribute('transform',`translate(${360+sh},640) scale(${z3.toFixed(4)}) translate(-360,${(-cy3).toFixed(1)})`);
  popLabel('lbLungs',T,E.land+.1,E.land+2.6,590,440);
}
function renderInset(T){
  const a=T>=E.ring-.35&&T<E.lights+1.6, b=T>=E.asleepB-.4&&T<E.burn-.1, on=a||b;
  show('bInset',on?1:0); if(!on) return;
  const t0=a?E.ring-.35:E.asleepB-.4, t1=a?E.lights+1.6:E.burn-.1;
  const k=eob(P(T,t0,t0+.3))*(1-eio(P(T,t1-.3,t1)));
  const ringOn=T>=E.ring&&T<E.brain-.05, shk=ringOn?Math.sin(T*60)*5:0;
  $('bInset').setAttribute('transform',`translate(${172+shk},${a?190:200}) scale(${k.toFixed(3)})`);
  show('ring',ringOn&&Math.floor(T*8)%2===0?1:0);
  const be=speak('brain',T);
  placeActor('brn','brain_base',0,118,212,{sy:1+be*.03+Math.sin(T*2.6)*.01,env:be,T,seed:7,rot:b?Math.sin(T*1.5)*3:0});
  show('zzz',(b||T>=E.lights+.4)&&Math.floor(T*2)%2===0?1:0);
}
function renderS2(T){
  const dT=speak('doctor',T), pT=speak('patient',T), d0=ST['16_doctor'], pa=ST['15_patient'];
  const dpose=T>=E.six-.2?'doc_point':(T>=E.relaxes-.15?'doc_explain':'doc_base');
  placeActor('pat','pat_bed',474,1250,770,{sy:1+Math.sin(T*1.4)*.006+pT*.01,rot:T<d0&&pT>.2?Math.sin(T*7)*.4:0,env:pT,T,seed:6});
  placeActor('doc',dpose,188,1236,740,{rot:dT>.15?Math.sin(T*6.5)*.6*dT:0,sy:1+Math.sin(T*1.3)*.006+dT*.012,env:dT,T,seed:5});
  const pq=eio(P(T,pa,pa+1.5))*(1-eio(P(T,d0-.2,d0+.4)));
  let z=1+.035*P(T,d0,END)+.08*pq, cx=lerp(360,470,pq), cy=lerp(640,600,pq);
  const pk=eio(P(T,E.aspiration-.15,E.aspiration+.15))*(1-eio(P(T,E.relaxes-.35,E.relaxes)));
  z=lerp(z,1.5,pk); cx=lerp(cx,215,pk); cy=lerp(cy,640,pk);
  const ty=lerp(640,600,pk); cx=clamp(cx,360/z,720-360/z); cy=clamp(cy,ty/z,1280-(1280-ty)/z);
  $('ccam').setAttribute('transform',`translate(360,${ty}) scale(${z}) translate(${-cx},${-cy})`);
  // thought bubble replays, cut on the doctor's words: door goes limp / can't cough / food comes back up / lands in the lungs
  const sA=E.relaxes-.15, sB=E.shuts-.15, sC=E.came-.45, sD=E.slipped-.15, sE=E.six-.3, bOn=T>=sA&&T<sE;
  $('bub').setAttribute('opacity',bOn?1:0);
  if(bOn){const seg=T<sB?0:T<sC?1:T<sD?2:3, t0=[sA,sB,sC,sD][seg], t1=[sB,sC,sD,sE][seg], u=P(T,t0,t1);
    const pop=seg===0?eob(P(T,sA,sA+.3)):1+.06*Math.sin(clamp(P(T,t0,t0+.25))*Math.PI);
    $('bub').setAttribute('transform',`translate(360,250) scale(${pop.toFixed(3)}) translate(-360,-250)`);
    show('bubA',seg%2===0?1:0); show('bubB',seg%2===1?1:0);
    if(seg===0) renderStomach(lerp(E.drowsy+.5,E.asleep+.4,u));
    else if(seg===1) renderLungs(lerp(E.cough1-.3,E.cant+.3,u));
    else if(seg===2) renderStomach(lerp(E.float-.1,T_THROAT-.05,u));
    else {const r=T-t0; renderLungs(r<1.4?E.land-.5+r:Math.min(E.burn-.1+(r-1.4),E.burn+2.5));}}
  popLabel('lbAsp',T,E.aspiration-.05,E.relaxes-.2,360,64);
  popLabel('lbTip',T,E.six-.1,END,360,80);
  show('indark',Math.max(P(T,T_STING-.22,T_STING),1-P(T,T_CLINIC,T_CLINIC+.22))*.9);
}
function renderSting(T){
  const t=T-T_STING, be=speak('burger',T);
  placeActor('bur4','burger_sulk',352,905,300,{rot:Math.sin(T*1.3)*1.2,sy:1+Math.sin(T*2.1)*.012+be*.02,env:be,T,seed:2});
  const zin=1.06+.06*eio(P(t,0,2)); $('gcam').setAttribute('transform',`translate(360,640) scale(${zin}) translate(-360,${-Math.min(1280-640/zin,690)})`);
  const ck=P(T,E.cta,E.cta+.35); show('cta',T>=E.cta?1:0);
  $('cta').setAttribute('transform',`translate(360,${230+Math.sin(T*3)*4}) rotate(${Math.sin(T*2.2)*2})`); $('cta_i').setAttribute('transform',`scale(${eob(ck)})`);
  show('indark',(1-P(t,0,.22))*.9);
}
function caption(T){let w='',ws=0;for(const L of D.lines)for(const x of L.words){if(T>=x[0]&&T<Math.max(x[1],x[0]+.12)){w=x[2];ws=x[0];}}
  if(!w){for(const L of D.lines)for(const x of L.words){if(T>=x[1]&&T<x[1]+.12){w=x[2];ws=x[0];}}}
  const c=$('cap'),big=KEY.test(w.replace(/[^A-Z']/g,'')); c.textContent=w; c.style.fontSize=big?'56px':'44px'; c.style.fill=big?'#ffd21f':'#fff';
  const k=eo(P(T,ws,ws+.09)); c.setAttribute('transform',`translate(360,1110) scale(${lerp(1.2,1,k)}) translate(-360,-1110)`);}
window.render=function(T){
  const sc=T<T_THROAT?1:T<T_LUNGS?2:T<T_CLINIC?3:T<T_STING?4:5;
  ['s1','s1b','s1c','s2','sg'].forEach((id,i)=>$(id).setAttribute('display',sc===i+1?'inline':'none'));
  show('indark',0);
  if(sc===1){renderStomach(T);const c=1.04+.02*Math.sin(T*.3);$('cam1').setAttribute('transform',`translate(360,640) scale(${c}) translate(-366,-650)`);
    show('dim1',.26*eio(P(T,E.lights,E.lights+.9))*(1-eio(P(T,E.float+.6,T_THROAT))));
    popLabel('lbSto',T,1.0,4.2,560,330); popLabel('lbSurg',T,E.surgery-.05,E.surgery+2.4,360,150);
    show('indark',Math.max(1-P(T,0,.06),P(T,T_THROAT-.15,T_THROAT))*.9*(T<.06?0:1));}
  if(sc===2){renderThroat(T); show('indark',Math.max(1-P(T,T_THROAT,T_THROAT+.15),P(T,T_LUNGS-.12,T_LUNGS))*.9);}
  if(sc===3){renderLungs(T); show('indark',Math.max(1-P(T,T_LUNGS,T_LUNGS+.15),P(T,T_CLINIC-.25,T_CLINIC))*.9);}
  if(sc===4) renderS2(T);
  if(sc===5) renderSting(T);
  if(sc<=3) renderInset(T); else show('bInset',0);
  caption(T);
};
window.render(0);

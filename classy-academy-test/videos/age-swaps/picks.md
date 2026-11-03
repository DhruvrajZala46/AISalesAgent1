# picks - 8 Things That Quietly Age You (first pass from thumbnails; every clip checked inside before use)
# never reuse footage from the last two videos (oldclash.py) or the #1 video
hook cafe 60s: h_older2 h_older22 h_older1 h_older7 h_older23 h_older17 h_older16 h_older39
SKIP h_older3 h_older30 h_older31 h_older33 h_older35 h_older40 h_older42 h_older47 h_older48 h_older5
hook silver: h_silver1 h_silver4 h_silver5 h_silver6 h_silver9 h_silver10 h_silver16 h_silver17 h_silver19 h_silver21 h_silver22 h_silver23 h_silver30 h_silver32 h_silver34 h_silver35 h_silver36 h_silver43 h_silver44
SKIP h_silver3 h_silver11 h_silver25 h_silver27 h_silver29 h_silver40 h_silver42 h_silver46 h_silver47 h_silver24
hook sixty: h_sixty2 h_sixty3 h_sixty5 h_sixty9 h_sixty10 h_sixty11 h_sixty12 h_sixty13 h_sixty15 h_sixty16 h_sixty18 h_sixty19 h_sixty20 h_sixty22 h_sixty23 h_sixty24 h_sixty25 h_sixty27 h_sixty28 h_sixty30 h_sixty31 h_sixty32 h_sixty33 h_sixty34 h_sixty36 h_sixty37 h_sixty38 h_sixty39 h_sixty40 h_sixty44 h_sixty47 h_sixty48
SKIP h_sixty29 h_sixty43 h_sixty14 h_sixty49 h_sixty26
DUP h_sixty1=h_older7 h_sixty11=h_older1
hook fresh (real only; most results AI): h_fresh10 h_fresh21 h_fresh35 h_fresh40
SKIP h_fresh7 h_fresh12 h_fresh13 h_fresh14 h_fresh15 h_fresh18 h_fresh27 h_fresh29 h_fresh32 h_fresh36 h_fresh37 h_fresh41 h_fresh42 h_fresh43 h_fresh44 h_fresh48 h_fresh49 h_fresh23
DUP h_fresh0=h_older2 h_fresh3=h_older1 h_fresh22=h_older7 h_fresh1=h_older3
hook walk: h_walk1 h_walk6 h_walk10 h_walk17 h_walk23 h_walk25 h_walk26 h_walk27 h_walk29 h_walk30 h_walk33 h_walk35 h_walk37 h_walk38 h_walk43 h_walk45 h_walk46 h_walk48 h_walk49
DUP h_walk0=h_older7 h_walk12=h_sixty2 h_walk21=h_sixty21 h_walk28=h_sixty3 h_walk36=h_older23
SKIP h_walk22
film (real films only): h_film3 h_film7 h_film34 h_film21 h_film12 h_film22 h_film11 h_film16
SKIP h_film0 h_film4 h_film10 h_film13 h_film15 h_film20 h_film37 h_film38 h_film39 h_film41 h_film46 h_film48 h_film29 h_film24
p1 pooling at the ankle: t_pool5 t_pool10 t_pool27 t_pool32 t_pool39 t_pool16 t_pool42 t_pool15 t_pool18 t_pool46 t_pool37
p1 tailor / hem: t_hem0 t_hem4 t_hem5 t_hem7 t_hem18 t_hem9 t_hem3 t_hem2_24
DUP t_hem2_20=t_pool5 t_hem2_37=t_pool18 t_hem2_3=t_hem6
p1 straight-leg trousers (try-ons): t_straight1 t_straight11 t_straight13 t_straight16 t_straight21 t_straight23 t_straight25 t_straight26 t_straight30 t_straight31 t_straight35 t_straight44 t_straight47 t_straight42
p1 wool trousers walking (real only): t_wool10 t_wool14 t_wool21 t_wool30 t_wool36 t_wool40 t_wool42 t_wool46 t_wool47
SKIP t_wool0 t_wool18 t_wool23 t_wool26 t_wool31 t_wool33 t_wool34 t_wool37 t_wool45 t_wool48 t_wool49
DUP t_wool9=t_straight1
p1 tailor: t_tailor0 t_tailor1 t_tailor4 t_tailor8 t_tailor12 t_tailor39 t_tailor49
DUP t_tailor3=t_hem4 t_tailor9=t_hem7 t_tailor45=t_hem0 t_tailor47=t_hem18 t_tailor37=t_hem5
p2 ruffles / bow at the neck: b_ruffle7 b_ruffle10 b_bow2 b_bow3 b_bow6 b_bow10 b_bow11 b_bow12 b_bow37
p2 soft silk / satin blouse (real only; many AI): b_silk0 b_silk3 b_silk6 b_silk10 b_silk11 b_silk35 b_silk38 b_silk39 b_silk40 b_silk47 b_satin1 b_satin5 b_satin6 b_satin10 b_satin12 b_satin18 b_satin20 b_satin22 b_satin26 b_satin29 b_satin37 b_satin38 b_satin40 b_satin41
SKIP b_silk1 b_silk2 b_silk16 b_silk19 b_silk20 b_silk22 b_silk23 b_silk29 b_silk30 b_silk32 b_silk33 b_silk37 b_silk42 b_silk43 b_silk44 b_silk45 b_silk25 b_satin17 b_satin25 b_satin30 b_satin33 b_satin34 b_satin35 b_satin15
DUP b_silk13=b_satin10 b_silk27=b_satin12 b_silk3=b_satin3
p3 chunky roll neck: r_chunky0 r_chunky4 r_chunky11 r_chunky13 r_chunky14 r_chunky15 r_chunky16 r_chunky18 r_chunky31 r_chunky33 r_chunky40 r_chunky42 r_chunky2 r_chunky12
p3 fine turtleneck: r_fine0 r_fine3 r_fine5 r_fine6 r_fine7 r_fine12 r_fine18 r_fine19 r_fine21 r_fine24 r_fine32 r_fine36 r_fine39 r_fine41 r_fine11 r_fine27
p3 mock neck / fine: r_mock3 r_mock8 r_mock10 r_mock20 r_mock27 r_mock37 r_mock35 r_mock2
p3 bulky more: r_mock25 r_mock15 r_mock18 r_mock7 r_mock41 r_mock1
DUP r_mock5=r_fine36 r_mock9=r_fine6 r_mock12=r_fine12 r_mock22=r_fine23
p3 merino fine (real only): r_merino3 r_merino28 r_merino38 r_merino39 r_merino42 r_merino46 r_merino10 r_merino12 r_merino24 r_merino47 r_merino9
SKIP r_merino2 r_merino4 r_merino13 r_merino18 r_merino20 r_merino22 r_merino23 r_merino25 r_merino31 r_merino33 r_merino35 r_merino43 r_merino45 r_merino48
DUP r_merino0=r_chunky42 r_merino11=r_chunky33 r_merino14=r_fine21 r_merino15=r_fine6 r_merino40=r_fine32
guide colours (draping): g_drape8 g_drape9 g_drape11 g_drape19 g_drape21 g_drape38 g_drape40 g_drape45 g_drape2 g_drape6 g_drape30
guide shapes / mirror: g_ready4 g_ready16 g_ready28 g_ready43 g_ready44 g_ready45 g_ready15 g_ready29
guide necklines: g_neck28 g_neck34 g_neck17
p4 long slouchy cardigan: c_long0 c_long5 c_long7 c_long10 c_long12 c_long17 c_long18 c_long19 c_long26 c_long28 c_long31 c_long32 c_long34 c_long35 c_long39 c_long42 c_long43 c_long38
p4 stretched / sagging / construction: c_saggy0 c_saggy6 c_saggy10 c_saggy14 c_saggy21 c_saggy33 c_saggy44 c_saggy48 c_saggy24 c_saggy1
p4 fine-knit hip-length, buttoned: c_fine1 c_fine4 c_fine10 c_fine11 c_fine12 c_fine13 c_fine14 c_fine16 c_fine17 c_fine19 c_fine21 c_fine25 c_fine27 c_fine31 c_fine33 c_fine37 c_fine38 c_fine39 c_fine40 c_fine24
SKIP c_fine30
DUP c_saggy0=c_fine1
p4 draped over shoulders: c_shoulders0 c_shoulders1 c_shoulders2 c_shoulders12 c_shoulders17 c_shoulders21 c_shoulders26 c_shoulders29 c_shoulders11 c_shoulders31
p4 cardigan as a top / over silk: c_silk7 c_silk10 c_silk11 c_silk14 c_silk18 c_silk24 c_silk26 c_silk27 c_silk30 c_silk31 c_silk35 c_silk36 c_silk45
SKIP c_silk28 c_silk37 c_silk38 c_silk44
DUP c_silk2=c_saggy28 c_silk13=c_fine13 c_silk16=c_fine35 c_silk8=c_fine11 c_silk39=c_fine11
p5 words across the chest (women, real): s_slogan6 s_slogan7 s_slogan9 s_slogan13 s_slogan2 s_slogan31 s_slogan40 s_slogan46 s_slogan30 s_slogan34 s_slogan43
SKIP s_slogan10 s_slogan22 s_slogan26 s_slogan27 s_slogan28 s_slogan29 s_slogan32 s_slogan35 s_slogan36 s_slogan37 s_slogan39 s_slogan42 s_slogan44 s_slogan45 s_slogan3
p5 graphic tees: s_graphic13 s_graphic26 s_graphic29 s_graphic43 s_graphic38 s_graphic17
DUP s_graphic0=s_slogan4 s_graphic5=s_slogan1 s_graphic9=s_slogan16 s_graphic10=s_slogan0 s_graphic14=s_slogan31 s_graphic19=s_slogan14 s_graphic32=s_slogan19 s_graphic39=s_slogan34 s_graphic41=s_slogan6
p5 plain soft tee: s_plain0 s_plain3 s_plain6 s_plain10 s_plain13 s_plain14 s_plain17 s_plain20 s_plain24 s_plain27 s_plain28 s_plain32 s_plain35 s_plain39 s_plain44 s_plain45 s_plain5
SKIP s_plain26
p5 breton: s_breton0 s_breton2 s_breton5 s_breton7 s_breton10 s_breton13 s_breton16 s_breton17 s_breton19 s_breton20 s_breton21 s_breton22 s_breton34 s_breton35 s_breton37 s_breton44
p5 v-neck / scoop (real only): s_vneck0 s_vneck1 s_vneck10 s_vneck12 s_vneck22 s_vneck28 s_vneck29 s_vneck30 s_vneck34 s_vneck26 s_vneck2
SKIP s_vneck15 s_vneck18 s_vneck19 s_vneck20 s_vneck4 s_vneck31
p6 wide belt / big buckle (on women): w_wide5 w_wide10 w_wide17 w_wide18 w_wide21 w_wide34 w_wide13 w_wide20 w_buckle1 w_buckle29 w_buckle30 w_buckle31 w_buckle11
p6 slim / matte belt, tonal: w_wide3 w_wide7 w_wide38 w_wide43 w_wide30 w_buckle4 w_buckle15 w_buckle23 w_buckle33 w_buckle35 w_buckle44 w_buckle45 w_buckle9 w_buckle21
SKIP w_buckle2 w_buckle3 w_buckle6 w_buckle7 w_buckle8 w_buckle17 w_buckle22 w_buckle24 w_buckle25 w_buckle26 w_buckle38 w_buckle40 w_buckle42 w_buckle46 w_buckle47 w_wide12 w_wide29
DUP w_buckle0=w_wide5 w_buckle13=w_wide37 w_buckle18=w_wide20 w_buckle20=w_wide8 w_buckle45=w_wide38
p6 slim tonal belts on outfits: w_slim0 w_slim1 w_slim2 w_slim4 w_slim7 w_slim8 w_slim9 w_slim10 w_slim12 w_slim13 w_slim14 w_slim16 w_slim24 w_slim27 w_slim29 w_slim31 w_slim32 w_slim37 w_slim39 w_slim47 w_slim49
SKIP w_slim20 w_slim41 w_slim19
DUP w_slim6=w_buckle9 w_slim17=w_buckle4 w_slim18=w_wide6 w_slim21=w_buckle16 w_slim26=w_wide20 w_slim30=w_buckle34 w_slim40=w_wide37 w_slim42=w_wide13 w_slim45=w_buckle27 w_slim46=w_buckle44 w_slim48=w_buckle33
p6 wrap dress (real only; many AI): w_wrap0 w_wrap2 w_wrap9 w_wrap10 w_wrap13 w_wrap16 w_wrap19 w_wrap21 w_wrap41 w_wrap37
SKIP w_wrap4 w_wrap5 w_wrap14 w_wrap15 w_wrap17 w_wrap18 w_wrap24 w_wrap25 w_wrap27 w_wrap29 w_wrap30 w_wrap31 w_wrap32 w_wrap33 w_wrap34 w_wrap36 w_wrap38 w_wrap42 w_wrap43 w_wrap44 w_wrap45 w_wrap46 w_wrap48 w_wrap49
p6 half tuck (women): w_tuck1 w_tuck6 w_tuck7 w_tuck9 w_tuck10 w_tuck21 w_tuck22 w_tuck26 w_tuck30 w_tuck31 w_tuck34 w_tuck40 w_tuck41 w_tuck47
p6 shaped jacket / belted: w_blazer5 w_blazer7 w_blazer11 w_blazer14 w_blazer16 w_blazer17 w_blazer20 w_blazer21 w_blazer26 w_blazer30 w_blazer33 w_blazer37 w_blazer38 w_blazer39 w_blazer42 w_blazer12
SKIP w_blazer31 w_blazer0
DUP w_blazer36=w_wide34 w_blazer45=w_wide13
p7 statement earrings (real; on women): e_statement2 e_statement3 e_statement5 e_statement8 e_statement11 e_statement16 e_statement19 e_statement20 e_statement22 e_statement23 e_statement25 e_statement26 e_statement28 e_statement29 e_statement30 e_statement31 e_statement34 e_statement38 e_statement44 e_statement0
SKIP e_statement7 e_statement14 e_statement39 e_statement42 e_statement45 e_statement18 e_statement36 e_statement43
p7 long heavy drops at the jaw: e_dangle1 e_dangle7 e_dangle14 e_dangle16 e_dangle20 e_dangle23 e_dangle25 e_dangle27 e_dangle36 e_dangle42 e_dangle43 e_dangle11
DUP e_dangle0=e_statement0
p7 small hoops on the ear: e_hoops1 e_hoops15 e_hoops18 e_hoops20 e_hoops24 e_hoops26 e_hoops27 e_hoops31 e_hoops39 e_hoops40 e_hoops42 e_hoops47 e_hoops14
p7 pearl studs / delicate drop: e_pearl12 e_pearl22 e_pearl25 e_pearl27 e_pearl8 e_pearl36 e_pearl18 e_pearl19 e_pearl29 e_pearl5 e_pearl1
p7 several necklaces (crowded): e_layer1 e_layer4 e_layer6 e_layer12 e_layer14 e_layer18 e_layer21 e_layer23 e_layer37 e_layer39 e_layer43 e_layer9
p7 one necklace at the collarbone: e_layer17 e_layer28 e_layer35 e_layer40 e_layer44 e_layer8 e_layer30
DUP e_layer16=e_statement20
p8 enormous packed tote (no brand names readable where possible): bag_big10 bag_big12 bag_big19 bag_big21 bag_big28 bag_big29 bag_big42 bag_big44 bag_big45 bag_big48 bag_big3
SKIP bag_big5 bag_big14 bag_big22 bag_big25 bag_big27 bag_big32 bag_big34 bag_big36 bag_big37 bag_big47 bag_big7 bag_big9 bag_big33
p8 heavy shoulder bag: bag_heavy2 bag_heavy5 bag_heavy6 bag_heavy9 bag_heavy13 bag_heavy15 bag_heavy26 bag_heavy28 bag_heavy30 bag_heavy39 bag_heavy49 bag_heavy7 bag_heavy10 bag_heavy16
p8 mid-sized bag, carried well: bag_heavy21 bag_heavy22 bag_heavy31 bag_heavy34 bag_heavy37 bag_heavy41 bag_heavy45 bag_heavy46 bag_heavy12 bag_heavy20
SKIP bag_heavy11 bag_heavy14 bag_heavy25 bag_heavy27 bag_heavy35 bag_heavy42 bag_heavy43 bag_heavy47 bag_heavy48 bag_heavy29
p8 mid-sized structured bag (real; many are brand ads): bag_mid3 bag_mid8 bag_mid12 bag_mid15 bag_mid22 bag_mid30 bag_mid37 bag_mid45 bag_mid46 bag_mid27 bag_mid28
SKIP bag_mid6 bag_mid26 bag_mid31 bag_mid32 bag_mid36 bag_mid38 bag_mid40 bag_mid42 bag_mid43 bag_mid47
p8 tip everything out / put back only what you need: bag_empty13 bag_empty16 bag_empty3 bag_empty20 bag_empty45 bag_pack37 bag_pack41 bag_pack22 bag_pack0
DUP bag_empty1=bag_big12 bag_empty14=bag_big28 bag_empty28=bag_big14 bag_pack15=bag_big7 bag_pack17=bag_big10 bag_pack42=bag_big14 bag_pack0=bag_big12
SKIP bag_pack0
close closet / look through what you have: z_closet0 z_closet10 z_closet12 z_closet18 z_closet20 z_closet33 z_closet42 z_closet44 z_closet9
close capsule rail, waiting at the back: z_wardrobe10 z_wardrobe11 z_wardrobe12 z_wardrobe15 z_wardrobe17 z_wardrobe20 z_wardrobe23 z_wardrobe28 z_wardrobe30 z_wardrobe32 z_wardrobe34 z_wardrobe40 z_wardrobe42
close women 60+ (real only): z_older3 z_older4 z_older12 z_older13 z_older14 z_older15 z_older16 z_older18 z_older19 z_older20 z_older24 z_older25 z_older26 z_older27 z_older30 z_older32 z_older33 z_older35 z_older36 z_older37 z_older38 z_older39 z_older40 z_older42 z_older44 z_older23
SKIP z_older7 z_older9 z_older2 z_older28 z_older41 z_older8 z_older11
DUP z_older6=h_older1 z_older10=h_older7 z_older31=h_older3 z_older34=h_sixty15
close walking out the door (real only): z_door7 z_door8 z_door11 z_door14 z_door24 z_door31 z_door36 z_door40 z_door43 z_door47 z_door48 z_door28
SKIP z_door2 z_door13 z_door16 z_door17 z_door20 z_door22 z_door30 z_door32 z_door34 z_door37 z_door39 z_door45 z_door46
p2 mirror (what you see first): z_mirror6 z_mirror7 z_mirror4 z_mirror16 z_mirror23 z_mirror36 z_mirror41
close walking (real only): z_smile10 z_smile21 z_smile33 z_smile35 z_smile43 z_smile46
SKIP z_smile2 z_smile8 z_smile20 z_smile22 z_smile25 z_smile27 z_smile31 z_smile32 z_smile36
p2b stiff ruffles at the neck: b_jabot1 b_jabot4 b_jabot16 b_jabot17 b_jabot26 b_jabot45 b_jabot46 b_jabot2 b_jabot6 b_jabot9 b_jabot27 b_jabot22 b_victorian0 b_victorian5 b_victorian6 b_victorian15 b_victorian36 b_victorian3 b_victorian12 b_stiff0 b_stiff9 b_stiff5 b_stiff36 b_stiff23
p3 audrey black turtleneck (Funny Face / b&w): r_audrey3_1 r_audrey3_4 r_audrey3_0 r_audrey3_32 r_audrey3_45 r_audrey3_27 r_audrey2_22 r_audrey2_37
DUP b_victorian13=b_jabot45 b_victorian40=b_jabot46 b_stiff13=b_jabot45 b_stiff1=b_jabot1 b_stiff27=b_jabot36 b_stiff33=b_jabot22 b_victorian43=b_bow37
# v2 re-edit (user: new intro clips): real-looking older women only; AI-looking pins (polished red-lip silver bob series etc.) left out
v2 hook: v_grey0 v_grey4 v_grey5 v_grey14 v_grey20 v_grey23 v_grey44 v_sixties2 v_sixties15 v_sixties27 v_sixties30 v_sixties32 v_sixties48 v_paris60_9 v_paris60_17 v_paris60_22 v_paris60_25 v_paris60_35 v_paris60_41 v_paris60_44 v_paris60_45 v_cafe40 v_cafe47
v2 trousers: v_hemlen45 v_hemlen19

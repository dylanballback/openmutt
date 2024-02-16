import pyodrivecan
import asyncio
from datetime import datetime, timedelta


new_positions = [0.21923021646216512, 0.21922312676906586, 0.2192177250981331, 0.21921232342720032, 0.21920692175626755, 0.21920152008533478, 0.21919647982576862, 0.2191931949928403, 0.21919228514889255, 0.21919313073158264, 0.21919433772563934, 0.21919554471969604, 0.21919675171375275, 0.21919795870780945, 0.2191991726285778, 0.21920042019337416, 0.21920171327656135, 0.21920304000377655, 0.2192043736577034, 0.21920570731163025, 0.2192070409655571, 0.21920837461948395, 0.21920962556032464, 0.2192104747518897, 0.21921078040031716, 0.219210684299469, 0.21921050548553467, 0.21921032667160034, 0.21921014785766602, 0.2192099690437317, 0.21921001432929188, 0.21921114809811115, 0.21921375452075154, 0.219217449426651, 0.21922136843204498, 0.21922528743743896, 0.21922920644283295, 0.21923312544822693, 0.21923673193668947, 0.2192388204857707, 0.2192388553521596, 0.21923737227916718, 0.21923557668924332, 0.21923378109931946, 0.2192319855093956, 0.21923018991947174, 0.21922793635167181, 0.21922345831990242, 0.21921597071923316, 0.21920625865459442, 0.21919608861207962, 0.21918591856956482, 0.21917574852705002, 0.21916557848453522, 0.21915636351332068, 0.2191517874598503, 0.21915348758921027, 0.2191598266363144, 0.21916712075471878, 0.21917441487312317, 0.21918170899152756, 0.21918900310993195, 0.21919641131535172, 0.2192043736577034, 0.21921308571472764, 0.21922235190868378, 0.2192317321896553, 0.21924111247062683, 0.21925049275159836, 0.21925987303256989, 0.2192680183215998, 0.21927016507834196, 0.2192641961737536, 0.21925222873687744, 0.2192390263080597, 0.21922582387924194, 0.2192126214504242, 0.21919941902160645, 0.21918732934864238, 0.21918064448982477, 0.21918127202661708, 0.21918730437755585, 0.2191944494843483, 0.21920159459114075, 0.2192087396979332, 0.21921588480472565, 0.219222234969493, 0.21922472398728132, 0.2192219891003333, 0.21921539306640625, 0.2192080020904541, 0.21920061111450195, 0.2191932201385498, 0.21918582916259766, 0.2191751300706528, 0.21914836298674345, 0.2190998568548821, 0.2190352827310562, 0.21896740049123764, 0.21889951825141907, 0.2188316360116005, 0.21876375377178192, 0.21870003652293235, 0.21865654923021793, 0.21864043187815696, 0.21864454448223114, 0.21865282207727432, 0.2186610996723175, 0.2186693772673607, 0.21867765486240387, 0.21867759677115828, 0.21863705106079578, 0.21854172798339278, 0.21840591728687286, 0.21826177090406418, 0.2181176245212555, 0.2179734781384468, 0.21782933175563812, 0.2176842062617652, 0.21753432508558035, 0.21737800975097343, 0.21721693873405457, 0.21705488860607147, 0.21689283847808838, 0.21673078835010529, 0.2165687382221222, 0.21605110372183844, 0.21380634512752295, 0.20922488922951743, 0.20291630923748016, 0.19625214487314224, 0.18958798050880432, 0.1829238161444664, 0.17625965178012848, 0.1691019901772961, 0.15954734198749065, 0.14674971194472164, 0.13155509531497955, 0.11586698144674301, 0.10017886757850647, 0.08449075371026993, 0.06880263984203339, 0.05309233441948891, 0.03727424144744873, 0.021310318261384964, 0.0052386075258255005, -0.0108552947640419, -0.026949197053909302, -0.0430430993437767, -0.059137001633644104, -0.07566569015034474, -0.09430619748309255, -0.11580387144931592, -0.13941336423158646, -0.16345764324069023, -0.187501922249794, -0.21154620125889778, -0.23559048026800156, -0.2589299859246239, -0.2788463067263365, 
-0.2941312597831711, -0.305993027985096, -0.3171500228345394, -0.32830701768398285, -0.3394640125334263, -0.3506210073828697, -0.36189323806320317, -0.373725185636431, -0.38631439724122174, -0.39946332573890686, -0.412727490067482, -0.42599165439605713, -0.43925581872463226, -0.4525199830532074, -0.4663895232370123, -0.4831994604319334, -0.5039875818183646, -0.5277161002159119, -0.552049994468689, -0.5763838887214661, -0.6007177829742432, -0.6250516772270203, -0.6488259648904204, -0.6698821634054184, -0.6872609471902251, -0.7019216418266296, -0.7160227298736572, -0.7301238179206848, -0.7442249059677124, -0.75832599401474, -0.7745867211488076, -0.8013371238484979, -0.8422794405487366, -0.8937114328145981, -0.9473030641674995, -1.000894695520401, -1.0544863268733025, -1.108077958226204, -1.1608134549460374, -1.209390583448112, -1.252341684361454, -1.2911344170570374, -1.3290710151195526, -1.3670076131820679, -1.4049442112445831, -1.4428808093070984, -1.4797140979208052, -1.511188454926014, -1.5354124926961958, -1.5542775988578796, -1.572039395570755, -1.5898011922836304, -1.6075629889965057, -1.625324785709381, -1.643217490753159, -1.6617460362613201, -1.6811348365154117, -1.7011594772338867, -1.7213150262832642, -1.7414705753326416, -1.761626124382019, -1.7817816734313965, -1.802183420630172, -1.8237809874117374, -1.8469964277464896, -1.871407687664032, -1.8960651457309723, -1.9207226037979126, -1.945380061864853, -1.9700375199317932, -1.994330688379705, -2.016854450106621, -2.0369843086227775, -2.0553447604179382, -2.0733409225940704, -2.0913370847702026, -2.109333246946335, -2.127329409122467, -2.144357027951628, -2.156680293381214, -2.1626388453878462, -2.1638930439949036, -2.1641786992549896, -2.1644643545150757, -2.1647500097751617, -2.165035665035248, -2.1653045397251844, -2.165491908788681, -2.165569005534053, -2.1655645966529846, -2.165543407201767, -2.1655222177505493, -2.1655010282993317, -2.165479838848114, -2.165456481743604, -2.165422596037388, -2.165374465752393, -2.165315806865692, -2.165254980325699, -2.1651941537857056, -2.1651333272457123, -2.165072500705719, -2.1650119186379015, -2.1649525240063667, -2.164894735906273, -2.164838135242462, -2.164781779050827, -2.164725422859192, -2.1646690666675568, -2.1646127104759216, -2.164550508139655, -2.1644599102437496, -2.16433089482598, -2.1641734838485718, -2.164010226726532, -2.163846969604492, -2.1636837124824524, -2.1635204553604126, -2.163334987126291, -2.1630416363477707, -2.1626023268327117, -2.1620551347732544, -2.161485731601715, -2.160916328430176, -2.1603469252586365, -2.159777522087097, -2.159193996572867, -2.15854187682271, -2.157796953106299, -2.156983435153961, -2.1561557948589325, -2.155328154563904, -2.154500514268875, -2.1536728739738464, -2.1528616377618164, -2.152130078524351, -2.151506317546591, -2.150962233543396, -2.1504345536231995, -2.149906873703003, -2.1493791937828064, -2.14885151386261, -2.148352130781859, -2.1479901894927025, -2.1478141988627613, -2.147775650024414, -2.1477653980255127, 
-2.1477551460266113, -2.14774489402771, -2.1477346420288086, -2.147724918089807, -2.147717759013176, -2.147714070044458, -2.1477129459381104, -2.1477123498916626, -2.147711753845215, -2.147711157798767, -2.1477105617523193, -2.147430845303461, -2.145795401185751, -2.142325737280771, -2.1375003457069397, -2.1323958337306976, -2.1272913217544556, -2.1221868097782135, -2.1170822978019714, -2.111595908878371, -2.104254689067602, -2.0944039921741933, -2.0826984643936157, -2.07061105966568, -2.058523654937744, -2.0464362502098083, -2.0343488454818726, -2.0220969289075583, -2.0090459547936916, -1.9949139028321952, -1.9799827933311462, -1.9648871719837189, -1.9497915506362915, -1.9346959292888641, -1.9196003079414368, -1.9042150180321187, -1.8874227665364742, -1.8687269787769765, -1.8486242294311523, -1.8282318115234375, -1.8078393936157227, -1.7874469757080078, -1.767054557800293, -1.7470193023327738, -1.7287188358604908, -1.7127654368523508, -1.698546826839447, -1.684685379266739, -1.6708239316940308, -1.6569624841213226, -1.6431010365486145, -1.6297032573493198, -1.6185575816780329, -1.6104588696034625, -1.6046122610569, -1.599229320883751, -1.5938463807106018, -1.5884634405374527, -1.5830805003643036, -1.577600980643183, -1.5716523602604866, -1.5650690742768347, -1.558016687631607, -1.550867721438408, -1.5437187552452087, -1.5365697890520096, -1.5294208228588104, -1.5216919287340716, -1.511146241798997, -1.4967895998852327, -1.4796161651611328, -1.4618628025054932, -1.4441094398498535, -1.4263560771942139, -1.4086027145385742, -1.3904655696824193, -1.370464339852333, -1.347941112704575, -1.3235538005828857, -1.2987827062606812, -1.2740116119384766, -1.249240517616272, -1.2244694232940674, -1.2000509393401444, -1.177345134317875, -1.156956483144313, -1.1382805109024048, -1.119957149028778, -1.1016337871551514, -1.0833104252815247, -1.064987063407898, -1.0467169667244889, -1.0287055866792798, -1.0110442350269295, -0.9936416000127792, -0.9762922301888466, -0.9589428603649139, -0.9415934905409813, -0.9242441207170486, -0.9071046803728677, -0.8909848975017667, -0.8762446512118913, -0.8625240623950958, -0.8490134030580521, -0.8355027437210083, -0.8219920843839645, -0.8084814250469208, -0.7953801323310472, -0.7842671917751431, -0.7758443747297861, -0.7694099098443985, -0.7633848115801811, -0.7573597133159637, -0.7513346150517464, -0.745309516787529, -0.738820854050573, -0.7300805924460292, -0.7182940500206314, -0.7042559087276459, -0.6897542029619217, -0.6752524971961975, -0.6607507914304733, -0.6462490856647491, -0.6316496955405455, -0.6165758385322988, -0.6008600557397585, -0.5846698060631752, -0.5683818720281124, -0.5520939379930496, -0.5358060039579868, -0.519518069922924, -0.503154925245326, -0.4864264717325568, -0.46920377685455605, -0.4516157731413841, -0.43395255878567696, -0.4162893444299698, -0.3986261300742626, -0.38096291571855545, -0.3631639471859671, -0.34470560122281313, -0.3253551563830115, -0.3053453341126442, -0.28519975766539574, -0.2650541812181473, -0.24490860477089882, -0.22476302832365036, -0.20473513141041622, -0.1852788208052516, -0.16659583285218105, -0.14848443120718002, -0.1304907090961933, -0.1124969869852066, -0.0945032648742199, -0.07650954276323318, -0.05897198515594937, -0.04365008370950818, -0.03132583471597172, -0.021217241883277893, -0.011564813554286957, -0.0019123852252960205, 0.007740043103694916, 0.017392471432685852, 0.027114261407405138, 0.03717295080423355, 0.04768744530156255, 0.05853883922100067, 0.06945959478616714, 0.08038035035133362, 0.09130110591650009, 0.10222186148166656, 0.11301717755850405, 0.1232032161206007, 0.13256493804510683, 0.14131738245487213, 0.14994438737630844, 0.15857139229774475, 0.16719839721918106, 0.17582540214061737, 0.18418017588555813, 0.19121268391609192, 0.19645624421536922, 0.20037753880023956, 0.20402660220861435, 0.20767566561698914, 0.21132472902536392, 0.2149737924337387, 0.2186227001948282, 0.22227085195481777, 0.22591798088978976, 0.2295643538236618, 0.23321057111024857, 0.23685678839683533, 0.2405030056834221, 0.24414922297000885, 0.24797199480235577, 0.2526523172855377, 0.25849285535514355, 0.2651909440755844, 0.27206558734178543, 0.27894023060798645, 0.28581487387418747, 0.2926895171403885, 
0.2998873935721349, 0.30865525966510177, 0.3195472294173669, 0.3320091888308525, 0.3447943814098835, 0.3575795739889145, 0.3703647665679455, 0.38314995914697647, 0.3959201643592678, 0.4086175737902522, 0.42121649481123313, 0.43374262005090714, 0.4462537579238415, 0.4587648957967758, 0.47127603366971016, 0.4837871715426445, 0.4958673658838961, 0.5058544059284031, 0.513009531336138, 0.5180715024471283, 0.5227025300264359, 0.5273335576057434, 0.531964585185051, 0.5365956127643585, 0.5412633869564161, 0.5461096446961164, 0.5511973801767454, 0.5564635992050171, 0.5617665648460388, 0.5670695304870605, 0.5723724961280823, 0.577675461769104, 0.5832496635848656, 0.5901412982493639, 0.5988153420621529, 0.6088068187236786, 0.6190695315599442, 0.6293322443962097, 0.6395949572324753, 0.6498576700687408, 0.6602891648653895, 0.6715404577553272, 0.6839008892420679, 0.6970811188220978, 0.7104301303625107, 0.7237791419029236, 0.7371281534433365, 0.7504771649837494, 0.7631346503039822, 0.7724332939833403, 0.7771876225015149, 0.7785831093788147, 0.7792870700359344, 0.7799910306930542, 0.780694991350174, 0.7813989520072937, 0.782067070598714, 0.7825610991567373, 0.7828195941401646, 0.7829039990901947, 0.7829525619745255, 0.7830011248588562, 0.783049687743187, 0.7830982506275177, 0.78314310812857, 0.7831699680536985, 0.7831724783172831, 0.7831569910049438, 0.7831377983093262, 0.7831186056137085, 0.7830994129180908, 0.7830802202224731, 0.7830590880475938, 0.7830285355448723, 0.7829852378927171, 0.7829325199127197, 0.7828778624534607, 0.7828232049942017, 0.7827685475349426, 0.7827138900756836, 0.7826593181816861, 0.7826051618903875, 0.7825515678850934, 0.7824983894824982, 0.7824452966451645, 0.7823922038078308, 0.7823391109704971, 0.7822860181331635, 0.7821798797231168, 0.781816091388464, 0.7811037178616971, 0.7801336944103241, 0.7791106253862381, 0.7780875563621521, 0.7770644873380661, 0.7760414183139801, 0.774904708028771, 0.773216025903821, 0.7707805583486333, 0.7677931189537048, 0.7646920382976532, 0.7615909576416016, 0.7584898769855499, 0.7553887963294983, 0.7521709867287427, 0.7483862079679966, 0.7438343532849103, 0.7387155294418335, 0.7334799766540527, 0.728244423866272, 0.7230088710784912, 0.7177733182907104, 0.7125649239169434, 0.7074884418398142, 0.7025904293404892, 0.6978243291378021, 0.6930853873491287, 0.6883464455604553, 0.6836075037717819, 0.6788685619831085, 0.6742716874578036, 0.670364853926003, 0.6673916052677669, 0.665108397603035, 0.6629672572016716, 0.6608261168003082, 0.6586849763989449, 0.6565438359975815, 0.6543348814593628, 0.6517965439707041, 0.6488125707255676, 0.6454992145299911, 0.6421180441975594, 0.6387368738651276, 0.6353557035326958, 0.631974533200264, 0.6284105160157196, 0.6239583855494857, 0.6183046900550835, 0.6117628812789917, 0.6050382256507874, 0.598313570022583, 0.5915889143943787, 0.5848642587661743, 0.578192577813752, 0.5717782024294138, 0.5657119463430718, 0.5599029958248138, 0.554147019982338, 0.5483910441398621, 0.5426350682973862, 0.5368790924549103, 0.53014318208443, 0.5186475897207856, 0.5007124276016839, 0.47801758348941803, 0.4543428048491478, 0.43066802620887756, 0.40699324756860733, 0.3833184689283371, 0.3593371115857735, 0.33386665768921375, 0.30638154374901205, 0.27740733325481415, 0.2481265440583229, 0.21884575486183167, 0.18956496566534042, 
0.16028417646884918, 0.13143295829650015, 0.10466822795569897, 0.08072639291640371, 0.05887104570865631, 0.03744526952505112, 0.016019493341445923, -0.005406282842159271, -0.026832059025764465, -0.048833595094038174, -0.07363167917355895, -0.10221332820947282, -0.13359152525663376, -0.1655454821884632, -0.19749943912029266, -0.22945339605212212, -0.26140735298395157, -0.292328455921961, -0.318232839461416, -0.337349896755768, -0.35145023465156555, -0.3645177185535431, -0.37758520245552063, -0.39065268635749817, -0.4037201702594757, -0.4169765812403057, -0.4311506380327046, -0.4465662156289909, -0.46289943903684616, -0.47942158952355385, -0.49594374001026154, -0.5124658904969692, -0.5289880409836769, -0.5458276730205398, -0.5642093583010137, -0.584677350911079, -0.6066873967647552, -0.6290149241685867, -0.6513424515724182, -0.6736699789762497, -0.6959975063800812, -0.7176657155505382, -0.7361315218731761, -0.750264665519353, -0.7611954063177109, -0.7714668288826942, -0.7817382514476776, -0.792009674012661, -0.8022810965776443, -0.8152444805018604, -0.8412831053137779, -0.8850117619149387, -0.941815659403801, -1.001311518251896, -1.0608073770999908, -1.1203032359480858, -1.1797990947961807, -1.2362624013912864, -1.2779961684718728, -1.2998017350328155, -1.306877762079239, -1.310921236872673, -1.3149647116661072, -1.3190081864595413, -1.3230516612529755, -1.3277589725330472, -1.3356906324625015, -1.3479846464470029, -1.3635030090808868, -1.3796852082014084, -1.39586740732193, -1.4120496064424515, -1.428231805562973, -1.4447015227051452, -1.4625677559524775, -1.4823233933420852, -1.503475546836853, -1.5249152183532715, -1.54635488986969, -1.5677945613861084, -1.5892342329025269, -1.609609124599956, -1.6248122286051512, -1.6330182080855593, -1.6360523998737335, -1.6380218118429184, -1.6399912238121033, -1.6419606357812881, -1.643930047750473, -1.6457902116235346, -1.6471197418868542, -1.6477313560899347, -1.6478123366832733, -1.6477840691804886, -1.6477558016777039, -1.6477275341749191, -1.6476992666721344, -1.6476725181564689, -1.6476531475782394, -1.6476437589153647, -1.6476417481899261, -1.6476412564516068, -1.6476407647132874, -1.647640272974968, -1.6476397812366486, -1.6476341963279992, -1.6476038731634617, -1.647540080593899, -1.6474515497684479, -1.647357925772667, -1.647264301776886, -1.647170677781105, -1.647077053785324, -1.646980534424074, -1.6468699518591166, -1.6467403426067904, -1.6465966701507568, -1.6464501023292542, -1.6463035345077515, -1.6461569666862488, -1.646010398864746, -1.6458496589912102, -1.64562008343637, -1.6452973772538826, -1.644905835390091, -1.644500121474266, -1.6440944075584412, -1.6436886936426163, -1.6432829797267914, -1.6428522978676483, -1.6423003431409597, -1.6415843133581802, -1.6407470107078552, -1.639884740114212, -1.6390224695205688, -1.6381601989269257, -1.6372979283332825, -1.63643994089216, -1.6356027573347092, -1.6347937202081084, -1.6340054869651794, -1.6332215368747711, -1.6324375867843628, -1.6316536366939545, -1.6308696866035461, -1.6301216250285506, -1.6295478790998459, -1.629209971986711, -1.629046380519867, -1.6289186775684357, -1.6287909746170044, -1.6286632716655731, -1.6285355687141418, -1.6284074550494552, -1.6282773464918137, -1.628144538961351, -1.6280097365379333, -1.6278745234012604, -1.6277393102645874, -1.6276040971279144, -1.6274688839912415, -1.6270537477685139, -1.6252789851278067, -1.6216647279215977, -1.616690844297409, -1.6114370375871658, -1.6061832308769226, -1.6009294241666794, -1.5956756174564362, -1.590410553617403, -1.5850908122956753, -1.5796970955561846, -1.5742487013339996, -1.5687890499830246, -1.5633293986320496, -1.5578697472810745, -1.5524100959300995, -1.5472493598936126, -1.5435404982417822, -1.5417959372280166, -1.5415032505989075, -1.5415094792842865, -1.5415157079696655, -1.5415219366550446, -1.5415281653404236, -1.5415340819163248, -1.5415384825319052, -1.5415408321423456, -1.5415416657924652, -1.541542187333107, -1.5415427088737488, -1.5415432304143906, -1.5415437519550323, -1.5415424652164802, -1.5415323954075575, -1.5415104426210746, -1.5414797067642212, -1.5414471626281738, -1.5414146184921265, -1.541382074356079, -1.5413495302200317, -1.541312400600873, -1.5412529986351728, -1.5411634634947404, -1.5410516560077667, -1.5409352630376816, -1.5408188700675964, -1.5407024770975113, -1.5405860841274261, -1.540449888096191, -1.5402175057679415, -1.539854989037849, -1.5393962860107422, -1.5389177799224854, -1.5384392738342285, -1.5379607677459717, -1.5374822616577148, -1.5370299116475508, -1.5367046054452658, -1.536551182041876, -1.5365248024463654, -1.5365245789289474, -1.5365243554115295, -1.5365241318941116, -1.5365239083766937, -1.5365227485308424, -1.5365170408040285, -1.5365051800617948, -1.5364887714385986, -1.536471426486969, -1.5364540815353394, -1.5364367365837097, -1.53641939163208, -1.536403421428986, -1.536394128575921, -1.5363938697846606, -1.5364002883434296, -1.536408081650734, -1.5364158749580383, -1.5364236682653427, -1.536431461572647, -1.536437850794755, -1.5364374201744795, -1.5364277627086267, -1.5364112854003906, -1.536393404006958, -1.5363755226135254, -1.5363576412200928, -1.5363397598266602, -1.5363251592498273, -1.5363264940679073, -1.5363493885379285, -1.5363882184028625, -1.5364303290843964, -1.5364724397659302, -1.536514550447464, -1.5365566611289978, -1.5365965740056708, -1.536625811830163, -1.5366406069369987, -1.5366447269916534, -1.5366466492414474, -1.5366485714912415, -1.5366504937410355, -1.5366524159908295, -1.536653479328379, -1.5366503708064556, -1.5366416180040687, -1.5366286933422089, -1.5366149097681046, -1.5366011261940002, -1.536587342619896, -1.5365735590457916, -1.5365605292608961, -1.5365511607378721, -1.5365467456867918, -1.536545991897583, -1.536545991897583, -1.536545991897583, -1.536545991897583, -1.536545991897583, -1.536545991897583, -1.536545991897583]


# Define path to database for pyodrivecan package.
database = pyodrivecan.OdriveDatabase('odrive_data.db')


def get_raw_position_over_time(trial_id, node_id):
    """
    Fetches raw position and time data for a given trial_id and node_id from the database.

    Parameters:
    - trial_id (int): The trial ID to filter the data.
    - node_id (int): The node ID to filter the data.

    Returns:
    - tuple: (times, positions, trial_id, node_id) where times and positions are lists of recorded data.
             Returns None for times and positions if no data is found.
    """
    # SQL query to select time and position for a specific trial_id and node_id
    sql = """
    SELECT time, position FROM ODriveData
    WHERE trial_id = ? AND node_ID = ?
    ORDER BY time;
    """
    # Execute the query and fetch all results
    results = database.fetch(sql, (trial_id, node_id))
    
    # If results are empty, inform the user and return None
    if not results:
        print("No data found for the given trial_id and node_id.")
        return

    # Unpack the results into separate lists
    times, positions = zip(*results)
    return times, positions, trial_id, node_id

async def smooth_send_positions_to_motor(odrive1):
     dt = 0.01
     #Run for set time delay example runs for 15 seconds.
     stop_at = datetime.now() + timedelta(seconds=30)
     while datetime.now() < stop_at:
        for pos in new_positions:
            odrive1.set_position(pos)
            print(f"Setting motor position to: {pos}") 
            await asyncio.sleep(dt)

     odrive1.running = False

# Function to send positions to the motor
async def send_positions_to_motor(odrive1, positions):
    """
    Sends the position commands to the motor to repeat the path.
    Parameters:
    - recorded_positions (list): The recorded positions to be used as via points.
    - total_time (float): The total time for the trajectory.
    - tacc (float): Acceleration time for the trajectory.
    - qdmax (float): Maximum speed for the trajectory.
    """
    
    #Run for set time delay example runs for 15 seconds.
    stop_at = datetime.now() + timedelta(seconds=30)
    while datetime.now() < stop_at:
        dt = 0.15
        # Iterate over the positions and send them to the motor
        for pos in positions.flatten():
            #odrive1.set_position(pos)
            print(f"Setting motor position to: {pos}") 
            await asyncio.sleep(dt)

    odrive1.running = False
    


#Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.
async def controller(odrive1, odrive2, odrive3):
        #odrive1.set_position(0)
        #print("Set odrive to postion 0")
        #odrive2.set_position(0)
        #odrive3.set_position(0)
        # Example usage
        #recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
        
        dt = 0.125


        #Run for set time delay example runs for 15 seconds.
        stop_at = datetime.now() + timedelta(seconds=15)
        while datetime.now() < stop_at:
            await asyncio.sleep(0) #Need this for async to work.
            #print(odrive1.position, odrive2.position)
            #for pos in recorded_positions:
                #odrive1.set_position(pos)
                #await asyncio.sleep(dt)
            #print("Set odrive to postion 0")
            #await asyncio.sleep(3)
            #odrive1.set_position(3)
            #print("Set odrive to postion 3")
            #await asyncio.sleep(3)
            
    
            

        #await asyncio.sleep(15) #no longer need this the timedelta =15 runs the program for 15 seconds.
        odrive1.running = False
        odrive2.running = False
        odrive3.running = False



# Run multiple busses.
async def main():
    #Set up Node_ID 1
    odrive1 = pyodrivecan.ODriveCAN(1, closed_loop_control_flag = True)
    odrive1.initCanBus()

    #Set up Node_ID 2 
    odrive2 = pyodrivecan.ODriveCAN(2, closed_loop_control_flag = True)
    odrive2.initCanBus()

    #Set up Node_ID 3 
    odrive3 = pyodrivecan.ODriveCAN(3, closed_loop_control_flag = True)
    odrive3.initCanBus()

    # Example usage
    #recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
    #total_time = 10  # Total time to complete the path in seconds

    
    #add each odrive to the async loop so they will run.
    await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        #controller(odrive1, odrive2, odrive3),
        smooth_send_positions_to_motor(odrive1)
        #send_positions_to_motor(odrive1, positions)
    )

if __name__ == "__main__":
    asyncio.run(main())
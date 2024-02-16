import pyodrivecan
import asyncio
from datetime import datetime, timedelta


nodeID_1_pos = [
    "-3.04743496",
    "-3.04742342",
    "-3.04741463",
    "-3.04740584",
    "-3.04739705",
    "-3.04738826",
    "-3.04738010",
    "-3.04737505",
    "-3.04737420",
    "-3.04737645",
    "-3.04737934",
    "-3.04738224",
    "-3.04738513",
    "-3.04738802",
    "-3.04739104",
    "-3.04739470",
    "-3.04739924",
    "-3.04740441",
    "-3.04740971",
    "-3.04741502",
    "-3.04742032",
    "-3.04742563",
    "-3.04743007",
    "-3.04743034",
    "-3.04742495",
    "-3.04741538",
    "-3.04740494",
    "-3.04739451",
    "-3.04738408",
    "-3.04737365",
    "-3.04736417",
    "-3.04735932",
    "-3.04736072",
    "-3.04736674",
    "-3.04737371",
    "-3.04738069",
    "-3.04738766",
    "-3.04739463",
    "-3.04740108",
    "-3.04740495",
    "-3.04740534",
    "-3.04740316",
    "-3.04740044",
    "-3.04739773",
    "-3.04739502",
    "-3.04739231",
    "-3.04739015",
    "-3.04739066",
    "-3.04739480",
    "-3.04740161",
    "-3.04740897",
    "-3.04741633",
    "-3.04742369",
    "-3.04743105",
    "-3.04743776",
    "-3.04744128",
    "-3.04744050",
    "-3.04743654",
    "-3.04743192",
    "-3.04742730",
    "-3.04742268",
    "-3.04741806",
    "-3.04741373",
    "-3.04741081",
    "-3.04740979",
    "-3.04741019",
    "-3.04741088",
    "-3.04741156",
    "-3.04741225",
    "-3.04741293",
    "-3.04741356",
    "-3.04741388",
    "-3.04741379",
    "-3.04741341",
    "-3.04741296",
    "-3.04741251",
    "-3.04741207",
    "-3.04741162",
    "-3.04741060",
    "-3.04740683",
    "-3.04739931",
    "-3.04738903",
    "-3.04737818",
    "-3.04736733",
    "-3.04735649",
    "-3.04734564",
    "-3.04733522",
    "-3.04732690",
    "-3.04732142",
    "-3.04731804",
    "-3.04731509",
    "-3.04731214",
    "-3.04730919",
    "-3.04730624",
    "-3.04729277",
    "-3.04722822",
    "-3.04709456",
    "-3.04690981",
    "-3.04671454",
    "-3.04651928",
    "-3.04632401",
    "-3.04612875",
    "-3.04570019",
    "-3.04413848",
    "-3.04104370",
    "-3.03681576",
    "-3.03235453",
    "-3.02789330",
    "-3.02343208",
    "-3.01897085",
    "-3.01424522",
    "-3.00823535",
    "-3.00048799",
    "-2.99145639",
    "-2.98216039",
    "-2.97286439",
    "-2.96356839",
    "-2.95427239",
    "-2.94467480",
    "-2.93361234",
    "-2.92056800",
    "-2.90605879",
    "-2.89124799",
    "-2.87643719",
    "-2.86162639",
    "-2.84681559",
    "-2.83206752",
    "-2.81762418",
    "-2.80359310",
    "-2.78986675",
    "-2.77620313",
    "-2.76253951",
    "-2.74887589",
    "-2.73521227",
    "-2.72162896",
    "-2.70843572",
    "-2.69577023",
    "-2.68349481",
    "-2.67129970",
    "-2.65910459",
    "-2.64690948",
    "-2.63471437",
    "-2.62258119",
    "-2.61074887",
    "-2.59932358",
    "-2.58819914",
    "-2.57713664",
    "-2.56607413",
    "-2.55501163",
    "-2.54394913",
    "-2.53286929",
    "-2.52170524",
    "-2.51042727",
    "-2.49906510",
    "-2.48768559",
    "-2.47630608",
    "-2.46492657",
    "-2.45354706",
    "-2.44218116",
    "-2.43088139",
    "-2.41967108",
    "-2.40852690",
    "-2.39739633",
    "-2.38626575",
    "-2.37513518",
    "-2.36400461",
    "-2.35260509",
    "-2.33989920",
    "-2.32542590",
    "-2.30964625",
    "-2.29359764",
    "-2.27754903",
    "-2.26150042",
    "-2.24545181",
    "-2.22929894",
    "-2.21263966",
    "-2.19529523",
    "-2.17744440",
    "-2.15948930",
    "-2.14153421",
    "-2.12357911",
    "-2.10562402",
    "-2.08774876",
    "-2.07026128",
    "-2.05329842",
    "-2.03672335",
    "-2.02022810",
    "-2.00373286",
    "-1.98723762",
    "-1.97074237",
    "-1.95444781",
    "-1.93912795",
    "-1.92512682",
    "-1.91210040",
    "-1.89927466",
    "-1.88644892",
    "-1.87362318",
    "-1.86079744",
    "-1.84802677",
    "-1.83552364",
    "-1.82338247",
    "-1.81150883",
    "-1.79969028",
    "-1.78787172",
    "-1.77605316",
    "-1.76423460",
    "-1.75219143",
    "-1.73905731",
    "-1.72444717",
    "-1.70874608",
    "-1.69282037",
    "-1.67689466",
    "-1.66096896",
    "-1.64504325",
    "-1.62928855",
    "-1.61436440",
    "-1.60056397",
    "-1.58759409",
    "-1.57479522",
    "-1.56199634",
    "-1.54919747",
    "-1.53639859",
    "-1.52334088",
    "-1.50902599",
    "-1.49301019",
    "-1.47573721",
    "-1.45820540",
    "-1.44067359",
    "-1.42314178",
    "-1.40560997",
    "-1.38753445",
    "-1.36681810",
    "-1.34252885",
    "-1.31559876",
    "-1.28812496",
    "-1.26065117",
    "-1.23317738",
    "-1.20570359",
    "-1.17842977",
    "-1.15212724",
    "-1.12713881",
    "-1.10312167",
    "-1.07930450",
    "-1.05548733",
    "-1.03167017",
    "-1.00785300",
    "-0.98458826",
    "-0.96400670",
    "-0.94705535",
    "-0.93278718",
    "-0.91907144",
    "-0.90535569",
    "-0.89163995",
    "-0.87792420",
    "-0.86443008",
    "-0.85201241",
    "-0.84105112",
    "-0.83116628",
    "-0.82150307",
    "-0.81183985",
    "-0.80217663",
    "-0.79251342",
    "-0.78311765",
    "-0.77502091",
    "-0.76868168",
    "-0.76364148",
    "-0.75886872",
    "-0.75409597",
    "-0.74932322",
    "-0.74455047",
    "-0.74002045",
    "-0.73666943",
    "-0.73491351",
    "-0.73433660",
    "-0.73400242",
    "-0.73366824",
    "-0.73333406",
    "-0.73299988",
    "-0.73268391",
    "-0.73245644",
    "-0.73234869",
    "-0.73232943",
    "-0.73232839",
    "-0.73232734",
    "-0.73232630",
    "-0.73232526",
    "-0.73232410",
    "-0.73232242",
    "-0.73232000",
    "-0.73231706",
    "-0.73231401",
    "-0.73231095",
    "-0.73230790",
    "-0.73230484",
    "-0.73230264",
    "-0.73230458",
    "-0.73231213",
    "-0.73232383",
    "-0.73233637",
    "-0.73234892",
    "-0.73236147",
    "-0.73237401",
    "-0.73238688",
    "-0.73240129",
    "-0.73241778",
    "-0.73243582",
    "-0.73245418",
    "-0.73247254",
    "-0.73249090",
    "-0.73250926",
    "-0.73252584",
    "-0.73253380",
    "-0.73253010",
    "-0.73251778",
    "-0.73250368",
    "-0.73248959",
    "-0.73247549",
    "-0.73246139",
    "-0.73246201",
    "-0.73253408",
    "-0.73270283",
    "-0.73294304",
    "-0.73319796",
    "-0.73345289",
    "-0.73370781",
    "-0.73396273",
    "-0.73437607",
    "-0.73555889",
    "-0.73778275",
    "-0.74077609",
    "-0.74392785",
    "-0.74707961",
    "-0.75023137",
    "-0.75338313",
    "-0.75644175",
    "-0.75904801",
    "-0.76104223",
    "-0.76258408",
    "-0.76403279",
    "-0.76548150",
    "-0.76693022",
    "-0.76837893",
    "-0.77027303",
    "-0.77433042",
    "-0.78131461",
    "-0.79046211",
    "-0.80005498",
    "-0.80964786",
    "-0.81924073",
    "-0.82883361",
    "-0.83912420",
    "-0.85280368",
    "-0.87106815",
    "-0.89272150",
    "-0.91507258",
    "-0.93742365",
    "-0.95977472",
    "-0.98212579",
    "-1.00429104",
    "-1.02555374",
    "-1.04559533",
    "-1.06473437",
    "-1.08368759",
    "-1.10264081",
    "-1.12159403",
    "-1.14054725",
    "-1.15921104",
    "-1.17646906",
    "-1.19182514",
    "-1.20577544",
    "-1.21943632",
    "-1.23309720",
    "-1.24675807",
    "-1.26041895",
    "-1.27411603",
    "-1.28798892",
    "-1.30209969",
    "-1.31638628",
    "-1.33070907",
    "-1.34503186",
    "-1.35935465",
    "-1.37367743",
    "-1.38823473",
    "-1.40393110",
    "-1.42116855",
    "-1.43954507",
    "-1.45815609",
    "-1.47676712",
    "-1.49537815",
    "-1.51398918",
    "-1.53235264",
    "-1.54951363",
    "-1.56504774",
    "-1.57937938",
    "-1.59346345",
    "-1.60754752",
    "-1.62163159",
    "-1.63571566",
    "-1.64969471",
    "-1.66316365",
    "-1.67594244",
    "-1.68821111",
    "-1.70037477",
    "-1.71253842",
    "-1.72470208",
    "-1.73686573",
    "-1.74907483",
    "-1.76150469",
    "-1.77423322",
    "-1.78718251",
    "-1.80017725",
    "-1.81317198",
    "-1.82616672",
    "-1.83916146",
    "-1.85250094",
    "-1.86751489",
    "-1.88479432",
    "-1.90374821",
    "-1.92304686",
    "-1.94234550",
    "-1.96164414",
    "-1.98094279",
    "-1.99988233",
    "-2.01707771",
    "-2.03191333",
    "-2.04500479",
    "-2.05773714",
    "-2.07046950",
    "-2.08320186",
    "-2.09593421",
    "-2.10885295",
    "-2.12267699",
    "-2.13772583",
    "-2.15367997",
    "-2.16982049",
    "-2.18596101",
    "-2.20210153",
    "-2.21824205",
    "-2.23437820",
    "-2.25049315",
    "-2.26657940",
    "-2.28264445",
    "-2.29870513",
    "-2.31476581",
    "-2.33082649",
    "-2.34688717",
    "-2.36247638",
    "-2.37577560",
    "-2.38597659",
    "-2.39388758",
    "-2.40132710",
    "-2.40876663",
    "-2.41620615",
    "-2.42364568",
    "-2.43133709",
    "-2.44025200",
    "-2.45082221",
    "-2.46261591",
    "-2.47466150",
    "-2.48670709",
    "-2.49875268",
    "-2.51079828",
    "-2.52280248",
    "-2.53460564",
    "-2.54613680",
    "-2.55746692",
    "-2.56875566",
    "-2.58004439",
    "-2.59133312",
    "-2.60262185",
    "-2.61410147",
    "-2.62650824",
    "-2.64016938",
    "-2.65475768",
    "-2.66953686",
    "-2.68431604",
    "-2.69909522",
    "-2.71387440",
    "-2.72884452",
    "-2.74474209",
    "-2.76189444",
    "-2.77997422",
    "-2.79824495",
    "-2.81651568",
    "-2.83478642",
    "-2.85305715",
    "-2.87102933",
    "-2.88755140",
    "-2.90211157",
    "-2.91522163",
    "-2.92803314",
    "-2.94084466",
    "-2.95365617",
    "-2.96646768",
    "-2.97883195",
    "-2.98902394",
    "-2.99627695",
    "-3.00135767",
    "-3.00599116",
    "-3.01062465",
    "-3.01525813",
    "-3.01989162",
    "-3.02427303",
    "-3.02743004",
    "-3.02893053",
    "-3.02920663",
    "-3.02923065",
    "-3.02925467",
    "-3.02927870",
    "-3.02930272",
    "-3.02932903",
    "-3.02936650",
    "-3.02941907",
    "-3.02948278",
    "-3.02954879",
    "-3.02961481",
    "-3.02968082",
    "-3.02974683",
    "-3.02981042",
    "-3.02986227",
    "-3.02989822",
    "-3.02992243",
    "-3.02994421",
    "-3.02996600",
    "-3.02998778",
    "-3.03000957",
    "-3.03003082",
    "-3.03004951",
    "-3.03006471",
    "-3.03007734",
    "-3.03008944",
    "-3.03010154",
    "-3.03011364",
    "-3.03012574",
    "-3.03013758",
    "-3.03014815",
    "-3.03015701",
    "-3.03016460",
    "-3.03017193",
    "-3.03017926",
    "-3.03018659",
    "-3.03019392",
    "-3.03020142",
    "-3.03020973",
    "-3.03021913",
    "-3.03022933",
    "-3.03023970",
    "-3.03025007",
    "-3.03026044",
    "-3.03027081",
    "-3.03028051",
    "-3.03028691",
    "-3.03028885",
    "-3.03028750",
    "-3.03028548",
    "-3.03028345",
    "-3.03028142",
    "-3.03027940",
    "-3.03027856",
    "-3.03028348",
    "-3.03029620",
    "-3.03031468",
    "-3.03033435",
    "-3.03035402",
    "-3.03037369",
    "-3.03039336",
    "-3.03046047",
    "-3.03075801",
    "-3.03136730",
    "-3.03220701",
    "-3.03309417",
    "-3.03398132",
    "-3.03486848",
    "-3.03575563",
    "-3.03692003",
    "-3.03752995",
]

nodeID_2_pos = [
    "-1.40026594",
    "-1.40025276",
    "-1.40024272",
    "-1.40023267",
    "-1.40022263",
    "-1.40021259",
    "-1.40020379",
    "-1.40020107",
    "-1.40020656",
    "-1.40021813",
    "-1.40023094",
    "-1.40024376",
    "-1.40025657",
    "-1.40026939",
    "-1.40028118",
    "-1.40028799",
    "-1.40028806",
    "-1.40028316",
    "-1.40027723",
    "-1.40027130",
    "-1.40026537",
    "-1.40025944",
    "-1.40025318",
    "-1.40024534",
    "-1.40023536",
    "-1.40022379",
    "-1.40021190",
    "-1.40020001",
    "-1.40018812",
    "-1.40017623",
    "-1.40016493",
    "-1.40015654",
    "-1.40015206",
    "-1.40015048",
    "-1.40014949",
    "-1.40014851",
    "-1.40014753",
    "-1.40014654",
    "-1.40014614",
    "-1.40014858",
    "-1.40015485",
    "-1.40016395",
    "-1.40017363",
    "-1.40018332",
    "-1.40019301",
    "-1.40020269",
    "-1.40021141",
    "-1.40021545",
    "-1.40021314",
    "-1.40020615",
    "-1.40019819",
    "-1.40019023",
    "-1.40018228",
    "-1.40017432",
    "-1.40016671",
    "-1.40016077",
    "-1.40015711",
    "-1.40015513",
    "-1.40015349",
    "-1.40015185",
    "-1.40015021",
    "-1.40014857",
    "-1.40014672",
    "-1.40014387",
    "-1.40013966",
    "-1.40013444",
    "-1.40012902",
    "-1.40012360",
    "-1.40011817",
    "-1.40011275",
    "-1.40009543",
    "-1.40002036",
    "-1.39986713",
    "-1.39965615",
    "-1.39943327",
    "-1.39921039",
    "-1.39898752",
    "-1.39876464",
    "-1.39855112",
    "-1.39838303",
    "-1.39827640",
    "-1.39821520",
    "-1.39816336",
    "-1.39811152",
    "-1.39805968",
    "-1.39800784",
    "-1.39795791",
    "-1.39791726",
    "-1.39788917",
    "-1.39787036",
    "-1.39785346",
    "-1.39783657",
    "-1.39781967",
    "-1.39780277",
    "-1.39778211",
    "-1.39774316",
    "-1.39767947",
    "-1.39759749",
    "-1.39751175",
    "-1.39742601",
    "-1.39734027",
    "-1.39725453",
    "-1.39695915",
    "-1.39564554",
    "-1.39295431",
    "-1.38924485",
    "-1.38532576",
    "-1.38140666",
    "-1.37748757",
    "-1.37356848",
    "-1.36949638",
    "-1.36468115",
    "-1.35886050",
    "-1.35229671",
    "-1.34557992",
    "-1.33886313",
    "-1.33214635",
    "-1.32542956",
    "-1.31857698",
    "-1.31106485",
    "-1.30266040",
    "-1.29359639",
    "-1.28439659",
    "-1.27519679",
    "-1.26599699",
    "-1.25679719",
    "-1.24763636",
    "-1.23866477",
    "-1.22994922",
    "-1.22142291",
    "-1.21293557",
    "-1.20444822",
    "-1.19596088",
    "-1.18747354",
    "-1.17912364",
    "-1.17144134",
    "-1.16466225",
    "-1.15855077",
    "-1.15257673",
    "-1.14660269",
    "-1.14062865",
    "-1.13465461",
    "-1.12860151",
    "-1.12216436",
    "-1.11520764",
    "-1.10786688",
    "-1.10044706",
    "-1.09302723",
    "-1.08560741",
    "-1.07818758",
    "-1.07073983",
    "-1.06315640",
    "-1.05538942",
    "-1.04748677",
    "-1.03955618",
    "-1.03162560",
    "-1.02369501",
    "-1.01576443",
    "-1.00776991",
    "-0.99946481",
    "-0.99073954",
    "-0.98170370",
    "-0.97260392",
    "-0.96350414",
    "-0.95440435",
    "-0.94530457",
    "-0.93622434",
    "-0.92723908",
    "-0.91838231",
    "-0.90962051",
    "-0.90087826",
    "-0.89213601",
    "-0.88339376",
    "-0.87465151",
    "-0.86581332",
    "-0.85650913",
    "-0.84657448",
    "-0.83617383",
    "-0.82567725",
    "-0.81518066",
    "-0.80468407",
    "-0.79418749",
    "-0.78379602",
    "-0.77391515",
    "-0.76472507",
    "-0.75604558",
    "-0.74747121",
    "-0.73889685",
    "-0.73032248",
    "-0.72174811",
    "-0.71334693",
    "-0.70578695",
    "-0.69936505",
    "-0.69378434",
    "-0.68837682",
    "-0.68296930",
    "-0.67756178",
    "-0.67215426",
    "-0.66640078",
    "-0.65896693",
    "-0.64925964",
    "-0.63787197",
    "-0.62613834",
    "-0.61440471",
    "-0.60267108",
    "-0.59093745",
    "-0.57933728",
    "-0.56838530",
    "-0.55831031",
    "-0.54888353",
    "-0.53959019",
    "-0.53029686",
    "-0.52100353",
    "-0.51171020",
    "-0.50255927",
    "-0.49410002",
    "-0.48657657",
    "-0.47974481",
    "-0.47305544",
    "-0.46636608",
    "-0.45967672",
    "-0.45298736",
    "-0.44601377",
    "-0.43765967",
    "-0.42743781",
    "-0.41583544",
    "-0.40394884",
    "-0.39206225",
    "-0.38017565",
    "-0.36828905",
    "-0.35619350",
    "-0.34308301",
    "-0.32859936",
    "-0.31310079",
    "-0.29739325",
    "-0.28168571",
    "-0.26597817",
    "-0.25027063",
    "-0.23478931",
    "-0.22040670",
    "-0.20751060",
    "-0.19571322",
    "-0.18414205",
    "-0.17257088",
    "-0.16099972",
    "-0.14942855",
    "-0.13821367",
    "-0.12872933",
    "-0.12158633",
    "-0.11617387",
    "-0.11111770",
    "-0.10606153",
    "-0.10100535",
    "-0.09594918",
    "-0.09090944",
    "-0.08594945",
    "-0.08109738",
    "-0.07632508",
    "-0.07156920",
    "-0.06681332",
    "-0.06205743",
    "-0.05730155",
    "-0.05275416",
    "-0.04921941",
    "-0.04705471",
    "-0.04590265",
    "-0.04495909",
    "-0.04401552",
    "-0.04307195",
    "-0.04212838",
    "-0.04123773",
    "-0.04060408",
    "-0.04031816",
    "-0.04028923",
    "-0.04031323",
    "-0.04033722",
    "-0.04036121",
    "-0.04038521",
    "-0.04040872",
    "-0.04042992",
    "-0.04044798",
    "-0.04046373",
    "-0.04047900",
    "-0.04049426",
    "-0.04050953",
    "-0.04052480",
    "-0.04053928",
    "-0.04054997",
    "-0.04055550",
    "-0.04055723",
    "-0.04055818",
    "-0.04055912",
    "-0.04056007",
    "-0.04056102",
    "-0.04056421",
    "-0.04057828",
    "-0.04060708",
    "-0.04064677",
    "-0.04068869",
    "-0.04073062",
    "-0.04077254",
    "-0.04081447",
    "-0.04085609",
    "-0.04089619",
    "-0.04093426",
    "-0.04097081",
    "-0.04100705",
    "-0.04104330",
    "-0.04107954",
    "-0.04111578",
    "-0.04114992",
    "-0.04117385",
    "-0.04118397",
    "-0.04118387",
    "-0.04118167",
    "-0.04117947",
    "-0.04117728",
    "-0.04117508",
    "-0.04118985",
    "-0.04128706",
    "-0.04149580",
    "-0.04178698",
    "-0.04209513",
    "-0.04240328",
    "-0.04271143",
    "-0.04301958",
    "-0.04334851",
    "-0.04377840",
    "-0.04434487",
    "-0.04501230",
    "-0.04570051",
    "-0.04638872",
    "-0.04707693",
    "-0.04776514",
    "-0.04849037",
    "-0.04939537",
    "-0.05054360",
    "-0.05187161",
    "-0.05323664",
    "-0.05460167",
    "-0.05596669",
    "-0.05733172",
    "-0.05933747",
    "-0.06445530",
    "-0.07378362",
    "-0.08622402",
    "-0.09930514",
    "-0.11238626",
    "-0.12546739",
    "-0.13854851",
    "-0.15164238",
    "-0.16479813",
    "-0.17803761",
    "-0.19133897",
    "-0.20465308",
    "-0.21796718",
    "-0.23128129",
    "-0.24459539",
    "-0.25762522",
    "-0.26927428",
    "-0.27905525",
    "-0.28745544",
    "-0.29557136",
    "-0.30368727",
    "-0.31180319",
    "-0.31991911",
    "-0.32804684",
    "-0.33623196",
    "-0.34449472",
    "-0.35281487",
    "-0.36114683",
    "-0.36947879",
    "-0.37781075",
    "-0.38614272",
    "-0.39461820",
    "-0.40379083",
    "-0.41390663",
    "-0.42471956",
    "-0.43567602",
    "-0.44663247",
    "-0.45758893",
    "-0.46854539",
    "-0.47938633",
    "-0.48966620",
    "-0.49918696",
    "-0.50814664",
    "-0.51699081",
    "-0.52583498",
    "-0.53467914",
    "-0.54352331",
    "-0.55205907",
    "-0.55909683",
    "-0.56410789",
    "-0.56762096",
    "-0.57082562",
    "-0.57403028",
    "-0.57723494",
    "-0.58043960",
    "-0.58398430",
    "-0.58918068",
    "-0.59661166",
    "-0.60569431",
    "-0.61511701",
    "-0.62453970",
    "-0.63396240",
    "-0.64338510",
    "-0.65258324",
    "-0.66069071",
    "-0.66732256",
    "-0.67286372",
    "-0.67818034",
    "-0.68349695",
    "-0.68881357",
    "-0.69413018",
    "-0.69951716",
    "-0.70524593",
    "-0.71143711",
    "-0.71797007",
    "-0.72457340",
    "-0.73117673",
    "-0.73778006",
    "-0.74438339",
    "-0.75107671",
    "-0.75820709",
    "-0.76592879",
    "-0.77408755",
    "-0.78233629",
    "-0.79058504",
    "-0.79883379",
    "-0.80708253",
    "-0.81546344",
    "-0.82448625",
    "-0.83437753",
    "-0.84491071",
    "-0.85557605",
    "-0.86624140",
    "-0.87690674",
    "-0.88757208",
    "-0.89796319",
    "-0.90702229",
    "-0.91427928",
    "-0.92020427",
    "-0.92585502",
    "-0.93150577",
    "-0.93715652",
    "-0.94280727",
    "-0.94856658",
    "-0.95485314",
    "-0.96185305",
    "-0.96938021",
    "-0.97701593",
    "-0.98465165",
    "-0.99228738",
    "-0.99992310",
    "-1.00750931",
    "-1.01485507",
    "-1.02187550",
    "-1.02865547",
    "-1.03538594",
    "-1.04211640",
    "-1.04884687",
    "-1.05557734",
    "-1.06250082",
    "-1.07036182",
    "-1.07949123",
    "-1.08955815",
    "-1.09981810",
    "-1.11007804",
    "-1.12033798",
    "-1.13059792",
    "-1.14070494",
    "-1.15006920",
    "-1.15842854",
    "-1.16604513",
    "-1.17350879",
    "-1.18097246",
    "-1.18843612",
    "-1.19589978",
    "-1.20339658",
    "-1.21105428",
    "-1.21892968",
    "-1.22696599",
    "-1.23503543",
    "-1.24310488",
    "-1.25117432",
    "-1.25924376",
    "-1.26733897",
    "-1.27555935",
    "-1.28394908",
    "-1.29246399",
    "-1.30100466",
    "-1.30954534",
    "-1.31808601",
    "-1.32662669",
    "-1.33490918",
    "-1.34193762",
    "-1.34726942",
    "-1.35134718",
    "-1.35516675",
    "-1.35898632",
    "-1.36280589",
    "-1.36662546",
    "-1.37023673",
    "-1.37283626",
    "-1.37406697",
    "-1.37428594",
    "-1.37429661",
    "-1.37430727",
    "-1.37431794",
    "-1.37432861",
    "-1.37433842",
    "-1.37434403",
    "-1.37434398",
    "-1.37433973",
    "-1.37433462",
    "-1.37432951",
    "-1.37432440",
    "-1.37431929",
    "-1.37431485",
    "-1.37431367",
    "-1.37431692",
    "-1.37432343",
    "-1.37433061",
    "-1.37433779",
    "-1.37434497",
    "-1.37435216",
    "-1.37435854",
    "-1.37436102",
    "-1.37435824",
    "-1.37435156",
    "-1.37434408",
    "-1.37433660",
    "-1.37432912",
    "-1.37432164",
    "-1.37431521",
    "-1.37431386",
    "-1.37431941",
    "-1.37433004",
    "-1.37434173",
    "-1.37435341",
    "-1.37436509",
    "-1.37437677",
    "-1.37438776",
    "-1.37439536",
    "-1.37439837",
    "-1.37439799",
    "-1.37439692",
    "-1.37439585",
    "-1.37439477",
    "-1.37439370",
    "-1.37439270",
    "-1.37439203",
    "-1.37439182",
    "-1.37439194",
    "-1.37439214",
    "-1.37439233",
    "-1.37439252",
    "-1.37439272",
    "-1.37439315",
    "-1.37439473",
    "-1.37439786",
    "-1.37440214",
    "-1.37440665",
    "-1.37441117",
    "-1.37441568",
    "-1.37442020",
    "-1.37442417",
    "-1.37442552",
    "-1.37442331",
    "-1.37441847",
    "-1.37441309",
    "-1.37440771",
    "-1.37440233",
    "-1.37439695",
    "-1.37438989",
    "-1.37438619",
]
# Define path to database for pyodrivecan package.

database = pyodrivecan.OdriveDatabase("odrive_data.db")


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


async def smooth_send_positions_to_motor(odrive1, odrive2):
    dt = 0.01
    # Run for set time delay example runs for 15 seconds.
    # stop_at = datetime.now() + timedelta(seconds=30)
    # while datetime.now() < stop_at:

    for pos1, pos2 in zip(nodeID_1_pos, nodeID_2_pos):
        odrive1.set_position(pos1)
        await asyncio.sleep(0.001)
        odrive2.set_position(pos2)
        print(f"Setting motor position to 1: {pos1}")
        print(f"Setting motor position to 2: {pos2}")

        await asyncio.sleep(dt)


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

    # Run for set time delay example runs for 15 seconds.

    stop_at = datetime.now() + timedelta(seconds=30)
    while datetime.now() < stop_at:
        dt = 0.15
        # Iterate over the positions and send them to the motor

        for pos in positions.flatten():
            # odrive1.set_position(pos)

            print(f"Setting motor position to: {pos}")
            await asyncio.sleep(dt)
    odrive1.running = False


# Example of how you can create a controller to get data from the O-Drives and then send motor comands based on that data.


async def controller(odrive1, odrive2, odrive3):
    # odrive1.set_position(0)
    # print("Set odrive to postion 0")
    # odrive2.set_position(0)
    # odrive3.set_position(0)
    # Example usage
    # recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)

    dt = 0.125

    # Run for set time delay example runs for 15 seconds.

    stop_at = datetime.now() + timedelta(seconds=15)
    while datetime.now() < stop_at:
        await asyncio.sleep(0)  # Need this for async to work.
        # print(odrive1.position, odrive2.position)
        # for pos in recorded_positions:
        # odrive1.set_position(pos)
        # await asyncio.sleep(dt)
        # print("Set odrive to postion 0")
        # await asyncio.sleep(3)
        # odrive1.set_position(3)
        # print("Set odrive to postion 3")
        # await asyncio.sleep(3)
    # await asyncio.sleep(15) #no longer need this the timedelta =15 runs the program for 15 seconds.

    odrive1.running = False
    odrive2.running = False
    odrive3.running = False


# Run multiple busses.


async def main():
    # Set up Node_ID 1

    odrive1 = pyodrivecan.ODriveCAN(1, closed_loop_control_flag=True)
    odrive1.initCanBus()

    # Set up Node_ID 2

    odrive2 = pyodrivecan.ODriveCAN(2, closed_loop_control_flag=True)
    odrive2.initCanBus()

    # Set up Node_ID 3

    odrive3 = pyodrivecan.ODriveCAN(3, closed_loop_control_flag=True)
    odrive3.initCanBus()

    # Example usage
    # recorded_times, recorded_positions, _, _ = get_raw_position_over_time(10, 1)
    # total_time = 10  # Total time to complete the path in seconds

    # add each odrive to the async loop so they will run.

    await asyncio.gather(
        odrive1.loop(),
        odrive2.loop(),
        odrive3.loop(),
        # controller(odrive1, odrive2, odrive3),
        smooth_send_positions_to_motor(odrive1, odrive2),
        # send_positions_to_motor(odrive1, positions)
    )


if __name__ == "__main__":
    asyncio.run(main())

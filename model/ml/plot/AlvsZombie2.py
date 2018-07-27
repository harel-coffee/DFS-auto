import numpy as np
import matplotlib.pyplot as plt



accuracy_zombie = np.array([0.05800584174190122, 0.05971853425385024, 0.06293149229952204, 0.06363515666489644, 0.06573287307488052, 0.06716675517790759, 0.06899893786510887, 0.07626128518321824, 0.07728359001593202, 0.07531864046733935, 0.07634094530005311, 0.07604885820499203, 0.079182156133829, 0.08359001593202338, 0.08243494423791821, 0.08174455655868293, 0.083935209771641, 0.08487785448751992, 0.08806425916091344, 0.09301646309081255, 0.09188794476898567, 0.09695963887413703, 0.09559214020180563, 0.09220658523632504, 0.09597716409984068, 0.09845990440785979, 0.09949548592671269, 0.10225703664365374, 0.10540361125862985, 0.10735528412108337, 0.11261285183218268, 0.11498937865108871, 0.11775092936802974, 0.12124269782262345, 0.12615507169410517, 0.1268454593733404, 0.1295804567180032, 0.13535581518852893, 0.1329925650557621, 0.13718799787573022, 0.14167551779075943, 0.14599044078597984, 0.1402549123738715, 0.14514073287307488, 0.14745087626128517, 0.14527349973446627, 0.14492830589484865, 0.1518720127456187, 0.15151354221986194, 0.15585501858736062, 0.15562931492299523, 0.15905469994689325, 0.15734200743494425, 0.15561603823685607, 0.15593467870419542, 0.15690387679235263, 0.15359798194370686, 0.15686404673393523, 0.15695698353690918, 0.15456718003186404, 0.1565719596388741, 0.15864312267657993, 0.1630642591609134, 0.1565321295804567, 0.154845990440786, 0.15451407328730749, 0.15799256505576212, 0.15856346255974513, 0.16185608072225172, 0.15795273499734463, 0.15938661710037175, 0.16030270844397237, 0.15959904407859798, 0.16068773234200745, 0.15938661710037172, 0.16009028146574616, 0.16200212426978228, 0.16159054699946895, 0.16303770578863513, 0.1650557620817844, 0.16587891662241105, 0.169105151354222, 0.16891927774827403, 0.16727296866702074, 0.16824216675517792, 0.16757833244822093, 0.1639537971322358, 0.16483005841741902, 0.16638343069569833, 0.16716675517790758, 0.16959638874137012, 0.1691449814126394, 0.169490175252257, 0.16875995751460432, 0.16958311205523102, 0.16976898566117898, 0.169105151354222, 0.1699150292087095, 0.1696893255443441, 0.17080456718003184])
time_zombie = np.array([0.8689687967300415, 1.3078452348709106, 1.7549347162246705, 2.2171095848083495, 2.6791528940200804, 3.1551707983016968, 3.647134232521057, 4.155094695091248, 4.664036297798157, 5.205277895927429, 5.747273683547974, 6.303445601463318, 6.884105801582336, 7.473022198677063, 8.04958426952362, 8.637885808944702, 9.22367959022522, 9.808480072021485, 10.414209175109864, 11.037391996383667, 11.678797006607056, 12.317204546928405, 12.97173194885254, 13.660099005699157, 14.376899123191833, 15.092448902130126, 15.834449100494385, 16.575988674163817, 17.305757999420166, 18.042117500305174, 18.80425093173981, 19.605642127990723, 20.41954300403595, 21.24172179698944, 22.108739376068115, 22.93812198638916, 23.797355198860167, 24.621499609947204, 25.464365911483764, 26.335591888427736, 27.203358602523803, 28.101931309700014, 29.0146772146225, 29.940623331069947, 30.86171250343323, 31.883026313781738, 32.89136381149292, 33.894778633117674, 34.83113691806793, 35.77612009048462, 36.794192504882815, 37.81520071029663, 38.82480781078338, 39.87678475379944, 40.896096682548524, 41.912110686302185, 42.914589810371396, 43.958440971374515, 45.04232361316681, 46.154723978042604, 47.261860489845276, 48.36600160598755, 49.48408010005951, 50.59044873714447, 51.716428565979, 52.8407347202301, 53.99297747612, 55.16850872039795, 56.366284704208375, 57.54374861717224, 58.737594556808475, 59.94101767539978, 61.173019123077395, 62.40337750911713, 63.636768984794614, 64.93609158992767, 66.19576647281647, 67.45362071990967, 68.71328892707825, 69.95651378631592, 71.22584266662598, 72.51553020477294, 73.82243511676788, 75.15639035701751, 76.52928416728973, 77.87561848163605, 79.25082831382751, 80.63893139362335, 82.03127570152283, 83.45291934013366, 84.86628649234771, 86.25692729949951, 87.69097559452057, 89.16702346801758, 90.61786150932312, 92.06143691539765, 93.50835509300232, 95.05900626182556, 96.63668353557587, 98.21209807395935])



accuracy_clustering = [0.05722251725969198, 0.05722251725969198, 0.057235793945831115, 0.057833244822092414, 0.059625597450876255, 0.061617100371747204, 0.06334306956983536, 0.06460435475305362, 0.0668613913967074, 0.07044609665427509, 0.07296866702071163, 0.07616834838024429, 0.07928836962294211, 0.08748008497079128, 0.09010886882634093, 0.09472915560276156, 0.09957514604354753, 0.10284121083377588, 0.10849707912904938, 0.11557355284121085, 0.11684811471056826, 0.12057886351566652, 0.1218534253850239, 0.12121614445034519, 0.11856080722251724, 0.12150823154540627, 0.11930430164630908, 0.12027349973446629, 0.11911842804036113, 0.12141529474243226, 0.12395114179500796, 0.12614179500796602, 0.12723048327137548, 0.1339086563993627, 0.13947158789166222, 0.13944503451938398, 0.13333775889537972, 0.13295273499734467, 0.1363382899628253, 0.14353425385023896, 0.14613648433351037, 0.14155602761550717, 0.14492830589484865, 0.1451805629314923, 0.14770313329792883, 0.14288369622942115, 0.1455124800849708, 0.14533988316516197, 0.1485661178969729, 0.15098247477429633, 0.15286776420605416, 0.15746149761019648, 0.15815188528943175, 0.15677110993096124, 0.15975836431226767, 0.16139139670738184, 0.16447158789166225, 0.16370154009559215, 0.16439192777482742, 0.1658258098778545, 0.1652018056293149, 0.16832182687201275, 0.1740706319702602, 0.1706186935740839, 0.16739245884227297, 0.17040626659585767, 0.1677110993096123, 0.16178969729155604, 0.16176314391927776, 0.1640467339352098, 0.15755443441317046]
time_clustering = np.array([0.4704603910446167, 0.9425914764404297, 1.4197508811950683, 1.9225783109664918, 2.4235575675964354, 2.935792398452759, 3.4599512100219725, 3.9993200063705445, 4.557330513000489, 5.130778217315674, 5.741201901435852, 6.332160067558289, 6.93572039604187, 7.535355067253112, 8.130404663085937, 8.733567357063293, 9.335773706436157, 9.96022469997406, 10.609791707992553, 11.275785899162292, 11.960897779464721, 12.671154761314392, 13.395733976364136, 14.126766800880432, 14.86618950366974, 15.634028887748718, 16.418536496162414, 17.24189097881317, 18.028101563453674, 18.83422095775604, 19.64961552619934, 20.491428470611574, 21.406596970558166, 22.303738498687743, 23.20130236148834, 24.110703706741333, 25.008490681648254, 25.92334349155426, 26.850559449195863, 27.80902268886566, 28.783007526397704, 29.74175274372101, 30.7281672000885, 31.711924505233764, 32.68846566677094, 33.69668779373169, 34.73538997173309, 35.74479477405548, 36.836293363571166, 37.93296446800232, 39.01753180027008, 40.091840386390686, 41.17760920524597, 42.29333348274231, 43.42109344005585, 44.58064031600952, 45.750243353843686, 46.88629310131073, 48.034959173202516, 49.23732783794403, 50.46615459918976, 51.62207038402558, 52.78977038860321, 54.01186113357544, 55.23184080123902, 56.448948454856875, 57.702634406089786, 58.936259508132935, 60.224737358093265, 61.56727018356323, 62.89340872764588])




accuracy_al = [0.05885554965480616, 0.06002389803505045, 0.06001062134891131, 0.06453797132235793, 0.06298459904407859, 0.06504248539564525, 0.06711364843335103, 0.06995485926712693, 0.0701141795007966, 0.07562400424853956, 0.07780138077535848, 0.08250132766861393, 0.08081518852894318, 0.08113382899628252, 0.08495751460435474, 0.08793149229952205, 0.0947158789166224, 0.09164896441848115, 0.0888210302708444, 0.08422729686670208, 0.0861789697291556, 0.08528943175783324, 0.09179500796601167, 0.09308284652150821, 0.09422464152947423, 0.09596388741370154, 0.0928040361125863, 0.0936404673393521, 0.09518056293149228, 0.09751725969198087, 0.09814126394052045, 0.10200477960701008, 0.10034519383961764, 0.10325278810408922, 0.10330589484864576, 0.10488582049920339, 0.10234997344662773, 0.10467339352097718, 0.11050185873605947, 0.1161710037174721, 0.11741901221455124, 0.11741901221455124, 0.12047265002655339, 0.12623473181094, 0.13060276155071693, 0.13126659585767392, 0.13247477429633564, 0.13718799787573024, 0.1401486988847584, 0.1421402018056293, 0.145246946362188, 0.14289697291556025, 0.14321561338289962, 0.1378252788104089, 0.14138343069569836, 0.144105151354222, 0.14593733404142326, 0.1456718003186405, 0.14871216144450344, 0.1489644184811471, 0.15021242697822623, 0.15310674455655868, 0.15710302708443974, 0.15727562400424855, 0.16074083908656397, 0.15916091343600638, 0.16104620286776422, 0.16548061603823686, 0.16607806691449814, 0.17114976101964946, 0.17340679766330322, 0.17470791290493892, 0.1783590015932023, 0.1770711630377058, 0.17626128518321826, 0.1781864046733935, 0.1795539033457249, 0.17323420074349444, 0.1758364312267658, 0.17914232607541156, 0.18365639936271907, 0.1826872012745619, 0.1792883696229421, 0.17810674455655867, 0.18224907063197024, 0.17996548061603823, 0.1810541688794477, 0.1812267657992565, 0.1831651619755709, 0.18449283058948485, 0.18382899628252786, 0.18627190653212958, 0.18844928305894848, 0.18550185873605948, 0.18836962294211365, 0.18846255974508763, 0.19320233669676048, 0.19695963887413703, 0.1937068507700478, 0.19750398300584174]
time_al = [1.9145783185958862, 3.420080471038818, 4.913273763656616, 6.47207362651825, 7.987259554862976, 9.562533521652222, 11.200302219390869, 12.854183006286622, 14.47935984134674, 16.132082319259645, 17.85032935142517, 19.62189462184906, 21.429228210449217, 23.240399718284607, 25.058423256874086, 26.951394581794737, 28.803102850914, 30.688730716705322, 32.665531921386716, 34.72372660636902, 36.75941531658172, 38.94466934204102, 41.0551025390625, 43.12208797931671, 45.304141497612, 47.49491052627563, 49.68050813674927, 51.81547381877899, 54.018060421943666, 56.2590261220932, 58.53730137348175, 60.8625953912735, 63.150468826293945, 65.52972371578217, 67.94330072402954, 70.31227021217346, 72.77834305763244, 75.43542029857636, 78.10794341564178, 80.76753084659576, 83.43738079071045, 86.13120110034943, 88.97211153507233, 91.75861110687256, 94.49752213954926, 97.2581038236618, 100.04016561508179, 102.83478894233704, 105.66013300418854, 108.48149540424347, 111.27812778949738, 114.09329733848571, 116.98398706912994, 119.84807500839233, 122.78249032497406, 125.92377882003784, 129.02124881744385, 131.98866934776305, 135.03721861839296, 138.1247282266617, 141.3138446331024, 144.45733799934388, 147.6307010412216, 150.88348100185394, 154.3096122264862, 157.74622991085053, 161.14813873767852, 164.50517699718475, 167.92395823001863, 171.32025849819183, 174.715372633934, 178.1779371023178, 181.6178259372711, 185.09840893745422, 188.62322390079498, 192.14781811237336, 195.72318723201752, 199.33427011966705, 203.27061793804168, 206.87353801727295, 210.51078271865845, 214.26480498313904, 217.9912804365158, 221.90385801792144, 225.61808376312257, 229.41061086654662, 233.2478833436966, 237.1105184316635, 240.93460671901704, 244.77428741455077, 248.84398653507233, 252.8732167482376, 256.9071388483047, 260.8815751314163, 264.95085933208463, 269.0284138917923, 273.3211144208908, 277.454544711113, 281.77051124572756, 286.15130681991576]


accuracy_al50 =[0.05869622942113648, 0.05958576739245884, 0.06263940520446096, 0.06585236325013276, 0.06706054168879447, 0.07148167817312799, 0.07205257567711099, 0.0717206585236325, 0.07563728093467871, 0.0785847052575677, 0.07898300584174192, 0.08028412108337757, 0.08491768454593732, 0.0865772703133298, 0.09240573552841211, 0.09640201805629316, 0.09936271906532129, 0.09640201805629314, 0.0955788635156665, 0.08969729155602761, 0.0880509824747743, 0.09044078597981944, 0.09549920339883165, 0.0958842272968667, 0.10492565055762082, 0.10722251725969198, 0.10690387679235262, 0.09811471056824216, 0.10217737652681891, 0.10261550716941052, 0.10469994689325546, 0.10779341476367499, 0.10253584705257568, 0.10711630377057886, 0.10801911842804035, 0.10722251725969198, 0.11059479553903347, 0.11244025491237386, 0.11068773234200742, 0.11330323951141794, 0.11184280403611258, 0.10788635156664897, 0.10546999468932554, 0.10738183749336165, 0.10951938396176313, 0.11220127456186935, 0.1118162506638343, 0.11228093467870419, 0.11444503451938397, 0.11893255443441315, 0.11582580987785449, 0.11824216675517789, 0.1185740839086564, 0.12189325544344129, 0.1229288369622942, 0.11987519915029207, 0.12276951672862454, 0.12373871481678174, 0.12298194370685075, 0.12291556027615509, 0.1257302177376527, 0.1268454593733404, 0.12766861391396706, 0.12847849176845458, 0.13027084439723843, 0.13490440785979818, 0.1362719065321296, 0.13894052044609667, 0.14125066383430698, 0.14298990971853426, 0.14451672862453532, 0.14750398300584172, 0.1527482740308019, 0.15395645246946363, 0.1524163568773234, 0.1525092936802974, 0.14832713754646837, 0.1489245884227297, 0.15126128518321827, 0.15278810408921933, 0.1558284652150823, 0.15860329261816247, 0.16144450345193842, 0.16378120021242695, 0.16545406266595858, 0.16585236325013278, 0.1671667551779076, 0.16909187466808287, 0.17108337758895378, 0.1719198088157196, 0.1717604885820499, 0.1734997344662772, 0.17801380775358472, 0.17737652681890598, 0.17938130642591613, 0.17997875730217738, 0.18146574614976102, 0.1802575677110993, 0.18157195963887413, 0.18000531067445563]
time_al50 =[1.4134501218795776, 2.385093879699707, 3.3673494338989256, 4.358350014686584, 5.343690586090088, 6.360514736175537, 7.389381313323975, 8.445897650718688, 9.558845400810242, 10.651835298538208, 11.779010891914368, 12.931541800498962, 14.092004227638245, 15.283008432388305, 16.47859654426575, 17.69481964111328, 18.879482436180115, 20.088304591178893, 21.314147210121156, 22.559076499938964, 23.806452584266662, 25.084192299842833, 26.358600306510926, 27.711117959022523, 29.077657794952394, 30.45695552825928, 31.895810294151307, 33.29482905864715, 34.72770118713379, 36.19336829185486, 37.64197690486908, 39.13666157722473, 40.62660191059113, 42.15714931488037, 43.696458792686464, 45.26302533149719, 46.857320833206174, 48.45011830329895, 50.083452463150024, 51.77804982662201, 53.46062788963318, 55.140355825424194, 56.806351804733275, 58.52193429470062, 60.314776635169984, 62.10540742874146, 63.88935439586639, 65.68708987236023, 67.49068517684937, 69.31065273284912, 71.13241043090821, 72.96123919486999, 74.83652038574219, 76.7296745300293, 78.67691342830658, 80.63606331348419, 82.63355271816253, 84.62775979042053, 86.67493689060211, 88.73622620105743, 90.79969501495361, 92.89096105098724, 94.96572837829589, 97.14995379447937, 99.40054240226746, 101.62354667186737, 103.87428941726685, 106.14847490787506, 108.35764472484588, 110.57612590789795, 112.81104238033295, 115.07321870326996, 117.3871634721756, 119.85568130016327, 122.28390154838561, 124.79849028587341, 127.24085595607758, 129.75288457870482, 132.338281416893, 134.88316051959993, 137.3599675655365, 139.9125808954239, 142.43794689178466, 145.00174419879914, 147.58180549144745, 150.1741925239563, 152.78859708309173, 155.402410531044, 158.03648481369018, 160.68421678543092, 163.40054361820222, 166.12970468997955, 168.8832159757614, 171.58247103691102, 174.29691929817199, 177.11555919647216, 179.89679799079894, 182.75021011829375, 185.73950328826905, 188.65911140441895]


accuracy_al10 =[0.05910780669144981, 0.06063462559745088, 0.0625862984599044, 0.06481678173127987, 0.06792352628783857, 0.07158789166224111, 0.07343335103558152, 0.07295539033457249, 0.07446893255443442, 0.07924853956452468, 0.08287307488050981, 0.08236856080722252, 0.08230217737652681, 0.08563462559745087, 0.08531598513011153, 0.08759957514604355, 0.09150292087095062, 0.09032129580456719, 0.09433085501858737, 0.09228624535315985, 0.09356080722251725, 0.09507434944237918, 0.09674721189591079, 0.09847318109399893, 0.09958842272968668, 0.10346521508231546, 0.10208443972384493, 0.1073685608072225, 0.11490971853425384, 0.11351566648964417, 0.11804301646309082, 0.12411046202867766, 0.1257700477960701, 0.1254381306425916, 0.12700477960701012, 0.12142857142857141, 0.12173393520977165, 0.12064524694636221, 0.12391131173659056, 0.13036378120021241, 0.12936802973977696, 0.1329660116834838, 0.13632501327668617, 0.13706850770047796, 0.14101168348380244, 0.1380111524163569, 0.14009559214020179, 0.1370552310143388, 0.14105151354221984, 0.14279075942644714, 0.14310939989378652, 0.14204726500265535, 0.14053372278279339, 0.14265799256505574, 0.14584439723844927, 0.1485661178969729, 0.14792883696229422, 0.14499468932554435, 0.14316250663834304, 0.14607010090281464, 0.14895114179500796, 0.14831386086032924, 0.1489909718534254, 0.1511683483802443, 0.1505045140732873, 0.15132766861391397, 0.154845990440786, 0.15744822092405736, 0.15796601168348381, 0.15743494423791818, 0.16145778013807754, 0.1602761550716941, 0.16294476898566118, 0.16352894317578334, 0.16505576208178438, 0.16468401486988848, 0.16391396707381836, 0.16326340945300052, 0.1650557620817844, 0.16540095592140203, 0.17085767392458845, 0.1733935209771641, 0.17862453531598513, 0.18291290493892726, 0.18485130111524162, 0.18722782793414766, 0.18482474774296337, 0.1834970791290494, 0.1832049920339883, 0.18070897503983005, 0.18267392458842274, 0.18482474774296337, 0.18680297397769516, 0.1837758895379713, 0.18570100902814657, 0.18636484333510356, 0.18908656399362717, 0.19151619755708976, 0.1942379182156134, 0.1958576739245884]
time_al10 =[1.0624226570129394, 1.6357703447341918, 2.248488998413086, 2.880932426452637, 3.5064125061035156, 4.134105086326599, 4.755466508865356, 5.388640022277832, 6.040355515480042, 6.724285411834717, 7.409491419792175, 8.115690541267394, 8.820300340652466, 9.536146116256713, 10.238152551651002, 10.951760029792785, 11.675907683372497, 12.452481627464294, 13.218264889717101, 14.038079857826233, 14.876784324645996, 15.74214277267456, 16.594607949256897, 17.442124009132385, 18.286010122299196, 19.12484440803528, 19.988093185424805, 20.85152292251587, 21.727959394454956, 22.605611705780028, 23.511697912216185, 24.43574333190918, 25.3654803276062, 26.317523527145386, 27.287298011779786, 28.25286931991577, 29.238122844696044, 30.2370717048645, 31.25136806964874, 32.29071238040924, 33.33822295665741, 34.40790376663208, 35.517196726799014, 36.65633330345154, 37.81244702339173, 38.92502202987671, 40.052444553375246, 41.1759281873703, 42.324346494674685, 43.519205808639526, 44.7169046163559, 45.941720724105835, 47.17177841663361, 48.3911150932312, 49.621935319900516, 50.865544128417966, 52.16116211414337, 53.48320963382721, 54.82324213981629, 56.14135038852692, 57.562981033325194, 58.96460094451904, 60.384470438957216, 61.80106072425842, 63.16588802337647, 64.52600343227387, 65.90733513832092, 67.30839903354645, 68.71449744701385, 70.13652300834656, 71.58124179840088, 73.07507801055908, 74.57608184814453, 76.06802492141723, 77.57993116378785, 79.1724058151245, 80.76144278049469, 82.41000628471375, 84.00995647907257, 85.57639758586883, 87.14189915657043, 88.72396802902222, 90.3080726146698, 91.90559873580932, 93.53796620368958, 95.17055740356446, 96.81985540390015, 98.50863411426545, 100.21179659366608, 101.95071198940278, 103.67653241157532, 105.37988252639771, 107.13578140735626, 108.93951101303101, 110.73871092796325, 112.55381259918212, 114.43066861629487, 116.2628569841385, 118.18775413036346, 120.12078821659088]

print len(accuracy_clustering)
print len(time_clustering)

time_zombie += 10
time_clustering += 10


fig, ax = plt.subplots()
ax.plot(time_clustering, accuracy_clustering, label='Clustering', linewidth=3)
ax.plot(time_zombie, accuracy_zombie, label='ZOMBIE', linewidth=3)

plt.axvline(x=time_clustering[70])

ax.set_ylabel('Test Accuracy')
ax.set_xlabel('Runtime')

ax.legend(loc=0)

plt.show()



fig, ax = plt.subplots()
ax.plot(time_al, accuracy_al, label='Active Learning', linewidth=3)
ax.plot(time_al50, accuracy_al50, label='Active Learning 50%', linewidth=3)
ax.plot(time_al10, accuracy_al10, label='Active Learning 10%', linewidth=3)
ax.plot(time_zombie, accuracy_zombie, label='ZOMBIE', linewidth=3)

plt.axvline(x=time_zombie[70])

ax.set_ylabel('Test Accuracy')
ax.set_xlabel('Runtime')

ax.legend(loc=0)

plt.show()




fig, ax = plt.subplots()
ax.plot(range(len(accuracy_al)), accuracy_al, label='Active Learning', linewidth=3)
ax.plot(range(len(accuracy_zombie)), accuracy_zombie, label='ZOMBIE', linewidth=3)

plt.axvline(x=70)

ax.set_ylabel('Test Accuracy')
ax.set_xlabel('Size of Training Set')

ax.legend(loc=0)

plt.show()
import numpy as np
import matplotlib.pyplot as plt

al = [0, 0.057222517259691984, 0.055098247477429634, 0.055496548061603826, 0.05616038236856081, 0.05682421667551779, 0.056691449814126396, 0.05921402018056293, 0.059877854487519915, 0.059877854487519915, 0.059877854487519915, 0.0604089219330855, 0.06147105682421668, 0.06173659054699947, 0.06651619755708975, 0.06757833244822092, 0.07142857142857142, 0.07222517259691981, 0.07434944237918216, 0.08151885289431758, 0.10740839086563994, 0.07992565055762081, 0.08005841741901222, 0.08032395114179501, 0.0807222517259692, 0.08112055231014338, 0.08324482209240573, 0.08550185873605948, 0.08563462559745087, 0.08961763143919278, 0.09081253319171535, 0.10169941582580988, 0.08112055231014338, 0.08616569304301647, 0.08616569304301647, 0.08669676048858205, 0.08682952734997344, 0.08682952734997344, 0.08696229421136484, 0.08722782793414764, 0.09028146574614976, 0.09054699946893255, 0.09625597450876261, 0.09851301115241635, 0.10103558151885289, 0.10329261816250664, 0.10847052575677112, 0.10913436006372809, 0.11617100371747212, 0.1172331386086033, 0.12626128518321827, 0.12838555496548062, 0.1290493892724376, 0.13210302708443972, 0.1404673393520977, 0.14352097716409984, 0.14352097716409984, 0.15215082315454062, 0.16317047265002654, 0.1647636749867233, 0.12413701540095592, 0.12413701540095592, 0.12719065321295805, 0.1051513542219862, 0.10939989378651088, 0.10939989378651088, 0.11537440254912373, 0.12745618693574085, 0.12772172065852364, 0.137546468401487, 0.13781200212426978, 0.14298990971853426, 0.14843335103558153, 0.14976101964949548, 0.1534784917684546, 0.1609134360063728, 0.16449814126394052, 0.1654275092936803, 0.16795007966011682, 0.17180031864046733, 0.1810939989378651, 0.18494423791821563, 0.18494423791821563, 0.18799787573021773, 0.19715878916622412, 0.1975570897503983, 0.1975570897503983, 0.2056558682952735, 0.21189591078066913, 0.21561338289962825, 0.21561338289962825, 0.19437068507700478, 0.20751460435475305, 0.21070100902814656, 0.21640998406797662, 0.22517259691980882, 0.2261019649495486, 0.23592671269251195, 0.24668082846521508, 0.24774296335634627, 0.2547796070100903, 0.26779075942644714]
zombie = [0, 0.057222517259691984, 0.059612320764737124, 0.061072756240042485, 0.0646574614976102, 0.0647902283590016, 0.06505576208178439, 0.06664896441848114, 0.07063197026022305, 0.07395114179500796, 0.07474774296335635, 0.08430695698353691, 0.09200743494423792, 0.10209771640998407, 0.10223048327137546, 0.11245353159851301, 0.11417950079660116, 0.11417950079660116, 0.08616569304301647, 0.08616569304301647, 0.09399893786510886, 0.096388741370154, 0.09891131173659054, 0.11789697291556028, 0.12028677642060542, 0.12028677642060542, 0.12068507700477961, 0.14312267657992564, 0.14591078066914498, 0.14617631439192777, 0.16423260754115773, 0.17246415294742432, 0.17591609134360064, 0.1812267657992565, 0.17644715878916623, 0.18228890069038767, 0.18481147105682422, 0.1898566117896973, 0.19941582580987785, 0.19503451938396177, 0.19516728624535315, 0.19569835369091876, 0.21866702071163038, 0.21893255443441317, 0.1737918215613383, 0.17551779075942645, 0.17565055762081785, 0.17565055762081785, 0.17604885820499203, 0.18242166755177908, 0.1861391396707382, 0.20233669676048857, 0.16715347849176845, 0.16715347849176845, 0.1775092936802974, 0.1735262878385555, 0.18866171003717472, 0.15042485395645247, 0.15042485395645247, 0.15878916622411046, 0.15892193308550187, 0.16317047265002654, 0.16317047265002654, 0.1691449814126394, 0.1453797132235794, 0.1488316516197557, 0.1577270313329793, 0.15998406797663303, 0.17113648433351036, 0.17458842272968667, 0.18255443441317049, 0.18348380244291024, 0.18374933616569306, 0.18653744025491237, 0.18693574083908657, 0.18693574083908657, 0.18693574083908657, 0.18773234200743494, 0.18826340945300052, 0.18866171003717472, 0.1899893786510887, 0.1899893786510887, 0.19038767923526287, 0.19583112055231014, 0.19622942113648434, 0.19622942113648434, 0.1974243228890069, 0.1974243228890069, 0.2047265002655337, 0.2056558682952735, 0.2055231014338821, 0.20671800318640468, 0.2099044078597982, 0.209506107275624, 0.22105682421667552, 0.2217206585236325, 0.22623473181093998, 0.22411046202867765, 0.2257036643653744, 0.22809346787041954, 0.22809346787041954, 0.22809346787041954]


fig, ax = plt.subplots()
ax.plot(range(len(al)), al, label='Active Learning')
ax.plot(range(len(zombie)), zombie, label='ZOMBIE')

plt.axvline(x=70)

ax.set_ylabel('Test Accuracy')
ax.set_xlabel('Size of Trainng Set')

ax.legend(loc=0)

plt.show()
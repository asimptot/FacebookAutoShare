import time
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *
from selenium.webdriver.common.action_chains import ActionChains

class FBPost:
    def setup(self):
        Setup.login(self)

    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        time.sleep(4)
        self.browser.get(group_url)
        time.sleep(2)

        text_to_post = '10.000+ km az kullanılmış, sahibinden 2020 model Clio. ' \
                       'İnternete bağlanan multimedya da içerikte mevcuttur. ' \
                       'Değişeni ve boyalı parçası yoktur.\n\n' \
                        'ilan linkini asagiya birakiyorum. ^^\n\n' \
                       'https://www.sahibinden.com/ilan/vasita-otomobil-renault-10.000-plus-km-az-kullanilmis-multimedyali-2020-model-clio-1046886621/detay/'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions = actions.send_keys(text_to_post)
        actions.perform()
        time.sleep(5)
        Setup.send_post(self)

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

araba = ["1712520632328326", "satilikarabailanlarii", "912325275445660", "725880574183459",
         "280689246332246", "552077451969938", "891432410953276", "turkiyeucuzaraba",
         "1999454820117187", "236886856829858", "757991430978047", "1043698118988448",
         "157949357956982", "125201876125378", "1553378708323448", "328064497604475",
         "1622954454588745", "1600395430201493", "2278837215735235", "1741915946036931",
         "1977045505936111", "kayseriikincielaraba", "1847520892132643", "388149651578405",
         "568306859986232", "177753004080514", "1804913393067179", "331835926980955",
         "413197749021198", "510546992446382", "1389316448058215", "erzurumikincielarabam",
         "Sivas2.ElArabaAlimSatim", "1446602842038143", "1581787365415048", "350208778520515",
         "1788953141320253", "1596124727273232", "629774913793364", "1441736839459994",
         "463826013795233", "397696947046355", "Diyarbakirikincielotoalimsatim", "889872241062548",
         "1760689137492540", "1850408268526034", "1565266633684986", "755337207901911", "335857923470730",
         "1608475462779854", "1811986482399657", "239783429735104"]

list = sample(araba, len(araba))

for i in range(len(araba)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

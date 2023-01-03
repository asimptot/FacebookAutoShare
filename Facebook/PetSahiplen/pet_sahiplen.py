import time
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *

class FBPost:
    def setup(self):
        Setup.login(self)

    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        time.sleep(4)
        self.browser.get(group_url)
        time.sleep(2)

        text_to_post = 'Merhaba arkadaşlar. PetSahiplen uygulaması artık Play Store''da! :)\n\n' \
                       'PetSahiplen ile artık evcil hayvanınıza sahip bulmak ve evcil hayvan sahiplenmek çok kolay. İçerikte: \n\n' \
                       '-Sahiplendirme Forumu\n' \
                       '-Kayıp Hayvan İhbar Forumu\n' \
                       '-Sohbet Özelliği\n' \
                       '-Çevrenizdeki Kişileri Görüntüleme\n' \
                       '-Haberler\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=petsahiplen.appxcb'

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

pet = ["huncalife35", "474842530016186", "kedikopekkussahiplendirme", "1065479390549253", "172459679848313",
       "izmirevcilhayvansahiplendirme", "607228792818322", "1317939498358641", "1256977574457496",
       "788584284552115", "533015283518913", "233571787510866", "2088427014800493", "412783958820720",
       "827540141115373", "1428188010818868", "594771670732498", "KopekSahiplendirme",
       "397204243774401", "hekimhanemersin", "163263510678375", "petdost06", "283106478550596",
       "2015921291971098", "2135577956687291", "867425070105002", "KopekSahiplendirme", "2235052526771916"]

list = sample(pet, len(pet))

for i in range(len(pet)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

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

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Değerli Kahta''mız artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Spor Haberleri\n' \
                       '-2.El Alım Satımlar\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Video Galeri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=kahta.lesi'

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

kahta = ["1624628781122113", "kahtakursu", "135970510441878", "589953031080035", "1625258187768294",
         "kahtayerelhaberler", "1488085274775480", "1647475768659710", "2388501501384981",
         "1847520892132643", "264388660669880", "699968396734840", "733411733471574", "327329167317350",
         "1518346504939007", "1831131667169122", "1753788418236087", "kahtagurbet"]

list = random.choice(kahta)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

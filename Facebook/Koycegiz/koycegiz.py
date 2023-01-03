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

        text_to_post = 'Güzel Köyceğiz''imin güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Köyceğiz İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Hal fiyatları\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Etkinlikler Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Video Galeri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.kyceiz.belediyesi'

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

koycegiz = ["1825550977701612", "1897150360563786", "koycegiz.kultur.sanat", "dursan48", "298189850576492",
            "101323133800031", "121712639052347", "256353364777997", "2909366672472920", "429940847106583",
            "559618474635468", "633634556772916", "stuffforsaleinkoycegiz", "163837907318247", "koycegizliyiz",
            "769021773258398", "802498176776999", "628767133957951"]

list = random.choice(koycegiz)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

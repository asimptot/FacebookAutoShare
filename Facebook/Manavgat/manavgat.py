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

        text_to_post = 'Güzel Manavgat''ımın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Manavgat İlçesi Play Store''da. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Spor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.manavgat.ilesi'

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

manavgat = ["1977654352501132", "152068948488893", "mangpz", "1235365273171718", "775320699267828",
            "1235437996536777", "269742907469940", "930377517038925", "216353675048716", "291503291352138",
            "343882795972237", "340120006345513", "1427277477512901", "810606215692882", "MANAVGAT2.ELPAZARI",
            "1847193255610019", "131161735437", "2000058830216565", "952443884824039", "209939369412433",
            "316784738707982", "1289244694459337", "945037175514343", "369677536786148", "407676326728979",
            "antalyateknealimsatim", "556712624481818"]

list = sample(manavgat, len(manavgat))

for i in range(len(manavgat)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

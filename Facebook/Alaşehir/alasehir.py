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

        text_to_post = 'Güzel Alaşehir''imin güzel insanları selamlar :)\n\n' \
                       'Mahallemiz Alaşehir İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Alaşehir Belediyespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.alaehir.ilesi'

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

alasehir = ["2482168202011446", "202346793639366", "203321580789724", "325220324225839", "1544979455609019", "1171012322964102",
            "729868704016034", "201187294327815", "735596626622864", "alasehirmuhabbet", "826697807434059", "alasehir.ulastirma",
            "496732401291955", "728139434428844", "857808581348055", "747661711923559", "566967630721933",
            "alasehirkiraliksatilikgayrimenkul", "434969670469315"]

for i in range(len(alasehir)):
    group_url = 'https://www.facebook.com/groups/' + alasehir[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
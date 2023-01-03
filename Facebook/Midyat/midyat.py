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
                       'Güzel Midyat''ımız artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-2.El Alım Satımlar\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=midyat.lesi'

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

midyat = ["366476150457472", "sevmektir.hedefimiz", "1657378104514078", "alsatikinciel", "midyatemlak",
          "179094605850162", "1858269431150159", "470681069789097", "6368330842", "midyatlilar", "644401365905547",
          "1583251101970768", "225415168351155", "1361704113856904", "320887686013399", "313527519293261",
          "302366493292190", "229982831566921", "1465378513718674", "733019106813950", "581408198549755",
          "437918623320210", "121644048494414", "973061699487117", "1219335254826260", "midyatsesi",
          "885727298193074", "1578130905807740", "820976911247639", "1010368612751341", "203263053485392",
          "586826778193137", "78777212424", "1103062410143331", "1767734176819749", "218407871507361",
          "2825560511057826", "674538589383416", "953375348014387", "1276311579152352", "1713153065572642",
          "midyat.ogretmenler"]

list = random.choice(midyat)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

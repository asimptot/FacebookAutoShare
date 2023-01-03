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

        text_to_post = 'Güzel Torbalı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Torbalı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Torbalıspor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=torbal.lesi'

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

torbali = ["1674448666166233", "torbalidais", "1674152716182011", "TRMEHMET", "3815981261797816", "1260348790815554",
           "2153944177989877", "1719536631616508", "531570480830339", "815312195557528", "1138779186487991",
           "992472454146407", "160202221998957", "461181397343488", "652045991632541", "194760451278928",
           "1581787365415048", "281538418715072", "1232530130137892", "827540141115373", "tobedak",
           "343288555591", "275915996290129", "624143651345231", "213121952562502", "3737007473081269"]

list = random.choice(torbali)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

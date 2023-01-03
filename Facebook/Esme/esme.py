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

        text_to_post = 'Güzel Eşme''min güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Eşme İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Hava Durumu\n' \
                       '-Yöresel Türküler\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Eşmespor Haberleri\n' \
                       '-Elektrik Arızaları\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.eme.ilesi'

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

esme = ["762951934454642", "1493055600830700", "452448632246858", "1030065057498284", "dervislikoyu", "422335515606986",
		"1562201027378354", "2323050764478917", "531806510545262", "1419604838253392", "574000413548546",
		"546914658780031", "1986018184978764", "662521437623764", "sivaslialsat", "796198000551872", "2462719980412101",
		"3115960435151650", "2302795416666275", "1751474938464718", "599522303449499", "180888425302580", "esmeet",
        "539569122884209", "515028112596989", "694003467429707"]

list = sample(esme, len(esme))

for i in range(len(esme)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

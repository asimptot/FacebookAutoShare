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

        text_to_post = 'Güzel Tavşanlı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Tavşanlı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Tavşanlı Belediyespor Haberleri\n' \
                       '-Elektrik Arızaları\n' \
                       '-Otobüs Saatleri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.tavanl.ilesi'

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

tavsanli = ["371521519658763", "2918986854785156", "203459223082833", "2095593284007825", "228511447587069",
            "1173935345995444", "318440788856233", "1783132881980335", "315152158878955", "142750250061341",
            "516140542385739", "383714302106284", "227459675083900", "723145614498513", "172594656722810",
            "1407897382839919", "243999833363938", "1009042875800957", "denizfeneritvsnl", "1415263425384958",
			"809726322875281", "438267427067482", "363401537388279", "1736313896533707", "1485263505113239",
            "590879721047611", "216310852991424"]

list = random.choice(tavsanli)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

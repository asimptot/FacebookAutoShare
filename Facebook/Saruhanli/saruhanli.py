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

        text_to_post = 'Güzel Saruhanlı''mın güzel insanları selamlar :)\n\n' \
                       'Yeni uygulamam Saruhanlı İlçesi Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n-Restoranlar\n' \
                       '-Taksiler\n-' \
                       '-Hava Durumu\n-' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Saruhanlı Belediyespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.saruhanl.ilesi'

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

saruhanli = ["3621892841232883", "625696608295240", "1026591190722191", "362381121834180", "323770108257399",
             "523087858374479", "yeniosmaniye", "1869857186600915", "200216664433261", "121237668553899",
             "1712520632328326", "2593150607677028", "217516450021487", "877884799676171", "399218583842570",
             "654117541890123", "112334160927"]

for i in range(len(saruhanli)):
    group_url = 'https://www.facebook.com/groups/' + saruhanli[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
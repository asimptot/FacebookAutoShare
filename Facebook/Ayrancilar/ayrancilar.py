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

        text_to_post = 'Güzel Ayrancılar''ımın güzel insanları selamlar :)\n\n' \
                       'Mahallemiz Ayrancılar Play Storeda. İçerikte neler mi var?\n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Ayrancılar Gençlikspor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=com.ayranclar'

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

ayrancilar = ["ayrancilar", "281538418715072", "2059423444286714", "516400849066648", "289817535039125",
			  "1674448666166233", "1586603538128730", "2240938972810805", "1192618434087801", "238656837475420",
			  "333284927980868", "2460181387617813", "167141027960807", "torbalidais", "1068832396815501",
			  "207248929672296", "131859181017957", "453756859346524", "712485366009386", "3441863649184399"]

list = sample(ayrancilar, len(ayrancilar))

for i in range(len(ayrancilar)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

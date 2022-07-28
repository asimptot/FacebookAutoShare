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

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Güzel Söke''miz artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Sökespor Haberleri\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Vefat Edenler\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=ske.lesi'

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

soke = ["718233511622533", "2198720647021293", "2614247848875259",
		"183032711887971", "284487099047799", "663096097179649", "651769814943857",
		"360540204506455", "1624229481102064", "331315010781464", "287030981364401",
		"1397160103912534", "624735251481542", "160022984027457",
		"1007108702776331", "1724842091109410", "447280948738495", "1598433740486562",
		"1652649881642707", "113022235388425", "1083834084969974", "107121203140839", "331835926980955"]

for i in range(len(soke)):
    group_url = 'https://www.facebook.com/groups/' + soke[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
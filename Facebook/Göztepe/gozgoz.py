import time
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *
from selenium.webdriver.common.action_chains import ActionChains

class FBPost:
    def setup(self):
        Setup.login(self)
        time.sleep(2)
        submit_button = self.browser.find_element_by_name('login')
        submit_button.click()
        time.sleep(2)
        self.browser.get('https://www.facebook.com/')

    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        time.sleep(4)
        self.browser.get(group_url)
        time.sleep(2)

        text_to_post = 'Değerli abilerim, sevgili kardeşlerim. GözGöz Sözlük uygulaması artık Play Store''da! :)\n\n' \
                       'İçerikte: \n\n' \
                       '-Maç bileti devretme, paylaşım vb. işlemleri yapabileceğiniz forum özelliği\n' \
                       '-Sohbet özelliği\n' \
                       '-Göztepe ile ilgili güncel haberler\n' \
                       '-Çevrenizdeki Göztepelileri görme\n' \
                       '-Marşlar\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=gozgoz.sozluk'

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

goztepe = ["632261113598528", "567832526708370", "278916619179669", "169197057727346", "1743504639157693", "122154371830585",
           "goztepecom", "1843095909327694", "goztepenineskileri", "139935412764982", "330761873609935", "256830128397118",
           "208028558536", "1482691535388761", "1540597852877697", "159424877529948", "332225360477262", "2730901190498018",
           "575389225857771", "1194038040638929", "wwwisoookubra", "229136775939229", "259943855903893",
           "416889008451550", "163485201272958", "259820858593897", "453152851683911", "257968525316500", "680538306155255",
           "156296471231004", "384831866221969", "202802114364116", "368964550120282", "1119653814739937", "936992506365153",
           "210922582375185", "154982691215447"]

for i in range(len(goztepe)):
    group_url = 'https://www.facebook.com/groups/' + goztepe[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
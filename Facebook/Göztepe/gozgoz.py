import time
import re
from bs4 import BeautifulSoup
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *
from selenium.webdriver.common.action_chains import ActionChains

class FBPost:
    def setup(self):
        Login.login(self)
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

        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element_by_class_name(post_class)
            click_post.click()
            time.sleep(5)

            actions = ActionChains(self.browser)
            actions = actions.send_keys(text_to_post)
            actions.perform()
            time.sleep(5)

            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
            id_ = str(all_pc[0].get('id'))
            xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div'
            post = self.browser.find_element_by_xpath(xpath)
            post.click()
            time.sleep(5)

        except:

            print("Something went wrong, exiting script to avoid conflicts")

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

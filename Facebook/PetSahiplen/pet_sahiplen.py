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

        text_to_post = 'Merhaba arkadaşlar. PetSahiplen uygulaması artık Play Store''da! :)\n\n' \
                       'PetSahiplen ile artık evcil hayvanınıza sahip bulmak ve evcil hayvan sahiplenmek çok kolay. İçerikte: \n\n' \
                       '-Sahiplendirme Forumu\n' \
                       '-Kayıp Hayvan İhbar Forumu\n' \
                       '-Sohbet Özelliği\n' \
                       '-Çevrenizdeki Kişileri Görüntüleme\n' \
                       '-Haberler\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=petsahiplen.appxcb'

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
            #sys.exit()

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

pet = ["huncalife35", "474842530016186", "kedikopekkussahiplendirme", "kedidostlarimiz", "1065479390549253",
       "izmirevcilhayvansahiplendirme", "607228792818322", "184081478662359", "1317939498358641", "1256977574457496",
       "788584284552115", "533015283518913", "233571787510866", "2088427014800493", "istanbulhayvansahiplendirme",
       "827540141115373", "245489422612202", "1428188010818868", "594771670732498", "KopekSahiplendirme",
       "400305423477123", "397204243774401", "hekimhanemersin", "163263510678375", "petdost06", "283106478550596",
       "2015921291971098", "2135577956687291", "867425070105002", "155015494670718", "153701498300383", "1310366372336233",
       "465906316799333", "KopekSahiplendirme", "2235052526771916", "399654688221686", "145702959520939",
       "172459679848313", "157031514849682", "471120629709284", "412783958820720"]


for i in range(len(pet)):
    group_url = 'https://www.facebook.com/groups/' + pet[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
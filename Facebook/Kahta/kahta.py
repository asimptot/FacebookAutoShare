import time
import re
from bs4 import BeautifulSoup
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Facebook')
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

        text_to_post = 'Sayın abilerim, ablalarım, sevgili kardeşlerim,\n' \
                       'Değerli Kahta''mız artık cep telefonumuzda. İlçemizle ilgili: \n\n' \
                       '-İş İlanları\n' \
                       '-Haberler\n' \
                       '-Spor Haberleri\n' \
                       '-2.El Alım Satımlar\n' \
                       '-Restoranlar\n' \
                       '-Taksiler\n' \
                       '-Hava Durumu\n' \
                       '-Nöbetçi Eczaneler\n' \
                       '-Su-Elektrik Arızaları\n' \
                       '-Video Galeri\n' \
                       '-Fotoğraf Galerisi\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=kahta.lesi'

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

kahta = ["1624628781122113", "kahtakursu", "135970510441878", "589953031080035", "1625258187768294",
         "kahtayerelhaberler", "1488085274775480", "633958143394456", "1647475768659710", "2388501501384981",
         "1847520892132643", "264388660669880", "699968396734840", "733411733471574", "327329167317350",
         "1518346504939007", "1831131667169122", "1753788418236087", "kahtagurbet"]

for i in range(len(kahta)):
    group_url = 'https://www.facebook.com/groups/' + kahta[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

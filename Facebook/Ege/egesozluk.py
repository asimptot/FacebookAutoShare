import time
import re
from bs4 import BeautifulSoup
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *

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

        text_to_post = 'Ege Üniversitesi sözlük uygulaması artık Play Market''te! :)\n' \
                       'İçerikte:\n\n' \
                       '-Paylaşım yapabileceğiniz sözlük bölümü\n' \
                       '-2. El Alım Satım\n' \
                       '-İş İlanları\n' \
                       '-Ev Arkadaşı Bulma\n' \
                       '-Çevrenizdeki Sözlük Kullanıcılarını Görüntüleme\n' \
                       '-Sohbet Özelliği\n' \
                       'özellikle mevcuttur. İyi günlerde kullanmanız temennimizle :)\n\n' \
                       'https://play.google.com/store/apps/details?id=ege.sozluk'


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

sozluk = ["egeevarkadasi", "1430596860532102", "254187258119986", "TopluluklarEge", "379934872198429", "egenso",
          "egeogrencileri", "Egeparttime", "18019857931", "215182778504930", "5272033731", "1480104958897419",
          "430556560443037", "egealimvesatim", "kucukmendereshavzasi", "egeunialimsatim", "66151379408",
          "ulitege", "1382454552016358", "5227134462", "220261332183076", "egeunibisiklet",
          "deuevarkadasi", "17657058816", "169716939731794", "1207874752574624", "9252779851",
          "6104626645", "18659112496", "748088955207007", "161523990674375", "226917504020810", "egeuniversitesigezi",
          "172110019647"]

list = random.choice(sozluk)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

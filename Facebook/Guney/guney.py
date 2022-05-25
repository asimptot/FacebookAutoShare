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

        text_to_post = 'Yenilenmis haliyle Guney Ilcesi uygulamamiz sizlerle :)\n' \
                       'Icerikte:\n\n' \
                       '-2.El Guney ici Alim Satim\n' \
                       '-Cevrenizdeki Guneylileri gorme\n' \
                       '-Sohbet Ozelligi\n' \
                       'Ozellikleri eklenmistir. Iyı gunlerde kullanmaniz temennimle :)\n\n' \
                       'https://play.google.com/store/apps/details?id=guney.ilcesi'


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

guney = ["317257795000307", "1483642681793339", "126322934624594", "6297103294", "615241465344174", "662521437623764",
		 "denizliguneycokresmisitesi", "1www234567891", "112811418811816"]

for i in range(len(guney)):
    group_url = 'https://www.facebook.com/groups/' + guney[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
    fb.browser.save_screenshot(guney[i]+'.png')
fb.close_browser()

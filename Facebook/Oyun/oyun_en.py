import time
import re
from bs4 import BeautifulSoup
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Facebook')
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

        text_to_post_en = 'Hi all, \n\n\n' \
                       'Retro Arcade Games are now on our smart phone! :) About: \n\n' \
                       '-64 Retro Arcade Games\n' \
                       '-Game Chat Forum\n\n' \
                       'To download please click in the following link: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element_by_class_name(post_class)
            click_post.click()
            time.sleep(5)

            post_content = self.browser.find_element_by_class_name('notranslate._5rpu')
            post_content = self.browser.switch_to_active_element()
            post_content.send_keys(text_to_post_en)
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

oyun_en = ["227842967426189", "appandroiddeveloper", "2061280740824150", "3288987951179541",
           "340386762706349", "470456896341368", "509078119424610", "androidevil", "308278413765308", "ggcreators",
           "btvgamingofficialgroup", "810855769860840", "831204153907361", "511573835572177", "1023527604798068",
           "Androidiapa", "blackberry.android", "24269513", "3954131844626903", "supercarstopspeed",
           "mobileappdevelopments", "519011588455568", "mobiloids", "thegamerlife", "gamersfrpnet", "501410144060723",
           "gamdeveloper", "355723031242469", "319019998906454", "273058220704295", "streamandpagesharing", "3dswiiugamers",
           "627460971527298", "499649376898165", "185762810426343", "scottsvintagemancavestuff", "318039912719508",
           "152228903476838", "2205727453048193", "1518367058334244"]

for i in range(len(oyun_en)):
    group_url = 'https://www.facebook.com/groups/' + oyun_en[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

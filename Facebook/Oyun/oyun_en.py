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

        text_to_post_en = 'Hi all, \n\n\n' \
                       'Retro Arcade Games are now on our smart phone! :) About: \n\n' \
                       '-64 Retro Arcade Games\n' \
                       '-Game Chat Forum\n\n' \
                       'To download please click in the following link: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions = actions.send_keys(text_to_post_en)
        actions.perform()
        time.sleep(5)
        Setup.send_post(self)

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

oyun_en = ["227842967426189", "appandroiddeveloper", "2061280740824150", "3288987951179541", "1507491152850856",
           "340386762706349", "470456896341368", "509078119424610", "androidevil", "308278413765308", "ggcreators",
           "btvgamingofficialgroup", "810855769860840", "831204153907361", "511573835572177", "1518367058334244",
           "Androidiapa", "blackberry.android", "3954131844626903", "supercarstopspeed", "2205727453048193",
           "mobileappdevelopments", "519011588455568", "mobiloids", "thegamerlife", "gamersfrpnet", "501410144060723",
           "gamdeveloper", "355723031242469", "319019998906454", "273058220704295", "streamandpagesharing", "3dswiiugamers",
           "627460971527298", "499649376898165", "185762810426343", "scottsvintagemancavestuff", "318039912719508",
           "152228903476838"]

list = sample(oyun_en, len(oyun_en))

for i in range(len(oyun_en)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

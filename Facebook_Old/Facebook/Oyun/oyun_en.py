import sys
sys.path.append(r'C:\\Projects\\Facebook_Old\\Facebook')
from init import *

class FBPost:
    def setup(self):
        Setup.login(self)
        sleep(2)

    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        sleep(4)
        self.browser.get(group_url)
        sleep(2)

        text_to_post_en = 'Hi all, \n\n\n' \
                       'Retro Arcade Games are now on our smart phone! :) About: \n\n' \
                       '-64 Retro Arcade Games\n' \
                       '-Game Chat Forum\n\n' \
                       'To download please click in the following link: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        try:
            post_class = 'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element(By.CLASS_NAME, post_class)
            click_post.click()
            sleep(10)

            actions = ActionChains(self.browser)
            actions.send_keys(text_to_post).perform()
            sleep(5)

            Setup.send_post(self)
            actions.send_keys(Keys.RETURN).perform()
        except:
            print("Something went wrong, exiting script to avoid conflicts")

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

oyun_en = ["227842967426189", "appandroiddeveloper", "2061280740824150", "3288987951179541",
           "340386762706349", "470456896341368", "509078119424610", "androidevil", "308278413765308", "ggcreators",
           "btvgamingofficialgroup", "810855769860840", "831204153907361", "511573835572177",
           "Androidiapa", "blackberry.android", "3954131844626903", "supercarstopspeed", "2205727453048193",
           "519011588455568", "thegamerlife", "gamersfrpnet", "501410144060723",
           "gamdeveloper", "355723031242469", "273058220704295", "streamandpagesharing",
           "627460971527298", "499649376898165", "185762810426343", "scottsvintagemancavestuff", "318039912719508",
           ]

list = sample(oyun_en, len(oyun_en))
for i in range(len(oyun_en)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

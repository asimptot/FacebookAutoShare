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

        text_to_post = 'Dear friends,\n' \
                       'Kilkenny City app is now on our mobile phone. About:  \n\n' \
                       '-News\n' \
                       '-Sports\n' \
                       '-Job Applications\n' \
                       '-Concerts\n' \
                       '-Exhibitions\n' \
                       '-Opera\n' \
                       '-Restaurants\n' \
                       '-Weather Forecast\n' \
                       '-Activities\n' \
                       '-Hotels\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=kilkenny.city'

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

kilkenny = ["1430412867205426", "2825610674352955", "148605668543143", "350691288286807", "teqsportskilkenny",
			"kilkennybitsandshits", "1587632794804215", "140111069525242", "301199310059406", "631488383595071",
            "2140959319539978"]

list = random.choice(kilkenny)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

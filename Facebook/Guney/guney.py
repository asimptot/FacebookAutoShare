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

        text_to_post = 'Yenilenmis haliyle Guney Ilcesi uygulamamiz sizlerle :)\n' \
                       'Ilcemizde vefat edenleri artik an itibariyle ogrenebilecegiz. ' \
                       'Iyi gunlerde kullanmaniz temennimle :)\n\n' \
                       'https://play.google.com/store/apps/details?id=guney.ilcesi'

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

guney = ["317257795000307", "1483642681793339", "126322934624594", "6297103294", "615241465344174",
         "662521437623764", "denizliguneycokresmisitesi", "1www234567891", "112811418811816"]

list = random.choice(guney)
group_url = 'https://www.facebook.com/groups/' + list + '/buy_sell_discussion'
fb.post_on_facebook(group_url)
fb.close_browser()

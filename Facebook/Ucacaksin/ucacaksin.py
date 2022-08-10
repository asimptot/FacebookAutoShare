import time
import sys
sys.path.append(r'C:\\Projects\\Sosyal\\Facebook')
from init import *
from selenium.webdriver.common.action_chains import ActionChains

class FBPost:
    def setup(self):
        Setup.login(self)

    def post_on_facebook(self, group_url):
        print('Posting  on Facebook group: ', group_url)
        time.sleep(4)
        self.browser.get(group_url)
        time.sleep(2)

        text_to_post = 'Değerli abilerim, sevgili kardeşlerim. Ucacaksin uygulaması artık Play Store''da! :)\n\n' \
                       'İçerikte: \n\n' \
                       '-En Ucuz Ucak Bileti Firsatlari\n' \
                       '-Indirim Kuponlari\n' \
                       '-Sohbet Ozelligi\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=ucacaksin.ucacaksin'

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

ucacaksin = ["ucakbiletleri", "220561833134593", "webbilet", "366226913916907", "indirimlibilet.net",
             "218051502116675", "1401292690119260", "2180149602228186", "econombilet", "1407977396175349",
             "183354628665079", "1450214861885604", "319379728089143", "ucuzucakbileti", "503111189722019",
             "123117417858654", "1259712310798927", "1589449664675322", "1772796709633633", "644639619043245",
             "425123868339887", "565174700918604", "11001805838", "229674040559521", "1112588998785166",
             "1917508198519480", "379081745533897", "723790614360147", "339984579545601", "YardimDukkani",
             "723790614360147"]

for i in range(len(ucacaksin)):
    group_url = 'https://www.facebook.com/groups/' + ucacaksin[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
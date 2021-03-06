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

        text_to_post_tr = 'Merhaba arkadaşlar, \n\n\n' \
                       'Retro Arcade oyunlar artık akıllı telefonlarımızda :) İçerikte: \n\n' \
                       '-64 Adet Retro Arcade Oyun\n' \
                       '-Oyun Sohbet Forumu\n\n' \
                       'yer alacaktir. İndirmek için aşağıdaki bağlantıya tıklamanız yeterli: \n\n' \
                       'https://play.google.com/store/apps/details?id=oyunhane.abvl'

        Setup.ready_for_post(self)
        actions = ActionChains(self.browser)
        actions = actions.send_keys(text_to_post_tr)
        actions.perform()
        time.sleep(5)
        Setup.send_post(self)

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

oyun_tr = ["1249974598366070", "androidoyun", "AndroidGelistirme", "GeneralMobileAndroidOne4G", "TOG.OyunTanitim",
        "AndroidProgramGelistiricileri", "softwaredevsgroup", "320608442250298", "394535784235625", "unlostv",
        "1028228647188038", "MobilGelistiriciler", "1176041742464242", "oyuncununbilgisayari",
        "1725332541112353", "togog", "MtaServerlers", "pc.toplama", "oyungelistiriciler",
        "programlamaogreniyorum", "yazilimgelistir", "1232456353464456", "654147301273036", "1502268376707060",
        "219888054757307", "androcag", "arenaofvalornoss", "1511527392393141", "1018785974868713", "btogtoplulugu",
        "trcastleclash"]

for i in range(len(oyun_tr)):
    group_url = 'https://www.facebook.com/groups/' + oyun_tr[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()
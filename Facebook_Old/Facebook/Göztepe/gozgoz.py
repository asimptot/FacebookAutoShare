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

        text_to_post = 'Değerli abilerim, sevgili kardeşlerim. GözGöz Avrupa uygulaması artık Play Store''da! :)\n\n' \
                       'İçerikte: \n\n' \
                       '-Maç bileti devretme, paylaşım vb. işlemleri yapabileceğiniz forum özelliği\n' \
                       '-Sohbet özelliği\n' \
                       '-Göztepe ile ilgili güncel haberler\n' \
                       '-Çevrenizdeki Göztepelileri görme\n' \
                       '-Marşlar\n\n' \
                       'yer almaktadır. İyi günlerde kullanmanız temennimle ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=gozgoz.sozluk'

        try:
            post_class = 'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element(By.CLASS_NAME, post_class)
            click_post.click()
            sleep(10)

            actions = ActionChains(self.browser)
            actions.send_keys(text_to_post).perform()
            sleep(5)

            send_post = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div'))
            )
            send_post.click()
            sleep(300)
        except:
            print("Something went wrong, exiting script to avoid conflicts")

    def close_browser(self):
        self.browser.close()

fb = FBPost()
fb.setup()

goztepe = ["256830128397118", "208028558536", "goztepecom", "goztepenineskileri", "139935412764982",
            "332225360477262", "210922582375185", "575389225857771", "122154371830585", "936992506365153",
            "1194038040638929", "wwwisoookubra", "229136775939229", "259943855903893", "680538306155255",
            "416889008451550", "259820858593897", "453152851683911", "257968525316500", "1119653814739937",
            "156296471231004", "384831866221969", "202802114364116", "632261113598528", "1743504639157693",
            "278916619179669", "169197057727346"]

list = sample(goztepe, len(goztepe))
for i in range(len(goztepe)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
    if i % 5 == 0:
        print('1 saat bekletiliyor...')
        sleep(3600)
fb.close_browser()
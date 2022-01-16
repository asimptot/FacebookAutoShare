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

        text_to_post = 'Artık halı saha maçına adam eksik olmayacak! ' \
                       'Halı Saha Oyuncusu Bul Uygulaması ile Türkiye çapında binlerce halı saha oyuncusuna ulaşabileceksiniz. ' \
                       'Her geçen gün artan oyuncu sayısı ile halı saha maçınıza eksik oyuncuyu tamamlamak daha kolay hale gelecek. ' \
                       'Halı Saha Oyuncusu Bul, maça adam eksik olmasın diye!\n\n' \
                       'TOPÇULARA HIZLI ERİŞİM!\n\n' \
                       'Maçınıza davet etmek istediğiniz oyuncunun profiline girdikten sonra ister uygulama üzerinden mesaj gönderebilir, ' \
                       'isterseniz oyuncu profil bilgileri kısmından özelden yazarak maçınıza davet edebilirsiniz.\n\n' \
                       'Bunun dışında uygulama içerisinde bulunan keşfet seçeneğinden çevrenizdeki oyuncuları görüntüleyebilirsiniz.\n\n' \
                       'İçerikte:\n' \
                       '* Halı saha oyuncusu bulma forumu\n' \
                       'Oyuncularla sohbet etme\n' \
                       'Çevrenizdeki oyuncuları görüntüleme\n' \
                       'Mobil oyun uygulaması\n\n' \
                       'özellikleri yer almaktadır. Halı sahanızı keyifleştiren uygulama, sizler için tasarlandı. ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=hali.sahaoyuncusubul'

        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element_by_class_name(post_class)
            click_post.click()
            time.sleep(5)

            post_content = self.browser.find_element_by_class_name('notranslate._5rpu')
            post_content = self.browser.switch_to_active_element()
            post_content.send_keys(text_to_post)
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

halisaha = ["704021893377737", "2042127099146855", "226545028007", "1545516495775774", "232482893525378", "1526281577639275",
            "500219933389663", "serefhalisaha", "1323820704398716", "186292634788799",
            "1374235479480096", "132196480204037", "819641191404421", "227057034339953", "255780481194859", "710886928950249",
            "247446628721533", "109456339122304", "KonyaHaliSahaRakipBul", "1576233845995645", "1471701356239772",
            "220499458527354", "147355395326560", "1584165131657944", "1415907698683049"]


for i in range(len(halisaha)):
    group_url = 'https://www.facebook.com/groups/' + halisaha[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

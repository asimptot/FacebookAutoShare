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

halisaha = ["704021893377737", "2042127099146855", "226545028007", "1545516495775774", "232482893525378", "1526281577639275",
            "500219933389663", "serefhalisaha", "1323820704398716", "186292634788799",
            "1374235479480096", "132196480204037", "819641191404421", "227057034339953", "255780481194859", "710886928950249",
            "247446628721533", "109456339122304", "KonyaHaliSahaRakipBul", "1576233845995645", "1471701356239772",
            "220499458527354", "147355395326560", "1584165131657944", "1415907698683049"]

list = sample(halisaha, len(halisaha))

for i in range(len(halisaha)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

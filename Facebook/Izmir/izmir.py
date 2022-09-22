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

        text_to_post = 'Guzel Izmir''imin guzel insanlari selamlar :)\n\n' \
                       'Yeni uygulamam Izmirde Hayat Play Storeda. Icerikte neler mi var?\n\n' \
                       '-Konserler\n' \
                       '-Tiyatrolar\n' \
                       '-Opera ve Bale Etkinlikleri\n' \
                       '-Duyurular\n' \
                       '-Deprem Haberleri\n' \
                       '-Firsatlar\n' \
                       '-Izban, Metro, Eshot, Vapur saatleri ve duyurulari\n' \
                       '-Izmirim Kart Bakiye Sorgulama\n' \
                       '-Sinema Seanslari\n-Nobetci Eczaneler\n' \
                       '-Su ve Elektrik Arizalari\n\n' \
                       'Hepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\n' \
                       'https://play.google.com/store/apps/details?id=izmirde.hayat'

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

izmir = ["izmirelektronikalimsatimtakas", "izmirxizmir", "1499452027011704",
         "karsiyakabitpazari", "izmirikincielpazarim", "izmirenglishspeakers", "izmirbilgisayar", "1624712331149186",
         "629100274121495", "1221311804559488", "1549495335274303", "3391919157530736", "izmirikincielgrup",
		 "251687191870465", "izmirdecevirme", "2125911384165459", "1674448666166233", "845375905550243", "1827537364172661",
		 "1728725010490278", "5888323829", "305154173262002", "167376063347023", "125445305365", "1797464497200766",
         "601714939977538", "devlettiyatrosuizmir", "2059423444286714", "1686130384939944", "1379419095718837",
         "226585790710064", "704334799674700", "359549237574312", "251687191870465", "1397454973918631", "185587091922956",
         "huncalife35", "231718924618567", "1572859096305343", "221942534620065", "888522511347259", "700258443358488",
         "tam35sohbet", "izmirsondakika", "401921643297200", "1946103148767720", "1786050418326386", "286039838397195"]

for i in range(len(izmir)):
    group_url = 'https://www.facebook.com/groups/' + izmir[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

import time
import re
from bs4 import BeautifulSoup
import sys
sys.path.append(r'D:\\Projects\\Sosyal\\Facebook')
from init import *
from selenium.webdriver.common.action_chains import ActionChains

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

        text_to_post = 'Guzel Izmir''imin guzel insanlari selamlar :)\n\nYeni uygulamam Izmirde Hayat Play Storeda. Icerikte neler mi var?\n\n-Konserler\n-Tiyatrolar\n-Opera ve Bale Etkinlikleri\n-Duyurular\n-Deprem Haberleri\n-Firsatlar\n-Izban, Metro, Eshot, Vapur saatleri ve duyurulari\n-Izmirim Kart Bakiye Sorgulama\n-Sinema Seanslari\n-Nobetci Eczaneler\n-Su ve Elektrik Arizalari\n\nHepsi tek bir uygulamada birlesti. Gule gule kullanin ^^\n\nhttps://play.google.com/store/apps/details?id=izmirde.hayat'

        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element_by_class_name(post_class)
            click_post.click()
            time.sleep(5)

            actions = ActionChains(self.browser)
            actions = actions.send_keys(text_to_post)
            actions.perform()
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

izmir = ["izmirelektronikalimsatimtakas", "izmirxizmir", "izmirlilerburada", "1499452027011704",
         "karsiyakabitpazari", "izmirikincielpazarim", "izmirenglishspeakers", "izmirbilgisayar", "1624712331149186",
         "629100274121495", "1221311804559488", "1549495335274303", "3391919157530736", "izmirikincielgrup",
		 "251687191870465", "izmirdecevirme", "700258443358488", "izmirsosyetepazari", "1568985910018328",
		 "2125911384165459", "1674448666166233", "1873627909579276", "dedakizmir", "1723737604525836", "845375905550243",
		 "1728725010490278", "5888323829", "305154173262002", "167376063347023", "125445305365", "1797464497200766",
         "1624803364401218", "601714939977538", "devlettiyatrosuizmir", "2059423444286714", "1686130384939944",
         "226585790710064", "704334799674700", "1568985910018328", "359549237574312", "251687191870465",
         "1397454973918631", "185587091922956", "1379419095718837", "huncalife35", "231718924618567", "1572859096305343",
         "tam35sohbet", "izmirsondakika", "401921643297200", "1946103148767720", "1786050418326386", "286039838397195",
         "1827537364172661", "700258443358488", "221942534620065", "888522511347259"]

for i in range(len(izmir)):
    group_url = 'https://www.facebook.com/groups/' + izmir[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

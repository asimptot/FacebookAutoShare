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

        text_to_post = 'Dear friends,\n\n' \
                       'Netherlandspat app is now on our mobile phone! About:  \n\n' \
                       '-Concerts\n' \
                       '-Fests\n' \
                       '-Chat\n' \
                       '-Meet New People\n' \
                       '-Rent Bike/Car/House\n' \
                       '-2nd Hand Buy/Sell\n' \
                       '-Sustainability Events\n' \
                       '-Jobs\n' \
                       '-Create Your Own Event\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=netherlandspat.app'

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

netherlandspat = ["allexpatsinthenetherlands", "internationalexpatamsterdam", "1041306749227527",
            "1425158030871295", "laughingatpotatoes", "2393398401", "475997376564057",
            "889833264399671", "2513882895499019", "expatjobsinthenetherlands",
            "3391670544390704", "486835584844585", "1510096729269075",
            "791192707594625",
            "IndianExpatsInNetherlands", "8139991343", "housesinthenetherlands",
            "2406969948", "1657109771244718", "1157446251688203",
            "expatseindhoven", "375891209146726", "iloveamsterdamcity", "expatrepublic",
            "exploringnetherlands", "284141089612808", "754897328263949", "2204519835",
            "190296879768427", "1827424617527053", "1503930726289016",
            "579985732134944", "979765652054041", "2244909725745375", "770298033460235",
            "expats.eindhoven.nl", "190230194807405", "amsterdam.housing.and.roommates",
            "605664986795169", "692490407596118", "ExpatsInAmsterdam", "1580853698814943",
            "ThefunExpatGroupofTheHague", "296739250466742", "rentamsterdam", "1123182838114831",
            "295804230488520", "478599220659459", "2345051369046723",
            "expatcommunity", "amsterdamcentrumexpats", "883328028399315", "303940726659024"]

list = sample(netherlandspat, len(netherlandspat))
for i in range(len(netherlandspat)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
    if i % 5 == 0:
        print('1 saat bekletiliyor...')
        sleep(3600)
fb.close_browser()
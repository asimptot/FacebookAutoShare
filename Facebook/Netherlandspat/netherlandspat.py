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

        text_to_post = 'Dear friends,\n' \
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

netherlandspat = ["allexpatsinthenetherlands", "internationalexpatamsterdam", "1041306749227527",
                  "1425158030871295", "laughingatpotatoes", "2393398401", "475997376564057",
                  "889833264399671", "AmsterdamRental", "2513882895499019", "expatjobsinthenetherlands",
                  "Best.Jobs.Netherlands", "3391670544390704", "486835584844585", "890187398511099",
                  "utrecht.expats", "vacantes.netherlands", "UnitedExpatsoftheNetherlands",
                  "IndianExpatsInNetherlands", "8139991343", "housesinthenetherlands",
                  "expatjobsinnetherlands", "2406969948", "JobsinHolland", "1657109771244718",
                  "expatseindhoven", "375891209146726", "iloveamsterdamcity", "expatrepublic",
                  "exploringnetherlands", "284141089612808", "754897328263949", "2204519835",
                  "190296879768427", "1827424617527053", "288221731281767", "1503930726289016",
                  "579985732134944", "979765652054041", "2244909725745375", "770298033460235",
                  "expats.eindhoven.nl", "190230194807405", "amsterdam.housing.and.roommates",
                  "605664986795169", "692490407596118", "ExpatsInAmsterdam", "713518162024562",
                  "ThefunExpatGroupofTheHague", "296739250466742", "rentamsterdam", "1123182838114831",
                  "295804230488520", "478599220659459", "2345051369046723", "realexpatseindhoven",
                  "expatcommunity", "amsterdamcentrumexpats", "883328028399315", "303940726659024",
                  "1510096729269075", "1157446251688203", "791192707594625", "1580853698814943",
                  "765584943917713"]

for i in range(len(netherlandspat)):
    group_url = 'https://www.facebook.com/groups/' + netherlandspat[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
fb.close_browser()

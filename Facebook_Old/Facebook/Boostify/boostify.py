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
                       'Boostify app is now on our mobile phone. ' \
                       'Boost your account without sharing your social media account password with us. ' \
                       'Moreover, the first follower, like or subscriber we will send is free.\n\n' \
                       'Features:  \n\n' \
                       '-Get more followers\n' \
                       '-Get more likes\n' \
                       '-Get more reposts\n' \
                       '-Get more subscribers\n' \
                       '-Live support\n\n' \
                       'You will now have easy access to information about :) To download it, just click the link below: \n\n' \
                       'https://play.google.com/store/apps/details?id=boostify.app'

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

boostify = ["568620580948603", "managers.social.media", "2815428158737599", "boostsocialmedia.net",
            "talentedindividual", "socialmediamarketinghubsmmh", "233921228105287", "4071283406227548",
            "socialmediamarketinggroup", "458611971395741", "677369376241448", "343581006189180",
            "523395511877590", "593847758000515", "128473199098432", "299735715633163", "1861331500694686",
            "617438695332439", "1129941290979676", "754979742462773", "1027140062009441", "288425432664540",
            "1394184004434735", "102106509917781", "325002039040858", "1041657709867391", "1902910166626174",
            "1564518510516445", "instagramfollowersgo", "3220778951364530", "OpenGroupFree", "5586200261456329",
            "103096463458577", "openaicontent", "1413062589012533", "515574005256991", "264691513711120",
            "498094584732613", "347316160599691", "2844512592450510", "557003561120252", "897525264308501",
            "youtubesubscribersfan", "177620938358820", "280724023017288", "177994190590941", "305244213921743"]

list = sample(boostify, len(boostify))
for i in range(len(boostify)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
    if i % 5 == 0:
        print('1 saat bekletiliyor...')
        sleep(3600)
fb.close_browser()
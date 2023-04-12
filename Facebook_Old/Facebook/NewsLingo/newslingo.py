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

        text_to_post = 'Dear friends,\n' \
                       'NewsLingo app is now on our mobile phone.\n\n' \
                       'Are you looking for a fun and easy way to improve your English skills? ' \
                       'Look no further than our new Android app! ' \
                       'Our app lets you read English news articles at your own level, ' \
                       'and even includes a chat feature to practice your conversation skills. ' \
                       'Whether you are a beginner or an advanced learner, our app has something for everyone. ' \
                       'Download it today and start learning English like never before!\n\n' \
                       'https://play.google.com/store/apps/details?id=neuslingo.aplihde'

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

newslingo = ["481561710258425", "learnenglish.improveyourenglishskills", "565542144351439", "329454095956360",
            "InnovativeToE", "englishspeakingpracticeesp", "239423810601657", "504633371543410",
            "358674591314394", "resimlerleingilizcekelimeler", "translationplatform", "125572928772269",
            "ingilizceplatform", "ydspublishing", "804277272929620", "514863742009381", "englishspeaking24",
            "329454095956360"]

list = sample(newslingo, len(newslingo))
for i in range(len(newslingo)):
    group_url = 'https://www.facebook.com/groups/' + list[i] + '/buy_sell_discussion'
    fb.post_on_facebook(group_url)
    if i % 5 == 0:
        print('1 saat bekletiliyor...')
        sleep(3600)
fb.close_browser()

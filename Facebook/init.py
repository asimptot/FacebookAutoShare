from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

class Setup:
    def login(self):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )
        self.browser.get('https://www.facebook.com/')

        time.sleep(5)

        N = 26  # number of times you want to press TAB

        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()

        time.sleep(2)
        actions1 = ActionChains(self.browser)
        actions1.send_keys(Keys.RETURN)
        actions1.perform()

        time.sleep(2)
        email = self.browser.find_element('id', 'email')
        email.send_keys("nagavaga")

        time.sleep(2)
        password = self.browser.find_element('id', 'pass')
        password.send_keys("haschmeth250*7")
        time.sleep(2)
        submit_button = self.browser.find_element('name', 'login')
        submit_button.click()
        time.sleep(2)
        self.browser.get('https://www.facebook.com/')

    def ready_for_post(self):
        try:
            post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element(By.CLASS_NAME, post_class)
            click_post.click()
            time.sleep(5)
        except:
            print("Something went wrong, exiting script to avoid conflicts")

    def send_post(self):
        try:
            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
            id_ = str(all_pc[0].get('id'))
            xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div'
            post = self.browser.find_element('xpath', xpath)
            post.click()
            time.sleep(5)

        except:
            print("Something went wrong, exiting script to avoid conflicts")

    def close_browser(self):
        self.browser.close()
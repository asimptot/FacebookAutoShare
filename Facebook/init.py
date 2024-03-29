from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumbase import Driver

class Setup:
    def login(self):
        self.browser = Driver(headless=False)

        self.browser.get('https://www.facebook.com/')
        sleep(5)

        N = 25  # number of times you want to press TAB

        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()

        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(2)
        email = self.browser.find_element('id', 'email')
        email.send_keys("100094451243160")

        sleep(2)
        password = self.browser.find_element('id', 'pass')
        password.send_keys("123abc123ABC*")
        sleep(2)
        submit_button = self.browser.find_element('name', 'login')
        submit_button.click()
        sleep(5)
        self.browser.get('https://www.facebook.com/')

    def ready_for_post(self):
        try:
            post_class = 'x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element(By.CLASS_NAME, post_class)
            click_post.click()
            sleep(10)
        except:
            print("Something went wrong, exiting script to avoid conflicts\n")

    def send_post(self):
        try:
            send_post = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div'))
            )
            send_post.click()
            '''
            N = 11  # number of times you want to press TAB
            actions = ActionChains(self.browser)
            for _ in range(N):
                actions = actions.send_keys(Keys.TAB)
            actions.perform()

            sleep(2)
            actions.send_keys(Keys.RETURN).perform()
            '''
            delay = randint(3600, 7200)
            sleep(delay)

        except:
            print("")

    def close_browser(self):
        self.browser.close()

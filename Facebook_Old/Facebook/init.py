from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, warnings
from random import randint, sample

class Setup:
    def login(self):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )
        self.browser.get('https://www.facebook.com/')
        sleep(5)

        N = 26  # number of times you want to press TAB

        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()

        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(2)
        email = self.browser.find_element('id', 'email')
        email.send_keys("YOUR FACEBOOK USERNAME")

        sleep(2)
        password = self.browser.find_element('id', 'pass')
        password.send_keys("YOUR FACEBOOK PASSWORD")
        sleep(2)
        submit_button = self.browser.find_element('name', 'login')
        submit_button.click()
        sleep(2)
        self.browser.get('https://www.facebook.com/')

    def ready_for_post(self):
        try:
            post_class = 'rtxb060y hpj0pwwo lc19xlkw l4uc2m3f mfclru0v t7p7dqev'
            post_class = post_class.replace(' ', '.')
            click_post = self.browser.find_element(By.CLASS_NAME, post_class)
            click_post.click()
            sleep(5)
        except:
            print("Something went wrong, exiting script to avoid conflicts")

    def send_post(self):
        try:
            send_post = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div'))
            )
            send_post.click()

            delay = randint(300, 600)
            sleep(delay)

        except:
            print("")

    def close_browser(self):
        self.browser.close()

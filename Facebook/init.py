from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import warnings
from bs4 import BeautifulSoup
import sys

class Login:
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

        time.sleep(2)
        email = self.browser.find_element_by_id('email')
        email.send_keys("joyosis972@whecode.com") #+44 7457 400328

        time.sleep(2)
        password = self.browser.find_element_by_id('pass')
        password.send_keys("10061144")
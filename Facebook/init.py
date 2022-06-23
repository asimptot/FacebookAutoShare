from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Login:
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
        email = self.browser.find_element_by_id('email')
        email.send_keys("nagavaga")

        time.sleep(2)
        password = self.browser.find_element_by_id('pass')
        password.send_keys("haschmeth250*7")

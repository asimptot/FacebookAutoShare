from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import warnings, os
from g4f.client import Client
import g4f.models
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
warnings.filterwarnings("ignore")
client = Client()
messages = []

class Setup:
    def login(self):
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-position=-2400,-2400")
        my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        options.add_argument(f"--user-agent={my_user_agent}")
        options.add_argument("--disable-gpu")
        options.add_argument("--force-device-scale-factor=0.75")

        self.browser = uc.Chrome(options=options, version_main=135)
        self.actions = ActionChains(self.browser)
        self.browser.maximize_window()
        self.browser.get('https://www.facebook.com/')
        sleep(5)

        cookies = 'x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w xeuugli x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4 xdl72j9'
        cookies = cookies.replace(' ', '.')
        cookies_post = self.browser.find_element(By.CLASS_NAME, cookies)
        cookies_post.click()
        sleep(4)

        email = self.browser.find_element('id', 'email')
        email.send_keys("YOUR FACEBOOK USERNAME")

        sleep(2)
        password = self.browser.find_element('id', 'pass')
        password.send_keys("YOUR FACEBOOK PASSWORD")
        sleep(2)
        submit_button = self.browser.find_element('name', 'login')
        submit_button.click()
        sleep(5)
        self.browser.get('https://www.facebook.com/')
        sleep(4)

    def ready_for_post(self, image_filename, item_description):
        try:
            self.browser.find_element(By.XPATH, "//*[contains(text(), 'Kapat')]").click()
        except:
            sleep(1)
        sleep(2)
        post_class = 'x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou'
        post_class = post_class.replace(' ', '.')
        click_post = self.browser.find_element(By.CLASS_NAME, post_class)
        click_post.click()

        dynamic_element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[starts-with(@id, 'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div[1]"))
        )
        dynamic_element.click()
        sleep(2)

        file_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//form[contains(@method, "POST")]//input[contains(@accept, "image/*")]'))
        )
        image_path = os.path.abspath(image_filename)

        self.browser.execute_script("arguments[0].style.display = 'block';", file_input)
        file_input.send_keys(image_path)
        sleep(10)

        prompt = f"Maak een unieke en boeiende post voor een tweedehands artikel. Beschrijving: {item_description}. "
        response = client.chat.completions.create(
            model=g4f.models.blackboxai,
            messages=[{"role": "user", "content": prompt}],
        )

        generated_text = response.choices[0].message.content

        dynamic_element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[starts-with(@id, 'mount_0_0_')]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]"))
        )
        dynamic_element.click()

        actions = ActionChains(self.browser)
        actions.send_keys(generated_text).perform()


    def send_post(self):
        send_post = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div/div[3]/div[3]'))
        )
        send_post.click()
        sleep(10)

        delay = randint(60, 120)
        sleep(delay)

    def close_browser(self):
        self.browser.close()

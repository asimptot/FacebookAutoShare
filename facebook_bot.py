# Facebook Bot Module
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import os
from random import randint
import pyautogui
import pyperclip

# Disable PyAutoGUI fail-safe (prevents mouse corner trigger)
pyautogui.FAILSAFE = False

from credentials import FACEBOOK_EMAIL, FACEBOOK_PASSWORD
from config import BROWSER_OPTIONS, WAIT_TIMES, FB_ELEMENTS
from ai_generator import AITextGenerator


class FacebookBot:
    """Bot class for Facebook group automation"""
    
    def __init__(self):
        self.browser = None
        self.actions = None
        self.ai_generator = AITextGenerator()
    
    def start_browser(self):
        """Start browser"""
        print("🌐 Starting browser...")
        
        try:
            print("🔧 Initializing Chrome with minimal settings...")
            # Use minimal settings
            options = uc.ChromeOptions()
            
            # Essential arguments for stability
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-features=IsolateOrigins,site-per-process")
            options.add_argument("--allow-running-insecure-content")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            
            # User agent
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36")
            
            if BROWSER_OPTIONS['headless']:
                options.add_argument('--headless=new')
            
            # Force Chrome version 145 driver (matches current Chrome version)
            print("📦 Downloading Chrome 145 compatible driver...")
            self.browser = uc.Chrome(options=options, version_main=145)
            self.actions = ActionChains(self.browser)
            
            # Wait a bit for browser to stabilize
            sleep(2)
            
            if not BROWSER_OPTIONS['headless']:
                self.browser.maximize_window()
            
            print("✅ Browser ready")
        except Exception as e:
            print(f"❌ Browser start failed: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def login(self):
        """Login to Facebook"""
        print("🔐 Logging in to Facebook...")
        try:
            self.browser.get('https://www.facebook.com/')
            print("✅ Page loaded")
            sleep(WAIT_TIMES['page_load'])
        except Exception as e:
            print(f"❌ Failed to load Facebook: {e}")
            raise
        
        # Handle cookie consent with Tab key
        try:
            from selenium.webdriver.common.keys import Keys
            # Wait a bit for cookie popup to appear
            sleep(2)
            # Press Tab 17 times to navigate and Enter to accept
            actions = ActionChains(self.browser)
            for _ in range(17):  # Tab 17 times to reach accept button
                actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.ENTER)  # Press Enter to accept
            actions.perform()
            print("✅ Cookie consent handled with Tab")
            sleep(WAIT_TIMES['after_click'])
        except Exception as e:
            print(f"⚠️ Cookie handling with Tab failed: {e}")
        
        # Wait for email input to be present
        try:
            # Try multiple methods to find email input
            email_input = None
            try:
                # First try by name attribute
                email_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.NAME, 'email'))
                )
            except:
                # Try by autocomplete attribute
                email_input = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username webauthn"]'))
                )
            
            email_input.clear()
            email_input.send_keys(FACEBOOK_EMAIL)
            print("✅ Email entered")
            sleep(WAIT_TIMES['after_click'])
        except Exception as e:
            print(f"❌ Could not find email input: {e}")
            print("Current URL:", self.browser.current_url)
            raise
        
        # Password input
        try:
            # Try multiple methods to find password input
            password_input = None
            try:
                # First try by name attribute
                password_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.NAME, 'pass'))
                )
            except:
                # Try by type=password
                password_input = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
                )
            
            password_input.clear()
            password_input.send_keys(FACEBOOK_PASSWORD)
            print("✅ Password entered")
            sleep(WAIT_TIMES['after_click'])
        except Exception as e:
            print(f"❌ Could not find password input: {e}")
            raise
        
        # Login button
        try:
            # Try multiple methods to find login button
            login_button = None
            try:
                # Try the specific xpath you provided
                login_button = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div'))
                )
            except:
                try:
                    # Try by name attribute
                    login_button = WebDriverWait(self.browser, 5).until(
                        EC.presence_of_element_located((By.NAME, 'login'))
                    )
                except:
                    try:
                        # Try by text "Giriş Yap" or "Log in"
                        login_button = WebDriverWait(self.browser, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Giriş Yap") or contains(text(), "Log in")]'))
                        )
                    except:
                        # Try any submit button in login form
                        login_button = WebDriverWait(self.browser, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="login_form"]//button[@type="submit"]'))
                        )
            
            # Use JavaScript click to avoid overlay issues
            self.browser.execute_script("arguments[0].click();", login_button)
            print("✅ Login button clicked")
            sleep(5)
            
            # Wait for potential Meta bot verification
            print("⏳ Waiting 30 seconds for Meta verification (solve manually if needed)...")
            sleep(30)
            print("✅ Proceeding...")
                
        except Exception as e:
            print(f"❌ Could not find login button: {e}")
            raise
        
        # Go to homepage
        try:
            self.browser.get('https://www.facebook.com/')
            sleep(WAIT_TIMES['after_click'])
            print("✅ Login successful")
        except Exception as e:
            print(f"❌ Could not navigate to homepage: {e}")
            raise
    
    def navigate_to_group(self, group_id):
        """Navigate to specified group"""
        group_url = f'https://www.facebook.com/groups/{group_id}/buy_sell_discussion'
        self.browser.get(group_url)
        sleep(WAIT_TIMES['after_click'])
    
    def create_post(self, images, post_text):
        """
        Create post in group
        
        Args:
            images (list or str): Path(s) to image(s) to upload (can be single string or list)
            post_text (str): Pre-generated text to post (already processed by AI or description)
        """
        # Convert single image to list for consistent handling
        if isinstance(images, str):
            images = [images]
        
        print(f"📸 Images to upload: {len(images)}")
        
        # Close any popups (if exists)
        try:
            close_buttons = self.browser.find_elements(By.XPATH, "//*[contains(text(), 'Kapat') or contains(text(), 'Close')]")
            for btn in close_buttons:
                try:
                    btn.click()
                    sleep(1)
                except:
                    pass
        except:
            pass
        
        sleep(WAIT_TIMES['after_click'])
        
        # Click "Write something..." / "Bir şeyler yaz..." box
        try:
            print("🖱️ Opening post dialog...")
            write_box = None
            
            # Try multiple methods to find the write box
            try:
                write_box = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, 
                        '//span[contains(@class, "x1lliihq") and contains(@class, "x6ikm8r") and contains(text(), "Bir şeyler yaz")]'))
                )
            except:
                try:
                    write_box = WebDriverWait(self.browser, 5).until(
                        EC.element_to_be_clickable((By.XPATH, 
                            '//span[contains(text(), "Bir şeyler yaz") or contains(text(), "Write something") or contains(text(), "What")]'))
                    )
                except:
                    try:
                        write_box = WebDriverWait(self.browser, 5).until(
                            EC.element_to_be_clickable((By.XPATH, 
                                '//*[@id="mount_0_0_wM"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span'))
                        )
                    except:
                        write_box = WebDriverWait(self.browser, 5).until(
                            EC.element_to_be_clickable((By.XPATH, 
                                '//div[@role="button" and contains(@aria-label, "Create")]'))
                        )
            
            # Click using JavaScript to avoid overlay issues
            self.browser.execute_script("arguments[0].click();", write_box)
            print("✅ Post dialog opened")
            sleep(5)
            
        except Exception as e:
            print(f"❌ Could not open post dialog: {e}")
            raise
        
        # Upload all images
        print(f"📤 Uploading {len(images)} image(s)...")
        for img_index, image_path in enumerate(images, 1):
            self._upload_single_image(image_path, img_index)
            if img_index < len(images):
                sleep(2)
        
        print(f"✅ All images uploaded!")
        sleep(WAIT_TIMES['image_upload'])
        
        # Now paste the text
        self._paste_text(post_text, len(images))
    
    def _upload_single_image(self, image_path, image_index):
        """Upload a single image to the post"""
        absolute_path = os.path.abspath(image_path)
        
        # Verify file exists
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"Image file not found: {absolute_path}")
        
        print(f"   📂 {os.path.basename(absolute_path)} (Foto #{image_index})")
        
        # Navigate to photo button with different Tab counts per image
        sleep(1)
        
        if image_index == 1:
            # First image: 4 Tabs
            for i in range(4):
                pyautogui.press('tab')
                sleep(0.2)
        elif image_index == 2:
            # Second image: 5 Tabs
            for i in range(5):
                pyautogui.press('tab')
                sleep(0.2)
        # Third and fourth images: No tabs, direct Enter
        
        # Open file dialog
        pyautogui.press('enter')
        sleep(3)
        
        # Type file path and submit
        pyautogui.write(absolute_path, interval=0.05)
        sleep(0.5)
        
        # Submit with 2 Tabs + Enter
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.press('enter')
        
        # Wait for upload
        sleep(5)
    
    def _paste_text(self, post_text, image_count):
        """Paste text into the post"""
        print(f"📝 Pasting text ({len(post_text)} chars)...")
        
        try:
            # Wait for form to be ready
            sleep(1)
            
            # Navigate to textbox based on image count
            # 1 foto: No tabs (cursor already in textbox)
            # 2+ foto: 10 Tabs to textbox
            if image_count == 1:
                print("   ⌨️ Cursor already in textbox (1 image)")
            else:
                print(f"   ⌨️ Navigating to textbox (10 Tabs for {image_count} images)...")
                for i in range(10):
                    pyautogui.press('tab')
                    sleep(0.2)
            
            print("   ✅ Reached textbox")
            sleep(0.5)
            
            # Copy text to clipboard
            pyperclip.copy(post_text)
            
            # Verify clipboard
            if pyperclip.paste() == post_text:
                print(f"   ✅ Clipboard ready")
            else:
                print(f"   ⚠️ Clipboard mismatch")
            
            sleep(0.3)
            
            # Paste with Ctrl+V
            pyautogui.hotkey('ctrl', 'v')
            sleep(2)
            
            print("✅ Text pasted!")
            
        except Exception as e:
            print(f"❌ Text pasting failed: {e}")
            raise
    
    def publish_post(self):
        """Publish the created post using keyboard navigation"""
        print("📤 Publishing post...")
        
        # Wait for content to be processed
        sleep(2)
        
        # Navigate to publish button with 10 Tabs, then Enter
        for i in range(10):
            pyautogui.press('tab')
            sleep(0.2)
        
        sleep(0.5)
        
        # Press Enter to publish
        pyautogui.press('enter')
        print("✅ Post published!")
        
        sleep(WAIT_TIMES['after_post'])
        
        # Random wait between groups
        wait_min, wait_max = WAIT_TIMES['between_groups']
        delay = randint(wait_min, wait_max)
        print(f"⏳ Waiting {delay} seconds...\n")
        sleep(delay)
    
    def close(self):
        """Close browser"""
        if self.browser:
            self.browser.quit()
            print("👋 Browser closed")

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
    
    def create_post(self, images, post_text, product_name=None, original_description=None):
        """
        Create marketplace listing in group
        
        Args:
            images (list or str): Path(s) to image(s) to upload (can be single string or list)
            post_text (str): AI-generated post text for description field
            product_name (str): Product title/name for marketplace listing
            original_description (str): Original product description (for price extraction)
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
        
        # Step 1: Click "Alım Satım" tab
        try:
            print("🖱️ Clicking 'Alım Satım' tab...")
            posts_tab = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.ID, "posts"))
            )
            self.browser.execute_script("arguments[0].click();", posts_tab)
            print("✅ 'Alım Satım' tab clicked")
            sleep(3)
        except Exception as e:
            print(f"❌ Could not click 'Alım Satım' tab: {e}")
            raise
        
        # Step 2: Click "Bir Şey Sat" button
        try:
            print("🖱️ Clicking 'Bir Şey Sat' button...")
            sell_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
                    '//div[@aria-label="Bir Şey Sat" or @aria-label="Sell Something"]'))
            )
            self.browser.execute_script("arguments[0].click();", sell_button)
            print("✅ 'Bir Şey Sat' button clicked")
            sleep(3)
        except Exception as e:
            print(f"❌ Could not click 'Bir Şey Sat' button: {e}")
            raise
        
        # Step 3: Click "Satılık ürün" option
        try:
            print("🖱️ Clicking 'Satılık ürün' option...")
            product_option = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
                    '//span[contains(text(), "Satılık ürün") or contains(text(), "Item for sale")]/ancestor::div[@role="button"]'))
            )
            self.browser.execute_script("arguments[0].click();", product_option)
            print("✅ 'Satılık ürün' option clicked")
            sleep(3)
        except Exception as e:
            print(f"❌ Could not click 'Satılık ürün' option: {e}")
            raise
        
        # Step 4: Find file input element and upload all photos at once
        try:
            print("🖱️ Finding file input element...")
            
            # First, try to find the input element directly
            file_input = None
            try:
                file_input = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, 
                        '//input[@type="file" and @accept and @multiple]'))
                )
                print("✅ File input found via generic selector")
            except:
                try:
                    # Try the specific XPath
                    file_input = WebDriverWait(self.browser, 5).until(
                        EC.presence_of_element_located((By.XPATH, 
                            '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/label[1]/input'))
                    )
                    print("✅ File input found via specific XPath")
                except:
                    # If not found, click the upload area first
                    print("   ⚠️ File input not visible, clicking upload area first...")
                    photo_upload_area = WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, 
                            '//span[contains(text(), "Fotoğraflar ekle") or contains(text(), "Add photos")]/ancestor::div[@role="button"]'))
                    )
                    self.browser.execute_script("arguments[0].click();", photo_upload_area)
                    sleep(2)
                    
                    # Try again to find input
                    file_input = WebDriverWait(self.browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, 
                            '//input[@type="file" and @accept and @multiple]'))
                    )
                    print("✅ File input found after clicking upload area")
            
            # Prepare absolute paths for all images
            absolute_paths = []
            for image_path in images:
                absolute_path = os.path.abspath(image_path)
                if not os.path.exists(absolute_path):
                    raise FileNotFoundError(f"Image file not found: {absolute_path}")
                absolute_paths.append(absolute_path)
                print(f"   📂 {os.path.basename(absolute_path)}")
            
            # Upload all images at once (multiple file upload)
            print(f"📤 Uploading {len(images)} image(s) via file input...")
            # Join paths with newline for multiple file upload
            all_paths = '\n'.join(absolute_paths)
            file_input.send_keys(all_paths)
            
            print(f"✅ All images uploaded!")
            sleep(WAIT_TIMES['image_upload'])
            
        except Exception as e:
            print(f"❌ Could not upload photos via file input: {e}")
            print(f"⚠️ Falling back to PyAutoGUI method...")
            
            # Fallback: Use PyAutoGUI method
            try:
                # Click photo upload area
                photo_upload_area = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, 
                        '//span[contains(text(), "Fotoğraflar ekle") or contains(text(), "Add photos")]/ancestor::div[@role="button"]'))
                )
                self.browser.execute_script("arguments[0].click();", photo_upload_area)
                print("✅ Photo upload area clicked")
                sleep(3)
                
                # Upload images one by one with PyAutoGUI
                print(f"📤 Uploading {len(images)} image(s) with PyAutoGUI...")
                for img_index, image_path in enumerate(images, 1):
                    self._upload_single_image_marketplace(image_path, img_index)
                    if img_index < len(images):
                        sleep(2)
                
                print(f"✅ All images uploaded!")
                sleep(WAIT_TIMES['image_upload'])
            except Exception as fallback_error:
                print(f"❌ PyAutoGUI fallback also failed: {fallback_error}")
                raise
        
        # Fill marketplace form fields (post_text = AI generated content)
        self._fill_marketplace_form(product_name, original_description, post_text)
    
    def _fill_marketplace_form(self, product_name, original_description, ai_description):
        """Fill marketplace listing form fields
        
        Args:
            product_name (str): Product title
            original_description (str): Original description from products.py (for price extraction)
            ai_description (str): AI-generated description text to use in form
        """
        print("📝 Filling marketplace form...")
        
        # Extract numeric price from original description
        price_number = None
        if original_description:
            import re
            # Extract number from string like "€120" or "Prijs: €120"
            match = re.search(r'€\s*(\d+)', original_description)
            if match:
                price_number = match.group(1)
                print(f"   💰 Extracted price: €{price_number}")
        
        # Step 1: Fill Title
        try:
            print("   ✏️ Filling title...")
            title_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, 
                    '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/div/label/div/input'))
            )
            title_input.clear()
            if product_name:
                title_input.send_keys(product_name)
                print(f"   ✅ Title: {product_name}")
            else:
                print("   ⚠️ No product name provided")
        except Exception as e:
            print(f"   ⚠️ Could not fill title: {e}")
        
        # Step 2: Fill Price
        try:
            print("   💰 Filling price...")
            price_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, 
                    '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[4]/div[1]/div/div/label/div/input'))
            )
            price_input.clear()
            if price_number:
                price_input.send_keys(price_number)
                print(f"   ✅ Price: €{price_number}")
            else:
                print("   ⚠️ No price found")
        except Exception as e:
            print(f"   ⚠️ Could not fill price: {e}")
        
        # Step 3: Select Condition (KULLANILMIŞ YENİ GİBİ) using keyboard
        try:
            print("   📦 Selecting condition with keyboard...")
            from selenium.webdriver.common.keys import Keys
            
            # Tab to condition field
            pyautogui.press('tab')
            sleep(1)
            print("   ⌨️ Tabbed to condition field")
            
            # Press Down arrow 2 times to reach "Kullanılmış - Yeni Gibi"
            pyautogui.press('down')
            sleep(1)
            print("   ⬇️ Down 1")
            
            pyautogui.press('down')
            sleep(1)
            print("   ⬇️ Down 2")
            
            # Press Enter to select
            pyautogui.press('enter')
            sleep(1)
            print("   ✅ Condition: KULLANILMIŞ - YENİ GİBİ selected")
            
        except Exception as e:
            print(f"   ⚠️ Could not select condition: {e}")
        
        # Step 4: Expand "Diğer detaylar" (Other details) section
        try:
            print("   📂 Expanding 'Diğer detaylar' section...")
            
            # Try multiple methods to find the button
            other_details_button = None
            try:
                # Method 1: Find by text content
                other_details_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, 
                        '//span[contains(text(), "Diğer detaylar") or contains(text(), "Other details")]/ancestor::div[@role="button"]'))
                )
                print("   ✅ Found 'Diğer detaylar' button via text")
            except:
                try:
                    # Method 2: Find by aria-expanded attribute
                    other_details_button = WebDriverWait(self.browser, 5).until(
                        EC.element_to_be_clickable((By.XPATH, 
                            '//div[@role="button" and @aria-expanded="false" and .//span[contains(text(), "Diğer detaylar")]]'))
                    )
                    print("   ✅ Found 'Diğer detaylar' button via aria-expanded")
                except:
                    # Method 3: Use specific XPath as last resort
                    other_details_button = WebDriverWait(self.browser, 5).until(
                        EC.element_to_be_clickable((By.XPATH, 
                            '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[6]'))
                    )
                    print("   ✅ Found 'Diğer detaylar' button via specific XPath")
            
            # Click the button
            self.browser.execute_script("arguments[0].click();", other_details_button)
            print("   ✅ 'Diğer detaylar' section expanded")
            sleep(2)
        except Exception as e:
            print(f"   ⚠️ Could not expand 'Diğer detaylar': {e}")
        
        # Step 5: Fill Description (with AI-generated content using clipboard)
        try:
            print("   📄 Filling description with AI content...")
            
            # Wait a bit more for textarea to become visible after expanding
            sleep(1)
            
            # Try multiple methods to find textarea
            description_textarea = None
            try:
                # Method 1: Find by tag name
                description_textarea = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, 
                        '//textarea[@dir="ltr"]'))
                )
                print("   ✅ Found description textarea via tag")
            except:
                # Method 2: Use specific XPath
                description_textarea = WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.XPATH, 
                        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[6]/div/div/div[2]/div/div/div/div/label/div/div/textarea'))
                )
                print("   ✅ Found description textarea via specific XPath")
            
            if ai_description:
                # Click textarea to focus
                description_textarea.click()
                sleep(0.5)
                
                # Clear existing content with Ctrl+A and Delete
                pyautogui.hotkey('ctrl', 'a')
                sleep(0.3)
                pyautogui.press('delete')
                sleep(0.3)
                
                # Copy AI description to clipboard
                pyperclip.copy(ai_description)
                
                # Verify clipboard
                if pyperclip.paste() == ai_description:
                    print(f"   ✅ Clipboard ready with AI content ({len(ai_description)} chars)")
                else:
                    print(f"   ⚠️ Clipboard mismatch")
                
                sleep(0.3)
                
                # Paste with Ctrl+V
                pyautogui.hotkey('ctrl', 'v')
                sleep(2)
                
                print(f"   ✅ AI description pasted: {len(ai_description)} chars")
            else:
                print("   ⚠️ No AI description provided")
            sleep(1)
        except Exception as e:
            print(f"   ⚠️ Could not fill description: {e}")
        
        # Step 6: Click checkbox at the bottom
        try:
            print("   ☑️ Clicking checkbox...")
            checkbox = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
                    '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]/div[6]/div/div/div[5]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[3]'))
            )
            self.browser.execute_script("arguments[0].click();", checkbox)
            print("   ✅ Checkbox clicked")
            sleep(1)
        except Exception as e:
            print(f"   ⚠️ Could not click checkbox: {e}")
        
        print("✅ Marketplace form filled!")
        sleep(2)
    
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
    
    def _upload_single_image_marketplace(self, image_path, image_index):
        """Upload a single image to marketplace listing"""
        absolute_path = os.path.abspath(image_path)
        
        # Verify file exists
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"Image file not found: {absolute_path}")
        
        print(f"   📂 {os.path.basename(absolute_path)} (Foto #{image_index})")
        
        # For first photo, file dialog is already open from clicking photo upload area
        # For subsequent photos, need to click "Fotoğraf Ekle" button
        if image_index > 1:
            try:
                print(f"   🖱️ Clicking 'Fotoğraf Ekle' for photo #{image_index}...")
                add_photo_button = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, 
                        '//div[@aria-label="Fotoğraf Ekle" or @aria-label="Add Photo"]'))
                )
                self.browser.execute_script("arguments[0].click();", add_photo_button)
                sleep(2)
                print(f"   ✅ 'Fotoğraf Ekle' clicked")
            except Exception as e:
                print(f"   ⚠️ Could not find 'Fotoğraf Ekle' button, trying alternative method: {e}")
                # Alternative: Use keyboard Tab navigation
                pyautogui.press('tab')
                sleep(0.2)
                pyautogui.press('enter')
                sleep(2)
        
        sleep(1)
        
        # Type file path in the open file dialog
        print(f"   ⌨️ Typing file path...")
        pyautogui.write(absolute_path, interval=0.05)
        sleep(0.5)
        
        # Submit with 2 Tabs + Enter (standard Windows file dialog)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.press('tab')
        sleep(0.2)
        pyautogui.press('enter')
        
        print(f"   ✅ Photo #{image_index} uploaded")
        
        # Wait for upload to process
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
        
        # Step 1: Navigate with 10 Tabs, then Enter
        print("   ⌨️ Step 1: 10 Tab + Enter...")
        for i in range(10):
            pyautogui.press('tab')
            sleep(0.2)
        
        sleep(0.5)
        pyautogui.press('enter')
        sleep(2)
        
        # Step 2: Navigate with 4 Tabs, then Enter to confirm publish
        print("   ⌨️ Step 2: 4 Tab + Enter (confirm publish)...")
        for i in range(4):
            pyautogui.press('tab')
            sleep(0.2)
        
        sleep(0.5)
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

import re
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ZiapngAutoV2_Workflow:

#---------- Locators ------------------------------

    Allow_button_ID =  (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    Hamburger_button_AU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    Login_option_AU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
    Email_filed_XPATH = (AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")
    Password_filed_XPATH = (AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")
    RememberMe_Radio_AU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)')
    Login_button_AU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)')

    Pre_bid_XPATH = (AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'Set Pre-Bid')]")
    Amount_XPATH = (AppiumBy.XPATH, "//android.widget.EditText[@text='Per Ct']")
    Save_button_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Save']")
    Confirm_Prebid_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Confirm Pre-Bid')]")
    Starting_price_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Starting Price')]")
    Yes_button_XPATH =(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Yes']")

    Cancel_Pre_bid_XPATH = (AppiumBy.XPATH,"//android.widget.TextView[@text='Cancel Pre-Bid']")
    Confirm_Pre_bid_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Confirm']")
    Okay_pre_bid_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Okay']")

# ------------- Constructor -------------------------

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

# -------------- Login ----------------------------

    def allow_Permission(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.Allow_button_ID)).click()
            print("\n Allow button is tapped")
        except:
            print("Allow button is not visible")

    def Open_LoginPage(self):
        Hamburger = self.wait.until(EC.element_to_be_clickable(self.Hamburger_button_AU))
        Hamburger.click()
        print("Hamburger is tapped")

        Login_option = self.wait.until(EC.element_to_be_clickable(self.Login_option_AU))
        Login_option.click()
        print("Login option is tapped")

    def Login(self,email,password):
        try:
            Email = self.wait.until(EC.presence_of_element_located(self.Email_filed_XPATH))
            Email.send_keys(email)
            print(f"Email is entered {email}")

            Password = self.wait.until(EC.presence_of_element_located(self.Password_filed_XPATH))
            Password.send_keys(password)
            print(f"Password is entered {password}")

            Readme = self.wait.until(EC.element_to_be_clickable(self.RememberMe_Radio_AU))
            Readme.click()
            print("Readme is tapped")

            Login_button = self.wait.until(EC.element_to_be_clickable(self.Login_button_AU))
            Login_button.click()
            print("Logged in successfully")
        except:
            print("Login button is not visible")
            assert False

# --------------- PRE-BID -------------------------
    def pre_bid(self, amount):
        print("Trying to locate Pre-bid...")

        self.wait.until(EC.presence_of_element_located(self.Pre_bid_XPATH))
        print("Pre-bid found")

        self.wait.until(EC.element_to_be_clickable(self.Pre_bid_XPATH)).click()
        print("Pre-bid clicked")

        self.wait.until(EC.presence_of_element_located(self.Amount_XPATH)).send_keys(amount)
        print("Amount entered")

        self.wait.until(EC.element_to_be_clickable(self.Save_button_XPATH)).click()
        print("Save clicked")

# --------------- ASSERTION -------------------------
    time.sleep(2)
    def Assertion_pre_bid(self,Certificate,exchange_rate):

        self.wait.until(EC.element_to_be_clickable(self.Confirm_Prebid_XPATH)).click()
        print("Waiting for confirmation popup")

        carat_text = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH,
             f"//android.widget.TextView[contains(@text,'1- 2467124122') or contains(@text,'{Certificate}')]")
        )).text

        carat_match = re.search(r'(\d+\.?\d*)\s*[cC][tT]', carat_text)

        if carat_match:
            carat_value = float(carat_match.group(1))
            print("Carat:", carat_value)

        price_text = self.wait.until(EC.presence_of_element_located(self.Starting_price_XPATH)).text

        price_match = re.search(r'\$([\d,]+)', price_text)

        if price_match:
            price_value = int(price_match.group(1).replace(",", ""))
            print("Starting Price:", price_value)

            exchange_rate = float(exchange_rate)

            Starting_price = self.driver.find_element(*self.Starting_price_XPATH)
            print(Starting_price.text)

            formatted_usd = f"{price_value:,}"
            formatted_yen = f"{int(price_value * exchange_rate):,}"

            Validate_Starting_price = f"Starting Price (PCt). - ${formatted_usd} (¥{formatted_yen})"
            print(Validate_Starting_price)

            assert Validate_Starting_price == Starting_price.text

            self.wait.until(EC.element_to_be_clickable(self.Yes_button_XPATH)).click()
            print("Yes button is tapped")

            self.wait.until(EC.element_to_be_clickable(self.Okay_pre_bid_XPATH)).click()

# --------------- CANCEL -------------------------#
    time.sleep(2)
    def cancel_prebid(self):

        elements = self.driver.find_elements(*self.Cancel_Pre_bid_XPATH)

        if elements:
            self.wait.until(EC.element_to_be_clickable(self.Cancel_Pre_bid_XPATH)).click()
            print("Cancel Pre-bid is tapped")

            self.wait.until(EC.element_to_be_clickable(self.Confirm_Pre_bid_XPATH)).click()
            print("Confirm Cancel Pre-bid is tapped")

            self.wait.until(EC.element_to_be_clickable(self.Okay_pre_bid_XPATH)).click()
            print("Okay is tapped")

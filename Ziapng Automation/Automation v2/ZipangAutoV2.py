import re
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


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


    NR_XPATH = (AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'NR')]")


    Search_Box_XPATH = (AppiumBy.XPATH,"//android.widget.TextView[@text='Search']")
    Search_Input_Class = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    Search_Product_Class = (AppiumBy.CLASS_NAME, "android.widget.TextView")
    Cancel_Search_AU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")')

    Export_sheet_AU = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")")
    Done_Option_XPATH = (AppiumBy.XPATH,"//android.widget.TextView[@text = 'Done!']")

    Certificate_XPATH = (AppiumBy.XPATH,f"//android.view.ViewGroup[contains(@content-desc,'GIA,')]")

    Watchlist_enable_XPATH = (AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc=''])[1]")
    Watchlist_disable_XPATH = (AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='']")

    Sort_Popup_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")")
    Serial_Number_Au = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Serial Number")')
    Lab_XPATH_AU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lab")')
    Carat_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Carat")')
    Color_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Color")')
    Clarity_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Clarity")')
    No_Of_Pieces_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No Of Pieces")')
    Shape_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Shape")')
    Sieve_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sieve")')
    Cut_Grade_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cut Grade")')
    Symmetry_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Symmetry")')
    Flour_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flour")')
    Starting_price1_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Starting Price")')
    Rap_Off_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rap Off")')
    Clear_Sort_XPATH = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Clear")')


    Notes_Padding_AU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)')
    Add_Notes_AU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().descriptionContains("Add Notes"))')
    Message_input_XPATH = (AppiumBy.XPATH,"//android.widget.EditText[@text='Enter Notes']")
    Save_Button_XPATH = (AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='Save']")
    Done_Button_XPATH = (AppiumBy.XPATH,"//android.widget.TextView[@text='Done!']")
    Okay_Button_Xpath = (AppiumBy.ACCESSIBILITY_ID, "Okay")
    View_Notes_Au = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().descriptionContains("View Notes"))')
    Clear_Notes_Au = (AppiumBy.XPATH,"//android.widget.TextView[@text='Clear']")
    Okay1_Button_XPATH = (AppiumBy.ACCESSIBILITY_ID,"Okay")


    Select_All_AU = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.view.ViewGroup\").instance(39)")
    Bulk_Bid_Au = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(0)')
    Items_Stored_XPATH = (AppiumBy.XPATH, "//android.widget.TextView[@text = '10 items selected']")
    Watchlist_AU = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"\").instance(0)")
    Proceed_Button_AU = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Proceed\")")
    Real_Text_AU = (AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'selected products watchlisted and pre-bidded.')]")
    Place_Bid_Access_ID = (AppiumBy.ACCESSIBILITY_ID,"Place Bid")

    Open_Filter_AU =  (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
    Weight_Dropdown_Au = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(1)')
    From_Weight_ct_Au = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(0)')
    To_Weight_ct_AU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").instance(1)')
    Apply_filter_Au =  (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")')
    Parcel_Filter_Weight_Au = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Parcel")')

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

    def cancel_prebid(self):
        print("Trying to locate the cancel Pre-bid icon")

        try:
            self.wait.until(EC.presence_of_element_located(self.Cancel_Pre_bid_XPATH))
            print("Cancel pre-bid is present")

            self.wait.until(EC.element_to_be_clickable(self.Cancel_Pre_bid_XPATH)).click()
            print("Cancel Pre-bid is tapped")

            self.wait.until(EC.element_to_be_clickable(self.Confirm_Pre_bid_XPATH)).click()
            print("Confirm Cancel Pre-bid is tapped")

            self.wait.until(EC.element_to_be_clickable(self.Okay_pre_bid_XPATH)).click()
            print("Okay is tapped")

        except Exception:
            print("Cancel Pre-bid not found or not clickable")
            assert False

# ---------------- NR --------------------------------#

    def NR(self):

        self.wait.until(EC.element_to_be_clickable(self.NR_XPATH)).click()
        print("NR button is tapped(enabled)")
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self.NR_XPATH)).click()
        print("NR button is tapped(disabled)")

# --------------- Search ------------------------------#

    def Search(self,search):

        self.wait.until(EC.element_to_be_clickable(self.Search_Box_XPATH)).click()
        print("Search button is tapped")

        self.wait.until(EC.presence_of_element_located(self.Search_Input_Class)).send_keys(search)
        print("Search input field is enable to search")

        self.wait.until(EC.presence_of_element_located(self.Search_Product_Class)).click()
        print(f"Search is tapped and the search produc has either remarks or S.no {search}")

        self.wait.until(EC.element_to_be_clickable(self.Cancel_Search_AU)).click()
        print("Search is cancelled")

# ------------------ Export ----------------------------#

    def Export(self):

        self.wait.until(EC.element_to_be_clickable(self.Export_sheet_AU)).click()
        print("Export button is tapped")

        Download = self.wait.until(EC.element_to_be_clickable(self.Done_Option_XPATH))
        assert Download
        Download.click()
        print("Done option button is tapped")

# ------------------- Certificate -----------------------#
    def Certificate(self):
        try:
            Type = input("Enter the Certificate type:")
            self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f"//android.view.ViewGroup[contains(@content-desc,'{Type},')]"))).click()
            print("Certificate type is tapped")
            time.sleep(2)
            self.driver.back()

        except:
            print("Element does not contain Certificate like Non-Cert and others")
            assert False

# ------------------- Watchlist --------------------------#

    def Watchlist(self):

        self.wait.until(EC.element_to_be_clickable(self.Watchlist_enable_XPATH)).click()
        print("Watchlist is placed")

        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable(self.Watchlist_disable_XPATH)).click()
        print("Watchlist is disabled")


# ------------------------- Sort ---------------------------#

    def Sort(self):

        try:
            Sort = self.wait.until(EC.presence_of_element_located(self.Sort_Popup_XPATH))
            Sort.click()
            print("Sort is clicked")

            print("\n Choose the options that how to sort the data:")
            print("1. Serial Number")
            print("2. Lab")
            print("3. Carat")
            print("4. Color")
            print("5. Clarity")
            print("6. No Of Pieces")
            print("7. Shape")
            print("8. Sieve")
            print("9. Cut Grade")
            print("10. Symmetry")
            print("11. Flour")
            print("12. Starting Price")
            print("13. Rap Off")

            choices5 = input("Enter the option: ")

            def Serial_Number():
                self.wait.until(EC.element_to_be_clickable(self.Serial_Number_Au)).click()
                print("Serial number is tapped")

            def Lab():
                self.wait.until(EC.element_to_be_clickable(self.Lab_XPATH_AU)).click()
                print("Lab is tapped")

            def Carat():
                self.wait.until(EC.element_to_be_clickable(self.Carat_XPATH)).click()
                print("Carat is tapped")

            def Color():
                self.wait.until(EC.element_to_be_clickable(self.Color_XPATH)).click()
                print("Color is tapped")

            def Clarity():
                self.wait.until(EC.element_to_be_clickable(self.Clarity_XPATH)).click()
                print("Clarity is tapped")

            def No_Of_Pieces():
                self.wait.until(EC.element_to_be_clickable(self.No_Of_Pieces_XPATH)).click()
                print("No Of Pieces is tapped")

            def Shape():
                self.wait.until(EC.element_to_be_clickable(self.Shape_XPATH)).click()
                print("Shape is tapped")

            def Sieve():
                self.wait.until(EC.element_to_be_clickable(self.Sieve_XPATH)).click()
                print("Sieve is tapped")

            def Cut_Grade():
                self.wait.until(EC.element_to_be_clickable(self.Cut_Grade_XPATH)).click()
                print("Cut Grade is tapped")

            def Symmetry():
                self.wait.until(EC.element_to_be_clickable(self.Symmetry_XPATH)).click()
                print("Symmetry is tapped")

            def Flour():
                self.wait.until(EC.element_to_be_clickable(self.Flour_XPATH)).click()
                print("Flour is tapped")

            def Starting_price():
                self.wait.until(EC.element_to_be_clickable(self.Starting_price1_XPATH)).click()
                print("Starting Price is tapped")

            def Rap_Off():
                self.wait.until(EC.element_to_be_clickable(self.Rap_Off_XPATH)).click()
                print("Rap Off is tapped")

            match choices5:
                case "1":
                    Serial_Number()
                case "2":
                    Lab()
                case "3":
                    Carat()
                case "4":
                    Color()
                case "5":
                    Clarity()
                case "6":
                    No_Of_Pieces()
                case "7":
                    Shape()
                case "8":
                    Sieve()
                case "9":
                    Cut_Grade()
                case "10":
                    Symmetry()
                case "11":
                    Flour()
                case "12":
                    Starting_price()
                case "13":
                    Rap_Off()

            is_closed = self.wait.until(EC.invisibility_of_element_located(self.Clear_Sort_XPATH))
            assert is_closed
            print("Sort applied and popup closed")

        except:
            print("You are in Past auction Choose different option")

        time.sleep(5)
        Sort.click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located(self.Clear_Sort_XPATH)).click()

# ------------------------------- Notes ------------------------#
    def notes(self, Element, Message):
        try:
            Target = str(Element)
            scrolls = 1000
            prev_source = ""

            for i in range(scrolls):

                print(f"Attempt {i + 1}")

                try:
                    element = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().text("{Target}")'
                    )

                    if element.is_displayed():
                        print("Performing Element Tapping")

                        element.click()
                        break

                except:
                    print("Not Visible yet...")

                current_source = self.driver.page_source

                if current_source == prev_source:
                    print("Reached end of list")
                    break

                prev_source = current_source

                self.driver.swipe(500, 1500, 500, 600, 800)

                time.sleep(1)

            # OUTSIDE LOOP
            self.wait.until(
                EC.element_to_be_clickable(self.Notes_Padding_AU)
            ).click()

            print("Opening notes option")

            Add_Notes = self.driver.find_elements(
                *self.Add_Notes_AU
            )

            if Add_Notes:
                Add_Notes[0].click()
                print("Add Notes")

                self.wait.until(
                    EC.presence_of_element_located(self.Message_input_XPATH)
                ).send_keys(Message)

                print(f"Message has been added : {Message}")

                self.wait.until(
                    EC.element_to_be_clickable(self.Save_Button_XPATH)
                ).click()

                print("Save button is tapped")

                Done = self.wait.until(
                    EC.presence_of_element_located(self.Done_Button_XPATH)
                )

                assert Done.text == "Done!"

                self.wait.until(
                    EC.element_to_be_clickable(self.Okay_Button_Xpath)
                ).click()

                print("Okay button is tapped")

                self.driver.back()

            else:
                self.wait.until(
                    EC.presence_of_element_located(self.View_Notes_Au)
                ).click()

                print("View notes option is tapped")

                self.wait.until(
                    EC.presence_of_element_located(self.Clear_Notes_Au)
                ).click()

                print("Clear notes option is tapped")

                self.wait.until(
                    EC.presence_of_element_located(self.Okay1_Button_XPATH)
                ).click()

                print("Okay button is tapped")

        except:
            print("You are in Past auction Choose different option")

            self.driver.back()
            assert False

# ---------------------------- Long press -----------------------

    def Long_Press(self, Element):

        global element
        try:
            Target = str(Element)
            scrolls = 1000
            prev_source = ""
            finger = PointerInput("touch", "finger")
            actions = ActionBuilder(self.driver, mouse=finger)

            for i in range(scrolls):

                print(f"Attempt {i + 1}")

                try:
                    element = self.driver.find_element(
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().text("{Target}")'
                    )

                    if element.is_displayed():
                        print("Performing Element Tapping")

                        loc = element.location
                        size = element.size

                        center_x = loc['x'] + size['width'] // 2
                        center_y = loc['y'] + int(size['height'] * 0.7)

                        actions.pointer_action.move_to_location(center_x, center_y)
                        actions.pointer_action.pointer_down()
                        actions.pointer_action.pause(2)
                        actions.pointer_action.pointer_up()
                        actions.perform()

                        break

                except:
                    print("Not Visible yet...")

                current_source = self.driver.page_source

                if current_source == prev_source:
                    print("Reached end of list")
                    break

                prev_source = current_source

                self.driver.swipe(500, 1500, 500, 600, 800)

                time.sleep(1)

        except:
            print(f"No element found {element}")

    def Bulk_Bid(self,bulkbid,element):

        self.wait.until(EC.element_to_be_clickable(self.Select_All_AU)).click()
        print("Select all is tapped")

        self.wait.until(EC.element_to_be_clickable(self.Bulk_Bid_Au)).click()
        print("Bulk bid is tapped")

        items = self.wait.until(EC.presence_of_element_located(self.Items_Stored_XPATH))
        Number_Items = int(re.search(r"\d+",items.text).group(0))
        time.sleep(2)

        try:
            self.wait.until(EC.element_to_be_clickable(self.Watchlist_AU)).click()
            print("Watchlist is added")
        except:
            print("Watchlist is already added")

        time.sleep(2)

        self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true))'f'.scrollIntoView(new UiSelector().text("{element}"))'))).click()
        print(f"{element} is shown")

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("$ {bulkbid}")'))).click()
        print(f"Placing the bid on {element} of ${bulkbid}")

        self.wait.until(EC.element_to_be_clickable(self.Proceed_Button_AU)).click()
        print("Proceed button is tapped")

        Real_text = self.wait.until(EC.presence_of_element_located(self.Real_Text_AU))
        print(Real_text.text)

        Result_text = f"{Number_Items}/10 selected products watchlisted and pre-bidded."
        print(Result_text)

        assert Real_text.text == Result_text

        self.wait.until(EC.element_to_be_clickable(self.Place_Bid_Access_ID)).click()
        print("Place a bid is tapped")

# -------------------------- Filter --------------------------------------------

    def Filter_Diamond(self,from_Weight_ct,to_Weight_ct):

        self.wait.until(EC.presence_of_element_located(self.Open_Filter_AU)).click()
        print("Filter is tapped")

        self.wait.until(EC.element_to_be_clickable(self.Weight_Dropdown_Au)).click()
        print("Weight dropdown is tapped")

        # From_Weight_ct = input("Enter the Weight From :")
        self.wait.until(EC.presence_of_element_located(self.From_Weight_ct_Au)).send_keys(from_Weight_ct)

        # To_Weight_ct = input("Enter the Weight To :")
        self.wait.until(EC.presence_of_element_located(self.To_Weight_ct_AU)).send_keys(to_Weight_ct)

        print(f"Weight is entered From: {from_Weight_ct} and To: {to_Weight_ct}")

        self.wait.until(EC.element_to_be_clickable(self.Apply_filter_Au)).click()
        print("Filter is applied")

    def Parcel_filter(self,from_Weight_ct,to_Weight_ct):

        self.wait.until(EC.presence_of_element_located(self.Open_Filter_AU)).click()
        print("Filter is tapped")
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.Parcel_Filter_Weight_Au)).click()
        print("Parcel is tapped")
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.Weight_Dropdown_Au)).click()
        print("Weight dropdown is tapped")
        time.sleep(1)
        # From_Weight_ct = input("Enter the Weight From :")

        self.wait.until(EC.presence_of_element_located(self.From_Weight_ct_Au)).send_keys(from_Weight_ct)

        # To_Weight_ct = input("Enter the Weight To :")
        self.wait.until(EC.presence_of_element_located(self.To_Weight_ct_AU)).send_keys(to_Weight_ct)

        print(f"Weight is entered From: {from_Weight_ct} and To: {to_Weight_ct}")

        self.wait.until(EC.element_to_be_clickable(self.Apply_filter_Au)).click()
        print("Filter is applied")
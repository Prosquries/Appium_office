# Workflow of preview section and past auction
import re
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pyasn1_modules.rfc3125 import PathLenConstraint
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()

#--------------- Desired Capabilities ---------------
options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.myauctions.zipang"
options.app_activity = "com.myauctions.zipang.MainActivity"

driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 15)

# -------------- Accounts --------------

Seller = "Kanika.agarwal@sysquare.in"
Bidder = "jagadeesh.yadav@sysquare.in"
Both = "aarav1@mail.com"

# -------------- Workflows ---------------

def Accounts():
    try:
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        )).click()
        print("Allow is clicked")
    except:
        print("Allow is not clicked")

    time.sleep(3)

    print("\n Choose the User")
    print("1. Seller account")
    print("2. Bidder account")
    print("3. Seller and bidder both")

    choices = input("Enter the account: ")
    return choices

def test_workflow():

    choices = Accounts()
    if choices == "1":
        email_value = Seller
    elif choices == "2":
        email_value = Bidder
    elif choices == "3":
        email_value = Both
    else:
        print("Invalid choice")

    try:
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'))).click()

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")'))).click()

        print("Login page is opened")
    except:
        print("Login is not opened")

    try:
        Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
        Email.send_keys(email_value)
        print("Email sent successfully")

        password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
        password.send_keys("password")
        print("Password sent successfully")

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()
        print("Remember me is Tapped")

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()
        print("Logged is Tapped")

    except:
        print("Login failed")
    time.sleep(2)

#----------------------- pre-bid -------------------------------------------

    try:
        pre_bid_element = driver.find_elements(AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'Set Pre-Bid')]")

        cancel_element = driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@text='Cancel Pre-Bid']")

        print("\n Choose weather you want to")
        print("1. Place a pre-bid")
        print("2. Cancel Pre-Bid")

        choices1 = input("Enter the state: ")
        time.sleep(1)
        def pre_bid():
            if pre_bid_element:
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc,'Set Pre-Bid')]"))).click()
                print("Set Pre-Bid is Tapped")
                amount = input("Enter the amount : ")

                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Per Ct']"))).send_keys(amount)
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Save']"))).click()
                time.sleep(2)

                # Wait for confirmation popup
                wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Confirm Pre-Bid')]")
                ))

                # Extract carat
                Certificate1 = input("Enter the Certificate type: ")
                carat_text = wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, f"//android.widget.TextView[contains(@text,'1- 2467124122') or contains(@text,'{Certificate1}')]")
                )).text

                carat_match = re.search(r'(\d+\.?\d*)\s*[cC][tT]', carat_text)

                if carat_match:
                    carat_value = float(carat_match.group(1))
                    print("Carat:", carat_value)

                # Extract starting price
                price_text = wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[contains(@text,'Starting Price')]")
                )).text

                price_match = re.search(r'\$([\d,]+)', price_text)

                if price_match:
                    price_value = int(price_match.group(1).replace(",", ""))
                    print("Starting Price:", price_value)

                Exchange_rate = float(input("Enter the exchange rate : "))

                Starting_Price = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Starting Price')]")
                print(Starting_Price.text)

                formatted_usd = f"{price_value:,}"
                formatted_yen = f"{int(price_value * Exchange_rate):,}"

                Validate_Starting_price = f"Starting Price (PCt). - ${formatted_usd} (¥{formatted_yen})"
                print(Validate_Starting_price)

                # print(repr(Starting_Price.text))
                # print(repr(Validate_Starting_price))

                assert Validate_Starting_price == Starting_Price.text
                amount = float(amount)
                if price_value >= 30000:
                    amount = amount * 100

                elif price_value >= 100:
                    amount = amount * 10

                else:
                    amount = amount

                total_usd = amount * carat_value
                total_yen = round(total_usd * Exchange_rate)

                formatted_usd = f"{total_usd:,.2f}"
                formatted_yen = f"{total_yen:,.2f}"

                Amount_After = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'Amount')]")
                print(Amount_After.text)

                Validate_Amount = f"Amount = $ {formatted_usd} (¥ {formatted_yen})"
                print(Validate_Amount)

                assert Validate_Amount == Amount_After.text

                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Yes']"))).click()
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Okay']"))).click()
                print("Pre-bid placed successfully")

        def cancel_prebid():
            if cancel_element:
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Cancel Pre-Bid']"))).click()
                print("Cancel Pre-Bid is Tapped")
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Confirm']"))).click()
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='Okay']"))).click()
                print("Pre-bid cancelled")

            else:
                print("None of the options available")

        match choices1:
            case "1":
                pre_bid()
            case "2":
                cancel_prebid()
    except:
        print("You are a seller or on past auction or the live bidding is started")
        assert False
# ------------------------- NR --------------------------------------

    time.sleep(2)

    try:
        NR = driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'NR')]")
        Disable_NR = driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'NR')]")

        print("\n Choose weather you want to")
        print("1. Place a NR")
        print("2. Remove NR")

        choices3 = input("Enter the state: ")

        def NR_enable():
            if NR:
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.view.ViewGroup[contains(@content-desc,'NR')]"))).click()
                print("NR is Enabled")



        def NR_disable():
            if Disable_NR:
                wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.view.ViewGroup[contains(@content-desc,'NR')]"))).click()
                print("NR is Disabled")

        match choices3:
            case "1":
                NR_enable()
            case "2":
                NR_disable()

    except:
        print("NR nott found or You or on past auction")

#  ------------------------- Search -------------------------------
    try:

        Non_Past = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(44)')
        Past = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(40)')

        print("\n Choose the options:")
        print("1. You are in either Pre-bid,Live-bid,Locked,Short-break,Paused stage")
        print("2. You are in past auction")

        choices4 = input("Enter the option: ")

        def non_past():
            if Non_Past:
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(44)'))).click()
                Search = input("Enter the Serial Number of Remarks to search the element: ")

                search_box = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
                search_box.send_keys(Search)

                wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.TextView"))).click()
                print(f"You have searched the product by S.no or Remarks  :{Search}")

                wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("")'))).click()
                print("Search cancelled")
        def past():
            if Past:
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(40)'))).click()
                Search = input("Enter the Serial Number of Remarks to search the element: ")

                search_box = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText")))
                search_box.send_keys(Search)

                wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.TextView"))).click()
                print(f"You have searched the product :{Search}")

        match choices4:
            case "1":
                non_past()
            case "2":
                past()

    except:
        print("Search not found either you are in past auction Choose different option")

    time.sleep(2)
# --------- Export sheet -------------

    try:
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")"))).click()
        Downloaded = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'Done!']")))
        assert Downloaded
        Downloaded.click()
        print("Downloaded successfully")
    except:
        print("Download Failed")


#---------------------Sort ------------------------

    try:
        Sort = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")")))
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
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Serial Number")'))).click()
            print("Serial number is tapped")

        def Lab():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lab")'))).click()
            print("Lab is tapped")

        def Carat():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Carat")'))).click()
            print("Carat is tapped")

        def Color():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Color")'))).click()
            print("Color is tapped")

        def Clarity():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Clarity")'))).click()
            print("Clarity is tapped")

        def No_Of_Pieces():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No Of Pieces")'))).click()
            print("No Of Pieces is tapped")

        def Shape():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Shape")'))).click()
            print("Shape is tapped")

        def Sieve():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sieve")'))).click()
            print("Sieve is tapped")

        def Cut_Grade():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Cut Grade")'))).click()
            print("Cut Grade is tapped")

        def Symmetry():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Symmetry")'))).click()
            print("Symmetry is tapped")

        def Flour():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flour")'))).click()
            print("Flour is tapped")

        def Starting_price():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Starting Price")'))).click()
            print("Starting Price is tapped")

        def Rap_Off():
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rap Off")'))).click()
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

        is_closed = wait.until(EC.invisibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Clear")')))
        assert is_closed
        print("Sort applied and popup closed")

    except:
        print("You are in Past auction Choose different option")

    input("Press enter to remove the sort and continue...")
    Sort.click()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Clear")'))).click()

#---------------- tapping on certificate -----------------------

    try:
        Type = input("Enter the Certificate type:")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH,f"//android.view.ViewGroup[contains(@content-desc,'{Type},')]"))).click()
        print("Certificate type is tapped")
        time.sleep(2)
        driver.back()

    except:
        print("Element does not contain Certificate like Non-Cert and others")
        assert False

# --------------------- Watchlist --------------------------

    try:

        print("\n Choose the Case:")
        print("1. Add the watchlist on the product")
        print("2. Remove the watchlist from the product")

        choices6 = input("Choose the number: ")

        def Watchlist_Enable():
            element = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"(//android.view.ViewGroup[@content-desc=''])[1]")))
            element.click()
            print("Watchlist is added")

        def Watchlist_Disabled():

            element = wait.until(EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[@content-desc='']"
            )))
            element.click()
            print("Watchlist removed")

        match choices6:
            case "1":
                Watchlist_Enable()
            case "2":
                Watchlist_Disabled()

    except:
        print("Watchlist cannot be placed")
        assert False

# ------------ Notes --------------------------

    try:
        Element = input("Enter the number of element to apply notes :")
        target = str(Element)  # Element = "7" or any number
        Scrolls = 100000
        prev_source = ""

        for i in range(Scrolls):
            print(f"Attempt {i + 1}")

            try:
                element = driver.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().text("{target}")'
                )

                if element.is_displayed():
                    print(" Performing Element Tapping functionality")

                    time.sleep(1)
                    element.click()

                    break

            except:
                print("Not visible yet... scrolling")

            #  Detect if list stopped loading
            current_source = driver.page_source
            if current_source == prev_source:
                print(" Reached end of list (no more items loading)")
                break

            prev_source = current_source

            #  Scroll down manually (IMPORTANT for lazy load)
            driver.swipe(500, 1500, 500, 600, 800)

            time.sleep(3)  # give time for new items (11,12...) to load

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)'))).click()
        print("Open the Notes and Padding options")

        try:
            Add_Notes = wait.until(EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().descriptionContains("Add Notes"))'
            )))

            Add_Notes.click()
            print("Add notes is tapped")

            Message = input("Enter the message to be sent: ")

            wait.until(EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.EditText[@text='Enter Notes']"
            ))).send_keys(Message)

            print(f"Message is entered {Message}")

            wait.until(EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.view.ViewGroup[@content-desc='Save']"
            ))).click()

            print("Save is clicked")

            Done = wait.until(EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Done!']"
            )))

            assert Done.text == "Done!"

            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Okay").click()

            driver.back()

        except:
            # fallback -> View Notes
            View_Notes = wait.until(EC.presence_of_element_located((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().descriptionContains("View Notes"))'
            )))

            View_Notes.click()
            print("View Notes is tapped")

            wait.until(EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.TextView[@text='Clear']"
            ))).click()

            print("Clear is tapped")

            Done1 = wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                "Okay"
            )))

            Done1.click()
            print("Done is pressed")

    except:
        print("You are a seller or on past auction or Notes already Written")
        driver.back()
        # assert False


#----------------- Long press or select a single product ----------------

    Element = input("Enter the number of element :")
    target = str(Element)  # Element = "7" or any number
    Scrolls = 100000
    prev_source = ""
    finger = PointerInput("touch", "finger")
    actions = ActionBuilder(driver, mouse=finger)

    for i in range(Scrolls):
        print(f"Attempt {i + 1}")

        try:
            element = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiSelector().text("{target}")'
            )

            if element.is_displayed():
                print(" Element found, performing long press")

                time.sleep(1)

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
            print("Not visible yet... scrolling")

        #  Detect if list stopped loading
        current_source = driver.page_source
        if current_source == prev_source:
            print(" Reached end of list (no more items loading)")
            break

        prev_source = current_source

        #  Scroll down manually (IMPORTANT for lazy load)
        driver.swipe(500, 1500, 500, 600, 800)

        time.sleep(3)  #  give time for new items (11,12...) to load

    else:
        print("Element not found")

# #----------------------- Bulk Bid --------------------------------- #
    try:

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.view.ViewGroup\").instance(39)"))).click()
        print("Select all is tapped")
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.ImageView\").instance(0)"))).click()
        print("Bulk bid is tapped")

        Items = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text = '10 items selected']")))
        Number_items = int(re.search(r"\d+",Items.text).group(0))
        time.sleep(1)

        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"\").instance(0)"))).click()
            print("Adding watchlist")
        except:
            print("Watchlist is already added")
        time.sleep(1)
        Bulk_bid = input("Enter the pre-bid amount (100,1000 or 10000):")

        Number = input("Enter the number")


        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true))'f'.scrollIntoView(new UiSelector().text("{Number}"))')))

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().description("+, $ {Bulk_bid}")'))).click()
        print(f"Placing a bid on {Number} of ${Bulk_bid}")
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Proceed\")"))).click()
        print("Tapped on proceed")
        time.sleep(2)
        Real_text = driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[contains(@text,'selected products watchlisted and pre-bidded.')]")
        print(Real_text.text)
        Result_text = f"{Number_items}/10 selected products watchlisted and pre-bidded."
        print(Result_text)
        assert Result_text == Real_text.text
        wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"Place Bid"))).click()
        print("Tapped on place a bid")

    except:
        print("Select all is failed to tapped")
        assert False

# -------------------- Filter --------------------------

    try:
        print("\n Choose the Filter Type:")
        print("1. Diamond")
        print("2. Parcel")

        Choose7 = input("Choose your option: ")

        def Diamond():
            try:
                wait.until(EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'))).click()
                print("Filter is tapped")

                print("\n Choose the options")
                print("1. Price")
                print("2. Weight")
                print("3. Shape")
                print("4. Color")
                print("5. Clarity")
                print("6. Grading ")

                choices8 = input("Choose your option: ")

                def price():
                    try:
                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)'))).click()
                        print("Price dropdown is tapped")

                        From_Price_ct = input("Enter the Price From :")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(0)'))).send_keys(
                            From_Price_ct)

                        To_Price_ct = input("Enter the Price To :")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(1)'))).send_keys(
                            To_Price_ct)

                        print(f"Price is entered From: {From_Price_ct} and TO: {To_Price_ct}")

                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Weight"))')))

                        From_Price_total = input("Enter the Total From:")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiScrollable(new UiSelector().scrollable(true))''.scrollIntoView(new UiSelector().className("android.widget.EditText").instance(2))'))).send_keys(
                            From_Price_total)

                        To_Price_total = input("Enter the Total To:")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(3)'))).send_keys(
                            To_Price_total)

                        print(f"Total price is entered From: {From_Price_total} and To: {To_Price_total}")

                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                        print("Filter is applied")

                    except:
                        print("You are a guest Login first to unlock the Price filter")

                def weight():
                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(1)'))).click()
                    print("Weight dropdown is tapped")

                    From_Weight_ct = input("Enter the Weight From :")
                    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().className("android.widget.EditText").instance(0)'))).send_keys(
                        From_Weight_ct)

                    To_Weight_ct = input("Enter the Weight To :")
                    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().className("android.widget.EditText").instance(1)'))).send_keys(
                        To_Weight_ct)

                    print(f"Weight is entered From: {From_Weight_ct} and To: {To_Weight_ct}")

                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                    print("Filter is applied")

                def shape():
                    try:
                        wait.until(EC.element_to_be_clickable((
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("").instance(2)'
                        ))).click()

                        print("Shape dropdown is tapped")

                        print("\n Choose the Shape:")
                        print("1. Round")
                        print("2. Emerald Cut")
                        print("3. Marquise")
                        print("4. Princess")
                        print("5. Oval")
                        print("6. Pear Shape")
                        print("7. Asscher")
                        print("8. Radiant")
                        print("9. Heart Shape")
                        print("10. Cushion Brilliant")
                        print("11. Baguette")
                        print("12. Rectangular")
                        print("13. Round Brilliant")
                        print("14. Round Brilliant Modified")
                        print("15. Square")
                        print("16. Tapered Baguette")
                        print("17. Trilliant")
                        print("18. Unknown")

                        choice = input("Enter your choice: ")

                        if choice == "1":
                            selected_shape = "Round"
                        elif choice == "2":
                            selected_shape = "Emerald Cut"
                        elif choice == "3":
                            selected_shape = "Marquise"
                        elif choice == "4":
                            selected_shape = "Princess"
                        elif choice == "5":
                            selected_shape = "Oval"
                        elif choice == "6":
                            selected_shape = "Pear Shape"
                        elif choice == "7":
                            selected_shape = "Asscher"
                        elif choice == "8":
                            selected_shape = "Radiant"
                        elif choice == "9":
                            selected_shape = "Heart Shape"
                        elif choice == "10":
                            selected_shape = "Cushion Brilliant"
                        elif choice == "11":
                            selected_shape = "Baguette"
                        elif choice == "12":
                            selected_shape = "Rectangular"
                        elif choice == "13":
                            selected_shape = "Round Brilliant"
                        elif choice == "14":
                            selected_shape = "Round Brilliant Modified"
                        elif choice == "15":
                            selected_shape = "Square"
                        elif choice == "16":
                            selected_shape = "Tapered Baguette"
                        elif choice == "17":
                            selected_shape = "Trilliant"
                        elif choice == "18":
                            selected_shape = "Unknown"
                        else:
                            print("Invalid choice")
                            return

                        wait.until(EC.element_to_be_clickable((
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiScrollable(new UiSelector().scrollable(true))'
                            f'.scrollIntoView(new UiSelector().text("{selected_shape}"))'
                        ))).click()

                        print(f"{selected_shape} is selected")

                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                        print("Filter is applied")

                    except:
                        print("Choose the correct Shape")

                def color():
                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(3)'))).click()
                    print("Color dropdown is tapped")

                    print("\n Choose the Color:")
                    print("1. Fancy")
                    print("2. D")
                    print("3. E")
                    print("4. F")
                    print("5. G")
                    print("6. H")
                    print("7. I")
                    print("8. J")
                    print("9. K")
                    print("10. L")
                    print("11. M")
                    print("12. UNDER N")
                    print("13. UNDER S")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        selected_color = "Fancy"
                    elif choice == "2":
                        selected_color = "D"
                    elif choice == "3":
                        selected_color = "E"
                    elif choice == "4":
                        selected_color = "F"
                    elif choice == "5":
                        selected_color = "G"
                    elif choice == "6":
                        selected_color = "H"
                    elif choice == "7":
                        selected_color = "I"
                    elif choice == "8":
                        selected_color = "J"
                    elif choice == "9":
                        selected_color = "K"
                    elif choice == "10":
                        selected_color = "L"
                    elif choice == "11":
                        selected_color = "M"
                    elif choice == "12":
                        selected_color = "UNDER N"
                    elif choice == "13":
                        selected_color = "UNDER S"

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true))'
                        f'.scrollIntoView(new UiSelector().description("{selected_color}"))'
                    ))).click()

                    print(f"{selected_color} is selected")

                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                    print("Filter is applied")

                def clarity():
                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("").instance(4)'
                    ))).click()

                    print("Clarity dropdown is tapped")

                    print("\n Choose the Clarity:")
                    print("1. FL")
                    print("2. IF")
                    print("3. VVS-1")
                    print("4. VVS-2")
                    print("5. VS-1")
                    print("6. VS-2")
                    print("7. SI-1")
                    print("8. SI-2")
                    print("9. SI-3")
                    print("10. I-1")
                    print("11. I-2")
                    print("12. I-3")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        selected_clarity = "FL"
                    elif choice == "2":
                        selected_clarity = "IF"
                    elif choice == "3":
                        selected_clarity = "VVS-1"
                    elif choice == "4":
                        selected_clarity = "VVS-2"
                    elif choice == "5":
                        selected_clarity = "VS-1"
                    elif choice == "6":
                        selected_clarity = "VS-2"
                    elif choice == "7":
                        selected_clarity = "SI-1"
                    elif choice == "8":
                        selected_clarity = "SI-2"
                    elif choice == "9":
                        selected_clarity = "SI-3"
                    elif choice == "10":
                        selected_clarity = "I-1"
                    elif choice == "11":
                        selected_clarity = "I-2"
                    elif choice == "12":
                        selected_clarity = "I-3"
                    else:
                        print("Invalid choice")
                        return

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true))'
                        f'.scrollIntoView(new UiSelector().text("{selected_clarity}"))'
                    ))).click()

                    print(f"{selected_clarity} is selected")

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().description("Apply filter")'
                    ))).click()

                    print("Filter is applied")

                def grading():
                    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(1)')
                    print("Scrolled till Grading")

                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(5)'))).click()

                    print("\n Choose the Grading:")
                    print("1. GIA")
                    print("2. CGL")
                    print("3. HRD")
                    print("4. AGT")
                    print("5. DGL")
                    print("6. IGI")
                    print("7. IGT")
                    print("8. NON-CERT")
                    print("9. OTHERS")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        selected_grading = "GIA"
                    elif choice == "2":
                        selected_grading = "CGL"
                    elif choice == "3":
                        selected_grading = "HRD"
                    elif choice == "4":
                        selected_grading = "AGT"
                    elif choice == "5":
                        selected_grading = "DGL"
                    elif choice == "6":
                        selected_grading = "IGI"
                    elif choice == "7":
                        selected_grading = "IGT"
                    elif choice == "8":
                        selected_grading = "NON-CERT"
                    elif choice == "9":
                        selected_grading = "OTHERS"
                    else:
                        print("Invalid choice")
                        return

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true))'
                        f'.scrollIntoView(new UiSelector().text("{selected_grading}"))'
                    ))).click()

                    print(f"{selected_grading} is selected")

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().description("Apply filter")'
                    ))).click()

                    print("Filter is applied")

                match choices8:
                    case "1":
                        price()
                    case "2":
                        weight()
                    case "3":
                        shape()
                    case "4":
                        color()
                    case "5":
                        clarity()
                    case "6":
                        grading()

            except:
                print("Diamond options are wrong")

        def Parcel():
            try:

                wait.until(EC.presence_of_element_located(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'))).click()
                print("Filter is tapped")

                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Parcel")'))).click()
                print("Parcel is selected")

                print("\n Choose the options")
                print("1. Price")
                print("2. Weight")
                print("3. Shape")
                print("4. Color")

                choices9 = input("Choose your option: ")

                def price():
                    try:
                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(0)'))).click()
                        print("Price dropdown is tapped")

                        From_Price_ct = input("Enter the Price From :")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(0)'))).send_keys(
                            From_Price_ct)

                        To_Price_ct = input("Enter the Price To :")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(1)'))).send_keys(
                            To_Price_ct)

                        print(f"Price is entered From: {From_Price_ct} and TO: {To_Price_ct}")

                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Weight"))')))

                        From_Price_total = input("Enter the Total From:")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiScrollable(new UiSelector().scrollable(true))''.scrollIntoView(new UiSelector().className("android.widget.EditText").instance(2))'))).send_keys(
                            From_Price_total)

                        To_Price_total = input("Enter the Total To:")
                        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   'new UiSelector().className("android.widget.EditText").instance(3)'))).send_keys(
                            To_Price_total)

                        print(f"Total price is entered From: {From_Price_total} and To: {To_Price_total}")

                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                        print("Filter is applied")

                    except:
                        print("You are a guest Login first to unlock the Price filter")

                def weight():
                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(1)'))).click()
                    print("Weight dropdown is tapped")

                    From_Weight_ct = input("Enter the Weight From :")
                    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().className("android.widget.EditText").instance(0)'))).send_keys(
                        From_Weight_ct)

                    To_Weight_ct = input("Enter the Weight To :")
                    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               'new UiSelector().className("android.widget.EditText").instance(1)'))).send_keys(
                        To_Weight_ct)

                    print(f"Weight is entered From: {From_Weight_ct} and To: {To_Weight_ct}")

                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                    print("Filter is applied")

                def shape():
                    try:
                        wait.until(EC.element_to_be_clickable((
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("").instance(2)'
                        ))).click()

                        print("Shape dropdown is tapped")

                        print("\n Choose the Shape:")
                        print("1. Round")
                        print("2. Fancy Mix")
                        print("3. CAR")
                        print("4. CAR & BG")
                        print("5. Emerald Cut")
                        print("6. Marquize")
                        print("7. Princess")
                        print("8. Oval")
                        print("9. Pear Shape")
                        print("10. Asscher")
                        print("11. Radiant")
                        print("12. Heart Shape")
                        print("13. Cushion Brilliant")
                        print("14. Baguette")
                        print("15. Rectangular")
                        print("16. Round Brilliant")
                        print("17. Round Brilliant Modified")
                        print("18. Square")
                        print("19. Tapered Baguette")
                        print("20. Trilliant")
                        print("21. TP")
                        print("22. Single Cut")
                        print("23. Rose Cut")
                        print("24. Unknown")

                        choice = input("Enter your choice: ")

                        if choice == "1":
                            selected_shape = "Round"
                        elif choice == "2":
                            selected_shape = "Fancy Mix"
                        elif choice == "3":
                            selected_shape = "CAR"
                        elif choice == "4":
                            selected_shape = "CAR & BG"
                        elif choice == "5":
                            selected_shape = "Emerald Cut"
                        elif choice == "6":
                            selected_shape = "Marquize"
                        elif choice == "7":
                            selected_shape = "Princess"
                        elif choice == "8":
                            selected_shape = "Oval"
                        elif choice == "9":
                            selected_shape = "Pear Shape"
                        elif choice == "10":
                            selected_shape = "Asscher"
                        elif choice == "11":
                            selected_shape = "Radiant"
                        elif choice == "12":
                            selected_shape = "Heart Shape"
                        elif choice == "13":
                            selected_shape = "Cushion Brilliant"
                        elif choice == "14":
                            selected_shape = "Baguette"
                        elif choice == "15":
                            selected_shape = "Rectangular"
                        elif choice == "16":
                            selected_shape = "Round Brilliant"
                        elif choice == "17":
                            selected_shape = "Round Brilliant Modified"
                        elif choice == "18":
                            selected_shape = "Square"
                        elif choice == "19":
                            selected_shape = "Tapered Baguette"
                        elif choice == "20":
                            selected_shape = "Trilliant"
                        elif choice == "21":
                            selected_shape = "TP"
                        elif choice == "22":
                            selected_shape = "Single Cut"
                        elif choice == "23":
                            selected_shape = "Rose Cut"
                        elif choice == "24":
                            selected_shape = "Unknown"
                        else:
                            print("Invalid choice")
                            return

                        wait.until(EC.element_to_be_clickable((
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiScrollable(new UiSelector().scrollable(true))'
                            f'.scrollIntoView(new UiSelector().text("{selected_shape}"))'
                        ))).click()

                        print(f"{selected_shape} is selected")

                        wait.until(EC.element_to_be_clickable(
                            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                        print("Filter is applied")

                    except:
                        print("Choose the correct Shape")

                def color():
                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("").instance(3)'))).click()
                    print("Color dropdown is tapped")

                    print("\n Choose the Color:")
                    print("1. Fancy")
                    print("2. D")
                    print("3. E")
                    print("4. F")
                    print("5. G")
                    print("6. H")
                    print("7. I")
                    print("8. J")
                    print("9. K")
                    print("10. L")
                    print("11. M")
                    print("12. UNDER N")
                    print("13. UNDER S")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        selected_color = "Fancy"
                    elif choice == "2":
                        selected_color = "D"
                    elif choice == "3":
                        selected_color = "E"
                    elif choice == "4":
                        selected_color = "F"
                    elif choice == "5":
                        selected_color = "G"
                    elif choice == "6":
                        selected_color = "H"
                    elif choice == "7":
                        selected_color = "I"
                    elif choice == "8":
                        selected_color = "J"
                    elif choice == "9":
                        selected_color = "K"
                    elif choice == "10":
                        selected_color = "L"
                    elif choice == "11":
                        selected_color = "M"
                    elif choice == "12":
                        selected_color = "UNDER N"
                    elif choice == "13":
                        selected_color = "UNDER S"
                    else:
                        print("These options are enough for testing")

                    wait.until(EC.element_to_be_clickable((
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true))'
                        f'.scrollIntoView(new UiSelector().description("{selected_color}"))'
                    ))).click()

                    print(f"{selected_color} is selected")

                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Apply filter")'))).click()
                    print("Filter is applied")

                match choices9:
                    case "1":
                        price()
                    case "2":
                        weight()
                    case "3":
                        shape()
                    case "4":
                        color()

            except:
                print("Parcel options are wrong")

        match Choose7:
            case "1":
                Diamond()
            case "2":
                Parcel()

        input("Press any key to continue")
        driver.quit()

    except:
        print("Filter is unavailable")
        assert False

# ------------------ Exit Code --------------------------

    input("Press any key to exit the automation")
    driver.quit()

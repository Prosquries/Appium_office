# Login automation that works in Every stage (Pre-bidding ends in, Live ongoing)
from appium import webdriver
import time
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()

# Desired Capabilities
options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.myauctions.zipang"
options.app_activity = "com.myauctions.zipang.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)
def test_Login():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text = 'Allow']"))).click()
        print("Allow pop up is pressed")
    except:
        print("Allow pop up is not appeared")

    print("\n Choose the options below")
    print("1. Login by hamburger")
    print("2. Login by Tapping image")
    print("3. Login by Tapping watchlist")
    print("4. Login by Tapping Product")
    print("5. Login by Tapping Set pre-bid")
    print("6. Login by Tapping Enter pre-bid carat")
    print("7. Login by Tapping on Live bidding is ongoing")
    print("8. Login by tapping Auction is ongoing ")
    choice = input("Enter the way of Login: ")

    def test_hamburger():
        try:
            el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")')
            el1.click()
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Login']"))).click()

            print("Login Page is opened")

        except:
            print("Login page is not opened")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")

        except:
            print("Email and password is not entered",)

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_image():
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(0)'))).click()
            print("Image is clicked")
        except:
            print("Image is not clicked")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")
            time.sleep(2)
            driver.back()

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_watchlist():
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("").instance(0)'))).click()
            print("Watchlist is tapped")
        except:
            print("Unable to watchlist the product")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_loginProductDeatil():
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"	//android.widget.TextView[@text='1']"))).click()
            print("Tapping on product deatils")
        except:
            print("Product is failed to tap")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")
            time.sleep(2)
            driver.back()
        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_prebid():
        try:
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Set Pre-Bid").instance(0)').click()
            print("Pre-bid is tapped successfully")

        except Exception as e:
            print("Pre-bid button failed to tap:", e)

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_EnterPrebid():
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'Enter prebid per carat']"))).click()
            print("Enter pre-bid per carat is tapped successfully")
        except:
            print("Pre-bid button failed to tap")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pre-bidding Ends in:")')))
        assert isLoggedin
        print("User is logged in")

    def test_ongoing():
        try:
            el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,value="new UiSelector().text(\"Live bidding is ongoing\")")
            el1.click()
            print("Live Ongoing bidding is ongoing is tapped")
        except:
            print("Live Ongoing bidding is ongoing is not tapped")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")
            time.sleep(5)
            driver.back()

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"10$\")')))
        assert isLoggedin
        print("User is logged in")

    def test_short():
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Auction will resume soon")'))).click()
            print("Auction will resume soon is tapped")
        except:
            print("Auction will resume soon is not tapped")

        try:
            Email = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Email']")))
            Email.send_keys("jagadeesh.yadav@sysquare.in")
            print("Email is entered")

            Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Password']")))
            Password.send_keys("password")
            print("Password is entered")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()

            print("Remember me is tapped")

            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()

            print("Login submitted")

        except:
            print("Email and password is not entered", )

        isLoggedin = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Bidding Countinues in")')))
        assert isLoggedin
        print("User is logged in")

    match choice:
        case "1":
            test_hamburger()
        case "2":
            test_image()
        case "3":
            test_watchlist()
        case "4":
            test_loginProductDeatil()
        case "5":
            test_prebid()
        case "6":
            test_EnterPrebid()
        case "7":
            test_ongoing()
        case "8":
            test_short()
        case _:
            print("Invalid choice")

driver.quit()

    # Problem in past auction all the cases will work but the assertion will fail because there is no difference between the guest user and the logged-in user.
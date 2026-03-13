from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time


def test_parallel(appium_driver):
    wait = WebDriverWait(appium_driver, 10)

    try:
        Number = input(str("Enter the number"))
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.EditText[@resource-id = 'com.samsung.android.dialer:id/digits']"))).send_keys(Number)
        print("Entered the Number")
    except:
        print("Unable to dial the number")

    time.sleep(1)

    try:
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.ImageView[@resource-id = 'com.samsung.android.dialer:id/dialButtonImage']"))).click()
        print("Calling")

    except:
        print("Unable to call")

    try:
        input("Press enter to end the call")
        wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc = 'End call']"))).click()
        print("Call is ended")

    except:
        print("Unable to call")

# To run this parallel we need to use this command ,This also requires packages like pytest-xdist
#python -m pytest -s -v --alluredir=AllureReprtDual  -n=2 test_parallel.py - But this should not include user interactions or it will fail or enter the number before in terminal like --Number= "your number" like that

# To run this 1 by 1 use this command
#python -m pytest -s -v --alluredir=AllureReprtDual  test_parallel.py  - This has a feature of user interactions
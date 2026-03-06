from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "io.appium.android.apis"
options.app_activity = "io.appium.android.apis.ApiDemos"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"Views"))).click()
    print("Clicking the Views option")
except:
    print("Failed to click the Views option")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"Gallery"))).click()
    print("Clicking the Gallery option")
except:
    print("Failed to click the Gallery option")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"1. Photos"))).click()
    print("Clicking the Photos option")
except:
    print("Failed to click the Photos option")

# 1.st way to scroll the list Horizontally
# try:
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward(2)')
#     print("Scrolled the horizontal list Forward")
# except:
#     print("Failed to scroll the horizontal list Forward")
#
# try:
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollBackward(2)')
#     print("Scrolled the horizontal list Backward")
# except:
#     print("Failed to scroll the horizontal list Backward")

## 2.nd
try:
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')
    print("Scroll to beginning")
except:
    print("Failed to scroll the horizontal list Forward")

try:
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)')
    print("Scroll to end")
except:
    print("Failed to scroll the horizontal list Backward")
time.sleep(2)
driver.quit()
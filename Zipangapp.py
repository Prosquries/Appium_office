import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.devtools.v143.target import expose_dev_tools_protocol
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired Capabilities
options = UiAutomator2Options()

options.platform_name="Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "uiautomator2"
options.app_package = "com.myauctions.zipang"
options.app_activity = "com.myauctions.zipang.MainActivity"

# Driver setup

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_button"))).click()
    print("CLicking the permission allow button")
except:
    print("Cannot find the allow button")
try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")"))).click()

    print("Clicking the grid option")
except:
    print("Cannot find the grid option")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Login\")"))).click()
    print("Clicking on login button")
except:
    print("Cannot find the login button")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Email\")"))).send_keys("jagadeesh.yadav@sysquare.in")
    print("Entering the email")
except:
    print("Cannot find the email")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Password\")"))).send_keys("password")
    print("Entering the password")
except:
    print("Cannot find the password")

wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.view.ViewGroup\").instance(25)"))).click()
time.sleep(5)
driver.quit()
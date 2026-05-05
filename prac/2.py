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

print("App is opened")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'Allow']"))).click()
    print("Allow pop up is pressed")
except:
    print("Allow pop up is not appeared")

time.sleep(5)

try:
    el1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"\")")
    el1.click()
    el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Login\")")
    el2.click()
    print("Login Page is opened")
except:
    print("Login page is not opened")

try:
   Email =  wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.EditText[@text = 'Email']")))
   # Email.click()
   Email.send_keys("jagadeesh.yadav@sysquare.in")
   print("Email is entered")
   Password = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.EditText[@text = 'Password']")))
   # Password.click()
   Password.send_keys("password")
   print("Password is entered")
   wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(23)'))).click()
   print("Remember me is tapped")
   wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().className(\"android.widget.ImageView\").instance(1)"))).click()
   print("Email and password is entered")
except:
    print("Email and password is not entered")



input("Press enter to quit the automation")
driver.quit()
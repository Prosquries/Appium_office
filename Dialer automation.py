import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait

#Desired Capabilities
options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.samsung.android.dialer"
options.app_activity = "com.samsung.android.dialer.DialtactsActivity"

driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
wait = WebDriverWait(driver, 10)

Number = str(input("Enter the Number:"))

try:
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

input("Press Enter to end the call")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.ImageButton[@content-desc = 'End call']"))).click()
    print("Call is ended")

except:
    print("Unable to call")


driver.quit()
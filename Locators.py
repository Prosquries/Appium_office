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
options.app_package = "com.android.chrome"
options.app_activity = "com.google.android.apps.chrome.Main"

# Connecting the app from locators

driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
wait = WebDriverWait(driver, 10)


try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'Continue as Aarav']"))).click()
    print("Continue as Aarav is clicked")

except:
    print("Continue as Aarav element is not present")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'Yes, I’m in']"))).click()
    print("Yes I am in is clicked")

except:
    print("Yes I am in is not clicked element is not present")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'Continue']"))).click()
    print("Continue as Aarav is clicked")
except:
    print("Continue element is not present")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'Allow']"))).click()
    print("Allow is clicked")

except:
    print("Allow is not clicked")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.EditText[@text = 'Search Google or type URL']"))).send_keys("selenium")
    print("Search Google or type URL is clicked")

except:
    print("Search element is not present")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'selenium']"))).click()
    print("selenium is clicked")

except:
    print("selenium is not present")

time.sleep(2)
driver.save_screenshot("chrome_test.png")

driver.quit()

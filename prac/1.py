from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.app_package = "com.android.settings"
options.app_activity = ".Settings"

driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 10)

print("App is opened")

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Software update"))')

wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'Software update']"))).click()
print("Software update is clicked")

wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.Button[@text = 'Check for updates']"))).click()

input("Enter to exit the automation")
driver.quit()

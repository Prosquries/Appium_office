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
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'App']"))).click()
    print("App is clicked")
except:
    print("App is not clicked")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.TextView[@text = 'Alert Dialogs']"))).click()
    print("Clicking Alert Dialogs")
except:
    print("Alert Dialogs is not clicked")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = 'TEXT ENTRY DIALOG']"))).click()
    print("Clicking TEXT ENTRY DIALOG")
except:
    print("TEXT ENTRY DIALOG is not clicked")

time.sleep(2)
alertWindow = driver.switch_to.alert


wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.EditText[@resource-id = 'io.appium.android.apis:id/username_edit']"))).send_keys("Aarav Mathur")

wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.EditText[@resource-id = 'io.appium.android.apis:id/password_edit']"))).send_keys("password")
time.sleep(2)
alertWindow.accept()

time.sleep(1)

wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.Button[@text = 'OK CANCEL DIALOG WITH A MESSAGE']"))).click()
alert2 = driver.switch_to.alert

print(alert2.text)
alert2.accept()
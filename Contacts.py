import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Desired Capabilities
options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.samsung.android.app.contacts"
options.app_activity = "com.samsung.android.contacts.contactslist.PeopleActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@content-desc='Create contact']"))).click()
    print("Adding the new contact...")
except:
    print("Failed to add the new contact...")

try:
    Name = input("Please enter the name of the contact: ")
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@text='Name']"))).send_keys(Name)
    print("Adding the name of the new contact...")
except:
    print("Failed to add the name...")

# FIXED NUMBER PART
try:
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//android.widget.RelativeLayout[@resource-id='com.samsung.android.app.contacts:id/titleLayout'])[1]"))).click()
    time.sleep(2)
    Number = str(input("Please enter the number of the contact: "))
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.EditText[@text='Phone']"))).send_keys(Number)
    print("Adding the phone number...")
except:
    print("Failed to add the phone number...")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='Save']"))).click()
    print("Saved the new contact...")
except:
    print("Failed to save the new contact...")

driver.save_screenshot("Contacts.png")
driver.quit()
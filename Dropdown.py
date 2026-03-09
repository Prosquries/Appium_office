from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.samsung.android.app.contacts"
options.app_activity = "com.samsung.android.contacts.contactslist.PeopleActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Create contact"))).click()
    print("Creating the contact")
except:
    print("Failed to create the contact")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.samsung.android.app.contacts:id/nameEdit"))).send_keys("Test2005")
    print("Entering the name of the contact")
except:
    print("Failed to enter the name of the contact")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().resourceId(\"com.samsung.android.app.contacts:id/editor_content_container\").instance(1)"))).click()
    print("Clicking the Phone")
except:
    print("Failed to click the Phone")

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"Select phone number type, Mobile, Dropdown list"))).click()
    print("Clicking the dropdown menu")
except:
    print("Failed to click the dropdown menu")

# # 1. This is the simplest method of choosing the element from the drop down
# try:
#     wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Work\")"))).click()
#     print("Choosing the field")
# except:
#     print("Failed to choose the field")

# # 2. Now this is looping method of selecting the dropdowns by using for loops

options = driver.find_elements(AppiumBy.XPATH,"//android.widget.TextView[@resource-id = 'com.samsung.android.app.contacts:id/selectCheckedText']")

for opt in options:
    print(opt.text)
    if opt.text == "Other":
        opt.click()
        break


time.sleep(2)
driver.quit()


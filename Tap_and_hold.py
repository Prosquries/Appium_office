from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.samsung.android.app.contacts"
options.app_activity = "com.samsung.android.contacts.contactslist.PeopleActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

# Tap Action
# try:
#     finger = PointerInput("touch","finger")
#     actions = ActionBuilder(driver, mouse=finger)
#
#     actions.pointer_action.move_to_location(806, 2838)
#     actions.pointer_action.pointer_down()
#     actions.pointer_action.pause(0.1)
#     actions.pointer_action.pointer_up()
#     actions.perform()
#     print("Tap Operation passed")
# except:
#     print("Tap Operation failed")

# Long Press
try:
    finger = PointerInput("touch","finger")
    actions = ActionBuilder(driver,mouse = finger)

    actions.pointer_action.move_to_location(806, 2838)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(2)
    actions.pointer_action.pointer_up()
    actions.perform()
    print("Long Press Operation pass")
except:
    print("Long press Operation failed")

time.sleep(2)
driver.quit()
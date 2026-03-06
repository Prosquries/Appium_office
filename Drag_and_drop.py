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
options.app_package = "com.expandtesting.practice"
options.app_activity = "com.expandtesting.practice.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"go-to-drag-drop-screen"))).click()
    print("Clicking on drag and drop screen")
except:
    print("Failed to click on drag and drop section")

try:
    finger = PointerInput("touch", "finger")
    actions = ActionBuilder(driver, mouse=finger)

    actions.pointer_action.move_to_location(720, 507)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(1)
    actions.pointer_action.move_to_location(1005, 2441.5)
    actions.pointer_action.pointer_up()

    actions.perform()
    print("Successfully moved object/Ghost to Bin")
except:
    print("Failed to move object/Ghost to Bin")

time.sleep(2)
driver.quit()
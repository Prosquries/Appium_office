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
    wait.until(EC.presence_of_element_located((AppiumBy.XPATH,"//android.widget.Button[@text = '08 DRAG AND DROP']"))).click()
    print("Printing the Drag and drop option")
except:
    print("Unable to click on Drag and drop option")

Ghost = driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@resource-id = 'com.expandtesting.practice:id/paper']")
Bin = driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@resource-id = 'com.expandtesting.practice:id/trash']")


sx = Ghost.location['x'] + Ghost.size['width']/2
sy = Ghost.location['y'] + Ghost.size['height']/2

tx = Bin.location['x'] + Bin.size['width']/2
ty = Bin.location['y'] + Bin.size['height']/2

finger = PointerInput("touch","finger")
actions = ActionBuilder(driver, mouse = finger)

actions.pointer_action.move_to_location(sx,sy)
actions.pointer_action.pointer_down()
actions.pointer_action.pause(1)
actions.pointer_action.move_to_location(tx,ty)
actions.pointer_action.pointer_up()

actions.perform()

time.sleep(2)
driver.quit()
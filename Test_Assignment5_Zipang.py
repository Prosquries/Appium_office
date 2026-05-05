from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.udid = "192.168.1.11:34267"

options.app_package = "com.myauctions.zipang"
options.app_activity = "com.myauctions.zipang.MainActivity"


driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']"))).click()
    print("Allow pressed")

except:
    print("Allow not present")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiSelector().text("2467124122 1 ct E SI-1 ROUND Good Good Good None")'))).click()

    print("Auction product clicked")
except:
    print("Unable to press auction product")

try:
    Email = input("Enter Email Address: ")

    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Email")'))).send_keys(Email)

    print("Email entered")
except:
    print("Email field not found")

try:
    Password = input("Enter Password: ")

    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Password")'))).send_keys(Password)

    print("Password entered")
except:
    print("Password field not found")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(38)'))).click()

    print("Remember Me clicked")
except:
    print("Remember me not found")

try:
    wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.ViewGroup").instance(41)'))).click()

    print("Login clicked")
except:
    print("Login button not found")

finger = PointerInput("touch","finger")
actions = ActionBuilder(driver,mouse = finger)
time.sleep(5)
try:
    actions.pointer_action.move_to_location(956,641)
    actions.pointer_action.pointer_down()
    actions.pointer_action.move_to_location(64,641)
    actions.pointer_action.pointer_up()
    actions.perform()
    print("Horizontal Scroll")
except:
    print("Horizontal scroll failed")

time.sleep(5)
driver.back()
time.sleep(5)
try:
    wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(1)'))).click()
    print("Opening the image")
except:
    print("Opening the image failed")
time.sleep(2)
try:
    from selenium.webdriver.common.actions.action_builder import ActionBuilder
    from selenium.webdriver.common.actions.pointer_input import PointerInput
    from selenium.webdriver.common.actions import interaction

    actions = ActionBuilder(driver)

    finger1 = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger1")
    finger2 = actions.add_pointer_input(interaction.POINTER_TOUCH, "finger2")

    # finger 1
    finger1.create_pointer_move(duration=0, x=540, y=900)
    finger1.create_pointer_down()
    finger1.create_pointer_move(duration=300, x=540, y=400)
    finger1.create_pointer_up(0)

    # finger 2
    finger2.create_pointer_move(duration=0, x=540, y=1050)
    finger2.create_pointer_down()
    finger2.create_pointer_move(duration=300, x=540, y=1600)
    finger2.create_pointer_up(0)

    actions.perform()

    actions.perform()
    print("Zoom in performed")

except Exception as e:
    print("Zoom error:", e)
time.sleep(2)
try:
    driver.find_element(AppiumBy.CLASS_NAME, "android.widget.TextView").click()
    print("Closing the image view")
except:
    print("Closing the image view failed")

# Long press

finger = PointerInput("touch","finger")
actions = ActionBuilder(driver,mouse = finger)
try:
    actions.pointer_action.move_to_location(666, 854)
    actions.pointer_action.pointer_down(2)
    actions.pointer_action.pause(3)
    actions.pointer_action.pointer_up()
    actions.perform()
    print("Performed long-press")
except:
    print("Longpress failed")

time.sleep(2)
driver.quit()



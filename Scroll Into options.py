from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
import time


options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.android.settings"
options.app_activity = ".Settings"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

# # Scroll option with scrollIntoView for specific text or any attributes
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Advanced features"));')
#
# time.sleep(1)
# try:
#     driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Advanced features")').click()
#     print("The Advance feature is clicked")
# except:
#     print("The Element is not clickable")
#
# driver.quit()

# # Scroll the element Vertical Scroll up and down

# device_size = driver.get_window_size()
# print(device_size)
#
# Screen_Width = device_size["width"]
# Screen_Height = device_size["height"]
#
# print(Screen_Width)
# print(Screen_Height)
#
# Start_X = Screen_Width/2
# end_X = Screen_Width/2
# Start_Y = Screen_Height*8/9
# end_Y = Screen_Height/9
# # Down operations
# finger = PointerInput("touch", "finger")
# actions = ActionBuilder(driver, mouse=finger)
#
# actions.pointer_action.move_to_location(int(Start_X), int(Start_Y))
# actions.pointer_action.pointer_down()
#
# actions.pointer_action.move_to_location(int(end_X), int(end_Y))
#
# actions.pointer_action.release()
# actions.perform()
# time.sleep(2)
#
# # Up operations
# finger = PointerInput("touch", "finger")
# actions = ActionBuilder(driver, mouse=finger)
#
# actions.pointer_action.move_to_location(int(end_X), int(end_Y))
# actions.pointer_action.pointer_down()
#
# actions.pointer_action.move_to_location(int(Start_X), int(Start_Y))
#
# actions.pointer_action.release()
# actions.perform()
#
#
# driver.quit()

# # Another method for Scrolling vertically - This tries to scroll 5 times until the end not reached so multiple scrolls might be possible

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')
# time.sleep(2)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')
# driver.quit()

# # Another method to scroll vertically - This method is to scroll down to up in single scroll but they might not reach at the end

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollForward(2)')
# time.sleep(2)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollBackward(2)')
# time.sleep(1)
# driver.quit()



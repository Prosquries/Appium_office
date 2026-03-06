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
options.app_package = "com.sec.android.app.music"
options.app_activity = "com.sec.android.app.music.common.activity.MusicMainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)


try:
    driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button").click()
    print("Pressing the continue1")
except:
    print("Press the continue1 failed")

try:
    driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button").click()
    print("Pressing the continue2")
except:
    print("Press the continue2 failed")
try:
    driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
    print("Pressing the Allow1")
except:
    print("Press the Allow1 failed")

try:
    driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
    print("Pressing the Allow2")
except:
    print("Press the Allow2 failed")

try:
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text = 'Favourites']").click()
    print("Pressing the Favourites section")
except:
    print("Failed to tap on Favourites section")

try:
    song = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().resourceId("com.sec.android.app.music:id/recommend_container")).setAsHorizontalList().scrollForward().scrollIntoView(new UiSelector().text("Shararat"))')
    print("Shararat song found")
    song.click()

except:
    print("Failed to find the song")


time.sleep(3)
driver.quit()

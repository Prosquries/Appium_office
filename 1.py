from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Desired capabilities

options = UiAutomator2Options()

options.platform_name="Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "Uiautomator2"
options.app_package = "com.android.settings"
options.app_activity = ".Settings"

# Connect to appium server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(3)
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.android.settings:id/recycler_view']/android.widget.LinearLayout[2]"))).click()

time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH,"//androidx.recyclerview.widget.RecyclerView[@resource-id='com.android.settings:id/recycler_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout"))).click()
print("Opened WiFi successfully!")
driver.quit()


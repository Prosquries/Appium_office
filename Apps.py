from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(3)

# Find all app names on home screen
apps = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")

app_names = []

for app in apps:
    name = app.text
    if name != "":
        app_names.append(name)

print("\nApps on Home Screen:")
for a in app_names:
    print(a)

driver.quit()
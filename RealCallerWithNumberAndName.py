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

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.samsung.android.app.contacts:id/search_src_text")
el2.send_keys("1234567890")


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

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"WhatsApp\")"))).click()

el = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.whatsapp:id/conversations_row_contact_name' and @text='+91 98870 45678 (You)']")))
print(el.text)
el.click()

wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"https://simple-books-api.glitch.me/api-clients/"))).click()
time.sleep(2)
print(driver.context)
print(driver.contexts)
time.sleep(2)
driver.back()

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------------------
# Desired Capabilities
# ---------------------------
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"
options.app_package = "com.myauctions.zipang"
options.app_activity = ".MainActivity"


# Start Driver

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)
time.sleep(3)
try:
    allow_btn = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@text='Allow']")))
    allow_btn.click()
    print("Permission allowed")

except:
    print("No permission popup appeared")
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.XPATH,"(//android.widget.TextView[@text='Set Pre-Bid'])[1]"))).click()

wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.EditText[@text='Email']"))).send_keys("jagadeesh.yadav@sysquare.in")

wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.EditText[@text='Password']"))).send_keys("password")
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.ImageView"))).click()
time.sleep(3)
print("Logged in Successfully")
time.sleep(2)

# Pressing the NR button

wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text='NR']"))).click()
time.sleep(5)
wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text='NR']"))).click()
print("NR functions are working correctly")

# Pressing the sorting button
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH,"//android.view.ViewGroup[@content-desc='# Search, '""]/android.view.ViewGroup"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.EditText[@text='Search']"))).send_keys("1")
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='Search']"))).click()
time.sleep(5)
print("Searching is also perfect")

# input("Press any key to exit...")
driver.quit()


import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
#
#
# # @pytest.fixture()
# # def Setup():
# #     # global appium_service
# #     appium_service = AppiumService()
# #     appium_service.start()
# #
# #     global driver
# #
# #     options = UiAutomator2Options()
# #
# #     options.platform_name = "Android"
# #     options.device_name = "RZCY1212F1W"
# #     options.automation_name = "UiAutomator2"
# #     options.app_package = "com.android.settings"
# #     options.app_activity = ".Settings"
# #
# #     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# #     yield
# #
# #     time.sleep(2)
# #     allure.attach(driver.get_screenshot_as_png(), name="Alert SS", attachment_type=AttachmentType.PNG)
# #     driver.quit()
#
#
#
# # This conftest file is fro parallel mobile testing
#
@pytest.fixture(params=["device1", "device2"], scope="function")

def appium_driver(request):
    global driver
    if request.param == "device1":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "192.168.1.11:36895"
        # options.app_package = "com.samsung.android.dialer"
        # options.app_activity = "com.samsung.android.dialer.DialtactsActivity"
        options.app_package = "com.myauctions.zipang"
        options.app_activity = "com.myauctions.zipang.MainActivity"
        options.system_port = 8201

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    elif request.param == "device2":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "192.168.1.8:46841"
        # options.app_package = "com.samsung.android.dialer"
        # options.app_activity = "com.samsung.android.dialer.DialtactsActivity"
        options.app_package = "com.myauctions.zipang"
        options.app_activity = "com.myauctions.zipang.MainActivity"
        options.system_port = 8202

        driver = webdriver.Remote("http://127.0.0.1:4724", options=options)

    yield driver
    driver.quit()
#

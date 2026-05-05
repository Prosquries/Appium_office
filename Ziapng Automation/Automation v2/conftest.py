import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from ZipangAutoV2 import ZiapngAutoV2_Workflow


@pytest.fixture(scope="function")
def driver(request):
    options = UiAutomator2Options()
    options.device_name = "RZCY1212F1W"
    options.automation_name = "uiautomator2"
    options.platform_name = "Android"
    options.app_package = "com.myauctions.zipang"
    options.app_activity = "com.myauctions.zipang.MainActivity"

    driver = webdriver.Remote("http://localhost:4723", options=options)

    if "login" not in request.keywords:
        app = ZiapngAutoV2_Workflow(driver)
        app.allow_Permission()
        app.Open_LoginPage()
        app.Login("jagadeesh.yadav@sysquare.in", "password")

    yield driver
    driver.quit()


# -------- Optional wait fixture --------
@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 15)
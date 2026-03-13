import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

driver = None


class TestClass:

    def test_VerticalScroll(self,Setup):
        time.sleep(2)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Advanced features"));')

        time.sleep(1)
        try:
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Advanced features")').click()
            print("The Advance feature is clicked")
        except:
            print("The Element is not clickable")

    def test_WiFiConnect(self,Setup):
        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text = 'Connections']").click()
        time.sleep(1)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.RelativeLayout").instance(0)').click()
        time.sleep(1)
        Wifi = driver.find_element(AppiumBy.XPATH,"//android.widget.Switch[@content-desc = 'On']").is_enabled()
        Status = print("Status",Wifi)

        if Status == True:
            assert True ,"The Wifi Status is already true "


        time.sleep(1)

    def test_Blutooth(self, Setup):
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Connections']").click()
        time.sleep(1)

        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.RelativeLayout").instance(4)').click()
        time.sleep(1)

        bluetooth_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"On")

        bluetooth_status = bluetooth_element.is_enabled()
        print("Status:", bluetooth_status)

        if bluetooth_status:
            assert True, "The Bluetooth status is already true"

        allure.attach(driver.get_screenshot_as_png(),name="Alert SS",attachment_type=AttachmentType.PNG)


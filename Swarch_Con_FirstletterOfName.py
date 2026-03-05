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
options.app_package = "com.samsung.android.app.contacts"
options.app_activity = "com.samsung.android.contacts.contactslist.PeopleActivity"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 10)

time.sleep(2)
print("\n Choose Options below:")
print("1. Call")
print("2. Message")
print("3. Details")
print("4. Create new Contact")

choice = input("Enter the choice with number:")


match choice:
    case "3":
        try:
            Name = str(input("Enter the name of the contact"))
            print("Searching the contact ...")
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{Name}"))')
            print("Contact found")
        except:
            print("Contact not found !")

        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,Name))).click()
            print("Selecting the contact")
        except:
            print("Selected Contact not found !")

        time.sleep(1)
        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Details")'))).click()
            print("Details of the contact")
        except:
            print("Failed to get the details of the contact")

    case "2":
        try:
            Name = str(input("Enter the name of the contact"))
            print("Searching the contact ...")
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{Name}"))')
            print("Contact found")
        except:
            print("Contact not found !")

        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, Name))).click()
            print("Selecting the contact")
        except:
            print("Selected Contact not found !")
        time.sleep(1)

        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Message")'))).click()
            print("Message clicked")
        except:
            print("Message not found !")

        try:
            Meassage = str(input("Enter the message"))
            el7 = driver.find_element(AppiumBy.ID,"com.samsung.android.messaging:id/message_edit_text")
            el7.click()
            el7.send_keys(Meassage)
            print("Message entered")
        except:
            print("Message cannot be sent !")



    case "1":
        try:
            Name = str(input("Enter the name of the contact"))
            print("Searching the contact ...")
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{Name}"))')
            print("Contact found")
        except:
            print("Contact not found !")

        time.sleep(1)
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, Name))).click()
            print("Selecting the contact")
        except:
            print("Selected Contact not found !")

        try:
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Call")'))).click()
            print("Calling the contact")
        except:
            print("Failed to call the contact")

        try:
            input("Press enter to end the call")
            wait.until(EC.element_to_be_clickable(
                (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc = 'End call']"))).click()
            print("Call is ended")

        except:
            print("Unable to call")

    case "4":
        try:
            wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Create contact']"))).click()
            print("Adding the new contact...")
        except:
            print("Failed to add the new contact...")

        try:
            Name = input("Please enter the name of the contact: ")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@text='Name']"))).send_keys(Name)
            print("Adding the name of the new contact...")
        except:
            print("Failed to add the name...")

            # FIXED NUMBER PART
        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
                                                   "(//android.widget.RelativeLayout[@resource-id='com.samsung.android.app.contacts:id/titleLayout'])[1]"))).click()
            time.sleep(2)
            Number = str(input("Please enter the number of the contact: "))
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='Phone']"))).send_keys(
                Number)
            print("Adding the phone number...")
        except:
            print("Failed to add the phone number...")

        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.Button[@text='Save']"))).click()
            print("Saved the new contact...")
        except:
            print("Failed to save the new contact...")


if choice <= "5":
    print("Please enter valid option next time")


time.sleep(3)

driver.quit()
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------- DEVICE SETUP ----------------

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "RZCY1212F1W"
options.automation_name = "UiAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

wait = WebDriverWait(driver, 15)

# ---------------- USER MENU ----------------

print("\nChoose options below :-")
print("1. Write the note by editing the existing one")
print("2. Create a new file")

choice = input("Enter your choice: ")

# ---------------- LOGIC ----------------

match choice:

    # ---------- EDIT EXISTING NOTE ----------
    case "1":

        try:
            obsidian = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Obsidian']")
                )
            )
            obsidian.click()

            print("Opening Obsidian application")

        except:
            print("Cannot find Obsidian on home screen")

        try:
            Heading = input("Enter the Heading of the Obsidian note: ")

            title = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, "android.widget.EditText")
                )
            )

            title.click()
            title.clear()
            title.send_keys(Heading)

            print("Heading entered")

        except:
            print("Unable to enter heading")

        try:
            Content = input("Enter the Content of the Obsidian note: ")

            editor = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, "android.widget.EditText")
                )
            )

            editor.send_keys(Content)

            print("Content entered")

        except:
            print("Unable to enter content")

    # ---------- CREATE NEW NOTE ----------
    case "2":

        try:
            obsidian = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Obsidian']")
                )
            )

            obsidian.click()

            print("Opening Obsidian application")

        except:
            print("Cannot find Obsidian")

        try:
            expand = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, "Expand")
                )
            )

            expand.click()

            print("Opening file menu")

        except:
            print("Cannot open menu")

        try:
            new_file = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, "android.widget.ImageView")
                )
            )

            new_file.click()

            print("Creating new file")

        except:
            print("Cannot create new file")

        try:
            Heading1 = input("Enter the Heading of the Obsidian note: ")

            heading_box = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, "android.widget.EditText")
                )
            )

            heading_box.send_keys(Heading1)

            print("Heading added")

        except:
            print("Unable to enter heading")

        try:
            Content1 = input("Enter the Content of the Obsidian note: ")

            editor = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.CLASS_NAME, "android.widget.EditText")
                )
            )

            editor.send_keys(Content1)

            print("Content added")

        except:
            print("Unable to enter content")

    # ---------- INVALID INPUT ----------
    case _:
        print("Invalid choice. Please run the script again.")


# Need to fix this bull shit script
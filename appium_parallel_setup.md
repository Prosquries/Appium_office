# Parallel Mobile Testing Setup (Appium + Pytest + Multiple Devices)

This guide explains how to run **parallel mobile automation tests on
multiple Android devices** using: - Appium 2 - Pytest - pytest-xdist -
UiAutomator2 - Wireless debugging (ADB)

------------------------------------------------------------------------

# 1. Install Required Tools

## Install Node.js

Download and install Node.js from: https://nodejs.org

Verify installation:

    node -v
    npm -v

------------------------------------------------------------------------

## Install Appium 2

    npm install -g appium

Verify:

    appium -v

------------------------------------------------------------------------

## Install UiAutomator2 Driver

Appium 2 requires drivers to be installed manually.

    appium driver install uiautomator2

Verify:

    appium driver list --installed

------------------------------------------------------------------------

# 2. Install Python Dependencies

Install required Python packages:

    pip install pytest
    pip install pytest-xdist
    pip install Appium-Python-Client
    pip install selenium

------------------------------------------------------------------------

# 3. Enable Developer Options on Phones

On each phone:

1.  Open **Settings**
2.  Go to **About Phone**
3.  Tap **Build Number 5 times**
4.  Developer Options will be enabled

------------------------------------------------------------------------

# 4. Enable Wireless Debugging

On each device:

1.  Open **Developer Options**
2.  Enable **Wireless Debugging**
3.  Note the **IP Address and Port**

Example:

    192.168.1.3:38571
    192.168.1.15:44593

------------------------------------------------------------------------

# 5. Connect Devices Using ADB

Run:

    adb connect 192.168.1.3:38571
    adb connect 192.168.1.15:44593

Verify devices:

    adb devices

Example output:

    192.168.1.3:38571    device
    192.168.1.15:44593   device

------------------------------------------------------------------------

# 6. Start Multiple Appium Servers

Each device should use a **different Appium port**.

Terminal 1:

    appium -p 4723

Terminal 2:

    appium -p 4724

------------------------------------------------------------------------

# 7. Configure Pytest Fixture (conftest.py)

Example:

``` python
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(params=["device1","device2"], scope="function")
def appium_driver(request):

    if request.param == "device1":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "192.168.1.3:38571"
        options.system_port = 8201
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    elif request.param == "device2":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "192.168.1.15:44593"
        options.system_port = 8202
        driver = webdriver.Remote("http://127.0.0.1:4724", options=options)

    yield driver
    driver.quit()
```

------------------------------------------------------------------------

# 8. Write Test File

Example:

``` python
def test_parallel(appium_driver):
    print(appium_driver.current_activity)
```

------------------------------------------------------------------------

# 9. Run Parallel Tests

Execute:

    pytest -v -n=2 test_parallel.py

Explanation:

  Option             Meaning
  ------------------ --------------------------
  -v                 verbose output
  -n=2               run two parallel workers
  test_parallel.py   test file

------------------------------------------------------------------------

# 10. Execution Flow

    pytest worker 1 → Appium (4723) → Device 1
    pytest worker 2 → Appium (4724) → Device 2

Both devices execute the test **simultaneously**.

------------------------------------------------------------------------

# Best Practices

-   Avoid `input()` in tests
-   Use dynamic test data
-   Assign different `systemPort` for each device
-   Ensure devices stay on same WiFi network
-   Always verify devices using `adb devices`

------------------------------------------------------------------------

# Useful Commands

Check connected devices:

    adb devices

Check current activity:

    adb shell dumpsys window | findstr mCurrentFocus

------------------------------------------------------------------------

# Result

You now have **parallel mobile automation running across multiple
devices using Appium and Pytest**.

## Adtional

If you want to connection across multiple devices using cable then u can do that by attaching cable inside phone and allow usb debugging in Developer options
and then search your device by command -

`adb devices`

You will get the real name of the device such as `RZCY1212F1W`

After this process make changes in `config.py` file like this -

``` python
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(params=["device1","device2"], scope="function")
def appium_driver(request):

    if request.param == "device1":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "RZCY1212F1W"
        options.system_port = 8201
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    elif request.param == "device2":
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = "RZCY1212F1W"
        options.system_port = 8202
        driver = webdriver.Remote("http://127.0.0.1:4724", options=options)

    yield driver
    driver.quit()
```

And then you are ready to go with wired testing which is more stable than the wireless testing 
but this is only for multiple device you can use wireless testing on a single device.

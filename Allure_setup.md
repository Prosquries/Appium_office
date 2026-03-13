# Commands to Setup Allure Report

## 1. Install Scoop (Package Manager for Windows)

`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex`


## 2. Install Allure

`scoop install allure`

-------- 


## 3. If Allure Installation Fails

`scoop update`
`scoop update allure`


## 4. Verify Allure Installation

`allure --version`

-----
## Running Allure with Pytest

# Run pytest and generate Allure results:

`pytest -v -s --alluredir=allureReport`

--------
# After the tests run, multiple files will be created inside the allureReport folder.


## Generate and View the Report

`allure serve allureReport`

## Take screenshot after completion of the tests 

`allure.attach(driver.get_screenshot_as_png(),name="Alert SS",attachment_type=AttachmentType.PNG)`
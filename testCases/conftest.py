import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        print("Launching chrome browser.................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser ...................")
    else:
        driver =webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
        print("Launching Edge browser ...................")

    return driver


def pytest_addoption(parser): #gets the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #returns browser value to setup method
    return request.config.getoption("--browser")


################ Pytest HTML Reports ###############

def pytest_configure(config): #It is hook for adding environment info to HTML reports
    config._metadata["Project Name"] = 'nop commerce'
    config._metadata["Module"] = 'Customers'
    config._metadata["Tester Name"]  = 'Prashanti'

#It is hook for delete/modify Environment info to HTML reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)


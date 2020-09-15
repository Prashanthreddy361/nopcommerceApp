from selenium import webdriver
import  pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
       driver=webdriver.Chrome(executable_path="C:\\Users\\Prashanth Reddy E\\Downloads\\chromedriver_win32\\chromedriver.exe")
       print("...........Launching chrome browser....................")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path="C:\\Users\\Prashanth Reddy E\\Downloads\\geckodriver-v0.23.0-win64\\geckodriver.exe")
        print("...........Launching Firefox browser....................")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## PyTest HTML Report ####################

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Prashanth Reddy'


#It is hook for delete/Modify Environment info to HTML report##

@pytest.mark.optionalhook
def pytest_metdata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
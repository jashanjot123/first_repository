import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture()
def setup(browser):
     if browser=='chrome':
         driver=webdriver.Chrome()
         driver.get("https://demo.guru99.com/test/newtours/register.php/")
         driver.implicitly_wait(5)
         driver.maximize_window()
         return driver
     elif browser=='edge':
           if browser == 'edge':
               driver = webdriver.Chrome()
               driver.get("https://demo.guru99.com/test/newtours/register.php")
               driver.implicitly_wait(5)
               driver.maximize_window()
               return driver

     elif browser=='firefox':
           if browser == 'firefox':
               driver = webdriver.Chrome()
               driver.get("https://demo.guru99.com/test/newtours/register.php")
               driver.implicitly_wait(5)
               driver.maximize_window()
               return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home",None)
#     metadata.pop("Plugins",None)


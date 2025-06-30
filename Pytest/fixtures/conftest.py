import pytest

@pytest.fixture()
def setup():
    print("Launching browser...")
    yield
    print("Closing browser...")

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
         def setup(browser):
           if browser == 'edge':
               driver = webdriver.Chrome()
               driver.get("https://demo.guru99.com/test/newtours/register.php")
               driver.implicitly_wait(5)
               driver.maximize_window()
               return driver

     elif browser=='firefox':
         def setup(browser):
           if browser == 'firefox':
               driver = webdriver.Chrome()
               driver.get("https://demo.guru99.com/test/newtours/register.php")
               driver.implicitly_wait(5)
               driver.maximize_window()
               return driver

def pytest_adoption(parser):
    parser.adoption("--browser")

@pytest.fixture()
def browser(request):
    return request.conftest.getoption("--browser")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome()
time.sleep(5)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
a=driver.find_elements(By.PARTIAL_LINK_TEXT,"Congratulations")




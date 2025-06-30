import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(1)
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element(By.XPATH,//input[@name="btnK"])
# *[@target="_top"]

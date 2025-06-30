import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
e=driver.find_elements(By.XPATH,"//*[contains(text() , 'Sonata Software')]/parent::*")
print(len(e))
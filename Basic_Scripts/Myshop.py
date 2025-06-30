import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(1)
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(1)
driver.find_element(By.NAME,"search_query").send_keys("tops")
time.sleep(1)
driver.find_element(By.NAME,'').click()
time.sleep(10)
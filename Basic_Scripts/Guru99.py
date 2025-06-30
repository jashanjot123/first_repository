import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(1)
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(1)
driver.find_element(By.NAME,"userName").send_keys("mercury")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("mercury")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input').click()
time.sleep(10)
#
actual_title=driver.title
expected_title="Login: Mercury Tours"
if actual_title==expected_title:
    print("test passed")
else:
    print("test failed")
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
time.sleep(4)
driver.get("https://www.google.co.in/")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("selenium")
time.sleep(2)
a=driver.find_elements(By.XPATH,"//*[@class='G43f7e']/li")
print(len(a))
for i in a:
    if i.text=="selenium":
        i.click()
        break
time.sleep(4)        
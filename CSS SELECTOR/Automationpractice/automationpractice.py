import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
time.sleep(4)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
dropdown=Select(driver.find_element(By.XPATH,"//*[contains(@id,'country')]"))
time.sleep(1)

#select by text
# dropdown.select_by_visible_text("India")
# time.sleep(1)

#select by value
# dropdown.select_by_value("india")
# time.sleep(5)

#select by index
# dropdown.select_by_index(1)
# time.sleep(2)

a=driver.find_elements(By.XPATH,"//*[contains(@id,'country')]/option")
print(len(a))
time.sleep(4)
for i in a:
    print(i.text)
     
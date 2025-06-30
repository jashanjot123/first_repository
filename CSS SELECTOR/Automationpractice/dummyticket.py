# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import select
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# time.sleep(4)
# driver.maximize_window()
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# time.sleep(2)
# driver.find_element(By.XPATH,"//*[@id='select2-reasondummy-container']").click()
# time.sleep(2)
# a=driver.find_elements(By.XPATH,'//*[@class="select2-results__options"]/li')
# print(len(a))
# time.sleep(2)
# for i in a:
#     print(i.text)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
time.sleep(3)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Jashan")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("jashanjot0943@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9356433005")
time.sleep(3)
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("abc Rajpura")
time.sleep(4)
male=driver.find_element(By.XPATH,"//input[@id='male']")
male.click()
time.sleep(3)
female=driver.find_element(By.XPATH,"//input[@id='female']")
time.sleep(3)

#doubt
# da=driver.find_elements(By.XPATH,"//*[@class='form-check form-check-inline']/input[@type='checkbox']")
# print(len(days))
# time.sleep(3)
# for i in da:
#     if i.get_attribute("tuesday")=="tuesday":
#     # if da[3].text=="wednesday":
#         i.click()
#         print("executed")
#         time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='wednesday']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//select[@id='country']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//*[contains(@id,'country')]/option[6]").click()
time.sleep(3)

driver.find_element(By.XPATH,"//*[contains(@id,'colors')]/option[6]").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[contains(@id,'animals')]/option[3]").click()
time.sleep(4)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame(0)
# driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("2/1/2003")
# time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()
time.sleep(2)
year='2024'
month='September'
date='21'
while True:
    mon=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    yea=driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    if mon==month and yea==year:
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]/span').click()


da=driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td')
for i in da:
    if date==i.text:
        i.click()
        time.sleep(10)




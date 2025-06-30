import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()
time.sleep(2)
# a=driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]').text
# winid=driver.current_window_handle
# print("the window id is",winid)
# the window id is E90C2E5ECC6747E342700B0A2519AA06
winid=driver.window_handles
print("the window ids are",winid)
parentid=winid[0]
childid=winid[1]
driver.switch_to.window(childid)
a=driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]').text
print(a)
driver.switch_to.window(parentid)
b=driver.title
print(b)

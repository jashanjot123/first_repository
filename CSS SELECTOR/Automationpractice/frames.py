import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
time.sleep(2)
driver.switch_to.frame("frm1")
time.sleep(3)
a=driver.find_element(By.LINK_TEXT,"HOME")
print(a.text)
time.sleep(2)
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame("frm2")
driver.find_element(By.ID,"firstName").send_keys("arjun")
time.sleep(5)


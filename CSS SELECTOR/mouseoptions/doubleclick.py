import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
time.sleep(2)
driver.switch_to.frame("iframeResult")
time.sleep(2)
a=driver.find_element(By.XPATH,'//*[@id="field1"]')
a.clear()
a.send_keys("selenium")
time.sleep(2)
act=ActionChains(driver)
button=driver.find_element(By.XPATH,'/html/body/button')
act.double_click(button).perform()
time.sleep(5)
c=driver.find_element(By.XPATH,'//*[@id="field2"]')
if a.get_attribute("value")==c.get_attribute("value"):
    print("Bhangre pao")
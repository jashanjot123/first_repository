import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
time.sleep(2)
button=driver.find_element(By.CSS_SELECTOR,'body > div > section > div > div > div > p > span')
time.sleep(2)
copy=driver.find_element(By.XPATH,"//*[@class='context-menu-item context-menu-icon context-menu-icon-copy']")
time.sleep(2)
act=ActionChains(driver)

act.context_click(button).perform()

copy.click()
time.sleep(5)
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
time.sleep(2)
min=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print("Before sliding")
print("Location of min slider is",min.location)
print("Location of max slider is",max.location)
act=ActionChains(driver)
act.drag_and_drop_by_offset(min,121,0).perform()
time.sleep(1)
act.drag_and_drop_by_offset(max,-40,0).perform()
time.sleep(2)
print("After sliding")
print("Location of min slider is",min.location)
print("Location of max slider is",max.location)

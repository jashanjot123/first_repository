import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(2)
rome=driver.find_element(By.XPATH,'//*[@id="box6"]')
italy=driver.find_element(By.XPATH,'//*[@id="box106"]')
act=ActionChains(driver)
act.drag_and_drop(rome,italy).perform()
time.sleep(5)
assert "box6" in italy.get_attribute("innerHTML"),"Rome doesnt drop in italy"
print("Bhangre Pao")

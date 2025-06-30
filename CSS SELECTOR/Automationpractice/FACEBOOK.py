import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#tag and id
driver=webdriver.Chrome()
time.sleep(1)
driver.get("https://www.facebook.com/")
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Jashan")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("123")
# time.sleep(3)

#tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("JAshan")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("45545")
time.sleep(1)
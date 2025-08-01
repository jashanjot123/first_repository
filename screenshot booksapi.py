import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://parabank.parasoft.com/parabank/openaccount.htm")
driver.find_element(By.XPATH,'//input[@class="input" and @name="username"]').send_keys("jashanjot")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@class="input" and @name="password"]').send_keys("itzjashan@123")
time.sleep(2)
driver.find_element(By.XPATH,'//input[@class="button" and @type="submit"]').click()
time.sleep(2)
driver.save_screenshot(r"C:\Users\HP\OneDrive\Pictures+\Screenshot.png")
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class,"title")]')))
    print("Login Successful")
except:
    print("Login Failed")
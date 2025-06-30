import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(1)
driver.get("http://www.automationpractice.pl/index.php")
time.sleep(1)
b=driver.find_elements(By.TAG_NAME,"img")
print("Total no of images are:",len(b))
a=driver.find_elements(By.TAG_NAME,"a")
print("Total no of links are:",len(a))
e=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print("Total no of imgs are:",len(e))
c=driver.find_elements(By.CLASS_NAME,"htmlcontent_home")
print("Total images:",len(c))

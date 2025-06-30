import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Chrome()
time.sleep(1)
driver.get("https://automationbookstore.dev/")
book2=driver.find_element(By.XPATH,"//*[contains(@id,'pid2_thumb')]")
bookname=driver.find_element(locate_with(By.TAG_NAME,"li").to_right_of(book2)).text
print(bookname)
book3=driver.find_element(locate_with(By.TAG_NAME,"li").to_left_of(book2)).text
print(book3)
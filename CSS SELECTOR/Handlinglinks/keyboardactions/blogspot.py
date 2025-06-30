import time
from tkinter.constants import BROWSE

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#count all the number of rows and columns
a=driver.find_elements(By.XPATH,'//*[@name="BookTable"]/tbody/tr')
print("Total number of rows",len(a))
time.sleep(3)
b=driver.find_elements(By.XPATH,'//*[@name="BookTable"]/tbody/tr/th')
print("Total number of columns",len(b))

#read the specific data in the table
d=driver.find_element(By.XPATH,'//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[2]')
print(d.text)

#Read all the rows and column
for r in range(2,len(a)+1):
    for c in range(2,len(b)+1):
        print(driver.find_element(By.XPATH,f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{r}]/td[{c}]').text)

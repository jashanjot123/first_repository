import requests as request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)
count=0
alllink=driver.find_elements(By.TAG_NAME,"a")
print(len(alllink))
for link in alllink:
    url=link.get_attribute("href")
    try:
        res=request.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," is broken link")
        count=count+1
    else:
        print(url," is valid link")

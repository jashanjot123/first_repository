import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

location=os.getcwd()
def chrome_setup():
    preferences={"download.default_directory":location}
    ops=webdriver.ChromeOptions()

    ops.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(options=ops)
    return driver
driver=chrome_setup()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="content"]/div/a[1]').click()
time.sleep(3)
for _ in range(15):
    if os.path.exists(location):
        print("File downloaded successfully",location)
        break
    time.sleep(2)
else:
    print("File doesnt exist")
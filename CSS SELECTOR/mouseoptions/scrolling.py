import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.get("https://www.orangehrm.com/")
time.sleep(5)

#1 scroll the page by pixel
# driver.execute_script("window.scrollBy(0,1500)")
# time.sleep(5)

#2 scroll by the element is visible
# logo=driver.find_element(By.XPATH,'/html/body/div/div/div/div/section[2]/div[4]/div/div[2]/div/ul/li[2]/div/a/div[1]/img')
# time.sleep(2)
# driver.execute_script("arguments[0].scrollIntoView();",logo)
# time.sleep(5)

#3 Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
value=driver.execute_script("return window.pageYOffset;")
time.sleep(5)
print("Number of pixels moved:",value)
time.sleep(5)



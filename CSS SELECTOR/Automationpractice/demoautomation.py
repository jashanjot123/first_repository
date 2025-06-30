import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
time.sleep(4)
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(2)
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("Jashanjot")
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys("Singh")
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys("jashanjot0943@gmail.com")
# time.sleep(1)
# # driver.find_element(By.XPATH,'//*[@id="genterWrapper"]/div[2]/div[1]').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="userNumber"]').send_keys("9356433005")
# time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="dateOfBirthInput"]').click()
time.sleep(2)
monyea = driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]').text
monthyear='February 2024'
date='1'
while True:
    monyea=driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select').text
    yeamon=driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select').text

    if monyea==monthyear and yeamon==monthyear :
        break
    else:
        driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/button[1]').click()
time.sleep(5)

da=driver.find_elements(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]')
for i in da:
    if date==i.text:
        i.click()
time.sleep(10)

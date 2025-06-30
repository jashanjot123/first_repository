import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# # open browser
# driver=webdriver.Chrome()
# time.sleep(5)
#
# # pass url to browser "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(6)
#
# # enter username
# driver.find_element(By.NAME,"username").send_keys("Admin")
# time.sleep(5)
#
# # enter password
# driver.find_element(By.NAME,"password").send_keys("admin123")
# time.sleep(5)
#
# # click on login
# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# time.sleep(5)
#
# # validation
#
# actual_title=driver.title
# expected_title="OrangeHRM"
# if actual_title==expected_title:
#     print("Test case passed")
# else:
#     print("Test Failed")

driver=webdriver.Chrome()
time.sleep(1)
driver.get("https://demo.guru99.com/test/newtours/")
time.sleep(1)
driver.find_element(By.NAME,"userName").send_keys("mercury")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("mercury")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input').click()
time.sleep(10)
#
actual_title=driver.title
expected_title="Login: Mercury Tours"
if actual_title==expected_title:
    print("test passed")
else:
    print("test failed")




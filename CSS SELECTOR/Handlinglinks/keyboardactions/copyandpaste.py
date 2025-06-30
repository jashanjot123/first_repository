# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common import keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.implicitly_wait(2)
# time.sleep(1)
# driver.get("https://text-compare.com/")
# driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("selenium")
# time.sleep(2)
# act=ActionChains(driver)
# #input1==ctrl+A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
# time.sleep(4)
#
#
# # input@===CTRL+C
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()
# time.sleep(4)
#
# act.send_keys(Keys.TAB).perform()
# time.sleep(2)
#
#
# act.key_down(Keys.CONTROL)
# act.send_keys("v")
# act.key_up(Keys.CONTROL)
# act.perform()
# time.sleep(4)
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
time.sleep(1)
driver.get("https://text-compare.com/")
driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("selenium")
time.sleep(2)
act=ActionChains(driver)
#input1==ctrl+A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(4)


# input@===CTRL+C
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(4)

act.send_keys(Keys.TAB).perform()
time.sleep(2)


act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="compareButton"]').click()
time.sleep(2)

a=driver.find_element(By.XPATH,'/html/body/div[2]/span')
print(a.text)
time.sleep(5)
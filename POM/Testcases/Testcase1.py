import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from POM.Pageobject.pageobject import loginpage


class testcase:
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
    lp=loginpage(driver)
    lp.setUserName('12jass2345@gmail.com')
    lp.setUserPasswd('1234567jass')
    lp.clickLogin()
    time.sleep(10)
    act_result=driver.find_element(By.XPATH,'//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span').text
    exp_result="Jashan jot"
    assert act_result==exp_result,"test failed"
    print("Bhangre Pao")
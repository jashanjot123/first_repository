import time
from multiprocessing.util import get_logger

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from POM.Logging.logger  import get_logger


logger =get_logger()
class Test_registration:
    def test_registration(self,setup):
        try:
            logger.info("Launching browser...")
            driver=setup
            driver.maximize_window()
            logger.info("Navigating to registration page...")

            logger.debug("Filling contact information...")
            driver.find_element(By.NAME,'firstName').send_keys("jashan")
            driver.find_element(By.NAME,'lastName').send_keys("jot")
            driver.find_element(By.NAME,'phone').send_keys("12345678")
            driver.find_element(By.NAME, 'userName').send_keys("jashan123")

            logger.debug("Filling the email information ")
            driver.find_element(By.NAME,'address1').send_keys("110panchkula")
            driver.find_element(By.NAME,'city').send_keys("Chandigarh")
            driver.find_element(By.NAME,'state').send_keys("Punjab")
            driver.find_element(By.NAME,'postalCode').send_keys("140401")
            country=Select(driver.find_element(By.NAME,'country'))
            country.select_by_visible_text("INDIA")

            logger.debug("Filling user information")
            driver.find_element(By.NAME,'email').send_keys("jashan")
            driver.find_element(By.NAME,'password').send_keys("1234")
            driver.find_element(By.NAME,'confirmPassword').send_keys("1234")
            driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input').click()
            time.sleep(5)
            logger.info("Verifying registration is success")
            if "Thank You for Registration" in driver.page_source:
                logger.info("Registration succeed")
        except:
            print("Error is occurred")







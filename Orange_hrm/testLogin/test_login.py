
from multiprocessing.util import get_logger

from Orange_hrm.Pageobjectorangehrm.pomorangehrm import Loginpage
from POM.Logging.logger  import get_logger


# logger =get_logger()
class Test_login:
    def test_login(self,setup):
        try:
            logger=get_logger()
            logger.info("Launching browser...")
            driver=setup
            print(setup)
            driver.maximize_window()
            # driver.get("")
            logger.info("Navigating to Loginpage...")
            user=Loginpage(self.test_login(driver))
            user.setusername("Admin")
            user.setpasswd("admin123")
            user.setbtnlick()
            expected_title="OrangeHRM"
            actual_title=driver.title
            assert expected_title==actual_title,"Test FAiled"
            print("Test passed")
        except:
            print("Test failed")
        # C:\Users\HP\PycharmProjects\PythonProject1\Selenium_Python\Orangehrm\testLogin\test_login.py
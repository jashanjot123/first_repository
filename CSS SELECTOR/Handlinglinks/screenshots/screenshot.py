import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# time.sleep(4)
# driver.maximize_window()
# time.sleep(2)
# driver.get("https://www.google.com/")
# time.sleep(2)
# driver.save_screenshot(r"C:\Users\HP\PycharmProjects\PythonProject1\Selenium_Python\CSS SELECTOR\Handlinglinks\keyboardactions\google.png")
# time.sleep(2)
# driver.get_screenshot_as_file(os.getcwd()+"\\googlee.png")
# time.sleep(2)


def capture_screenshot():
    global driver
    try:
        driver = webdriver.Chrome()
        time.sleep(4)
        driver.maximize_window()
        time.sleep(2)
        driver.get("https://www.google.com/")
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path=os.path.join("screenshots12",f"screenshots_{timestamp}.png")

        driver.save_screenshot(screenshot_path)

        print(f"Screenshot has been captured {screenshot_path}")
    except Exception as e:
        print(f"Error is occurred",e)
    finally:
        driver.quit()


capture_screenshot()

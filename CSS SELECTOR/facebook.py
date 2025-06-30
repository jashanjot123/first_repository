
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

fb_drive=webdriver.Chrome()

login=fb_drive.get("https://www.facebook.com/login.php/")

email=fb_drive.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")
time.sleep(2)

pass_1=fb_drive.find_element(By.XPATH,"//input[@type='password']").send_keys("12345")
time.sleep(2)
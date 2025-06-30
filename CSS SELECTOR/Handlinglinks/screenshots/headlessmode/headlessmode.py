from selenium import webdriver
def headless_chrome():
    ops=webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver=webdriver.Chrome(options=ops)
    return driver
driver=headless_chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
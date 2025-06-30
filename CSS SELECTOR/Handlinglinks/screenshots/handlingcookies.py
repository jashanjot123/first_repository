from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
cookies=driver.get_cookies()
print("size of the cookies",len(cookies))
for c in cookies:
    print(c)
driver.add_cookie({"name":"Mycookie","value":"1234"})

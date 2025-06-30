import os
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.maximize_window()
time.sleep(2)
# driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
file=os.getcwd()+r"\test2.xlsx"
workbook=openpyxl.load_workbook(file)
sheet=workbook.active
# for r in range(1,6):
#     for c in range(1,4):
#         sheet.cell(r,c).value='Welcome'


#Create the file with multiple data
sheet.cell(1,1).value=123
sheet.cell(1,2).value="arjun123"
sheet.cell(1,3).value="Panchkula"
workbook.save(file)

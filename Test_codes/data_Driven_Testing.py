from selenium.webdriver import Chrome, ChromeOptions
from time import *
from selenium.webdriver.common.by import By
from xlrd import *

o = ChromeOptions()
o.add_experimental_option("detach", True)

d = []
wb = open_workbook("//Users//rajib//PycharmProjects//M4_selenium//excel_file//register_data.xlsx")
sh = wb.sheet_by_name("Sheet 1")
row_count = sh.nrows
for i in range(1, row_count):
    data = sh.row_values(i)
    d.append(data)

for gender, fname, lname, email, password, conf_pass in d:
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    driver.implicitly_wait(10)

    if gender == "Male":
        driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
    else:
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()

    driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys(fname)
    driver.find_element(By.XPATH, "//input[@name='LastName']").send_keys(lname)
    driver.find_element(By.XPATH, "//input[@name='Email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='ConfirmPassword']").send_keys(conf_pass)

    driver.find_element(By.XPATH, "//input[@name='register-button']").click()

    driver.close()



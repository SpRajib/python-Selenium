
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

#---------------------------------
#Hidden popup
#---------------------------------
driver = Chrome(options=o)
driver.get("https://www.shine.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[text()='Register']").click()
sleep(2)
driver.find_element(By.XPATH, "//input[@type='file']").send_keys("/Users/rajib/Downloads/Rajib_Sahoo_IBM.pdf")
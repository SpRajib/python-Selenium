from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
driver.find_element("xpath", "(//span[.='Select Location'])[3]").click()
driver.find_element("xpath", "(//input[@placeholder='Search for area or street name'])[2]").send_keys("Rajajinagar")
driver.find_element(By.XPATH, "(//li[@class='sc-eIcdZJ ehmwMw'])[1]").click()
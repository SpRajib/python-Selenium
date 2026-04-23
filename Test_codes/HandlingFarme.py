from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("file:///Users/rajib/PythonTutorial/demo.html")
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys("Rajib")
driver.find_element(By.NAME, "password").send_keys("2002")

sleep(2)
ele = driver.find_element(By.XPATH, "//iframe[@src='child.html']")
driver.switch_to.frame(ele)

driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("9870654321")
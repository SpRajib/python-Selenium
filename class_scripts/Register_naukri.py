from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options = o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, "register_Layer").click()
sleep(2)
driver.find_element(By.ID, "name").send_keys("Rajib Sahoo")
sleep(2)
driver.find_element(By.ID, "email").send_keys("xyz@gmail.com")
sleep(2)
driver.find_element(By.ID, "password").send_keys("xyz@123")
sleep(2)
driver.find_element(By.ID, "mobile").send_keys("1234567890")
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Send me important").click()
sleep(2)
driver.find_element(By.CLASS_NAME, "submitbtn.resman-btn-primary.resman-btn-regular.resman-btn-disabled").click()

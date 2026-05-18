from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//a[text()='Twitter']").click()
parentId = driver.current_window_handle # returns parent window address
print(parentId)
allid = driver.window_handles # It store all the window address as a list at the allid variable
print(allid)
driver.switch_to.window(allid[1])
driver.find_element(By.XPATH, "//span[text()='Follow']").click()

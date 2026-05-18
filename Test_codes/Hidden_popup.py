from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

#---------------------------------
#Hidden popup
#---------------------------------
driver = Chrome(options=o)
driver.get("https://www.zepto.com/?srsltid=AfmBOoq9YJ8ogXsPQeDaWqvOcMuzNYgJQWjd-fUolBU8FT_Lyfy67Ws1")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//button[@aria-label='Cart']").click()
sleep(2)
driver.find_element(By.XPATH, "//h6[text()='Login']").click()
sleep(2)
driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9988776655")
driver.find_element(By.XPATH, "//div[text()='Continue']").click()

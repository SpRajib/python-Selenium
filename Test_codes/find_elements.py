from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.swiggy.com/search")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("biryani")
sleep(2)
elems = driver.find_elements(By.XPATH, "//button[@class='xN32R']")

for i in elems:
    print(i.text)
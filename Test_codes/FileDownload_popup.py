from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()

driver.find_element(By.XPATH, "(//a[text()='Download Python 3.14.5'])[2]").click()
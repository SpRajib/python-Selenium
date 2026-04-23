from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
d = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
driver.get("https://www.x.com/")
driver.maximize_window()
driver.save_screenshot(f"/Users/rajib/PycharmProjects/M4_selenium/screenshots/{d}.png")
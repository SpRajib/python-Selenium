from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

@pytest.fixture
def launch():
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
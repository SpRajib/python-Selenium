from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.jiomart.com/?tab=groceries")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//button[text()='Enable Location']").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("lays chips")
sleep(2)
driver.find_element(By.XPATH,"//span[text() = 'lays chips']").click()
sleep(6)
driver.find_element(By.XPATH,"//div[@class='plp-card-container']").click()
sleep(4)
driver.find_element(By.XPATH,"//button[contains(@class,'jm-btn primary medium center')]").click()
sleep(8)
driver.find_element(By.XPATH,"//button[@id='minicart_proceed']").click()
sleep(5)
driver.find_element(By.XPATH,"//button[@id='Login-button']").click()
sleep(5)
driver.find_element(By.XPATH,"//input[@id='phoneNumber']").send_keys("9348086735")
sleep(2)
driver.find_element(By.XPATH,"//button[@aria-label='Sign In']").click()



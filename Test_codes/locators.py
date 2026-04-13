from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options = o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "ico-register").click()
sleep(2)
gender = driver.find_element(By.ID, "gender-male")
gender.click()
sleep(2)
first_name = driver.find_element(By.ID, "FirstName")
first_name.send_keys("Rajib")
sleep(2)
last_name = driver.find_element(By.ID, "LastName")
last_name.send_keys("Sahoo")
sleep(2)
email = driver.find_element(By.NAME, "Email")
email.send_keys("rajibsahoo123@gmail.com")
sleep(2)
pwd = driver.find_element(By.ID, "Password")
pwd.send_keys("rajib@123")
sleep(2)
confirm_pwd = driver.find_element(By.ID, "ConfirmPassword")
confirm_pwd.send_keys("rajib@123")
sleep(2)

submit = driver.find_element(By.ID, "register-button")
submit.click()
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.firstcry.com/")
driver.maximize_window()
sleep(2)
# driver.find_element(By.XPATH,"//a[text()= 'BOY FASHION']").click()
driver.find_element(By.LINK_TEXT,"BOY FASHION").click()
sleep(2)
driver.find_element(By.XPATH,"//img[@title='Kids Magic Cotton Knit Half Sleeves Printed Hooded Shirt & Shorts Set With T-Shirt - Multicolor']").click()
sleep(2)
allid = driver.window_handles
driver.switch_to.window(allid[1])
driver.find_element(By.XPATH, "//span[text()='3 - 4 Y']").click()
sleep(2)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter Pincode'])[3]").send_keys("560076")
sleep(2)
driver.find_element(By.XPATH, "//span[@class='chngeBtn link_bold changepin']").click()
sleep(4)
driver.find_element(By.XPATH, "//span[@class='J16SB_42 cl_fff acttext']").click()
sleep(1)
driver.find_element(By.XPATH, "//span[@id='cart_TotalCount']").click()
sleep(2)
driver.find_element(By.XPATH, "//a[text()='LOGIN TO PLACE ORDER']").click()
sleep(2)
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("9988776655")
sleep(2)
driver.find_element(By.XPATH, "//span[@class='J14SB_42 cl_fff']").click()

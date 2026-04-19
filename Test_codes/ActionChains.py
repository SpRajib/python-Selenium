from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

#------------------------------------
#  Mouse Hover
#------------------------------------
'''
driver = Chrome(options=o)
driver.get("https://www.nike.in/")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//span[text()='New & Featured']")
a = ActionChains(driver)
a.move_to_element(ele).perform()
'''

#------------------------------------
#  Mouse Hover
#------------------------------------
'''
driver = Chrome(options=o)
driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()
sleep(2)
drag_ele = driver.find_element(By.XPATH,"//img[@id='angular']")
drop_ele = driver.find_element(By.XPATH,"//div[@id='droparea']")
a = ActionChains(driver)
a.drag_and_drop(drag_ele, drop_ele).perform()
'''

#------------------------------------
#  Double Click
#------------------------------------
'''
driver = Chrome(options=o)
driver.get("https://checkcps.com/double-click/")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//p[text()='Click here to test your mouse clicks.']")
a = ActionChains(driver)
a.double_click(ele).perform()
'''

#------------------------------------
#  Right click
#------------------------------------
'''
driver = Chrome(options=o)
driver.get("https://github.com/SpRajib")
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH,"//span[@data-content='Repositories']")
a = ActionChains(driver)
ele.context_click(ele).perform()
'''
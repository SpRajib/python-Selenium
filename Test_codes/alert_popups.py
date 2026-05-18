from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

#---------------------------------
#Alert and confirmation popup
#---------------------------------
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, "englishBtn").click()
sleep(2)
driver.find_element(By.XPATH, "//a[@title='Login']").click()
sleep(2)
a = driver.switch_to.alert
a.accept()     #--> To click on ok
# a.dismiss()    #--> To click on cancel
# print(a.text)  #--> To print the text inside the alert
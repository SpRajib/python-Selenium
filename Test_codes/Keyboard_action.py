from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://sprajib.vercel.app/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='user_email']").send_keys("xyz@gmail.com")
sleep(2)
ele = driver.find_element(By.XPATH, "//input[@name='user_email']")
for i in range(13) :
    ele.send_keys(Keys.BACK_SPACE)

ele.send_keys("rajibsahoo95892@gmail.com")
ele.send_keys(Keys.COMMAND+"a")
ele.send_keys(Keys.COMMAND+"c")
sleep(2)
name = driver.find_element(By.XPATH, "//input[@name='user_name']")
name.send_keys(Keys.COMMAND+"v")
for i in range(15) :
    name.send_keys(Keys.BACK_SPACE)

for i in range(5):
    name.send_keys(Keys.ARROW_LEFT)
name.send_keys(Keys.SPACE)
sleep(2)

sub =  driver.find_element(By.XPATH, "//input[@name='subject']")
sub.send_keys("Nothing")
sleep(2)

name.send_keys(Keys.COMMAND+"ac")

msg = driver.find_element(By.XPATH, "//textarea[@name='message']")
msg.send_keys("Hiii,"+Keys.SPACE+Keys.COMMAND+"v")
sleep(2)

driver.find_element(By.XPATH, "//button[@type='submit']").click()





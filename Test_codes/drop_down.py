from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://landrecords.karnataka.gov.in/Service2/")
driver.maximize_window()
sleep(5)
# driver.find_element(By.XPATH,"(//a[@data-toggle='tooltip'])[2]").click()
# sleep(5)

dist = driver.find_element(By.ID, "ctl00_MainContent_ddlCDistrict")
s1 = Select(dist)
s1.select_by_index(3)
sleep(5)

Taluka = driver.find_element(By.ID, "ctl00_MainContent_ddlCTaluk")
s2 = Select(Taluka)
s2.select_by_value("3")
sleep(5)

hobli = driver.find_element(By.ID, "ctl00_MainContent_ddlCHobli")
s3 = Select(hobli)
s3.select_by_visible_text("KUNDANA")
sleep(5)

village = driver.find_element(By.ID, "ctl00_MainContent_ddlCVillage")
s4 = Select(village)
s4.select_by_value("47")


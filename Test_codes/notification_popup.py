from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_argument("--disable-notifications")

driver = Chrome(options=o)
driver.get("https://in.puma.com/in/en?utm_source=GGL-SEA&utm_medium=BS&utm_campaign=BS_GGL_SEA_IN_STAG_agency_1000067495857508873&gad_source=1&gad_campaignid=22200704844&gbraid=0AAAAADiCiZcCFT3dnqHUgEdS8XVPCppN1&gclid=CjwKCAjw8arQBhB9EiwAfIKdQjhqdjimFMBE3pawdbi6yUEO_ZY7tEc1cCz4G8dEeWM00ZNyvowVMhoC2yQQAvD_BwE")
driver.maximize_window()

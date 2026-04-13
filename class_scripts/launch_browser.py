'''
from selenium.webdriver import Chrome
c = Chrome()
'''

#---------------------------
# open and hold browser
#---------------------------
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True) # Not to close browser automatically

#driver = Chrome(options=o) # Open browser and stay for long duration
# Driver : It is a variable which holds the opened browser address

#-----------------------
# Enter URL
#-----------------------

# Example for secured URL
"""
driver = Chrome(options=o)
driver.get("https://www.google.com")
"""

# Example for non-secured URL
"""
driver = Chrome(options=o)
driver.get("http://www.google.com")
"""

# Example for other than HTTPS and HTTP
"""
driver = Chrome(options=o)
driver.get("www.google.com")
# InvalidArgumentException
"""

#-------------------------------
#close() : It is used to close current window/Tab
#quit() : It is used to close complete browser
"""
driver = Chrome(options=o)
driver.get("https://www.google.com")
sleep(5.0)
# driver.close()
driver.quit()
"""

#---------------------------
# Size Manage
#--------------------------
"""
driver = Chrome(options=o)
driver.get("https://www.google.com")
sleep(2)
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
"""

#control browser
"""
driver = Chrome(options=o)
driver.get("https://www.gmail.com")
driver.maximize_window()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
"""
# get size
"""
driver = Chrome(options=o)
driver.get("https://www.google.com")
driver.maximize_window()
res = driver.get_window_size()
print(res)  #{'width': 1440, 'height': 793}

res1 = driver.get_window_position()
print(res1) # {'x': 0, 'y': 30}

res2 = driver.get_window_rect()
print(res2) # {'height': 793, 'width': 1440, 'x': 0, 'y': 30}
"""

# set size
"""
driver = Chrome(options=o)
driver.get("https://www.google.com")
driver.maximize_window()
sleep(2)
driver.set_window_size(1040, 593)
sleep(2)
driver.set_window_position(2, 20)
sleep(2)
driver.set_window_rect(10, 20, 10, 20)
"""

# Verification Property
# title, current_url, page_source
"""
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
print(driver.title)       # Selenium
sleep(2)
print(driver.current_url)         # https://www.selenium.dev/
sleep(2)
print(driver.page_source)        # <html>.....</html>
driver.quit()
"""

from welcome_page import *
from login_page import *

def test_login_tc(launch):
    driver = launch

    w = WelcomePage(driver)
    w.login_page()

    l = LoginPage(driver)
    l.email("selenium@gmail.com")
    l.password("selenium")
    l.submit()
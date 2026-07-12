from welcome_page import *
from register_page import *

def test_register_tc(launch):
    driver = launch
    w = WelcomePage(driver)
    w.register_link()

    r = RegisterPage(driver)
    r.gender("Male")
    r.first_name("selenium")
    r.last_name("automation")
    r.email("selenium@gmail.com")
    r.password("selenium")
    r.confirm_password("selenium")
    r.register_button()
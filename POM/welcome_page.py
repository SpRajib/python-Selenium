from selenium.webdriver.common.by import By


class WelcomePage():
    def __init__(self, driver):
        self.driver = driver

    def register_link(self):
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()

    def login_page(self):
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()
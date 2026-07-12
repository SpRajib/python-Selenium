from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def email(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='Email']").send_keys(data)

    def password(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='Password']").send_keys(data)

    def submit(self):
        self.driver.find_element(By.XPATH, "(//input[@type='submit'])[2]").click()
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def gender(self, option):
        if option == 'Male':
            self.driver.find_element(By.XPATH, "//input[@id='gender-male']").click()
        else:
            self.driver.find_element(By.XPATH, "//input[@id='gender-female']").click()

    def first_name(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='FirstName']").send_keys(data)

    def last_name(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='LastName']").send_keys(data)

    def email(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='Email']").send_keys(data)

    def password(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='Password']").send_keys(data)

    def confirm_password(self,data):
        self.driver.find_element(By.XPATH, "//input[@name='ConfirmPassword']").send_keys(data)

    def register_button(self):
        self.driver.find_element(By.XPATH, "//input[@name='register-button']").click()
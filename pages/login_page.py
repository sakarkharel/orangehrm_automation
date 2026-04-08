from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username_input = (By.XPATH, "//input[@placeholder='Username']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    error_message = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def load(self):
         self.open(self.url)
         WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located(self.username_input)
         )

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        self.type(*self.username_input, username)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )
        self.type(*self.password_input, password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        self.click(*self.login_button)

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        )
        return self.find(*self.error_message).text
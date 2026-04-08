
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
    user_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_button = (By.XPATH, "//a[text()='Logout']")
    about_button = (By.XPATH, "//a[normalize-space()='About']")
    support_button = (By.XPATH, "//a[normalize-space()='Support']")

    def load(self):
        self.open(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_header)
        )

    def is_dashboard_loaded(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.dashboard_header)
        ).is_displayed()

    def open_user_dropdown(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.user_dropdown)
        )
        self.click(*self.user_dropdown)

    def click_logout(self):
        self.open_user_dropdown()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logout_button)
        )
        self.click(*self.logout_button)

    def click_about(self):
        self.open_user_dropdown()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.about_button)
        )
        self.click(*self.about_button)


    def click_support(self):
        self.open_user_dropdown()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.support_button)
        )
        self.click(*self.support_button)


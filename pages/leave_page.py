from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LeavePage(BasePage):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"
    PAGE_HEADER = (By.XPATH, "//h6[text()='Leave']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    REPORT_DROPDOWN = (By.XPATH, "//span[normalize-space()='Reports']//i[@class='oxd-icon bi-chevron-down']")
    LEAVE_ENTITLEMENT_REPORT = (
        By.XPATH,
        "//a[text()='Leave Entitlements and Usage Report']"
    )

    LOCATION_DROPDOWN = (By.XPATH, "//div[text()='-- Select --']")
    SUBUNIT_DROPDOWN = (By.XPATH, "//div[text()='-- Select --']")
    TEXAS_RD_OPTION = (By.XPATH, "//span[text()='Texas R&D']")
    ENGINEERING_OPTION = (By.XPATH, "//span[text()='Engineering']")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")

    def open_leave(self):
        self.open(self.url)

    def go_to_leave_via_menu(self):
        leave_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LEAVE_MENU)
        )
        leave_menu.click()

    def open_entitlement_report(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REPORT_DROPDOWN)
        )
        dropdown.click()

        report_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LEAVE_ENTITLEMENT_REPORT)
        )
        report_option.click()
        time.sleep(10)


    def select_location(self):
        location = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATION_DROPDOWN)
        )
        location.click()

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TEXAS_RD_OPTION)
        )
        option.click()

    def select_subunit(self):
        subunit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBUNIT_DROPDOWN)
        )
        subunit.click()

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ENGINEERING_OPTION)
        )
        option.click()
        time.sleep(5)
    
    def click_submit(self):
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT_BTN)
        )
        submit_btn.click()
        time.sleep(5)

    def verify_leave_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PAGE_HEADER)
        )


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.leave_page import LeavePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_navigate_to_leave_page(driver):
    login_page = LoginPage(driver)
    leave_page = LeavePage(driver)

    login_page.load()
    login_page.login("Admin", "admin123")

    dashboard = login_page.wait_for_element(By.XPATH, "//h6[text()='Dashboard']")
    assert dashboard is not None

    leave_page.go_to_leave_via_menu()
    leave_page.open_entitlement_report()
    leave_page.select_location()
    leave_page.select_subunit()
    leave_page.click_submit()

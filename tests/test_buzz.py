import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.buzz_page import BuzzPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_create_buzz_post(driver):
    login_page = LoginPage(driver)
    buzz_page = BuzzPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    dashboard = login_page.wait_for_element(By.XPATH, "//h6[text()='Dashboard']")
    assert dashboard is not None
    buzz_page.open_buzz()
    buzz_page.create_buzz_post()
    buzz_page.add_comment()




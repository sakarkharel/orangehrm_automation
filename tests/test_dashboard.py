from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_logout(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_loaded()
    dashboard_page.click_logout()

def test_about_popup(driver):
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_loaded()
    dashboard_page.click_about()

def test_support_page(driver):
    from pages.login_page import LoginPage
    from pages.dashboard_page import DashboardPage
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    dashboard_page.click_support()




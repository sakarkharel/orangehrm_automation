from pages.login_page import LoginPage

#valid username and valid passocode
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    
#both invalid username and invalid passcode
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wronguser", "wrongcode")

    assert "Invalid credentials" in login_page.get_error_message()

#valid username and invalid passcode 
def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "wrongpass")

    assert "Invalid credentials" in login_page.get_error_message()

#empty username and passcode 
def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")

#empty username only 
def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "admin123")


#empty passcode only 
def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "")


# case sensitivity check i.e. both lowercase  -- fails in this 
def test_case_sensitive_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("admin", "admin123")  # lowercase username, same passcode 












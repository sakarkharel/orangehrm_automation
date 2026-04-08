from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time


class BuzzPage(BasePage):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"

    TEXTAREA = (By.XPATH, "//textarea[@placeholder=\"What's on your mind?\"]")
    SHARE_PHOTOS_BTN = (By.XPATH, "//button[normalize-space()='Share Photos']")
    SHARE_BTN = (By.XPATH, "//div[@class='oxd-form-actions orangehrm-buzz-post-modal-actions']//button[1]")
    COMMENT_ICON = (By.XPATH, "//i[contains(@class,'bi-chat-text-fill')]")
    COMMENT_BOX = (By.XPATH, "//input[@placeholder='Write your comment...']")
    def open_buzz(self):
        self.open(self.url)

    def create_buzz_post(self):
        self.wait_for_element(*self.TEXTAREA)
        self.click(*self.TEXTAREA)
        self.type(*self.TEXTAREA, text="This is my new cat")
        self.click(*self.SHARE_PHOTOS_BTN)
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        file_path = os.path.abspath("catimages.jpeg")
        file_input.send_keys(file_path)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SHARE_BTN)
        )
        self.click(*self.SHARE_BTN)

    def add_comment(self):
        self.driver.execute_script("window.scrollBy(0, 300);")
        comment_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COMMENT_ICON)
        )
        comment_icon.click()
        comment_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.COMMENT_BOX)
        )
        comment_box.send_keys("hey lets catch up")
        comment_box.send_keys(Keys.ENTER)
        time.sleep(5)
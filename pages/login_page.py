"""
pages/login_page.py
Locators and actions for the SauceDemo login page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME    = (By.ID, "user-name")
    PASSWORD    = (By.ID, "password")
    LOGIN_BTN   = (By.ID, "login-button")
    ERROR_MSG   = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def error_visible(self):
        return self.is_visible(self.ERROR_MSG)

"""
pages/checkout_page.py
Covers checkout step 1 (form), step 2 (overview), step 3 (complete).
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME    = (By.ID, "first-name")
    LAST_NAME     = (By.ID, "last-name")
    ZIP_CODE      = (By.ID, "postal-code")
    CONTINUE_BTN  = (By.ID, "continue")
    FINISH_BTN    = (By.ID, "finish")
    ERROR_MSG     = (By.CSS_SELECTOR, "h3[data-test='error']")
    CONFIRM_HDR   = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first, last, zip_code):
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        self.type_text(self.ZIP_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish(self):
        self.click(self.FINISH_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def error_visible(self):
        return self.is_visible(self.ERROR_MSG)

    def get_confirmation(self):
        return self.get_text(self.CONFIRM_HDR)

    def is_complete(self):
        return self.is_visible(self.CONFIRM_HDR)

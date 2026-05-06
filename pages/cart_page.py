"""
pages/cart_page.py
Locators and actions for the shopping cart page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE          = (By.CLASS_NAME, "title")
    ITEM_NAMES     = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN   = (By.ID, "checkout")
    CONTINUE_BTN   = (By.ID, "continue-shopping")

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_items(self):
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_BTN)

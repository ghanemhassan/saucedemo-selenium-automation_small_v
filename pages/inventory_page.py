"""
pages/inventory_page.py
Locators and actions for the products / inventory page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE        = (By.CLASS_NAME, "title")
    PRODUCT_NAMES= (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE   = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON    = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_BTN   = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK  = (By.ID, "logout_sidebar_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_NAMES))

    def add_to_cart(self, product_name):
        btn_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.click((By.CSS_SELECTOR, f"[data-test='{btn_id}']"))

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(self.CART_ICON)

    def logout(self):
        self.click(self.BURGER_BTN)
        self.click(self.LOGOUT_LINK)

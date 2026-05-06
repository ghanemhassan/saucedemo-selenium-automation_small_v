"""
tests/test_products.py  — 4 test cases
TC5  Inventory page loads with 6 products
TC6  Adding one product shows badge count of 1
TC7  Adding multiple products shows correct badge count
TC8  Removing a product decrements the badge count
"""

from pages.inventory_page import InventoryPage

BACKPACK   = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


class TestProducts:

    def test_product_list_loads(self, logged_in):
        """TC5 – Exactly 6 products are displayed on the inventory page."""
        assert InventoryPage(logged_in).get_product_count() == 6

    def test_add_single_product(self, logged_in):
        """TC6 – Adding one item shows a cart badge of 1."""
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        assert inv.get_cart_count() == 1

    def test_add_multiple_products(self, logged_in):
        """TC7 – Adding two items shows a cart badge of 2."""
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        inv.add_to_cart(BIKE_LIGHT)
        assert inv.get_cart_count() == 2

    def test_remove_product(self, logged_in):
        """TC8 – Removing an item decrements the badge back to 0."""
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        assert inv.get_cart_count() == 1
        # The button label switches to "Remove" after adding
        from selenium.webdriver.common.by import By
        inv.click((By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']"))
        assert inv.get_cart_count() == 0

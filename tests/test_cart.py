"""
tests/test_cart.py  — 3 test cases
TC9   Added product appears in the cart
TC10  'Continue Shopping' returns to inventory
TC11  'Checkout' button navigates to checkout step 1
"""

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BACKPACK      = "Sauce Labs Backpack"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CHECKOUT_URL  = "https://www.saucedemo.com/checkout-step-one.html"


class TestCart:

    def test_product_appears_in_cart(self, logged_in):
        """TC9 – A product added on the inventory page is listed in the cart."""
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        inv.open_cart()
        assert BACKPACK in CartPage(logged_in).get_items()

    def test_continue_shopping(self, logged_in):
        """TC10 – 'Continue Shopping' returns to the inventory page."""
        InventoryPage(logged_in).open_cart()
        CartPage(logged_in).continue_shopping()
        assert INVENTORY_URL in logged_in.current_url

    def test_checkout_button(self, logged_in):
        """TC11 – 'Checkout' navigates to checkout step 1."""
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        inv.open_cart()
        CartPage(logged_in).proceed_to_checkout()
        assert CHECKOUT_URL in logged_in.current_url

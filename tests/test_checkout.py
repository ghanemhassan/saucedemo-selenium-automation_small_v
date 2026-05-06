"""
tests/test_checkout.py  — 4 test cases
TC12  Empty form shows a validation error
TC13  Valid info advances to checkout step 2
TC14  Completing the order shows a confirmation message
TC15  Full end-to-end purchase flow
"""

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BACKPACK     = "Sauce Labs Backpack"
COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"
STEP2_URL    = "https://www.saucedemo.com/checkout-step-two.html"


def _add_and_checkout(driver):
    """Helper: add one product and reach checkout step 1."""
    inv = InventoryPage(driver)
    inv.add_to_cart(BACKPACK)
    inv.open_cart()
    CartPage(driver).proceed_to_checkout()
    return CheckoutPage(driver)


class TestCheckout:

    def test_empty_form_shows_error(self, logged_in):
        """TC12 – Submitting step-1 with no data shows a validation error."""
        checkout = _add_and_checkout(logged_in)
        checkout.click(checkout.CONTINUE_BTN)
        assert checkout.error_visible()
        assert "First Name is required" in checkout.get_error()

    def test_valid_info_reaches_step2(self, logged_in):
        """TC13 – Valid customer info advances to the order overview page."""
        checkout = _add_and_checkout(logged_in)
        checkout.fill_info("Jane", "Doe", "90210")
        assert STEP2_URL in logged_in.current_url

    def test_order_confirmation(self, logged_in):
        """TC14 – Finishing the order shows a thank-you confirmation."""
        checkout = _add_and_checkout(logged_in)
        checkout.fill_info("Jane", "Doe", "90210")
        checkout.finish()
        assert checkout.is_complete()
        assert "Thank you" in checkout.get_confirmation()

    def test_full_end_to_end_flow(self, logged_in):
        """TC15 – Complete happy path: add → cart → checkout → confirm."""
        # Add product and verify badge
        inv = InventoryPage(logged_in)
        inv.add_to_cart(BACKPACK)
        assert inv.get_cart_count() == 1

        # Go to cart and verify item
        inv.open_cart()
        assert BACKPACK in CartPage(logged_in).get_items()

        # Complete checkout
        CartPage(logged_in).proceed_to_checkout()
        checkout = CheckoutPage(logged_in)
        checkout.fill_info("Jane", "Doe", "90210")
        checkout.finish()

        # Confirm order complete
        assert COMPLETE_URL in logged_in.current_url
        assert "Thank you" in checkout.get_confirmation()

"""
tests/test_login.py  — 4 test cases
TC1  Valid login navigates to inventory page
TC2  Invalid credentials show an error message
TC3  Empty username shows a validation error
TC4  Logout returns to the login page
"""

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL      = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


class TestLogin:

    def test_valid_login(self, driver):
        """TC1 – Valid credentials land on the inventory page."""
        LoginPage(driver).login("standard_user", "secret_sauce")
        assert INVENTORY_URL in driver.current_url
        assert InventoryPage(driver).get_title() == "Products"

    def test_invalid_credentials(self, driver):
        """TC2 – Wrong password shows an error banner."""
        page = LoginPage(driver)
        page.login("standard_user", "wrong_password")
        assert page.error_visible()
        assert "Username and password do not match" in page.get_error()

    def test_empty_username(self, driver):
        """TC3 – Submitting without a username shows a validation error."""
        page = LoginPage(driver)
        page.type_text(page.PASSWORD, "secret_sauce")
        page.click(page.LOGIN_BTN)
        assert page.error_visible()
        assert "Username is required" in page.get_error()

    def test_logout(self, logged_in):
        """TC4 – Logging out returns the user to the login page."""
        InventoryPage(logged_in).logout()
        assert logged_in.current_url == BASE_URL

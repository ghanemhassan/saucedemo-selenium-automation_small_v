"""
conftest.py — shared pytest fixtures.
The `driver` fixture opens Chrome before each test and quits after.
The `logged_in` fixture reuses `driver` and performs a login first.
"""

import pytest
from utils.driver_factory import DriverFactory
from utils.screenshot_helper import ScreenshotHelper
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture()
def driver(request):
    headless = request.config.getoption("--headless")
    web_driver = DriverFactory.get_driver(headless=headless)
    web_driver.get("https://www.saucedemo.com/")
    yield web_driver
    # Capture screenshot on failure, then quit
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        ScreenshotHelper.capture(web_driver, request.node.name)
    web_driver.quit()


@pytest.fixture()
def logged_in(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    yield driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

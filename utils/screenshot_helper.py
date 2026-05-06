"""
utils/screenshot_helper.py
Saves a timestamped screenshot to the /screenshots/ folder.
Called automatically by conftest.py when a test fails.
"""

import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")


class ScreenshotHelper:
    @staticmethod
    def capture(driver: WebDriver, test_name: str) -> None:
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, filename))
        print(f"Screenshot saved: {filename}")

# SauceDemo Selenium Automation — Student Project

A beginner-friendly Selenium automation project for [SauceDemo](https://www.saucedemo.com/), built with Python, PyTest, and the Page Object Model.

## Tech Stack
- Python 3.10+
- Selenium WebDriver 4
- PyTest + pytest-html
- webdriver-manager (auto-downloads ChromeDriver)

## Project Structure
```
saucedemo_small/
├── pages/
│   ├── base_page.py        # Shared helpers (click, type, wait)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py       # TC1  – TC4
│   ├── test_products.py    # TC5  – TC8
│   ├── test_cart.py        # TC9  – TC11
│   └── test_checkout.py    # TC12 – TC15
├── utils/
│   ├── driver_factory.py   # Creates Chrome WebDriver
│   └── screenshot_helper.py# Saves screenshot on failure
├── screenshots/            # Auto-created on first failure
├── reports/                # HTML report saved here
├── conftest.py             # Shared fixtures (driver, logged_in)
├── pytest.ini
└── requirements.txt
```

## Test Cases (15 total)

| #    | Area     | Description                          |
|------|----------|--------------------------------------|
| TC1  | Login    | Valid login → inventory page         |
| TC2  | Login    | Invalid credentials → error message  |
| TC3  | Login    | Empty username → validation error    |
| TC4  | Login    | Logout → back to login page          |
| TC5  | Products | Inventory loads 6 products           |
| TC6  | Products | Add one item → badge shows 1         |
| TC7  | Products | Add two items → badge shows 2        |
| TC8  | Products | Remove item → badge back to 0        |
| TC9  | Cart     | Added product appears in cart        |
| TC10 | Cart     | Continue Shopping → inventory        |
| TC11 | Cart     | Checkout button → step 1             |
| TC12 | Checkout | Empty form → validation error        |
| TC13 | Checkout | Valid info → step 2 overview         |
| TC14 | Checkout | Finish order → confirmation shown    |
| TC15 | Checkout | Full end-to-end purchase flow        |

## Installation (Fedora Linux)

```bash
# Install Chrome if needed
sudo dnf install -y fedora-workstation-repositories
sudo dnf config-manager --set-enabled google-chrome
sudo dnf install -y google-chrome-stable

# Set up the project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all 15 tests
pytest

# Run one file
pytest tests/test_login.py

# Run headless (no browser window)
pytest --headless

# Open the HTML report
xdg-open reports/report.html
```

## Credentials
| Username      | Password     |
|---------------|--------------|
| standard_user | secret_sauce |



# Automated End-to-End Checkout Flow Test for SauceDemo

## Overview
This project contains a Python Selenium automation script that performs an **end-to-end checkout flow** on the [SauceDemo](https://www.saucedemo.com/) demo e-commerce website. The script automates the entire user journey starting from login, adding a product to the cart, proceeding through checkout steps, filling user information, completing the purchase, and verifying the success message on order completion.

## Features
- Browser automation using **Selenium WebDriver** with Chrome
- Comprehensive checkout flow validation with assertions at each step
- Clear stepwise print outputs for tracking progress during test execution
- Implicit waits to handle dynamic page elements
- Final wait pause to allow manual observation before browser closes

## Pre-requisites
- Python 3.7 or higher installed
- Google Chrome browser installed
- `chromedriver` should be available or managed automatically by Selenium
- Required Python packages:
  - `selenium`
  - `pytest`

You can install Selenium and Pytest via pip if not already installed:

```bash
pip install selenium pytest
```

## Files
- `test_saucedemo_checkout.py` — Contains the pytest automation test script for the checkout flow

## Test Description
The test script `test_end_to_end_checkout_flow` does the following:

1. Opens the SauceDemo website and logs in with valid standard user credentials.
2. Adds the "Sauce Labs Backpack" product to the shopping cart.
3. Navigates to the cart page and verifies the presence of the product.
4. Initiates the checkout process.
5. Fills in user details (First name, Last name, Postal code).
6. Completes the purchase process.
7. Validates the order success message "Thank you for your order!" is displayed.

## How to Run the Test

1. Save the Python test script file (e.g., `test_saucedemo_checkout.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the test script.
4. Run the test using pytest:

```bash
pytest test_saucedemo_checkout.py
```

The test will launch Chrome browser, execute the checkout flow, print step completion messages, and automatically close the browser after a brief pause.

## Notes
- The script uses a Pytest fixture to handle browser setup and teardown cleanly.
- Implicit waits and element checks are used to ensure UI stability during automation.
- The test assumes stable internet connectivity and availability of the SauceDemo site.
- This script can be extended or adapted for more complex scenarios or other browsers by modifying the fixture.

***

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Pytest fixture to set up and tear down the browser for the test.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Standard wait time
    driver.maximize_window()
    yield driver
    # Pause at the end to observe the final page
    time.sleep(5) 
    driver.quit()

def test_end_to_end_checkout_flow(driver):
    """
    Automates the entire checkout process on saucedemo.com,
    including login, adding an item, filling the form, and verifying the purchase.
    """
    
    # Step 1: Login to the application
    print("Step 1: Logging in...")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # Verification: Ensure login was successful and we are on the inventory page.
    assert "inventory.html" in driver.current_url, "Login failed or did not redirect to inventory page."
    print("Login successful.")

    # Step 2: Add an item to the cart
    print("Step 2: Adding an item to the cart...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # Verification: Check if the cart badge updates to '1'.
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1", "Cart badge count is not 1 after adding an item."
    print("Item added to cart successfully.")

    # Step 3: Navigate to the shopping cart
    print("Step 3: Navigating to the cart...")
    driver.find_element(By.ID, "shopping_cart_container").click()
    # Verification: Ensure we are on the cart page.
    assert "cart.html" in driver.current_url, "Did not navigate to the cart page."
    print("Successfully navigated to the cart page.")

    # Step 4: Proceed to checkout
    print("Step 4: Proceeding to checkout...")
    driver.find_element(By.ID, "checkout").click()
    # Verification: Ensure we are on the checkout information page.
    assert "checkout-step-one.html" in driver.current_url, "Did not proceed to the checkout information page."
    print("Successfully on the checkout information page.")

    # Step 5: Fill out user information
    print("Step 5: Filling out user information...")
    driver.find_element(By.ID, "first-name").send_keys("Bharath")
    driver.find_element(By.ID, "last-name").send_keys("MM")
    driver.find_element(By.ID, "postal-code").send_keys("560001")
    driver.find_element(By.ID, "continue").click()
    # Verification: Ensure we are on the checkout overview page.
    assert "checkout-step-two.html" in driver.current_url, "Did not proceed to the checkout overview page."
    print("User information filled successfully.")

    # Step 6: Finish the purchase
    print("Step 6: Finishing the purchase...")
    driver.find_element(By.ID, "finish").click()
    # Verification: Ensure we are on the checkout complete page.
    assert "checkout-complete.html" in driver.current_url, "Did not proceed to the checkout complete page."
    print("Purchase finished.")

    # Step 7: Verify the success message
    print("Step 7: Verifying the success message...")
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in success_message, "Success message is incorrect or not found."
    print(f"Success message found: '{success_message}'")
    print("Checkout flow completed and verified successfully!")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Setup ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Wait time for elements to appear
    driver.maximize_window()  # Maximize browser window
    yield driver
    time.sleep(3)  # Pause for observation before closing
    driver.quit()

def test_end_to_end_checkout_flow(driver):
    # Step 1: Navigate and log in
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Login failed or not on inventory page"

    # Step 2: Add product to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", "Cart count did not update to 1"

    # Step 3: Navigate to the cart
    driver.find_element(By.ID, "shopping_cart_container").click()
    assert "cart.html" in driver.current_url, "Did not reach cart page"

    # Step 4: Proceed to checkout
    driver.find_element(By.ID, "checkout").click()
    assert "checkout-step-one.html" in driver.current_url, "Did not reach checkout information page"

    # Step 5: Fill out checkout information
    driver.find_element(By.ID, "first-name").send_keys("Junaid")
    driver.find_element(By.ID, "last-name").send_keys("Ahmed")
    driver.find_element(By.ID, "postal-code").send_keys("563101")
    driver.find_element(By.ID, "continue").click()
    assert "checkout-step-two.html" in driver.current_url, "Did not reach checkout overview page"

    # Step 6: Finish purchase
    driver.find_element(By.ID, "finish").click()
    assert "checkout-complete.html" in driver.current_url, "Did not reach checkout complete page"

    # Step 7: Verify success message
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in success_message, "Success message not found"

    print("Checkout flow completed successfully!")

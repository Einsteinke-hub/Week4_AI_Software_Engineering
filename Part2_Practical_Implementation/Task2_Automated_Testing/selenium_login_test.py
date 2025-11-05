from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_functionality():
    """Automated test for login page functionality"""
    driver = webdriver.Chrome()
    
    try:
        # Test valid login
        driver.get("https://example.com/login")
        
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-btn")
        
        username_field.send_keys("test_user")
        password_field.send_keys("correct_password")
        login_button.click()
        
        # Wait for login success
        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )
        print("✓ Valid login test passed")
        
        # Take screenshot
        driver.save_screenshot("test_results/valid_login.png")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        driver.save_screenshot("test_results/test_failure.png")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_functionality()
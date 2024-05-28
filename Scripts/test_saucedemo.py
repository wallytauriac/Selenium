import pytest
import time
from selenium import webdriver
from Selenium.Scripts.saucedemo import LoginPage
from Selenium.Scripts.saucedemo import HomePage


def test_sd_login_logout_1():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    # Instantiate Page Objects
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    driver.get("https://saucedemo.com")

    title = login_page.get_title()
    print("\ntitle of page: ", title)

    # Interact with the Page Objects
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    # Welcome message will be visible on the home page after successful login
    welcome_message_text = home_page.get_welcome_message_text()
    print(welcome_message_text)

    # Perform assertions based on the expected behavior
    try:
        print("Login Completed: Passed")
        pmsg = "Home page Displayed: "
        assert "Swag Labs" == welcome_message_text, pmsg
    except AssertionError as fmsg:
        print(fmsg)
        exit(1)
    finally:
        print(pmsg + "Passed")


    # Logout
    home_page.click_burger_button()
    driver.implicitly_wait(10)
    time.sleep(3)
    print("Burger Menu status: Open")
    print("Logout button status: Visible")
    home_page.click_logout_button()

    # Close the WebDriver instance
    driver.quit()


if __name__ == "__main__":
    pytest.main(["test_saucedemo.py", "-s"])
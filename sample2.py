import pytest
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # You can use any other WebDriver (e.g., Firefox, Safari) here
    html_file_path = os.path.abspath("Selenium/Templates/nestedElements.html")
    driver.get("file://" + html_file_path)
    yield driver
    # Teardown - close the browser window
    driver.quit()

def test_should_find_element_by_xpath(browser):

    element = browser.find_element(By.NAME, "form2")
    child = element.find_element(By.XPATH, "select")
    assert child.get_attribute("id") == "2"
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # You can use any other WebDriver (e.g., Firefox, Safari) here
    yield driver
    # Teardown - close the browser window
    driver.quit()

def test_get_tag_elements(browser):
    # Load the local HTML file
    html_file_path = os.path.abspath("Selenium/Templates/index.html")
    browser.get("file://" + html_file_path)
    # Find elements and display *****************************
    # Use this for HTML tags that have text values enclosed in > <
    type = ["h2", "a", "input"]
    # Get all the elements available with tag name
    for t in type:
        element = browser.find_elements(By.TAG_NAME, t)
        print_elements(t, element)

def test_get_id_elements(browser):
    # Load the local HTML file
    html_file_path = os.path.abspath("Selenium/Templates/index.html")
    browser.get("file://" + html_file_path)
    # Get all the elements available with ID
    # Use this for HTML tags that have ID= elements
    type = ["fname", "lname"]
    for t in type:
        element = browser.find_element(By.ID, t)
        print("Element for " + t + " found: \n" + element.text)

def print_elements(type, element):
    print("Elements for " + type + " found: ")
    for e in element:
        print(e.text)
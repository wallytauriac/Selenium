import os
# import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # You can use any other WebDriver (e.g., Firefox, Safari) here
    yield driver
    # Teardown - close the browser window
    driver.quit()

def test_html_1(browser):
    # Load the local HTML file
    html_file_path = os.path.abspath("Templates/index.html")
    browser.get("file://" + html_file_path)
    print("Test Name: test_html_1")
    print("Test File: " + html_file_path)
    # Find elements and perform actions and assertions
    heading_element = browser.find_element(By.TAG_NAME, "h3")

    wait = WebDriverWait(browser, timeout=15)
    wait.until(lambda d: heading_element.is_displayed())

    print("Find element success for h2 tag")
    assert heading_element.text == "Contact Selenium"
    print("Title assertion passed: " + heading_element.text)

def test_html_2(browser):
    # Load the local HTML file
    html_file_path = os.path.abspath("Templates/index.html")
    browser.get("file://" + html_file_path)
    print("Test Name: test_html_2")
    print("Test File: " + html_file_path)
    # Find elements and perform actions and assertions
    heading_element = None
    try:
        heading_element = browser.find_element(By.LINK_TEXT, "Selenium Official Page")
        print("Find element success for link text")
        assert heading_element.text == "Selenium Official Page"
    except AssertionError:
        print("Link assertion error encountered")
        exit(1)
    except NoSuchElementException:
        print("Element Exception")
        exit(1)
    finally:
        print("Link assertion passed--> " + heading_element.text)


if __name__ == "__main__":
    pytest.main(["ASO3.py", "-s"])

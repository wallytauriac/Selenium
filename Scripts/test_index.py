import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    # Load the local HTML file
    # Fill first name and last name
    # Check the newsletter checkbox
    # Submit the form
    # Assertion examples


if __name__ == "__main__":
    pytest.main(["test_index.py", "-s", "--html=report.html", "--self-contained-html"])
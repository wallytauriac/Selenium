import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))

def test_marital_status(driver):
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    # driver.get("path_to_your_html_file.html")

    # Select Marital status
    marital_status = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//select[@name='stats']")))
    marital_status_select = Select(marital_status)
    marital_status_select.select_by_value("married")
    time.sleep(2)
    take_screenshot(driver, "admin/index1.png")
    assert marital_status_select.first_selected_option.text == "Married"

def test_radio_button(driver):
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    # driver.get("path_to_your_html_file.html")

    # Select radio button
    gender_female = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//input[@name='gender' and @value='f']")))
    time.sleep(2)
    gender_female.click()
    take_screenshot(driver, "admin/index2.png")
    assert gender_female.is_selected()


def test_first_name(driver):
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    # driver.get("path_to_your_html_file.html")

    # Fill first name
    first_name_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//input[@id='fname']")))
    first_name_input.clear()
    time.sleep(2)
    first_name_input.send_keys("John")
    take_screenshot(driver, "admin/index3.png")
    assert first_name_input.get_attribute("value") == "John"

def test_last_name(driver):
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    # driver.get("path_to_your_html_file.html")
    # Fill last name
    last_name_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@id='lname']")))
    last_name_input.clear()
    time.sleep(2)
    last_name_input.send_keys("Doe")
    take_screenshot(driver, "admin/index4.png")
    assert last_name_input.get_attribute("value") == "Doe"

def test_nl_checkbox(driver):
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    # driver.get("path_to_your_html_file.html")

    # Check the newsletter checkbox
    newsletter_checkbox = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "//input[@name='newsletter']")))
    newsletter_checkbox.click()
    take_screenshot(driver, "admin/index5.png")
    assert newsletter_checkbox.is_selected()

def none():
    # Submit the form
    submit_button = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
    submit_button.click()


if __name__ == "__main__":
    pytest.main(["test_index2.py", "-s", "--html=report.html", "--self-contained-html"])
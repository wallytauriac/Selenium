import pytest
import os
import time
from Selenium.validate_IFI2 import InputFieldInspector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

XP = {
    "marital_status": "//select[@name='stats']",
    "f_gender": "//input[@name='gender' and @value='f']",
    "m_gender": "//input[@name='gender' and @value='m']",
    "first_name": "//input[@id='fname']",
    "last_name": "//input[@id='lname']",
    "nl_checkbox": "//input[@name='newsletter']"
}

def index_html():
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    fpath = "file://" + html_file_path
    return fpath

def print_results(attributes):
    for x in attributes.items():
        print(x)


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_marital_status(driver):
    # Load the local HTML file
    driver.get(index_html())

    # Select Marital status
    marital_status = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, XP["marital_status"])))
    marital_status_select = Select(marital_status)
    marital_status_select.select_by_value("married")
    time.sleep(2)

    input_field_inspector = InputFieldInspector(marital_status)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)

def test_radio_button(driver):
    # Load the local HTML file
    driver.get(index_html())

    # Select radio button
    gender_female = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, XP["f_gender"])))
    gender_female.click()
    time.sleep(2)
    input_field_inspector = InputFieldInspector(gender_female)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)

def test_radio_button2(driver):
    # Load the local HTML file
    driver.get(index_html())

    # Select radio button
    gender_male = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, XP["m_gender"])))
    gender_male.click()
    time.sleep(2)
    input_field_inspector = InputFieldInspector(gender_male)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)


def test_first_name(driver):
    # Load the local HTML file
    driver.get(index_html())

    # Fill first name
    first_name_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, XP["first_name"])))
    first_name_input.clear()
    time.sleep(1)
    first_name_input.send_keys("John")
    time.sleep(2)
    input_field_inspector = InputFieldInspector(first_name_input)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)


def test_last_name(driver):
    # Load the local HTML file
    driver.get(index_html())
    # Fill last name
    last_name_input = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, XP["last_name"])))
    last_name_input.clear()
    last_name_input.send_keys("Doe")
    time.sleep(2)
    input_field_inspector = InputFieldInspector(last_name_input)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)


def test_nl_checkbox(driver):
    # Load the local HTML file
    driver.get(index_html())
    # Check the newsletter checkbox
    newsletter_checkbox = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, XP["nl_checkbox"])))
    newsletter_checkbox.click()
    time.sleep(2)
    input_field_inspector = InputFieldInspector(newsletter_checkbox)
    attributes = input_field_inspector.inspect_attributes("static/expected_values.json")
    print_results(attributes)


if __name__ == "__main__":
    pytest.main(["validate_index.py::test_nl_checkbox", "-s"])
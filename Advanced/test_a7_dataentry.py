import pytest
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
    driver.get("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    time.sleep(1)

    # Select Marital status
    marital_status = Select(driver.find_element(By.XPATH, "//select[@name='stats']"))
    marital_status.select_by_value("married")
    ms_text = marital_status.first_selected_option.text

    # Select radio button
    gender_female = driver.find_element(By.XPATH, "//input[@name='gender' and @value='f']")
    gender_female.click()
    gf_status = gender_female.is_selected()
    time.sleep(1)

    # Fill first name and last name
    first_name_input = driver.find_element(By.XPATH, "//input[@id='fname']")
    first_name_input.clear()
    first_name_input.send_keys("John")
    fn_text = first_name_input.get_attribute("value")

    last_name_input = driver.find_element(By.XPATH, "//input[@id='lname']")
    last_name_input.clear()
    last_name_input.send_keys("Doe")
    ln_text = last_name_input.get_attribute("value")
    time.sleep(1)

    # Check the newsletter checkbox
    newsletter_checkbox = driver.find_element(By.XPATH, "//input[@name='newsletter']")
    newsletter_checkbox.click()
    nc_box = newsletter_checkbox.is_selected()

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    time.sleep(1)

# How to avoid Stale Element Exception error condition
    # Assertion examples
#    assert marital_status.select_by_value("married") == "Married"
    assert ms_text == "Married"
    assert gf_status == True
    assert fn_text == "John"
    assert ln_text == "Doe"
    assert nc_box == True


if __name__ == "__main__":
    pytest.main(["test_a7.py", "-s", "--html=report.html", "--self-contained-html"])
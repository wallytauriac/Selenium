from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import random
import string

# Function to generate random string
def random_string(length):
    # string.ascii_letters contains all uppercase and lowercase letters
    letters = string.ascii_letters
    # random.choice(letters) picks a random character from letters
    # The loop generates 'length' number of random characters and joins them together
    return ''.join(random.choice(letters) for i in range(length))

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the sample form
def get_page():
    # Load the local HTML file
    html_file_path = os.path.abspath("C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html")
    driver.get("file://" + html_file_path)
    time.sleep(3)

# Function to fill form with random data
def fill_form(n):
    # Enter random text in first name field
    name_field = driver.find_element(By.NAME, "fname")
    name_field.clear()
    name_field.send_keys(random_string(8))

    # Enter random text in last name field
    name_field = driver.find_element(By.NAME, "lname")
    name_field.clear()
    name_field.send_keys(random_string(12))

    # Enter random email address
    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys(random_string(6) + "@example.com")

    # Select a random option in dropdown
    dropdown = driver.find_element(By.NAME, "stats")
    options = dropdown.find_elements(By.TAG_NAME, "option")
    random_option = random.choice(options)
    random_option.click()
    time.sleep(3)

    # Enter random text in text area
    textarea = driver.find_element(By.NAME, "message")
    textarea.clear()
    textarea.send_keys("Member or Officer - " + random_string(4))

    # Request webpage screenshot
    take_screenshot(driver, "datagen/index" + str(n) + ".png")

    # Click on submit button
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submit")))
    submit_button.click()   # Will cause an error display indicating file cannot be accessed
    time.sleep(1)

# Record screencast
def take_screenshot(driver, name):
    os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))
# Here you can use any screen recording software to record the actions performed by the script

# Loop to demonstrate entering various combinations of data
for n in range(5):  # Perform 5 iterations
    get_page()
    fill_form(n)
    time.sleep(2)  # Wait for 2 seconds before filling the form again

# Close the browser
driver.quit()

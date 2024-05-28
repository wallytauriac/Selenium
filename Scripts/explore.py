from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import random
import string


# Function to generate random string
def random_string(length):
    # string.ascii_letters contains all uppercase and lowercase letters
    letters = string.ascii_letters
    # random.choice(letters) picks a random character from letters
    # The loop generates 'length' number of random characters and joins them together
    return ''.join(random.choice(letters) for i in range(length))

# Function to fill form with random data
def fill_form(driver):
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

def scrape_and_store_data(url, output_file, cnt):
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the webpage
        driver.get(url)
        time.sleep(5)

        fill_form(driver)

        # Get input data from the webpage
        input_data = {
            "field1": "'" + driver.find_element(By.ID, "fname").get_attribute("value") + "'",
            "field2": "'" + driver.find_element(By.ID, "lname").get_attribute("value") + "'",
            "field3": "'" + driver.find_element(By.ID, "email").get_attribute("value") + "'",
            "field4": "'" + driver.find_element(By.ID, "message").get_attribute("value") + "'",
            "field5": "'" + driver.find_element(By.XPATH, "//select[@name='stats']").get_attribute("value") + "'",
            # Add more fields as needed
        }

        # Write data to CSV file
        if cnt == 1:
            with open(output_file, 'w', newline='') as csvfile:
                fieldnames = input_data.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(input_data)
                print("Data successfully scraped and stored in new file:", output_file)

        else:
            with open(output_file, 'a', newline='') as csvfile:
                fieldnames = input_data.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(input_data)
                print("Data successfully scraped and stored in file:", output_file)


    finally:
        # Close the WebDriver
        driver.quit()

# Example usage:
if __name__ == "__main__":
    # URL of the webpage to scrape data from
    url = "file://" + "C:/Users/wally/Documents/Python/Demo/Selenium/Templates/index.html"

    # Initialize record counter
    cnt = 1

    # Output CSV file to store scraped data
    output_file = "scraped_data.csv"

    # Scrape data and store it in the CSV file
    for records in range(5):
        scrape_and_store_data(url, output_file, cnt)
        cnt += 1
        time.sleep(1)

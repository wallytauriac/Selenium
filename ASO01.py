import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
This module was developed to explore elements in an HTML file
It processes elements by locator strategy.
There is one function per locator strategy with one exception.
'''
# This function is designed to process a list array of elements
def print_elements(type, element):
    print("Elements for " + type + " found: ")
    for e in element:
        print("Get Text found: " + e.text)
        print("Accessible name found: " + e.accessible_name)
        print("Aria role found: " + e.aria_role)
        print("Tag Name found: " + e.tag_name)

# This function is designed to process a single special element
# Elements that have an aria role of Link
# Elements that do not have a value in element.text
# Elements that have a property of "value"
def print_list(t, element):
    print(t + " List")
    if element.aria_role == "link":
        print("Get Text for " + t + " found: " + element.get_property("text"))
    else:
        print("Get Property Value for " + t + " found: " + element.get_property("value"))

    print("Accessible name for " + t + " found: " + element.accessible_name)
    print("Aria role for " + t + " found: " + element.aria_role)
    print("Tag name for " + t + " found: " + element.tag_name)

# This function processes tag name elements that have text data
def get_tag_name():
    # # Get all the elements available with tag name
    # # Use this for HTML tags that have text values enclosed in > <
    type = ["h2", "a", "input"]
    for t in type:
        element = driver.find_elements(By.TAG_NAME, t)
        print_elements(t, element)

# This function processes ID names
def get_id():
    # Get all the elements available with ID attributes
    # Use this for HTML tags that have ID= elements
    type = ["fname", "lname"]
    for t in type:
        element = driver.find_element(By.ID, t)
        print_list(t, element)

# This function processes element NAME attributes
def get_name():
    # Get all the elements available with NAME
    # Use this for HTML tags that have NAME= elements
    type = ["fname", "lname", "newsletter"]
    for t in type:
        element = driver.find_element(By.NAME, t)
        print_list(t, element)

# This function processes single elements with CLASS name attributes
def get_class_name():
    # Get all the elements available with CLASS NAME
    # Use this for HTML tags that have CLASS= elements
    type = ["information"]
    for t in type:
        element = driver.find_element(By.CLASS_NAME, t)
        print_list(t, element)

# This function processes multiple elements with class name
def get_class_names():
    # Get all the elements available with CLASS NAME
    # Use this for HTML tags that have CLASS= elements
    type = ["information"]
    for t in type:
        element = driver.find_elements(By.CLASS_NAME, t)
        if len(element) > 0:
            for e in element:
                print_list("Information", e)

# This function performs XPath element detection
def get_xpath():
    element = driver.find_element(By.XPATH, "//input[@type='submit']")
    print_list("Link Element", element)
    element = driver.find_element(By.XPATH, "//form/input[4]")
    print_list("Link Element", element)

# This function performs Link text element detection
def get_link_text():
    element = driver.find_element(By.LINK_TEXT, 'Selenium Official Page')
    print_list("Full Link Text Element", element)
    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Selenium Off')
    print_list("Partial Link Text Element", element)

# This function performs CSS Selector element detection
def get_css_selector():
    element = driver.find_element(By.CSS_SELECTOR, "#fname")
    print_list("CSS Selector Element", element)


# Store start time
t = time.time()

# This is the beginning of code execution
# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other WebDriver (e.g., Firefox, Safari) here
# Load the local HTML file
html_file_path = os.path.abspath("Templates/index.html")
driver.get("file://" + html_file_path)
print("HTML File path: ", html_file_path)
# The RC value controls what test is performed
# RC 1, 6 and 7 causes multiple elements to be located for testing
time.sleep(3)
rc = 2
# Find elements and display *****************************
if rc == 1:
    get_tag_name()  # Test Element by TAG_NAME
elif rc == 2:
    get_id()  # Test Element by ID
elif rc == 3:
    get_name()  # Test Element by NAME
elif rc == 4:
    get_class_name()  # Test Element by CLASS NAME
elif rc == 5:
    get_class_names()  # Test Element by CLASS NAME Entries
elif rc == 6:
    get_xpath()  # Test Element by XPATH
elif rc == 7:
    get_link_text()  # Test Element by LINK TEXT
elif rc == 8:
    get_css_selector()  # Test Element by CSS SELECTOR


# Teardown - close the browser window
driver.quit()
# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")


if __name__ == "__main__":
    print("Bye")
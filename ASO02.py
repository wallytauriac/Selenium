import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
This module was developed to explore elements in an HTML file
It processes elements by locator strategy. But it uses two functions for locator strategy.

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
    elif element.text != "":
        print("Get Text found: " + element.text)
    else:
        print("Get Property Value for " + t + " found: " + element.get_property("value"))

    print("Accessible name for " + t + " found: " + element.accessible_name)
    print("Aria role for " + t + " found: " + element.aria_role)
    print("Tag name for " + t + " found: " + element.tag_name)

# This function creates a dictionary array of locator strategy keys
# The function returns the appropriate By value
def get_strategy(locator_strategy):
    locators = {"id": By.ID, "name": By.NAME, "tag name": By.TAG_NAME,
                "class name": By.CLASS_NAME,
                "link text": By.LINK_TEXT,
                "partial link text": By.PARTIAL_LINK_TEXT,
                "css selector": By.CSS_SELECTOR,
                "xpath": By.XPATH
                }
    return locators.get(locator_strategy)

# This function used the find_elements method to locate one or more page elements
def get_elements(locator_strategy, value):
    # # Get all the elements available
    # # Use this for HTML tags that have text values enclosed in > <
    element = driver.find_elements(get_strategy(locator_strategy), value)
    if len(element) > 0:
        for e in element:
            print_list(value, e)
    else:
        print_elements(value, element)

# This function uses the find_element method to locate a single page element
def get_element(locator_strategy, value):
    # # Get all the elements available
    # # Use this for HTML tags that have text values enclosed in > <
    element = driver.find_element(get_strategy(locator_strategy), value)
    print_list(value, element)


# Store start time
t = time.time()

# The code from this point is not in a function. This is where code execution begins.
# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other WebDriver (e.g., Firefox, Edge, Safari) here

# Load the local HTML file instead of a URL
html_file_path = os.path.abspath("Templates/index.html")
driver.get("file://" + html_file_path)
print("HTML File path: ", html_file_path)
time.sleep(2)
# The RC value controls what test is performed
# RC 1, 6 and 7 causes multiple elements to be located for testing
rc = 2
# Find elements and display *****************************
if rc == 1:  # Test Elements
    get_element("tag name", "h2")  # Test Element by tag
    get_element("tag name", "a")  # Test Element by tag
    get_elements("tag name", "input")  # Test Elements by tag
elif rc == 2:
    get_element("id", "fname")  # Test Element by ID
    get_element("id", "lname")  # Test Element by ID
elif rc == 3:
    get_element("name", "fname")  # Test Element by NAME
    get_element("name", "lname")  # Test Element by NAME
    get_element("name", "newsletter")  # Test Element by NAME
elif rc == 4:
    get_element("class name", "information")  # Test Element by CLASS NAME
elif rc == 5:
    get_elements("class name", "information")  # Test Element by CLASS NAME Multiple Entries
elif rc == 6:
    get_element("xpath", "//input[@type='submit']")  # Test Element by XPATH
    get_element("xpath", "//form/input[4]")  # Test Element by XPATH
elif rc == 7:
    get_element("link text", "Selenium Official Page")  # Test Element by LINK TEXT
    get_element("partial link text", "Selenium Off")  # Test Element by LINK TEXT
elif rc == 8:
    get_element("css selector", "#fname")  # Test Element by CSS SELECTOR

# Store end time
e = time.time()
print("Execution time: ", round(e-t, 2), " seconds!")


if __name__ == "__main__":
    print("Bye")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage -- Using one of the Internet Herokuapp webpages

'''
Test = 1 --> XPATH Test for absolute and relative path approaches
Test = 2 --> XPATH Test for XPATH functions
Test = 3 --> XPATH Test for XPATH Axes
Test = 4 --> XPATH Test for XPATH Conditions
Test = 5 --> XPATH Test for XPATH Wildcard

'''


def xpath_1():
    print("XPATH Test Case 1: Absolute/Relative XPATH Approaches")

    # Absolute XPath example
    element1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    print("--> Absolute path test completed.")
    # Relative XPath example
    element2 = driver.find_elements(By.XPATH, "//a[starts-with(@id,'4a05')]")  # Pickup multiple elements
    element2a = driver.find_element(By.XPATH, "//a[@class='button']")
    print("--> Relative path test completed.")
    return "OK"

def xpath_2():
    print("XPATH Test Case 2: XPATH Contains and Text functions")
    # Using functions example
    element3 = driver.find_element(By.XPATH, "//a[contains(., 'bar')]")
    print("--> Contains with text function test completed.")
    element4 = driver.find_element(By.XPATH, "//h3[text()='Challenging DOM']")
    print("--> Text find function test completed.")
    return "OK"

def xpath_3():
    print("XPATH Test Case 3: XPATH Axe functions")

    # Using axes example
    element4 = driver.find_element(By.XPATH, "//tbody/tr/child::td[1]")
    print("--> XPATH Axe test completed for first cell in table.")
    element4a = driver.find_element(By.XPATH, "//tbody/tr/child::td[1]/following-sibling::td")
    print("--> XPATH Axe test completed for second cell in table.")
    return "OK"

def xpath_4():
    print("XPATH Test Case 4: XPATH Combining Conditions")
    # Combining conditions example
    element5 = driver.find_element(By.XPATH, "//input[@type='text' and @name='username']")
    print("--> XPATH Condition completed for User name entry box.")

    element5a = driver.find_element(By.XPATH, "//button[@class='radius' and @type='submit']")
    print("--> XPATH Condition completed for Submit button.")

    return "OK"

def xpath_5():
    print("XPATH Test Case 5: XPATH Wildcard Processing")
    # Wildcard example
    element6 = driver.find_element(By.XPATH, "//*[text()='The Internet']")
    print("--> XPATH Wildcard process completed for the Title element.")

    element6a = driver.find_element(By.XPATH, "//*[text()='Challenging DOM']")
    print("--> XPATH Wildcard process completed for visible title text element.")

    return "OK"

x = "NOK"
test = 5

if test == 4:
    driver.get("https://the-internet.herokuapp.com/login")
else:
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

function_name = f"xpath_{test}"
func = getattr(sys.modules[__name__], function_name)
x = func()  # Call the function

if x == "OK":
    print("All Tests completed successfully.")


# Close the driver
driver.quit()


if __name__ == "__main__":
    print("\nMain module completed")
# Python program to implement Locating by a tag name
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# Replace this with your actual url
url = "https://www.selenium.dev/about/"
driver.get(url)
time.sleep(3)
# Specify an HTML tag name to locate text between <h1> </h1>
try:
    # Find single element based on locator strategy
    element = driver.find_element(By.TAG_NAME, "h1")
    assert element.text == "About Selenium"
except NoSuchElementException:
    print("Not Found")
else:
    print("Found")
finally:
    print("Element text: " + element.text)

driver.quit()

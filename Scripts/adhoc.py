from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open a website
driver.get("https://selenium-python.readthedocs.io/ ")
print("Page 1 Title: ", driver.title)
assert "Selenium with Python — Selenium Python Bindings 2 documentation" in driver.title

# Interact with UI elements
search_box = driver.find_element (By.NAME, "q")  # assuming there is a search box with name "q"
search_box.clear()  # clear any existing text in the search box
search_box.send_keys("Python Selenium")  # type in the search query
search_box.send_keys(Keys.RETURN)  # hit Enter

# Wait for the page to load
time.sleep(5)  # You should use explicit waits instead of time.sleep()
print("Page 2 Title: ", driver.title)
# Click on a link
search_results = driver.find_elements(By.CSS_SELECTOR, "h3.r a")  # assuming search results are represented by <h3> tags with class "r"
if search_results:
    search_results[0].click()  # Click on the first search result

# Wait for the page to load
time.sleep(5)

# Perform some assertions or further interactions
# For example, you could verify if a specific element exists on the page
print("Page 3 Title: ", driver.title)
assert "Selenium Python Bindings 2" in driver.title

# Close the browser
driver.quit()

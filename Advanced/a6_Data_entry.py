from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(15)

# Find an element using XPath
try:
    element = driver.find_element(By.CSS_SELECTOR, "#username")
    time.sleep(1)
except Exception as err:
    print("Username element not detected.")
    exit(1)

# Perform actions on the element
element.send_keys("tomsmith")
time.sleep(1)
print("Username value populated.")
time.sleep(1)
# Confirm value entered
element = driver.find_element(By.CSS_SELECTOR, "#username").get_attribute("value")
print("Username value entered: ", element)

# Continue with further automation...
driver.quit()

if __name__ == "__main__":
    print("\nMain module completed")



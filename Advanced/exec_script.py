from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Optional approach to add options to the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to website
driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

# Locate element to scroll to
element = driver.find_element(By.XPATH, "//a[normalize-space()='WYSIWYG Editor']")
time.sleep(1)
# Execute JavaScript to scroll to element
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(1)
print("\nWindow scrolled to WYSIWYG Editor link text")

# Navigate to website
driver.get("https://example.com")
time.sleep(1)
# Execute custom JavaScript function
title = driver.execute_script("return document.title;")
time.sleep(1)
print("\nPage title: ", title)

# Close the driver
driver.quit()


if __name__ == "__main__":
    print("\nMain module completed")